from selenium import webdriver
from time import sleep
from random import randint
import pandas as pd
import MySQLdb


chromedriver_path = '/home/ashwmadhu/Projects/twitter_bot/chromedriver_linux64/chromedriver'
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(7)
webdriver.get('https://twitter.com/login')
sleep(8)

username = webdriver.find_element_by_css_selector(
    '#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input')
username.send_keys('AvinashOd')
password = webdriver.find_element_by_css_selector(
    '#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input')
password.send_keys('ashwmadhu1207$')

sleep(7)

remember_login = webdriver.find_element_by_css_selector(
    '#page-container > div > div.signin-wrapper > form > div.clearfix > div > label > input[type="checkbox"]')
if remember_login.is_selected():
    remember_login.click()
sleep(8)
button_login = webdriver.find_element_by_css_selector(
    '#page-container > div > div.signin-wrapper > form > div.clearfix > button')

button_login.click()
sleep(randint(8, 12))

#---------------------------------------- Search work -----------------------------
db = MySQLdb.connect("127.0.0.1","root","","datingapp-staging" )
print(db)
# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM `da_30search_keywords`"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      search_keyword = row[1]
      print(search_keyword)
      webdriver.get('https://twitter.com/search?src=typd&q=%(search_keyword)s' % {"search_keyword": search_keyword})
      sleep(10)
except:
   print("Error: unable to fecth data")

# disconnect from server
db.close()
#---------------------------------------- End -------------------------------------



# hashtag_list = ['travelblog', 'travel']

# prev_user_list = pd.read_csv('followed_user_list.csv', delimiter=',').iloc[:, 1:2]  # keep the user records
# prev_user_list = [list(prev_user_list)]

# new_followed = []
# tag = -1
# followed = 0
# likes = 0
# comments = 0

# for hashtag in hashtag_list:
#     tag += 1
#     webdriver.get('https://twitter.com/hashtag/%(hashtag)s?f=users&vertical=default&src=hash' % {"hashtag": hashtag})
#     sleep(10)

#     for user in webdriver.find_elements_by_class_name('ProfileCard'):
#         try:
#             username = user.find_element_by_class_name('ProfileCard-screennameLink').text
#             if username not in prev_user_list:
#                 button = user.find_element_by_class_name('EdgeButton').click()
#                 new_followed.append(username)
#                 followed += 1
#                 sleep(randint(9, 13))
#         except:
#             continue
#     sleep(randint(6, 13))


# for n in range(0, len(new_followed)):
#     prev_user_list.append(new_followed[n])

# updated_user_df = pd.DataFrame(prev_user_list)
# updated_user_df.to_csv('followed_user_list.csv')
