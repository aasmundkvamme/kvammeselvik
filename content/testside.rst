Testside
###########

:date: 2026-05-07
:author: Aasmund Kvamme
:slug: testside
:status: published

Dette er første avsnitt. Det inneheld *kursiv* og **feit** tekst. Det inneheld også ei lenke til `ein artikkel om Lotto <{filename}a-vinne-i-lotto.md>`_. Vi har to måtar å lage fotnotar på; den første [#]_ har flest "gode" eigenskaper; den andre[ref]Som kjem via ein tilleggsmodul.[/ref] ser litt penare ut, men har mindre funksjonar for formattering.

Eg skal legge ut eit stort verk; Rytters omsetjing av *Beowulf*:

Grendel-Ota
~~~~~~~~~~~

| Beowulf Scylding var då på borga,
| ljuve lyddrotten, langan tid,
| **55** kjend av alt folket. (Faren var kvorven
| herifrå or heimen). Han og fekk son:
| Healfdene [#]_  høge. Herrevald han gjævt,
| aldrug og otefus [#]_, øvde hjå Scyldingom.


Kode
~~~~~~~~~~~~

Her kjem litt kode:

.. code-block:: python

   def hello_world():
       print("Hello, world!")

Matematikk
~~~~~~~~~~~~

Her kjem litt matematikk: 

.. math::

   E = mc^2

   \int_a^b f(x) dx


.. rubric:: Fotnoter

.. [#] Denne er *innebygd* i reStructuredText.
.. [#] **Healfdene** med tilnamnet «den høge». Namnet tyder «halvdene». Han er og kjend i nordiske kjeldeskrifter og heiter der Halfdanr (latinisera Haldanus). Han har tri søner: Heorogar (gn. Hjrgeirr), Hrodgar (gn. Hroarr, Roe) og Halga (gn. Helge).
.. [#] **«otefus»** av *ote* = strid og *fus* = huga (på eitkvart).
