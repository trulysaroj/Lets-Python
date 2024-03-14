
# extending built in type in class

class Text(str):
    # extending duplicate methods in str
    def duplicate(self):
        return self + self


text = Text('Python')
print(text.lower())  # python
print(text.duplicate())  # PythonPython
