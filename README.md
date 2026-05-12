Projekta apraksts:
Programma izseko izdevumus, tos pievienojot, parādot, filtrējot pēc mēneša, veidojot kopsavilkumu pēc kategorijām, dzēšot noteiktu izdevumu, dodot iespēju eksportēt uz csv.
Viscaur tiek lietots input(), lai lietotājs varētu mijiedarboties ar programmu, kā arī pastāv dažādi validācijas principi (nevar būt nepozitīvi skaitļi, jābūt pareizam datuma formātam utt.).

Uzstādīšana:
1. Noklonēt repozitoriju:
```bash
git clone https://github.com/ellinjaaaa/5week-final-project.git
```

2. Atvērt projekta mapi:
```bash
cd 5week-final-project
```

3. Palaist programmu:
```bash
python app.py
```

Pieejamās komandas:
1) Pievienot izdevumu - pievieno izdevumu, lietotājam parsot ievadīt datumu, cenu, kategoriju un aprakstu; ja tas viss iziet cauri validācijai un viss ok, tiek pievienots sarakstam expenses.
2) Parādīt izdevumus - parāda formatētu sarakstu ar visiem izdevumiem un to kopsummu.
3) Filtrēt pēc mēneša - no sākuma izfiltrē visus pieejamos mēnešus, tad pēc lietotāja izvēles parāda tā mēneša visus izdevumus; ja kļūdaina izvēle - atbilstošs paziņojums.
4) Kopsavilkums pa kategorijām - parāda katras kategorijas kopsummu un pilnīgi visu izdevumu kopsummu.
5) Dzēst izdevumu - pēc lietotāja izvēles tiek izdzēsts saraksta elements; ja ievade 0 - nekas netiek dzēsts; ja neatbilstoša ievade - paziņojums, ka nepareizs numurs.
6) Eksportēt CSV - saraksts tiek eksportēts csv formātā (Excel, Google Sheets u.tml.).
7) Iziet - beidzas programmas darbība.

Autore: Ella Luīze Zarāne