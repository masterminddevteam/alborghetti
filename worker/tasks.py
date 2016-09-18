from __future__ import absolute_import

from celery import shared_task

import urllib
from bs4 import BeautifulSoup

from .models import SpiderContent
from datetime import datetime
import re


@shared_task
def start_routine():
    starbucks_spider()
    outback_spider()

def starbucks_spider():
    url = "https://www.starbucks.com.br/card/rewards"
    htmltext = urllib.urlopen(url).read()
    soup = BeautifulSoup(htmltext)
    body = ''
    for tag in soup.findAll('p')[56]:
        body = tag

    spider_content, created = \
    SpiderContent.objects.get_or_create(name='starbucks')
    if created:
       SpiderContent.objects.create(
            name='starbucks',
            updated_on=datetime.now(),
            content=body.encode('utf-8'),
            content_length=str(len(body))
        )
    else:
        spider_content.updated_on = datetime.now()
        spider_content.save()

def outback_spider():
    url = "http://www.outback.com.br/institucional/?uri=faq"
    htmltext = urllib.urlopen(url).read()
    soup = BeautifulSoup(htmltext)
    txt1 = ""
    txt1 = soup.findAll('p')[8]
    regex = re.compile(r'<[^<]*?>')
    semtag = regex.sub('', str(txt1))

    spider_content, created = \
    SpiderContent.objects.get_or_create(name='outback')
    if created:
       SpiderContent.objects.create(
            name='outback',
            content=semtag,
            content_length=len(semtag)
        )
    else:
        spider_content.updated_on = datetime.now()
        spider_content.save()
