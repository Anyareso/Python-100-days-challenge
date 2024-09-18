facebook_posts = eval(input("Enter: "))

total_likes = 0
# TODO Catch the KeyError exception
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass


print(total_likes)
