import csv 
import faker
import random

def fake_tenant(n):
  # create a faker object
  fake = faker.Faker()

  # create an empty list to store all data
  data = []
  for i in range (n):
    # create a dictionary for each row/entry
    tenant_df = {}
    tenant_df['id'] = i + 1
    tenant_df['first_name'] = fake.first_name()
    tenant_df['last_name'] = fake.last_name()
    tenant_df['birthdate'] = fake.date(pattern="%Y-%m-%d", end_datetime=None)
    tenant_df['email'] = fake.email()
    tenant_df['phone_number'] = fake.phone_number()
    data.append(tenant_df)


  # open csv file for writing
  file = open('Tenant.csv', 'w', newline = '')
  fieldnames = ['id', 'first_name', 'last_name', 'birthdate', 'email', 'phone_number']
  writer = csv.DictWriter(file, fieldnames = fieldnames)

  # write a row with the fieldnames
  writer.writeheader()

  # write out the data
  for i in range (len(data)):
    writer.writerow(data[i])

  # close the csv file
  file.close()

def fake_property(n):
  # create a faker object
  fake = faker.Faker()

  # create an empty list to store all data
  data = []
  for i in range (n):
    nbs = ["West Campus", "Northridge", "Avery Ranch", "Downtown", "North Campus", "East Downtown", "Rainey", "Riverside", "South Congress", "Barton Hills", "Zilker"]
    # create a dictionary for each row/entry
    property_df = {}
    property_df['id'] = i + 1
    property_df['neighborhood'] = random.choice(nbs)
    holder = fake.address()
    property_df['address'] = holder[:holder.find("\n")]
    property_df['city'] = "Austin"
    property_df['state'] = "TX"
    property_df['zipcode'] = fake.zipcode()
    data.append(property_df)


  # open csv file for writing
  file = open('Property.csv', 'w', newline = '')
  fieldnames = ['id', 'neighborhood', 'address', 'city', 'state', 'zipcode']
  writer = csv.DictWriter(file, fieldnames = fieldnames)

  # write a row with the fieldnames
  writer.writeheader()

  # write out the data
  for i in range (len(data)):
    writer.writerow(data[i])

  # close the csv file
  file.close()

def fake_property_summary(n):
  # create a faker object
  fake = faker.Faker()

  # create an empty list to store all data
  data = []
  for i in range (n):
    # create a dictionary for each row/entry
    pt = ["Penthouse", "Apartment", "House", "Condo", "Lakehouse", "Cabin"]
    property_df = {}
    property_df['property_id'] = i + 1
    property_df['property_type'] = random.choice(pt)
    property_df['year_built'] = fake.year()
    property_df['date_of_ownership'] = fake.date(pattern="%Y-%m-%d", end_datetime=None)
    sp = random.randint(100000, 890000)
    property_df['sale_price'] = float(sp)
    mg = random.choice([0.8 * sp, None])
    property_df['initial_mortgage'] = mg
    if(mg == None):
      property_df['interest'] = None
      property_df['remaining_mortgage'] = None
    else:
      property_df['remaining_mortgage'] = mg * random.random()
      property_df['interest'] = float(random.randint(2,7))
    property_df['yearly_hoa'] = float(random.randint(1500,4000))
    property_df['property_tax'] = float(random.randint(1500,4000))
    property_df['num_beds'] = random.randint(1,6)
    property_df['num_bath'] = random.randint(0,6)
    property_df['area_sqft'] = float(random.randint(100,1500))
    data.append(property_df)


  # open csv file for writing
  file = open('Property_summary.csv', 'w', newline = '')
  fieldnames = ['property_id', 'property_type', 'year_built', 'date_of_ownership', 'sale_price', 'initial_mortgage', 'remaining_mortgage', 'interest', 'yearly_hoa', 'property_tax', 'num_beds', 'num_bath', 'area_sqft']
  writer = csv.DictWriter(file, fieldnames = fieldnames)

  # write a row with the fieldnames
  writer.writeheader()

  # write out the data
  for i in range (len(data)):
    writer.writerow(data[i])

  # close the csv file
  file.close()

def fake_contract(n):
  # create a faker object
  fake = faker.Faker()

  # create an empty list to store all data
  data = []
  for i in range (100):
    # create a dictionary for each row/entry
    contract_df = {}
    contract_df['property_id'] = 100 - i 
    contract_df['tenant_id'] = i + 1
    contract_df['move_in_date'] = fake.date(pattern="%Y-%m-%d", end_datetime=None)
    contract_df['move_out_date'] = fake.date(pattern="%Y-%m-%d", end_datetime=None)
    contract_df['monthly_rent'] = random.randint(400, 5000)
    dep = random.randint(100,1500)
    contract_df['deposit'] = dep
    contract_df['refund'] = random.random() * dep
    data.append(contract_df)

  for i in range (n-100):
    # create a dictionary for each row/entry
    contract_df = {}
    contract_df['property_id'] = random.randint(1,50)
    contract_df['tenant_id'] = random.randint(1,50)
    contract_df['move_in_date'] = fake.date(pattern="%Y-%m-%d", end_datetime=None)
    contract_df['move_out_date'] = fake.date(pattern="%Y-%m-%d", end_datetime=None)
    contract_df['monthly_rent'] = random.randint(400, 5000)
    dep = random.randint(100,1500)
    contract_df['deposit'] = dep
    contract_df['refund'] = random.random() * dep
    data.append(contract_df)

  # open csv file for writing
  file = open('Contract.csv', 'w', newline = '')
  fieldnames = ['property_id', 'tenant_id', 'move_in_date', 'move_out_date', 'monthly_rent', 'deposit', 'refund']
  writer = csv.DictWriter(file, fieldnames = fieldnames)

  # write a row with the fieldnames
  writer.writeheader()

  # write out the data
  for i in range (len(data)):
    writer.writerow(data[i])

  # close the csv file
  file.close()

def main():
  # 100 tenants, 100 properties, and 140 contracts
  fake_tenant(100)
  fake_property(100)
  fake_property_summary(100)
  fake_contract(140)
  print()
  print("Generated tables")

main()
  