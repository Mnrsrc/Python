# -*- coding: utf-8 -*-
"""
Created on Tue May 21 15:44:39 2019

@author: Munire
"""

class Computer:
    def __init__(self,hdd,ram,displayCard,MonitorSize):
        self.harddisk=hdd
        self.ram=ram
        self.displayCard=displayCard
        self.monitor=MonitorSize

asus=Computer("1 TB",8,"Nvidia GeForce GT930MX","15.6 inch")
print("Display Card of Asus: " , asus.displayCard)