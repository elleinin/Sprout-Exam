from tortoise import fields, models

# WHEN MAKING CHANGES TO MODEL
# docker-compose exec backend aerich migrate
# docker-compose exec backend aerich upgrade

class Employee(models.Model):
    id = fields.IntField(pk=True)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    email = fields.CharField(max_length=50, null=True)
    employee_type = fields.CharField(max_length=50, null=False)

class Regular(models.Model):
    id = fields.IntField(pk=True)
    profile = fields.ForeignKeyField("models.Employee", related_name="Regular Employee")
    number_of_leaves = fields.FloatField(null=True)
    benefits = fields.JSONField(null=True)

class Contractual(models.Model):
    id = fields.IntField(pk=True)
    profile = fields.ForeignKeyField("models.Employee", related_name="Contractual Employee")
    contract_end_date = fields.CharField(max_length=50, null=True)
    project = fields.TextField(null=True)