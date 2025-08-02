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


def contacts_to_text(contacts: list[dict]) -> None:
  contacts = contacts.copy()
  new_contacts = []

  for contact in contacts:
    line = f"{contact['name']}, {contact['phone']}, {contact['email']}\n"
    new_contacts.append(line)

  with open('contacts.txt', 'w') as file:
    print(new_contacts) 
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

input_and_validate_contact_data()