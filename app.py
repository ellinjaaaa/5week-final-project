from storage import load_expenses, save_expenses
from logic import sum_total, add_expense, list_expenses
from logic import get_available_months, filter_by_month, sum_by_category
from export import export_to_csv
from datetime import date

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
            today=date.today()

            other_date=input(f"Datums (YYYY-MM-DD) [{today}]: ")
            amount=input("Cena: ")
            category=input("Kategorija: 1) Ēdiens, 2) Transports, 3) Izklaide, 4) Komunālie maksājumi, 5) Veselība, 6) Iepirkšanās, 7) Cits: ")
            description=input("Apraksts: ")

            message=add_expense(expenses, other_date, amount, category, description)
            print(message)

            if message.startswith("Pievienots"):
                save_expenses(expenses) 

        elif choice=="2":
            print(f"\n{'Datums':<12} {'Summa':>15} {'Kategorija':>21} {'Apraksts':>17}")
            print("-" * 80) 
            print(list_expenses(expenses))
            print("-" * 80) 
            print("\nKopsumma: ")
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

            print("-" * 80) 

            print(f"{'Datums':<12} {'Summa':>15} {'Kategorija':>21} {'Apraksts':>17}")

            print("-" * 80) 

            print(list_expenses(filtered))

            print("-" * 80) 

            print(f"\nKopā: {sum_total(filtered):.2f} EUR ({len(filtered)} ieraksti)")

        elif choice=="4":
            catsum=sum_by_category(expenses)

            print("\nKopsavilkums pa kategorijām: ")

            print("-" * 50) 

            for category, amount in catsum.items():
                print(f"{category:<21}: {amount:<10.2f} EUR")

            print("-" * 50) 

            print(f"KOPĀ: {sum_total(expenses):.2f} EUR")

        elif choice=="5":
            print("\nIzdevumi: ")
            print(list_expenses(expenses))

            text=int(input("Kuru dzēst? (numurs vai 0, lai atceltu)").strip())

            if text==0:
                print("Nekas netika izdzēsts.")

            elif 1<=text<=len(expenses):
                n=expenses.pop(text-1)

                save_expenses(expenses)

                print(f"Dzēsts: {n['date']} | {n['amount']:.2f} EUR | {n['category']} | {n['description']}")

            else:
                print("Nepareizs numurs.")

        elif choice=="6":
            file=input("Faila nosaukums [izdevumi.csv]: ")
            if file.endswith(".csv"):
                export_to_csv(expenses, f"{file}")
                print(f"Eksportēts: {len(expenses)} ieraksti -> {file}")

            else:
                print("Kaut kas aizgāja ne tā...")

        elif choice=="7": 
            print("Visu labu!") 
            break 

        else:
            print("Nezināma komanda.")
        
if __name__ == "__main__": 
    main() 