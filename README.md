#### Planisphere generator with the option of Lithuanian language

This repository contains Python scripts that can be used to produce a cardboard cut-and-glue kit to make your own model planisphere in Lithuanianan language (as well as English and Spanish).

### Sukamasis žvaigždėlapis (planisfera) lietuvių kalba V.2

### Skirtumai nuo V.1:

Skirtumai nuo "Sukamasis žvaigždėlapis (planisfera) lietuvių kalba V.1": Kad pagreitinti planisferų generavimą paliktos tik trys kalbos (anglų, lietuvių ir ispanų); Platumos, kurioms generuojamos planisferos, intervalas yra nuo 52°N pietuose iki 56°N šiaurėje; Planisferos generuojamos kas 1°, o ne 5°.

#### Pasigaminkite kartoninį sukamojo žvaigždėlapio (planisferos) modelį V.2

Čia pateikiami Python skriptai, kuriuos galima naudoti norint pasigaminti kartoninį sukamojo žvaigždėlapio arba planisferos modelį lietuvių kalba (+ anglų ir ispanų), skirtą bet Lietuvos platumoms (nuo 52°N iki 56°N). Lietuvos ribinės geografinės platumos: Šiaurėje – 56°27'N (į šiaurės vakarus nuo Aspariškių kaimo, Biržų raj.); Pietuose – 53°54'N (į pietryčius nuo Kabelių ir į pietus nuo Musteikos kaimų, Varėnos raj.). Platumos skirtumas iki 5° nėra reikšmingas šios planisferos veikimui. 
Kartoninei planisferai nereikia baterijos ir interneto ryšio, tačiau naudojant planisferą naktį labai pravečia raudonos šviesos žibintuvėlis.

#### Įvadas

Planisfera - tai paprastas sukamasis žvaigždėlapis, kuriame matomos žvaigždės, matomos naktiniame danguje bet kuriuo konkrečiu metu. Sukant diską rodoma, kaip žvaigždės juda dangumi naktį ir kaip skirtingu metų laiku matomi skirtingi žvaigždynai. Planisfera yra puikus dangaus orientyras, ieškant žvaigždynų, ūkų, galaktikų ir planetų. Planisfera galima naudoti, kaip mokymo priemonę. Su planisferos pagalba galima apytiksliai nustatyti laiką arba kryptį. 

Kam reikalinga kartoninė, savo rankomis suklijuota planisfera, kai telefone yra daugybė žvaigždėlapio programėlių? Jeigu jums kyla toks klausimas - šis Github kampelis yra ne jums, negaiškite čia savo brangaus laiko.

#### Kaip naudoti

Norėdami sukurti Lietuvos platumų planisferos modelius 1° intervalais, paleiskite skriptą `main_planisphere.sh`. Planisferos dalys (.svg, .png, .pdf) sugeneruojamos "Output" direktorijoje. Planisferos sugeneruojamos platumoms nuo 52°N iki 56°N (kas 1°). Planisferos sugeneruojamos anglų, lietuvių ir ispanų kalbomis. Geriausia naudoti kažkurią linux OS su instaliuotu python'u ir LaTex (Kile ir Okular). Puikiai veikia su Raspberry pi minikompiuteriu ir Bookworm OS. Suteikite skriptui reikiamus linux saugumo leidimus (`chmod 777 main_planisphere.sh`). Paleiskite planisferų generavimo skriptą:  `./main_planisphere.sh` arba `sudo ./main_planisphere.sh`.

#### Apribojimai

Planisferos netinka, kai jos naudojamos arti ekvatoriaus. Šioje saugykloje esantys skriptai neleidžia kurti planisferų platumoms tarp 15 laipsnių šiaurės platumos ir 15 laipsnių pietų platumos, nes dangaus ašigalis yra per arti horizonto.

#### Autorinės teisės

Ši kodą sukūrė Dominic Ford <https://dcford.org.uk>. Jis platinamas pagal „Gnu General Public License V3“.
