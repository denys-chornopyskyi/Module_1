def parse_contacts() -> list[dict]:
  """
  Parses contact file and return list of contacts as dict

  Returns:
    list[dict]: a list where each contact is represented as dict
  """

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
  """
  overwrites contacts file with updated list of contacts

  Args:
  contacts (list[dict]): a list of contacts to write to the file
  """
  contacts = contacts.copy()
  new_contacts = []

  for contact in contacts:
    line = f"{contact['name']}, {contact['phone']}, {contact['email']}\n"
    new_contacts.append(line)

  with open('contacts.txt', 'w') as file:
    file.writelines(new_contacts)


def input_and_validate_contact_data() -> dict:
  """
  Prompts the user to enter their name, phone, email, validating each input

  Returns:
    dict: A dict containing the user's name, phone and email
  """
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


def validate_number_input(start: int, stop: int, input_text: str) -> int:
  """
  Prompts the user to enter a number within the specified range and validates the input.

  Args:
    start (int): The beginning of the range (inclusive)
    stop (int): The end of the valid range (exclusive)
    input_text (str): The text shown to the user when asking for input

  Returns:
    int: A valid number entered by the user within the specified range.
  """


  while True:
      try: 
        chosen_number = int(input(f'{input_text}: '))
      except ValueError:
        print('Error!! Введите число')
      else:
        if chosen_number < stop and chosen_number >= start:
          return chosen_number
        else:
          print(f'Введите соответствующий номер ({start} - {stop - 1})')


def detect_name_or_number() -> tuple:
  """
  Prompts the user to enter either a name or a phone and determines which types was entered.

  Returns:
    tuple: a tuple(formatted_contact_query, contact_type), where:
      - formatted_contact_query (str): The formatted contact string (lowercased, no "+"), for comparison in the same form.
      - contact_type (str): either 'name' or 'phone', needed for accurate lookup through the contacts dict


  """


  while True:
    contact_to_find = input('Введите имя или номер телефона: ')
    formatted_contact_query = contact_to_find.lstrip('+').lower()

    if formatted_contact_query.isdigit() and len(formatted_contact_query) == 12:
      contact_type = 'phone'
      break
    elif contact_to_find.isalpha():
      contact_type = 'name'
      break
  return (formatted_contact_query, contact_type)


def add_contact(contacts: list[dict]) -> None:
  """
  Prompts the user to enter data for a new contact and adds it to the contact list

  Args:
    contacts (list[dict]): A list of contacts to which the new contact will be added
  """
  contact = input_and_validate_contact_data()
  contacts.append(contact)
  write_file(contacts)
  print('✅ Контакт успешно добавлен!')


def print_sorted_contacts_by_name(contacts: list[dict]) -> None:
  """
  print the contacts sorted by their name in the console

  Args: 
    contacts (list[dict]): A list of contact dict, each containg (name, phone, email)
  """

  # sort contacts alphabetically by name without case sensitivity 
  sorted_contacts = sorted(contacts, key=lambda contact: contact.get('name').lower())
  numeration = 1

  for contact in sorted_contacts:
    print(f"{numeration}. {contact['name']},   {contact['phone']},   {contact['email']}")
    numeration += 1


def find_contact(contacts: list[dict]) -> None:
  """
  Promts the user to enter either name or phone, then search and print matching contacts

  Args:
    contacts (list[dict]): A list of existing contacts to search through
  """
  # gets user's input and determine its type for searching
  formatted_contact_query, contact_type = detect_name_or_number()

  # checks if there is any matching contact in the current list
  if any(contact[contact_type].lower().lstrip('+') == formatted_contact_query for contact in contacts):
    print('\n')
    for contact in contacts:
      if contact[contact_type].lower().lstrip('+') == formatted_contact_query:
        print(f"{contact['name']},   {contact['phone']},   {contact['email']}")
  else:
    print('❌ Контакт не найден.')


def remove_contact(contacts: list[dict]) -> None:
  """
  Prompts the user to enter either name or phone. If mathing contacts are found, allows the user to choose which one to delete. Otherwise print a message 
  """
  formatted_contact_query, contact_type = detect_name_or_number()

  if any(contact[contact_type].lower().lstrip('+') == formatted_contact_query for contact in contacts):
    numeration = 1
    # 
    matching_contact_indices = []


    # look through the contact list. If matching contacts are found, adds their index to matching_contact_indices for later deletion and then print them
    for contact in contacts:
      if contact[contact_type].lower().lstrip('+') == formatted_contact_query:
        matching_contact_indices.append(contacts.index(contact))
        print(f"{numeration}. {contact['name']},   {contact['phone']},   {contact['email']}")
        numeration += 1

    # returns validated number of the contact the user wants to delete
    chosen_number = validate_number_input(0, numeration, 'Выберите контакт для удаления (введите номер, 0 — если все)')

    if chosen_number == 0:
      # deletes all matching contacts using reversed, sorted list of indices to avoid index shifting
      for index in sorted(matching_contact_indices, reverse=True):
        del contacts[index]
      write_file(contacts)
      print('✅ Контакты удалены!')

    else:
      # deletes selected contact
      del contacts[matching_contact_indices[chosen_number - 1]]
      write_file(contacts)
      print('✅ Контакт удалён!')

  else:
    print('❌ Контакт не найден.')


def update_contact(contacts: list[dict]) -> None:
  """
  Prompts the user to enter either number or name. If matching contacts are found, prompts the user to choose one to update, then ask for a new contact data. finally, updates to the current contact list and save it to the contacts file.
  """

  formatted_contact_query, contact_type = detect_name_or_number()

  if any(contact[contact_type].lower().lstrip('+') == formatted_contact_query for contact in contacts): 
    numeration = 1
    matching_contact_indices = []
    
    for contact in contacts:
      if contact[contact_type].lower().lstrip('+') == formatted_contact_query:
        matching_contact_indices.append(contacts.index(contact))
        print(f"{numeration}. {contact['name']},   {contact['phone']},   {contact['email']}")
        numeration += 1

    chosen_number = validate_number_input(1, numeration, 'Выберите контакт для обновления')
    updated_contact = input_and_validate_contact_data()
    contacts[matching_contact_indices[chosen_number - 1]].update(updated_contact)
    write_file(contacts)
    print('✅ Контакт обновлён!')


  else:
    print('❌ Контакт не найден.')


def main() -> None:
  """
  parses contacts from contacts file, then display the menu of options the user can perform on the contact list
  """
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
      user_query = validate_number_input(1, 7, 'Введите номер действия')
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
          print('👋 Программа завершена. До свидания!')
          break


main()