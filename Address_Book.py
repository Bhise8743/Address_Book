"""

@Author: Omkar Bhise

@Date: 2023-12-12 09:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-12 12:30:00

@Title :  Address Book Program

"""


class Contact:

    def __init__(self, name, address, city, state, zip_code, p_num, email):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.p_num = p_num
        self.email = email

    def display_contact(self):
        """
           Description:
               this function used to display contact details

           Parameter: self

           Return: None

        """
        print(f"Name : {self.name} ,")
        print(f"{self.address},")
        print(f"{self.city} {self.state} -{self.zip_code},")
        print(f"Phone No. : {self.p_num}")
        print(f"Email : {self.email}")


class AddressBook():

    def __init__(self,name):
        self.addres_book_name = name
        self.contact_dict = {}

    def add_contact(self,con_obj):
        """
           Description:
               this function used to add new contact in the contact book

           Parameter: self , contact object

           Return: None

        """
        self.contact_dict.update({con_obj.name:con_obj})

    def display_all_contacts(self):
        """
           Description:
               this function used to display all contact details

           Parameter: self

           Return: None

        """
        for key,value in self.contact_dict.items():
            value.display_contact()


def main():
    """
       Description:
           this function used to create object of class and call the member function of the class

       Parameter: self

       Return: None

    """

    print("Welcome To Address Book program in AddressBookMain class on Master Branch ")
    address_book = AddressBook("Maha Address")
    while True:

        user_choice = int(input("""
                    1. Add contact in the Address book
                    2. Display Contact 
                    3. exist 
        """))

        match user_choice:
            case 1:

                name = input("Enter the first and last name ")
                address = input("Enter the address ")
                city = input("Enter the city ")
                state = input("Enter the state ")
                zip_code = input("Enter the zip code ")
                p_num = input("Enter the Phone number ")
                email = input("Enter the email ")
                con_obj= Contact(name,address,city,state,zip_code,p_num,email)
                address_book.add_contact(con_obj)
                address_book.display_all_contacts()
            case 2:
                break


if __name__ == '__main__':
    main()
