from django.db import models

# Create your models here.
class Employee(models.Model):
    
    """Employee Model Definition"""

    TYPE_HOUSEMAN = "houseman"
    TYPE_LONDRY = "londry"
    TYPE_OPERATOR = "operator"
    TYPE_RECEPTION = "reception"
    TYPE_RESERVATION = "reservation"
    TYPE_ROOMMAID = "roommaid"
    TYPE_OTHER = "other"


    TYPE_CHOICES = [
        (TYPE_HOUSEMAN, "Houseman"),
        (TYPE_LONDRY, "Londry"),
        (TYPE_OPERATOR, "Operator"),
        (TYPE_RECEPTION, "Reception"),
        (TYPE_RESERVATION, "Reservation"),
        (TYPE_ROOMMAID, "Room maid"),
        (TYPE_OTHER, "Other"),
        ]
    
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = [
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    ]


    e_ID = models.CharField(max_length=20, primary_key=True)
    e_PW = models.CharField(max_length=20)
    e_name = models.CharField(max_length=20, default="-")
    e_gender = models.CharField(choices=GENDER_CHOICES, max_length=20, blank=True)
    e_work_type = models.CharField(choices=TYPE_CHOICES, max_length=20, blank=True)
    e_birthdate = models.DateField(blank=True, null=True)
    e_address = models.CharField(max_length=200, default="-")
    e_salary = models.IntegerField(null=True, blank=True, default=0)
    e_phone_number = models.CharField(max_length=100, default="000-0000-0000")

    def __str__(self):
        return self.e_ID
