# -*- coding: utf-8 -*-
# Created by Adam Odell, MIT License. V.1.0
# This file contains the Wolf class and all the functions realting to moving the wolf and wolf-agent interactions. 

import random

class Wolf:  
    def __init__(self, environment, wolfs, agents): #self can only operate inside the agents data
        self.environment = environment
        self.x = random.randint(0,(len(self.environment[0]))-1)
        self.y = random.randint(0,(len(self.environment))-1)
        self.wolfs = wolfs
        self.store = 0 
        self.agents = agents
        
    
    def move2(self): 
     
        """
        This funcition is called to move the agent by 1 within the environment 

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

    def wolf_distance(self, agents):
        """
        

        This function calculates the distance between wolfs and agent
        ----------
        agents : list
            This functions takes the agent location list.

        Returns
        -------
        
            This function returns the distance between wolfs and agents

        """
        return (((self.x - agents.x)**2) + ((self.y - agents.y)**2))**0.5
    
    def eat_agent (self,neighbourhood,agents):
        """
        This Function determines if agents should be killed if within the neighborhood distance to wolfs 

        Parameters
        ----------
        neighbourhood : Interger
            Pre defined neighbourhood distace.
        agents : List
            List of all agents and paramters.

        Returns
        -------
        integert
            Returns the number 1 if the agent should be killed.

        """
        for wolfs in self.wolfs:
            distance = self.wolf_distance(wolfs)
            if distance < neighbourhood:
                self.store +=1 
                return 1
