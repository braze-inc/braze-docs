---
nav_title: Badges
article_title: Badges de carte de contenu pour iOS
platform: iOS
page_order: 5
description: "Cet article traite des badges de vos cartes de contenu dans votre application iOS."
channel:
  - cartes de contenu

---

# Badges

## Demande du nombre de cartes de contenu non lues

Si vous souhaitez afficher le nombre de cartes de contenu non lues de votre utilisateur, nous vous suggérons de demander un décompte de cartes et de le représenter par un badge. Les badges constituent un excellent moyen d’attirer l’attention sur le nouveau contenu en attente de vos utilisateurs dans les cartes de contenu. Si vous souhaitez ajouter un badge à vos cartes de contenu, le SDK de Braze fournit des méthodes permettant d’interroger les éléments suivants :

- Cartes de contenu non consultées pour l’utilisateur actuel
- Nombre total de cartes de contenu visibles pour l’utilisateur actuel

Les déclarations de méthodes suivantes dans [`ABKContentCardsController`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html) décrivent cela en détail :

```objc
- (NSInteger)unviewedContentCardCount;
/*
La méthode renvoie le nombre de Cartes de contenu actuellement active qui n’ont pas été visualisées.
Une « vue » survient lorsqu’une carte devient visible dans la vue Cartes de contenu. Ceci permet de faire la différence entre les cartes qui sont hors écran dans la vue de défilement et celles qui sont à l’écran, lorsqu’une carte défile sur l’écran, elle est comptabilisée comme visualisée.
Les cartes sont comptabilisées comme visualisées une seule fois – si une carte défile hors de l’écran et y revient, elle n’est pas re-comptabilisée.
Les cartes ne sont comptabilisées qu’une seule fois, même si elles s’affichent dans plusieurs vues de Cartes de contenu ou sur plusieurs appareils.
*/

- (NSInteger)contentCardCount;
/* 
La méthode renvoie le nombre total de Cartes de contenu actuellement actives. Les cartes ne sont comptabilisées qu’une seule fois, même si elles s’affichent dans plusieurs vues de Cartes de contenu.
 */
```

## Affichage du nombre de cartes de contenu non consultées sur le nombre de badges d’application

En plus de servir de rappels de notification push pour une application, les badges peuvent également être utilisés pour indiquer des éléments non consultés dans le flux de cartes de contenu de l’utilisateur. La mise à jour du nombre de badges en fonction des mises à jour des cartes de contenu non consultées peut être utile pour attirer les utilisateurs vers votre application et augmenter les sessions.

Cette méthode enregistre le nombre de badges une fois l’application fermée et la session de l’utilisateur terminée :

{% tabs %}
{% tab OBJECTIVE-C %}

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

Pour plus d’informations, voir le [fichier d’en-tête](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h) `Appboy.h`.
