import sys
import pandas as pd
import numpy as np
import settings
from termcolor import colored,cprint



class RegressionTest:

	def __init__(self):
		self.base_url = settings.BASE_URL
		self.route_list = settings.ROUTE_LIST

	def save(self):
		for route in self.route_list:
			name = route[0]
			arguments = ''
			if len(route) > 1:
				arguments = arguments.join(route[1:])
			url = self.base_url+name+'?filter=min_year:1991,max_year:2018,'+arguments+'&format=csv'
			try:
				api_csv = pd.read_csv(url,float_precision='round_trip', encoding="utf-8-sig") #get from api
				api_csv.to_csv('route_result/'+name+'.csv', encoding="utf-8-sig") #save
				cprint("Saved "+name+" "+url,'green')
			except Exception as ex:
				cprint(str(ex)+" Not saved, a problem ocurred at "+name+" "+url,'red')
	
	def comparison(self):
		for route in self.route_list:
			name = route[0]
			arguments = ''
			if len(route) > 1:
				arguments = arguments.join(route[1:])
			url = self.base_url+name+'?filter=min_year:1991,max_year:2018,'+arguments+'&format=csv'
			try:
				api_csv = pd.read_csv(url,float_precision='round_trip', encoding="utf-8-sig") #get from api
				csv_route = pd.read_csv('route_result/'+name+'.csv', index_col=0, float_precision='round_trip', encoding="utf-8-sig") #get file
				#print(np.array_equal(api_csv,csv_route))
				if(csv_route.equals(api_csv)): #compare csv
					cprint(name+' OK!','green')
				else:
					cprint(name+' FAIL!','red')
					print(api_csv)
					print(csv_route)
					#api_csv.to_csv(name+'2.csv',encoding="utf-8-sig") 
					#csv_route.to_csv(name+'.csv',encoding="utf-8-sig") 
					ne = pd.concat([api_csv, csv_route]).drop_duplicates(keep=False)					
					print(ne)
			except Exception as ex:
					cprint(str(ex)+"\n"+name+' FAIL!','red')


def main(argv):
	try:
		if(argv[0] == '--save'):
			rt = RegressionTest()
			rt.save()
		elif(argv[0] == '--compare'):
			rt = RegressionTest()
			rt.comparison()
		else:
			print('usage: regression_test.py <command>')
			print('commands:')
			print('--save	   #save in file the current csv response of api')
			print('--compare  #compare the current csv response of api with last saved file of response')
	except:	
		print('usage: regression_test.py <command>')
		print('commands:')
		print('--save	   #save in file the current csv response of api')
		print('--compare  #compare the current csv response of api with last saved file of response')

if __name__ == "__main__":
	main(sys.argv[1:])
