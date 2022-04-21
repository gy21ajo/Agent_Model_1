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


# # How to Run the Model:
1) Download all the files into the same folder
2) Open a command window in the same file 
3) Type: python model.py -h  This will show you the atributs you need to define: Number of Agents, number of Wolfs, Number of iterations and Size of Environment 
4) Type: python model.py x x x x       and press enter (where X is the the values you want to select) 
5) A GUI will appear, press run, then run model
6) The Model will now run. 

# # Outputs 
1) 'agents.txt' a text file containg the 'id' of each agennt. For each iteration and each agent the x, and y, locations and amount in the store is shown. 
2) A animation of the agents moving around the environment and 

# # Testing 
Two files were produced during testing: 
  agents.txt
  wolf.txt
For each itteration the  agents  'id' number assocaited with, x and y location, and amount within the store is written in the text file. This shows that model is workig if the values are changing.  


# # Issues 
1) Wolf frame work is not yet complete. When a wolf would eat an agents, within the defined neigbourhood distance, eat agent is printed
2) End of model is printed multiple times. 

# # Future Development 
1) 
