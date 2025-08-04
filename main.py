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
    if phone.lstrip('+').isdigit() and len(phone.lstrip('+')) == 12 and name != '':
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


def detect_name_or_number() -> tuple:
  while True:
    contact_to_find = input('Введите имя или номер телефона: ')
    formated_contact_query = contact_to_find.lstrip('+').lower()

    if formated_contact_query.isdigit() and len(formated_contact_query) == 12:
      contact_type = 'phone'
      break
    elif contact_to_find.isalpha():
      contact_type = 'name'
      break
  return (formated_contact_query, contact_type)


def add_contact(contacts: list[dict]) -> None:
  contact = input_and_validate_contact_data()
  contacts.append(contact)
  write_file(contacts)
  print('✅ Контакт успешно добавлен!')


def print_sorted_contacts_by_name(contacts: list[dict]) -> None:
  sorted_contacts = sorted(contacts, key=lambda contact: contact.get('name').lower())
  numeration = 1

  for contact in sorted_contacts:
    print(f"{numeration}. {contact['name']},   {contact['phone']},   {contact['email']}")
    numeration += 1


def find_contact(contacts: list[dict]) -> None:
  formated_contact_query, contact_type = detect_name_or_number()

  if any(contact[contact_type].lower().lstrip('+') == formated_contact_query for contact in contacts):
    print('\n')
    for contact in contacts:
      if contact[contact_type].lower().lstrip('+') == formated_contact_query:
        print(f"{contact['name']},   {contact['phone']},   {contact['email']}")
  else:
    print('❌ Контакт не найден.')


def remove_contact(contacts: list[dict]) -> None:
  formated_contact_query, contact_type = detect_name_or_number()

  if any(contact[contact_type].lower().lstrip('+') == formated_contact_query for contact in contacts):
    numeration = 1
    index = 0
    matching_contact_indices = []

    for contact in contacts:
      if contact[contact_type].lower().lstrip('+') == formated_contact_query:
        matching_contact_indices.append(index)
        print(f"{numeration}. {contact['name']},   {contact['phone']},   {contact['email']}")
        numeration += 1
      
      index += 1

    while True:
      try: 
        chosen_number = int(input('Выберите контакт для удаления (введите номер, 0 — если все): '))
      except ValueError:
        print('Введите число')
      else:
        if chosen_number < numeration and chosen_number >= 0:
          break
        else:
          print('Введите соответствующий номер')

    if chosen_number == 0:
      for index in sorted(matching_contact_indices, reverse=True):
        del contacts[index]
      write_file(contacts)
      print('✅ Контакты удалены!')

    else:
      del contacts[matching_contact_indices[chosen_number - 1]]
      print('✅ Контакт удалён!')

  else:
    print('❌ Контакт не найден.')


def update_contact(contacts: list[dict]) -> None:
  formated_contact_query, contact_type = detect_name_or_number()

  if any(contact[contact_type].lower().lstrip('+') == formated_contact_query for contact in contacts): 
    for contact in contacts:
      if contact[contact_type].lower().lstrip('+') == formated_contact_query:
        print(f"{contact['name']},   {contact['phone']},   {contact['email']}")
        updated_contact = input_and_validate_contact_data()
        contacts[contacts.index(contact)].update(updated_contact)
        print('✅ Контакт обновлён!')
        break

  else:
    print('❌ Контакт не найден.')


def main():
  contacts = parse_contacts()
  menu = (
        '\n1. Добавить контакт\n'
        '2. Найти контакт\n'
        '3. Удалить контакт\n'
        '4. Обновить контакт\n'
        '5. Просмотреть контакты\n'
        '6. Выйти\n'
        )

  while True:
      print(menu) 
      user_query = int(input('Введите номер действия: '))
      match(user_query):
        case 1:
          add_contact(contacts)
        case 2:
          find_contact(contacts)
        case 3: 
          remove_contact(contacts)
        case 4:
          update_contact(contacts)
        case 5:
          print_sorted_contacts_by_name(contacts)
        case 6:
          break


main()

