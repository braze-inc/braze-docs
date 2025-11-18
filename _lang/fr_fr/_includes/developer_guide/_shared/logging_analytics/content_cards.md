> Lorsque vous créez une interface utilisateur personnalisée pour les cartes de contenu, vous devez consigner manuellement les analyses/analytiques telles que les impressions, les clics et les fermetures, car elles ne sont gérées automatiquement que pour les modèles de cartes par défaut. L'enregistrement de ces événements fait partie intégrante de l'intégration de la carte de contenu et est essentiel à la précision des rapports de campagne et de la facturation. Pour ce faire, alimentez votre interface utilisateur personnalisée avec des données issues des modèles de données de Braze, puis enregistrez manuellement les événements. Une fois que vous avez compris comment enregistrer les analyses/analytiques, vous pouvez voir les façons courantes dont les clients de Braze [créent des cartes de contenu personnalisées]({{site.baseurl}}/developer_guide/content_cards/creating_cards/). 

## Écouter les mises à jour de la carte

Lorsque vous implémentez vos cartes de contenu personnalisées, vous pouvez analyser les objets des cartes de contenu et extraire leurs données utiles, telles que `title`, `cardDescription` et `imageUrl`. Vous pouvez ensuite utiliser les données du modèle résultant pour alimenter votre interface utilisateur personnalisée. 

Pour obtenir les modèles de données des cartes de contenu, abonnez-vous aux mises à jour des cartes de contenu. Deux propriétés doivent faire l'objet d'une attention particulière :

* **`id`**: Conseille la chaîne de caractères de l'ID de la carte de contenu. Il s'agit de l'identifiant unique utilisé pour enregistrer les analyses des cartes de contenu personnalisées.
* **`extras`**: englobe toutes les paires clé-valeur du tableau de bord de Braze. 

Toutes les propriétés autres que `id` et `extras` sont facultatives pour analyser les cartes de contenu personnalisées. Pour plus d'informations sur le modèle de données, consultez l'article sur l'intégration de chaque plateforme : [Android]({{site.baseurl}}/developer_guide/content_cards/?sdktab=android), [iOS]({{site.baseurl}}/developer_guide/content_cards/?sdktab=swift), [Web.]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web)


{% tabs %}
{% tab android %}
{% subtabs local %}
{% subtab Java %}

### Étape 1 : Créez une variable privée pour l'utilisateur abonné

Pour vous abonner aux mises à jour des cartes, commencez par déclarer une variable privée dans votre classe personnalisée, qui contiendra votre abonné :

```java
// subscriber variable
private IEventSubscriber<ContentCardsUpdatedEvent> mContentCardsUpdatedSubscriber;
```

### Étape 2 : S'abonner aux mises à jour

Ensuite, ajoutez le code suivant pour vous abonner aux mises à jour de cartes de contenu de Braze, généralement à l’intérieur de vos activités personnalisées de carte de contenu `Activity.onCreate()` :

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

### Étape 3 : Se désabonner

Nous vous recommandons également de vous désabonner lorsque votre activité personnalisée n’est plus visible. Ajoutez le code suivant à la méthode de cycle de vie `onDestroy()` de votre activité :

```java
Braze.getInstance(context).removeSingleSubscription(mContentCardsUpdatedSubscriber, ContentCardsUpdatedEvent.class);
```

{% endsubtab %}
{% subtab Kotlin %}

### Étape 1 : Créez une variable privée pour l'utilisateur abonné

Pour vous abonner aux mises à jour des cartes, commencez par déclarer une variable privée dans votre classe personnalisée, qui contiendra votre abonné :

```kotlin
private var contentCardsUpdatedSubscriber: IEventSubscriber<ContentCardsUpdatedEvent>? = null
```

### Étape 2 : S'abonner aux mises à jour

Ensuite, ajoutez le code suivant pour vous abonner aux mises à jour de cartes de contenu de Braze, généralement à l’intérieur de vos activités personnalisées de carte de contenu `Activity.onCreate()` :

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

### Étape 3 : Se désabonner

Nous vous recommandons également de vous désabonner lorsque votre activité personnalisée n’est plus visible. Ajoutez le code suivant à la méthode de cycle de vie `onDestroy()` de votre activité :

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

En outre, vous pouvez également gérer un abonnement pour observer les changements dans vos cartes de contenu. Vous pouvez le faire de deux manières : 
1. Gestion d'une possibilité d'annulation ou 
2. Gestion d'un `AsyncStream`.

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

