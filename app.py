from storage import load_expenses, save_expenses
from logic import sum_total, add_expense, list_expenses
from logic import get_available_months, filter_by_month, sum_by_category

CATEGORIES = ["Ēdiens", "Transports", "Izklaide", "Komunālie maksājumi", "Veselība", "Iepirkšanās", "Cits"] 

def show_menu():
    """
    Parāda galveno izvēlni un atgriež lietotāja izveli.
    """
    print("\n1) Pievienot izdevumu") 
    print("2) Parādīt izdevumus") 
    print("3) Filtrēt pēc mēneša")
    print("4) Kopsavilkums pa kategorijām")
    print("5) Dzēst izdevumu")
    print("6) Eksportēt CSV")
    print("7) Iziet")

    return input("\nIzvēlies darbību (1-7): ").strip()

def main(): 
    """
    Galvenā programma, kas mijiedarbojas ar lietotāju, atkarībā no iepriekšējās izvēles.
    """ 
    expenses = load_expenses() 

    while True: 
        choice=show_menu() 

        if choice=="1": 
            date=input("Datums (YYYY-MM-DD) [2026-05-11]: ")
            amount=input("Cena: ")
            category=input("Kategorija: 1) Ēdiens, 2) Transports, 3) Izklaide, 4) Komunālie maksājumi, 5) Veselība, 6) Iepirkšanās, 7) Cits: ")
            description=input("Apraksts: ")

            message=add_expense(expenses, date, amount, category, description)
            print(message)

            if message.startswith("Pievienots"):
                save_expenses(expenses) 

        elif choice=="2":
            print("Izdevumi: ")
            print(list_expenses(expenses))
            print("Kopsumma: ")
            print(f"{sum_total(expenses):.2f} EUR")

        elif choice=="3":
            months=get_available_months(expenses)

            print("\nPieejamie mēneši:")
            for i, (year, month) in enumerate(months, start=1):
                print(f"{i}) {year}-{month:02d}") #02d - mēnesis vienmēr sastāves no 2 cipariem.
            
            n=int(input("Izvēlies mēnesi: "))

            if n<1 or n>len(months):
                print("Nepareiza izvēle.")
                continue #Lai programma tomēr turpinātu strādāt, nevis immediately apstātos.

            selected_year, selected_month=months[n - 1]

            filtered=filter_by_month(expenses, selected_year, selected_month)

            print(f"\n{selected_year}-{selected_month:02d} izdevumi: ")

            print(list_expenses(filtered))

            print(f"\nKopā: {sum_total(filtered):.2f} EUR ({len(filtered)} ieraksti)")

        elif choice=="7": 
            print("Visu labu!") 
            break 

        else:
            print("Nezināma komanda.")
        
if __name__ == "__main__": 
    main() 