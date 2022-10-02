import os


class StringOutputClass:
    def __init__(self):
        self.text_file = open('dirStructOutput.txt', 'w')
        self.current_file_path = os.path.dirname(os.path.abspath(__file__))

    def output_a_string(self, output_string):
        print(output_string, end="")
        self.text_file.write(output_string)

    def close_file(self):
        self.text_file.close()