from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from polls.models import Question

class RssSiteNewsFeed(Feed):
    title = "Q&A Forum"
    link = "/rss/"
    description = "You will always get your answer here"

    def items(self):
        return Question.objects.order_by('-pub_date')[:5]
    def item_link(self,item):
        return "polls/rss/"