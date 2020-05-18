# Instagram-Bot
The third of my 10-bots-10-days series. 
\
\
This bot will log into your instagram account, go to the user of your choice, and like and comment on every single one of their posts (The comment will be one out of 102 possible compliments that have been generated so far). This bot works for any profile you select -- simply enter their name in the "account" variable of contact.py!

\
\
P.S. It also has a simple way of closing any bot-prevention popups using this simple Finite State Machine:
\
\
while there_are_more_posts:\
  // See if there is a pop-up (meaning the bot is being detected) and close it\
  try:\
    close_pop_up()  \
  \
  // If there is no bot-detecting pop-up, continue\
  except NoSuchElementException:\
    continue_like_comment()

