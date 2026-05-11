1. solis: Plānošana (bez koda!) 
Mērķis: iemācīties domāt par programmu pirms tās rakstīšanas. 
 
A. Programmas apraksts (2–3 teikumi) 
• Ko programma dara? Kam tā ir domāta? 

Programma izsekos izdevumus, lietotājam ievadot nepieciešamos datus. Varēs pievienot jaunus izdevumus (uzskaitot datumu, kategoriju, apmaksu un aprakstu), apskatīt, dzēst, filtrēt, kopā summēt, kā arī eksportēt CSV, piem., lai apskatītu Excelī.

B. Datu struktūra 
• Kā izskatās viens izdevuma ieraksts? (uzraksti piemēru) 

expense = {
"date": "2026-05-11", 
"amount": 3.50,
"category": "Food",
"description": "Lido pusdienas"
}

• Kāpēc izvēlējies tieši šādu struktūru? 

Jo viens izdevums ir ar vairākiem saistītiem datiem, kuriem visērtāk būtu piekļūt caur atslēgām (tātad - nepieciešams vārdnīcas (dictionary) formāts).

C. Moduļu plāns 
• Kādi faili būs projektā? Ko katrs darīs? 

app.py - galvenā programma, kur lietotājs ievadīs, apskatīs u. tml. mijiedarbosies ar info
storage.py - funkcijas saistībā ar json failiem (to lasīšanu, pārrakstīšanu, saglabāšanu)
logic.py -  ar datiem veicamās darbības: filtrēšana, summēšana, grupēšana, dzēšana
export.py - csv eksports (piem., Excel, Google Sheets)
expenses.json - automātiski izveidotais fails, kas glabā vārdnīcas ar saistītajiem datiem

• Kuras funkcijas būs katrā failā? (nosaukumi un īsi apraksti) 

storage.py: load_expenses() - nolasa sarakstu ar vārdnīcām; ja nekā nav - tukšs saraksts.
storage.py: save_expenses(expenses) - saglabā, pievienojot/pārrakstot izmaiņas.
logic.py: filter_by_month(expenses, year, month)  - atgriež noteikta mēneša izmaksas.
logic.py: list_expenses(expenses) - parāda pilno sarakstu ar visiem izdevumiem.
logic.py: sum_total(expenses) - aprēķina visu izdevumu kopējo summu.
logic.py: sum_by_category(expenses) - aprēķina, atgriež katras specifiskās kategorijas kopējos izdevumus.
logic.py: add_expense(expenses) - pievienos izdevumus.
logic.py: delete_expense(expenses) - izdzēš ierakstu pēc tā numura sarakstā.
export.py: export_to_csv(expenses, filepath) - eksportē CSV, lai varētu atvērt Excel u.tml.

D. Lietotāja scenāriji 
• Apraksti 2–3 scenārijus: ko lietotājs dara un ko programma atbild. Piemēram: "Lietotājs pievieno izdevumu bez summas — programma parāda kļūdas paziņojumu un ļauj mēģināt vēlreiz." 

1. Lietotājs mēģina dzēst kādu no izdevumiem sarakstā, taču nav izdevuma ar tādu kārtas numuru: paziņojums "Nav izdevuma ar tādu kārtas numuru" un tad var atkal mēģināt.
2. Lietotājs mēģina pievienot izdevumu ar kategoriju, kas nepastāv sarakstā. Paziņojums: "Tādas kategorijas nav. Pieejamās kategorijas: (tiek uzskaitītas visas esošās kategorijas)."

E. Robežgadījumi 
• Kas notiek, ja expenses.json neeksistē? 

Tiek atgriezts tukšs saraksts.

• Kas notiek, ja lietotājs ievada negatīvu summu? Tukšu aprakstu? Nepareizu datumu? 

Paziņojums:
negatīva summa - skaitlim jābūt pozitīvam;
tukšs apraksts - tekstam jābūt garākam par 0 rakstzīmēm un nevar būt tukšs;
nepareizs datums - pareizais datuma formāts: GGGG-MM-DD.

• Kas notiek, ja saraksts ir tukšs un lietotājs izvēlas "Parādīt"? 

Paziņojums: "Sarakstā nav uzskaitīts neviens izdevums."