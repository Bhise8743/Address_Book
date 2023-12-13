"""

@Author: Omkar Bhise

@Date: 2023-12-12 09:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-12 12:30:00

@Title :  Address Book Program

"""

"""
debug
info
warning
exception
error
"""

import logging

logging.basicConfig(filename="Address_book_log.log", level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
logger = logging.getLogger(__name__)  # current file name


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
        print(f"Name : {self.name} , Address : {self.address},")
        print(f"{self.city} {self.state} - {self.zip_code},")
        print(f"Phone No. : {self.p_num}  Email : {self.email}")
        print("----------------------------------------------------------------------------")

    def update_contact(self):
        """
           Description:
               this function used to update the contact details

           Parameter: self

           Return: None

        """
        try:
            while True:

                user_choice = int(input("""
                                                1. change name
                                                2. change address 
                                                3. change city
                                                4. change state
                                                5. change zip code
                                                6. change phone number
                                                7. change email
                                                8. exist
                                        """))
                if user_choice != 8:
                    change_con = input("Enter the changeable thing ")  # changeable content
                match user_choice:
                    case 1:
                        self.name = change_con
                    case 2:
                        self.address = change_con
                    case 3:
                        self.city = change_con
                    case 4:
                        self.state = change_con
                    case 5:
                        self.zip_code = change_con
                    case 6:
                        self.p_num = change_con
                    case 7:
                        self.email = change_con
                    case 8:
                        break
        except Exception as ex:
            logger.exception(ex)


class AddressBook():

    def __init__(self, name):
        self.address_book_name = name
        self.contact_dict = {}

    def add_contact(self, con_obj):
        """
           Description:
               this function used to add new contact in the contact book

           Parameter: self , con_obj: contact object

           Return: None

        """
        self.contact_dict.update({con_obj.name: con_obj})

    def display_all_contacts(self):
        """
           Description:
               this function used to display all contact details

           Parameter: self

           Return: None

        """
        try:
            for key, value in self.contact_dict.items():
                value.display_contact()
        except Exception as ex:
            print(ex)

    def update_contact_in_book(self, name):
        """
           Description:
               this function used update the contact details of one person

           Parameter: self , name of person

           Return: None

        """
        try:
            con_obj: Contact = self.contact_dict.get(name)
            if con_obj:
                con_obj.update_contact()
        except Exception as ex:
            print(ex)

    def delete_contact(self, name):
        """
           Description:
               this function used to delete contact form the address book

           Parameter: self

           Return: None

        """
        try:
            self.contact_dict.pop(name)
        except Exception as ex:
            print(ex)
        else:
            print("Contact deleted successfully ")


class MultipleAddressBook:
    def __init__(self):
        self.add_book_dict = {}

    def add_new_book(self, add_obj: AddressBook):
        """
           Description:
               this function used to add an address book in the multiple books

           Parameter: self , object of address book class

           Return: None

        """
        self.add_book_dict.update({add_obj.address_book_name: add_obj})

    def get_book(self, name):
        """
           Description:
               this function used to return the address book

           Parameter: self

           Return: None

        """
        return self.add_book_dict.get(name)  # address book name as a key


def main():
    """
       Description:
           this function used to create object of class and call the member function of the class

       Parameter: self

       Return: None

    """

    print("Welcome To Address Book program in AddressBookMain class on Master Branch ")
    mul_a_b_obj = MultipleAddressBook()
    try:
        while True:
            user_choice = int(input("""
                        1. Add contact in the Address book
                        2. Update Contact 
                        3. Display all contacts 
                        4. Delete contact of Person
                        5. Exit
            """))

            match user_choice:
                case 1:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    if add_book_obj is None:
                        add_book_obj = AddressBook(a_book_name)

                    name = input("Enter the first and last name ")
                    address = input("Enter the address ")
                    city = input("Enter the city ")
                    state = input("Enter the state ")
                    zip_code = input("Enter the zip code ")
                    p_num = input("Enter the Phone number ")
                    email = input("Enter the email ")
                    con_obj = Contact(name, address, city, state, zip_code, p_num, email)

                    add_book_obj.add_contact(con_obj)
                    mul_a_b_obj.add_new_book(add_book_obj)

                case 2:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    name = input("Enter the name of person ")
                    add_book_obj.update_contact_in_book(name)
                case 3:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    add_book_obj.display_all_contacts()
                case 4:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    name = input("Enter the name person name you want to remove from the address book ")
                    add_book_obj.delete_contact(name)
                case 5:
                    break
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    main()
