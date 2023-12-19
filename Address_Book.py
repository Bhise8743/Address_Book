"""

@Author: Omkar Bhise

@Date: 2023-12-12 09:30:00

@Last Modified by: Omkar Bhise

@Last Modified time: 2023-12-14 02:30:00

@Title :  Address Book Program

"""
import csv

"""
debug
info
warning
exception
error
critical
"""
# stream handler
import logging

logging.basicConfig(filename="Address_book_log.log", level=logging.DEBUG,  # by default filemode is the append()  if
                    # you want the wirte the update every time then the filemode is the write
                    format='%(asctime)s %(levelname)s %(message)s')
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
               this function is used to display contact details

           Parameter: self

           Return: None

        """
        print(f"Name : {self.name} , Address : {self.address},")
        print(f"City : {self.city}, State : {self.state} - {self.zip_code},")
        print(f"Phone No. : {self.p_num}  Email : {self.email}")
        print("----------------------------------------------------------------------------")

    def update_contact(self):
        """
           Description:
               this function is used to update the contact details

           Parameter: self

           Return: None

        """
        try:
            while True:

                user_choice = int(input("""
                                                1. exit
                                                2. change address 
                                                3. change city
                                                4. change state
                                                5. change zip code
                                                6. change phone number
                                                7. change email
                                                
                                        """))
                if user_choice != 8:
                    change_con = input("Enter the changeable thing ")  # changeable content
                match user_choice:
                    case 1:
                        break
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

        except Exception as ex:
            logger.exception(ex)

    def add_contact_to_txt(self):
        """
           Description:
               this function is used to return the contact

           Parameter: self

           Return: it returns the contact Object

        """
        return {
            f'Name : {self.name} , Address : {self.address} , City : {self.city} , State : {self.state} , Zip-Code : {self.zip_code}, '
            f'Phone Number {self.p_num} , E-mail : {self.email}'}

    def add_contact_to_csv(self):
        """
           Description:
               this function is used to return the contact

           Parameter: self

           Return: it returns the contact Object

        """
        return {
            "name": self.name, "address": self.address, "city": self.city, "state": self.state,
            "zip_code": self.zip_code, "p_num": self.p_num, "email": self.email}


class AddressBook():

    def __init__(self, name):
        self.address_book_name = name
        self.contact_dict = {}

    def add_contact(self, con_obj):
        """
           Description:
               this function is used to add new contact in the contact book

           Parameter: self , con_obj: contact object

           Return: None

        """
        self.contact_dict.update({con_obj.name: con_obj})

    def display_one_contact(self, name):
        """
           Description:
               this function is used to display one person contact details

           Parameter: self

           Return: None

        """
        con_obj = self.contact_dict.get(name)
        con_obj.display_contact()

    def display_all_contacts(self):
        """
           Description:
               this function is used to display all contact details

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
               this function is used update the contact details of one person

           Parameter: self , name of person

           Return: None

        """
        try:
            con_obj: Contact = self.contact_dict.get(name)
            if con_obj:
                con_obj.update_contact()
        except Exception as ex:
            print(ex)

    def search_contact(self, city):
        """
           Description:
               this function is used search the contact using city or state name

           Parameter: self , city :city in the contact

           Return: None

        """

        contacts = dict(filter(lambda x: x[1].city.lower() == city.lower() or x[1].state.lower() == city.lower(),
                               self.contact_dict.items()))
        # print(contacts)
        for i in contacts.values():
            i.display_contact()
        return len(contacts)

    def sort_contact_using_person_name(self):
        """
           Description:
               this function is used sort the contact using person name

           Parameter: self

           Return: None

        """
        for key, value in dict(sorted(self.contact_dict.items())).items():
            value.display_contact()

    def make_a_dict_person_city_state(self, ):
        """
           Description:
               this function is used to make a dictionary of person city , state

           Parameter: self

           Return: None

        """

        for key, value in self.contact_dict.items():
            print(f" Name : {value.name}  city : {value.city}  state : {value.state}")

        # print(f"Person :City {self.person_city_dict}")
        # print(f"Person : state {self.person_state_dict}")
        # contacts = filter(lambda x : x[1].city)

    def sort_add_book_con_using_city(self, city_name):
        """
           Description:
               this function is used to sort contact using city or state

           Parameter: self

           Return: None

        """
        sorted_con = sorted(self.contact_dict.values(), key=lambda x: x.city == city_name, reverse=False)
        for i in sorted_con:
            i: Contact
            print(f"{i.name} --> {i.city}")

    def delete_contact(self, name):
        """
           Description:
               this function is used to delete contact form the address book

           Parameter: self , name : name of contact person

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
               this function is used to add an address book in the multiple books

           Parameter: self , object of address book class

           Return: None

        """
        self.add_book_dict.update({add_obj.address_book_name: add_obj})

    def get_book(self, name):
        """
           Description:
               this function is used to return the address book

           Parameter: self, name : name of the contact person

           Return: contact object

        """
        return self.add_book_dict.get(name)  # address book name as a key

    def search_con_using_city(self, city):
        """
           Description:
               this function is used to search contact using city name

           Parameter: self, city : city of the contact person

           Return: contact object

        """
        for key, value in self.add_book_dict.items():
            value.search_contact(city)

    def search_con_using_state(self, state):
        """
           Description:
               this function is used to search contact using state name

           Parameter: self, state : state of the contact person

           Return: contact object

        """
        for key, value in self.add_book_dict.items():
            value.search_contact(state)

    def add_contact_to_txt_file(self):
        """
           Description:
               this function is used to write the details of the contacts in the text file

           Parameter: self

           Return: None

        """
        with open("add_book_contact.txt", 'w') as f:
            for book, add_book_obj in self.add_book_dict.items():
                add_book_obj: AddressBook
                for contact, con_obj in add_book_obj.contact_dict.items():
                    con_obj: Contact
                    f.write(str(f'{con_obj.add_contact_to_txt()} \n'))

        # read the text file data
        with open("add_book_contact.txt", 'r') as f:
            i = f.read()
        print(i)

    def add_book_csv_file(self):
        """
           Description:
               this function is used to write the details of the contacts in the csv file

           Parameter: self

           Return: None

        """
        with open("add_book_csv.csv", 'w', newline="") as f:
            filed_name = ["name", "address", "city", "state", "zip_code", "p_num", "email", "book_name"]
            writer = csv.DictWriter(f, fieldnames=filed_name)
            writer.writeheader()
            for book, add_book_obj in self.add_book_dict.items():
                add_book_obj: AddressBook
                for contact, con_obj in add_book_obj.contact_dict.items():
                    data = con_obj.add_contact_to_csv()
                    data.update({'book_name': contact})
                    print(data)
                    writer.writerow(data)


def main():
    """
       Description:
           this function is used to create object of class and call the member function of the class

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
                        5. Search Contact using state 
                        6. Search Contact using city
                        7. Maintain dictionary of Person City State
