# -*- coding: UTF-8 -*-
from __future__ import unicode_literals
import sys,os
sys.path.append("../")
from whoosh.index import create_in,open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
import chardet
from jieba.analyse import ChineseAnalyzer

def build_index(cDir):
	analyzer = ChineseAnalyzer()

	schema = Schema(title=TEXT(stored=True), path=ID(stored=True), content=TEXT(stored=True, analyzer=analyzer))
	if not os.path.exists("tmp"):
	    os.mkdir("tmp")

	ix = create_in("tmp", schema) # for create new index
	#ix = open_dir("tmp") # for read only
	writer = ix.writer()

	for dirpath, dirnames, filenames in os.walk(cDir):
	    for searchFile in filenames:
	    	if searchFile[-3:] == '.md':
	    		print 'now ', searchFile, cDir + "/" + searchFile

		        with open(cDir + "/" + searchFile) as f:
		            print chardet.detect(str(dirpath + "/" + searchFile))
		            writer.add_document(title=searchFile.decode("utf-8"), path=str(dirpath + "/" + searchFile).decode('utf-8'), content=f.read().decode("utf-8"))
		       

	writer.commit()
