from django.db import models


class Kingdom(models.Model):
    kingdom_name = models.CharField(max_length=128)

    def __str__(self):
        return self.kingdom_name

class Subordinate(models.Model):
    name = models.CharField(max_length=128)
    kingdom = models.ForeignKey(to=Kingdom, on_delete=models.CASCADE)
    age = models.PositiveSmallIntegerField()
    email = models.CharField(max_length=128)

    def __str__(self):
        return "name: " + self.name + " | kingdom: " + self.kingdom.kingdom_name 

class King(models.Model):
    name = models.CharField(max_length=128)
    kingdom = models.ForeignKey(to=Kingdom, on_delete=models.CASCADE)

    def __str__(self):
        return "name: " + self.name + " | kingdom: " + self.kingdom.kingdom_name 

class Question(models.Model):
    content = models.TextField(max_length=20)
    kingdom = models.ForeignKey(to=Kingdom, on_delete=models.CASCADE)
    correct_answer = models.CharField(max_length=8)
    def __str__(self):
        return "question: " + self.content + " | for kingdom: " + self.kingdom.kingdom_name + " | correct answer: " + self.correct_answer 

class Answer(models.Model):
    subordinate = models.ForeignKey(to=Subordinate, on_delete=models.CASCADE)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    isAnswerCorrect = models.BooleanField()
    def __str__(self):
        word = "not " if not self.isAnswerCorrect else ""
        return "Answer is " + word + "correct: " + " | for question: " + self.question.content + " | by subordinate: " + self.subordinate.name 

class Accept(models.Model):
    subordinate = models.ForeignKey(to=Subordinate, on_delete=models.CASCADE)
    king = models.ForeignKey(to=King, on_delete=models.CASCADE)
    accepted = models.BooleanField()
    def __str__(self):
        word = "not " if self.accepted == False else ""
        return self.subordinate.name + " is " + word + str("accepted") + " by king: " + self.king.name 

