import praw
import threading
import re

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("sandboxtest")

file = open('palindromes-results.txt', 'w+')

for comment in subreddit.stream.comments():
	# use xmlcharref
	comments = str(comment.body.encode('ascii', 'ignore'))
	print 'COMMENT: ' + comments
	str_len = len(comments)
	print 'COMMENT LENGTH: ' + str(str_len)
 
	# old code :  and comment.id not in comments_replied_to 
	if str_len > 3:
		# def search():
		# threading.Timer(10.0, search).start()
			# if str_len is an odd number
			if str_len % 2 != 0:
				lhs = comments[:(str_len-1)/2]
				rhs = comments[-(str_len-1)/2:]
				print 'lhs: ' + lhs
				print 'rhs: ' + rhs
				print ''.join(reversed(rhs))

				if lhs == ''.join(reversed(rhs)):
					if re.search(r'\b' + comment.id + r'\b', open('palindromes-results.txt').read()):
						print 'comment id already exists in file'
					else:
						# start of debugging 1
						print "You used the word '" + comments + "' which is a palindrome"
						comment.reply("You used the word '" + comments + "' which is a palindrome")
						file.write(comment.id + ' ')
				else:
					print 'not a palindrome'
			elif str_len % 2 == 0:
				lhs = comments[:str_len/2]
				rhs = comments[-str_len/2:]
				print 'even lhs: ' + lhs
				print 'even rhs: ' + rhs
				print ''.join(reversed(rhs))

				if lhs == ''.join(reversed(rhs)):
					if re.search(r'\b' + comment.id + r'\b', open('palindromes-results.txt').read()):
						print 'comment id already exists in file'
					else:
						# start of debugging 2
						print "You used the word '" + comments + "' which is a palindrome"
						comment.reply("You used the word '" + comments + "' which is a palindrome")
						file.write(comment.id + ' ')
				else:
					print 'not a palindrome'
		# search()
file.close()