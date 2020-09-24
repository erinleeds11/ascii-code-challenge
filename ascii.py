
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

def translate(current_canvas, axis, num, name, fill_char_pass):
    """Translates shape on x or y axis"""

    if axis == "y":
        startY = dicts[name]["start_y"] + num
        endY = dicts[name]["end_y"] + num
        if num > 0:
            for column in range(dicts[name]["start_y"], dicts[name]["end_y"]+num+1):
                for row in range(dicts[name]["start_x"], dicts[name]["end_x"] +1):
                    current_canvas[column][row] = "."
        else:
            for column in range(dicts[name]["end_y"]+num, dicts[name]["end_y"]+1):
                for row in range(dicts[name]["start_x"], dicts[name]["end_x"] + 1):
                    current_canvas[column][row] = "."
        current_canvas = create_rectangle(current_canvas, dicts[name]["start_x"], startY, dicts[name]["end_x"], endY, dicts[name]["fill_char"])
    else:
        startX = dicts[name]["start_x"] + num
        endX = dicts[name]["end_x"] + num
        if num > 0:
            for column in range(dicts[name]["start_y"], dicts[name]["end_y"]+1):
                for row in range(dicts[name]["start_x"], dicts[name]["end_x"] + num+1):
                    current_canvas[column][row] = "."
        else:
            for column in range(dicts[name]["start_y"], dicts[name]["end_y"]+1):
                for row in range(dicts[name]["end_x"] + num, dicts[name]["end_x"] + 1):
                    current_canvas[column][row] = "."
        current_canvas = create_rectangle(current_canvas, startX, dicts[name]["start_y"], endX, dicts[name]["end_y"], dicts[name]["fill_char"])
    
    return current_canvas
    
    
print("Welcome to ascii shape builder!")
option = ""
lst_names = []
dicts = {}
current_canvas = {0: ['', '', '', '', '', '', '', '', '', ''],
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


while option != "F":
    option = menu()
    if option == "A":
        print("There is a canvas that holds 10x10 characters\n")
        start_x = int(input("X coordinate of the upper-left-hand corner of the shape (0-9): "))
        start_y = int(input("Y coordinate of the upper-left-hand corner of the rectangle (0-9): "))
        end_x = int(input("X coordinate of the lower-right-hand corner of the rectangle (0-9): "))
        end_y = int(input("Y coordinate of the lower-right-hand corner of the rectangle (0-9): "))
        if (start_x >= 0 and start_x <=9) and (start_y >= 0 and start_y <=9) and (end_x >= 0 and end_x <=9) and (end_y >= 0 and end_y <=9): 
            fill_char = input("Character that should be used to draw the rectangle: ")
            name = input("Name your shape: ").lower()
            print("")
            lst_names.append(name)
            dicts[name] = {"start_x": start_x, "start_y": start_y, "end_x": end_x, "end_y": end_y, "fill_char": fill_char}
            current_canvas = create_rectangle(current_canvas, start_x, start_y, end_x, end_y, fill_char)
        else:
            print("\nInvalid coordinates\n")
        
    if option == "B":
        current_canvas = clear_shape()

    if option == "C":
        print("Your shapes:")
        for name in lst_names:
            print(name)
        current_name = input("\nWhat shape do you want to change fill character?: ").lower()
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
        fill_char_pass = dicts[shape_name]["start_x"]
        translate(current_canvas, axis, num, shape_name, fill_char_pass)



    if option == "E":
        render_canvas(current_canvas)

        




