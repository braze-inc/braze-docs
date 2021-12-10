---
nav_title: Badges
article_title: Badges de carte de contenu pour iOS
platform: iOS
page_order: 5
description: "Cet article explique comment ajouter des badges à vos Cartes de Contenu dans votre application iOS."
channel:
  - cartes de contenu
---

# Badges

## Demander le nombre de cartes de contenu non lues

Si vous souhaitez afficher le nombre de cartes de contenu non lues que votre utilisateur a, Nous vous suggérons de demander un comptage de cartes et de le représenter avec un badge. Les badges sont un excellent moyen d'attirer l'attention sur les nouveaux contenus qui attendent vos utilisateurs dans les Cartes de Contenu. Si vous souhaitez ajouter un badge à vos Cartes de Contenu, le Braze SDK fournit des méthodes pour interroger les éléments suivants :

- Cartes de contenu non vues pour l'utilisateur actuel
- Total des cartes de contenu visibles pour l'utilisateur actuel

Les déclarations de méthode dans [ABKContentCardsController](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_content_cards_controller.html) ci-dessous décrivent cela en détail :

```
/*!
 * Cette méthode retourne le nombre de cartes de contenu actuellement actives qui n'ont pas été consultées.
 * Une "vue" se produit lorsqu'une carte devient visible dans la vue Cartes de Contenu.  Cela différencie
 * entre les cartes qui sont hors écran dans la vue défilement, et celles qui
 * sont à l'écran ; quand une carte fait défiler sur l'écran, elle est comptée comme affichée.
 *
 * Les cartes ne sont comptées qu'une seule fois -- si une carte défile l'écran et
 * en marche il n'est pas recensé.
 *
 * Les cartes ne sont comptées qu'une seule fois même si elles apparaissent dans plusieurs vues de cartes de contenu ou sur plusieurs appareils.
 */
- (NSInteger)unviewedContentCardCount;
/*!
 * Cette méthode retourne le nombre total de cartes de contenu actuellement actives. Les cartes sont comptées
 * une seule fois même si elles apparaissent dans plusieurs vues de cartes de contenu.
 */
- (NSInteger)contentCardCount;
```


## Affichage du nombre de cartes de contenu non vues sur le nombre de badges de l'application

En plus de servir de rappel de notification push pour une application, Les badges peuvent également être utilisés pour désigner les éléments non consultés dans le flux des Cartes de Contenu de l'utilisateur. Mettre à jour le nombre de badges en fonction des mises à jour non vues des Cartes de Contenu peut être un outil précieux pour attirer les utilisateurs vers votre application et augmenter les sessions.

Cette méthode enregistre le nombre de badges une fois que l'application est fermée et que la session de l'utilisateur se termine:

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
((void)applicationDidEnterBackground:(UIApplication *)application
```

Dans la méthode ci-dessus, implémente le code suivant qui met à jour le nombre de badges pendant que l'utilisateur voit les cartes pendant une session donnée :

```objc
[UIApplication sharedApplication].applicationIconBadgeNumber = [[Appboy sharedInstance].contentCardsController unviewedContentCardCount];
```

{% endtab %}
{% tab swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Dans la méthode ci-dessus, implémente le code suivant qui met à jour le nombre de badges pendant que l'utilisateur voit les cartes pendant une session donnée :

```swift
UIApplication.shared.applicationIconBadgeNumber =
  Appboy.sharedInstance()?.contentCardsController.unviewedContentCardCount() ?? 0
```

{% endtab %}
{% endtabs %}

Pour plus d'informations, voir le fichier d'en-tête [`Appboy.h`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h).
