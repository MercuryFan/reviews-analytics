data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1            #count = count + 1
		if count % 1000 == 0: #%為求餘數的意思,ex:7除3 = 2..1 取餘數就是1
			print(len(data))  #這個寫法等於每一千筆才印一次數量。
print(len(data)) #印出總共幾筆資料
print(data[0])
print('----------------')
print(data[1])
