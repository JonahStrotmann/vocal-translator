sentence = input("please insert sentence here: ")

sentence = sentence.replace("o", "oob") 
sentence = sentence.replace("a", "oob") 
sentence = sentence.replace("e", "oob") 
sentence = sentence.replace("i", "oob") 
sentence = sentence.replace("u", "oob") 

sentence = sentence.replace("O", "oob") 
sentence = sentence.replace("A", "oob") 
sentence = sentence.replace("E", "oob") 
sentence = sentence.replace("I", "oob") 
sentence = sentence.replace("U", "oob") 

sentence = sentence.replace("ö", "ööb") 
sentence = sentence.replace("ä", "ööb") 
sentence = sentence.replace("ü", "ööb")

sentence = sentence.replace("Ö", "ööb") 
sentence = sentence.replace("Ä", "ööb") 
sentence = sentence.replace("Ü", "ööb")

print(sentence)

input('Press enter to exit')