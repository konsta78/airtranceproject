from django.db import models

# Create your models here.

class Booking(models.Model):
    book_ref = models.AutoField(primary_key=True)
    book_date = models.DateField()
    total_amount = models.FloatField()


class Ticket(models.Model):
    ticket_no = models.AutoField(primary_key=True)
    book_ref = models.ForeignKey('Booking', on_delete=models.CASCADE)
    passenger_id = models.PositiveIntegerField()
    passenger_name = models.CharField(max_length=50)
    contact_data = models.TextField(max_length=200)


class Flight(models.Model):
    flight_id = models.AutoField(primary_key=True)
    flight_no = models.CharField(max_length=10)
    depature_airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='+')
    arrival_airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='+')


class TicketFlight(models.Model):
    FARE_CONDIION = (
        ('1', 'Econom'),
        ('2', 'Bisness'),
        ('3', 'First class')
    )
    ticket_no = models.ForeignKey('Ticket', on_delete=models.CASCADE)
    flight_id = models.ForeignKey("Flight", on_delete=models.CASCADE)
    fare_condition = models.CharField(max_length=1, choices=FARE_CONDIION)

    class Meta:
        unique_together = (('ticket_no', 'flight_id'),)


class Airport(models.Model):
    airport_code = models.CharField(max_length=3, default="DME")


class BoardingPass(models.Model):
    ticket_flight = models.OneToOneField('TicketFlight', on_delete=models.CASCADE, primary_key=True)
    boarding_no = models.IntegerField()
    seat_no = models.CharField(max_length=3)
