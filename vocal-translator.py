import sys, getopt


def translate_sentence(sentence):
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
    
    return sentence

def show_help():
    print('-f for the input file -o for the output file. To exit the program just type in "exit"')
    sys.exit(0)


output_file = ""
input_file = ""

opts, rest = getopt.getopt(sys.argv[1:], "hf:o:")

for opt, arg in opts:
    if opt == '-h':
        show_help();
    if opt == '-o':
        output = True
        output_file = arg
    if opt == '-f':
        input_file = arg



def save(translated_string):
    if(output_file != ""):
        ofile = open(output_file, 'w')
        ofile.write(translated)
    sys.exit(0)

if(input_file != ""):
    translated = ""
    ifile = open(input_file, 'r')
    translated_lines = []
    for line in ifile:
        translated += translate_sentence(line)
    save(translated)
    sys.exit(0)


while True:
    if(input_file == ""):
        translated = ""
        sentence = input("please insert sentence here: ")
        if(sentence == "exit"):
            sys.exit(0)
        translated = translate_sentence(sentence)
        print(translated)
        save(translated)
