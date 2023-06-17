from py_youtube import Data

# video_url = "https://www.youtube.com/watch?v=Prt_SKkZji8"
#
# data = Data(video_url).data()
# print(data)

my_links = ["https://www.youtube.com/watch?v=YDp73WjNISc", "https://www.youtube.com/watch?v=Prt_SKkZji8",
           "https://www.youtube.com/watch?v=dLgquj0c5_U&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=1&t=1s&pp=iAQB",
           "https://www.youtube.com/watch?v=S41RPtdWe78&list=PLCC34OHNcOtpz7PJQ7Tv7hqFBP_xDDjqg&index=3&t=310s"]
likes_dict = {}
views_dict = {}
for link in my_links:
    data = Data(link).data()
    likes_dict[data["title"]] = data["likes"]
    views_dict[data["title"]] = data["views"]

print(likes_dict)
print(views_dict)