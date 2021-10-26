from django.db import models

# Create your models here.

class MachineMaster(models.Model):
    machine_name=models.CharField(max_length=128,blank=True,null=True)
    country_id=models.IntegerField(blank=True,null=True)
    machine_type_id=models.IntegerField(blank=True,null=True)
    customer_id=models.IntegerField(blank=True,null=True)
    is_active=models.IntegerField(blank=True,null=True)
    created_by=models.IntegerField(blank=True,null=True)
    created_dttm=models.DateTimeField(blank=True,null=True)
    modified_by=models.DateTimeField(blank=True,null=True)
    modified_dttm=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.machine_name




class DailyFieldReports(models.Model):
    machine_id=models.IntegerField(blank=True,null=True)
    report_date=models.DateField(blank=True,null=True)
    shift_date=models.DateField(blank=True,null=True)
    call_time_1=models.DateTimeField(blank=True,null=True)
    release_time_1=models.DateTimeField(blank=True,null=True)
    call_time_2=models.DateTimeField(blank=True,null=True)
    release_time_2=models.DateTimeField(blank=True,null=True)
    customer_id=models.IntegerField(blank=True,null=True)
    cust_region=models.CharField(max_length=100,blank=True,null=True)
    cust_division=models.CharField(max_length=128,blank=True,null=True)
    cust_subdivision=models.CharField(max_length=128,blank=True,null=True)
    cust_tieuplocation=models.CharField(max_length=128,blank=True,null=True)
    cust_machine_availability=models.IntegerField(blank=True,null=True)
    remarks=models.TextField(max_length=5000,blank=True,null=True)
    ir_rep=models.CharField(max_length=250,blank=True,null=True)
    vandhana_rep=models.CharField(max_length=250,blank=True,null=True)
    is_active=models.IntegerField(blank=True,null=True)
    created_by=models.IntegerField(blank=True,null=True)
    created_dttm=models.DateTimeField(blank=True,null=True)
    modified_by=models.IntegerField(blank=True,null=True)
    modified_dttm=models.DateTimeField(blank=True,null=True)
    dailyFieldReports_machineid_idx=models.ForeignKey(MachineMaster,on_delete=models.CASCADE)




