'''Settings used by LDE regression test'''

'''URL API to test'''
BASE_URL = 'https://simcaq.c3sl.ufpr.br/api/v1/'

'''List of all routes available to test'''
ROUTE_LIST = [
		['class'],
		['enrollment'],
		['state'],
		['region'],
		['city'],
		['school','id:11000023'],
		['classroom'],
		['teacher'],
		['idhm', '&dims=state'],
		['idhmr','&dims=state'],
		['idhml','&dims=state'],
		['idhme', '&dims=state'],
		['pibpercapita'],
		['population'],
		['rate_school','&dims=age_range'],
		['gloss_enrollment_ratio','&dims=education_level_basic'],
		['liquid_enrollment_ratio','&dims=education_level_basic'],
		['education_years'],
		['infrastructure'],
		#['school_infrastructure'],
		#['siope'],
		['out_of_school'],
		#['class_count','&dims=education_level_mod'],
		['daily_charge_amount','integral_time:\"1\"'],
		['transport'],
		['cub'],
		['auxiliar'],
		#'portal_mec_inep',
		['enrollment_projection'],
		['employees'],
		['financial'],
		['university_enrollment'],
		#['university'],
		['university_teacher'],
		['course_count']
]
