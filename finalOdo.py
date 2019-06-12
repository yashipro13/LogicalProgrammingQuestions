def isValidReading(reading):
    reading_str = str (reading)
    i = 0
    returnVal = True
    while i < len (reading_str) - 1:
        if reading_str[i] >= reading_str[i + 1]:
            return False
        i += 1
    return returnVal

def getNext(curr_reading):
    next_read = curr_reading + 1
    while not isValidReading(next_read):
        next_read += 1
    return next_read

def getPrevious(curr_reading):
    prev_read = curr_reading - 1
    while not isValidReading(prev_read):
        prev_read -= 1
    return prev_read

def getNthNext(curr_reading, n):
    count = 0
    while count != n:
        curr_reading = getNext(curr_reading)
        count = count + 1
    return curr_reading

def getNthPrevious(curr_reading, n):
    count = 0
    while count != n:
        curr_reading = getPrevious(curr_reading)
        count += 1
    return curr_reading

def getStep (reading1, reading2):
    small = min (reading1, reading2)
    big = max (reading1, reading2)
    step = 0
    while small <= big:
        small = getNext(small)
        step += 1
    return step

print(getNext(129))
print(getNthNext(789,3))
print(getPrevious(123))
print(getNthPrevious(123,5))
print(getStep(123,134))