En outre, si vous souhaitez gérer un abonnement à vos cartes de contenu, vous pouvez appeler [`subscribeToUpdates`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/subscribetoupdates(_:)) :

```objc
// This subscription is maintained through Braze cancellable, which will continue to observe for changes until the subscription is cancelled.
BRZCancellable *cancellable = [self.braze.contentCards subscribeToUpdates:^(NSArray<BRZContentCardRaw *> *contentCards) {
  // Implement your completion handler to respond to updates in `contentCards`.
}];
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
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
Les cartes de contenu ne seront actualisées au démarrage de la session que si une demande d'abonnement est appelée avant `openSession()`. Vous pouvez également choisir d'[actualiser manuellement le flux]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/).
{% endalert %}

{% endtab %}
{% endtabs %}

## Enregistrer les événements

L'enregistrement d'indicateurs utiles, tels que les impressions, les clics et les rejets, est simple et rapide. Définissez un écouteur de clic personnalisé pour traiter manuellement ces analyses.

{% tabs %}
{% tab android %}

Les [`BrazeManager`](https://github.com/braze-inc/braze-growth-shares-android-demo-app/blob/main/app/src/main/java/com/braze/advancedsamples/BrazeManager.kt) peut faire référence aux dépendances du SDK de Braze, telles que la liste des tableaux d'objets de la carte de contenu, afin d'obtenir l'information nécessaire à l'appel des méthodes de journalisation de Braze. [`Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) pour appeler les méthodes de journalisation de Braze. Utilisez la classe de base `ContentCardable` pour référencer et fournir facilement des données à `BrazeManager`. 

Pour enregistrer une impression ou cliquer sur une carte, appelez le [`Card.logClick()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-click.html) ou [`Card.logImpression()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/log-impression.html) respectivement. 

Vous pouvez enregistrer manuellement une carte de contenu ou la définir comme "fermée" à Braze pour une carte particulière avec [`isDismissed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/is-dismissed.html). Si une carte est déjà marquée comme étant rejetée, elle ne peut pas être marquée comme étant de nouveau rejetée.

Pour créer un récepteur de clic personnalisé, créez une classe qui met en œuvre la fonction [`IContentCardsActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/index.html) et enregistrez-la auprès de [`BrazeContentCardsManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.managers/-braze-content-cards-manager/index.html). Implémentez la méthode [`onContentCardClicked()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards.listeners/-i-content-cards-action-listener/on-content-card-clicked.html) qui sera appelée lorsque l'utilisateur cliquera sur une carte de contenu. Ensuite, demandez à Braze d'utiliser votre carte de contenu en tant qu'auditeur de clics. 

{% subtabs local %}
{% subtab Java %}

Par exemple :

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

Par exemple :

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
Pour gérer la variante de contrôle des cartes de contenu dans votre interface utilisateur personnalisée, transmettez votre objet [`com.braze.models.cards.Card`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/index.html) puis appelez la méthode `logImpression` comme vous le feriez avec n'importe quel autre type de carte de contenu. L'objet enregistrera implicitement une impression de contrôle pour informer notre analyse du moment où un utilisateur aurait vu la carte de contrôle.{% endalert %}

{% endtab %}
{% tab swift %}

Implémentez le protocole [`BrazeContentCardUIViewControllerDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazecontentcarduiviewcontrollerdelegate) et définissez votre objet délégué comme la propriété `delegate` de votre `BrazeContentCardUI.ViewController`. Ce délégué se chargera de transmettre les données de votre objet personnalisé à Braze pour qu'elles soient enregistrées. Pour un exemple, voir le [tutoriel sur l'interface utilisateur des cartes de contenu](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c2-contentcardsui/).

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
Pour gérer la variante de contrôle des cartes de contenu dans votre interface utilisateur personnalisée, transmettez votre objet [`Braze.ContentCard.Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/control(_:)) puis appelez la méthode `logImpression` comme vous le feriez avec n'importe quel autre type de carte de contenu. L'objet enregistrera implicitement une impression de contrôle pour informer notre analyse/analytique du moment où un utilisateur aurait vu la carte de contrôle.
{% endalert %}
{% endtab %}

{% tab web %}

Enregistrer les événements d’impression lorsque les cartes sont vues par des utilisateurs avec [`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions) :

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardImpressions([card1, card2, card3]);
```

Enregistrer les événements de clic sur la carte lorsque les utilisateurs interagissent avec une carte avec [`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick) :

```javascript
import * as braze from "@braze/web-sdk";

braze.logContentCardClick(card);
```

{% endtab %}
{% endtabs %}
