# create a madlib text for being completed


raw_text = ('Complete the following text with the words referenced: \n \
One of my favorite sports is ______ (sport name). I consider it my favorite sport as it is ______(adj1) and ______(adj2).\
I always love ______(verb) the ______(sport name) team ______(name of team).\n')

print(raw_text)

sport_name = input('Sport name: ')
adj1 = input('Adjective 1: ')
adj2 = input('Adjective 2: ')
verb = input('Verb: ')
name_of_team = input('Name of team: ')

completed_text = (f'One of my favorite sports is {sport_name}. I consider it my favorite sport as it is {adj1} and {adj2}.\
I always love {verb} the {sport_name} team {name_of_team}).')
print(completed_text)