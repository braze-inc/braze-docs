---
nav_title: Livraison de Message In-App
article_title: Livraison de message dans l'application pour Android/FireOS
page_order: 3
platform:
  - Android
  - Pare-feu
description: "Cet article couvre la livraison de messages dans l'application Android, la liste des différents types de déclenchements, la sémantique de livraison et les étapes de déclenchement d'événements."
channel:
  - messages intégrés à l'application
---

# Envoi de messages dans l'application

## Types de déclenchement

Notre produit de message intégré vous permet de déclencher un affichage de message dans l'application en raison de plusieurs types d'événements différents : `Tout achat`, `Achat spécifique`, `Début de session`, `Événement personnalisé`, `Clic Push`.  De plus, les déclencheurs `Achat spécifique` et `Événement personnalisé` peuvent contenir des filtres de propriétés robustes.

{% alert note %}
Les messages activés dans l'application ne fonctionnent qu'avec les événements personnalisés enregistrés via le SDK et non via les API REST. Si vous travaillez avec Android ou FireOS, consultez comment enregistrer les événements personnalisés [ici]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

## Sémantique de livraison

Tous les messages dans l'application pour lesquels un utilisateur est éligible sont envoyés à l'appareil de l'utilisateur au début de la session. Pour plus d'informations sur la sémantique de démarrage de la session SDK, consultez notre [documentation sur le cycle de vie de la session][84]. Lors de la livraison, le SDK va préextraire les actifs afin qu'ils soient disponibles immédiatement au moment du déclenchement, ce qui minimise la latence d'affichage.

Lorsqu'un événement déclencheur a plus d'un message admissible dans l'application, seul le message dans l'application avec la plus haute priorité sera distribué.

Pour les messages intégrés qui s'affichent immédiatement à la livraison (*i.e.*, session start, push click) il peut y avoir une certaine latence en raison du fait que les actifs ne sont pas prérécupérés.

## Intervalle de temps minimum entre les déclencheurs

Par défaut, nous évaluons la limite des messages dans l'application à une fois toutes les 30 secondes pour assurer une expérience utilisateur de qualité.

Pour remplacer cette valeur, définissez `com_braze_trigger_action_minimum_time_interval_seconds` dans votre `braze.xml` via:

```xml
  <integer name="com_braze_trigger_action_minimum_time_interval_seconds">5</integer>
```

## Déclenchement d'événement côté serveur

Par défaut, les messages dans l'application sont déclenchés par des événements personnalisés enregistrés par le SDK. Si vous souhaitez déclencher des messages dans l'application par des événements envoyés par le serveur, vous pouvez également y arriver.

Pour activer cette fonctionnalité, un push silencieux est envoyé à l'appareil qui permet à un récepteur push personnalisé d'enregistrer un événement basé sur le SDK. Cet événement SDK déclenchera par la suite le message de l'utilisateur dans l'application.

### Étape 1 : Enregistrez un BroadcastReceiver personnalisé pour enregistrer un événement personnalisé

Enregistrez votre `BroadcastReceiver personnalisé` pour écouter une poussée silencieuse spécifique dans votre AndroidManifest.xml. Pour plus d'informations sur comment enregistrer un `BroadcastReceiver personnalisé` veuillez consulter la [documentation push de Braze][78].

### Étape 2 : Créez votre BroadcastReceiver

Votre récepteur gérera l'intention de diffusion par le push silencieux et enregistrera un événement SDK.

Il va sous-classer `BroadcastReceiver` et remplacer `onReceive()`. Pour un exemple détaillé, veuillez consulter notre [EventBroadcastReceiver.java][72] dans la liste liée.

> Deux événements seront enregistrés pour que le message dans l'application soit envoyé, un par le serveur et un par l'intérieur de votre `BroadcastReceiver personnalisé`. Pour s'assurer que le même événement ne soit pas dupliqué, l'évènement enregistré depuis votre `BroadcastReceiver` devrait recevoir une convention de nommage générique, par exemple, "l'évènement de déclenchement de message dans l'application", et pas le même nom que l'événement envoyé par le serveur. Si cela n'est pas fait, la segmentation et les données utilisateur peuvent être affectées par des événements doublons en cours de journalisation pour une seule action utilisateur.

