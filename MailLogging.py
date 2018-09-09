import os
import json
import shutil

dir = os.getcwd()+'/logs'

class Debug:

	def createLog(self, dir=dir):
		if os.path.isdir(dir):
			shutil.rmtree(dir)
		os.mkdir(dir)

	def writeLog(self, name, content, directory='', extension='json'):
		contentType = type(content)
		directory = dir+'/'+directory+name+'.'+extension
		print(name, 'was added to', directory)
		file = open(directory, 'w')
		if contentType == dict or contentType == list:
			json.dump(content, file)
		else:
			file.write(content)

debug = Debug()