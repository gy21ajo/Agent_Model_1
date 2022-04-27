# Created by Adam Odell, MIT License. V.1.0
# This file contains the Class agents, and all the functions relating to moving, eating and sharing. 

import random

class Agent: 
    """This class contains function for moving the Agent, eating the environment, seeing distance between agents, and sharing with neighboroughs """        
    def __init__(self, environment, agents, y, x, ia, wolfs):#self can only operate inside the agents data
        self.environment = environment
        #set starting location
        self.y = y
        self.x = x
        self.id = ia
        self.agents = agents
        self.store = random.randint(0,30) # We'll come to this in a second.
        self.wolfs = wolfs
        
    def __str__(self):
        """
        This function creates an id for agents 

        Returns
        id of each agent 
        x = position
        y = position
        store = number of agents in  store 
        -------
        TYPE
            DESCRIPTION.

        """
        return "id = " + str(self.id) + ", x =" + str(self.x) + ", y =" + str(self.y) + ", store =" + str(self.store)
       
    def move(self): 
     
        """
        This funcition is called to move the agent in a random direction by 1

        Returns
        -------
        None.

        """
     
        if random.random() < 0.5:
            self.x = (self.x + 1) % len(self.environment[0])
        else:
            self.x = (self.x - 1) % len(self.environment[0])
    
        if random.random() < 0.5:
              self.y = (self.y + 1) % len(self.environment)
        else:
              self.y = (self.y - 1) % len(self.environment)
             
    def eat(self): 
        """
        This function will alows the agents to eat the environment. If there is 
        greater than 10 the agent will eat ten if there is less the agent will 
        eat whats left.

        Returns
        -------
        None.

        """
   
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
        else: 
            self.environment[self.y][self.x] += self.store 
            self.environment[self.y][self.x] = 0 
        if self.store >= 100:
            self.store -=100
            self.environment[self.y][self.x] += 100
            
            
    def distance_between(self, agents):
        """
        This function calculates the distance between agents

        Parameters
        ----------
        agents : List
            Full lits of agents.

        Returns
        -------
        TYPE
            This is the distance between other agents.

        """
        return (((self.x - agents.x)**2) + ((self.y - agents.y)**2))**0.5
    
    def share_with_neighbours(self, neighbourhood):
        """
        This function allows agents to a share there resources if they are in the neighboorhood distance. If there store is greater then 10 they will share, if it is less then they will steal of the agents resources

        Parameters
        ----------
        neighbourhood : Intiger
            The size of the neighborhood.

        Returns
        -------
        None.

        """
        for agents in self.agents:
            distance = self.distance_between(agents)
                
            if distance <= neighbourhood:
                if self.store >= 10:
                    sum = self.store + agents.store
                    ave = sum /2
                    self.store = ave
                    agents.store = ave
                    #print("sharing " + str(distance) + " " + str(ave))
                else:
                    sum = self.store + agents.store
                    self.store = sum
                    agents.store = 0
                
    # def wolf_distance(self, wolfs):
    #     return (((self.x - wolfs.x)**2) + ((self.y - wolfs.y)**2))**0.5
    
    # def eat_agent (self,neighbourhood,wolfs):
    #     for agents in self.agents:
    #         wolfdistance = self.wolf_distance(agents)
    #         if wolfdistance < neighbourhood:
    #             return 1
#test comment
