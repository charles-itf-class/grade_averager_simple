""" Grade Averager
 for_class.py
 To demonstrate a working version of the grade averager
 Python 3
 Charles Becker, chbecker0@protonmail.com
 2019-09-10
 Based on pseudocode by Gavin Plaisance
"""

# Setting this in the global namespace
# In python this is called a 'list' and is similar to an array
# Though Python has a distinct data structure for Arrays 
grade_names = ['A', 'B', 'C', 'D', 'F']

# These would be pulled from a database, but this is for demonstration
# This is close to what is called an 'associative array' in other langauges
# In Python this is called a Dict (short for Dictionary).
# It is an implemenation of a data structure called a 'hash map'
student_grades = {'121':64.5, '212':93, '418':72, '616':23}

def main():
	''' Python does not require a 'main' function, but for best practicies it is usually 
		implemented.
		Within the main process no unnecessary processing, input, or output should be placed '''
	# Here we are setting up an empty variable (type Int) to receive the processed data
	student_average = 0
	current_average = get_grade_average(student_grades)
	current_grade_letter = get_grade_name(current_average)
	display_grades(current_average, current_grade_letter)


def get_grade_average(grades):
	''' This calculates and returns the student's average grade to the main function '''

	counter = 0.0
	hold_grades = 0
	for test_id in grades:
		hold_grades += grades[test_id]
		counter += 1

	return hold_grades / counter


def get_grade_name(average):
	''' This returns the letter representation of the grade to the main function '''

	if average > 90:
		return grade_names[0]
	elif average > 80:
		return grade_names[1]
	elif average > 70:
		return grade_names[2]
	elif average > 60:
		return grade_names[3]
	else:
		return grade_names[5]


def display_grades(average, letter):
	''' This provides the user with output on the student'''

	print("The students average grade is: {}".format(average))
	print("The students average grade letter is: {}".format(letter))


# Below the 'main' function is called to begin program operation
main()
