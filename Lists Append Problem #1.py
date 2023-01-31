# List_Length is variable storing user input for the length of the list
List_Length = int(input("Enter length of List: "))

# input_values_List is declared as an empty list outside the for loop so that append() method work correctly
input_values_List = []

# for loop has looped till the List_Length (length of the list) so that correct total number of elements are stored in input_values_List (List name) 
for i in range(List_Length):
    print("Enter ",i+1, "element of list: ")

    # element variable taking user input element of list
    element = int(input())

    # input_values_List (List name) appending each element in list at each iteration using append() method
    input_values_List.append(element)

# Prints the whole List i.e. input_values_List
print("The final list is: ", input_values_List)