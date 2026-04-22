from datetime import datetime, timedelta


# ================== DATA ==================
library = {
    "Python": {"available": True},
    "Java": {"available": True},
    "C++": {"available": True},
    "Data Structures": {"available": True}
}

issued_books = {}


# ================== FUNCTIONS ==================

def show_books():
    print("\n📚 Available Books:")
    for book, details in library.items():
        status = "Available" if details["available"] else "Issued"
        print(f"- {book} ({status})")


def issue_book():
    book_name = input("\nEnter book name to issue: ")

    if book_name not in library:
        print("❌ Book not found!")
        return

    if not library[book_name]["available"]:
        print("❌ Book already issued!")
        return

    student = input("Enter student name: ")
    days = int(input("Enter number of days to issue: "))

    issue_date = datetime.now()
    return_date = issue_date + timedelta(days=days)

    issued_books[book_name] = {
        "student": student,
        "issue_date": issue_date,
        "return_date": return_date
    }

    library[book_name]["available"] = False

    print(f"✅ Book issued to {student}")
    print(f"📅 Return by: {return_date.date()}")

    print("\n⚠️ Fine Rules:")
    print("1st week: ₹10/day")
    print("2nd week: ₹20/day")
    print("3rd week: ₹60/day and so on...")


def calculate_fine(days_late):
    fine = 0
    rate = 10
    week = 1

    while days_late > 0:
        days_in_week = min(7, days_late)
        fine += days_in_week * rate
        days_late -= days_in_week
        week += 1
        rate = rate * week   # increasing rate

    return fine


def return_book():
    book_name = input("\nEnter book name to return: ")

    if book_name not in issued_books:
        print("❌ This book was not issued!")
        return

    record = issued_books[book_name]
    today = datetime.now()

    if today <= record["return_date"]:
        print("✅ Book returned on time. No fine.")
    else:
        late_days = (today - record["return_date"]).days
        fine = calculate_fine(late_days)
        print(f"⚠️ Late by {late_days} days")
        print(f"💰 Fine to pay: ₹{fine}")

    library[book_name]["available"] = True
    del issued_books[book_name]

    print("📚 Book returned successfully!")


# ================== MAIN MENU ==================

def main():
    while True:   # Infinite loop (required)
        print("\n====== 📚 LIBRARY MENU ======")
        print("1. Show Books")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_books()

        elif choice == '2':
            issue_book()

        elif choice == '3':
            return_book()

        elif choice == '4':
            print("👋 Thank you for using Library System!")
            break

        else:
            print("❌ Invalid choice! Try again.")


if __name__ == "__main__":
    main()