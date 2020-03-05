list = ['3,307.65','345','43,234.65']

for num in list:
	if ',' in num:
		nums = num.replace(',','')
		print(nums)
