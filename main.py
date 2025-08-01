def read_file():
  with open('contacts.txt', 'r') as file:
    return file.readlines()
  
def parse_contacts(lines : list[str]) -> list[dict]:
  contacts = []
  for line in lines:
    formated_list = line.strip('\n').split(', ');
    contact = {
      'name': formated_list[0].strip(),
      'phone': formated_list[1].strip(),
      'email': formated_list[2].strip()
    }
    contacts.append(contact)
  return contacts

content = read_file()
contacts = parse_contacts(content)

print(contacts[0]['name'])