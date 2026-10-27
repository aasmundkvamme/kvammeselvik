+++
title = "Hello World"
date = 2026-10-26
draft = false
+++

My first Hugo blog post.
Det ser bra ut hittil.

Men datoen vert ikkje rett? Det har med kvar parametrane vert plassert i `.toml`-fila.

Her er litt kode, og det ser jo fint ut:
{{< highlight python "linenos=table" >}}
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
{{< /highlight >}}
Kodeblokken får ikonet "kopier meg!" når du peiker på det.
Klarer den matematikk også? \(\sqrt{x^2+3}\) er inne i teksten, medan $$\int_{x=0}^{x=\pi}e^{x^2-3}dx$$ er mellom to linjer med tekst.

