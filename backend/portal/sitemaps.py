from django.contrib.sitemaps import Sitemap
from blog.models import Post


class PortalSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        # if  object have pub_date
        return obj.date_created
        # pass