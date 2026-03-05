{% multi_lang_include developer_guide/prerequisites/android.md %}

## Les messages déclenchés

### Types de déclencheurs

Les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre l'un des types d'événements personnalisés suivants : `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, et `Push Click`. Notez que les déclencheurs `Specific Purchase` et `Custom Event` contiennent également des filtres de propriété robustes.

{% alert note %}
Les messages in-app ne peuvent pas être déclenchés par l'API ou par des événements de l'API, mais uniquement par des événements personnalisés enregistrés par le SDK. Pour en savoir plus sur la journalisation, reportez-vous à la section [Journalisation des événements personnalisés]({{site.baseurl}}/developer_guide/analytics/logging_events/).
{% endalert %}

### Sémantiques de livraison

Tous les messages in-app éligibles sont envoyés à l'appareil d'un utilisateur au début de sa session. Lorsqu'il est livré, le SDK prélève les ressources de manière à ce qu'elles soient disponibles au moment du déclenchement, ce qui minimise la latence d'affichage. Si l'événement déclencheur comporte plusieurs messages in-app éligibles, seul le message ayant la priorité la plus élevée sera délivré.

Pour plus d'informations sur la sémantique de démarrage de session du SDK, reportez-vous à la[sectionCycle de vie d']({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android)une session.

### Limite de débit

Par défaut, nous appliquons des limites de débit d’une fois toutes les 30 secondes pour les messages in-app afin de garantir une expérience utilisateur de qualité.

Pour remplacer cette valeur, définissez `com_braze_trigger_action_minimum_time_interval_seconds` dans votre `braze.xml` via :

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Paires clé-valeur

Lorsque vous créez une campagne dans Braze, vous pouvez définir des paires clé-valeur en tant que `extras`, que l'objet de message in-app peut utiliser pour envoyer des données à votre application. Par exemple :

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

Pour empêcher les messages in-app de se déclencher automatiquement :

1. Assurez-vous d’utiliser l’initiateur d’intégration automatique, activé par défaut à partir de la version `2.2.0`.
2. Définissez l’opération par défaut de message in-app `DISCARD` en ajoutant la ligne suivante à votre fichier `braze.xml`.

```xml
<string name="com_braze_flutter_automatic_integration_iam_operation">DISCARD</string>
```

## Déclenchement manuel des messages

Par défaut, les messages in-app sont automatiquement déclenchés lorsque le SDK enregistre un événement personnalisé. Toutefois, vous pouvez déclencher manuellement un message à l'aide des méthodes suivantes.

### Utilisation d'un événement côté serveur

Pour déclencher un message in-app à l'aide d'un événement envoyé par le serveur, envoyez une notification push silencieuse à l'appareil, ce qui permet à un rappel push personnalisé d'enregistrer un événement basé sur le SDK. Cet événement déclenchera alors le message in-app destiné à l'utilisateur.

#### Étape 1 : Créez un rappel de poussée pour recevoir la poussée silencieuse.

Enregistrez [votre rappel personnalisé de push even]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#push-callback) pour écouter une notification push silencieuse spécifique.

Dans l'exemple suivant, deux événements seront enregistrés pour la remise du message in-app, l'un par le serveur et l'autre à partir de votre callback push personnalisé. Pour vous assurer que le même événement n'est pas dupliqué, l'événement consigné dans votre rappel push doit suivre une convention de dénomination générique, par exemple, "événement déclencheur de message in-app", et ne pas porter le même nom que l'événement envoyé par le serveur. Si cela n’est pas fait, la segmentation et les données utilisateur peuvent être affectées par des événements enregistrés en double pour une seule action utilisateur.

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

![Deux ensembles de paires clé-valeur : IS_SERVER_EVENT avec la valeur "true" et CAMPAIGN_NAME avec la valeur "example campaign name".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

Le code exemple de fonction de rappel de notification push reconnaît les paires clé-valeur et enregistre l’événement personnalisé SDK approprié.

Si vous souhaitez inclure les propriétés de l’événement à joindre à votre événement « déclencheur de message in-app », vous pouvez y parvenir en les transmettant dans les paires clé-valeur de la charge utile de la notification push. Dans cet exemple, le nom de campagne du message in-app suivant a été inclus. Votre fonction de rappel de notification push personnalisée peut ensuite transmettre la valeur comme paramètre de la propriété de l’événement lors de l’enregistrement de l’événement personnalisé.

#### Étape 3 : Créer une campagne de communication in-app

Créez votre campagne de messages in-app visibles par l'utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l’événement personnalisé enregistré à partir de la fonction de rappel de notification push  personnalisée.

Dans l’exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété de l’événement dans le cadre de la première notification push silencieuse.

![Une campagne de réception/distribution par événement dans laquelle un message in-app se déclenchera lorsque "campaign_name" sera égal à "Exemple de nom de campagne IAM".]({% image_buster /assets/img_archive/iam_event_trigger.png %})

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
