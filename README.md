# Agent_Model_1
This is a agent based model. This model simulates agents, moving around a environment from either set starting point downloaded from xxx 
or random starting points. The Agents then move around the environment 'nibbling' at it and then storing this in the stores. The Agents are able
to share resources dependent on the location and how much they all ready have stored. The Resulting model is displayed on a GUI and a text file called 
'Agents' allocated each Agent a ID and shows the location 'x' and 'y' coordiantes and the amount of environment in there store. 

# # Licensing 
This software is licensined using a MIT License. More infromation is available in the license.txt file 


# # Files 
1) 'Model.py' - File to run the model, generate GUI and write files. 
2) 'agent_framework.py' - agent class containg all the fuctions relating the agents: move, eat, self, distance_between, share_with neighboroughs
3) 'wolf_framework.py' - wolf class containing all the functions relating to moving the wolf: move(2), wolf_distance, eat_agent 
4) 'in.txt' - This file is read to create the environment dataset. 


# # How to Run the Model:
1) Download all the files into the same folder
2) Open a command window in the same file path. (hold shift and right click)
3) Type: python model.py -h  This will show you the attributes you need to define: number of Agents, number of Wolfs, number of iterations and size of neighbourhood. 
4) Type: python model.py x x x x  and press enter  (where x is the the attributes above you want to select). For example: 'python model.py 100 10 100 20'
5) A GUI will appear titled model. Press run on the upper menu bar and then run model.
6) The Model will now run. 

# # Outputs 
1) A animation will apear on the GUI showing agents (white) and wolfs (grey) moving around the environment, and the evironment (background) changing colour as it is eaten.
2) 'Wolf.tx' A file showing the location of each wolf at intervals. 
3) 'agents.txt' a text file containg the 'id' of each agennt. For each iteration and each agent the x, and y, locations and amount in the store is shown. 

# # Testing 
Testing was completed throughout the process to make sure the model is running as required, predomintley through the use of print functions which have been commented out in the final version.
During running of the model two text files 'agents.txt' and 'wolf.txt' are produced for testing purposes.
'Agent.txt' shows for  each itteration the  agents  'id' number assocaited with, x and y location, and amount within the store is written in the text file. 
'wolf.text' shows for each itteration the wolfs 'id' and x and y locations.
The text files can be used to show the values are changing and the model is working.

# # Issues 
1) Wolf frame work is not yet complete. When a wolf would eat an agents, within the defined neigbourhood distance, eat agent is printed. The final out would then remove this agent from the model. 
2) End of model is printed twice

# # Future Development 
1) Completion of the wolf framework directive. When a wolf distance is equal to or less than neighbourhood to agent, this agent is delted and removed from the model. 
2) Better writing of the test files used for testing. For example sorting by 'id' smallest to largest and writing to a new line for each itteration. 
