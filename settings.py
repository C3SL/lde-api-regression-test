'''Settings used by LDE regression test'''

'''URL API to test'''
BASE_URL = 'https://simcaq.c3sl.ufpr.br/api/v1/'

'''List of all base routes available to test'''
BASE_ROUTE_LIST = [
		['class'],
		['enrollment'],
		['enrollment', '&dims=location'],
		['enrollment', '&dims=rural_location'],
		['enrollment', '&dims=school_year'],
		['enrollment', '&dims=educational_level'],
		['enrollment', '&dims=adm_dependency'],
		['enrollment', '&dims=gender'],
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
		#['infrastructure'],
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

'''SIMCAQ ROUTE LIST'''
SIMCAQ_ROUTE_LIST = [
	['enrollment','&dims=school_year'],
	['enrollment','&dims=school_year,adm_dependency_detailed'],
	['enrollment','&dims=school_year,location'],
	['enrollment_projection'] ,
	['teacher', 'adm_dependency:[\"1\",\"2\",\"3\"],education_type:[\"3\",\"4\",\"5\",\"6\",\"7\",\"8\",\"9\",\"10\",\"11\",\"12\"]&dims=education_type'],
	#['classroom_count','adm_dependency:[\"1\",\"2\",\"3\"]'],
	#['enrollment','adm_dependency:[\"1\",\"2\",\"3\"]&dims=school,location'],
	['daily_charge_amount','adm_dependency:[\"1\",\"2\",\"3\"],education_level_mod:[\"1\",\"2\",\"4\",\"5\",\"6\",\"8\",\"9\"],integral_time:[\"0\"],period:[\"1\",\"2\"]&dims=education_level_short'],
	['daily_charge_amount','adm_dependency:[\"1\",\"2\",\"3\"],education_level_mod:[\"1\",\"2\",\"4\",\"5\",\"6\",\"8\",\"9\"],integral_time:[\"0\"],period:[\"3\"]&dims=education_level_short'],
	['daily_charge_amount','adm_dependency:[\"1\",\"2\",\"3\"],education_level_mod:[\"1\",\"2\",\"4\",\"5\",\"6\",\"8\",\"9\"],integral_time:[\"1\"]&dims=education_level_short'],
	['enrollment','adm_dependency[\"1\",\"2\",\"3\"],education_level_mod:[\"1\",\"2\",\"4\",\"5\",\"6\",\"8\",\"9\"],integral_time:[\"1\"]&dims=education_level_short'],
	['enrollment','adm_dependency:[\"1\",\"2\",\"3\"]&dims=education_level_short'],
	['enrollment','integral_time:\"true\",education_level_short:[\"1\",\"2\",\"3\",\"4\",\"5\"],adm_dependency:[\"1\",\"2\",\"3\"]&education_level_short,integral_time'],
	['class_count/count','adm_dependency:[\"1\",\"2\",\"3\"],education_level_short:[\"1\",\"2\",\"3\",\"4\",\"5\",\"6\"]&dims=education_level_short,location'],
	['teacher','adm_dependency:[\"1\",\"2\",\"3\"]'],
	['auxiliar','adm_dependency:[\"1\",\"2\",\"3\"],education_level_mod:[\"1\",\"2\",\"4\",\"5\",\"6\",\"8\",\"9\"]'],
	['teacher','adm_dependency:[\"1\",\"2\",\"3\"],education_type:[\"3\",\"4\",\"5\",\"6\",\"7\",\"8\",\"9\",\"10\",\"11\",\"12\"]&dims=education_type'],
	['teacher','adm_dependency:[\"1\",\"2\",\"3\"],education_type:[\"3\",\"4\",\"5\",\"6\",\"7\",\"8\",\"9\",\"10\",\"11\",\"12\"]&dims=education_type'],
	['employees','adm_dependency:[\"1\",\"2\",\"3\"]'],
	['school/count','adm_dependency:[\"1\",\"2\",\"3\"],school_building:\"true\"'],
	['school/count','adm_dependency:[\"1\",\"2\",\"3\"],school_building:\"true\"&dims=location'],
	['school/count','adm_dependency:[\"1\",\"2\",\"3\"],school_building:\"false\"'],
	['school_infrastructure','adm_dependency:[\"1\",\"2\",\"3\"]&dims=location'],
	['cub','min_month:\"10\",max_month\"10\"'],
	#### Segundo Relatorio
	['population', '&dims=state'],
	['pibpercapita', '&dims=state'],
	['school/count', '&dims=adm_dependency_detailed,location'],
	['enrollment', '&dims=adm_dependency_detailed,location'],
	['class','adm_dependency:[\"1\",\"2\",\"3\"]'],
	['auxiliar','adm_dependency:[\"1\",\"2\",\"3\"],education_level_mod:[\"1\",\"2\",\"4\",\"5\",\"6\",\"8\",\"9\"]'],
	['classroom',',adm_dependency:[\"1\",\"2\",\"3\"]'],
	['school/count','adm_dependency:[1,2,3],school_building:true&dims=location'],
	['school/count','adm_dependency:[1,2,3],school_building:true'],
	['school/count','adm_dependency:[1,2,3],school_building:false'],
	['cub','min_month:\"10\",max_month:\"10\"&dims=state'],
	['employees','adm_dependency:[\"1\",\"2\",\"3\"]'],
	['enrollment','&dims=school_year'],
	['enrollment','&dims=school_year,adm_dependency_detailed'],
	['enrollment','&dims=school_year,location'],
	['enrollment_projection',''],
	['financial','sphere_adm:[\"1\",\"2\"],financial_data:[\"1\",\"3\"]'],
	['school_infrastructure','adm_dependency:[1,2,3]&dims=location'],
	['teacher',',adm_dependency:[\"1\",\"2\",\"3\"],education_type:[\"3\",\"4\",\"5\",\"6\",\"7\",\"8\",\"9\",\"10\",\"11\",\"12\"]&dims=education_type'],
	['teacher',',adm_dependency:[\"1\",\"2\",\"3\"]']

]

'''LDE ROUTE LIST'''
LDE_ROUTE_LIST = []
