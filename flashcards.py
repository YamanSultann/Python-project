class flashcard:
    def __init__(self,word,meaning):
        self.word = word
        self.meaning = meaning
    
    def __str__(self):
        return self.word+'('+self.meaning+')'
    
flass = []
print("Welcome to flashcard application")

while(True):
    word = input("Enter the name you want to add to flashcard")
    meaning = input("Enter the meaning of the word")
    