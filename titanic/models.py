from django.db import models

class Prediction(models.Model):
    Pclass = models.IntegerField()
    Age = models.FloatField()
    SibSp = models.IntegerField()
    Parch = models.IntegerField()
    Fare = models.FloatField()
    Sex_male = models.IntegerField()
    Embarked_Q = models.IntegerField()
    Embarked_S = models.IntegerField()
    prediction = models.CharField(max_length=20)
    probability = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction({self.Pclass}, {self.Age}, {self.Sex_male})"
