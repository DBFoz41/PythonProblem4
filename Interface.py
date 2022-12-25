"""

"""

class Interface:

    def __init__(self):
        self.selection = ""
        self.command_menu = f"""I M N:   Create new image M cols and N rows all colored white
C:          Clear
L X Y C:    Color pixel X,Y in color C
V X Y1 Y2 C: Draw vertical segment of color C in col X between rows Y1 and Y2 inclusive
H X1 X2 Y C: Draw horizontal segment of color C in th row Y, between cols X1 and X2 inclusive
K X1 Y1 X2 Y2 C: Draw filled rectangle of color C, where X1,Y1 is upper left and X2,Y2 is lower right
F X Y C:     Fill the region with color C where the region touches X,Y and is the same color
S Name:      Write to file
X:          Quit"""

    def interface(self):
        
        valid_entry = {"C":"valid","I":"valid", "L":"valid", "V":"valid", "H":"valid", "K":"valid", "F":"valid", "S":"valid", "X":"valid", "M":"valid"}
        while True:
            self.selection = ""
            self.selection = input("Select a command or enter M to see the menu:")
            try:
                valid_entry[self.selection[0]] == "valid"
            except KeyError:
                print("Please make a valid selection, enter M to see menu")
                continue
            if self.selection == "M":
                print(self.command_menu)
            elif self.selection == "X":
                print("Exiting")
                return self.selection
                break
            elif valid_entry[self.selection[0]] == "valid":
                print("valid selction")
                return self.selection
            else:
                print("Please make a valid selection, enter M to see menu")