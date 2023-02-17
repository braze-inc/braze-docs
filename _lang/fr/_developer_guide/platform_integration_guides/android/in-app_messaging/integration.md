---
nav_title: Intégration
article_title: Intégration de message in-app pour Android et FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "Cet article de référence explique comment intégrer les messages in-app dans votre application Android ou FireOS."
channel:
  - messages in-app
search_rank: 2
---

# Intégration de message in-app

Les [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) vous aident à proposer du contenu à vos utilisateurs sans interrompre leur journée avec une notification push. Des messages in-app personnalisés et adaptés améliorent l’expérience utilisateur et aident votre public à tirer le meilleur parti de votre application. Avec plusieurs mises en page et outils de personnalisation, les messages in-app impliquent plus que jamais vos utilisateurs.

Pour voir des exemples de messages in-app, consultez nos [études de cas][83].

## Types de messages in-app

Braze propose plusieurs types de messages in-app par défaut, tous personnalisables par des messages, des images, des icônes [Font Awesome][15], des boutons d’action, de l’analytique, des styles modifiables et des thèmes de couleurs. Les types actuellement disponibles sont :

- [`Slideup`][91]
- [`Modal`][90]
- [`Full`][93]
- [`HTML Full`][92]

Il est également possible de définir votre propre [affichage personnalisé de message in-app][12].

Tous les messages in-app implémentent l’interface [`IInAppMessage`][3], qui définit tous leurs comportements et traits de base. [`InAppMessageBase`][27]  est une classe abstraite qui implémente `IInAppMessage` et fournit le socle de l’implémentation des messages in-app. Toutes les classes de messages in-app sont des sous-classes de `InAppMessageBase`.

En outre, il existe une sous-interface de `IInAppMessage` appelée [`IInAppMessageImmersive`][8], qui ajoute des [buttons][50] d’action permettant des actions analytiques, ainsi qu’un texte d’en-tête et un bouton de fermeture.[`InAppMessageImmersiveBase`][28] est une classe abstraite qui implémente `IInAppMessageImmersive` et fournit la base d’implémentation des messages in-app`immersive`. Les messages in-app  `Modal` et `Full` sont des sous-classes de `InAppMessageImmersiveBase` .

Les messages in-app entièrement en HTML sont des instances [`InAppMessageHtmlFull`][51], qui implémentent [`IInAppMessageHtml`][52], une autre sous-classe de `IInAppMessage`.

### Comportements attendus par type de message

Voilà à quoi ressemble l’ouverture de nos types de messages in-app par défaut pour vos utilisateurs.

{% tabs local %}
{% tab Slideup %}
Les messages in-app [`Slideup`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) sont ainsi nommés car ils « glissent vers le haut » ou « glissent vers le bas » depuis le haut ou le bas de l’écran. Ils recouvrent une petite partie de l’écran et offrent une fonctionnalité de messagerie efficace et non intrusive.

![Un message in-app surgissant du bas d’un écran de téléphone et affichant « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché dans l’angle inférieur droit d’une page Web.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}
Les messages in-app [`Modal`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) apparaissent au centre de l’écran et sont encadrés par un panneau translucide. Ils sont utiles pour les messages plus critiques et peuvent être équipés de deux boutons d’action permettant l’analytique.

![Un message in-app modal au centre d’un écran de téléphone affichant : « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le même message in-app est affiché au centre d’une page Web.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Full Screen %}
Les messages in-app [`Full`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html) sont utiles pour maximiser le contenu et l’impact de votre communication utilisateur. La moitié supérieure d’un `full` message in-app contient une image, et la moitié inférieure affiche le texte et deux boutons d’action permettant l’analyse.

![Un message in-app plein écran s’affiche sur l’ensemble de l’écran du téléphone et affiche : « Les humains sont compliqués. L’engagement des clients ne devrait pas l’être. » En arrière-plan, le message in-app est affiché en grand au centre d’une page Web.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endtab %}
{% tab Custom HTML %}
Les messages in-app [`HTML Full`](https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html) sont utiles pour créer un contenu utilisateur entièrement personnalisé. Le contenu des messages in-app entièrement en HTML défini par l’utilisateur est affiché dans un `WebView` et peut éventuellement contenir d’autres contenus enrichis, tels que des images et des polices, permettant un contrôle total de l’apparence et de la fonctionnalité du message. <br><br>Les messages in-app Android prennent en charge une interface JavaScript `brazeBridge` pour appeler des méthodes SDK Braze pour le Web depuis votre HTML. Consultez nos <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/">meilleures pratiques</a> pour plus de détails.

