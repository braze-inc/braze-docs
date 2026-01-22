{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Utilisation d'un rappel pour les événements de type "push" (pousser) {#push-callback}

Braze propose une fonction de rappel [`subscribeToPushNotificationEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-push-notification-events.html) pour la réception, l’ouverture ou le rejet des notifications push. Nous vous recommandons de placer cette fonction de rappel dans votre `Application.onCreate()` pour ne manquer aucun événement survenant lorsque votre application n’est pas en fonctionnement.

{% alert note %}
Si vous utilisiez un Récepteur de diffusion personnalisé pour cette fonctionnalité dans votre application, vous pouvez le supprimer en toute sécurité pour adopter cette option d’intégration.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).subscribeToPushNotificationEvents(event -> {
  final BrazeNotificationPayload parsedData = event.getNotificationPayload();

  //
  // The type of notification itself
  //
  final boolean isPushOpenEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_OPENED;
  final boolean isPushReceivedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_RECEIVED;
  // Sent when a user has dismissed a notification
  final boolean isPushDeletedEvent = event.getEventType() == BrazePushEventType.NOTIFICATION_DELETED;

  //
  // Notification data
  //
  final String pushTitle = parsedData.getTitleText();
  final Long pushArrivalTimeMs = parsedData.getNotificationReceivedTimestampMillis();
  final String deeplink = parsedData.getDeeplink();

  //
  // Custom KVP data
  //
  final String myCustomKvp1 = parsedData.getBrazeExtras().getString("my first kvp");
  final String myCustomKvp2 = parsedData.getBrazeExtras().getString("my second kvp");
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).subscribeToPushNotificationEvents { event ->
    val parsedData = event.notificationPayload

    //
    // The type of notification itself
    //
    val isPushOpenEvent = event.eventType == BrazePushEventType.NOTIFICATION_OPENED
    val isPushReceivedEvent = event.eventType == BrazePushEventType.NOTIFICATION_RECEIVED
    // Sent when a user has dismissed a notification
    val isPushDeletedEvent = event.eventType == BrazePushEventType.NOTIFICATION_DELETED

    //
    // Notification data
    //
    val pushTitle = parsedData.titleText
    val pushArrivalTimeMs = parsedData.notificationReceivedTimestampMillis
    val deeplink = parsedData.deeplink

    //
    // Custom KVP data
    //
    val myCustomKvp1 = parsedData.brazeExtras.getString("my first kvp")
    val myCustomKvp2 = parsedData.brazeExtras.getString("my second kvp")
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Avec les boutons d’action de notification, les intentions `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` se déclenchent lorsque les boutons avec les actions `opens app` ou `deep link` sont cliqués. La gestion des liens profonds et des compléments reste la même. Les boutons avec des actions `close` ne déclenchent pas les intentions `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` et rejettent automatiquement la notification.
{% endalert %}

{% alert important %}
Créez votre listener de notification push dans `Application.onCreate` pour vous assurer que votre listener est déclenché après qu'un utilisateur final ait tapé une notification alors que votre application est dans un état terminé.
{% endalert %}

## Personnalisation de l'affichage des notifications {#customization-display}

### Étape 1 : Créer votre fabrique de notification personnalisée

Dans certains scénarios, vous pourriez désirer personnaliser les notifications push d’une manière qui pourrait être encombrante ou non disponible côté serveur. Pour vous donner un contrôle complet de l'affichage des notifications, nous avons ajouté la possibilité de définir vos propres objets de notification. [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) pour créer des objets de notification qui seront affichés par Braze.

Si une `IBrazeNotificationFactory` personnalisée est définie, Braze appellera la méthode `createNotification()` de votre fabrique lors de la réception de la notification push avant qu’elle ne soit affichée à l’utilisateur. Braze transmettra un `Bundle` contenant les données de notification push Braze et un autre `Bundle` contenant les paires clé-valeur personnalisées envoyées soit via le tableau de bord soit par les API de messagerie :

Braze transmettra un fichier [`BrazeNotificationPayload`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html) contenant les données de la notification push de Braze.

{% tabs %}
{% tab JAVA %}

```java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
  // Example of getting notification title
  String title = brazeNotificationPayload.getTitleText();

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
  // Example of getting notification title
  val title = brazeNotificationPayload.getTitleText()

  // Example of retrieving a custom KVP ("my_key" -> "my_value")
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my_key")
}
```

{% endtab %}
{% endtabs %}

Vous pouvez renvoyer `null` à partir de votre méthode `createNotification()` personnalisée pour ne pas afficher du tout la notification, utiliser `BrazeNotificationFactory.getInstance().createNotification()` pour obtenir notre objet `notification` par défaut pour ces données et le modifier avant l'affichage, ou générer un objet `notification` complètement séparé pour l'affichage.

{% alert note %}
Pour obtenir de la documentation sur les clés de données Braze push, reportez-vous au [SDK Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html).
{% endalert %}

### Étape 2 : Définir votre fabrique de notification personnalisée

Pour demander à Braze d’utiliser votre fabrique de notification personnalisée, utilisez la méthode `setCustomBrazeNotificationFactory` afin de définir votre [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) :

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

L’endroit recommandé pour définir votre `IBrazeNotificationFactory` personnalisée est dans la méthode de cycle de vie de l’application `Application.onCreate()` (pas activité). Cela permettra à la fabrique de notification d’être correctement définie chaque fois que le processus de votre application est actif.

{% alert important %}
La création de votre propre notification à partir de zéro est un cas d'utilisation avancé et ne doit être effectuée qu'après des tests approfondis et une compréhension approfondie de la fonctionnalité push de Braze. Par exemple, vous devez vous assurer que vos journaux de notifications push s'ouvrent correctement.
{% endalert %}

Pour annuler la définition de votre [`IBrazeNotificationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html) personnalisée et revenir à la gestion par défaut de Braze pour les notifications push, transmettez `null` à notre système de définition de fabrique de notification personnalisée :

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## Rendu d'un texte multicolore

