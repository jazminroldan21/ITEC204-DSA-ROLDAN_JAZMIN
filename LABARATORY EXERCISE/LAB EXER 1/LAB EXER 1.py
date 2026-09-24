class Ticket:
    """A node in the linked list holding one incident ticket."""

    def __init__(self, incident_id, bot, description):
        self.incident_id = incident_id
        self.bot = bot
        self.description = description
        self.next = None


class TicketManager:
    """Singly linked list of active incident tickets."""

    def __init__(self):
        self.head = None
        self.size = 0

    # 1. Add a new ticket (appended at the tail)
    def add_ticket(self, incident_id, bot, description):
        if self.search_ticket(incident_id):
            print(f"\n[!] Ticket {incident_id} already exists. Not added.")
            return False
        new_ticket = Ticket(incident_id, bot, description)
        if self.head is None:
            self.head = new_ticket
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_ticket
        self.size += 1
        return True

    # 2. Display all active tickets
    def display_tickets(self):
        if self.head is None:
            print("\nNo active incident tickets.")
            return
        print("\n" + "=" * 92)
        print(f"{'No.':<5}{'Incident ID':<15}{'Bot':<20}{'Short Description'}")
        print("=" * 92)
        current, n = self.head, 1
        while current:
            print(f"{n:<5}{current.incident_id:<15}{current.bot:<20}{current.description}")
            current = current.next
            n += 1
        print("=" * 92)

    # 3. Search a ticket by Incident ID
    def search_ticket(self, incident_id):
        current = self.head
        while current:
            if current.incident_id.upper() == incident_id.upper():
                return current
            current = current.next
        return None

    # 4. Remove a resolved ticket
    def remove_ticket(self, incident_id):
        current, prev = self.head, None
        while current:
            if current.incident_id.upper() == incident_id.upper():
                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return True
            prev, current = current, current.next
        return False

    # 5. Count active tickets
    def count_tickets(self):
        return self.size


SAMPLE_DATA = [
    ("INC1392939", "BOT-Inventory", "Failed to generate the daily report"),
    ("INC1392940", "BOT-Email", "Failed to send the scheduled notification"),
    ("INC1392941", "BOT-DataSync", "Encountered an error during data transfer"),
    ("INC1392942", "BOT-Invoice", "Failed to process an invoice"),
    ("INC1392943", "BOT-Report", "Failed to generate the weekly report"),
    ("INC1392944", "BOT-FileTransfer", "Failed to upload the required file"),
    ("INC1392945", "BOT-DataEntry", "Encountered an error while entering records"),
    ("INC1392946", "BOT-Backup", "Failed to complete the scheduled backup"),
    ("INC1392947", "BOT-Validation", "Failed to validate the submitted records"),
    ("INC1392948", "BOT-Notification", "Failed to send the system alert"),
]


def print_menu():
    print("\n" + "=" * 45)
    print("   IT AUTOMATION INCIDENT TICKET MANAGER")
    print("=" * 45)
    print("  1. Add a new incident ticket")
    print("  2. Display all active incident tickets")
    print("  3. Search a ticket by Incident ID")
    print("  4. Remove a resolved ticket")
    print("  5. Display total active tickets")
    print("  6. Exit")
    print("=" * 45)


def main():
    manager = TicketManager()
    for inc_id, bot, desc in SAMPLE_DATA:
        manager.add_ticket(inc_id, bot, desc)
    print(f"Loaded {manager.count_tickets()} sample incident tickets.")

    while True:
        print_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            inc_id = input("Incident ID        : ").strip()
            bot = input("Bot                : ").strip()
            desc = input("Short Description  : ").strip()
            if not (inc_id and bot and desc):
                print("\n[!] All fields are required.")
            elif manager.add_ticket(inc_id, bot, desc):
                print(f"\n[+] Ticket {inc_id} added successfully.")

        elif choice == "2":
            manager.display_tickets()

        elif choice == "3":
            inc_id = input("Enter Incident ID to search: ").strip()
            t = manager.search_ticket(inc_id)
            if t:
                print("\n[✓] Ticket found:")
                print(f"    Incident ID      : {t.incident_id}")
                print(f"    Bot              : {t.bot}")
                print(f"    Short Description: {t.description}")
            else:
                print(f"\n[x] Ticket {inc_id} not found.")

        elif choice == "4":
            inc_id = input("Enter Incident ID to remove: ").strip()
            if manager.remove_ticket(inc_id):
                print(f"\n[-] Ticket {inc_id} resolved and removed.")
            else:
                print(f"\n[x] Ticket {inc_id} not found.")

        elif choice == "5":
            print(f"\nTotal active incident tickets: {manager.count_tickets()}")

        elif choice == "6":
            print("\nExiting program. Goodbye!")
            break

        else:
            print("\n[!] Invalid choice. Please enter 1-6.")


if __name__ == "__main__":
    main()
