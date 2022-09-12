#Function to update all users' PluralSight details (email, first name, last name)
# you can run this function from the command line: python manage.py shell

def updateAllPluralSightFields():
    from codershq.users.models import User
    for user in User.objects.all():
        user.pluralSightFirstName=str(user.id)
        user.pluralSightLastName='codershq'
        user.pluralSightEmail=str(user.id)+"@codershq.ae"
        user.save()
