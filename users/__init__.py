""" This config for makes our app to run signals in admin """
default_app_config = "users.apps.UsersConfig"


# Other method finding in bin chat

""" example of how to use signals in Django admin pages """

# from django.contrib import admin
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from .models import MyModel

# class MyModelAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         super().save_model(request, obj, form, change)
#         post_save.send(sender=MyModel)

# @receiver(post_save, sender=MyModel)
# def my_handler(sender, **kwargs):
#     # Do something here
#     pass

# admin.site.register(MyModel, MyModelAdmin)


""" In this example, we’re using the @receiver decorator to connect our signal handler function to the post_save signal for the MyModel model. We’re also overriding the save_model method of the ModelAdmin class to send the post_save signal after the model instance is saved.

I hope this helps. Let me know if you have any other questions."""
