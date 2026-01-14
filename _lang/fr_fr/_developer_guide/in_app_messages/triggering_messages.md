---
nav_title: Déclenchement des messages
article_title: Déclencher des messages in-app via le SDK de Braze
page_order: 0.2
description: "Découvrez comment déclencher des messages in-app grâce au SDK de Braze."
platform: 
  - Android
  - FireOS
  - Swift
  - Web
---

# Déclenchement de messages in-app

> Découvrez comment déclencher des messages in-app grâce au SDK de Braze.

## Déclencheurs et réception/distribution de messages

Les messages in-app sont déclenchés lorsque le SDK enregistre l'un des types d'événements personnalisés suivants : `Session Start`, `Push Click`, `Any Purchase`, `Specific Purchase`,et `Custom Event` (les deux derniers contenant des filtres de propriétés robustes).

Au début de la session d'un utilisateur, Braze enverra tous les messages in-app éligibles à son appareil, tout en préemptant simultanément les ressources pour minimiser la latence d'affichage. Si l'événement déclencheur comporte plusieurs messages in-app éligibles, seul le message ayant la priorité la plus élevée sera délivré. Pour plus d'informations, voir [Cycle de vie des sessions]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_sessions/#session-lifecycle).

{% alert note %}
Les messages in-app ne peuvent pas être déclenchés par l'API ou par des événements de l'API, mais uniquement par des événements personnalisés enregistrés par le SDK. Pour en savoir plus sur la journalisation, reportez-vous à la section [Journalisation des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

## Paires clé-valeur

Lorsque vous créez une campagne dans Braze, vous pouvez définir des paires clé-valeur en tant que `extras`, que l'objet de message in-app peut utiliser pour envoyer des données à votre application.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}
```java
Map<String, String> getExtras()
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Pour plus d'informations, reportez-vous au [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}
{% endtab %}

{% tab swift %}
L'exemple suivant utilise une logique personnalisée pour définir la présentation d'un message in-app en fonction de ses paires clé-valeur dans `extras`. Pour un exemple de personnalisation complète, consultez [notre exemple d'application.](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)

{% subtabs %}
{% subtab swift %}

```swift
let customization = message.extras["custom-display"] as? String
if customization == "colorful-slideup" {
  // Perform your custom logic.
}
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
if ([message.extras[@"custom-display"] isKindOfClass:[NSString class]]) {
  NSString *customization = message.extras[@"custom-display"];
  if ([customization isEqualToString:@"colorful-slideup"]) {
    // Perform your custom logic.
  }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  if (inAppMessage instanceof braze.ControlMessage) {
    return braze.showInAppMessage(inAppMessage);
  }


  if (inAppMessage instanceof braze.InAppMessage) {
    const extras = inAppMessage.extras;
    if (extras) {
      for (const key in extras) {
        console.log("key: " + key + ", value: " + extras[key]);
      }
    }
  }
  braze.showInAppMessage(inAppMessage);
});
```
{% endtab %}
{% endtabs %}

## Désactivation des déclencheurs automatiques

Par défaut, les messages in-app se déclenchent automatiquement. Pour désactiver cette fonction :

{% tabs %}
{% tab android %}
1. Vérifiez que vous utilisez l'initialisateur d'intégration automatique, qui est activé par défaut dans les versions `2.2.0` et ultérieures.
2. Définissez l’opération par défaut de message in-app `DISCARD` en ajoutant la ligne suivante à votre fichier `braze.xml`.
    ```xml
    <string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
    ```
{% endtab %}

{% tab swift %}
1. Implémentez le délégué `BrazeInAppMessageUIDelegate` dans votre application. Pour obtenir une présentation complète, consultez [Tutoriel : Message in-app UI](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui).
2. Mettez à jour votre méthode de délégué `inAppMessage(_:displayChoiceForMessage:)` pour qu’elle retourne `.discard`.
{% endtab %}

{% tab web %}
Supprimez l'appel à `braze.automaticallyShowInAppMessages()` dans votre extrait de code, puis créez une logique personnalisée pour gérer l'affichage ou non d'un message in-app.

```javascript
braze.subscribeToInAppMessage(function(inAppMessage) {
  // control group messages should always be "shown"
  // this will log an impression and not show a visible message
  
  if (inAppMessage.isControl) { // v4.5.0+, otherwise use  `inAppMessage instanceof braze.ControlMessage`
     return braze.showInAppMessage(inAppMessage);
  }
  
  // Display the in-app message. You could defer display here by pushing this message to code within your own application.
  // If you don't want to use the display capabilities in Braze, you could alternatively pass the in-app message to your own display code here.
  
  if ( should_show_the_message_according_to_your_custom_logic ) {
      braze.showInAppMessage(inAppMessage);
  } else {
      // do nothing
  }
});
```

{% alert important %}
Si vous appelez `braze.showInAppMessage` sans retirer `braze.automaticallyShowInAppMessages()`, les messages peuvent s'afficher deux fois.
{% endalert %}
{% endtab %}

{% tab Unity %}
{% subtabs %}
{% subtab Android %}
Pour Android, désélectionnez **Afficher automatiquement les messages in-app** dans l'éditeur de configuration de Braze. Vous pouvez également définir `com_braze_inapp_show_inapp_messages_automatically` comme `false` dans le fichier `braze.xml` de votre projet Unity.

Le fonctionnement initial de l'affichage des messages in-app peut être défini dans Braze config à l'aide du "Fonctionnement initial de l'affichage du gestionnaire de messages in-app".
{% endsubtab %}

{% subtab iOS %}
Pour iOS, définissez les auditeurs d'objets de jeu dans l'éditeur de configuration de Braze et assurez-vous que **Braze affiche les messages in-app** n'est pas sélectionné.

Le fonctionnement initial de l'affichage des messages in-app peut être défini dans Braze config à l'aide du "Fonctionnement initial de l'affichage du gestionnaire de messages in-app".
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Dépassement de la limite de débit par défaut

Par défaut, vous pouvez envoyer un message in-app une fois toutes les 30 secondes. Pour outrepasser cela, ajoutez la propriété suivante à votre fichier de configuration avant l'initialisation de l'instance de Braze. Cette valeur sera utilisée comme nouvelle limite de débit en secondes.

{% tabs %}
{% tab android %}
```xml
<integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
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
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                    endpoint:@"<BRAZE_ENDPOINT>"];
// Sets the minimum trigger time interval to 5 seconds
configuration.triggerMinimumTimeInterval = 5;
Braze *braze = [BrazePlugin initBraze:configuration];
AppDelegate.braze = braze;
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
```javascript
// Sets the minimum time interval between triggered in-app messages to 5 seconds instead of the default 30
braze.initialize('YOUR-API-KEY', { minimumIntervalBetweenTriggerActionsInSeconds: 5 })
```
{% endtab %}
{% endtabs %}

