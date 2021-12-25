from django.db import models


# Create your models here.

class project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    leader = models.CharField(max_length=200)
    tester = models.CharField(max_length=200)
    programmer = models.CharField(max_length=200)
    publish_app = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return {'id': self.id,
                'name': self.name,
                'desc': self.desc,
                'leader': self.leader,
                'tester': self.tester,
                'programmer': self.programmer,
                'publish_app': self.publish_app,
                'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')}


class interfaces(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    project = models.CharField(max_length=200)
    project_id = models.CharField(max_length=200)
    tester = models.CharField(max_length=200)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def to_dict(self):
        return {'id': self.id,
                'name': self.name,
                'desc': self.desc,
                'project': self.project,
                'project_id': self.project_id,
                'tester': self.tester,
                'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S'),
                'update_time': self.update_time.strftime('%Y-%m-%d %H:%M:%S')}
