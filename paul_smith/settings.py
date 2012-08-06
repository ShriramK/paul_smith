# Scrapy settings for paul_smith project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'paul_smith'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['paul_smith.spiders']
NEWSPIDER_MODULE = 'paul_smith.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

