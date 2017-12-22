import praw
import matplotlib.pyplot as plt	#generally you'll want to plot data as they come in so I always have this
import datetime
import numpy as np

reddit = praw.Reddit(client_id=******,
                     client_secret=******,
                     password=******,
                     user_agent=******,
                     username=******)

textFile = open('C:\Temp\whentoposttodataisbeautiful.txt', 'w')	#file to dump stats
start=1513346400				#of seconds at midnight starting December 15, 2017 (Central Time)
while(start > 1481810400):
	stop = start + 86399			#stop at the end of the current day
	for submission in reddit.subreddit('dataisbeautiful').submissions(start, stop):
		#print(submission.title)
		#print(submission.created)
		#print(submission.score)
		textFile.write(str(submission.created) + "\t" + str(datetime.datetime.fromtimestamp(submission.created).strftime('%Y-%m-%d %H:%M:%S')) + "\t" + str(submission.score) + "\r\n")	#write the day's info to the file
	start = start - 86400			#move to the next day
	print(datetime.datetime.fromtimestamp(start).strftime('%Y-%m-%d %H:%M:%S'))

textFile.close()				#dump data to file
