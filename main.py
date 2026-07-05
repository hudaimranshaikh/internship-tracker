applications = []
def add_internship():
   company = input("Enter Company Name: ")
   position = input("Enter Position:")
   status = input("Enter Status:")
   application_date = input("Enter Application Date:")
   internship = {
      "company": company,
      "position": position,
      "status": status,
      "application_date": application_date
   }
   applications.append(internship)
   print("\nInternship added successfully!")
def view_applications():
   for internship in applications:
      print(internship)
   
   
def main():
    while True:
      print("=" * 40)
      print("Internship Application Tracker")
      print("=" * 40)

      print("\n1. Add Internship ")
      print("2. View Applications")
      print("3. Search Application")
      print("4. Update Application")
      print("5. Delete Application")
      print("6. Statistics")
      print("7. Exit")
      choice = input("\nChoose an option :")

      if choice == "1":
         add_internship()
      elif choice == "2":
         view_applications()
      elif choice == "3":
         print("\nSearching Application...")
      elif choice == "4":
         print("\nUpdating Application...")
      elif choice == "5":
         print("\nDeleting Application...")
      elif choice == "6":
         print("\nShowing Statistics...")
      elif choice == "7":
         print("\nGoodbye!")
         break 
      else:
         print("\nInvalid Option")
  
      
if __name__ == "__main__":
        main()
