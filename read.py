data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1            #count = count + 1
		if count % 1000 == 0: #%為求餘數的意思,ex:7除3 = 2..1 取餘數就是1
			print(len(data))  #這個寫法等於每一千筆才印一次數量。
print('檔案讀取完了,總共有:', len(data), '筆資料。') #印出總共幾筆資料

sum_len = 0
for d in data:
	sum_len += len(d)  #sum_len = sum_len + len(d)

print('每筆留言平均長度是:', sum_len/len(data)) #留言總長度(sum_len) 除以 留言總筆數len(data)

# 篩選概念寫法:

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言小於100')
print(new[0])
print(new[1])

#篩選寫法II: 篩選出內容含有GOOD的留言。

#good = []
#for d in data:
#	if 'good' in d:
#		good.append(d)
#print('一共有', len(good), '筆留言提到good。'
#print(good[0])

good = [d for d in data if 'good' in d] #此為29~32行速寫法
print(good[0])