Pour plus de détails sur la gestion personnalisée des reçus push, des ouvertures et des paires clé-valeur, veuillez visiter cette section de notre [Documentation][78].

### Étape 3 : Créer une campagne de push

Créez une campagne de push silencieuse déclenchée via l'événement envoyé par le serveur. Pour plus de détails sur la façon de créer une campagne de push silencieuse, veuillez consulter cette section de notre [Guide de l'Utilisateur][73].

!\[serverEventTrigger\]\[75\]

La campagne "push" doit inclure des extras de la paire "clé-valeur" qui indiquent que cette campagne "push" est envoyée avec l'intention d'enregistrer un événement personnalisé du SDK. Cet événement sera utilisé pour déclencher le message dans l'application.

!\[kvpConfiguration\]\[76\]{: style="max-width:70%;" }

La [EventBroadcastReceiver.java][72] reconnaît les paires clé-valeur et enregistre l'événement personnalisé SDK approprié.

Si vous voulez inclure des propriétés d'événement à joindre à votre événement 'In-App Message Trigger' vous pouvez y parvenir en les transmettant dans les paires clé-valeur du bloc push. Dans l'exemple ci-dessus, le nom de la campagne du message suivant dans l'application a été inclus. Votre `BroadcastReceiver personnalisé` peut alors passer la valeur en tant que paramètre de la propriété événement lors de l'enregistrement de l'événement personnalisé.

### Étape 4 : Créer une campagne de message dans l'application

Créez votre campagne de message dans l'application à partir du tableau de bord de Brase. This campaign should have an Action Based delivery, and be triggered from the custom event logged from within the custom [EventBroadcastReceiver.java][72].

Dans l'exemple ci-dessous, le message spécifique dans l'application à déclencher a été configuré en envoyant la propriété événement dans le cadre de la poussée silencieuse initiale.

!\[serverEventTrigger\]\[77\]

> Si un événement envoyé par un serveur est enregistré alors que l'application n'est pas au premier plan, l'évènement se connectera mais le message dans l'application ne sera pas affiché. Si vous voulez que l'événement soit retardé jusqu'à ce que l'application soit au premier plan, une vérification doit être incluse dans votre récepteur push personnalisé pour rejeter ou retarder l'événement jusqu'à ce que l'application soit entrée au premier plan.

## Messages locaux dans l'application

Les messages intégrés peuvent être créés dans l'application et affichés localement en temps réel. Toutes les options de personnalisation disponibles sur le tableau de bord sont également disponibles localement.  Ceci est particulièrement utile pour afficher les messages que vous souhaitez déclencher dans l'application en temps réel.

{% tabs %}
{% tab JAVA %}

```java
// Initialise un nouveau type de diaporama dans l'application et spécifie son message.
InAppMessageSlideup inAppMessage = new InAppMessageSlideup();
inAppMessage.setMessage("Bienvenue au Brésil ! Ceci est un message glissant dans l'application.");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Initialise un nouveau type de diaporama dans l'application et spécifie son message.
val inAppMessage = InAppMessageSlideup()
inAppMessage.message = "Bienvenue au Brésil! Ceci est un message glissant dans l'application."
```

{% endtab %}
{% endtabs %}

{% alert important %}
Ne pas afficher les messages dans l'application lorsque le clavier logiciel est affiché à l'écran car le rendu n'est pas défini dans cette circonstance.
{% endalert %}

### Déclenchement manuel de l'affichage des messages dans l'application

La méthode suivante affichera manuellement votre message dans l'application.

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
[75]: {% image_buster /assets/img_archive/serverSentPush.png %} [76]: {% image_buster /assets/img_archive/kvpConfiguration.png %} [77]: {% image_buster /assets/img_archive/iam_event_trigger.png %}

[72]: https://gist.github.com/robbiematthews/1d037e2c366e523b2dda5f2e053ea2a9
[73]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/
[78]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#custom-handling-for-push-receipts-opens-dismissals-and-key-value-pairs
[78]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/#custom-handling-for-push-receipts-opens-dismissals-and-key-value-pairs
[84]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle
