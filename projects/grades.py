#This program calculates letter grades for students based on data from a .txt file
def main():
  grade_data = []

  correct_filename = False
  while not correct_filename:
    file_name = input("Enter the name of the file: ")
    try:
      my_file = open(file_name, "r")
      correct_filename = True
    except:
      print("Couldn't find a file with that name.")
  
  line = my_file.readline()
  while line != "":
    line = line.rstrip("\n").split(":")
    for index in range(2, 5):
      line[index] = eval(line[index])
    grade_data.append(line)
    line = my_file.readline()
  my_file.close()

  my_file = open(file_name, "a")
  my_file.write("\n\n")
  sorted_grades = []

  for gr in grade_data:
    final_grade_info = []
    weighted = gr[2] * 0.25 + gr[3] * 0.30 + gr[4] * 0.45

    if weighted >= 90:
      letter_gr = "A"
    elif weighted >= 80:
      letter_gr = "B"
    elif weighted >= 70:
      letter_gr = "C"
    elif weighted >= 60:
      letter_gr = "D"
    else:
      letter_gr = "F"
    
    my_file.write("{} {} {} {}\n".format(gr[1], gr[0], weighted, letter_gr))
    final_grade_info.extend([letter_gr, gr[1], gr[0]])
    sorted_grades.append(final_grade_info)
  
  view_in_order = input("Sort grades? (yes/no): ")
  if view_in_order in ["yes", "y", "yeah", "yes!", "ok", "okay"]:
    sorted_grades.sort()

  for gr in sorted_grades:
    print("{} {} {}".format(gr[0], gr[1], gr[2]))

  my_file.close()


main()