import praw
import threading
import re

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("sandboxtest")

file = open('palindromes-results.txt', 'w+')

for comment in subreddit.stream.comments():
	comments = str(comment.body.encode('ascii', 'ignore'))
	print 'COMMENT: ' + comments
	str_len = len(comments)
	print 'COMMENT LENGTH: ' + str(str_len)
 
	if str_len > 3:
		# if str_len is an odd number
		if str_len % 2 != 0:
			lhs = comments[:(str_len-1)/2]
			rhs = comments[-(str_len-1)/2:]
				if lhs == ''.join(reversed(rhs)):
					if re.search(r'\b' + comment.id + r'\b', open('palindromes-results.txt').read()):
						print 'comment id already exists in file'
					else:
						print "You used the word '" + comments + "' which is a palindrome"
						comment.reply("You used the word '" + comments + "' which is a palindrome")
						file.write(comment.id + ' ')
				else:
					print 'not a palindrome'
			elif str_len % 2 == 0:
				lhs = comments[:str_len/2]
				rhs = comments[-str_len/2:]

				if lhs == ''.join(reversed(rhs)):
					if re.search(r'\b' + comment.id + r'\b', open('palindromes-results.txt').read()):
						print 'comment id already exists in file'
					else:
						print "You used the word '" + comments + "' which is a palindrome"
						comment.reply("You used the word '" + comments + "' which is a palindrome")
						file.write(comment.id + ' ')
				else:
					print 'not a palindrome'
file.close()
