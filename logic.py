from datetime import datetime

def sum_total(expenses):
    '''
    Sasummē kopā pilnīgi visas izmaksas ar sum() un for cikla palīdzību.
    '''
    return sum(expense["amount"] for expense in expenses)

def add_expense(expenses, date, amount, category, description):
    '''
    Pievieno izdevumu (datums | izmaksas | kategorija | apraksts). Ja nekas netiek ievadīts, negatīvs izdevums vai nav skaitlis - atbilstoši
    paziņojumi. Ja viss ok - pievieno expenses sarakstam doto vārdnīcu ar izdevuma atslēgām un vērtībām; tad atgriež, ka pievienots.    
    '''

    date=date.strip()
    category=category.strip()
    description=description.strip()

    if not date or not amount or not category or not description:
        return "Nevar būt tukša ievade."
    
    try:
        amount=float(amount)
    except ValueError:
        return "Izdevumam jābūt skaitlim."
    
    if amount <=0:
        return "Izdevums nevar būt negatīvs."
    
    expenses.append({"date":date, "amount":amount, "category":category, "description":description})

    return f"Pievienots: {date} | {amount:.2f} EUR | {category} | {description}"

def list_expenses(expenses):
    '''
    Atgriež sanumurētu sarakstu ar saistītajiem datiem no expenses saraksta. Citādāk - nav izdevumu.
    '''
    if not expenses:
        return "Nav izdevumu."
    
    lines=[]

    for i, expense in enumerate(expenses):
        lines.append(f"{i+1}. {expense['date']} | {expense['amount']:.2f} EUR | {expense['category']} | {expense['description']}")
    
    return "\n".join(lines) #\n - katrs elements izdrukāts jaunā rindā; join - saliek vienā tekstā. 

def filter_by_month(expenses, year, month): 
    """
    Atgriež izdevumus, kuru datums ir norādītajā mēnesī.
    """ 
    result = [] 

    for expense in expenses: 
        d = datetime.strptime(expense["date"], "%Y-%m-%d") 
        if d.year == year and d.month == month: 
            result.append(expense) 
    return result 

#def sum_by_category():

#def get_available_motnhs():

#def 