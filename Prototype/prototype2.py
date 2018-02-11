# Import library
import psycopg2
import getpass
import pandas.io.sql as psql

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
  # Groups neighbourhood name and zipcode together. Shows the number of
  # listings in each zipcode, shows the average number of bedrooms
  q1 = """SELECT neighbourhood, 
    zipcode, 
    COUNT(neighbourhood), 
    ROUND(CAST(AVG(beds) as NUMERIC), 2) AS Avg_num_bedrooms

    FROM Listings 
       GROUP BY neighbourhood, 
            zipcode ORDER BY 3 DESC LIMIT 10"""

  # Group the listings by neighbourhood and show me the number of listings
  # in each neighbourhood and zipcode and show me each average price

  q2 = """SELECT Listings.neighbourhood, 
    Summary_listings.neighbourhood AS zipcode, 
    COUNT(*), 
    ROUND(CAST(AVG(Summary_listings.price) as NUMERIC), 2) AS Avg_price
    FROM Listings 
    INNER JOIN Summary_listings
      ON  Listings.id = Summary_listings.id
        GROUP BY  Listings.neighbourhood, 
                Summary_listings.neighbourhood
        ORDER BY 3 DESC LIMIT 10"""

  return q1, q2

def main():
# Prompt user for info
  u_n, pw = get_info()
# Connect to the postgres
  con = psycopg2.connect(dbname="airbnb", user=u_n, password=pw, host= "localhost")
# Get queries
  q1, q2 = queries()
# Message
  print("You're connected!")
  done = 'no'
  while(done == 'no'):
    print()
    print()
    # Show all query choices
    print("""q1: Groups neighbourhood name and zipcode together. 
    Shows the number of listings in each zipcode, and shows the average number of bedrooms in DESC order""")
    print("q2: Group the listings by neighbourhood and show me the number of listings in each neighbourhood and zipcode and show me each average price")
    
    # Prompt user for query choice
    print()
    print()
    choice = input('What would you like to query?')
    print()
    while(choice != 'q2' and choice !='q1'):
      choice = input('What would you like to query?')

    if(choice == 'q1'):
      print(psql.read_sql_query(q1,con))
    else:
      print(psql.read_sql_query(q2,con))

    # Ask if user is finished
    print()
    print("Are you done with this session?")
    print()
    done = input("(yes/no):")
    while(done!= 'yes' and done!='no'):
      done = input("(yes/no):")

  # Print goodbye
  print()
  print('See you later!')

# Close connection man
  con.close()
    

main()