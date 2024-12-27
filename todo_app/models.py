from django.db import models # type: ignore

class ToDoModel(models.Model):
    DONE = 'Done'
    UNFINISHED = 'Unfinished'
    POSTPONED = 'Postponed'
    CANCELLED = 'Cancelled'
    STATUS_CHOICES = [
        (DONE,'Done'),
        (UNFINISHED,'Unfinished'),
        (POSTPONED, 'Postponed'),
        (CANCELLED, 'Cancelled'),
    ]
    id = models.AutoField(primary_key=True)
    sr_no = models.IntegerField(default=1, blank=True)
    task = models.CharField(max_length=150, unique= True, blank=True)
    status = models.CharField(max_length=20,
        choices=STATUS_CHOICES, default= UNFINISHED,)
   
   
    
    def __unicode__(self):
        return self.sr_no, self.task
    
class StartTime(models.Model):
    start_time = models.TimeField(null=False, auto_now=False, blank=True)

    def __unicode__(self):
        return self.start_time
    

