from django.db import models
from django.contrib.auth.models import User

class UserAttendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attendance_date = models.DateField(auto_now_add=True)
    attendance_status = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user.username} - {self.attendance_date} - {self.attendance_status}'
