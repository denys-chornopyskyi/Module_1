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