'''Command-menu driven application for matrix multiplication
and data validation'''
import re
import sys
import pandas as pd
import numpy as np
            
def print_matrix(matrix):
    '''Prints 3x3 matrix without brackets'''
    # converts to dataframe
    dfr = pd.DataFrame(matrix)
    # rounds to 2 decimal places
    dfr = dfr.round(2)
    # uses built-in dataframe functionality to print nicely
    print(dfr.to_string(header=False, index=False))

def matrix_transpose_mean(matrix):
    '''Performs tranpose and mean operations and prints results'''
    matrix = np.array(matrix)
    trp = np.transpose(matrix)
    print("The transpose is:")
    print_matrix(trp)
    # gets means of columns and rounds to 2 places
    col_means = np.mean(matrix, axis=0)
    col_means = np.round(col_means,2)
    # gets means of rows and rounds to 2 places
    row_means = np.mean(matrix, axis=1)
    row_means = np.round(row_means,2)
    print("The row and column mean values of the results are:")
    # prints row results on one line with comma separator
    print("Row:", end = " ")
    str_row = ", ".join(f"{num:g}" for num in row_means)
    print(str_row)
    # prints column results on one line with comma separator
    print("Column:", end = " ")
    str_col = ", ".join(f"{num:g}" for num in col_means)
    print(str_col)
    print() # just a blank line for readability

def matrix_menu(matrix1, matrix2):
    '''function to handle matrix operations with 2 matrices'''
    while True:
        try:
            print("Select a matrix operation from the list below:")
            print("a. Addition")
            print("b. Subtraction")
            print("c. Matrix multiplication")
            print("d. Element by element multiplication")
            user_input = input()
            # handle menu option and then break loop
            if user_input == "a":
                add_result = np.add(matrix1, matrix2)
                print("You selected addition. The results are:")
                print_matrix(add_result)
                matrix_transpose_mean(add_result)
                break
            if user_input == "b":
                sub_result = np.subtract(matrix1, matrix2)
                print("You selected subtraction. The results are:")
                print_matrix(sub_result)
                matrix_transpose_mean(sub_result)
                break
            if user_input == "c":
                mult_result = np.matmul(matrix1, matrix2)
                print("You selected matrix multiplication. The results are:")
                print_matrix(mult_result)
                matrix_transpose_mean(mult_result)
                break
            if user_input == "d":
                elem_result = np.multiply(matrix1, matrix2)
                print("You selected element by element multiplication. The results are:")
                print_matrix(elem_result)
                matrix_transpose_mean(elem_result)
                break
            print("Please enter a letter a-d\n")
        except ValueError:
            print("Please enter a letter")

def handle_matrix_input():
    '''function to handle matrix input'''
    while True:
        try:
            print("Enter your first 3x3 matrix:")
            # initialize matrix 1
            user_matrix_1 = []

            # for loop for appending rows
            for _ in range(3):
                row = list(float(num) if "." in num else int(num) for num in input().split())
                user_matrix_1.append(row)
            matrix1 = np.asmatrix(user_matrix_1)

            # print matrix 1
            print("Your first 3x3 matrix is:")
            print_matrix(matrix1)

            print("Enter your second 3x3 matrix:")
            # initialize matrix 2
            user_matrix_2 = []

            # for loop for appending rows
            for _ in range(3):
                row = list(float(num) if "." in num else int(num) for num in input().split())
                user_matrix_2.append(row)
            matrix2 = np.asmatrix(user_matrix_2)

            # print matrix 2
            print("Your second 3x3 matrix is:")
            print_matrix(matrix2)

            # use matrices for operations
            matrix_menu(matrix1, matrix2)
            # break once selected operation complete
            break
        except ValueError:
            print("Please enter numeric values")

def validate_phone_zip():
    '''function to validate user phone # and zip code'''
    while True:
        try:
            phon_num = input("Enter your phone number (XXX-XXX-XXXX):\n")
            # use regex to validate format
            phon_formatted = bool(re.match(r"^\d{3}-\d{3}-\d{4}$", phon_num))
            if phon_formatted:
                # use regex to validate format
                zip_plus4 = input("Enter your zip code +4 (XXXXX-XXXX):\n")
                zip_formatted = bool(re.match(r"^\d{5}-\d{4}$", zip_plus4))
                if zip_formatted:
                    # go to handling matrices once phone/zip are validated
                    handle_matrix_input()
                    # break loop once operation is complete
                    break
                print("Your zip code is not in the correct format. Please try again\n")
            # prompts for starting over from phone number reentry
            else:
                print("Your phone number is not in the correct format. Please try again\n")
        except ValueError:
            print("Please enter valid input")

def main():
    '''Main function to handle initial user input'''
    # matrix1 = np.array([[9.55,4.46,5.58], [5.83,3.17,8.91], [7.25,4.02,1.65]])
    # matrix2 = np.array([[4.44,6.76,5.13], [1.70,6.73,1.50,], [7.75,1.90,9.79]])
    # matrix3 = np.array([[4,5,1],[8,6,3],[9,6,2]])
    # matrix4 = np.array([[2,4,2],[8,8,6],[1,9,4]])
    # add_result = np.add(matrix3, matrix4)
    # print_matrix(add_result)
    # matrix_transpose_mean(add_result)
    while True:
        try:
            print("******* Welcome to the Python Matrix Application *******")
            print("Do you want to play the Matrix Game?")
            user_input = input("Enter Y for Yes or N for No:\n")
            if user_input.lower() == "y":
                validate_phone_zip()
            elif user_input.lower() == "n":
                print("You've indicated you want to stop. Thanks and goodbye")
                sys.exit()
            else:
                print("Invalid choice, please enter Y or N\n")
        except ValueError:
            print("Please enter a letter\n")

# execute main function
if __name__ == "__main__":
    main()
