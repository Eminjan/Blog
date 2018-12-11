#!/usr/bin/env
# -*-coding:utf-8-*-
# @Author  : E🚀M

from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

from .models import Blog


class AllBlogsRssFeed(Feed):
    title = "EM's Blog"
    link = "/"
    description = "EM's Blog的最新文章"

    def items(self):
        return Blog.objects.all()

    def item_title(self, item):
        return '[%s]%s' % (item.blog_type, item.title)

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('blog_detail', args=[item.pk])


class AllBlogsAtomFeed(AllBlogsRssFeed):
    feed_type = Atom1Feed
    subtitle = AllBlogsRssFeed.description
