def sentence_maker(phrase):
    question = ("where","why","how","who","what","which")
    capitalized = phrase.capitalize()
    if phrase.startswith(question):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)
    

sentence = []

while True:
    user_input = input("Phrase:")
    if user_input == "!end":
        break
    else:
        sentence.append(sentence_maker(user_input))

print(" ".join(sentence))