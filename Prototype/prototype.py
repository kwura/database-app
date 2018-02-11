# Import library
import psycopg2
import getpass
import pandas.io.sql as psql

def get_info():
  print("Hey what's up!! Welcome to your database!")
  # u_n = input("Please enter username: ")
  # pw = getpass.getpass("Please enter your password: ")
  u_n = "postgres"
  pw = "lilli4n"
  return u_n, pw

def main():
# Prompt user for info
  if __name__ == '__main__':
    u_n, pw = get_info()

    column_names = []
    data_rows = []

    con = psycopg2.connect(dbname="postgres", user=u_n, password=pw, host= "localhost") 
    cur = con.cursor()
    cur.execute("SELECT * FROM cats")
    rows = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    for row in cur:
      data_rows.append(row)

  # print("Column names: {}\n".format(column_names))
    print()
    print()
    print(column_names)
    print('______________________________')
    for i in rows:
      print(i)

main()