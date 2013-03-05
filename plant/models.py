from django.db import models

# Create your models here.
class Plant(models.Model):
    genus = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
# this is usually a range. shoud it be a string? how best to represent?
    zone = models.IntegerField()
# maybe more like 'special features'? (velvety stems, brilliant fall color) 
    featureColor = models.CharField(max_length=20)
    nativeRegion = models.CharField(max_length=50)
#     image = models.ImageField(upload_to=None)
    plantDescription = models.TextField()    
# should below be an organized list? see model field reference in docs
# such as: bush, tree, conifer, vine, grass, etc
# the list would be really long, but otherwise data could be conflicting yet matching (Vine, vines, climber, climbing rose, etc)
    plantType = models.CharField(max_length=20)
# blooming time choice set   
    SPRING = 'SP'
    SUMMER = 'SM'
    FALL = 'FL'
    WINTER = 'WT'
    BLOOM_TIME_CHOICES = (
        (SPRING, 'Spring'),
        (SUMMER, 'Summer'),
        (FALL, 'Fall'),
        (WINTER, 'Winter'),
    )
    bloom_time = models.CharField(max_length=2,
        choices=BLOOM_TIME_CHOICES, 
        default=SPRING
    )
# sunlight-needs choice set    
    FULL_SUN = 'FS'
    PART_SUN = 'PS'
    SHADE = 'SH'
    SUN_NEEDS_CHOICES = (
        (FULL_SUN, 'Full Sun'),
        (PART_SUN, 'Part Sun'),
        (SHADE, 'Shade'),
    )
    sun_needs = models.CharField(max_length=2,
        choices=SUN_NEEDS_CHOICES,
        default = FULL_SUN
    )
    

    def __unicode__(self):
        return ('%s %s' % (self.genus, self.species))
        
    