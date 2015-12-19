def my(mis):

	if mis==1 or mis==2 or mis==12:
		print(str(mis) +' zima')
	elif 3<=mis<=5:
		print(str(mis) +' vesna')
	elif  6<=mis<=8:
		print(str(mis) +' lito')
	else:
		print(str(mis) +' osin')
my(5)