.                        8. Sort data in address book using person name 
                        9. sort address book contact using city name 
                        10. Add contact to the text files 
                        11. Add contact to the csv files 
                        12. exit
            """))

            match user_choice:
                case 1:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    if add_book_obj is None:
                        add_book_obj = AddressBook(a_book_name)

                    name = input("Enter the first and last name ")
                    if add_book_obj.contact_dict.get(name) is None:
                        address = input("Enter the address ")
                        city = input("Enter the city ")
                        state = input("Enter the state ")
                        zip_code = input("Enter the zip code ")
                        p_num = input("Enter the Phone number ")
                        email = input("Enter the email ")
                    else:
                        print("Contact already present ")
                        add_book_obj.display_one_contact(name)
                        continue

                    con_obj = Contact(name, address, city, state, zip_code, p_num, email)
                    add_book_obj.add_contact(con_obj)
                    mul_a_b_obj.add_new_book(add_book_obj)

                case 2:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    if add_book_obj is None:
                        print("This book is not present ")

                    name = input("Enter the name of person ")
                    add_book_obj.update_contact_in_book(name)
                case 3:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    if add_book_obj is None:
                        print("This book is not present ")

                    add_book_obj.display_all_contacts()
                case 4:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    if add_book_obj is None:
                        print("This book is not present ")

                    name = input("Enter the name person name you want to remove from the address book ")
                    add_book_obj.delete_contact(name)
                case 5:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    if add_book_obj is None:
                        print("This book is not present ")

                    state = input("Enter state name ")
                    temp = add_book_obj.search_contact(state)
                    print(f"In the {state} there are {temp} Contact present")
                case 6:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    if add_book_obj is None:
                        print("This book is not present ")

                    city = input("Enter city name ")
                    temp = add_book_obj.search_contact(city)
                    print(f"In the {city} there are {temp} contact present ")
                case 7:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    if add_book_obj is None:
                        print("This book is not present ")
                    add_book_obj.make_a_dict_person_city_state()
                case 8:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    if add_book_obj is None:
                        print("This book is not present ")
                    add_book_obj.sort_contact_using_person_name()
                case 9:
                    a_book_name = input("Enter the address book name : ")
                    add_book_obj = mul_a_b_obj.get_book(a_book_name)
                    if add_book_obj is None:
                        print("This book is not present ")
                    city_name = input("Enter the city name ")
                    add_book_obj.sort_add_book_con_using_city(city_name)
                case 10:
                    mul_a_b_obj.add_contact_to_txt_file()
                case 11:
                    mul_a_b_obj.add_book_csv_file()
                case 12:
                    break

    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    main()
