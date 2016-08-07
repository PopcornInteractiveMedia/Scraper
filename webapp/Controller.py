#!/usr/bin/python3.4
# -*-coding:UTF-8 -*
'''
Created on 01 08 2016
 
@author: Assamba 
'''

import pickle
 
class Controller(object):
    '''
    classdocs
    '''
 
    def __init__(self, model):
        '''
        Constructeur
        @param model: medel reference
        @param view: View reference
        '''
        # model reference
        self.__model = model
 
    def get_model(self):
        return self.__model
 
    def switch_on_acquisition(self):
        '''
        public method that start acquiring
        '''
        print('Controller => start acquiring')
        self.__model.on()
        self.save_changes()
 
    def switch_off_acquisition(self):
        '''
        public method that stop acquiring
        '''
        print('Controller => stop acquiring')
        self.__model.off()
        self.save_changes()
 
    def save_changes(self):
        '''
        serialization of Controller so that cgi could no it instance
        '''
        with open('controller.pickle', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
 
    def get_data(self, link):
        '''
        get data from url
        '''
        return self.__model.pull_data(link)