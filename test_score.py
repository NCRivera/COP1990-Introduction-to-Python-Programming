#get three test scores, NUMBERS 0 - 100.

#get score 1
#store the score1
score_1 = float(input('What is the first test score: '))

#get score 2
#store the score2
score_2 = float(input('What is the second test score: '))

#get score 3
#store the score3
score_3 = float(input('What is the third test score: '))

#calculate average by adding the 3 scores together and divide by 3
average = (score_1 + score_2 + score_3)/3.0

#display average
print("The average score is: ", str(average))
