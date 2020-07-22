from nltk.chat.util import Chat,reflections
pairs=[
    [
        r"What is your name?|who are you",
        ["My name is stella and I am a chatbot",]
    ],
    [
        r"How are you",
        ["I am fine and what about you"],
    ],
    [
        r"I am doing good",
        ["nice to hear that :)",]
    ],
    [
        r"hi|hey|hello",
        ["hello","hey there",]
    ],
    [
        r"quit",
        ["Thank u , See u again",]
    ],
]
def stella():
    pritn("THANK U < SEE YOU AGAIN:)")
chat=Chat(pairs,reflections)
chat.converse()
if __name__=="__main__":
    stella()