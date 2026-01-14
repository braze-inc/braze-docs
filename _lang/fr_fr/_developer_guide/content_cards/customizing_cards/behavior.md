---
nav_title: Comportement
article_title: Personnaliser le comportement des cartes de contenu
page_order: 2
description: "Ce guide de mise en œuvre aborde la modification du comportement des cartes de contenu, l'ajout d'éléments supplémentaires tels que des paires clé-valeur à votre charge utile, ainsi que des recettes pour des personnalisations courantes."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personnaliser le comportement des cartes de contenu

> Ce guide de mise en œuvre aborde la modification du comportement des cartes de contenu, l'ajout d'éléments supplémentaires tels que des paires clé-valeur à votre charge utile, ainsi que des recettes pour des personnalisations courantes. Pour obtenir la liste complète des types de cartes de contenu, voir [À propos des cartes de contenu.]({{site.baseurl}}/developer_guide/content_cards/) 

## Paires clé-valeur

Braze vous permet d'envoyer des charges utiles de données supplémentaires via des cartes de contenu aux appareils des utilisateurs à l'aide de paires clé-valeur. Ces derniers peuvent vous aider à suivre les indicateurs internes, à mettre à jour le contenu de l'app et à personnaliser les propriétés. [Ajoutez des paires clé-valeur à l'aide du tableau de bord]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create#step-4-configure-additional-settings-optional). 
 
{% alert note %}
Nous vous déconseillons d'envoyer des valeurs JSON imbriquées sous forme de paires clé-valeur. Aplanissez plutôt les valeurs JSON avant de les envoyer.
{% endalert %}

{% tabs %}
{% tab Android %}

Les paires clé-valeur sont stockées sur des objets de type <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> sous la forme de `extras`. Ces données peuvent être utilisées pour envoyer des données avec une carte pour une manipulation ultérieure par l’application. Appelez <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> pour accéder à ces valeurs.

{% endtab %}
{% tab iOS %}

Les paires clé-valeur sont stockées sur des objets de type <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> sous la forme de `extras`. Ces données peuvent être utilisées pour envoyer des données avec une carte pour une manipulation ultérieure par l’application. Appelez <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> pour accéder à ces valeurs.

{% endtab %}
{% tab Web %}

Les paires clé-valeur sont stockées sur des objets de type <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> sous la forme de `extras`. Ces données peuvent être utilisées pour envoyer des données avec une carte pour une manipulation ultérieure par l’application. Appelez `card.extras` pour accéder à ces valeurs.

{% endtab %}
{% endtabs %}

{% alert tip %}
Il est important que vos équipes de marketing et de développement se coordonnent sur les paires clé-valeur qui seront utilisées (par exemple, `feed_type = brand_homepage`), car toutes les paires clé-valeur saisies par les marketeurs dans le tableau de bord de Braze doivent correspondre exactement aux paires clé-valeur que les développeurs créent dans la logique de l'application.
{% endalert %}

## Cartes de contenu en tant que contenu supplémentaire

![]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Vous pouvez mélanger de façon transparente les cartes de contenu dans un flux existant, ce qui permet de charger simultanément les données de plusieurs flux. Cela crée une expérience cohésive et harmonieuse avec les cartes de contenu Braze et le contenu du flux existant.

L’exemple à droite montre un flux avec une liste hybride d’éléments qui sont renseignés par les données locales et les cartes de contenu alimentées par Braze. Avec cette méthode, les cartes de contenu ne peuvent pas être différenciées au regard du contenu existant.

### Paires clé-valeur déclenchées par l'API

Les [campagnes déclenchées par l'API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) sont une bonne stratégie à employer lorsque les valeurs d'une carte dépendent de facteurs externes pour déterminer le contenu à afficher à l'utilisateur. Par exemple, pour afficher du contenu supplémentaire, définissez des paires clé-valeur à l'aide de Liquid. Notez que `class_type` doit être connu au moment de la configuration.

![Les paires clé-valeur pour le cas d’usage des cartes de contenu supplémentaires. Dans cet exemple, différents aspects de la carte tels que "tile_id", "tile_deeplink" et "tile_title" sont définis à l'aide de Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Les cartes de contenu en tant que contenu interactif
![Une carte de contenu interactive affichant une promotion de 50 % apparaît dans le coin en bas à gauche de l’écran. Après avoir cliqué, une promotion sera appliquée au panier.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

Les cartes de contenu peuvent être utilisées pour créer des expériences dynamiques et interactives pour vos utilisateurs. Dans l’exemple à droite, une fenêtre contextuelle de carte de contenu apparaît au moment du paiement, fournissant aux utilisateurs des promotions de dernière minute. Des cartes bien placées comme ceci constituent un excellent moyen d’encourager les utilisateurs à entreprendre des actions spécifiques. 

Les paires clé-valeur pour ce cas d’usage comprennent un ensemble `discount_percentage` défini comme montant de remise souhaité et un ensemble `class_type` défini comme `coupon_code`. Ces paires clé-valeur vous permettent de filtrer et d'afficher des cartes de contenu spécifiques à un type dans l'écran de paiement. Pour plus d'informations sur l'utilisation de paires clé-valeur pour gérer plusieurs flux, voir [Personnaliser le flux par défaut de la carte de contenu.]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds)
<br>
<br>

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"} 

## Badges de cartes de contenu

![Écran d'accueil d'un iPhone montrant un exemple d'application Braze nommé Swifty avec un badge rouge affichant le nombre 7]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Les badges sont de petites icônes idéales pour attirer l'attention d'un utilisateur. L'utilisation de badges pour alerter l'utilisateur sur le nouveau contenu de la carte de contenu peut inciter les utilisateurs à revenir sur votre application et augmenter le nombre de sessions.

### Affichage du nombre de cartes de contenu non lues sous forme de badge

Vous pouvez afficher le nombre de cartes de contenu non lues de votre utilisateur sous forme de badge sur l'icône de votre application. 

{% tabs %}
{% tab Android %}

Vous pouvez à tout moment demander le nombre de cartes non lues en appelant :

{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endsubtab %}
{% endsubtabs %}

Vous pouvez ensuite utiliser ces informations pour afficher un badge indiquant le nombre de cartes de contenu non lues. Consultez la <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">documentation de référence du SDK</a> pour plus d'informations.


{% endtab %}
{% tab iOS %}

L'exemple suivant utilise `braze.contentCards` pour demander et afficher le nombre de cartes de contenu non lues. Après la fermeture de l'application et la fin de la session de l'utilisateur final, ce code demande un décompte des cartes, en filtrant le nombre de cartes en fonction de la propriété `viewed`.

{% subtabs %}
{% subtab Swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Pour cette méthode, implémentez le code suivant, qui actualise activement le nombre de badges alors que l’utilisateur visualise les cartes pendant une session donnée :

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Pour cette méthode, implémentez le code suivant, qui actualise activement le nombre de badges alors que l’utilisateur visualise les cartes pendant une session donnée :

```objc
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if (card.viewed == NO) {
    unreadCardCount += 1;
  }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Web %}

Vous pouvez à tout moment demander le nombre de cartes non lues en appelant :

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Vous pouvez ensuite utiliser ces informations pour afficher un badge indiquant le nombre de cartes de contenu non lues. Consultez la <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">documentation de référence du SDK</a> pour plus d'informations.

{% endtab %}
{% endtabs %}


