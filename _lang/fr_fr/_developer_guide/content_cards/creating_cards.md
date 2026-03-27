---
nav_title: Créer des cartes
article_title: Créer des cartes de contenu
page_order: 0
description: "Cet article couvre les composants de la création d'une interface utilisateur personnalisée pour les cartes de contenu."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Créer des cartes de contenu

> Cet article présente l'approche de base pour mettre en œuvre des cartes de contenu personnalisées, ainsi que trois cas d'utilisation courants. Il part du principe que vous avez déjà lu les autres articles du guide de personnalisation des cartes de contenu pour comprendre ce qui peut être fait par défaut et ce qui nécessite du code personnalisé. Il est particulièrement utile de comprendre comment [enregistrer les analyses]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) pour vos cartes de contenu personnalisées. 

{% multi_lang_include banners/content_card_alert.md %}

## Création d'une carte

### Étape 1 : Créer une IU personnalisée 

{% tabs local %}
{% tab web %}

Commencez par créer votre composant HTML personnalisé qui servira à afficher les cartes. 

{% endtab %}
{% tab android %}

Commencez par créer votre propre fragment personnalisé. Le [`ContentCardsFragment`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/index.html) par défaut est uniquement conçu pour gérer les types de cartes de contenu standard, mais il constitue un bon point de départ.

{% endtab %}
{% tab swift %}

Commencez par créer votre propre composant de contrôleur de vue personnalisé. Le [`BrazeContentCardUI.ViewController`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcardui/viewcontroller) par défaut est uniquement conçu pour gérer les types de cartes de contenu standard, mais il constitue un bon point de départ.

{% endtab %}
{% endtabs %}

### Étape 2 : S'abonner aux mises à jour des cartes

Enregistrez une fonction de rappel pour vous abonner aux mises à jour des données lorsque les cartes sont actualisées. Vous pouvez analyser les objets de cartes de contenu et extraire leurs données utiles, telles que `title`, `cardDescription` et `imageUrl`, puis utiliser les données du modèle résultant pour alimenter votre IU personnalisée.

Pour obtenir les modèles de données des cartes de contenu, abonnez-vous aux mises à jour des cartes de contenu. Portez une attention particulière aux propriétés suivantes :

* **`id` :** Représente la chaîne de caractères d'ID de la carte de contenu. Il s'agit de l'identifiant unique utilisé pour enregistrer les analyses des cartes de contenu personnalisées.
* **`extras` :** Englobe toutes les paires clé-valeur du tableau de bord de Braze. 

Toutes les propriétés en dehors de `id` et `extras` sont facultatives pour les cartes de contenu personnalisées. Pour plus d'informations sur le modèle de données, consultez l'article d'intégration de chaque plateforme : [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).

{% tabs local %}
{% tab web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
// For example:
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to call `logContentCardImpressions([card])`
    }
    else if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      // Use `card.title`, `card.imageUrl`, etc.
    }
    else if (card instanceof braze.ImageOnly) {
      // Use `card.imageUrl`, etc.
    }
  })
});

braze.openSession();
```

{% alert note %}
Les cartes de contenu ne sont actualisées au démarrage de la session que si `subscribeToContentCardsUpdates()` est appelé avant `openSession()`. Vous pouvez également [actualiser manuellement le flux]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/) à tout moment.
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

#### Étape 2a : Créer une variable d'abonné privée

Pour vous abonner aux mises à jour des cartes, déclarez d'abord une variable privée dans votre classe personnalisée pour contenir votre abonné :

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

#### Étape 2b : S'abonner aux mises à jour

Ajoutez le code suivant pour vous abonner aux mises à jour des cartes de contenu de Braze, généralement dans la méthode `Activity.onCreate()` de votre activité de cartes de contenu personnalisée :

```java
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
mContentCardsUpdatedSubscriber = new IEventSubscriber<ContentCardsUpdatedEvent>() {
    @Override
    public void trigger(ContentCardsUpdatedEvent event) {
        // List of all Content Cards
        List<Card> allCards = event.getAllCards();

        // Your logic below
    }
};
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber);
Braze.getInstance(context).requestContentCardsRefresh();
```

#### Étape 2c : Se désabonner

Désabonnez-vous lorsque votre activité personnalisée n'est plus visible. Ajoutez le code suivant à la méthode de cycle de vie `onDestroy()` de votre activité :

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

#### Étape 2a : Créer une variable d'abonné privée

Pour vous abonner aux mises à jour des cartes, déclarez d'abord une variable privée dans votre classe personnalisée pour contenir votre abonné :

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

#### Étape 2b : S'abonner aux mises à jour

Ajoutez le code suivant pour vous abonner aux mises à jour des cartes de contenu de Braze, généralement dans la méthode `Activity.onCreate()` de votre activité de cartes de contenu personnalisée :

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh()
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(mContentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

#### Étape 2c : Se désabonner

Désabonnez-vous lorsque votre activité personnalisée n'est plus visible. Ajoutez le code suivant à la méthode de cycle de vie `onDestroy()` de votre activité :

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Pour accéder au modèle de données des cartes de contenu, appelez [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) sur votre instance `braze`.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Vous pouvez également maintenir un abonnement pour observer les changements dans vos cartes de contenu. Deux approches sont possibles : 
1. Maintenir un cancellable ; ou 
2. Maintenir un `AsyncStream`.

##### Cancellable 

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

##### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Si vous souhaitez maintenir un abonnement à vos cartes de contenu, vous pouvez appeler [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) :

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}


### Étape 3 : Mettre en œuvre les analyses

Les impressions, clics et fermetures de cartes de contenu ne sont pas automatiquement enregistrés dans votre vue personnalisée. Vous devez [mettre en œuvre chaque méthode correspondante]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/) pour enregistrer correctement tous les indicateurs dans les analyses du tableau de bord de Braze.

### Étape 4 : Tester votre carte (facultatif)

Pour tester votre carte de contenu :

1. Définissez un utilisateur actif dans votre application en appelant la méthode [`changeUser()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser).
2. Dans Braze, accédez à **Campagnes**, puis [créez une nouvelle campagne de cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create).
3. Dans votre campagne, sélectionnez **Test**, puis saisissez le `user-id` de l'utilisateur test. Lorsque vous êtes prêt, sélectionnez **Envoyer le test**. Vous pourrez bientôt lancer une carte de contenu sur votre appareil.

