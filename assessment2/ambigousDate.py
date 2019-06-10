import sys
def ambigousDate(date_string):
    first_sep =  date_string.find('/')
    first_part = date_string[:first_sep]
    second_part = date_string[first_sep+1:]
    second_sep = second_part.find('/')
    second_part = second_part[:second_sep]
    return first_part <= '12' and second_part <= '12'

print(ambigousDate(sys.argv[1])) 