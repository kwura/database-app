import csv 
import faker

def create_fake(n):
  # create a faker object
  fake = faker.Faker()

  # create an empty list to store all data
  a = []
  for i in range (n):
  	# create a simple profile for a row
  	# username, name, sex, address, mail, birthdate
    a.append(fake.simple_profile())

  return a

def main():
  # open csv file for writing
  file = open('names.csv', 'w', newline = '')
  fieldnames = ['username', 'name', 'sex', 'address', 'mail', 'birthdate']
  writer = csv.DictWriter(file, fieldnames = fieldnames)
  
  # generate the data
  data = create_fake(3000)

  # write a row with the fieldnames
  writer.writeheader()

  # write out the data
  for i in range (len(data)):
    writer.writerow(data[i])

  # close the csv file
  file.close()

main()
  
