
CLEAR_CANVAS = {0: ['', '', '', '', '', '', '', '', '', ''],
         1: ['', '', '', '', '', '', '', '', '', ''],
         2: ['', '', '', '', '', '', '', '', '', ''],
         3: ['', '', '', '', '', '', '', '', '', ''],
         4: ['', '', '', '', '', '', '', '', '', ''],
         5: ['', '', '', '', '', '', '', '', '', ''],
         6: ['', '', '', '', '', '', '', '', '', ''],
         7: ['', '', '', '', '', '', '', '', '', ''],
         8: ['', '', '', '', '', '', '', '', '', ''],
         9: ['', '', '', '', '', '', '', '', '', ''],
}



def menu():
    """Prints list of options for the user"""

    print("A. Add shape")
    print("B. Clear all shapes")
    print("C. Change fill character")
    print("D. translate rectangle")
    print("E. Print shapes")
    print("F. Quit\n")

    option = input("Please choose an option:  ").upper()
    print("")

    return option

def clear_shape():
    """Clears canvas"""

    return CLEAR_CANVAS
    

def create_rectangle(current_canvas, start_x, start_y, end_x, end_y, fill_char):
    """Creates rectangle with given coordinates"""

    for column in range(start_y, end_y+1):
        for row in range(start_x, end_x+1):
            current_canvas[column][row] = fill_char
            
    return current_canvas
    
def render_canvas(current_canvas):
    """Prints canvas to terminal"""

    for key,values in current_canvas.items():
        print(" ".join(values))

def translate(current_canvas, axis, num, name):
    if axis == "y":
        start_y = dicts[name]["start_y"] + num
        end_y = dicts[name]["end_y"] + num
        current_canvas = create_rectangle(current_canvas, dicts[name]["start_x"], start_y, dicts[name]["end_x"], end_y, dicts[name]["fill_char"])
    else:
        start_x = dicts[name]["start_x"] + num
        end_x = dicts[name]["end_x"] + num
        current_canvas = create_rectangle(current_canvas, start_x, dicts[name]["start_y"], end_x, dicts[name]["end_y"], dicts[name]["fill_char"])
    
    return current_canvas
    
    
print("Welcome to ascii shape builder!")
option = ""
lst_names = []
dicts = {}
current_canvas = {0: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         1: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         2: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         3: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         4: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         5: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         6: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         7: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         8: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
         9: ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
}



while option != "F":
    option = menu()
    if option == "A":
        print("There is a canvas that holds 10x10 characters\n")
        start_x = int(input("X coordinate of the upper-left-hand corner of the shape: "))
        start_y = int(input("Y coordinate of the upper-left-hand corner of the rectangle: "))
        end_x = int(input("X coordinate of the lower-right-hand corner of the rectangle: "))
        end_y = int(input("Y coordinate of the lower-right-hand corner of the rectangle: "))
        fill_char = input("Character that should be used to draw the rectangle: ")
        name = input("Name your shape: \n").lower()
        lst_names.append(name)
        dicts[name] = {"start_x": start_x, "start_y": start_y, "end_x": end_x, "end_y": end_y, "fill_char": fill_char}
        current_canvas = create_rectangle(current_canvas, start_x, start_y, end_x, end_y, fill_char)
        

    if option == "B":
        current_canvas = clear_shape()


    if option == "C":
        print("Your shapes:")
        for name in lst_names:
            print(name)
        current_name = input("\nWhat shape do you want to fill character?: ").lower()
        new_char = input("What character do you want your shaped to be filled in: ")
        dicts[current_name]["fill_char"] = new_char
        current_canvas = create_rectangle(current_canvas, dicts[current_name]["start_x"], dicts[current_name]["start_y"], dicts[current_name]["end_x"], dicts[current_name]["end_y"], dicts[current_name]["fill_char"])


    if option == "D":
        print("Your shapes:")
        for name in lst_names:
            print(name)
        shape_name = input("Which shape would you like to translate?: ")
        axis = input("Which axis do you want to translate the shape on?: ").lower()
        num = int(input(f"How much would you like to move shape {shape_name}?: \n"))
        translate(current_canvas, axis, num, shape_name)



    if option == "E":
        render_canvas(current_canvas)

        




