def prrr(tlist):
	for each in tlist:
		if isinstance(each,list):
			prrr(each)
		else:
			print(each)
