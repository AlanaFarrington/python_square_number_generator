#square number generator
def square_number_generator(user_number):
    return user_number ** 2

#triangle number generator
def triangle_number_generator(user_number):
    row = 1
    row_triangle = 0
    while row <= user_number:
        #print(row + row_triangle)
        row_triangle = row + row_triangle
        row += 1
    return row_triangle

#user_number = input("Pick a number between 1 and 100. ")
while True:
    try:
        user_number = int(input("Pick a number between 1 and 100. "))
        if user_number < 1 or user_number > 100:
            print("Oops! The number is outside of specified range")
            continue

        sq_result = square_number_generator(user_number)
        tri_result = triangle_number_generator(user_number)
        print("The square number of {} is {} and the triangle of it is {}. ".format(user_number, sq_result, tri_result))
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")
    except KeyboardInterrupt:
        print("\nExiting game. Goodbye!")
        break
    except:
        print("Unexpected fatal error!")
        break