![Un message in-app HTML avec un carrousel de contenus et des boutons interactifs.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Actuellement, nous ne prenons pas en charge l’affichage de messages in-app HTML personnalisés dans un iFrame sur les plateformes iOS et Android.
{% endalert %} 

{% endtab %}
{% endtabs %}

#### Définir des types de messages in-app personnalisés

L’objet de message in-app `slideup` étend [`InAppMessageBase`][27]. 
Les types de messages `full` et `modal` étendent [`InAppMessageImmersiveBase`][28]. L’extension de l’une de ces classes vous permet d’ajouter des fonctionnalités personnalisées à vos messages in-app générés localement.

## Intégration {#in-app-messaging-integration}

### Étape 1 : Enregistrer le gestionnaire de messages in-app Braze

L’affichage des messages in-app est géré par la classe [`BrazeInAppMessageManager`][34] . Chaque activité de votre application doit être enregistrée avec le `BrazeInAppMessageManager` pour lui permettre d’ajouter des vues de messages in-app à la hiérarchie de vues. Il existe deux manières de le faire :

#### Intégration de la fonction de rappel du cycle de vie de l’activité (recommandé)

L’[intégration de la fonction de rappel du cycle de vie de l’activité ][59] s’occupe automatiquement de l’enregistrement des messages in-app. Aucune intégration supplémentaire n’est requise. Il s’agit de l’intégration recommandée pour la gestion des messages in-app.

#### Enregistrement manuel des messages in-app

{% alert warning %}
Si vous avez fait l’intégration du cycle de vie de l’activité, vous *ne devriez pas* réaliser une intégration manuelle des messages in-app.
{% endalert %}

Tout d’abord, dans votre [`Application.onCreate()`][82], appelez [`ensureSubscribedToInAppMessageEvents()`][69]:

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

Ensuite, dans chaque activité où les messages in-app peuvent être montrés, [`registerInAppMessageManager()`][80] doit être appelé dans le  de cette activité `onResume()`:

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onResume() {
  super.onResume();
  // Enregistre le BrazeInAppMessageManager pour l’activité en cours. Cette activité va écouter
  // les messages in-app de Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onResume() {
  super.onResume()
  // Enregistre le BrazeInAppMessageManager pour l’activité en cours. Cette activité va écouter
  // les messages in-app de Braze.
  BrazeInAppMessageManager.getInstance().registerInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

Enfin, dans chaque activité où [`registerInAppMessageManager()`][80]  a été appelé, [`unregisterInAppMessageManager()`][81]  doit être appelé dans le `onPause()`de cette activité :

{% tabs %}
{% tab JAVA %}

```java
@Override
public void onPause() {
  super.onPause();
  // Supprime le BrazeInAppMessageManager pour l’activité en cours.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(activity);
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
public override fun onPause() {
  super.onPause()
  // Supprime le BrazeInAppMessageManager.
  BrazeInAppMessageManager.getInstance().unregisterInAppMessageManager(this)
}
```

{% endtab %}
{% endtabs %}

### Étape 2 : Liste noire du gestionnaire de messages in-app (facultatif)

Dans votre intégration, vous pouvez exiger que certaines activités de votre application n’affichent pas de messages in-app. L’[intégration de fonction de rappel du cycle de vie de l’activité][59] permet de le faire facilement.

L’exemple de code suivant ajoute deux activités à la liste noire d’enregistrement de messages in-app, `SplashActivity` et `SettingsActivity` :

{% tabs %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    Set<Class> inAppMessageBlacklist = new HashSet<>();
    inAppMessageBlacklist.add(SplashActivity.class);
    inAppMessageBlacklist.add(SettingsActivity.class);
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(inAppMessageBlacklist));
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    val inAppMessageBlacklist = HashSet<Class<*>>()
    inAppMessageBlacklist.add(SplashActivity::class.java)
    inAppMessageBlacklist.add(SettingsActivity::class.java)
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(inAppMessageBlacklist))
  }
}
```

{% endtab %}
{% endtabs %}


[34]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html
[69]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html
[80]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html
[81]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html
[82]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[83]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html
[59]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android
[3]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html
[8]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-view-factory
[15]: https://fontawesome.com/icons?d=gallery&p=2
[27]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html
[28]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html
[50]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html
[51]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[52]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[90]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html
[91]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html
[92]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[93]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html
