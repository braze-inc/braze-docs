---
nav_title: Defining a News Feed Category
article_title: Defining a News Feed Category for Android/FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "This reference article shows how to define a News Feed category in your Android application."
channel:
  - news feed
  
---

# Defining a news feed category

Instances of the Braze News Feed can be configured to only receive cards from a certain “category”. This allows for effective integration of multiple News Feed streams within a single application. For more information on this feature see more in our [News Feed best practices][14]

News Feed Categories can be defined by calling the following methods as you load the News Feed:

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
