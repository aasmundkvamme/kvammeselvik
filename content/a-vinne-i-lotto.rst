Å vinne i Lotto
###############
:date: 2021-02-10 21:53
:author: Aasmund
:category: HVL, Statistikk, Undervising
:tags: lotto, sannsynlighet
:slug: a-vinne-i-lotto
:status: published

Bakgrunn
--------

Eg tippar Lotto fast kvar veke, og vinn av og til. I 2020 vant eg faktisk 13 av 52 veker, og synest dette var svært ofte. Ikkje store gevinstar; stort sett 50 kroner, så det var eit tapsprosjekt. Men eg vart interessert, og reknar her ut sannsynligheten for at eg skal vinne 13 veker (eller fleire) i løpet av eit år.

Premissane er altså: eg tippar ti ulike rekker kvar veke, 52 veker i året. På kvar rekke kan eg vinne ein av fem ulike gevinstar: 7 rette, 6 rette og tilleggstal, 6 rette, 5 rette eller 4 rette.

Sidan dette er ein del av undervisinga i emnet "Statistikk og landmåling" ved Høgskulen på Vestlandet, så er alle utrekningar gjort i programmet MATLAB. Men om du vil kontrollere kjem formlane på slutten.

Vinne på ei rekke
-----------------

Eg reknar først ut sannsynligheten for å vinne ein eller annan gevinst på ei rekke. Dette gjer eg ved ein heimesnekra MATLAB-funksjon ``plotto(h, t)`` der ``h`` er antal rette eg får blant "hovedtala" og ``t`` er antal rette eg får blant tilleggstala.

``prekke = plotto(4,0)+plotto(5,0)+plotto(6,0)+plotto(6,1)+plotto(7,0)``

Dette gir at $latex P(\\text{ein elller annan gevinst på ei rekke}) = 0,01822$

Vinne minst ein gevinst på ti rekker
------------------------------------

Så ser eg på sannsynligheten for å vinne på minst ei av dei ti rekkene kvar veke. Dette er eit *binomisk* forsøk, med $latex n=10$ og $latex p = 0,01822$ (altså variabelen ``prekke``). La $latex X$ vere antal gevinstar på 10 rekker; eg skal då rekne ut $latex P(X\\geq1)=1-P(X=0)$:

``pveke = 1-binopdf(0,10,prekke)``

Som gir $latex P(\\text{minst ein gevinst ei veke})= 0,16796$

Vinne minst 13 gevinstar på 52 veker
------------------------------------

Så det store spørsmålet: kva er sannsynligheten for å vinne i 13 eller fleire av dei 52 vekene? Dette er også eit binomisk forsøk, med $latex n=52$ og $latex p=0,16796$ (altså variabelen ``pveke``). Eg skal rekne ut $latex P(X\\geq13)=1-P(X\\leq12)$:

``paar = 1-binocdf(12,52,pveke)``

som gir $latex P(\\text{vinne 13 eller fleire ganger på eit år})= 0,085775$

Det er altså 8,5 % sannsynlighet for at eg skal vinne så mange ganger (eller fleire) i løpet av eit år. Er det stor eller liten sannsynlighet? Det er ganske nær $latex 1/12$, så om du er i eit rom med 11 andre så kan du forvente at ein av dykk har vunnet så ofte. Døm sjølv!

Matematikken
------------

Eg bruker standardformlar frå sannsynlighetsrekning og kombinatorikk. Den viktigaste byggesteinen er *binomialkoeffisienten*

$latex \\displaystyle {{n}\\choose{k}} = \\frac{n!}{x!(n-x)!}$, der $latex n! = n\\cdot(n-1)\\cdot(n-2)\\cdots 3\\cdot 2\\cdot 1$

Til dømes er $latex \\displaystyle 4! = 4\\cdot3\\cdot2\\cdot1=24$.

Binomialkoeffisienten kan eg bruke til å rekne ut kor mange ulike måtar eg kan velje $latex k$ tal frå $latex n$ på. Til dømes vert då antalet Lotto-rekker

$latex \\displaystyle {{34}\\choose{7}} = \\frac{34!}{7!(27)!} = 5\\,379\\,616$.

Så er det den heimesnekra MATLAB-funksjonen ``plotto(h, t)``. Den er bygd opp som ein *hypergeometrisk* sannsynlighet, der eg ser på antal "gunstige" kombinasjonar av *hovedtal* (``h``) og *tilleggstal* (``t``) eg har tippa:

$latex P\_{\\text{lotto}}(h, t) = \\displaystyle\\frac{{{7}\\choose{h}}\\cdot{{1}\\choose{t}}\\cdot{{26}\\choose{7-(h+t)}}}{{34}\\choose{7}}$

Til slutt har eg nytta formelen for *punktsannsynlighet* i binomisk fordeling (med parametre $latex n$ og $latex p$):

$latex P(X=x) = {{n}\\choose{x}}p^x(1-p)^{n-x}$

og formelen for *kumulativ sannsynlighet*:

$latex P(X\\leq x) = \\sum\_{k=0}^{x} {{n}\\choose{x}}p^k(1-p)^{n-k}$

Men som sagt: alt dette ligg innebygd i kommandoane ``binopdf(x, n, p)`` og ``binocdf(x, n, p)`` i MATLAB, og studentane skal sleppe å rekne ut alt dette for hand.
