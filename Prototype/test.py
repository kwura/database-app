import csv
def __init__(self):
    self.myCsv = csv.writer(open('Item.csv', 'w'))
    self.myCsv.writerow(['title', 'link'])

with open('eggs.csv', 'w') as csvfile:
    spamwriter = csv.writer(csvfile,   #delimiter=' '
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])