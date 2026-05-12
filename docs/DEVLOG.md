Izstrādes žurnāls.

1. solis: Plānošana

Izplānoju projekta struktūru: gan no kādiem failiem sastāv, gan no kādām funkcijām.
Grūti bija izplānot katru funckiju - kā var redzēt, nebiju iedomājusies, ka get_available_months() būs nepieciešama, kaut arī tā skaidri un gaiši redzama projekta uzdevuma aprakstā. Tikai rakstot programmu sapratu, kur un kādēļ tā vispār tikusi pieminētu, kāpēc nepieciešama.
Iemācījos apmēram vizualizēt projekta kopbildi un struktūru. 
Nebija diez ko grūti izdomāt robežgadījumus un kā apstrādāt. 

2. solis: Datu slānis un pamata darbības

Uzrakstīju storage.py funkcijas json failu lasīšanai un saglabāšanai. Tas padevās viegli un saprotami, tā kā jau iepriekš tādas funkcijas tika rakstītas un strādāja pareizi.
Uzrakstīju logic.py funkcijas kopsummai, pievienošanai, izdevumu parādīšanai. Funkcijas kopumā nebija grūti uzrakstīt, taču validāciju pievienoju tikai pa visam vēlāk (tikai tad, kad sāka pielekt, ka kaut kas trūkst, nav tā). 
Pagrūti bija iztēloties, kā uzrakstīt app.py, jo iepriekš līdzīga programma tika rakstīta ar sys.argv palīdzību, toties šeit nācās paļauties uz input(), kas uzreiz lika funkcijai atšķirties.

3. solis: Filtrēšana, kopsavilkums un dzēšana

Pievienoju logic.py filter_by_month, sum_by_category, get_available_months + citas nianses, lai programma varētu izskatīties kā paraugizvadē. 
Kā jau iepriekš minēju - bija ļoti grūti saprast, kas vispār ir get_available_months funkcija, kur un kam tā vajadzīga, kamēr nesāku rakstīt to programmas daļu un neredzēju paraugizvadi.
Filtrēšana kopumā bija sarežģīta, runaiesot par tās ieviešanu app.py. Sarežģīta loģika.
Kopumā dabūju cīnīties ar to, lai uzrakstītu programmu kā paraugizvadē, jo tā noteikti bija grūtāka par manis iepriekš iztēloto rezultātu - toties sanāca vairak apgūt.
Cīnījos šajā solī ar datu formatēšanu.

4. solis: CSV eksports un dokumentācija 

Izveidoju export.py, kur uzrakstīju export_to_csv. Šis bija diezgan viegli, tā kā bija paraugs un ieviest validāciju nebija sarežģīti. Atbilstoši ievietot app.py arī nesagādāja grūtības.