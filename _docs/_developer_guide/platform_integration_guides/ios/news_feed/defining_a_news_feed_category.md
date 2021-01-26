---
nav_title: Defining a News Feed Category
platform: iOS
page_order: 2

---

# Defining a News Feed Category

Instances of the Braze News Feed can be configured to only receive cards from a certain "category". This allows for the effective integration of multiple News Feed streams within a single application. For more information on this feature visit our [News Feed Best Practices][40] doc.

News Feed Categories can be defined by calling the following methods as you load the News Feed:

```objc
[newsFeed setCategories:ABKCardCategoryAll];
[newsFeed setCategories:ABKCardCategoryAnnouncements];
[newsFeed setCategories:ABKCardCategoryAdvertising];
[newsFeed setCategories:ABKCardCategorySocial];
[newsFeed setCategories:ABKCardCategoryNews];
[newsFeed setCategories:ABKCardCategoryNoCategory];
```

You can also populate a feed with a combination of categories as in the following example:

```objc
[newsFeed setCategories:ABKCardCategoryAnnouncements|ABKCardCategoryAdvertising];
```


[40]: {{site.baseurl}}/help/best_practices/news_feed/