## Déclenchement manuel des messages

Par défaut, les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre un événement personnalisé. Toutefois, en plus de cela, vous pouvez déclencher manuellement des messages à l'aide des méthodes suivantes.

### Utilisation d'un événement côté serveur

{% tabs %}
{% tab android %}
Pour déclencher un message in-app à l'aide d'un événement envoyé par le serveur, envoyez une notification push silencieuse à l'appareil, ce qui permet à un rappel push personnalisé d'enregistrer un événement basé sur le SDK. Cet événement déclenchera alors le message in-app destiné à l'utilisateur.

#### Étape 1 : Créez un rappel de poussée pour recevoir la poussée silencieuse.

Enregistrer votre fonction de rappel de notification push personnalisée pour écouter une notification push silencieuse spécifique. Pour plus d'informations, reportez-vous à l'[intégration standard du push Android.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback)

Deux événements seront enregistrés pour que le message in-app soit livré, un par le serveur et l’autre à partir de votre fonction de rappel de notification push personnalisée. Pour vous assurer que le même événement n'est pas dupliqué, l'événement consigné dans votre rappel push doit suivre une convention de dénomination générique, par exemple, "événement déclencheur de message in-app", et ne pas porter le même nom que l'événement envoyé par le serveur. Si cela n’est pas fait, la segmentation et les données utilisateur peuvent être affectées par des événements enregistrés en double pour une seule action utilisateur.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final Bundle kvps = event.getNotificationPayload().getBrazeExtras();
  if (kvps.containsKey("IS_SERVER_EVENT")) {
    BrazeProperties eventProperties = new BrazeProperties();

    // The campaign name is a string extra that clients can include in the push
    String campaignName = kvps.getString("CAMPAIGN_NAME");
    eventProperties.addProperty("campaign_name", campaignName);
    Braze.getInstance(context).logCustomEvent("IAM Trigger", eventProperties);
  }
});
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).subscribeToPushNotificationEvents { event ->
    val kvps = event.notificationPayload.brazeExtras
    if (kvps.containsKey("IS_SERVER_EVENT")) {
        val eventProperties = BrazeProperties()

        // The campaign name is a string extra that clients can include in the push
        val campaignName = kvps.getString("CAMPAIGN_NAME")
        eventProperties.addProperty("campaign_name", campaignName)
        Braze.getInstance(applicationContext).logCustomEvent("IAM Trigger", eventProperties)
    }
}
```

{% endsubtab %}
{% endsubtabs %}

#### Étape 2 : Créer une campagne de notification push

Créez une [campagne de push silencieuse]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) déclenchée par l'événement envoyé par le serveur.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

La campagne de notifications push doit inclure des suppléments de paires clé-valeur qui indiquent que cette campagne de notifications push est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app.

![Deux ensembles de paires clé-valeur : IS_SERVER_EVENT à "true", et CAMPAIGN_NAME à "exemple de nom de campagne".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

Le code exemple de fonction de rappel de notification push reconnaît les paires clé-valeur et enregistre l’événement personnalisé SDK approprié.

Si vous souhaitez inclure les propriétés de l’événement à joindre à votre événement « déclencheur de message in-app », vous pouvez y parvenir en les transmettant dans les paires clé-valeur de la charge utile de la notification push. Dans cet exemple, le nom de campagne du message in-app suivant a été inclus. Votre fonction de rappel de notification push personnalisée peut ensuite transmettre la valeur comme paramètre de la propriété de l’événement lors de l’enregistrement de l’événement personnalisé.

#### Étape 3 : Créer une campagne de communication in-app

Créez votre campagne de messages in-app visibles par l'utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l’événement personnalisé enregistré à partir de la fonction de rappel de notification push  personnalisée.

Dans l’exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété de l’événement dans le cadre de la première notification push silencieuse.

![Une campagne de réception/distribution basée sur des actions où un message in-app se déclenche lorsque "campaign_name" est égal à "IAM campaign name example".]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Si un événement envoyé par le serveur est enregistré alors que l’application n’est pas au premier plan, l’événement se connectera, mais le message in-app ne s’affichera pas. Si vous souhaitez que l’événement soit retardé jusqu’à ce que l’application soit au premier plan, une vérification doit être incluse dans votre récepteur de notification push personnalisé pour rejeter ou retarder l’événement jusqu’à ce que l’application passe au premier plan.
{% endtab %}

{% tab swift %}
#### Étape 1 : Gérer les paires clé-valeur et les notifications push silencieuses

Implémentez la fonction suivante et appelez-la dans la méthode [`application(_:didReceiveRemoteNotification:fetchCompletionHandler:)`](https://developer.apple.com/documentation/uikit/uiapplicationdelegate/1623013-application/) :

{% subtabs %}
{% subtab swift %}

```swift
func handleExtras(userInfo: [AnyHashable : Any]) {
  print("A push was received")
  if userInfo != nil && (userInfo["IS_SERVER_EVENT"] as? String) != nil && (userInfo["CAMPAIGN_NAME"] as? String) != nil {
    AppDelegate.braze?.logCustomEvent("IAM Trigger", properties: ["campaign_name": userInfo["CAMPAIGN_NAME"]])
  }
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)handleExtrasFromPush:(NSDictionary *)userInfo {
  NSLog(@"A push was received.");
  if (userInfo !=nil && userInfo[@"IS_SERVER_EVENT"] !=nil && userInfo[@"CAMPAIGN_NAME"]!=nil) {
    [AppDelegate.braze logCustomEvent:@"IAM Trigger" properties:@{@"campaign_name": userInfo[@"CAMPAIGN_NAME"]}];
  }
};
```

{% endsubtab %}
{% endsubtabs %}

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
{% endtab %}

{% tab web %}
À l'heure actuelle, le SDK Braze ne prend pas en charge le déclenchement manuel de messages à l'aide d'événements côté serveur.
{% endtab %}
{% endtabs %}

### Affichage d'un message prédéfini

Pour afficher manuellement un message in-app prédéfini, utilisez la méthode suivante :

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
```swift
if let inAppMessage = AppDelegate.braze?.inAppMessagePresenter?.nextAvailableMessage() {
  AppDelegate.braze?.inAppMessagePresenter?.present(message: inAppMessage)
}
```
{% endtab %}

{% tab web %}
```javascript
braze.requestInAppMessageDisplay();
```
{% endtab %}
{% endtabs %}

### Affichage d'un message en temps réel 

Vous pouvez également créer et afficher des messages in-app locaux en temps réel, en utilisant les mêmes options de personnalisation que celles disponibles sur le tableau de bord. Pour ce faire :

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endsubtab %}
{% endsubtabs %}

{% alert important %}
N’affichez pas les messages in-app lorsque le clavier logiciel est affiché à l’écran, car le rendu n’est pas défini dans ce cas.
{% endalert %}
{% endtab %}

{% tab swift %}
Appelez manuellement la méthode [`present(message:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/present(message:)) sur votre site `inAppMessagePresenter`. Par exemple :

