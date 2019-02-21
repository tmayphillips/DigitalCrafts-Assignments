from datetime import datetime

pool_tables = {}
cost_per_hour = 30

class PoolTable:
    def __init__(self,table_num):
        self.table_num = table_num
        self.is_available = True
        self.start_time = datetime.now()
        self.end_time = datetime.now()

    #def __repr__(self):
        #self.table_num

    def checkout(self):
        self.is_available = False
        self.start_time = datetime.now()

    def checkin(self):
        self.is_available = True
        self.end_time = datetime.now()

    def __str__(self):
        return '{}: {} available'.format(self.table_num, self.is_available)

    def to_dictionary(self):
        return {"is_available": self.is_available}

    def from_dictionary(dictionary):
        is_available = dictionary["is_available"]
        #age = dictionary["age"]
        return PoolTable(is_available)



#for index in range(1,13):
    #pool_table = "Table " + str(PoolTable(index).table_num)
 #   table = PoolTable(index)
 #   pool_tables.append(pool_table)

#table_3 = PoolTable(3)
#pool_tables.append(table_3)
#print(pool_tables[12].is_available)

for index in range(1, 13):
    globals()['table_%s' % index] = PoolTable(index)
    pool_tables['table_%s' % index] = PoolTable('table_%s' % index)

#print(pool_tables)

table_3_dictionary = table_3.to_dictionary()
table_3.checkout()
table_3_from_dictionary = PoolTable.from_dictionary(table_3_dictionary)
print(table_3.is_available)
#print(pool_tables)



#for table in pool_tables:
#    print(table)

for index in range(1, 12):
    if 'table_%s' % index.is_available == True:
        print(f"{'table_%s' % index} is available.")
    if 'table_%s' % index.is_available == False:
        print(f"{'table_%s' % index} is not available.")

#for index in range(1,13):
#    if PoolTable(index).is_available == True:
#        print(f"Table {PoolTable(index).table_num} is available.")
#    if PoolTable(index).is_available == False:
#        total_time = datetime.now() - PoolTable(index).start_time 
#        print(f"Table {PoolTable(index).table_num} is NOT available.")
  #      print(f"The table has been occupied for {total_time} minutes.")

#print(pool_tables)

