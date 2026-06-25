:date: 2026-06-23
:author: Aasmund Kvamme

.. contents::

1 Henting av data via REST API
------------------------------

1.1 Autorisasjon
~~~~~~~~~~~~~~~~

Først må eg skaffe meg eit ``access_token`` som varer i ein time (og så får eg litt kvittering som strengt tatt ikkje er nødvendig):

(Alle variable som starter på "DAP\_" er lokale eg henter via ``os.environ['DAP_']``)

.. code:: python

    token_url = f"{DAP_BASE_URL}/ids/auth/login"
    basic_auth_header = base64.b64encode(
        f"{DAP_CLIENT_ID}:{DAP_CLIENT_SECRET}".encode()
    ).decode()
    headers = {
        "Authorization": f"Basic {basic_auth_header}",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    payload = {
        "grant_type": "client_credentials"
    }
    response = requests.post(token_url, data=payload, headers=headers)
    if response.status_code == 200:
        token_data = response.json()
        access_token = token_data["access_token"]
        expires_in   = token_data.get("expires_in")   # seconds until expiry (optional)
        print("Token retrieved")
        print(f"Access token: {access_token}")
        print(f"Expires in: {expires_in} seconds")
    else:
        # Something went wrong – print the status and any error payload
        print(f"Failed ({response.status_code})", end="")
        try:
            print(f" JSON: {response.json()}")
        except ValueError:
           print(f" ValueError: {response.text}")

1.2 Bruke tokenet
~~~~~~~~~~~~~~~~~

Dette er ein todelt prosess:

1. Start ein jobb

2. Hent resultatet (ei eller fleire filar som må bli pakka ut)

1.2.1 1. Start jobb
^^^^^^^^^^^^^^^^^^^

For å få eit snapshot set vi ``incremental = False`` (og omvent: ``True`` for incremental).
Send ein POST med ``since`` (for incremental):

.. code:: python

    status = ''
    forseinking = 5
    incremental = False
    if incremental:
      timar = 4
      temp = datetime.now(timezone.utc) - timedelta(hours=timar)
      dt = datetime.fromisoformat(str(temp))
      last_seen = dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
      data=json.dumps({
        "format": "jsonl",
        "since": str(last_seen),
        # "until": "2026-02-06T00:30:00Z"
        })
    else:
      data=json.dumps({
        "format": "jsonl",
        # "since": str(last_seen),
        # "until": "2026-02-06T00:30:00Z"
        })
    while status != 'complete':
      respons = requests.post(
        f"{DAP_BASE_URL}/dap/query/canvas/table/enrollment_terms/data",
        headers={
          "Authorization": f"Bearer {access_token}", 
          "Content-Type":"application/json",
          },
        data=data,
        )
      jobb = respons.json()
      print(jobb)
      status = jobb['status']
      time.sleep(forseinking)

1.2.2 2. Hent resultatet
^^^^^^^^^^^^^^^^^^^^^^^^

Dette er den tricky delen. Eg må ta lista med filer og endre alle \`'\` til \`"\`, og så sende denne som ``payload`` i ein POST:

.. code:: python

    filar = jobb['objects']
    payload = f"{filar}".replace('\'', '\"')
    print(payload)
    headers = {
        'x-instauth': f"{access_token}", 
        'Content-Type': 'text/plain'
    }
    respons = requests.post(f"{DAP_BASE_URL}/dap/object/url", headers=headers, data=payload)
    r = respons.json()

    n = 1
    for fil in filar:
      url = r['urls'][filar[0]['id']]['url']
      data = requests.request("GET", url)
      utfil = f"dap_data_{n}"
      n += 1
      open(f'{utfil}.gz', 'wb').write(data.content)
      with gzip.open(f'{utfil}.gz', 'rb') as f_in:
          with open(f'{utfil}.txt', 'wb') as f_out:
              shutil.copyfileobj(f_in, f_out)
      os.remove(f"{utfil}.gz")

No har eg ei eller fleire filar med data i JSON-format. Eg kan lese desse inn i ei dataramme og bearbeide dei:

.. code:: python

    liste = []
    for fil in glob.glob('dap_data_*'):
        df = pd.read_json(fil, lines=True)
        df = pd.concat([
            pd.json_normalize(df['key']).add_prefix('key_'),
            pd.json_normalize(df['value']).add_prefix('value_'),
        ], axis=1)
        liste.append(df)
    dataliste = pd.concat(df for df in liste)
