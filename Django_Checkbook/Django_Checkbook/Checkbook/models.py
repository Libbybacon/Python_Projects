from django.db import models


class Account(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Starting_Balance = models.DecimalField(max_digits=15, decimal_places=2)

    Accounts = models.Manager()

    def __str__(self):
        return self.First_Name + ' ' + self.Last_Name


TRANSACTION_CHOICES = (
    ('Deposit', 'Deposit'),
    ('Withdrawal', 'Withdrawal'),

)


class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TRANSACTION_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()
