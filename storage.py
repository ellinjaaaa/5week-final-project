import json
import os

expenses_file="expenses.json"

def load_expenses():
    '''
    Nolasa izdevumus no JSON faila, pārveidojot Python failā. Ja fails neeksistē vai bojāts, atgriež tukšu sarakstu.
    '''
    if not os.path.exists(expenses_file):
        return []
    try:
        with open(expenses_file, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError): #Ja fails bojāts kādā veidā, tiek atgriezts tukšs saraksts.
        return []
    
def save_expenses(expenses):
    '''
    Saglabā izdevumu sarakstu ar vārdnīcām; Python -> JSON. Ja kļūda - paziņojums ar kļūdu.
    '''
    try:
        with open(expenses_file, "w", encoding="utf-8") as f:
            json.dump(expenses, f, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f"Nevar saglabāt failu: {e}.") #Paglābj no programmas crashošanas vai citām kļūdām, 
    #pie reizes norādot kļūdu (kas saglabāta, kā mainīgais e).