---
nav_title: Définir une catégorie de flux d'actualités
article_title: Définition d'une catégorie de flux d'actualités pour iOS
platform: iOS
page_order: 2
description: "Cet article de référence montre comment définir une catégorie de flux d'actualité dans votre application iOS."
channel:
  - fil d'actualité
---

# Définition d'une catégorie de flux d'actualité

Les instances de Braze News Feed peuvent être configurées pour ne recevoir que les cartes d'une certaine "catégorie". Cela permet l'intégration effective de plusieurs flux de nouvelles dans une seule application. Pour plus d'informations sur cette fonctionnalité, visitez notre documentation sur les [meilleures pratiques][40] du flux d'actualités.

Les catégories de flux d'actualités peuvent être définies en appelant l'une des méthodes suivantes lorsque vous chargez le flux d'actualités :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[newsFeed setCategories:ABKCardCategoryAll];
[newsFeed setCategories:ABKCardCategoryAnnouncements];
[newsFeed setCategories:ABKCardCategoryAdvertising];
[newsFeed setCategorySocial];
[newsFeed setCategories:ABKCardCategories:ABKCardCategoryNews];
[newsFeed setCategories:ABKCardCategoryNoCategoryNoCategory];
```

{% endtab %}
{% tab swift %}

```swift
NewsFeed.categories = ABKCardCategory.all
newsFeed.categories = ABKCardCategory.announcements
newsFeed.categories = ABKCardCategory.advertising
newsFeed.categories = ABKCardCategory.social
newsFeed.categories = ABKCardCategory.news
newsFeed.categories = ABKCardCategory.noCategory
```

{% endtab %}
{% endtabs %}


Vous pouvez également remplir un flux avec une combinaison de catégories comme dans l'exemple suivant :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[newsFeed setCategories:ABKCardCategoryAnnouncements|ABKCardCategoryAdvertising];
```

{% endtab %}
{% tab swift %}

```swift
NewsFeed.categories = Catégorie ABKCard([.announcements, .advertising])
```

{% endtab %}
{% endtabs %}

[40]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
