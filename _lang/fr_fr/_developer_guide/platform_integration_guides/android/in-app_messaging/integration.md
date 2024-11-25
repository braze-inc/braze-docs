---
nav_title: Intégration
article_title: Intégration de message in-app pour Android et FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "Cet article de référence explique comment intégrer les messages in-app dans votre application Android ou FireOS."
channel:
  - in-app messages
search_rank: 2
---

# Intégration de message in-app

> Cet article de référence explique comment intégrer les messages in-app dans votre application Android ou FireOS.

Les [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) vous aident à transmettre du contenu à vos utilisateurs sans interrompre leur journée avec une notification push. Des messages in-app personnalisés et adaptés améliorent l’expérience utilisateur et aident votre audience à tirer le meilleur parti de votre application. Avec plusieurs mises en page et outils de personnalisation, les messages in-app impliquent plus que jamais vos utilisateurs.

Pour voir des exemples d'envois de messages in-app, consultez nos [études de cas.](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html)

## Types de messages in-app

Braze propose plusieurs types de messages in-app par défaut, chacun personnalisable avec des messages, des images, des icônes [Font Awesome](https://fontawesome.com/icons?d=gallery&p=2), des actions de clic, des analyses, des styles modifiables et des schémas de couleurs. Les types actuellement disponibles sont :

- [`Slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html)
- [`Modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html)
- [`Full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html)
- [`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html)

Il est également possible de définir votre propre [affichage personnalisé des messages in-app.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-view-factory)

Tous les messages in-app implémentent l'interface [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html), qui définit tous les comportements et caractéristiques de base des messages in-app. [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html) est une classe abstraite qui implémente `IInAppMessage` et fournit le socle de l’implémentation des messages in-app. Toutes les classes de messages in-app sont des sous-classes de `InAppMessageBase`.

En outre, il existe une sous-interface de `IInAppMessage` appelée [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html), qui ajoute des [boutons](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) d’action et d’analyse, ainsi qu'un texte d'en-tête et un bouton de fermeture.

{% alert important %}
Pour les messages in-app contenant des boutons, le message `clickAction` sera également inclus dans la charge utile finale si l'action de clic est ajoutée avant l'ajout du texte du bouton.
{% endalert %}

[`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html) est une classe abstraite qui implémente `IInAppMessageImmersive` et fournit l'implémentation de base des messages in-app de type `immersive`. Les messages in-app de type `Modal` constituent une sous-classe de `InAppMessageImmersiveBase`.

Les messages in-app HTML sont des instances [`InAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) qui implémentent [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html), une autre sous-classe de `IInAppMessage`.

### Comportements attendus par type de message

Voilà à quoi ressemble l’ouverture de nos types de messages in-app par défaut pour vos utilisateurs.

{% tabs local %}
{% tab Contextuel %}
Les messages in-app [`Slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) sont ainsi nommés parce qu'ils « surgissent » du haut ou du bas de l'écran. Ils recouvrent une petite partie de l’écran et offrent une fonctionnalité de messagerie efficace et non intrusive.

![Un message in-app surgissant du bas d’un écran de téléphone et affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché dans l’angle inférieur droit d'une page web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fenêtre modale %}
Les messages in-app de type [`Modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) apparaissent au centre de l'écran et sont encadrés par un panneau transparent. Ils sont utiles pour les messages plus critiques et peuvent être équipés d'un bouton d’action et d'un bouton activé par analyse.

![Un message in-app modal au centre d’un écran de téléphone affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché au centre d'une page Web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Plein écran %}
Les messages in-app [`Full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) sont utiles pour maximiser le contenu et l'impact de votre communication avec les utilisateurs. La moitié supérieure d’un `full` message in-app contient une image, et la moitié inférieure affiche le texte et deux boutons d’action permettant l’analyse.

![Un message in-app plein écran s’affiche sur l’ensemble de l’écran du téléphone et affiche : « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché en grand au centre d'une page web.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endtab %}
{% tab HTML personnalisé %}
Les messages in-app [`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html) sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le contenu du message in-app en HTML défini par l’utilisateur est affiché dans un `WebView` et peut éventuellement contenir d’autres contenus enrichis, tels que des images et des polices, permettant un contrôle total de l’apparence et de la fonctionnalité du message. <br><br>Les messages in-app Android prennent en charge une interface JavaScript `brazeBridge` pour appeler des méthodes SDK Braze pour le Web depuis votre HTML. Consultez nos <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/">meilleures pratiques</a> pour plus de détails.

![Un message in-app en HTML avec un carrousel de contenu et des boutons interactifs.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Actuellement, nous ne prenons pas en charge l’affichage de messages in-app HTML personnalisés dans un iFrame sur les plateformes iOS et Android.
{% endalert %} 

{% endtab %}
{% endtabs %}

#### Définir des types de messages in-app personnalisés

L'objet de message in-app `slideup` étend [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).
Les messages de type `full` et `modal` s'étendent [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html). L’extension de l’une de ces classes vous permet d’ajouter des fonctionnalités personnalisées à vos messages in-app générés localement.

## Intégration {#in-app-messaging-integration}

### Étape 1 : Enregistrer le gestionnaire de messages in-app Braze

L’affichage des messages in-app est géré par la classe [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html). Chaque activité de votre application doit être enregistrée avec le `BrazeInAppMessageManager` pour lui permettre d’ajouter des vues de messages in-app à la hiérarchie de vues. Il existe deux manières de le faire :

#### Intégration de la fonction de rappel du cycle de vie de l’activité (recommandé)

L'[intégration du rappel du cycle de vie de l'activité]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) gère automatiquement l'enregistrement des messages in-app ; aucune intégration supplémentaire n'est nécessaire. Il s’agit de l’intégration recommandée pour la gestion des messages in-app.

#### Enregistrement manuel des messages in-app

{% alert warning %}
Si vous avez fait l’intégration du cycle de vie de l’activité, vous ne devriez *pas* réaliser une intégration manuelle des messages in-app.
{% endalert %}

Tout d’abord, dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()), appelez [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html):

