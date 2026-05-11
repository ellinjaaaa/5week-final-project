import sys
from storage import load_expenses, save_expenses
from logic import sum_total, add_expense, list_expenses

CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Cits"] 

def show_menu():
    """
    Parāda galveno izvēlni un atgriež lietotāja izveli.
    """
    print("\n1) Pievienot izdevumu") 
    print("2) Parādīt izdevumus") 
    print("7) Iziet")

    return input("\nIzvēlies darbību (1-7): ")