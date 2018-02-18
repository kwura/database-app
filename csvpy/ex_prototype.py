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
  q1 = """SELECT neighborhood, 
    zipcode, 
    COUNT(neighborhood), 
    ROUND(CAST(AVG(beds) as NUMERIC), 2) AS Avg_num_bedrooms

    FROM Listing 
       GROUP BY neighborhood, 
            zipcode ORDER BY 3 DESC LIMIT 10"""

  # Group the listings by neighbourhood and show me the number of listings
  # in each neighbourhood and zipcode and show me each average price

  q2 = """SELECT Listing.neighborhood, 
    Summary_listing.zipcode AS zipcode, 
    COUNT(*), 
    ROUND(CAST(AVG(Summary_listing.price) as NUMERIC), 2) AS Avg_price
    FROM Listing 
    INNER JOIN Summary_listing
      ON  Listing.id = Summary_listing.id
        GROUP BY  Listing.neighborhood, 
                Summary_listing.zipcode
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
  done = 'n'
  while(done == 'n'):
    print()
    print()
    # Show all query choices
    print("""q1: Groups neighbourhood name and zipcode together. 
    Shows the number of listings in each zipcode, and shows the average number of bedrooms in DESC order""")
    print("q2: Group the listings by neighbourhood and show me the number of listings in each neighbourhood and zipcode and show me each average price")
    
    # Prompt user for query choice
    print()
    print()
    choice = input('Choose query: ')
    print()
    while(choice != 'q2' and choice !='q1'):
      choice = input('Choose query: ')

    if(choice == 'q1'):
      print(psql.read_sql_query(q1,con))
    else:
      print(psql.read_sql_query(q2,con))

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