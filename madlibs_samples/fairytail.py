# create a madlib text for being completed


raw_text = ('Complete the following text with the words referenced: \n \
Once upon a time, a ______(noun1) was caught by a ______(adj1) dragon that lived in a tower far far away\n \
Despite of the risk, ______(name), a ______(adj2) and ______(adj3) horse rider ______(verb) to the rescue\n')

print(raw_text)

noun1 = input('Noun 1: ')
adj1 = input('Adjective 1: ')
name = input('Name: ')
adj2 = input('Adjective 2: ')
adj3 = input('Adjective 3: ')
verb = input('Verb: ')

completed_text = (f'Once upon a time, a {noun1} was caught by a {adj1} dragon that lived in a tower far far away\n \
Despite of the risk, {name}, a {adj2} and {adj3} horse rider {verb} to the rescue\n')

print(completed_text)