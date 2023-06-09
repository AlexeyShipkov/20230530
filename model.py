phone_book = []
path = 'phone.txt'
def open_pb ():
    print('test')
    global phone_book, path
    with open(path, 'r+', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(':')
        phone_book.append({'name':contact[0], 'phone':contact[1], 'comment':contact[2]})
        

def print_pb ():
   #print(phone_book)
   for line in phone_book:
            print(line)
 
 #   for contact in phone_book:
        #print (contact)
       