![Une campagne de carte de contenu Braze indiquant que vous pouvez ajouter votre propre ID utilisateur en tant que destinataire de test pour tester votre carte de contenu.]({% image_buster /assets/img/react-native/content-card-test.png %} "Content Card Campaign Test")

## Placements des cartes de contenu

Les cartes de contenu peuvent être utilisées de nombreuses façons. Trois implémentations courantes consistent à les utiliser comme centre de messages, comme bannière d'image dynamique ou comme carrousel d'images. Pour chacun de ces placements, vous attribuerez des [paires clé-valeur]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) (la propriété `extras` dans le modèle de données) à vos cartes de contenu et, en fonction des valeurs, ajusterez dynamiquement le comportement, l'apparence ou la fonctionnalité de la carte au moment de l'exécution. 

![]({% image_buster /assets/img_archive/cc_placements.png %}){: style="border:0px;"}

### Boîte de réception de messages

Les cartes de contenu peuvent être utilisées pour simuler un centre de messages. Dans ce format, chaque message est sa propre carte contenant des [paires clé-valeur]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#key-value-pairs) qui alimentent les événements au clic. Ces paires clé-valeur sont les identifiants clés que l'application examine pour décider où rediriger l'utilisateur lorsqu'il clique sur un message de la boîte de réception. Les valeurs des paires clé-valeur sont arbitraires. 

#### Exemple

Par exemple, vous pouvez créer deux cartes de message : un appel à l'action pour inciter les utilisateurs à activer les recommandations de lecture, et un code de coupon destiné à votre nouveau segment d'utilisateurs abonnés.

Les clés telles que `body`, `title` et `buttonText` peuvent comporter des valeurs de chaînes de caractères simples que vos marketeurs peuvent définir. Les clés telles que `terms` peuvent avoir des valeurs fournissant une petite collection de phrases approuvées par votre service juridique. Les clés telles que `style` et `class_type` ont des valeurs de chaînes de caractères que vous pouvez définir pour déterminer le rendu de votre carte sur votre application ou votre site.

{% tabs local %}
{% tab Reading recommendations %}
Paires clé-valeur pour la carte de recommandation de lecture :

| Clé         | Valeur                                                                |
|------------|----------------------------------------------------------------------|
| `body`       | Ajoutez vos centres d'intérêt à votre profil Politer Weekly pour obtenir des recommandations de lecture personnalisées. |
| `style`      | info                                                                 |
| `class_type` | notification_center                                                 |
| `card_priority` | 1                                                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab New subscriber coupon %}
Paires clé-valeur pour un coupon destiné aux nouveaux utilisateurs abonnés :

| Clé         | Valeur                                                            |
|------------|------------------------------------------------------------------|
| `title`      | Abonnez-vous pour bénéficier de jeux illimités                                    |
| `body`       | Offre spéciale de fin d'été - 10 % de réduction sur les jeux Politer              |
| `buttonText` | S'abonner                                                    |
| `style`      | promo                                                            |
| `class_type` | notification_center                                              |
| `card_priority` | 2                                                              |
| `terms`      | new_subscribers_only                                             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

{% details Informations supplémentaires pour Android %}

Dans le SDK Android et FireOS, la logique du centre de messages est pilotée par la valeur `class_type` fournie par les paires clé-valeur de Braze. La méthode [`createContentCardable`]({{site.baseurl}}/developer_guide/content_cards/) vous permet de filtrer et d'identifier ces types de classes.

{% tabs local %}
{% tab Kotlin %}
**Utilisation de `class_type` pour le comportement au clic**<br>
Lorsque nous intégrons les données de la carte de contenu dans nos classes personnalisées, nous utilisons la propriété `ContentCardClass` des données pour déterminer quelle sous-classe concrète doit être utilisée pour stocker les données.

