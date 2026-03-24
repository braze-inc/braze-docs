{% multi_lang_include developer_guide/prerequisites/android.md %}

## Déclencheurs de messages

### Types de déclencheurs

Les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre l'un des types d'événements personnalisés suivants : `Any Purchase`, `Specific Purchase`,`Session Start` , `Custom Event`, et `Push Click`. Veuillez noter que les `Specific Purchase`déclencheurs`Custom Event` et contiennent également des filtres de propriétés robustes.

{% alert note %}
Les messages in-app ne peuvent pas être déclenchés par l'API ou par des événements de l'API, mais uniquement par des événements personnalisés enregistrés par le SDK. Pour en savoir plus sur la journalisation, reportez-vous à la section [Journalisation des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Sémantiques de livraison

Tous les messages in-app éligibles sont envoyés sur l'appareil de l'utilisateur au début de sa session. À la livraison, le SDK préchargera les ressources afin qu'elles soient disponibles au moment du déclencheur, ce qui minimisera la latence d'affichage. Si l'événement déclencheur comporte plusieurs messages in-app éligibles, seul le message ayant la priorité la plus élevée sera délivré.

Pour plus d'informations sur la sémantique de démarrage de session du SDK, veuillez [consulter la section Cycle de vie de la session]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android).

### Limite de débit

Par défaut, nous appliquons des limites de débit d’une fois toutes les 30 secondes pour les messages in-app afin de garantir une expérience utilisateur de qualité.

Pour remplacer cette valeur, définissez `com_braze_trigger_action_minimum_time_interval_seconds` dans votre `braze.xml` via :

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Paires clé-valeur

Lorsque vous créez une campagne dans Braze, vous pouvez définir des paires clé-valeur que l'objet de message in-app peut utiliser pour`extras` envoyer des données à votre application. Par exemple :

{% tabs %}
{% tab JAVA %}
```java
Map<String, String> getExtras()
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
extras: Map<String, String>
```
{% endtab %}
{% endtabs %}

{% alert note %}
Pour plus d'informations, consultez le [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html#1498425856%2FProperties%2F-1725759721).
{% endalert %}

## Désactivation des déclencheurs automatiques

Pour éviter que les messages in-app ne se déclenchent automatiquement :

1. Assurez-vous d’utiliser l’initiateur d’intégration automatique, activé par défaut à partir de la version `2.2.0`.
2. Définissez l’opération par défaut de message in-app `DISCARD` en ajoutant la ligne suivante à votre fichier `braze.xml`.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## Déclenchement manuel des messages

Par défaut, les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre un événement personnalisé. Cependant, vous pouvez déclencher manuellement l'envoi d'un message en utilisant les méthodes suivantes.

### Utilisation d'un événement côté serveur

Pour déclencher un message in-app à l'aide d'un événement envoyé par le serveur, envoyez une notification push silencieuse à l'appareil, ce qui permet à un rappel push personnalisé d'enregistrer un événement basé sur le SDK. Cet événement déclenchera alors le message in-app destiné à l'utilisateur.

#### Étape 1 : Créez un rappel de poussée pour recevoir la poussée silencieuse.

Veuillez enregistrer [votre rappel push personnalisé]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback) afin de recevoir une notification push silencieuse spécifique.

Dans l'exemple suivant, deux événements seront enregistrés pour le message in-app à livrer, l'un par le serveur et l'autre à partir de votre rappel push personnalisé. Pour vous assurer que le même événement n'est pas dupliqué, l'événement consigné dans votre rappel push doit suivre une convention de dénomination générique, par exemple, "événement déclencheur de message in-app", et ne pas porter le même nom que l'événement envoyé par le serveur. Si cela n’est pas fait, la segmentation et les données utilisateur peuvent être affectées par des événements enregistrés en double pour une seule action utilisateur.

{% tabs %}
{% tab JAVA %}

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

{% endtab %}
{% tab KOTLIN %}

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

{% endtab %}
{% endtabs %}

#### Étape 2 : Créer une campagne de notification push

Créez une [campagne de push silencieuse]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android) déclenchée par l'événement envoyé par le serveur.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

La campagne de notifications push doit inclure des suppléments de paires clé-valeur qui indiquent que cette campagne de notifications push est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app.

![Deux ensembles de paires clé-valeur :IS_SERVER_EVENTdéfini sur « true » etCAMPAIGN_NAMEdéfini sur « nom de campagne à titre d'exemple ».]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

Le code exemple de fonction de rappel de notification push reconnaît les paires clé-valeur et enregistre l’événement personnalisé SDK approprié.

Si vous souhaitez inclure les propriétés de l’événement à joindre à votre événement « déclencheur de message in-app », vous pouvez y parvenir en les transmettant dans les paires clé-valeur de la charge utile de la notification push. Dans cet exemple, le nom de campagne du message in-app suivant a été inclus. Votre fonction de rappel de notification push personnalisée peut ensuite transmettre la valeur comme paramètre de la propriété de l’événement lors de l’enregistrement de l’événement personnalisé.

#### Étape 3 : Créer une campagne de communication in-app

Créez votre campagne de messages in-app visibles par l'utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l’événement personnalisé enregistré à partir de la fonction de rappel de notification push  personnalisée.

Dans l’exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété de l’événement dans le cadre de la première notification push silencieuse.

![Une campagne de livraison par événement où un message in-app se déclenchera lorsque"campaign_name"  est égal à « exemple de nom de campagne IAM ».]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Si un événement envoyé par le serveur est enregistré alors que l’application n’est pas au premier plan, l’événement se connectera, mais le message in-app ne s’affichera pas. Si vous souhaitez que l’événement soit retardé jusqu’à ce que l’application soit au premier plan, une vérification doit être incluse dans votre récepteur de notification push personnalisé pour rejeter ou retarder l’événement jusqu’à ce que l’application passe au premier plan.

### Affichage d'un message prédéfini

Pour afficher manuellement un message in-app prédéfini, utilisez la méthode suivante :

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().addInAppMessage(inAppMessage)
```

{% endtab %}
{% endtabs %}

### Affichage d'un message en temps réel 

Vous pouvez également créer et afficher des messages in-app locaux en temps réel, en utilisant les mêmes options de personnalisation que celles disponibles sur le tableau de bord. Pour ce faire :

{% tabs %}
{% tab JAVA %}

```java
// Initializes a new slideup type in-app message and specifies its message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Welcome to Braze! This is a slideup in-app message.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initializes a new slideup type in-app message and specifies its message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Welcome to Braze! This is a slideup in-app message."
```

{% endtab %}
{% endtabs %}

{% alert important %}
N’affichez pas les messages in-app lorsque le clavier logiciel est affiché à l’écran, car le rendu n’est pas défini dans ce cas.
{% endalert %}
