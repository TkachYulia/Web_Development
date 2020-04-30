from django.db import models


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    city = models.CharField(max_length=50)
    address = models.TextField()
    class Meta:
        verbose_name_plural = "companies"
    def to_json(self):
        return {
            'Company Name': self.name,
            'id': self.id,
            'Description': self.description,
            'City': self.city,
            'Address': self.address
        }


class Vacancy(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    salary = models.FloatField('')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "vacancies"
    def to_json(self):
        return {
            'Name': self.name,
            'id': self.id,
            'Description': self.description,
            'Salary': self.salary,
            'Company': self.company.name
        }