```kotlin
 private fun createContentCardable(metadata: Map<String, Any>, type: ContentCardClass?): ContentCardable?{
        return when(type){
            ContentCardClass.AD -> Ad(metadata)
            ContentCardClass.MESSAGE_WEB_VIEW -> WebViewMessage(metadata)
            ContentCardClass.NOTIFICATION_CENTER -> FullPageMessage(metadata)
            ContentCardClass.ITEM_GROUP -> Group(metadata)
            ContentCardClass.ITEM_TILE -> Tile(metadata)
            ContentCardClass.COUPON -> Coupon(metadata)
            else -> null
        }
    }
```

Ensuite, lors du traitement de l'interaction utilisateur avec la liste des messages, nous utilisons le type de message pour déterminer la vue à afficher à l'utilisateur.

```kotlin
override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //...
        listView.onItemClickListener = AdapterView.OnItemClickListener { parent, view, position, id ->
           when (val card = dataProvider[position]){
                is WebViewMessage -> {
                    val intent = Intent(this, WebViewActivity::class.java)
                    val bundle = Bundle()
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.contentString)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
                is FullPageMessage -> {
                    val intent = Intent(this, FullPageContentCard::class.java)
                    val bundle = Bundle()
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.icon)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.messageTitle)
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.cardDescription)
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        }
    }
```
{% endtab %}
{% tab Java %}
**Utilisation de `class_type` pour le comportement au clic**<br>
Lorsque nous intégrons les données de la carte de contenu dans nos classes personnalisées, nous utilisons la propriété `ContentCardClass` des données pour déterminer quelle sous-classe concrète doit être utilisée pour stocker les données.

```java
private ContentCardable createContentCardable(Map<String, ?> metadata,  ContentCardClass type){
    switch(type){
        case ContentCardClass.AD:{
            return new Ad(metadata);
        }
        case ContentCardClass.MESSAGE_WEB_VIEW:{
            return new WebViewMessage(metadata);
        }
        case ContentCardClass.NOTIFICATION_CENTER:{
            return new FullPageMessage(metadata);
        }
        case ContentCardClass.ITEM_GROUP:{
            return new Group(metadata);
        }
        case ContentCardClass.ITEM_TILE:{
            return new Tile(metadata);
        }
        case ContentCardClass.COUPON:{
            return new Coupon(metadata);
        }
        default:{
            return null;
        }
    }
}

```

Ensuite, lors du traitement de l'interaction utilisateur avec la liste des messages, nous utilisons le type de message pour déterminer la vue à afficher à l'utilisateur.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState)
        //...
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id){
               ContentCardable card = dataProvider.get(position);
               if (card instanceof WebViewMessage){
                    Bundle intent = new Intent(this, WebViewActivity.class);
                    Bundle bundle = new Bundle();
                    bundle.putString(WebViewActivity.INTENT_PAYLOAD, card.getContentString());
                    intent.putExtras(bundle);
                    startActivity(intent);
                }
                else if (card instanceof FullPageMessage){
                    Intent intent = new Intent(this, FullPageContentCard.class);
                    Bundle bundle = Bundle();
                    bundle.putString(FullPageContentCard.CONTENT_CARD_IMAGE, card.getIcon());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_TITLE, card.getMessageTitle());
                    bundle.putString(FullPageContentCard.CONTENT_CARD_DESCRIPTION, card.getCardDescription());
                    intent.putExtras(bundle)
                    startActivity(intent)
                }
            }

        });
    }
```

{% endtab %}
{% endtabs %}
{% enddetails %}

### Carrousel

Vous pouvez intégrer des cartes de contenu dans un flux de carrousel entièrement personnalisé, permettant aux utilisateurs de balayer l'écran pour découvrir d'autres cartes en vedette. Par défaut, les cartes de contenu sont triées par date de création (la plus récente en premier), et vos utilisateurs verront toutes les cartes auxquelles ils ont droit.

Pour mettre en place un carrousel de cartes de contenu :

1. Créez une logique personnalisée qui observe les [changements dans vos cartes de contenu]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#refreshing-the-feed) et gère l'arrivée de nouvelles cartes.
2. Créez une logique personnalisée côté client pour afficher un nombre spécifique de cartes dans le carrousel à un instant donné. Par exemple, vous pouvez sélectionner les cinq premiers objets de cartes de contenu du tableau ou introduire des paires clé-valeur pour créer une logique conditionnelle.

{% alert tip %}
Si vous implémentez un carrousel en tant que flux secondaire de cartes de contenu, veillez à [trier les cartes dans le flux approprié à l'aide de paires clé-valeur]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).
{% endalert %}

### Image seule

Les cartes de contenu n'ont pas besoin de ressembler à des « cartes ». Par exemple, elles peuvent prendre la forme d'une image dynamique affichée en permanence sur votre page d'accueil ou en haut de pages spécifiques.

Pour y parvenir, vos marketeurs créeront une campagne ou une étape du canvas avec une carte de contenu de type **Image Only**. Définissez ensuite les paires clé-valeur appropriées pour utiliser les [cartes de contenu en tant que contenu supplémentaire]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_behavior/#content-cards-as-supplemental-content).