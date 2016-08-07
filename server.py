#!/usr/bin/python3.4
# -*-coding:UTF-8 -*
'''
Created on 01 08 2016
 
@author: Assamba 
'''

from http.server import HTTPServer, CGIHTTPRequestHandler
from webapp import Model, Controller
import pickle

model = Model.Model()
controller = Controller.Controller(model)

with open('controller.pickle', 'wb') as f:
    pickle.dump(controller, f, pickle.HIGHEST_PROTOCOL)

# Port du serveur http
port = 8081
# Allocation de l'objet de gestion du serveur
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
 
# On lance le serveur indéfiniement
print('Lancement du serveur http sur le port: ' + str(httpd.server_port))
httpd.serve_forever()