import sys
import os
import math
import datetime

DT = datetime.datetime

def process(beg = DT(2015,9,30), fir_mon = 11, total_money = 40000, total_month = 20):
	'''
	beg = 
	fir_mon = 11
	total_money = 40000
	total_month = 20
	'''
	if beg.month < 12:
		fir_year = beg.year
	else:
		fir_year = beg.year + 1
	
	mons = []
	pay_list = []
	
	idx = 0
	total_interest = 0
	
	while idx < total_month:
		cur_year = fir_year + (fir_mon + idx - 1) / 12		
		cur_mon = (fir_mon + idx - 1) % 12 + 1
		cur_tm = DT(cur_year, cur_mon, 28)
		
		dd = (cur_tm - beg).days
		
		#print(beg, cur_tm, dd)
		
		loc_interest = dd * (total_money - idx * 2000) * 0.0002
		total_interest += loc_interest
		
		pay = 2000 + loc_interest
		beg = cur_tm
		
		mons.append( cur_mon )
		pay_list.append(pay)
		
		idx += 1
	
	#print(mons)
	#print(pay_list)
	
	idx = 0
	while idx < len(pay_list):
		print( "%d month, pay = %f" % (mons[idx], pay_list[idx]) )
		idx += 1
	
	print(total_interest)
	
def main():
	
	if len(sys.argv) <= 1:
		sys.exit(1)
	
	process()
	
	
if __name__ == "__main__":
	main()