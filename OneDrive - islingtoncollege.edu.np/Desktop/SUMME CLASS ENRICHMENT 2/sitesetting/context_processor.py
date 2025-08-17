from . models import sitesetting
 
def site_settings(request):
    setting = sitesetting.objects.first()
    return{'Site_Setting': setting}
