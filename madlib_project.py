with open ("story.txt","r") as f:
    story = f.read()

words =set()
start_word = -1

target_start = "<"
target_end = ">"
for i ,char in enumerate(story):
    if char == target_start:
        start_word = 1

    if char == target_end and start_word != 1:
        word = story [start_word :i +1]
        word.add(word)
        sart_word = -1
    
answer ={}

for word in words:
    answer = input("enter a  word for " + word + ":")
    answer[word] = answer

for word in  words:
    story = story.replace(word , answer[word])

print(story)