def parse_contacts() -> list[dict]:
  contacts = []
  
  with open('contacts.txt', 'r') as file:
    lines = file.readlines()
    
  for line in lines:
    formated_list = line.strip('\n').split(', ');
    contact = {
      'name': formated_list[0].strip(),
      'phone': formated_list[1].strip(),
      'email': formated_list[2].strip()
    }
    contacts.append(contact)
  return contacts


def write_file(contacts: list[dict]) -> None:
  contacts = contacts.copy()
  new_contacts = []

  for contact in contacts:
    line = f"{contact['name']}, {contact['phone']}, {contact['email']}\n"
    new_contacts.append(line)

  with open('contacts.txt', 'w') as file:
    file.writelines(new_contacts)


def input_and_validate_contact_data() -> dict:
  while True:
    name = input('Введите имя: ')
    if name.isalpha():
      break

  while True:
    phone = input('ведите номер телефона: ')
    if phone.isdigit() and len(phone.lstrip('+')) == 12 and name != '':
      break
    else: 
      print('Номер должен состоять из 12 символов и содержать только цифры.')

  while True:
    email = input('Введите адрес электронной почты: ')
    if '@' in email and email:
      break
    else:
      print('Электронная почта должна содержать символ "@".')

  return dict(name=name, phone=phone, email=email)


def add_contact(contacts: list[dict]) -> None:
  contact = input_and_validate_contact_data()
  contacts.append(contact)
  write_file(contacts)


def display_sorted_contacts_by_name(contacts: list[dict]) -> None:
  sorted_contacts = sorted(contacts, key=lambda contact: contact.get('name'))
  numeration = 1

  for contact in sorted_contacts:
    print(f"{numeration}. {contact['name']},   {contact['phone']},   {contact['email']}")
    numeration += 1


def find_contact(contacts: list[dict]) -> None:
  while True:
    contact_to_find = input('Введите имя или номер телефона: ')
    formated_contact_query = contact_to_find.lstrip('+').lower()

    if formated_contact_query.isdigit() and len(formated_contact_query) == 12:
      contact_type = 'phone'
      break
    elif contact_to_find.isalpha():
      contact_type = 'name'
      break

  if any(contact[contact_type].lower().lstrip('+') == formated_contact_query for contact in contacts):
    for contact in contacts:
      if contact[contact_type].lower().lstrip('+') == formated_contact_query:
        print(f"{contact['name']},   {contact['phone']},   {contact['email']}")
  else:
    print('❌ Контакт не найден.')

contacts = parse_contacts()

find_contact(contacts)