# -*- coding: utf-8 -*-
# https://doc.scrapy.org/en/latest/intro/install.html
# https://www.cnblogs.com/wuxl360/p/5567631.html
# https://blog.csdn.net/la_vie_est_belle/article/details/79017358
#
#import sys, os
#sys.path.append(os.path.abspath(os.path.realpath(os.path.dirname(__file__))))
#sys.path.append(os.path.join(os.path.dirname(__file__), "xca_amazon"))
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# �����Ǳ��������
import robotparser
import htmlentitydefs

import scrapy.spiderloader
import scrapy.statscollectors
import scrapy.logformatter
import scrapy.dupefilters
import scrapy.squeues

import scrapy.extensions.spiderstate
import scrapy.extensions.corestats
import scrapy.extensions.telnet
import scrapy.extensions.logstats
import scrapy.extensions.memusage
import scrapy.extensions.memdebug
import scrapy.extensions.feedexport
import scrapy.extensions.closespider
import scrapy.extensions.debug
import scrapy.extensions.httpcache
import scrapy.extensions.statsmailer
import scrapy.extensions.throttle

import scrapy.core.scheduler
import scrapy.core.engine
import scrapy.core.scraper
import scrapy.core.spidermw
import scrapy.core.downloader

import scrapy.downloadermiddlewares.stats
import scrapy.downloadermiddlewares.httpcache
import scrapy.downloadermiddlewares.cookies
import scrapy.downloadermiddlewares.useragent
import scrapy.downloadermiddlewares.httpproxy
import scrapy.downloadermiddlewares.ajaxcrawl
#import scrapy.downloadermiddlewares.chunked
import scrapy.downloadermiddlewares.decompression
import scrapy.downloadermiddlewares.defaultheaders
import scrapy.downloadermiddlewares.downloadtimeout
import scrapy.downloadermiddlewares.httpauth
import scrapy.downloadermiddlewares.httpcompression
import scrapy.downloadermiddlewares.redirect
import scrapy.downloadermiddlewares.retry
import scrapy.downloadermiddlewares.robotstxt

import scrapy.spidermiddlewares.depth
import scrapy.spidermiddlewares.httperror
import scrapy.spidermiddlewares.offsite
import scrapy.spidermiddlewares.referer
import scrapy.spidermiddlewares.urllength

import scrapy.pipelines
from scrapy.exporters import CsvItemExporter

import scrapy.core.downloader.handlers.http
import scrapy.core.downloader.contextfactory

# �����������ҵ���Ŀ���õ���
import scrapy.pipelines.images  # �õ�ͼƬ�ܵ�
import openpyxl  # �õ�openpyxl��
from xca_amazon.items import XcaAmazonItem

process = CrawlerProcess(get_project_settings())

# 'Books' is the name of one of the spiders of the project.
process.crawl('start_search')
process.start()  # the script will block here until the crawling is finished
