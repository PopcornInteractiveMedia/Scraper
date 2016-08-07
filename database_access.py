import pymysql
import pymysql.cursors
import json

class DB:
	pymysql = __import__('pymysql')
	cur = __import__('pymysql.cursors')
	def __init__(self):
		medialist = {};
		medialist["website"] = '';
		medialist["links"] = [];
		
		with open("json_feed.json", "r", encoding="utf-8") as f:
			medialist = json.load(f)
		print(medialist["website"]);
		
		conn= pymysql.connect(host='localhost',user='root',password='',db='testdb',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)
		a=conn.cursor()
		
		for media in medialist["links"]:
			try:
				a.execute("insert into mediaLinks values ('"+medialist["website"]+"','"+media+"',null,null)");
			except conn.Error as err:
				print("Something went wrong: {}".format(err))
				pass;
		a.close();