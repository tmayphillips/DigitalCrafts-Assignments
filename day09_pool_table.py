from datetime import datetime
from datetime import timedelta

pool_tables = {}
cost = 30

class PoolTable:
    def __init__(self,table_num):
        self.table_num = table_num
        self.is_available = True
        self.start_time = datetime.now()
        self.end_time = datetime.now()
        self.time_played = 0
        self.profit = (self.end_time - self.start_time) * 0.5

    def checkout(self):
        self.is_available = False
        self.start_time = datetime.now()
        print(self.is_available)

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



for index in range(1, 13):
    globals()['table_%s' % index] = PoolTable(index)
    #pool_tables['table_%s' % index] = PoolTable('table_%s' % index)

def view_tables():
    for table in pool_tables:
        print(table)
    for index in range(1, 13):
        if eval(f"{'table_%s' % index}").is_available == True:
            print(f"{'table_%s' % index} is available.")
        if eval(f"{'table_%s' % index}").is_available == False:
            print(f"{'table_%s' % index} is not available.")
            print(f"It was checked out at {eval('table_%s' % index).start_time.strftime('%H:%M')}.")
            eval(f"{'table_%s' % index}").time_played = days_hours_minutes(datetime.now() - eval(f"{'table_%s' % index}").start_time)
            print(eval(f"{'table_%s' % index}").time_played)
            eval(f"{'table_%s' % index}").profit = profit(datetime.now() - eval(f"{'table_%s' % index}").start_time)
            print(eval(f"{'table_%s' % index}").profit)

def checkout():
    user_input = input("What pool table would you like to checkout? ")
    if eval(f"{'table_%s' % user_input}").is_available == True:
        eval(f"{'table_%s' % user_input}").checkout()
    else:
        print("That table is already occupied.")

def checkin():
    user_input = input("What pool table would you like to checkin? ")
    if eval(f"{'table_%s' % user_input}").is_available == False:
        eval(f"{'table_%s' % user_input}").checkin()
        date = datetime.now().date()
        with open('%s.txt' % date, 'w') as file_object:
            file_object.write(str(eval(f"{'table_%s' % user_input}").table_num))
            file_object.write(str(eval(f"{'table_%s' % user_input}").is_available))
            file_object.write(str(eval(f"{'table_%s' % user_input}").time_played))
            #file_object.write("\n")
    else:
        print("That table is not checked out.")

def days_hours_minutes(td):
    return td.days, td.seconds//3600, (td.seconds//60)%60

def profit(td):
    return (td.days) * (cost * 24) + (td.seconds//3600) * cost + ((td.seconds//60)%60) * (cost / 60)


#start_time = datetime.now()
#end_time = datetime.now() + timedelta(minutes=10)

#time_played = end_time - start_time

#print(start_time.strftime("%H:%M"))
#print(end_time.strftime("%H:%M"))
#print(time_played)

def show_menu():
    print("Press 1 to see pool table availability")
    print("Press 2 to checkout a table")
    print("Press 3 to checkin a table")
    print("Press 4 to see profit of table")
    menu_input = int(input("Enter your choice: "))
    if menu_input == 1:
        view_tables()
        show_menu()
    if menu_input == 2:
        checkout()
        show_menu()
    if menu_input == 3:
        checkin()
        show_menu()
    if menu_input == 4:
        profit()
        show_menu()
    if menu_input == "q":
        exit
    

show_menu()