Dans le SDK Braze version 3.1.1, du HTML peut être envoyé à un appareil pour afficher du texte multicolore dans les notifications push.

![Un envoi de messages Android "Multicolor Push test message" où les lettres sont de différentes couleurs, en italique et avec une couleur de fond.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

Cet exemple est affiché avec le code HTML suivant :

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>

<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Gardez à l'esprit qu'Android limite les éléments et les tags HTML valides dans vos notifications push. Par exemple, `marquee` n’est pas autorisé.

{% alert important %}
Le rendu du texte multicolore est spécifique à l'appareil et peut ne pas s'afficher en fonction de l'appareil ou de la version d'Android.
{% endalert %}

Pour rendre le texte multicolore dans une notification push, vous pouvez mettre à jour votre `braze.xml` ou `BrazeConfig`:

{% tabs local %}
{% tab braze.xml %}
Ajoutez ce qui suit dans votre `braze.xml` :

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```
{% endtab %}

{% tab BrazeConfig %}
Ajoutez ce qui suit dans votre [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs local %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Tags HTML pris en charge

À l'heure actuelle, Google ne répertorie pas les étiquettes HTML prises en charge pour Android directement dans sa documentation. Cette information ne peut être trouvée que dans [le fichier `Html.java` de son dépôt Git](https://android.googlesource.com/platform/frameworks/base/+/master/core/java/android/text/Html.java). Gardez cela à l'esprit lorsque vous vous référez au tableau suivant, car ces informations ont été extraites de ce fichier et les tags HTML pris en charge peuvent être modifiés.

<table>
  <thead>
    <tr>
      <th>Catégorie</th>
      <th>Étiquette HTML</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="7">Style de texte de base</td>
      <td><code>&lt;b&gt;</code>, <code>&lt;strong&gt;</code></td>
      <td>Texte en gras</td>
    </tr>
    <tr>
      <td><code>&lt;i&gt;</code>, <code>&lt;em&gt;</code></td>
      <td>Texte en italique</td>
    </tr>
    <tr>
      <td><code>&lt;u&gt;</code></td>
      <td>Souligner le texte</td>
    </tr>
    <tr>
      <td><code>&lt;s&gt;</code>, <code>&lt;strike&gt;</code>, <code>&lt;del&gt;</code></td>
      <td>Texte barré</td>
    </tr>
    <tr>
      <td><code>&lt;sup&gt;</code></td>
      <td>Texte en exposant</td>
    </tr>
    <tr>
      <td><code>&lt;sub&gt;</code></td>
      <td>Texte en indice</td>
    </tr>
    <tr>
      <td><code>&lt;tt&gt;</code></td>
      <td>Texte monospace</td>
    </tr>
    <tr>
      <td rowspan="3">Taille/Police</td>
      <td><code>&lt;big&gt;</code>, <code>&lt;small&gt;</code></td>
      <td>Modification de la taille relative du texte</td>
    </tr>
    <tr>
      <td><code>&lt;font color="..."&gt;</code></td>
      <td>Définit la couleur d'avant-plan</td>
    </tr>
    <tr>
      <td><code>&lt;span&gt;</code> (avec insertion CSS)</td>
      <td>Styles en ligne (e.g., couleur, arrière-plan)</td>
    </tr>
    <tr>
      <td rowspan="4">Paragraphe et bloc</td>
      <td><code>&lt;p&gt;</code>, <code>&lt;div&gt;</code></td>
      <td>Sections au niveau des blocs</td>
    </tr>
    <tr>
      <td><code>&lt;br&gt;</code></td>
      <td>Retour à la ligne</td>
    </tr>
    <tr>
      <td><code>&lt;blockquote&gt;</code></td>
      <td>Bloc cité</td>
    </tr>
    <tr>
      <td><code>&lt;ul&gt;</code> + <code>&lt;li&gt;</code></td>
      <td>Liste non ordonnée avec puces</td>
    </tr>
    <tr>
      <td>Rubriques</td>
      <td><code>&lt;h1&gt;</code> - <code>&lt;h6&gt;</code></td>
      <td>Titres (différentes tailles)</td>
    </tr>
    <tr>
      <td rowspan="2">Liens et images</td>
      <td><code>&lt;a href="..."&gt;</code></td>
      <td>Lien cliquable</td>
    </tr>
    <tr>
      <td><code>&lt;img src="..."&gt;</code></td>
      <td>Image incorporée</td>
    </tr>
    <tr>
      <td>Autres en ligne</td>
      <td><code>&lt;em&gt;</code>, <code>&lt;strong&gt;</code>, <code>&lt;dfn&gt;</code>, <code>&lt;cite&gt;</code></td>
      <td>Synonymes de italique ou gras</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Rendu des images en ligne

### Fonctionnement

Vous pouvez présenter une image plus grande dans votre notification push Android à l'aide de la fonction inline image push. Avec cette conception, les utilisateurs n’auront pas à étendre manuellement la notification push pour agrandir l’image. Contrairement aux notifications push standard pour Android, les images des notifications push d’image insérée ont un rapport hauteur/largeur de 3:2.

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="max-width:50%;"}

### Compatibilité

Bien que vous puissiez envoyer des images en ligne à n'importe quel appareil, les appareils et les SDK qui ne respectent pas les versions minimales afficheront une image standard à la place. Pour que les images en ligne s'affichent correctement, le SDK Android Braze v10.0.0+ et un appareil fonctionnant sous Android M+ sont nécessaires. Le SDK doit également être activé pour que l'image soit rendue.

{% alert note %}
Les appareils fonctionnant sous Android 12 s’afficheront différemment en raison des modifications dans les styles personnalisés de notification push.
{% endalert %}

### Envoi d'un push d'image en ligne

Lors de la création d'un message push Android, cette fonctionnalité est disponible dans le menu déroulant **Type de notification**.

![L'éditeur de campagne push montrant l'emplacement du menu déroulant "Type de notification" (au-dessus de l'aperçu push standard).]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})

## Paramètres

De nombreux paramètres avancés sont disponibles pour les notifications push Android envoyées via le tableau de bord de Braze. Le présent article décrit ces fonctionnalités et la manière de les utiliser avec succès.

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### ID de notification {#notification-id}

Un **ID de notification** est un identifiant unique pour une catégorie de message de votre choix qui informe le service de messagerie de ne respecter que le message le plus récent de cet ID. Définir un ID de notification vous permet d’envoyer uniquement le message le plus récent et le plus pertinent, plutôt qu’une pile de données obsolètes et non pertinentes.

### Priorité de livraison d’envoi de message Firebase {#fcm-priority}

Le champ [Priorité d'envoi/distribution de la messagerie Firebase](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) vous permet de contrôler si un push est envoyé avec une priorité "normale" ou "élevée" à la messagerie Firebase Cloud.

### TTL (Durée de vie) {#ttl}

Le champ **Durée en vie** (TTL) vous permet de définir une durée personnalisée de stockage des messages avec le service de messagerie push. Les valeurs par défaut pour la durée de vie sont de quatre semaines pour FCM et de 31 jours pour ADM.

### Texte récapitulatif {#summary-text}

Le texte récapitulatif vous permet de définir un texte supplémentaire dans la vue de notification étendue. Il sert également de légende pour les notifications avec des images.

![Un message Android avec le titre "Ceci est le titre de la notification" et le texte résumé "Ceci est le texte résumé de la notification".]({% image_buster /assets/img/android/push/collapsed-android-notification.png %}){: style="max-width:65%;"}

Le texte récapitulatif s’affiche sous le corps du message dans la vue étendue. 

![Un message Android avec le titre "Ceci est le titre de la notification" et le texte résumé "Ceci est le texte résumé de la notification".]({% image_buster /assets/img/android/push/expanded-android-notification.png %}){: style="max-width:65%;"}

Pour les notifications push qui incluent des images, le texte du message s’affiche dans la vue réduite tandis que le texte récapitulatif s’affiche comme légende d’image lorsque la notification est étendue. 

### URI personnalisés {#custom-uri}

La fonctionnalité **URI personnalisé** vous permet de spécifier une URL Web ou une ressource Android vers laquelle naviguer lorsque l'on clique sur la notification. Si aucun URI personnalisé n’est spécifié, cliquer sur la notification amène les utilisateurs dans votre application. Vous pouvez utiliser l’URI personnalisé pour créer un lien profond à l’intérieur de votre application et diriger les utilisateurs vers des ressources qui existent en dehors de votre application. Ceci peut être spécifié via l'[API Messages]({{site.baseurl}}/api/endpoints/messaging/) ou notre tableau de bord sous **Paramètres avancés** dans le compositeur de push comme illustré :

![La création de liens profonds avancement dans le compositeur poussoir Braze.]({% image_buster /assets/img_archive/deep_link.png %})

### Priorité d’affichage de la notification {#notification-priority}

{% alert important %}
Le paramètre de priorité d’affichage de notification n’est plus utilisé sur les appareils exécutant Android O ou plus récents. Pour les appareils plus récents, définissez la priorité par le biais de la [configuration du canal de notification.](https://developer.android.com/training/notify-user/channels#importance)
{% endalert %}

Le niveau de priorité d’une notification push affecte la manière dont votre notification est affichée dans la barre de notification par rapport à d’autres notifications. Il peut également affecter la vitesse et la manière de livrer, car les messages normaux et moins prioritaires peuvent être envoyés avec une latence légèrement plus élevée ou groupés pour préserver la durée de vie de la batterie, alors que les messages haute priorité sont toujours envoyés immédiatement.

Dans Android O, la priorité de notification est devenue une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir la priorité d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos sons de notification. Pour les appareils exécutant des versions d'Android antérieures à O, la spécification d'un niveau de priorité pour les notifications Android est possible via le tableau de bord de Braze et l'API d'envoi de messages. 

Pour envoyer un message à l'ensemble de votre base d'utilisateurs avec une priorité spécifique, nous vous recommandons de spécifier indirectement la priorité via la [configuration du canal de communication](https://developer.android.com/training/notify-user/channels#importance) (pour cibler les appareils O+) *et d'* envoyer la priorité individuelle à partir du tableau de bord (pour cibler les appareils <O).

Les niveaux de priorité que vous pouvez définir sur les notifications push Android ou Fire OS sont les suivants :

| Priorité | Description ou utilisation prévue | Valeur de `priority` (pour les messages API) |
|----------|--------------------------|-------------------------------------|
| Max      | Messages urgents ou à délai de réponse critique | `2` |
| Élevée     | Communication importante, telle que le nouveau message d’un ami | `1` |
| Par défaut  | La plupart des notifications : utilisez « par défaut » si votre message ne tombe pas explicitement dans les autres types de priorité | `0` |
| Faible      | Informations que vous voulez que les utilisateurs connaissent, mais ne nécessitant pas d’action immédiate | `-1` |
| Min      | Informations contextuelles ou d’arrière-plan. | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour plus d'informations, consultez la documentation de Google sur [les notifications Android](http://developer.android.com/design/patterns/notifications.html).

### Sons {#sounds}

Dans Android O, les sons de notification sont devenus une propriété des canaux de notification. Vous devrez travailler avec votre développeur pour définir le son d’un canal pendant sa configuration, puis utiliser le tableau de bord pour sélectionner le canal approprié lors de l’envoi de vos notifications.

Pour les appareils fonctionnant dans des versions d’Android antérieures à O, Braze vous permet de définir le son d’un message de notification push individuel via le composeur du tableau de bord. Vous pouvez le faire en spécifiant une ressource sonore locale sur l'appareil (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`). Spécifier « par défaut » dans ce champ jouera le son de notification par défaut sur l’appareil. Cela peut être spécifié via l'[API Messages]({{site.baseurl}}/api/endpoints/messaging/) ou le tableau de bord sous **Paramètres avancés** dans le compositeur de push.

![Le réglage avancé du son dans le compositeur poussoir de Braze.]({% image_buster /assets/img_archive/sound_android.png %})

Saisissez l'URI complet de la ressource sonore (par exemple, `android.resource://com.mycompany.myapp/raw/mysound`) dans l'invite du tableau de bord.

Pour envoyer un message à l'ensemble de votre base d'utilisateurs avec un son spécifique, nous vous recommandons de spécifier indirectement le son via la [configuration du canal de communication](https://developer.android.com/training/notify-user/channels) (pour cibler les appareils O+) *et d'* envoyer le son individuel à partir du tableau de bord (pour cibler les appareils <O).
