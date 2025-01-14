---
nav_title: Badges
article_title: Badges du fil d’actualités pour iOS
platform: iOS
page_order: 3
description: "Cet article de référence explique comment implémenter le nombre de badges du fil d’actualités dans votre application iOS."
channel:
  - news feed

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Badges

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

## Demande de décompte de cartes de fil d’actualité non lues

![]({% image_buster /assets/img_archive/newsfeed_badges.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Les badges constituent un excellent moyen d’attirer l’attention sur le nouveau contenu en attente de vos utilisateurs dans le Fil d’actualité. Si vous souhaitez ajouter un badge à votre fil d’actualité, le SDK de Braze fournit des méthodes permettant d’interroger les éléments suivants :

- Les cartes de fil d’actualité non lues pour l’utilisateur actuel
- Total des cartes de fil d’actualité visibles pour l’utilisateur actuel

Les déclarations de méthodes suivantes dans [`ABKFeedController`](http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller") décrivent cela en détail :

```
- (NSInteger)unreadCardCountForCategories:(ABKCardCategory)categories;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)cardCountForCategories:(ABKCardCategory)categories;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once, even if they appear in multiple Content Cards views.
 */
 ```

## Afficher le nombre d’articles du fil d’actualités non lus pour le nombre de badges d’application

En plus de servir de rappels de notification push pour une application, les badges peuvent également spécifier des éléments non consultés dans le fil d’actualité de l’utilisateur. La mise à jour du nombre de badges basée sur les mises à jour du fil d’actualité non lu peut constituer un outil précieux pour attirer les utilisateurs vers votre application et augmenter les sessions.

Appelez cette méthode qui enregistre le nombre de badges après la fermeture de l'application et la fin de la session de l'utilisateur final :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

{% endtab %}
{% endtabs %}

Pour cette méthode, implémentez le code suivant, qui actualise activement le nombre de badges alors que l’utilisateur visualise les cartes pendant une session donnée.

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].feedController unreadCardCountForCategories:ABKCardCategoryAll];
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = Appboy.sharedInstance()?.feedController.unreadCardCount(forCategories: ABKCardCategory.all) ?? 0
```

{% endtab %}
{% endtabs %}

À tout moment, par exemple, avec la méthode `applicationDidBecomeActive`, utilisez le code suivant pour effacer le nombre de badges :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = 0;
```

{% endtab %}
{% tab swift %}

```swift
UIApplication.shared.applicationIconBadgeNumber = 0
```

{% endtab %}
{% endtabs %}

Pour plus d'informations, consultez le `Appboy.h` [fichier d'en-tête](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.hFichier d'en-Tête").

