> Lors de la création d'une interface utilisateur personnalisée pour les Content Cards, vous devez enregistrer manuellement les données analytiques telles que les impressions, les clics et les rejets, car cela n'est géré automatiquement que pour les modèles de cartes par défaut. L'enregistrement de ces événements fait partie intégrante de l'intégration des Content Cards et est essentiel pour garantir l'exactitude des rapports et de la facturation des campagnes. Pour ce faire, alimentez votre interface utilisateur personnalisée avec les données provenant des modèles de données Braze, puis enregistrez manuellement les événements. Une fois que vous avez compris comment enregistrer les analyses, vous pouvez découvrir les façons courantes dont les clients de Braze [créent des Content Cards personnalisées]({{site.baseurl}}/developer_guide/content_cards/creating_cards/). 

## Enregistrer les analyses

Lorsque vous implémentez vos Content Cards personnalisées, vous pouvez analyser les objets des cartes de contenu et extraire leurs données utiles, telles que `title`, `cardDescription` et `imageUrl`. Vous pouvez ensuite utiliser les données du modèle résultant pour alimenter votre interface utilisateur personnalisée. 

Pour obtenir les modèles de données des cartes de contenu, abonnez-vous aux mises à jour des cartes de contenu. Deux propriétés méritent une attention particulière :

* **`id`** : Représente la chaîne de caractères de l'ID de la carte de contenu. Il s'agit de l'identifiant unique utilisé pour enregistrer les analyses des Content Cards personnalisées.
* **`extras`** : Englobe toutes les paires clé-valeur du tableau de bord de Braze. 

Toutes les propriétés autres que `id` et `extras` sont facultatives pour l'analyse des Content Cards personnalisées. Pour plus d'informations sur le modèle de données, consultez l'article sur l'intégration de chaque plateforme : [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web).


{% tabs %}
{% tab web %}

Enregistrez une fonction de rappel pour vous abonner aux mises à jour lorsque les cartes sont actualisées.

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
Les Content Cards ne seront actualisées au démarrage de la session que si une demande d'abonnement est appelée avant `openSession()`. Vous pouvez également choisir d'[actualiser manuellement le flux]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/).
{% endalert %}

