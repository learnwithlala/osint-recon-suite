from modules import linkedin_enum, social_osint, github_footprint, breach_check, name_targeting

def banner():
    with open("banner.txt", "r") as b:
        print(b.read())

def main():
    banner()
    print("1. LinkedIn Enumeration")
    print("2. Social Media OSINT")
    print("3. GitHub Footprinting")
    print("4. Breach Check (HIBP, IntelX, Pastebin)")
    print("5. First-Name Based LinkedIn Targeting")
    
    choice = input("Choose an option: ")

    if choice == "1":
        company = input("Enter company name: ")
        linkedin_enum.linkedin_enum(company)

    elif choice == "2":
        username = input("Enter username/full name: ")
        social_osint.social_media(username)

    elif choice == "3":
        company = input("Enter company name: ")
        github_footprint.github_footprint(company)

    elif choice == "4":
        email = input("Enter email: ")
        breach_check.breach_check(email)

    elif choice == "5":
        company = input("Enter company: ")
        name = input("Enter first name (e.g. admin/dev/engineer): ")
        name_targeting.name_targeting(company, name)

    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
