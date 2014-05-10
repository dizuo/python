def proc_work_time(filename):
	fp = open(filename, "r")

	start_map = {}
	end_map = {}

	while True:
		line = fp.readline()

		if len(line) < 2:
			break		

		res = line.split(' ', 7)
		# print(res[4], res[5])

		datetag = res[4]
		timetag = res[5].split('\n', 2)[0]

		if start_map.__contains__(datetag) == False:
			start_map[datetag] = timetag
		else:
			end_map[datetag] = timetag

	fp.close()

	# 对无序的字典结果进行排序	
	end_map_sorted = sorted(end_map.items(), key=lambda d:d[0])
	for k,v in end_map_sorted:
		print(k, v)
                
	
	# print(end_map)
	# print(len(end_map))

proc_work_time('201404_work_time.txt')
