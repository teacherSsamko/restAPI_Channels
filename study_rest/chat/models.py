#  Developed by taejong.im(jeff@gdflab.com) on 2019.12.9.
#  Last Modified 19. 12. 9. 오후 9:59.
#  Copyright (c) 2019 GDFLAB. All right reserved
from __future__ import unicode_literals

from django.db import models


from django.core.validators import FileExtensionValidator
from django.dispatch import receiver
from django.db.models.signals import pre_save


videoEXT_CHOICES = (
    ('ASF', 'ASF'),
    ('AVI', 'AVI'),
    ('FLV', 'FLV'),
    ('MPG', 'MPG'),
    ('MPEG', 'MPEG'),
    ('MP4', 'MP4'),
    ('MOV', 'MOV'),
    ('3GP', '3GP'),
    ('WEBM', 'WEBM'),   
    ('MKV', 'MKV'), 
    ('WMV', 'WMV'),                              
)

vEncoder_CHOICES  = (
    ('H264','H.264/AVC'),
    ('MPEG4','MPEG-4'),
    ('H265','H.265/HEVC'),
)

audioEXT_CHOICES  = (
    ('mp3', 'mp3'),
    ('wav', 'wav'),
    ('m4a', 'm4a'),
    ('flac', 'flac'),
    ('ogg', 'ogg'),
    ('mp2', 'mp2'),     
    ('amr', 'amr'),           
)


audioEXT_CHOICES  = (
    ('mp3', 'mp3'),
    ('wav', 'wav'),
    ('m4a', 'm4a'),
    ('flac', 'flac'),
    ('ogg', 'ogg'),
    ('mp2', 'mp2'),     
    ('amr', 'amr'),           
)

aQuality_CHOICES  = (
    ('8k','8k'),
    ('20k','20k'),
    ('44.1k','44.1k'),
    ('64k','64k'),
    ('80k','80k'),
    ('96k','96k'),
    ('128k','128k'),
    ('160k','160k'),    
    ('192k','192k'),
    ('256k','256k'),
    ('320k','320k'),
) 
    
aEncoder_CHOICES  = (
    ('AAC','AAC' ),
    ('MP3','MP3' ),      
)

aSampleRate_CHOICES = (
    ('8000','8000'),
    ('11025','11025'),    
    ('12000','12000'),
    ('16000','16000'),
    ('22050','22050'),
    ('24000','24000'),
    ('32000','32000'),
    ('44100','44100'),  
    ('48000','48000'),       
)     

VideoPreset_CHOICES = (
    ('7680x4320 25','8K/(7680x4320/) 25p'),
    ('3840x2160 25','UHD 4K(3840x2160) 25p'),    
    ('1920x1080 25','FHD 1080p(1920x1080) 25p'),
    ('1280x720 25','HD 720p(1280x720) 25p'),
    ('854x480 25','480p(854x480) 25p'),
    ('640x360 25','360p(640x360) 25p'),
    ('426x240 25','260p(426x240) 25p'),
    ('720x576 25','DVD(720x576) 25p'),
    ('640x480 25','TV(640x480) 25p'),
    ('320x240 25','Mobile(320x240) 25p'),
    ('7680x4320 30','8K(7680x4320) 30p'),
    ('3840x2160 30','UHD 4K(3840x2160) 30p'),      
    ('1920x1080 30','FHD 1080p(1920x1080) 30p'),
    ('1280x720 30','HD 720p(1280x720) 30p'),
    ('854x480 30','480p(854x480) 30p'),
    ('640x360 30','360p(640x360) 30p'),
    ('426x240 30','260p(426x240) 30p'),
    ('720x576 30','DVD(720x576) 30p'),
    ('640x480 30','TV(640x480) 30p'),
    ('320x240 30','Mobile(320x240) 30p'),
    ('7680x4320 60','8K(7680x4320) 60p'),
    ('3840x2160 60','UHD 4K(3840x2160) 60p'),      
    ('1920x1080 60','FHD 1080p(1920x1080) 60p'),
    ('1280x720 60','HD 720p(1280x720) 60p'),
    ('854x480 60','480p(854x480) 60p'),
    ('640x360 60','360p(640x360) 60p'),
    ('426x240 60','260p(426x240) 60p'),
    ('720x576 60','DVD(720x576) 60p'),
    ('640x480 60','TV(640x480) 60p'),
    ('320x240 60','Mobile(320x240) 60p'),
) 

aimodel_alias_CHOICES = (
    ('1x2_3c', 'pikavue_1x2_3c'),
    ('4x2_3c', 'pikavue_4x2_3c'),    
    ('1x4_3c', 'pikavue_1x4_3c'),
    ('4x4_3c', 'pikavue_4x4_3c'),
)
    
class Video(models.Model):
    status = models.CharField(max_length=10, default='Wait')
    file = models.FileField(upload_to='upload/', validators=[FileExtensionValidator(allowed_extensions=['asf','avi','flv','mpg','mpeg','mp4','mov','webm','mkv','wmv','ogv'])])
    filesize = models.CharField(max_length=20, default=None)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    aimodel_alias = models.CharField(max_length=255, choices=aimodel_alias_CHOICES, default='1x2_3c')
    target = models.FileField(upload_to='upscale/', null=True, default=None)
    width = models.IntegerField(null=True, default=None)
    height = models.IntegerField(null=True, default=None)
    vframeRate = models.CharField(max_length=5, blank=True)    #"25,30,60"
    scale = models.FloatField(default=4)
    afilesize = models.CharField(max_length=20, default=None)
    up_width = models.IntegerField(null=True, default=None)
    up_height = models.IntegerField(null=True, default=None)
    start_dt = models.DateTimeField(null=True, default=None)
    complete_dt = models.DateTimeField(null=True, default=None)
    processed_time= models.DateTimeField(null=True, default=None)

'''@receiver(pre_save, sender=Video)
def pre_save_Video(sender, instance, *args, **kwargs):
    mime_type = magic.from_buffer(instance.file.read(2048), mime=True)
    # Do something with mime_type   
    print("check this mime", mime_type)
    is_video = mime_type.split("/")[0]'''


