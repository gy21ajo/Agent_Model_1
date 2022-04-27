# -*- coding: utf-8 -*-
#Agent Based Model, This file runs the model.

import matplotlib
matplotlib.use('TkAgg')
import random
import matplotlib.pyplot
import agentframework
import wolfframework
import matplotlib.animation
import argparse 
import tkinter
import csv
import requests
import bs4


#importy and x location data from the internet 
r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text 
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
#print(td_ys)
#print(td_xs) 

#Running the Animation
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw() 

#create figure which appears in the animation window 
fig = matplotlib.pyplot.figure(figsize=(7,7))
ax = fig.add_axes([0, 0, 1, 1])
#ax.set_autoscale_on(False)


#Create GUI using tkinter.TK()
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root) #build menu 
root.config(menu=menu_bar) #configure to window just built
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu) #sub menu
model_menu.add_command(label="Run model", command=run) #run function will run
 #wait for interactiom
  



#this mean you can run it from the command line inputting valuable variables 
parser = argparse.ArgumentParser(description='Sheep Eating environment model')
parser.add_argument('num_of_agents', type=int, help='Number of agents or individuals')
parser.add_argument('num_of_wolf', type=int, help='Number of agents or individuals')
parser.add_argument('num_of_iterations', type=int, help='How many times the agents will move')
parser.add_argument('neighbourhood', type=int, help='Size of neighbourhood')
args = parser.parse_args()

#create environment list
environment = []


# #opening and readinf environment file and appending into the environment file 
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:	
    rowlist = []
    for value in row:
        rowlist.append(value)			# A list of rows
    environment.append(rowlist)				# A list of value				
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.


#setting number of agents 
num_of_agents = args.num_of_agents
num_of_iterations = args.num_of_iterations
neighbourhood = args.neighbourhood
num_of_wolfs = args.num_of_wolf

#create agents and wolfs list
agents = []
wolfs = []

#Make the agents using values from the internet or random if there are more agents then values
for i in range(num_of_agents):
    if  num_of_agents <= 100:
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
    else: 
        y = random.randint(0,(len(environment))-1)
        x = random.randint(0,(len(environment[0]))-1)
    agents.append(agentframework.Agent(environment,agents,y,x,i,wolfs))

#Make the wolfs using random location
for w in range(num_of_wolfs):
    wolfs.append(wolfframework.Wolf(environment,wolfs,agents))
    


# open file to record the location and stores of agents and wolf
f3 = open('agents.txt', 'w', newline='') 
f4 = open('wolfs.txt','w',newline='')
carry_on = True

def update(frame_number):
    
    fig.clear()
    global carry_on

#move the agents and eat the environmentfor j in range(num_of_iterations) and write file:
    for i in range(len(agents)):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood) 
        f3.write(str(agents[i]))
        f3.flush()
#move the wolf around and get wolfs to display when they might 'Eat'
    for w in range(num_of_wolfs):
        wolfs[w].move2()
        kill = wolfs[w].eat_agent(neighbourhood,agents)
        if kill == 1:
            f4.write('Eat')
            f4.flush()
        random.shuffle(wolfs)

    
    if random.random() < 0.1:
        cary_on = False
        print('stopping condition')
   
    #create animation plot
    matplotlib.pyplot.xlim(0, len(environment[0]))
    matplotlib.pyplot.ylim(0, len(environment))
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y, color="WHITE")
        #print(agents[i].x,agents[i].y)
        #print(agents[i].store)
    for w in range(num_of_wolfs):
        matplotlib.pyplot.scatter(wolfs[w].x,wolfs[w].y, color="GREY")
  
    
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1


tkinter.mainloop() 
f3.close()
f4.close()


