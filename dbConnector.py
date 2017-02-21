#!/usr/bin/env python
# Created by: Zac Smith
# 2017-2-15                   
# -------------------------- #

import mysql.connector
from functools import wraps


class Connector(object):
	"""This class handles the connection between back-end scripts and the database"""
	
	def __init__(self, usr="root", pw="1q2w3e4r", hosted="localhost", db="betaaggro"):
		self.connection = mysql.connector.connect(user=usr, password=pw, host=hosted, database=db)
		self.cursor = self.connection.cursor()
		self.response = None
		self.errors = None
		
	def commit(func):
		"""Decorator to commit after wrapped function"""
		def _decorator(self, *args, **kwargs):
			r = func(self, *args, **kwargs)
			self.connection.commit()
			print "Committed."
			return r
		return wraps(func)(_decorator)
		
		
	def close(self):
		"""Closes connection nicely"""
		self.connection.commit()
		self.cursor.close()
		self.connection.close()
		
		
	@commit
	def addYelpBusiness(self, dic):
		"""This makes an entry into the 'yelp' table and related tables"""
		business = ("INSERT INTO yelp "
							"(claimed, rating, ratingImage, reviewCount, name, ratingImageSmall, "
							"url, isClosed, phone, snippet, imageURL, snippetURL, uniqueName) "
							"VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")
							

		businessData = (dic.get("is_claimed", ""), dic.get("rating", ""), dic.get("rating_img_url", ""), dic.get("review_count", ""), 
									dic.get("name", ""), dic.get("rating_img_url_small", ""), dic.get("url", ""), dic.get("is_closed", ""), dic.get("phone", ""),
									dic.get("snippet_text", ""), dic.get("image_url", ""), dic.get("snippet_image_url", ""), dic.get("id", ""))			
									
		self.cursor.execute(business, businessData)
		
		
	@commit
	def addGoogleBusiness(self, dic):
		"""This makes an entry into the 'google' table and related tables"""
		pass
		
		
	@commit
	def addFacebookBusiness(self, dic):
		"""This makes an entry into the 'facebook' table and related tables"""
		pass
		
		
	@commit
	def addUser(self, dic):
		"""This adds a user to the 'user' table and related tables"""
		pass
		
		
	def select(self, table, criteria):
		"""This will select from table WHERE K = V from criteria"""
		pass
	
	
	@commit
	def update(self, table, dic, criteria):
		"""This will update a specific table using Key, Value pairs in dic"""
		pass
		
		
	@commit
	def delete(self, table, criteria):
		"""This will delete a database entry based on criteria"""
		pass
		
		
	

		
	
			
	