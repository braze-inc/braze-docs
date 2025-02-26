---
nav_title: Livraison de messages in-app
article_title: Livraison de messages in-app pour Android et FireOS
page_order: 3
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre la livraison de messages in-app Android et FireOS, répertoriant différents types de déclencheurs, de sémantiques de livraison et d’étapes de déclenchement d’événements."
channel:
  - in-app messages

---

# Livraison de messages in-app

> Cet article de référence couvre la livraison de messages in-app Android et FireOS, répertoriant différents types de déclencheurs, de sémantiques de livraison et d’étapes de déclenchement d’événements.

## Types de déclencheurs

Notre produit de messages in-app vous permet de déclencher un affichage de messages in-app suite à plusieurs types d’événements différents : `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event` et `Push Click`. En outre, les déclencheurs `Specific Purchase` et `Custom Event` peuvent contenir des filtres de propriétés robustes.

{% alert note %}
Les messages in-app déclenchés ne fonctionnent qu’avec des événements personnalisés enregistrés via le SDK de Braze. Les messages in-app peuvent être déclenchés via l’API ou les événements API (comme les événements d’achat). N'oubliez pas de vérifier comment [enregistrer des événements personnalisés]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/).
{% endalert %}

## Sémantiques de livraison

Tous les messages in-app auxquels un utilisateur peut prétendre sont envoyés à l'appareil de l'utilisateur au [début de la session.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle) Dès la livraison, le SDK capture à l’avance les actifs à mettre immédiatement à disponibilité au moment du déclenchement, réduisant ainsi la latence d’affichage.

Lorsqu’un événement déclencheur comporte plus d’un message in-app éligible associé, seul le message in-app avec la priorité la plus élevée sera livré.

Une certaine latence peut se produire pour les messages in-app qui s’affichent immédiatement à la livraison (c.-à-d. au démarrage de la session et lors du clic d’une notification push) en raison de ressources ne faisant pas l’objet d’une capture à l’avance.

## Intervalle de temps minimum entre les déclencheurs

Par défaut, nous appliquons des limites de débit d’une fois toutes les 30 secondes pour les messages in-app afin de garantir une expérience utilisateur de qualité.

Pour remplacer cette valeur, définissez `com_braze_trigger_action_minimum_time_interval_seconds` dans votre `braze.xml` via :

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Déclenchement d’événements côté serveur

Par défaut, les messages in-app sont déclenchés par des événements personnalisés enregistrés par le SDK. Si vous souhaitez déclencher des messages in-app par des événements envoyés par le serveur, vous pouvez également le faire.

Pour activer cette fonction, une notification push silencieuse est envoyée à l’appareil ce qui permet à une fonction de rappel de notification push personnalisé d’enregistrer un événement basé sur le SDK. Cet événement SDK déclenchera ensuite le message in-app pour l’utilisateur.

### Étape 1 : Créez un rappel de poussée pour recevoir la poussée silencieuse.

Enregistrer votre fonction de rappel de notification push personnalisée pour écouter une notification push silencieuse spécifique. Pour plus d'informations, reportez-vous à l'[intégration standard du push Android.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback)

Deux événements seront enregistrés pour que le message in-app soit livré, un par le serveur et l’autre à partir de votre fonction de rappel de notification push personnalisée. Pour vous assurer que le même événement n'est pas dupliqué, l'événement consigné dans votre rappel push doit suivre une convention de dénomination générique, par exemple, "événement déclencheur de message in-app", et ne pas porter le même nom que l'événement envoyé par le serveur. Si cela n’est pas fait, la segmentation et les données utilisateur peuvent être affectées par des événements enregistrés en double pour une seule action utilisateur.

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

### Étape 2 : Créer une campagne de notification push

Créez une [campagne de push silencieuse]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/) déclenchée par l'événement envoyé par le serveur.

![]({% image_buster /assets/img_archive/serverSentPush.png %})

La campagne de notifications push doit inclure des suppléments de paires clé-valeur qui indiquent que cette campagne de notifications push est envoyée pour enregistrer un événement personnalisé SDK. Cet événement sera utilisé pour déclencher le message in-app.

![Deux ensembles de paires clé-valeur : IS_SERVER_EVENT à "true", et CAMPAIGN_NAME à "exemple de nom de campagne".]({% image_buster /assets/img_archive/kvpConfiguration.png %}){: style="max-width:70%;" }

Le code exemple de fonction de rappel de notification push reconnaît les paires clé-valeur et enregistre l’événement personnalisé SDK approprié.

Si vous souhaitez inclure les propriétés de l’événement à joindre à votre événement « déclencheur de message in-app », vous pouvez y parvenir en les transmettant dans les paires clé-valeur de la charge utile de la notification push. Dans cet exemple, le nom de campagne du message in-app suivant a été inclus. Votre fonction de rappel de notification push personnalisée peut ensuite transmettre la valeur comme paramètre de la propriété de l’événement lors de l’enregistrement de l’événement personnalisé.

### Étape 3 : Créer une campagne de communication in-app

Créez votre campagne de messages in-app visibles par l'utilisateur dans le tableau de bord de Braze. Cette campagne doit avoir une livraison par événement et être déclenchée par l’événement personnalisé enregistré à partir de la fonction de rappel de notification push  personnalisée.

Dans l’exemple suivant, le message in-app spécifique à déclencher a été configuré en envoyant la propriété de l’événement dans le cadre de la première notification push silencieuse.

![Une campagne de réception/distribution basée sur des actions où un message in-app se déclenche lorsque "campaign_name" est égal à "IAM campaign name example".]({% image_buster /assets/img_archive/iam_event_trigger.png %})

Si un événement envoyé par le serveur est enregistré alors que l’application n’est pas au premier plan, l’événement se connectera, mais le message in-app ne s’affichera pas. Si vous souhaitez que l’événement soit retardé jusqu’à ce que l’application soit au premier plan, une vérification doit être incluse dans votre récepteur de notification push personnalisé pour rejeter ou retarder l’événement jusqu’à ce que l’application passe au premier plan.

## Messages in-app locaux

Les messages in-app peuvent être créés dans l’application et affichés localement en temps réel. Toutes les options de personnalisation disponibles sur le tableau de bord sont également disponibles localement. Ceci est particulièrement utile pour afficher les messages que vous souhaitez déclencher dans l’application en temps réel.

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

### Déclencher manuellement l’affichage des messages in-app

La méthode suivante affiche manuellement votre message in-app :

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

