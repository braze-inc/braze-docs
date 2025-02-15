---
nav_title: Badges
article_title: Badges de carte de contenu pour iOS
platform: iOS
page_order: 5
description: "Cet article traite des badges de vos cartes de contenu dans votre application iOS."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Badges

## Demander le décompte des cartes de contenu non lues

Si vous souhaitez afficher le nombre de cartes de contenu non lues de votre utilisateur, nous vous suggérons de demander un décompte des cartes et de le représenter par un badge. Les badges constituent un excellent moyen d’attirer l’attention sur le nouveau contenu en attente de vos utilisateurs dans les cartes de contenu. Si vous souhaitez ajouter un badge à vos cartes de contenu, le SDK de Braze fournit des méthodes permettant d’interroger les éléments suivants :

- Cartes de contenu non consultées pour l’utilisateur actuel
- Nombre total de cartes de contenu visibles pour l’utilisateur actuel

Les déclarations de méthodes suivantes dans [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html) décrivent cela en détail :

```objc
- (NSInteger)unviewedContentCardCount;
/*
This method returns the number of currently active Content Cards that have not been viewed.
A "view" happens when a card becomes visible in the Content Cards view. This differentiates between cards that are off-screen in the scrolling view and those which are on-screen; when a card scrolls onto the screen, it's counted as viewed.
Cards are counted as viewed only once -- if a card scrolls off the screen and back on, it's not re-counted.
Cards are counted only once, even if they appear in multiple Content Cards views or across multiple devices.
*/

- (NSInteger)contentCardCount;
/* 
This method returns the total number of currently active Content Cards. Cards are counted only once even if they appear in multiple Content Cards views.
 */
```

## Affichage du nombre de cartes de contenu non consultées sur le nombre de badges d’application

En plus de servir de rappels de notification push pour une application, les badges peuvent également être utilisés pour indiquer des éléments non consultés dans le flux de cartes de contenu de l’utilisateur. La mise à jour du nombre de badges en fonction des mises à jour des cartes de contenu non consultées peut être utile pour attirer les utilisateurs vers votre application et augmenter les sessions.

Cette méthode enregistre le nombre de badges après la fermeture de l'application et la fin de la session de l'utilisateur final :

{% tabs %}
{% tab OBJECTIF-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Pour cette méthode, implémentez le code suivant, qui actualise activement le nombre de badges alors que l’utilisateur visualise les cartes pendant une session donnée :

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].contentCardsController unviewedContentCardCount];
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Pour cette méthode, implémentez le code suivant, qui actualise activement le nombre de badges alors que l’utilisateur visualise les cartes pendant une session donnée :

```swift
UIApplication.shared.applicationIconBadgeNumber =
  Appboy.sharedInstance()?.contentCardsController.unviewedContentCardCount() ?? 0
```

{% endtab %}
{% endtabs %}

Pour plus d'informations, consultez le [fichier d'en-tête](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`.
