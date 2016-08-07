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

from webapp.View import View
import cgi
import pickle

message = ''

with open('controller.pickle', 'rb') as f:
    controller = pickle.load(f)
	
#object to use with forms
form = cgi.FieldStorage()
 
if form.getvalue('set-on') != None:
    message += 'browser asked to start retrieving <br />'
    controller.switch_on_acquisition()
 
if form.getvalue('set-off') != None:
    message += 'browser asked to stop processing <br />'
    controller.switch_off_acquisition()
 
if form.getvalue('get-data') != None:
    #message += 'browser asked to get data<br />'
    message += controller.get_data(form.getvalue('link'))
	
if controller.get_model().get_state() == True:
    message += '<div class="acq-on"></div><div class="acq-message">getting datas...</div> <br />'
else:
    message += '<div class="acq-off"></div><div class="acq-message">waiting...</div> <br />'
 
print(View.HTML_TEMPLATE['header'])

print(View.HTML_TEMPLATE['beginning'])
 
print(View.HTML_WIDGETS['get_data'])
print('<br />')
print(View.HTML_WIDGETS['acquisition_off'])
print('<br />')
 
# Messages
print(message)
 
print(View.HTML_TEMPLATE['end'])
