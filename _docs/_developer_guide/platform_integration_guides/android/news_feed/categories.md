---
nav_title: Defining a News Feed Category
article_title: Defining a News Feed Category for Android and FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "This reference article shows how to define a News Feed category in your Android or FireOS application."
channel:
  - news feed
  
---

# Defining a News Feed category

Instances of the Braze News Feed can be configured to only receive cards from a certain “category”. This allows for the effective integration of multiple News Feed streams within a single application. For more information on this feature, see our News Feed [best practices][14]

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


[14]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
