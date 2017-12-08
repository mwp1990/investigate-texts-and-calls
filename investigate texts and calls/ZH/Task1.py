"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."
"""
"""
First, catch phone numbers from the list.and store them in list
"""
texts_phone = []
for index in range(len(texts)):
	if index %3 != 2:
		texts_phone.append(texts[index])
calls_phone =[]
for index in range(len(calls)):
	if index %4 != 3:
		calls_phone.append(texts[index])

"""
Second,delet the repeat numbers from itself list.
"""
texts_phone_no_repeat = []
calls_phone_no_repeat = []

for phone in texts_phone:
	if phone not in texts_phone_no_repeat:
		texts_phone_no_repeat.append(phone)
for phone in calls_phone:
	if phone not in calls_phone_no_repeat:
		calls_phone_no_repeat.append(phone)

"""
Third,connect the texts_phone_no_repeat list and calls_phone_no_repeat list.and delete the repeat phone numbers
"""

for index in range(len(texts_phone_no_repeat)):
	if texts_phone_no_repeat[index] not in calls_phone_no_repeat:
		calls_phone_no_repeat.append(texts_phone_no_repeat[index])

sum_phone_numbers = len(calls_phone_no_repeat)

print ("There are {} different telephone numbers in the records.".format(sum_phone_numbers)
		