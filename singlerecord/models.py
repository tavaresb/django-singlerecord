from django.db import models

class SingleRecordModel(models.Model):
    
    class Meta:
        abstract = True

    @classmethod
    def get(cls):
        return cls.objects.get_or_create(pk=1)[0]
            
    def save(self, *args, **kwargs):
        self.id=1
        super(SingleRecordModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

        
