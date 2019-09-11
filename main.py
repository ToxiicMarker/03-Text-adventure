import sys, logging, json

#check to make sure we are running the right version of Python
version = (3,7)
assert sys.version_info >= version, "This script requires at least Python {0}.{1}".format(version[0],version[1])

#turn on logging, in case we have to leave ourselves debugging messages
logging.basicConfig(format='[%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

'''Notes
.upper()
.strip()
.lower()

game
game['verbs']
game['rooms']
              ['WHOUS']
              ['NHOUS']
                       ['name']
                       ['description']
                       ['exits']
                       ['inventory']

'''

def render(game,current):
    '''Display the current location'''
    print ('You are at the' + game['rooms'][current]['name'])
    print (game['rooms']['current']['desc'])
    return True

def update(game,current:response):
    '''Update our location, if possible, etc'''
    for e in game['rooms'][current]['exits']:
      if response == e['verb']:
        current = e['target']

    return True

def check_input():
    '''Get user input'''
    response = input('What would you like to do?')
    return response




def main():
    game = {} #empty dictionary
    with open('zork.json') as json_file:
        game = json.load(json_file)
    # Your game goes here!

    current = 'WHOUS'

quit = False
while not quit:
    #render
  render()
    #check player input
  check_input()
    #update
  update()
 



#if we are running this from the command line, run main
if __name__ == '__main__':
	main()