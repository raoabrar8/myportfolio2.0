from django.db import models

# Create your models here.

# Home models


class ProfileModel(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='my_profile', height_field=None, width_field=None, max_length=None)
    job_title= models.CharField(max_length=100)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    

class CvModel(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    details = models.CharField(max_length=255, null=True, blank=True, default=None)
    cv_file = models.FileField(upload_to='my_cv/', max_length=254)
    update_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    

class ShowContactsModel(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=254, blank=True, default=None)
    details = models.CharField(max_length=200)
    updated_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    


class SocialModel(models.Model):
    name = models.CharField(max_length=40, default=None)
    link = models.URLField(max_length=254)
    icon = models.CharField(max_length=50)
    updated_on = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.name
    

class ContactsModel(models.Model):
    email = models.EmailField(max_length=254)
    phone_no = models.CharField(max_length=100)
    birthday = models.DateField()
    address = models.CharField(max_length=254)
    whatsapp_no = models.CharField(max_length=200, default='0317 4196972')
    


class AboutModel(models.Model):
    about = models.TextField()


class JobModel(models.Model):
    job_logo = models.ImageField(upload_to='job_logo/')
    title = models.CharField(max_length=100)
    description= models.TextField()

    def __str__(self):
        return self.title
    


class TestimonialsModel(models.Model):
    client_profile = models.ImageField(upload_to='client_images/')
    client_name = models.CharField(max_length=100)
    client_feedback = models.TextField()
    feedback_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.client_name
    

class ClinetsModel(models.Model):
    partner_logo = models.ImageField(upload_to='partner_logo')
    partner_url = models.URLField(max_length=254)



# Resume Models

class EducationModel(models.Model):
    university = models.CharField(max_length=100)
    degree = models.CharField(max_length=50)
    details = models.CharField(max_length=254)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(default='Present', blank=True)

    def __str__(self):
        return self.degree
    


class ExperineceModel(models.Model):
    job_title = models.CharField(max_length=50)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(default='Present', blank=True)
    institude = models.CharField(max_length=100)
    details = models.CharField(max_length=254)

    def __str__(self):
        return self.job_title
    

class CertficateModel(models.Model):
    institude = models.CharField(max_length=100)
    certi_name = models.CharField(max_length=100)
    certi_url = models.URLField(max_length=254)
    issued_date = models.DateField(blank=True, default=None)

    def __str__(self):
        return self.certi_name


class SkillsModel(models.Model):
    skill_title = models.CharField(max_length=50)
    level = models.IntegerField()

    def __str__(self):
        return self.skill_title
    

# Portfolio Models
class CatrgoryModel(models.Model):
    name = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name
    

class ProjectModel(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(CatrgoryModel, related_name='projects', on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='project_image/')
    project_url = models.URLField(max_length=254)


    def __str__(self):
        return self.title
    


# blog models

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50)
    post_date = models.DateField(blank=True)
    blog_image = models.ImageField(upload_to='blog_images/')
    blog_url = models.URLField(max_length=254)

    def __str__(self):
        return self.title
    


# contact models

class ContactModel(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, help_text='Required')
    your_message = models.TextField()


    def __str__(self):
        return self.full_name
    


# frontend Skills Model



class LanguageModel(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name
class FrontendSkillModel(models.Model):


    language = models.ForeignKey(LanguageModel, related_name='frontends', on_delete=models.CASCADE)
    expertise = models.CharField(max_length=20, choices=[
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    level = models.PositiveIntegerField(help_text="Enter skill level as a percentage (0-100)")
    icon = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.language} - ({self.level}%)"


class BackendSkillModel(models.Model):

    language = models.ForeignKey(LanguageModel, related_name='backends', on_delete=models.CASCADE)
    expertise = models.CharField(max_length=20, choices=[
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    level = models.PositiveIntegerField(help_text="Enter skill level as a percentage (0-100)")
    icon = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.language} - ({self.level}%)"
    

class AISkillModel(models.Model):

    language = models.ForeignKey(LanguageModel, related_name='ai', on_delete=models.CASCADE)
    expertise = models.CharField(max_length=20, choices=[
        ('basic', 'Basic'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ])
    level = models.PositiveIntegerField(help_text="Enter skill level as a percentage (0-100)")
    icon = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.language} - ({self.level}%)"