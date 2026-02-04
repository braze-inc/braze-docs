---
nav_title: Récepteur de diffusion de la Fonction de rappel par notification push
article_title: Fonction de rappel par notification push du récepteur de diffusion personnalisé pour Android
description: "Cet article de référence traite de la création de récepteurs de diffusion personnalisés pour les notifications push Android"
---

# Gestion personnalisée des reçus, ouvertures, rejets et paires clé-valeur de notification push par un récepteur de diffusion {#android-push-listener-broadcast-receiver}

{% alert important %}
L’utilisation d’un `BroadcastReceiver` personnalisé pour les notifications push est obsolète. Utilisez plutôt [` subscribeToPushNotificationEvents()`]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android#android_using-a-callback-for-push-events) à la place.
{% endalert %}

Braze diffuse également des intentions personnalisées lorsque des notifications push sont reçues, ouvertes ou rejetées. Si vous avez un cas d’usage spécifique pour ces scénarios (comme la nécessité d’écouter des paires clé-valeur personnalisées ou une gestion propriétaire des liens profonds), vous devrez écouter ces intentions en créant un `BroadcastReceiver` personnalisé.

## Étape 1 : Enregistrer votre BroadcastReceiver

Enregistrez votre `BroadcastReceiver` personnalisé pour écouter les intentions d'ouverture et de réception de Braze push dans votre [`AndroidManifest.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/custom-broadcast/src/main/AndroidManifest.xml):

```xml
<receiver android:name="YOUR-BROADCASTRECEIVER-NAME" android:exported="false" >
  <intent-filter>
    <action android:name="com.braze.push.intent.NOTIFICATION_RECEIVED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_OPENED" />
    <action android:name="com.braze.push.intent.NOTIFICATION_DELETED" />
  </intent-filter>
</receiver>
```

## Étape 2 : Créer votre BroadcastReceiver

Votre récepteur doit gérer les intentions diffusées par Braze et lancer votre activité avec elles :

- Il devrait sous-classer [`BroadcastReceiver`](https://developer.android.com/reference/android/content/BroadcastReceiver.html) et surcharger `onReceive()`.
- La méthode `onReceive()` doit écouter les intentions diffusées par Braze.
  - Une intention `NOTIFICATION_RECEIVED` sera reçue lorsqu’une notification push arrive.
  - Une intention `NOTIFICATION_OPENED` sera reçue lorsque l’utilisateur clique une notification push.
  - Une intention `NOTIFICATION_DELETED` sera reçue lorsqu’une notification push est rejetée (fermée en la glissant) par l’utilisateur.
- Il doit exécuter votre logique personnalisée pour chacun de ces cas. Si votre récepteur doit ouvrir des liens profonds, assurez-vous de désactiver l’ouverture automatique du lien profond en réglant `com_braze_handle_push_deep_links_automatically` sur `false` dans votre `braze.xml`.

Pour un exemple de récepteur personnalisé détaillé, consultez les extraits de code suivants :

{% tabs %}
{% tab JAVA %}

```java
public class CustomBroadcastReceiver extends BroadcastReceiver {
  private static final String TAG = CustomBroadcastReceiver.class.getName();

  @Override
  public void onReceive(Context context, Intent intent) {
    String pushReceivedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED;
    String notificationOpenedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED;
    String notificationDeletedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_DELETED;

    String action = intent.getAction();
    Log.d(TAG, String.format("Received intent with action %s", action));

    if (pushReceivedAction.equals(action)) {
      Log.d(TAG, "Received push notification.");
    } else if (notificationOpenedAction.equals(action)) {
      BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(context, intent);
    } else if (notificationDeletedAction.equals(action)) {
      Log.d(TAG, "Received push notification deleted intent.");
    } else {
      Log.d(TAG, String.format("Ignoring intent with unsupported action %s", action));
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class CustomBroadcastReceiver : BroadcastReceiver() {
  override fun onReceive(context: Context, intent: Intent) {
    val pushReceivedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_RECEIVED
    val notificationOpenedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_OPENED
    val notificationDeletedAction = Constants.BRAZE_PUSH_INTENT_NOTIFICATION_DELETED

    val action = intent.action
    Log.d(TAG, String.format("Received intent with action %s", action))

    when (action) {
      pushReceivedAction -> {
        Log.d(TAG, "Received push notification.")
      }
      notificationOpenedAction -> {
        BrazeNotificationUtils.routeUserWithNotificationOpenedIntent(context, intent)
      }
      notificationDeletedAction -> {
        Log.d(TAG, "Received push notification deleted intent.")
      }
      else -> {
        Log.d(TAG, String.format("Ignoring intent with unsupported action %s", action))
      }
    }
  }

  companion object {
    private val TAG = CustomBroadcastReceiver::class.java.name
  }
}
```

{% endtab %}
{% endtabs %}

{% alert tip %}
Avec les boutons d’action de notification, les intentions `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` se déclenchent lorsque les boutons avec les actions `opens app` ou `deep link` sont cliqués. La gestion des liens profonds et des compléments reste la même. Les boutons avec des actions `close` ne déclenchent pas les intentions `BRAZE_PUSH_INTENT_NOTIFICATION_OPENED` et rejettent automatiquement la notification.
{% endalert %}

## Étape 3 : Accéder aux paires clé-valeur personnalisées

Les paires clé-valeur personnalisées envoyées soit via le tableau de bord, soit par les API de messagerie seront accessibles dans votre récepteur de diffusion personnalisé, pour quelque raison de votre choix que ce soit :

{% tabs %}
{% tab JAVA %}

```java
// intent is the Braze push intent received by your custom broadcast receiver.
String deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY);

// The extras bundle extracted from the intent contains all custom key-value pairs.
Bundle extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY);

// example of getting specific key-value pair from the extras bundle.
String myExtra = extras.getString("my_key");
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// intent is the Braze push intent received by your custom broadcast receiver.
val deepLink = intent.getStringExtra(Constants.BRAZE_PUSH_DEEP_LINK_KEY)

// The extras bundle extracted from the intent contains all custom key-value pairs.
val extras = intent.getBundleExtra(Constants.BRAZE_PUSH_EXTRAS_KEY)

// example of getting specific key-value pair from the extras bundle.
val myExtra = extras.getString("my_key")
```

{% endtab %}
{% endtabs %}

{% alert note %}
Pour obtenir de la documentation sur les clés de données Braze push, reportez-vous au [SDK Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html?query=object%20Constants).
{% endalert %}

