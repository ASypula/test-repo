class Hello():
    
    def __init__(self):
        self.test="testing"
    
    def test_hello(self):
        print("Hi!")
        text=f"{self.test}, Hello World"
        return text