{% endtab %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

### Étape 1 : Créer une variable privée pour l'utilisateur abonné

Pour vous abonner aux mises à jour des cartes, commencez par déclarer une variable privée dans votre classe personnalisée, qui contiendra votre abonné :

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### Étape 2 : S'abonner aux mises à jour

Ensuite, ajoutez le code suivant pour vous abonner aux mises à jour des Content Cards de Braze, généralement à l'intérieur de la méthode `Activity.onCreate()` de votre activité personnalisée de Content Cards :

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

### Étape 3 : Se désabonner

Nous vous recommandons également de vous désabonner lorsque votre activité personnalisée n'est plus visible. Ajoutez le code suivant à la méthode de cycle de vie `onDestroy()` de votre activité :

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### Étape 1 : Créer une variable privée pour l'utilisateur abonné

Pour vous abonner aux mises à jour des cartes, commencez par déclarer une variable privée dans votre classe personnalisée, qui contiendra votre abonné :

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### Étape 2 : S'abonner aux mises à jour

Ensuite, ajoutez le code suivant pour vous abonner aux mises à jour des Content Cards de Braze, généralement à l'intérieur de la méthode `Activity.onCreate()` de votre activité personnalisée de Content Cards :

```kotlin
// Remove the previous subscriber before rebuilding a new one with our new activity.
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
contentCardsUpdatedSubscriber = IEventSubscriber { event ->
  // List of all Content Cards
  val allCards = event.allCards

  // Your logic below
}
Braze.getInstance(context).subscribeToContentCardsUpdates(contentCardsUpdatedSubscriber)
Braze.getInstance(context).requestContentCardsRefresh(true)
```

### Étape 3 : Se désabonner

Nous vous recommandons également de vous désabonner lorsque votre activité personnalisée n'est plus visible. Ajoutez le code suivant à la méthode de cycle de vie `onDestroy()` de votre activité :

```kotlin
Braze.getInstance(context).removeSingleSubscription(contentCardsUpdatedSubscriber, ContentCardsUpdatedEvent::class.java)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab swift %}

Pour accéder au modèle de données des Content Cards, appelez [`contentCards.cards`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/cards) sur votre instance `braze`.

{% subtabs local %}
{% subtab Swift %}

```swift
let cards: [Braze.ContentCard] = AppDelegate.braze?.contentCards.cards
```

Vous pouvez également gérer un abonnement pour observer les changements dans vos Content Cards. Deux approches sont possibles : 
1. Gérer un objet annulable ; ou 
2. Gérer un `AsyncStream`.

### Annulable 

```swift
// This subscription is maintained through a Braze cancellable, which will observe for changes until the subscription is cancelled.
// You must keep a strong reference to the cancellable to keep the subscription active.
// The subscription is canceled either when the cancellable is deinitialized or when you call its `.cancel()` method.
let cancellable = AppDelegate.braze?.contentCards.subscribeToUpdates { [weak self] contentCards in
  // Implement your completion handler to respond to updates in `contentCards`.
}
```

### AsyncStream

```swift
let stream: AsyncStream<[Braze.ContentCard]> = AppDelegate.braze?.contentCards.cardsStream
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
NSArray<BRZContentCardRaw *> *contentCards = AppDelegate.braze.contentCards.cards;
```

Si vous souhaitez gérer un abonnement à vos cartes de contenu, vous pouvez appeler [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) :

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab react native %}

Pour obtenir les données des Content Cards, utilisez la méthode `getContentCards` :

```javascript
import Braze from "@braze/react-native-sdk";

const cards = await Braze.getContentCards();
```

Pour être informé des mises à jour, abonnez-vous aux événements de mise à jour des Content Cards :

```javascript
const subscription = Braze.addListener(Braze.Events.CONTENT_CARDS_UPDATED, (update) => {
  const cards = update.cards;
  cards.forEach(card => {
    if (card.isControl) {
      // Do not display the control card, but remember to log an impression
    } else {
      // Use card.title, card.cardDescription, card.image, etc.
    }
  });
});
```

Pour demander une actualisation manuelle des Content Cards depuis les serveurs Braze :

```javascript
Braze.requestContentCardsRefresh();
```

Pour obtenir des Content Cards mises en cache sans requête réseau :

```javascript
const cachedCards = await Braze.getCachedContentCards();
```

{% endtab %}
{% endtabs %}

## Enregistrer les événements

L'enregistrement d'indicateurs utiles, tels que les impressions, les clics et les rejets, est simple et rapide. Définissez un écouteur de clic personnalisé pour traiter manuellement ces analyses.

{% tabs %}
{% tab web %}

Enregistrez les événements d'impression lorsque les cartes sont vues par les utilisateurs avec [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions) :

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

Enregistrez les événements de clic lorsque les utilisateurs interagissent avec une carte avec [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick) :

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% tab android %}

Le [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) peut faire référence aux dépendances du SDK Braze, telles que la liste d'objets Content Cards, afin d'obtenir l'objet [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) permettant d'appeler les méthodes de journalisation Braze. Utilisez la classe de base `ContentCardable` pour référencer et fournir facilement des données au `BrazeManager`. 

Pour enregistrer une impression ou un clic sur une carte, appelez respectivement [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) ou [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html). 

Vous pouvez enregistrer manuellement une carte de contenu ou la définir comme « rejetée » dans Braze pour une carte particulière avec [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html). Si une carte est déjà marquée comme rejetée, elle ne peut pas être marquée comme rejetée à nouveau.

Pour créer un écouteur de clic personnalisé, créez une classe qui implémente [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) et enregistrez-la avec [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html). Implémentez la méthode [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html), qui sera appelée lorsque l'utilisateur cliquera sur une Content Card. Ensuite, indiquez à Braze d'utiliser votre écouteur de clic pour les Content Cards. 

{% subtabs local %}
{% subtab Java %}

Par exemple :

```java
BrazeContentCardsManager.getInstance().setContentCardsActionListener(new IContentCardsActionListener() {
  @Override
  public boolean onContentCardClicked(Context context, Card card, IAction cardAction) {
    return false;
  }

  @Override
  public void onContentCardDismissed(Context context, Card card) {

  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

Par exemple :

```kotlin
BrazeContentCardsManager.getInstance().contentCardsActionListener = object : IContentCardsActionListener {
  override fun onContentCardClicked(context: Context, card: Card, cardAction: IAction): Boolean {
    return false
  }

  override fun onContentCardDismissed(context: Context, card: Card) {

  }
}
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Pour gérer la variante de contrôle des Content Cards dans votre interface utilisateur personnalisée, transmettez votre objet [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html), puis appelez la méthode `logImpression` comme vous le feriez avec n'importe quel autre type de Content Card. L'objet enregistrera implicitement une impression de contrôle pour informer nos analyses du moment où un utilisateur aurait vu la carte de contrôle.{% endalert %}

{% endtab %}

{% tab swift %}

Implémentez le protocole [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) et définissez votre objet délégué comme la propriété `delegate` de votre `BrazeContentCardUI.ViewController`. Ce délégué se chargera de transmettre les données de votre objet personnalisé à Braze pour qu'elles soient enregistrées. Pour un exemple, consultez le [tutoriel sur l'interface utilisateur des Content Cards](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

{% subtabs local %}
{% subtab Swift %}

```swift
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate

// Method to implement in delegate
func contentCard(
    _ controller: BrazeContentCardUI.ViewController,
    shouldProcess clickAction: Braze.ContentCard.ClickAction,
    card: Braze.ContentCard
  ) -> Bool {
  // Intercept the content card click action here.
  return true
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// Set the delegate when creating the Content Cards controller
contentCardsController.delegate = delegate;

// Method to implement in delegate
- (BOOL)contentCardController:(BRZContentCardUIViewController *)controller
                shouldProcess:(NSURL *)url
                         card:(BRZContentCardRaw *)card {
  // Intercept the content card click action here.
  return YES;
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Pour gérer la variante de contrôle des Content Cards dans votre interface utilisateur personnalisée, transmettez votre objet [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)), puis appelez la méthode `logImpression` comme vous le feriez avec n'importe quel autre type de Content Card. L'objet enregistrera implicitement une impression de contrôle pour informer nos analyses du moment où un utilisateur aurait vu la carte de contrôle.
{% endalert %}
{% endtab %}

{% tab react native %}

Enregistrez les événements d'impression lorsque les cartes sont consultées par les utilisateurs :

```javascript
Braze.logContentCardImpression(card.id);
```

Enregistrez les événements de clic lorsque les utilisateurs interagissent avec une carte :

```javascript
Braze.logContentCardClicked(card.id);
```

Enregistrez les événements de rejet lorsqu'un utilisateur rejette une carte :

```javascript
Braze.logContentCardDismissed(card.id);
```

{% endtab %}
{% endtabs %}

## Gérer le comportement au clic

{% tabs %}
{% tab web %}

Lorsqu'un utilisateur clique sur une Content Card dans un flux personnalisé, le comportement au clic (comme la navigation vers une URL, la création d'un lien profond ou l'enregistrement d'un événement personnalisé) n'est pas géré automatiquement. Utilisez [`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction) pour traiter l'URL de la carte et exécuter l'action au clic configurée, y compris les actions Braze (URLs `brazeActions://`).

```javascript
import * as braze from "@braze/web-sdk";

// In your card click handler
function onCardClick(card) {
  // Log the click
  braze.logContentCardClick(card);

  // Handle the on-click behavior
  if (card.url) {
    braze.handleBrazeAction(card.url);
  }
}
```

| Paramètre | Description |
|---|---|
| `url` | Une URL valide, ou une URL d'action Braze valide avec le schéma `brazeActions://`. |
| `openLinkInNewTab` | (Facultatif) Indique si l'URL doit s'ouvrir dans un nouvel onglet. Par défaut : `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Si vous n'appelez pas `handleBrazeAction()`, les comportements au clic configurés dans le tableau de bord de Braze (tels que « Enregistrer un événement personnalisé » ou « Naviguer vers une URL ») ne s'exécuteront pas pour les cartes affichées dans un flux personnalisé.
{% endalert %}

{% endtab %}
{% tab android %}

Le comportement au clic est géré automatiquement par l'interface utilisateur par défaut des Content Cards. Pour les implémentations personnalisées, utilisez l'interface [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) décrite dans la section [Enregistrer les analyses](#logging-analytics) ci-dessus.

{% endtab %}
{% tab swift %}

Le comportement au clic est géré automatiquement par l'interface utilisateur par défaut des Content Cards. Pour les implémentations personnalisées, utilisez le protocole [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) décrit dans la section [Enregistrer les analyses](#logging-analytics) ci-dessus.

{% endtab %}
{% endtabs %}