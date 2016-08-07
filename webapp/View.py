#!/usr/bin/python3.4
# -*-coding:UTF-8 -*
'''
Created on 01 08 2016
 
@author: Assamba 
'''

class View(object):
    '''
    Cette classe contient des ressources de la partie Vue du
    design pattern MVC
    '''
 
    HTML_TEMPLATE = {'beginning': '''
        <!DOCTYPE html>
        <html>
            <head>
                <meta charset=utf-8 />
                <title>Web media Scraper!</title>
            </head>
            <body>
			<h2>Hello World! Welcome to our intelligent scraper!</h2>
        ''',
        'end': '''
            </body>
        </html>''',
        'header': 'Content-type: text/html\r\n\r\n'}
 
    HTML_WIDGETS = {'get_data':'''
        <form method="post" action="">
			<label> enter the link to scrap: </label>
			<input type="text" name="link"/>
			<input type="submit" value="start scraping" name="get-data"/>
		</form>''',
		
        'acquisition_off':'''
        <form method="post" action="index.py">
            <input type="submit" value="Stop scraping" name="set-off" />
        </form>''',
		
       }