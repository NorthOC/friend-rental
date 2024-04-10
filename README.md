# Anti Vienas - Draugų platforma

Mano bandymas nerti į verslą, kuriant [rental friend platformą](https://www.afar.com/magazine/the-incredibly-true-story-of-renting-a-friend-in-tokyo) Lietuvoje. Kadangi nepažįstu nei vieno verslininko savo gyvenime, atliksiu dokumentavimą, kad tokie kaip aš esu dabar, turėtų į ką atsižvelgti kuriant verslą ateityje.

## Kodėl būtent rental friend?

Dabar yra 2024 m. Balandžio 9 d. 

Nuėjus į reddit svetainės /r/lithuania ir /r/lietuva forumus galime rasti daug postų apie tai kaip žmonės neturi draugų, antrų pusių ir yra izoliuoti nuo visų socializavimosi ritualų dėl karjeros, psichologinės būklės ar kitų aplinkybių.

Taigi, pradžiai parašiau knygą [Meilės Žaidimas](https://www.meileszaidimas.lt/) kadangi norėjau padėti vyrams su santykiais. Po kažkiek laiko reklamuojant ir pardavinėjant, pastebėjau, kad su tuo yra dvi problemos: 

1) Nedaug vyrų mėgsta ieškoti atsakymų knygose savo problemoms
2) Parašyta ne moterims, nors moterys perka už vyrus 4 kartus dažniau ir daugiau.
3) Sunku reklamuoti sprendimą, kuris yra bent N-16.

Taigi, manau laikas palikti knygą pasyvioje lentynoje, ir pereiti prie šio projekto. A/V draugų platformą galėsiu daug lengviau reklamuoti, bei žmonės iš to galės užsidirbti (finansinė paskata). Ar tai gera idėja? Negali žinoti, nes Lietuvoje to kaip ir nėra.

Jeigu trumpai, man patinka spręsti vienatvės problemas žmonių, taigi manau, kad galėsiu prie šio projekto dirbti long-term ir nepasiduoti, jeigu kažkas bus ne taip.

## Dizainas

Padariau su Figma. Nieko įspudingo - pirmas puslapis rodo galimus draugus, gali peržiūrėti profilius, ir yra užsakymų valdymo skydas. Dar reikės padaryti piniginės valdymo skydą:

![Pagrindinis puslapis](/readme_assets/1.png)

![Profilis](/readme_assets/2.png)

![Užsakymų valdymo skydas](/readme_assets/3.png)

Matosi vientisa tema. Logotipas padarytas su Photopea (aka. nemokamas photoshop) bet dar daug kas gali keistis. Dalis elementų nepadaryta nu nes padarysiu pagal tai, kaip kiti elementai jau atrodo.

## Web Stekas

Django + DRF + PostgreSQL + JS (galbūt bus dar ir HTMX)

Jei reiks, įdėsiu caching su Redis.

Hostinsiu viską serveryje arba VPS. Jokių Amazon ar Azure. Tai sprendimas sojos vartotojams.

Payment procesoriaus dar nežinau. Pasirinkimas yra tarp Stripe, Paysera ir Montonio. Tas kuris turės geriausias sąlygas mano verslo tipui.

Žodžiu, bandau sau neapsisunkint per daug ir fokusuojuosi į server-side rendering.

## Funkcionalumų milestone

MVP:
* Registracija
* Prisijungimas (jwt-auth)
* READ ir UPDATE profiliai
* Tapimas draugu
* Užsakymų CRUD
* Review CRUD
* Pinigų įdėjimas
* Pinigų išsiėmimas
* ID verifikacija
* Svetainės admin kontaktavimo forma.

Extras:
* Report vartotojas funkcija
* Svetainės Analitika
* Registracijos aktivavymas per email

## Duomenų bazės projektavimas

Padariau duomenų bazės planą, kad būtų lengviau suprogramuoti su Django ORM.

![pirmoji versija, tikrai bus daugiau](/readme_assets/5.png)

## Programavimas

Pirmiausia suprogramavau User modelį. Nusprendžiau, sujungti User ir Profile, nes mažiau DB bus calls. (žiūrėti `antivienas/database/models.py`)

box_color modelis taip pat išnyko. Tapo pasirinkimų laukeliu. Vėlgi - mažiau DB calls.

Atsirado nauji du modeliai, nes pagalvojau, kad durna, jog netrackinu payments. Taigi, payment_history ir withdrawal_request modeliai dar bus included.

Taip pat pasidomėjau daugiau apie svetainių architektūrą. Tai manau apsieisim ir be Svelte. Didžioji dalis svetainės bus server-side rendered, ir, tik kai kurie komponentai bus padaryti su Django REST framework (pavyzdžiui, profile EDIT funkcija).

Laukite tesinio.