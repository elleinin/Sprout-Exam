from tortoise import fields, models

# WHEN MAKING CHANGES TO MODEL
# docker-compose exec backend aerich migrate
# docker-compose exec backend aerich upgrade

class Employee(models.Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    email = fields.CharField(max_length=50, null=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"