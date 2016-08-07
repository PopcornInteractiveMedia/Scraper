#!/usr/bin/python3.4
# -*-coding:UTF-8 -*
'''
Created on 01 08 2016
 
@author: Assamba 
'''
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 

from automate2 import * 
from database_access import * 

class Model(object):
    
    def __init__(self):
        
        self.__acquisition_on = False
		
    def get_state(self):
        return self.__acquisition_on
 
    def on(self):
        '''
        public method that start acquiring
        '''
        self.__acquisition_on = True
 
    def off(self):
        '''
         public method that stop acquiring
        '''
        self.__acquisition_on = False
 
    def toogle(self):
        '''
        swich the state of model.
        '''
        self.__acquisition_on = not self.__acquisition_on
 
    def pull_data(self, link):
        '''
        obtaining datas
        '''
        Automate(link);
        DB();
        return '--- <strong>Media links scraped successfully. See the database</strong> ---'
		