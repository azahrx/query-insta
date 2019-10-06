import instaloader
import pandas as pd

username = "mandce"
L = instaloader.Instaloader()
profil = instaloader.Profile.from_username(L.context, username)

captionlist = []
hashtaglist = []
likeslist = []
commentlist = []
usernamelist = []

for post in profil.get_posts():
    captpost = post.caption
    if captpost is None:
        continue
    captpost = captpost.encode('ascii', 'ignore')
    tagspost = post.caption_hashtags
    likespost = post.likes
    commentspost = []
    for comment in post.get_comments():
        commentspost.append(comment.text.encode('ascii', 'ignore'))
    captionlist.append(captpost)
    hashtaglist.append(tagspost)
    likeslist.append(likespost)
    commentlist.append(commentspost)
    usernamelist.append(username)

data = pd.DataFrame({"Account":usernamelist, "Post":captionlist, "Tag":hashtaglist, "Likes":likeslist, "Comments":commentlist})
print(data)
data.to_csv('dataset.csv')
