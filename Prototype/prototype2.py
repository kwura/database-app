# Import library
import psycopg2
import getpass
import pandas as pd
import pandas.io.sql as psql

def big_print():
  print("""




































    """)
def print_full(x):
  pd.set_option('display.height', 1000)
  pd.set_option('display.max_rows', 500)
  pd.set_option('display.max_columns', 500)
  pd.set_option('display.width', 1000)
  print(x)
  pd.reset_option('display.max_rows')

def get_info():
  print()
  print()
  print("Hey what's up!! Welcome to your LCN investments database! Hope you're well!")
  # u_n = input("Please enter username: ")
  # pw = getpass.getpass("Please enter your password: ")
  u_n = "postgres"
  pw = "lilli4n"
  return u_n, pw

def queries():
  # Show current top 15 highest monthly paying properties. Return property id, tenant name, address, and monthly rent
  q1 = """SELECT t.first_name, t.last_name,  p.address, c.monthly_rent
FROM Property as p 
JOIN Contract AS c ON p.id = c.property_id
JOIN Tenant AS t ON t.id = c.tenant_id
WHERE c.move_out_date > '2012/1/1'
ORDER BY 4 DESC
LIMIT 15 """

  # Show the properties with the 5 lowest HOA fees. Return Property id, neighborhood, address, yearly_hoa and prop_tax.

  q2 = """SELECT p.id, p.neighborhood, p.address, ps.yearly_hoa, ps.property_tax
FROM Property as p
JOIN Property_summary as ps ON p.id = ps.property_id
ORDER BY 4 DESC
LIMIT 5"""

  # Show the tenants who moved out from 2006 to 2011 and returns deposit and refund amounts.
  q3 = """SELECT t.first_name, t.last_name, t.email, t.phone_number, c.deposit, c.refund, c.move_out_date
FROM Tenant as t 
JOIN Contract as c ON t.id = c.tenant_id
WHERE EXTRACT(year FROM c.move_out_date) >= '2006' AND EXTRACT(year FROM c.move_out_date) <= '2011'
ORDER BY c.deposit DESC"""

  # Show the number of properties without a mortgage
  q4 = """SELECT Count(*) AS Number_of_properties_without_mortgage FROM 
Property_summary WHERE initial_mortgage IS NULL"""

  # -- Show the 10 lowest current mortgages.
  q5 = """SELECT p.neighborhood, p.address, ps.property_type, ps.year_built, ps.sale_price, ps.initial_mortgage, ps.remaining_mortgage, ps.interest
FROM Property_summary AS ps
JOIN Property AS p ON p.id = ps.property_id
ORDER BY 7 ASC
LIMIT 10"""

  # Show tenants who are living in properties with greater than 4 bathrooms
  q6 = """SELECT t.first_name, t.last_name, p.neighborhood, ps.property_type, p.address, ps.num_beds, ps.num_bath
FROM Property_summary AS ps
JOIN Property AS p ON p.id = ps.property_id
JOIN Contract AS c ON c.property_id = p.id
JOIN Tenant AS t ON t.id = c.tenant_id
WHERE num_bath > 4
ORDER BY 7 DESC"""

  return q1, q2, q3, q4, q5, q6

def main():
# Prompt user for info
  u_n, pw = get_info()
# Connect to the postgres
  con = psycopg2.connect(dbname="lcn", user=u_n, password=pw, host= "localhost")
# Get queries
  q1, q2, q3, q4, q5, q6 = queries()
# Message
  print("You're connected!")
  done = 'n'
  while(done == 'n'):
    print()
    print()
    # Show all query choices
    print("""[1] : Show current top 15 highest monthly paying properties. Return property id, tenant name, neighborhood, address, and monthly rent""")
    print("[2] : Show the properties with the 5 lowest HOA fees. Return Property id, neighborhood, address, yearly_hoa and prop_tax.")
    print("[3] : Show the tenants who moved out from 2006 to 2011 and returns deposit and refund amounts.")
    print("[4] : Show the number of properties without a mortgage.")
    print("[5] : Show the 10 lowest current mortgages.")
    print("[6] : Show tenants who are living in properties with greater than 4 bathrooms.")
    
    # Prompt user for query choice
    print()
    print()
    choice = input('Choose query [1 - 6] : ')
    print()
    while(choice != '1' and choice !='2' and choice !='3' and choice !='4' and choice !='5' and choice !='6'):
      choice = input('Choose query [1 - 6] : ')

    if(choice == '1'):
      big_print()
      print("""[1] : Show current top 15 highest monthly paying properties. Return tenant name, address, and monthly rent""")
      print()
      print_full(psql.read_sql_query(q1,con))
    elif(choice == '2'):
      big_print()
      print("[2] : Show the properties with the 5 lowest HOA fees. Return Property id, neighborhood, address, yearly_hoa and prop_tax.")
      print()
      print_full(psql.read_sql_query(q2,con))
    elif(choice == '3'):
      big_print()
      print("[3] : Show the tenants who moved out from 2006 to 2011 and returns deposit and refund amounts.")
      print()
      print_full(psql.read_sql_query(q3,con))
    elif(choice == '4'):
      big_print()
      print("[4] : Show the number of properties without a mortgage.")
      print()
      print_full(psql.read_sql_query(q4,con))
    elif(choice == '5'):
      big_print()
      print("[5] : Show the 10 lowest current mortgages.")
      print()
      print_full(psql.read_sql_query(q5,con))
    else:
      big_print()
      print("[6] : Show tenants who are living in properties with greater than 4 bathrooms.")
      print()
      print_full(psql.read_sql_query(q6,con))

    # Ask if user is finished
    print()
    print("Are you done with this session?")
    print()
    done = input("[y / n]:")
    while(done!= 'y' and done!='n'):
      done = input("[y / n]:")

  # Print goodbye
  print()
  print('See you later!')

# Close connection man
  con.close()
    

main()