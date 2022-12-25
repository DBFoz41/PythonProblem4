"""

"""
import Interface as Inter
import file_writer as fw
                
class Drawing:

    def __init__(self):
        self.command = ""
        self.image = None
        self.rows = 0
        self.cols = 0
        self.row_range = None
        self.slice_start = 0
        self.slice_stop = 0
        self.temp_list = []
        self.target_color = ""
        self.write_string = ""
        self.file_name = ""
        self.output_file = None
   
    def command_router(self, command, image):
        self.image = image
        self.command = command
        if self.command[0] == "I":
            self.image = self.create_new_image(image)
        elif self.command[0] == "C":
            self.image = self.clear_image(image)
        elif self.command[0] == "L":
            self.image = self.color_the_pixel(image)
        elif self.command[0] == "V":
            self.image = self.draw_vert_segment(image)
        elif self.command[0] == "H":
            self.image = self.draw_horz_segment(image)
        elif self.command[0] == "K":
            self.image = self.draw_rectangle(image)
        elif self.command[0] == "F":
            self.image = self.fill_region(image)
        elif self.command[0] == "S":
            self.write_to_file(image)
        else:
            None
        return self.image

    def create_new_image(self, image):
        self.image = image
        if self.image == None:
            self.rows = int(self.command[4])
            self.cols = int(self.command[2])

            self.image = [["1" for i in range(self.cols)] for i in range(self.rows)]
            print(self.image)
        return self.image

    def clear_image(self, image):
        self.image = image
        if self.image == None:
            print("No image has been created, run command I M N")
        else:
            for index, row in enumerate(self.image):
                for index2, num in enumerate(row):
                    self.image[index][index2] = "0"
        print(self.image)
        return self.image

    def color_the_pixel(self, image):
        self.image = image
        if self.image == None:
            print("No image has been created, run command I M N")
        else:
            self.image[int(self.command[2])-1][int(self.command[4])-1] = self.command[6]
            print(self.image)
        return self.image

    def draw_vert_segment(self, image):
        self.image = image
        if self.image == None:
            print("No image has been created, run command I M N")
        else:
            self.row_range = range(int(self.command[4])-1, int(self.command[6]), 1)
            for j in self.row_range:
                self.image[j][int(self.command[2])-1] = self.command[8]
        print(self.image)
        return self.image

    def draw_horz_segment(self, image):
        self.temp_list = []
        self.image = image
        if self.image == None:
            print("No image has been created, run command I M N")
        else:
            self.slice_start = (int(self.command[2])-1)
            self.slice_stop = int(self.command[4])
            for i in range(self.slice_stop - self.slice_start):
                self.temp_list.append(self.command[8])
            self.image[int(self.command[6])-1][self.slice_start:self.slice_stop] = self.temp_list
        print(self.image)
        return self.image 

    def draw_rectangle(self, image):
        self.temp_list = []
        self.image = image
        if self.image == None:
            print("No image has been created, run command I M N")
        else:
            self.slice_start = (int(self.command[2])-1)
            self.slice_stop = int(self.command[8])
            for i in range(self.slice_stop - self.slice_start):
                self.temp_list.append(self.command[10])
            self.row_range = range(int(self.command[4])-1, int(self.command[8]), 1)
            for j in self.row_range:
                self.image[j][self.slice_start:self.slice_stop] = self.temp_list
            print(self.image)
            return self.image

    def fill_region(self, image):
        self.image = image
        if self.image == None:
            print("No image has been created, run command I M N")
        else:
            self.target_color = self.image[int(self.command[2])-1][int(self.command[4])-1]
            print(f"target {self.target_color}")
            for index, num_row in enumerate(self.image):
                for index2, color_val in enumerate(num_row):
                    if color_val == self.target_color:
                        self.image[index][index2] = self.command[6]
                    else:
                        None
            print(self.image)
            return self.image                 

    def write_to_file(self, image):
        self.write_string = ""
        self.file_name = self.command[2:]
        for num_row in self.image:
            self.write_string += " ".join(num_row)
            self.write_string += "\n"

        self.output_file = fw.FileWriter(file_name)
        self.output_file.file_write_all_str(self.write_string)
        



def execute_main():
    return_command = ""
    image = None
    problem4_interface = Inter.Interface()
    process_drawing = Drawing()
    while return_command != "X":
        return_command = problem4_interface.interface()
        if return_command != "X":
            image = process_drawing.command_router(return_command, image)
        else:
            continue




if __name__ == "__main__":
    execute_main()