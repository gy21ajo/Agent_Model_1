# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:07:34 2022

@author: odell
"""

import random

class Wolf:  
    def __init__(self, environment, wolfs, agents): #self can only operate inside the agents data
        self.environment = environment
        self.x = random.randint(0,(len(self.environment[0]))-1)
        self.y = random.randint(0,(len(self.environment))-1)
        self.wolfs = wolfs
        self.store = 0 # We'll come to this in a second.
        self.agents = agents
        
    
    def move2(self): 
     
        """
        This funcition is called to move the agent 

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
        return (((self.x - agents.x)**2) + ((self.y - agents.y)**2))**0.5
    
    def eat_agent (self,neighbourhood,agents):
        for wolfs in self.wolfs:
            distance = self.wolf_distance(wolfs)
            if distance < neighbourhood:
                self.store +=1 
                return 1
  