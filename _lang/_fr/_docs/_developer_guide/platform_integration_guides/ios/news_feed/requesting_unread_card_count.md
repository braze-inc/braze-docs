---
nav_title: Nombre de cartes non lues en attente
article_title: Demander le nombre de cartes non lues pour le flux d'actualités pour iOS
platform: iOS
page_order: 3
description: "Cet article de référence couvre la façon d'implémenter des indicateurs de lecture et de lecture dans votre flux d'actualités pour votre application iOS."
channel:
  - fil d'actualité
---

# Demander le nombre de cartes non lues

!\[Exemple de Badge de Flux de Nouvelles\]\[45\]{: style="float:right;max-width:25%;margin-left:15px;"}

Les badges sont un excellent moyen d'attirer l'attention sur le nouveau contenu qui attend vos utilisateurs dans le flux d'actualités. Si vous souhaitez ajouter un badge à votre flux d'actualités, le Braze SDK fournit des méthodes pour interroger les éléments suivants :

- Cartes de flux d'actualités non lues pour l'utilisateur actuel
- Total des fiches d'actualités visibles pour l'utilisateur actuel

Les déclarations de méthode dans [ABKFeedController][44] ci-dessous décrivent cela en détail :

```objc
/*!
 * Cette méthode retourne le nombre de cartes actuellement actives qui n'ont pas été vues dans les catégories données.
 * Une "vue" se produit lorsqu'une carte devient visible dans la vue du flux.  Cela différencie
 * entre les cartes qui sont hors écran dans la vue défilement, et celles qui
 * sont à l'écran ; quand une carte fait défiler sur l'écran, elle est comptée comme affichée.
 *
 * Les cartes ne sont comptées qu'une seule fois -- si une carte défile l'écran et
 * en marche il n'est pas recensé.
 *
 * Les cartes ne sont comptées qu'une seule fois même si elles apparaissent dans plusieurs vues de flux ou sur plusieurs appareils.
 */
- (NSInteger)unreadCardCountForCategories:(ABKCardCategory)categories;

/*!
 * Cette méthode retourne le nombre total de cartes actuellement actives appartient à des catégories données. Les cartes sont comptées
 * une seule fois même si elles apparaissent dans plusieurs vues de flux.
 */
- (NSInteger)cardCountForCategories:(ABKCardCategory)categories;
```

## Affichage du nombre d'actualités non lues sur le nombre de badges de l'application

!\[Exemple de badge\]\[42\]{: style="float:right;max-width:70%;margin-left:15px;"}

En plus de servir de rappel de notification push pour une application, les badges peuvent également être utilisés pour désigner les éléments non vus dans le flux d'actualités de l'utilisateur. Mettre à jour le nombre de badges basé sur les mises à jour des flux d'actualités non lus peut être un outil précieux pour attirer les utilisateurs vers votre application et augmenter les sessions.

Appeler cette méthode qui enregistre le nombre de badges une fois que l'application est fermée et que la session de l'utilisateur se termine.

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
((void)applicationDidEnterBackground:(UIApplication *)application
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

{% endtab %}
{% endtabs %}

Dans la méthode ci-dessus, implémente le code suivant qui met à jour le nombre de badges pendant que l'utilisateur voit les cartes pendant une session donnée.

{% tabs %}
{% tab OBJECTIVE-C %}

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

À tout moment, par exemple dans la méthode `applicationDidBecomeActive` , utilisez le code suivant pour effacer le nombre de badges.

{% tabs %}
{% tab OBJECTIVE-C %}

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

Pour plus d'informations, voir le fichier d'en-tête [`Appboy.h`][15].
[42]: {% image_buster /assets/img_archive/badge_example.png %} "Exemple" [45]: {% image_buster /assets/img_archive/newsfeed_badges.png %}

[15]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h "Appboy.h Header File"
[44]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_feed_controller.html "abk feed controller"
