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
    if name != '':
      break

  while True:
    phone = input('ведите номер телефона: ')
    if phone.isdigit() and len(phone) == 12 and name != '':
      break
    else: 
      print('Номер должен состоять из 12 символов и содержать только цифры.')

  while True:
    email = input('Введите адрес электронной почты: ')
    if '@' in email and email != '':
      break
    else:
      print('Электронная почта должна содержать символ "@".')

  return dict(name=name, phone=phone, email=email)


def detect_name_or_phone(input: str) -> str | None:
  if input != '' and input.isdigit():
    return 'phone'
  elif input != '':
    return 'name'
  else:
    print('Введите имя или номер телефона:')


def add_contact(contacts: list[dict]) -> None:
  contact = input_and_validate_contact_data()
  contacts.append(contact)
  write_file(contacts)


def display_sorted_contacts_by_name(contacts):
  sorted_contacts = sorted(contacts, key=lambda contact: contact.get('name'))
  
  numeration = 1
  for contact in sorted_contacts:
    print(f"{numeration}. {contact['name']},   {contact['phone']},   {contact['email']}")
    numeration += 1

contacts = [
    {'name': 'Denys', 'phone': '+42087584', 'email': 'chornopyskyidenys@gmail.com'},
    {'name': 'Artem', 'phone': '+420989485093', 'email': 'chornopyskyiartem@gmail.com'},
    {'name': 'Olga', 'phone': '+420123456789', 'email': 'olga@example.com'}
]

display_sorted_contacts_by_name(contacts)
