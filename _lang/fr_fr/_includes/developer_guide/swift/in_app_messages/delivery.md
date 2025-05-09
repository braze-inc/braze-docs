{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Les messages déclenchés

### Types de déclencheurs

Les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre l'un des types d'événements personnalisés suivants : `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, et `Push Click`. Notez que les déclencheurs `Specific Purchase` et `Custom Event` contiennent également des filtres de propriété robustes.

{% alert note %}
Les messages in-app ne peuvent pas être déclenchés par l'API ou par des événements de l'API, mais uniquement par des événements personnalisés enregistrés par le SDK. Pour en savoir plus sur la journalisation, reportez-vous à la section [Journalisation des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift).
{% endalert %}

### Sémantiques de livraison

Tous les messages in-app éligibles sont envoyés à l'appareil d'un utilisateur au début de sa session. Lorsqu'il est livré, le SDK prélève les ressources de manière à ce qu'elles soient disponibles au moment du déclenchement, ce qui minimise la latence d'affichage. Si l'événement déclencheur comporte plusieurs messages in-app éligibles, seul le message ayant la priorité la plus élevée sera délivré.

Pour plus d'informations sur la sémantique de démarrage de session du SDK, reportez-vous à la[sectionCycle de vie d']({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift)une session.

### Limite de débit par défaut

Par défaut, vous pouvez envoyer un message in-app une fois toutes les 30 secondes.

Pour outrepasser cela, ajoutez la propriété `triggerMinimumTimeInterval` à votre configuration Braze avant l'initialisation de l'instance Braze. Il peut être défini comme un nombre entier positif et représente l'intervalle de temps minimum en secondes. Par exemple :

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "YOUR-APP-IDENTIFIER-API-KEY",
  endpoint: "YOUR-BRAZE-ENDPOINT"
)
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5
let braze = Braze(configuration: configuration) 
AppDelegate.braze = braze
```
{% endtab %}
{% tab OBJECTIF-C %}

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% endtabs %}

## Paires clé-valeur

Lorsque vous créez une campagne dans Braze, vous pouvez définir des paires clé-valeur en tant que `extras`, que l'objet de message in-app peut utiliser pour envoyer des données à votre application. Par exemple :