{% subtabs %}
{% subtab swift %}

```swift
let customInAppMessage = Braze.InAppMessage.slideup(
  .init(message: "YOUR_CUSTOM_SLIDEUP_MESSAGE", slideFrom: .bottom, themes: .defaults)
)
AppDelegate.braze?.inAppMessagePresenter?.present(message: customInAppMessage)
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

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

{% endsubtab %}
{% endsubtabs %}

{% alert note %}
En créant votre propre message in-app, vous vous abonnez à tout suivi analytique et devrez gérer manuellement l'enregistrement des clics et des impressions à l'aide de votre site `message.context`.
{% endalert %}
{% endtab %}

{% tab web %}
```javascript
  // Displays a slideup type in-app message.
  var message = new braze.SlideUpMessage("Welcome to Braze! This is an in-app message.");
  message.slideFrom = braze.InAppMessage.SlideFrom.TOP;
  braze.showInAppMessage(message);
```
{% endtab %}

{% tab Unity %}
Pour afficher le message suivant dans la pile, utilisez la méthode `DisplayNextInAppMessage()`. Les messages seront enregistrés dans cette pile si `DISPLAY_LATER` ou `BrazeUnityInAppMessageDisplayActionType.IAM_DISPLAY_LATER` est choisi comme action d'affichage des messages in-app.

```csharp
Appboy.AppboyBinding.DisplayNextInAppMessage();
```
{% endtab %}
{% endtabs %}

## Messages d'intention de sortie pour le web

Les messages d'intention de sortie sont des messages in-app non perturbateurs utilisés pour communiquer des informations importantes aux visiteurs avant qu'ils ne quittent votre site web.

Pour configurer des déclencheurs pour ces types de messages dans le SDK Web, mettez en œuvre une bibliothèque exit-intent sur votre site web (telle que la [bibliothèque open-source de ouibounce](https://github.com/carlsednaoui/ouibounce)), puis utilisez le code suivant pour enregistrer `'exit intent'` en tant qu'événement personnalisé dans Braze. Désormais, vos futures campagnes de messages in-app peuvent utiliser ce type de message comme déclencheur d'événement personnalisé.

```javascript
  var _ouibounce = ouibounce(false, {
    callback: function() { braze.logCustomEvent('exit intent'); }
  });
```
