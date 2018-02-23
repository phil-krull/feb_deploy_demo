from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def add_user(self, post_data):
        # do some validations
        return self.create(first_name = post_data['first_name'], last_name = post_data['last_name'], email = post_data['email'])

    def get_users(self):
        return self.all()

    def get_user(self, user_id):
        return self.get(id = user_id)

    def update_user(self, user_id, post_data):
        user_to_update = self.get_user(user_id)
        # add in some validations
        user_to_update.first_name = post_data['first_name']
        user_to_update.last_name = post_data['last_name']
        user_to_update.email = post_data['email']
        user_to_update.save()

    def delete_user(self, user_id):
        self.get(id = user_id).delete()

class User(models.Model):
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()