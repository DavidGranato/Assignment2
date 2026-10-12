"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    return cost_per_semester(annual_cost) / CLASS_DAYS_PER_SEMESTER


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    return cost_per_semester(annual_cost) / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    return cost_per_credit(annual_cost, credits) * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER


# ---- PROGRAM ----

def main():
    print("The Cost of College")
    try:
        annual_cost = float(input("Enter the total cost for one year: $"))
        credits = int(input("Enter the credits you are taking this semester: "))
    except ValueError:
        print("Enter a numeric yearly cost and a whole number of credits.")
        return

    if annual_cost < 0 or credits <= 0:
        print("The yearly cost must be zero or more, and credits must be greater than zero.")
        return

    while True:
        print("\n1. Cost per semester")
        print("2. Cost per academic month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per 50-minute CS 1430 meeting")
        print("6. Worth It? The cost of missing CS 1430")
        print("Q. Quit")

        choice = input("Choose an option: ").strip().upper()

        if choice == "Q":
            print("Goodbye!")
            break
        elif choice == "1":
            print(f"Cost per semester: ${cost_per_semester(annual_cost):,.2f}")
        elif choice == "2":
            print(f"Cost per academic month: ${cost_per_month(annual_cost):,.2f}")
        elif choice == "3":
            print(f"Cost per class day: ${cost_per_day(annual_cost):,.2f}")
        elif choice == "4":
            print(f"Cost per credit: ${cost_per_credit(annual_cost, credits):,.2f}")
        elif choice == "5":
            print(f"Cost per 50-minute CS 1430 meeting: ${cost_per_class(annual_cost, credits):,.2f}")
        elif choice == "6":
            try:
                missed_meetings = int(input("How many CS 1430 meetings would you miss? "))
                hourly_pay = float(input("Enter your hourly pay for comparison: $"))
            except ValueError:
                print("Enter a whole number of meetings and a numeric hourly pay.")
                continue

            if missed_meetings < 0 or missed_meetings > CS1430_MEETINGS_PER_SEMESTER:
                print(f"Enter a number of meetings from 0 to {CS1430_MEETINGS_PER_SEMESTER}.")
            elif hourly_pay <= 0:
                print("Hourly pay must be greater than zero.")
            else:
                # Use the unrounded meeting cost so rounding does not accumulate.
                missed_cost = missed_meetings * cost_per_class(annual_cost, credits)
                work_hours = missed_cost / hourly_pay
                print(f"College cost allocated to those missed meetings: ${missed_cost:,.2f}")
                print(f"At ${hourly_pay:,.2f} per hour, that equals {work_hours:.2f} hours of work before taxes.")
                print("Missing class does not reduce your bill. Is skipping worth that value to you?")
        else:
            print("Invalid option. Choose 1 through 6, or Q to quit.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
