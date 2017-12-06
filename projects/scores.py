#This program gets test scores from the user and calculates the highest, lowest, and average grade
def main():
  students = 0
  total_scores = 0
  score_prompt = "Student's Score (enter '-1' when finished): "
  error_str = "Enter a number from 0 - 100."

  score = input(score_prompt)
  while not score.isdigit():
    if score == "-1":
      break
    else:
      print(error_str)
      score = input(score_prompt)
  score = eval(score)

  while score != -1 :
    if score < 0 or score > 100 :
      print(error_str)
    else :
      if students == 0 :
        min_score = score
        max_score = score
      else :
        if score > max_score :
          max_score = score
        elif score < min_score :
          min_score = score
      students += 1
      total_scores += score

    score = input(score_prompt)
    while not score.isdigit():
      if score == "-1":
        break
      else:
        print(error_str)
        score = input(score_prompt)
    score = eval(score)

  if students != 0 :
    test_avg = total_scores / students
    print("\nLowest Score:", min_score)
    print("Highest Score:", max_score)
    print("Average Score:", test_avg)
  else :
    print("Not enough data.")

main()