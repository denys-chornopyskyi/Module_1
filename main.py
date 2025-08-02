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

contacts = parse_contacts()

def contacts_to_string(contacts: list[dict]) -> None:
  contacts = contacts.copy()
  new_contacts = []
  for contact in contacts:
    line = f"{contact['name']}, {contact['phone']}, {contact['email']}\n"
    new_contacts.append(line)
  with open('contacts.txt', 'w') as file:
    print(new_contacts)
    file.writelines(new_contacts)

def add_contact():
  while True:
    name = input('Введите имя: ')
    if name.strip() == '':
      continue
    break

  while True:
    phone = input('Введите телефон: ')
    if name.strip() == '':
      continue
    if len(phone) < 12:
      continue
    break

  while True:
    email = input('Введите email: ')
    if name.strip() == '':
      continue
    if '@' not in email:
      continue
    break

  print('✅ Контакт успешно добавлен!')

      
  contact = {
      'name': name,
      'phone': phone,
      'email': email
    }
  contacts.append(contact)
  
  print(contacts)
  
  contacts_to_string(contacts)

add_contact()