{% tabs %}
{% tab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```

{% endtab %}
{% endtabs %}

Pour une mise en œuvre complète, vous pouvez vous référer aux exemples de personnalisation des messages in-app dans notre [application Exemple.](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)

## Désactivation des déclencheurs automatiques

Pour empêcher les messages in-app de se déclencher automatiquement :

1. Implémentez le délégué `BrazeInAppMessageUIDelegate` comme décrit dans notre [article iOS ici](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Mettez à jour votre méthode de délégué `inAppMessage(_:displayChoiceForMessage:)` pour qu’elle retourne `.discard`.

## Déclenchement manuel des messages

### Utilisation d'un événement côté serveur

Pour déclencher des messages in-app à l'aide d'événements côté serveur, envoyez une notification push silencieuse à l'appareil pour lui permettre d'enregistrer un événement basé sur le SDK. Cet événement SDK peut ensuite déclencher le message in-app destiné à l'utilisateur.

#### Étape 1 : Gérer les paires clé-valeur et les notifications push silencieuses

Implémentez la fonction suivante et appelez-la dans la méthode [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/) :

{% tabs %}
{% tab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endtab %}
{% endtabs %}

Lorsque la notification push silencieuse est reçue, un événement enregistré par le SDK « in-app message trigger » sera enregistré par rapport au profil utilisateur. 

{% alert important %}
En raison d’un message push utilisé pour enregistrer un événement personnalisé, Braze devra stocker un jeton de notification push pour chaque utilisateur afin de permettre cette solution. Pour les utilisateurs d’iOS, Braze ne stocke un jeton qu’à partir du point où un utilisateur a été invité à l’invite de notification push de l’iOS. Avant cela, l’utilisateur ne sera pas joignable par notification push, et la solution précédente ne sera pas possible.
{% endalert %}

#### Étape 2 : Créez une campagne de push silencieuse

Créez une [campagne de push silencieuse]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift) déclenchée par l'événement envoyé par le serveur. 

![Une campagne de messages in-app de livraison par action qui sera délivrée aux utilisateurs dont les profils utilisateurs ont l'événement personnalisé "server_event".]({% image_buster /assets/img_archive/iosServerSentPush.png %})

La campagne de notification push doit inclure des extras de paires clé-valeur, qui indiquent que cette campagne de notification push est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app.

![Une campagne de messages in-app de réception/distribution basée sur des actions qui comporte deux paires clé-valeur. "CAMPAIGN_NAME" devient "Exemple de nom de message in-app" et IS_SERVER_EVENT" devient "true".]({% image_buster /assets/img_archive/iOSServerPush.png %})

Le code de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)` vérifie la clé `IS_SERVER_EVENT` et enregistrera un événement personnalisé SDK s’il existe.

Vous pouvez modifier le nom de l’événement ou les propriétés d’événement en envoyant la valeur souhaitée dans les options de paires clé-valeur de la charge utile de notification push. Lors de la journalisation de l’événement personnalisé, ces extras peuvent être utilisés comme paramètre du nom de l’événement ou comme propriété de l’événement.

#### Étape 3 : Créer une campagne de communication in-app

Créez votre campagne de messages in-app visibles par l'utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l’événement personnalisé enregistré à partir de la méthode `application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`.

Dans l’exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété de l’événement dans le cadre de la première notification push silencieuse.

![Une campagne de messages in-app basée sur une action qui sera délivrée aux utilisateurs qui effectuent l'événement personnalisé "In-app message trigger" où "campaign_name" est égal à "IAM Campaign Name Example".]({% image_buster /assets/img_archive/iosIAMeventTrigger.png %})

{% alert note %}
Notez que ces messages in-app ne se déclencheront que si la notification push silencieuse est reçue pendant que l’application se trouve au premier plan.
{% endalert %}

### Affichage d'une image prédéfinie

Pour afficher manuellement un message in-app prédéfini, utilisez la méthode suivante :

```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```

### Affichage d'un message en temps réel

Vous pouvez également afficher les messages in-app locaux en temps réel en appelant manuellement la méthode [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) sur votre site `inAppMessagePresenter`. Par exemple :

{% tabs %}
{% tab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
BRZInAppMessageRaw *customInAppMessage = [[BRZInAppMessageRaw alloc] init];
customInAppMessage.type = BRZInAppMessageRawTypeSlideup;
customInAppMessage.message = @"YOUR_CUSTOM_SLIDEUP_MESSAGE";
customInAppMessage.slideFrom = BRZInAppMessageRawSlideFromBottom;
customInAppMessage.themes = @{
  @"light": BRZInAppMessageRawTheme.defaultLight,
  @"dark": BRZInAppMessageRawTheme.defaultDark
};
[AppDelegate.braze.inAppMessagePresenter presentMessage:customInAppMessage];
```

{% endtab %}
{% endtabs %}

{% alert note %}
En créant votre propre message in-app, vous vous abonnez à tout suivi analytique et devrez gérer manuellement l'enregistrement des clics et des impressions à l'aide de votre site `message.context`.
{% endalert %}

## La pile de messages in-app

### Ajout de messages in-app à la pile

Les utilisateurs peuvent recevoir un message in-app dans les situations suivantes :

- Un événement déclencheur de message in-app est déclenché
- Une session est lancée
- L’application est ouverte à partir d’une notification push

Lorsque l'événement déclencheur d'un message in-app est déclenché, il est placé sur une « pile ». Si plusieurs messages in-app sont dans la pile et en attente d’être affichés, Braze affichera le message in-app le plus récemment reçu (dernier entré, premier sorti).

Lorsqu'un utilisateur est éligible pour recevoir un message in-app, le `BrazeInAppMessagePresenter` demande le dernier message in-app de la pile de messages in-app. La pile ne conserve que les messages in-app stockés en mémoire et est effacée entre les lancements de l’application depuis le mode suspendu.

### Retour des messages in-app à la pile

Un message in-app déclenché peut être renvoyé à la pile dans les situations suivantes :

- Le message in-app est déclenché lorsque l’application est en arrière-plan.
- Un autre message in-app est actuellement visible.
- La [méthode de délégation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` a renvoyé `.reenqueue`.

Le message in-app déclenché sera placé en haut de la pile pour un affichage ultérieur lorsqu'un utilisateur est éligible pour recevoir un message in-app.

### Écarter les messages in-app

Un message in-app déclenché sera écarté dans les situations suivantes :

- La [méthode de délégation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb) `inAppMessage(_:displayChoiceForMessage:)` a renvoyé `.discard`.
- L’actif (fichier image ou ZIP) du message in-app n’a pas pu être téléchargé.
- Le message in-app est prêt à être affiché mais a dépassé le délai d'attente.
- L’orientation du appareil ne correspond pas à l’orientation du message in-app déclenché.

Le message in-app sera retiré de la pile. Après avoir été rejeté, le message in-app peut être déclenché ultérieurement par une autre instance de l'événement déclencheur.
