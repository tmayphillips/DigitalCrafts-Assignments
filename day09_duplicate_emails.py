filename = 'emails.txt'
emails = []

with open(filename,'r') as open_file:
    line = open_file.readline()
    for line in open_file:
        currentline = line.split(",")
        for email in currentline:
            if currentline in emails:
                pass
            else:
                emails.append(currentline)

print(emails)
