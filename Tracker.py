applications = []

def load_apps():
    try:
        with open("internship_applications.txt", 'r') as f:
            return eval(f.read())
    except:
        return []
def save_apps():
    with open("internship_applications.txt", "w") as f:
        f.write(str(applications))
applications = load_apps()
while True:
    print("Internship Tracker Program")
    print("1. Add Application")
    print("2. View All")
    print("3. Stats")
    print("4. Quit")

    choice = input("Pick 1-4: ")

    if choice == '1':
        company = input("Company: ")
        role = input("Role: ")
        status =  input("Status: ")
        applications.append(f"Company: {company}, Role: {role}, Status: {status}")
        print(f"Added {company}!")
    if choice == '2':
        if applications:
            for app in applications:
                print(app)
        else:
            print("No applications yet!")
    if choice == '3':
        total = len(applications)
        print(f"Total applications: {total}")
    if choice == '4':
        save_apps()
        print("Applications saved.")
        print("Thank you, keep on applying!")
        break