class BugTracker:
    def __init__(self):
        # Dictionary to store bugs: {bug_id: {description, severity, status}}
        self.bugs = {}

   
    def add_bug(self, bug_id, description, severity):
        if bug_id in self.bugs:
            print(f"Bug ID {bug_id} already exists!")
        else:
            self.bugs[bug_id] = {
                "description": description,
                "severity": severity,
                "status": "Open"
            }
            print(f"Bug {bug_id} added successfully.")

   
    def update_status(self, bug_id, new_status):
        if bug_id in self.bugs:
            self.bugs[bug_id]["status"] = new_status
            print(f"Bug {bug_id} status updated to {new_status}.")
        else:
            print(f"Bug ID {bug_id} not found!")

   
    def list_all_bugs(self):
        if not self.bugs:
            print("No bugs reported.")
        else:
            print("\n--- All Bugs ---")
            for bug_id, details in self.bugs.items():
                print(f"ID: {bug_id}")
                print(f"  Description: {details['description']}")
                print(f"  Severity:    {details['severity']}")
                print(f"  Status:      {details['status']}")
                print("-" * 30)


if __name__ == "__main__":
    tracker = BugTracker()

    
    tracker.add_bug(101, "Login button not working", "High")
    tracker.add_bug(102, "Page takes too long to load", "Medium")
    tracker.add_bug(103, "Typo in homepage heading", "Low")

    
    tracker.update_status(101, "In Progress")
    tracker.update_status(102, "Closed")

    
    tracker.list_all_bugs()

    