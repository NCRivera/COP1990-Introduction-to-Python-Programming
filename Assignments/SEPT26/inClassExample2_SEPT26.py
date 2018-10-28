# Declare the books read variable.
books = 0
# Prompt the user to enter the number of books they have read this month.
books = int(input('How many books have you read this month: '))

# 8 or more books = 60 Points
if books >= 8:
    print('You get 60 POINTS!!!')

# 6 books = 30 Points
elif books >= 6:
    print('You get 30 POINTS!!!')

# 4 books = 15 Points
elif books >= 4:
    print('You get 15 POINTS!!!')

# 2 books = 5 Points
elif books >= 2:
    print('You get5  POINTS!!!')
# 0 books = 0 Points
elif books >= 0:
    print('You get 0 POINTS!!!')
# Based on the int given, award points for number of books read.
else:
    print('I DON\'T KNOW')

# Display the points awarded

