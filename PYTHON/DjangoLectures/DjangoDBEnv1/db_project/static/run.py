import os,django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','db_project.settings')
django.setup()

from django.contrib.auth.models import User
from db_app.models import Post

print(User.objects.all()) #<QuerySet [<User: arun>, <User: TestUser>]>
print(User.objects.first()) #arun
print(User.objects.filter(username='arun')) #<QuerySet [<User: arun>]>
print(User.objects.filter(username='arun').first()) #arun

user = User.objects.filter(username='arun').first()
print(user.id)
print(user.pk)
print(user)
#Insert record into Post Table
# post_obj = Post(title = "Django Db Details",content = "This is sample insert post",author = user)#Create insert obj
# post_obj.save()#save insert obj
# post_obj2 = Post(title = "Django Db Details2",content = "This is sample insert post2",author_id = user.id)#Create insert obj, here author_id is accepted since author has a foreign key on User
# post_obj2.save()#save insert obj

row1 = Post.objects.first() #get row in variable and query each column in it
print(row1.author) #arun
print(row1.content) #This is sample insert post
print(row1.author.email) #arunkumar.a@prodapt.com there email brings mail from the user configuration of django users

#new way to insert records in table
print(user.post_set.all()) #<QuerySet [<Post: Django Db Details , This is sample insert post , 2018-12-08 10:01:48.694181+00:00 , arun>, <Post: Django Db Details2 , This is sample insert post2 , 2018-12-08 10:11:09.208012+00:00 , arun>]>
user.post_set.create(title = "Django Db Details3",content = "This is sample insert post3") #here author is automatically picked from Django user variable and save is not required

print(Post.objects.all())#return all objects in post #<QuerySet [<Post: Post object (1)>]> #Here object is return and we can change the return object from Post by adding __str__ method in Post model

