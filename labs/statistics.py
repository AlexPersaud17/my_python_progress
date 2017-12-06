def main():
  
  data_file = open("student_data.txt", "r")
  data = []
  student_info = []
  line = data_file.readline().rstrip("\n")
  while line != "":
    data.append(line)
    line = data_file.readline().rstrip("\n")
  data_file.close()

  for student in data:
    grades = []
    grades.append(student.split(" ")[0].capitalize())
    for item in student.split(" ")[1:]:
      grades.append(eval(item))
    student_info.append(grades)


  print("\nSTUDENT GRADE DATABASE")
  go_again =  True

  while go_again:
    print("\t1. Display students who have more than 6 scores.")
    print("\t2. Calculate average for each student.")
    print("\t3. Display each student's lowest and highest grade.")
    print("\t4. Quit.\n")
    
    option = input("What would you like to do? (Enter a number from 1-4): ")
    print()
    
    if not option.isdigit():
      print("Invalid option.\n")
      
    else:
      option = eval(option)
      if option == 1:
        print("Students with more than 6 grades:")
        for student in student_info:
          if len(student[1:]) > 6:
            print(student[0])
        print()

      elif option == 2:
        print("Average score for each student:")
        for student in student_info:
          print(student[0], round(sum(student[1:])/len(student[1:]), 2), sep = ": ")
        print()

      elif option == 3:
        for student in student_info:
          print(student[0] + ":")
          print("High -", max(student[1:]), "Low -", min(student[1:]))
        print()

      elif option == 4:
        print("Exiting...")
        go_again = False

      else:
        print("Invalid option.\n")

main()
