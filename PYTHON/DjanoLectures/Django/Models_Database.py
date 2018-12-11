---Create admin user
python manage.py createsuperuser


'-----------------MODELS starts-----------------'
    'Models are like tables in database e.g Employee model, Student model'
'Model.py'
    'Use OOP to create models for Django'
'Create models'
    'Go to models.py and create a class with name same as the table which you want to create'

    '''
        from django.db import models

        class Topic(models.Model):
            top_name = models.CharField(max_length=264,unique=True)
            def __str__(self):
                return self.top_name

        class Webpage(models.Model):
            topic = models.ForeignKey(Topic)
            name = models.CharField(max_length=264,unique=True)
            url = models.URLField(unique=True)
            def __str__(self):
                return self.name

        class AccessRecord(models.Model):
            name = models.ForeignKey(Webpage)
            data = models.DateField()
            def __str__(self):
                return str(self.data)
    '''
'Migrate Models (Building DB)'
    'run python manage.py migrate'
'Register changes to Application'
    'run python manage.py makemigrations first_app'
'''Now our model is ready and got registed in the sql database'''

'Interact with the database - Method one:'
    'Using models'
    '''Open python shell using 'python manage.py shell --> import the table(i.e clase name from models.py)'''
    'Insert record to table using '
    '''
        >>> t = Topic(top_name="Social Network")
        >>> t.save()
        >>> print(Topic.objects.all())
        <QuerySet [<Topic: Social Network>]>
    '''
    '''Query rows from tables
        search a records in tables:
        mytable.objects.filter(col="mycol")

         print(mytable.objects.all()) gives all records
         print(mytable.objects.first()) gives first row
         print(mytable.objects.last()) gives last row
         table_obj = mytable.objects.all()

         for i in table_obj: parse through all the rows and get each column info
            print(i.first_name)
            print(i.last_name)
            print(i.Email)

    '''
''' So far we have created three tables and inserted a record in Topic table'''

---view the sql present in mirgration
    '''python manage.py sqlmigrate db_app 0001'''
