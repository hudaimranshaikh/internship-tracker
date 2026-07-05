#Internship Application Tracker 
#python CRUD Project
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
      print("Company:",internship["company"])
      print("Position",internship["position"])
      print("Status",internship["status"])
      print("Application Date:",internship["application_date"])
      print("-"*30)
def search_application():
   company_name =input("Enter Company Name to Search:")
   for internship in applications:
      if internship["company"] == company_name:  
         print("Company:",internship["company"])
         print("Position",internship["position"])
         print("Status",internship["status"])
         print("Application Date:",internship["application_date"])   
         print("-"*30)
def update_application():
   company_name = input("Enter Company Name to Update:")
   found = False 
   for internship in applications:
       if internship["company"] == company_name:
          new_status = input("Enter New Status:")
          internship["status"]= new_status
          found = True 
          print("\nStatus updated successfully")
          break
   if not found:
      print("company not found")
def delete_application():
   company_name = input("Enter Company Name to Delete:")
   found = False

   for internship in applications:
      if internship["company"] == company_name:
         applications.remove(internship)
         found = True
         print("\nApplication deleted successfully!")
         break
   if not found:
      print("Company not found.")   
def show_statistics():
    total = len(applications)
    
    approved = 0
    rejected = 0
    for internship in applications:
       if internship["status"] == "approved":
          approved +=1
       if internship["status"] == "rejected":
        rejected += 1
    print("Total Applications:",total)
    print("Approved Applications:",approved)
    
    print("Rejected Applications:", rejected)
def main():
    while True:
      print("\n" + "=" * 50)
      print("      INTERNSHIP APPLICATION TRACKER")
      print("=" * 50)

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
         search_application()
      elif choice == "4":
         update_application()
      elif choice == "5":
         delete_application()
      elif choice == "6":
         show_statistics()
      elif choice == "7":
         print("\nGoodbye!")
         break 
      else:
         print("\nInvalid Option")
  
      
if __name__ == "__main__":
        main()
