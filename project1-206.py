import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
import csv

def getData(file):
# get a list of dictionary objects from the file, setting the first row of data as the keys and the other rows as values
#Input: file name
#Ouput: return a list of dictionary objects where
	
	a = []
	with open(file) as myfile:
		firstline = True
		for line in myfile:
			if firstline:
				mykeys = "".join(line.split()).split(',')
				firstline = False
			else:
				values = ''.join(line.split()).split(',')
				a.append({mykeys[n]:values[n] for n in range(0, len(mykeys))})
	return a

def mySort(data,col):
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	
	sort_list = sorted(data, key = lambda k: k[col])

	first_name =  sort_list[0]['First']
	last_name = sort_list[0]['Last']

	return first_name + " " + last_name


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	seniors = 0
	juniors = 0
	sophomores = 0
	freshman = 0

	for student in data:
		if student['Class'] == 'Senior':
			seniors += 1
		elif student['Class'] == 'Junior':
			juniors += 1
		elif student['Class'] == 'Sophomore':
			sophomores += 1
		else:
			freshman += 1

	student_class = [('Senior', seniors), ('Junior', juniors), ('Sophomore', sophomores), ('Freshman', freshman)]
	return sorted(student_class, key = lambda k: k[1], reverse = True)


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	one = 0
	two = 0
	three = 0
	four = 0
	five = 0
	six = 0
	seven = 0
	eight = 0
	nine = 0
	ten = 0
	eleven = 0
	twelve = 0

	for student in a:
		birthday = student['DOB']
		dates = birthday.split('/')
		month = dates[0]

		if month == '1':
			one += 1
		elif month == '2':
			two += 1
		elif month == '3':
			three += 1
		elif month == '4':
			four += 1
		elif month == '5':
			five += 1
		elif month == '6':
			six += 1
		elif month == '7':
			seven += 1
		elif month == '8':
			eight += 1
		elif month == '9':
			nine += 1
		elif month == '10':
			ten += 1
		elif month == '11':
			eleven += 1
		elif month == '12':
			twelve += 1

	months = [(1, one), (2, two), (3, three), (4, four), (5, five), (6, six), (7, seven), (8, eight), (9, nine), (10, ten), (11, eleven), (12, twelve)]

	months_sorted = sorted(months, key = lambda k: k[1], reverse = True)

	return months_sorted[0][0]




def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	sort_list = sorted(a, key = lambda k: k[col])

	with open(fileName, mode = 'w+') as csv_file:
		'''fieldnames = ['First', 'Last', 'Email']
		writer = csv.DictWriter(csv_file, fieldnames = fieldnames)'''

		for row in sort_list:
			csv_file.write(row['First'] + ',' + row['Last'] + ',' +row['Email'])
			csv_file.write("\n")
			

	

def findAge(a):
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.
	pass
	


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB2.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
