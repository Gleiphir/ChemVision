import xml.etree.ElementTree as ET
import time
import csv

of_path = './products.csv'


begin = time.time()
print('begin ',begin)
tree = ET.parse('full_database.xml')
end = time.time()
print('end ',end )
print()
print('duration',end-begin)
print()
input()
