import os
import blog
import unittest
import tempfile
from flask import Flask, url_for
class test_blog(unittest.TestCase):
	"""docstring for test_blog"""
	#def __init__(self, arg):
	#	super(test_blog, self).__init__()
	#	self.arg = arg
	def setUp(self):
		pass
	def test_config(self):
		app =  blog.app
		assert app.config['POST_DIR'] == 'posts'
	def test_slider(self):
		app =  blog.app
		with app.test_request_context():
			print url_for('index')
			print url_for('slide.all_slides')
			print url_for('slide.one_slide')
	def tearDown(self):
		pass
		
if __name__ == '__main__':
	unittest.main()