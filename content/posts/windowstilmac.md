+++
title = "Frå Windows til Mac"
date = 2026-10-26
draft = false
wordCount = true
readingTime = true
+++
Av ulike grunnar måtte eg få ny PC på jobb. Og då kom ein god kollega med den gode ideen at eg skulle få ein MacBook Pro, og bruke den mellom anna for å køyre store språkmodellar lokalt. Det er mykje data i Canvas som er gult (ikkje med vilje, men av di studentar skriv litt mykje om seg sjølv innimellom), og til tider svakt raudt, så det kan vere greitt å ikkje spre slikt for alle vindar. Og det er også greitt å bygge opp kompetansen på å jobbe mot språkmodellane.

## Førebuing
Etter eit godt hint friska eg opp abonnementet på Medium, og der er det mange gode artiklar skrevet *av* amatørar *til* amatørar. Så eg leste meg oopp på alt eg kunne om Mac.

## Overgang
**Det første** eg måtte setje meg inn i var tastaturet. Å gå frå `Ctrl` og `Alt` til `Option` og `Command` var mykje enklare enn eg hadde trudd, mykje grunna at eg hadde [eit tastatur](https://www.logitech.com/en-us/shop/p/mx-keys-mini.920-010388) som er lagd for å skifte mellom dei. Så etter to veker har det aller, aller meste satt seg i fingrane.

**Det andre** var oppsett av programvare. Her er jo det aller meste likt (i alle fall Office-programma), og ein del kan eg skaffe via Firmaportalen (HVL si kurerte liste over programvare vi skal få lov til å installere). Men den *store* fordelen er at eg kan installere det aller, aller meste berre på min brukar, og denne brukaren er mykje meir isolert frå resten av maskina enn under Windows. Det er to måtar eg bruker mest:

1. `homebrew` - terminalbasert styring av pakker. 
2. Laste ned filer - med unntak av [Karabiner-Elements](https://karabiner-elements.pqrs.org) laster eg ned ei `.dmg`-fil, opner den, og sletter den etterpå. 

**Det tredje**, som eg var mest spent på, var [Emacs](https://www.gnu.org/software/emacs/). Først installerte eg via `brew install emacs`, men då fekk eg "berre" terminalbasert versjon. Den fungerte fint, men eg ville også prøve ut grafikkbasert. Under Windows fekk eg aldri til å vise grafikk inne i Emacs (til dømes PDF-ar av førelesingsnotat), men hadde eit håp om at dette skulle gå betre under Mac. Så eg fant [Emacs for Mac OS X](https://emacsformacosx.com/), og etter ein del slåssing med symbolske lenker for å få snarvegen "`Command+Space emacs`" til å peike til rett plass fungerte det heilt fint.

## Konklusjon (førebels)
Mac er, trass alle mine fordommer, *veldig* mykje betre å jobbe på enn Windows. Det lett paradoksale (for meg) var at sjølv om eg trudde at alt var grafikkbasert ("klikk eit bilete og dra det til eit anna, så skjer akkurat det som skal skje") så arbeider eg mykje meir i terminalvindauge (ja, fleirtal) enn under Windows. 
