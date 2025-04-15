# Defining a News Feed category

> Learn how to define a News Feed category for the Braze Android SDK.

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Defining a category

Instances of the Braze News Feed can be configured to only receive cards from a certain "category". This allows for the effective integration of multiple News Feed streams within a single application. For more information on this feature, see our News Feed [best practices]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/)

News Feed categories can be defined by calling the following methods as you load the News Feed:

```xml
newsFeed.setCategories(CardCategory.ALL_CATEGORIES);
newsFeed.setCategories(CardCategory.ADVERTISING);
newsFeed.setCategories(CardCategory.ANNOUNCEMENTS);
newsFeed.setCategories(CardCategory.NEWS);
newsFeed.setCategories(CardCategory.SOCIAL);
newsFeed.setCategories(CardCategory.NO_CATEGORY);
```

You can also populate a feed with a combination of categories as in the following example:

```xml
newsFeed.setCategories:EnumSet.of(CardCategory.ANNOUNCEMENTS, CardCategory.NEWS);
```
