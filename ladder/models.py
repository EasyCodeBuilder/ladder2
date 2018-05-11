# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TblBalance(models.Model):
    user_id = models.CharField(max_length=20)
    current_day = models.CharField(max_length=5)
    total_day = models.CharField(max_length=6)
    total_balance = models.CharField(max_length=6)
    over_day = models.CharField(max_length=4)
    server_id = models.CharField(max_length=20)
    resv1 = models.CharField(max_length=200)
    resv2 = models.CharField(max_length=200)
    rec_crt_ts = models.DateTimeField()
    rec_upd_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_balance'
        unique_together = (('id', 'user_id'),)


class TblRequest(models.Model):
    req_no = models.CharField(unique=True, max_length=50)
    req_cd = models.CharField(max_length=5)
    req_param = models.TextField()
    settle_dt = models.CharField(max_length=8)
    res_msg = models.CharField(max_length=1024)
    rec_crt_ts = models.DateTimeField()
    rec_upd_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_request'


class TblServer(models.Model):
    server_id = models.CharField(max_length=17)
    ip = models.CharField(max_length=20)
    port = models.CharField(max_length=5)
    password = models.CharField(max_length=128)
    server_status = models.CharField(max_length=1)
    resv1 = models.CharField(max_length=200)
    resv2 = models.CharField(max_length=200)
    rec_crt_ts = models.DateTimeField()
    rec_upd_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_server'
        unique_together = (('id', 'server_id'),)


class TblTestUser(models.Model):
    user_id = models.CharField(max_length=20)
    nickname = models.CharField(max_length=64)
    qq_no = models.CharField(max_length=15)
    qq_name = models.CharField(max_length=64)
    wechat_no = models.CharField(max_length=30)
    wechat_name = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=11)
    user_status = models.CharField(max_length=1)
    password = models.CharField(max_length=64)
    settle_dt = models.CharField(max_length=8)
    current_balance = models.IntegerField()
    resv1 = models.CharField(max_length=200)
    resv2 = models.CharField(max_length=200)
    rec_crt_ts = models.DateTimeField()
    rec_upd_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_test_user'


class TblTrans(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=20)
    buss_no = models.CharField(primary_key=True, max_length=25)
    trans_cd = models.CharField(max_length=5)
    trans_at = models.CharField(max_length=6)
    trans_day = models.CharField(max_length=4)
    settle_dt = models.CharField(max_length=8)
    curr_day = models.CharField(max_length=4)
    curr_balance = models.CharField(max_length=6)
    resv1 = models.CharField(max_length=200)
    resv2 = models.CharField(max_length=200)
    rec_crt_ts = models.DateTimeField()
    rec_upd_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_trans'


class TblUser(models.Model):
    user_id = models.CharField(max_length=20)
    nickname = models.CharField(max_length=64)
    qq_no = models.CharField(max_length=15)
    qq_name = models.CharField(max_length=64)
    wechat_no = models.CharField(max_length=30)
    wechat_name = models.CharField(max_length=64)
    phone_no = models.CharField(max_length=11)
    user_status = models.CharField(max_length=1)
    password = models.CharField(max_length=64)
    settle_dt = models.CharField(max_length=8)
    resv1 = models.CharField(max_length=200)
    resv2 = models.CharField(max_length=200)
    rec_crt_ts = models.DateTimeField()
    rec_upd_ts = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tbl_user'
        unique_together = (('id', 'user_id'),)
