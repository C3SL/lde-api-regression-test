# Copyright (C) 2016 Centro de Computacao Cientifica e Software Livre
# Departamento de Informatica - Universidade Federal do Parana - C3SL/UFPR

# This file is part of simcaq-node.

# simcaq-node is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# simcaq-node is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with simcaq-node.  If not, see <https://www.gnu.org/licenses/>.

import sys
import pandas as pd
import numpy as np
import settings
from termcolor import colored,cprint



class RegressionTest:

	def __init__(self, route):
		self.base_url = settings.BASE_URL
		self.route_list = settings.BASE_ROUTE_LIST+settings.SIMCAQ_ROUTE_LIST
		if len(route) > 0:
			self.route_list = filter(lambda k: route[0] in k, self.route_list)

	def save(self):
		for route in self.route_list:
			name = route[0]
			arguments = ''
			if len(route) > 1:
				arguments = arguments.join(route[1:])
			file_name = name+arguments
			url = self.base_url+name+'?filter=min_year:1991,max_year:2018,'+arguments+'&format=csv'
			try:
				api_csv = pd.read_csv(url,float_precision='round_trip', encoding="utf-8-sig") #get from api
				api_csv.to_csv('route_result/'+file_name+'.csv', encoding="utf-8-sig") #save
				cprint("Saved "+name+" with arguments: ["+arguments+"] URL: <"+url+">",'green')
			except Exception as ex:
				cprint(str(ex)+" Not saved, a problem ocurred at "+name+" "+url,'red')
	
	def comparison(self):
		fail = 0
		for route in self.route_list:
			name = route[0]
			arguments = ''
			if len(route) > 1:
				arguments = arguments.join(route[1:])
			file_name = name+arguments
			url = self.base_url+name+'?filter=min_year:1991,max_year:2018,'+arguments+'&format=csv'
			try:
				api_csv = pd.read_csv(url,float_precision='round_trip', encoding="utf-8-sig") #get from api
				csv_route = pd.read_csv('route_result/'+file_name+'.csv', index_col=0, float_precision='round_trip', encoding="utf-8-sig") #get file
				#print(np.array_equal(api_csv,csv_route))
				if(csv_route.equals(api_csv)): #compare csv
					cprint(name+' OK!','green')
				else:
					fail+=1
					cprint(name+' FAIL!','red')
					print(api_csv)
					print(csv_route)
					#api_csv.to_csv(name+'2.csv',encoding="utf-8-sig") 
					#csv_route.to_csv(name+'.csv',encoding="utf-8-sig") 
					#ne = pd.concat([api_csv, csv_route]).drop_duplicates(keep=False)					
					#print(ne)
			except Exception as ex:
					cprint(str(ex)+"\n"+name+' FAIL!','red')
					fail+=1
		cprint('TOTAL FAIL: '+str(fail),'red')


def main(argv):
	try:
		if(argv[0] == '--save'):
			rt = RegressionTest(argv[1:])
			rt.save()
		elif(argv[0] == '--compare'):
			rt = RegressionTest(argv[1:])
			rt.comparison()
		else:
			print('usage: regression_test.py <command>')
			print('commands:')
			print('--save	   #save in file the current csv response of api')
			print('--compare  #compare the current csv response of api with last saved file of response')
			print('[route_name]  #optional to test or save specific routes')
#	except:	
	except Exception as ex:
		cprint(str(ex)+"\n FAIL!",'red')
		print('usage: regression_test.py <command>')
		print('commands:')
		print('--save	   #save in file the current csv response of api')
		print('--compare  #compare the current csv response of api with last saved file of response')
		print('[route_name]  #optional to test or save specific routes')

if __name__ == "__main__":
	main(sys.argv[1:])