{% tabs %}
{% tab JAVA %}

```java
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
BrazeInAppMessageManager.getInstance().ensureSubscribedToInAppMessageEvents(context)
```

{% endtab %}
{% endtabs %}

Ensuite, dans chaque activité où des messages in-app peuvent être affichés, [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) doit être appelé dans le `onResume()` de cette activité :

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onResume() {
  super.onResume();
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onResume() {
  super.onResume()
  // Registers the BrazeInAppMessageManager for the current Activity. This Activity will now listen for
  // in-app messages from Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

Enfin, dans toutes les activités où [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) a été appelé, [`unregisterInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html) doit être appelé dans le `onPause()` de cette activité :

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onPause() {
  super.onPause();
  // Unregisters the BrazeInAppMessageManager for the current Activity.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onPause() {
  super.onPause()
  // Unregisters the BrazeInAppMessageManager.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

### Étape 2 : Liste de blocage du gestionnaire des messages in-app (facultatif)

Dans votre intégration, vous pouvez exiger que certaines activités de votre application n’affichent pas de messages in-app. L'[intégration du rappel du cycle de vie de l'activité]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) offre un moyen simple d'y parvenir.

L'exemple de code suivant ajoute deux activités à la liste de blocage de l'enregistrement des messages in-app, `SplashActivity` et `SettingsActivity`:

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Set<Class> inAppMessageBlocklist = new HashSet<>();
    inAppMessageBlocklist.add(SplashActivity.class);
    inAppMessageBlocklist.add(SettingsActivity.class);
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist));
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    val inAppMessageBlocklist = HashSet<Class<*>>()
    inAppMessageBlocklist.add(SplashActivity::class.java)
    inAppMessageBlocklist.add(SettingsActivity::class.java)
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(inAppMessageBlocklist))
  }
}
```

{% endtab %}
{% endtabs %}


