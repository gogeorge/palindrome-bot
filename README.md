# palindrome-bot

palindrome = a word, phrase, or sequence that reads the same backwards as forwards, e.g. madam or racecar.
<br><br>
This is a reddit bot which will detect any palindromes in the comments of a post. Then it will reply "You used the word {something} which is a palindrome".
<br><br>
- The code is very sketchy because this my first time writing in python
<br><br>
- ```palindrome-results.txt``` is the file where the comment ids -- of comments the bot has replied to -- will be stored to prevent the bot from replying to the same comment more than once.
<br><br>
- To use this bot you need to put your username, password, client id and client secret on the ```praw.ini``` file
