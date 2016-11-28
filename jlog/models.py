# coding=utf-8

from django.db import models
from juser.models import User
import time


class Log(models.Model):
    user = models.CharField(max_length=20, null=True)
    host = models.CharField(max_length=200, null=True)
    remote_ip = models.CharField(max_length=100)
    login_type = models.CharField(max_length=100)
    log_path = models.CharField(max_length=100)
    start_time = models.DateTimeField(null=True)
    pid = models.IntegerField()
    is_finished = models.BooleanField(default=False)
    end_time = models.DateTimeField(null=True)
    filename = models.CharField(max_length=40)
    '''
    add by liuzheng
    '''
    # userMM = models.ManyToManyField(User)
    # logPath = models.TextField()
    # filename = models.CharField(max_length=40)
    # logPWD = models.TextField()  # log zip file's
    # nick = models.TextField(null=True)  # log's nick name
    # log = models.TextField(null=True)
    # history = models.TextField(null=True)
    # timestamp = models.IntegerField(default=int(time.time()))
    # datetimestamp = models.DateTimeField(auto_now_add=True)


    def __unicode__(self):
        return self.log_path


class Alert(models.Model):
    msg = models.CharField(max_length=20)
    time = models.DateTimeField(null=True)
    is_finished = models.BigIntegerField(default=False)


class TtyLog(models.Model):
    log = models.ForeignKey(Log)
    datetime = models.DateTimeField(auto_now=True)
    cmd = models.CharField(max_length=200)


class ExecLog(models.Model):
    user = models.CharField(max_length=100)
    host = models.TextField()
    cmd = models.TextField()
    remote_ip = models.CharField(max_length=100)
    result = models.TextField(default='')
    datetime = models.DateTimeField(auto_now=True)


class FileLog(models.Model):
    user = models.CharField(max_length=100)
    host = models.TextField()
    filename = models.TextField()
    type = models.CharField(max_length=20)
    remote_ip = models.CharField(max_length=100)
    result = models.TextField(default='')
    datetime = models.DateTimeField(auto_now=True)


class TermLog(models.Model):
    user = models.ManyToManyField(User)
    logPath = models.TextField()
    filename = models.CharField(max_length=40)
    logPWD = models.TextField()  # log zip file's
    nick = models.TextField(null=True)  # log's nick name
    log = models.TextField(null=True)
    history = models.TextField(null=True)
    timestamp = models.IntegerField(default=int(time.time()))
    datetimestamp = models.DateTimeField(auto_now_add=True)


class RunProcess(models.Model):
    class Meta:
        db_table = "tb_task"
    run_time = models.CharField(name="time", max_length=64)
    user = models.CharField(max_length=32)
    ip = models.CharField(max_length=100)
    task = models.TextField()


class HadoopProcess(models.Model):
    class Meta:
        db_table = "rpt_jobs_info"

    jobId = models.CharField(max_length=32)
    sDateTime = models.CharField(max_length=22)  # 时间
    submitTime = models.DateTimeField()  # 提交时间
    startTime = models.DateTimeField()  # 开始时间
    finishTime = models.DateTimeField()  # 完成时间

    jobName = models.CharField(max_length=255)  # 任务名称
    queue = models.CharField(max_length=60)  # 队列名
    userName = models.CharField(max_length=62)  # 用户名
    state = models.CharField(max_length=20)  # 状态
    mapsTotal = models.IntegerField(max_length=11)  # map数
    mapsCompleted = models.IntegerField(max_length=11)  # map完成数
    reducesTotal = models.IntegerField(max_length=11)  # reduce数
    reducesCompleted = models.IntegerField(max_length=11)  # reduce完成数
    cpuMap = models.BigIntegerField()  # map使用cpu数
    cpuReduce = models.BigIntegerField()  # reduce使用cpu数
    cpuTotal = models.BigIntegerField()  # 使用cpu总核数
    memMap = models.BigIntegerField()  # map使用内存数
    memReduce = models.BigIntegerField()  # reduce使用内存数
    memTotal = models.BigIntegerField()  # 使用内存总数
    fileBytesReadMap = models.BigIntegerField()  # map读取字节数

    fileBytesReadRed = models.BigIntegerField()  # reduce读取字节数
    fileBytesReadTotal = models.BigIntegerField()  # 总读取字节数
    fileBytesWriteMap = models.BigIntegerField()  # map写字节数
    fileBytesWriteRed = models.BigIntegerField()  # reduce写字节数
    fileBytesWriteTotal = models.BigIntegerField()  # 总写字节数
    hdfsBytesReadMap = models.BigIntegerField()  # map读hdfs字节数
    hdfsBytesReadRed = models.BigIntegerField()  # reduce读hdfs字节数
    hdfsBytesReadTotal = models.BigIntegerField()  # 总读取hdfs字节数
    hdfsBytesWriteMap = models.BigIntegerField()  # map写hdfs字节数
    hdfsBytesWriteRed = models.BigIntegerField()  # reduce写hdfs字节数
    hdfsBytesWriteTotal = models.BigIntegerField()  # 总写hdfs字节数

    workflowName = models.TextField()  # 任务具体信息
    hiveQuery = models.TextField()  # hive任务详细信息
    otherQuery = models.TextField()  # 其它


class DatabaseProcess(models.Model):
    class Meta:
        db_table = "tb_db_process"

    sql = models.TextField()
    userName = models.CharField(max_length=255)
    remote_ip = models.CharField(max_length=255)
    executeTime = models.DateTimeField()
    database = models.CharField(max_length=255)

"""
DatabaseProcess(sql="SELECT * FROM tb_user",
                userName="root",
                remote_ip="192.168.0.1",
                executeTime=datetime.datetime(2016, 11, 25, 23, 0, 0),
                database="mytest")

HadoopProcess(jobId="job-121212121",
              sDateTime="2016-11-26",
              submitTime=datetime.datetime(2016, 11, 25, 23, 0, 0),
              startTime=datetime.datetime(2016, 11, 26, 1, 0, 0),
              finishTime=datetime.datetime(2016, 11, 26, 13, 0, 0),
              jobName="query user",
              queue="test",
              userName="test",
              state="SUCCESS",
              mapsTotal=10,
              mapsCompleted=10,
              reducesTotal=2,
              reducesCompleted=2,
              cpuMap=8,
              cpuReduce=1,
              cpuTotal=32,
              memMap=10240,
              memReduce=10240,
              memTotal=10240,
              fileBytesReadMap=102400,

              fileBytesReadRed=102400,
              fileBytesReadTotal=102400,
              fileBytesWriteMap=102400,
              fileBytesWriteRed=102400,
              fileBytesWriteTotal=102400,
              hdfsBytesReadMap=102400,
              hdfsBytesReadRed=102400,
              hdfsBytesReadTotal=102400,
              hdfsBytesWriteMap=102400,
              hdfsBytesWriteRed=102400,
              hdfsBytesWriteTotal=102400,

              workflowName="hive -e ",
              hiveQuery="SELECT * FROM lv_user1",
              otherQuery="")
"""