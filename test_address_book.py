import pytest
from Address_Book import AddressBook, Contact, MultipleAddressBook


@pytest.fixture
def contact_obj():
    return Contact('Omakr Bhise', "Mahalangi", "Latur", "Maharashtra", 413529, 9960401728, "omakrbhise8743@gmail.com")


@pytest.fixture
def address_book_obj():
    return AddressBook("Maha")


@pytest.fixture
def multiple_address_book_obj():
    return MultipleAddressBook()


def test_add_contact_in_address_book(contact_obj, address_book_obj):
    assert len(address_book_obj.contact_dict) == 0
    address_book_obj.add_contact(contact_obj)
    assert len(address_book_obj.contact_dict) > 0


def test_update_contact(contact_obj):
    assert contact_obj.city == "Latur"
    contact_obj.update_contact(3, "Pune")
    assert contact_obj.city == "Pune"


def test_contact(contact_obj, address_book_obj):
    address_book_obj.add_contact(contact_obj)
    assert len(address_book_obj.contact_dict) > 0
    address_book_obj.delete_contact('Omakr Bhise')
    assert len(address_book_obj.contact_dict) == 0


def test_get_book(address_book_obj):
    assert isinstance(address_book_obj, AddressBook) == True


def test_search_contact_using_City(address_book_obj, contact_obj):
    address_book_obj.add_contact(contact_obj)
    assert address_book_obj.search_contact('Latur')


def test_add_new_address_book(multiple_address_book_obj, address_book_obj):
    assert len(multiple_address_book_obj.add_book_dict) == 0
    multiple_address_book_obj.add_new_address_book(address_book_obj)
    assert len(multiple_address_book_obj.add_book_dict) > 0
