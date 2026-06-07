class StreamWriter:

    def __init__(self, file_path):
        self.file_path = file_path

    def open_stream(self):
        self.file = open(self.file_path, "w", encoding="utf-8")

    def close_stream(self):
        self.file.close()

    def writeline(self, line):
        try:
            self.file.write(line + "\n")
        except:
            self.file.close()