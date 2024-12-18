---
nav_title: Écouteurs personnalisés
article_title: Écouteurs de messages in-app personnalisés pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 3
description: "Cet article de référence décrit les écouteurs de messagerie in-app personnalisés pour votre application Android ou FireOS."
channel:
  - in-app messages

---

# Écouteurs personnalisés

> Cet article de référence décrit les écouteurs de messagerie in-app personnalisés pour votre application Android ou FireOS.

Avant de personnaliser les messages in-app avec des écouteurs personnalisés, il est important de comprendre le [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html), qui gère la majorité des manipulations de messages in-app. Comme décrit dans l’[étape 1]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#step-1-braze-in-app-message-manager-registration) du guide d’intégration des messages in-app, il doit être enregistré pour que les messages in-app fonctionnent correctement.

`BrazeInAppMessageManager` gère l’affichage des messages in-app sur Android. Il contient des instances de classe d’aide qui permettent de gérer le cycle de vie et l’affichage des messages in-app. Toutes ces classes ont des implémentations standard et définir des classes personnalisées est entièrement facultatif. Cependant, elles peuvent ajouter un autre niveau de contrôle sur l’affichage et le comportement des messages in-app. Ces classes personnalisables comprennent :

- [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) - [Gestion personnalisée de l'affichage et du comportement des messages in-app.](#custom-manager-listener)
- [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) - [Création de vues personnalisées de messages in-app](#custom-view-factory)
- [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html) - [Définir des animations personnalisées pour les messages in-app](#custom-animation-factory)
- [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html) - [Gestion personnalisée de l'affichage et du comportement des messages in-app au format HTML](#custom-html-in-app-message-action-listener)
- [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) - [Gestion personnalisée de l'interaction hiérarchique de l'affichage des messages in-app](#custom-view-wrapper-factory)

{% alert note %}
Cet article comprend des informations sur les fils d’actualité, qui deviennent obsolètes. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

## Gestionnaire d’écouteur personnalisé

Le `BrazeInAppMessageManager` gère automatiquement l’affichage et le cycle de vie des messages in-app. Si vous souhaitez contrôler davantage le cycle de vie d'un message, la mise en place d'un gestionnaire d'écoute personnalisé vous permettra de recevoir l'objet message in-app à différents moments du cycle de vie du message in-app, ce qui vous permettra de gérer vous-même son affichage, d'effectuer un traitement supplémentaire, de réagir au comportement de l'utilisateur, de traiter les [extras de]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/customization/key_value_pairs/) l'objet, et bien d'autres choses encore.

### Étape 1 : Implémenter un gestionnaire d’écouteur de message in-app

Créez une classe qui implémente [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html).

Les fonctions de rappel dans votre `IInAppMessageManagerListener` seront appelées à différents moments du cycle de vie des messages in-app.

Par exemple, si vous définissez un gestionnaire d’écouteur personnalisé lorsque vous recevez un message in-app depuis Braze, la méthode `beforeInAppMessageDisplayed()` sera appelée. Si votre implémentation de cette méthode renvoie [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html#27659854%2FClasslikes%2F-1725759721)cela indique à Braze que le message in-app sera traité par l'application hôte et ne doit pas être affiché par Braze. Si `InAppMessageOperation.DISPLAY_NOW` est retourné, Braze tentera d’afficher le message in-app. Cette méthode doit être utilisée si vous choisissez d’afficher le message in-app de manière personnalisée.

`IInAppMessageManagerListener` comprend également des méthodes de délégué pour les clics sur le message lui-même ou l’un des boutons. Un cas d’usage commun intercepterait un message lorsqu’un bouton ou un message est cliqué pour un traitement ultérieur.

### Étape 2 : Utiliser les méthodes de cycle de vie de l’affichage de message in-app (facultatif)

L'interface [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) comporte des méthodes d'affichage de messages in-app appelées à des moments distincts du cycle de vie de l'affichage de messages in-app. Ces méthodes sont appelées dans l’ordre suivant :

- [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html) : appelé juste avant que le message in-app soit ajouté à la vue de l’activité. Le message in-app n’est pas encore visible pour l’utilisateur à ce moment-là.
- [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) : appelé juste après l’ajout du message in-app à la vue de l’activité. Le message in-app est maintenant visible pour l’utilisateur.
- [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) : appelé juste avant que le message in-app ne soit supprimé de la vue de l’activité. Le message in-app est toujours visible pour l’utilisateur à ce moment-là.
- [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html) : appelé juste après la suppression du message in-app de la vue de l’activité. Le message in-app n’est plus visible pour l’utilisateur à ce moment-là.

Pour plus d’informations, le temps entre [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) et [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) est lorsque l’affichage de message in-app est à l’écran et visible pour l’utilisateur.

{% alert note %}
L’implémentation de ces méthodes n’est pas requise. Elles sont simplement fournies pour suivre et renseigner le cycle de vie de l’affichage des messages in-app. Il est fonctionnellement acceptable de laisser ces implémentations de méthodes vides.
{% endalert %}

### Étape 3 : Demander à Braze d’utiliser votre gestionnaire d’écouteur de message in-app

Une fois que votre `IInAppMessageManagerListener` est créé, appelez `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` pour demander à `BrazeInAppMessageManager`
d’utiliser votre `IInAppMessageManagerListener` personnalisé au lieu de l’écouteur par défaut.

Nous vous recommandons de définir votre `IInAppMessageManagerListener` dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze. L'écouteur personnalisé est ainsi activé avant l'affichage de tout message in-app.

#### Modifier les messages in-app avant l’affichage

Lorsqu’un nouveau message in-app est reçu et qu’il y a déjà un message in-app affiché, le nouveau message sera placé sur la partie supérieure de la pile et peut être affiché ultérieurement.

Cependant, s’il n’y a pas de message in-app affiché, la méthode de délégation suivante dans `IInAppMessageManagerListener` sera appelée :

{% tabs %}
{% tab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessageBase) {
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessageBase: IInAppMessage): InAppMessageOperation {
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

La valeur de retour `InAppMessageOperation()` peut contrôler quand le message doit être affiché. L’utilisation suggérée de cette méthode serait de retarder les messages dans certaines parties de l’application en retournant `DISPLAY_LATER` lorsque les messages in-app perturberaient l’expérience sur l’application de l’utilisateur.

| Valeur de retour `InAppMessageOperation` | Comportement |
| -------------------------- | -------- |
| `DISPLAY_NOW` | Le message s’affiche |
| `DISPLAY_LATER` | Le message sera renvoyé à la pile et affiché à l’occasion suivante |
| `DISCARD` | Le message sera supprimé |
| `null` | Le message sera ignoré. Cette méthode ne doit **PAS** renvoyer `null` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour plus de détails, voir [`InAppMessageOperation.java`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html).

{% alert tip %}
Si vous choisissez de `DISCARD` le message in-app et de le remplacer par votre vue de message in-app, vous devrez enregistrer manuellement les clics et les impressions de messages in-app.
{% endalert %}

Sur Android, cela est fait en appelant `logClick` et `logImpression` sur les messages in-app et `logButtonClick` sur des messages in-app immersifs.

{% alert tip %}
Une fois qu’un message in-app a été placé sur la pile, vous pouvez demander qu’il soit récupéré et affiché à tout moment en appelant [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html). Cette méthode demande à Braze d’afficher le prochain message in-app disponible dans la pile.
{% endalert %}

### Étape 4 : Personnaliser le comportement du thème sombre (facultatif) {#android-in-app-message-dark-theme-customization}

Dans la logique par défaut `IInAppMessageManagerListener`, dans `beforeInAppMessageDisplayed()`, les paramètres système sont vérifiés et permettent d’activer conditionnellement le style de thème sombre sur le message avec le code suivant :

{% tabs %}
{% tab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  if (inAppMessage instanceof IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(BrazeInAppMessageManager.getInstance().getApplicationContext())) {
    ((IInAppMessageThemeable) inAppMessage).enableDarkTheme();
  }
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  if (inAppMessage is IInAppMessageThemeable && ViewUtils.isDeviceInNightMode(BrazeInAppMessageManager.getInstance().applicationContext!!)) {
    (inAppMessage as IInAppMessageThemeable).enableDarkTheme()
  }
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

Si vous souhaitez utiliser votre propre logique conditionnelle, vous pouvez appeler [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) à n'importe quelle étape du processus de pré-affichage.

## Fabrique de vue personnalisée

Les types de messages in-app de Braze sont suffisamment polyvalents pour couvrir la plupart des cas d'utilisation personnalisés. Cependant, si vous souhaitez définir complètement l’apparence visuelle de vos messages in-app au lieu d’utiliser un type par défaut, Braze rend cela possible en définissant une fabrique de vue personnalisée.

### Étape 1 : Implémenter une fabrique de vue de message in-app

Créez une classe qui implémente [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html):

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageViewFactory implements IInAppMessageViewFactory {
  @Override
  public View createInAppMessageView(Activity activity, IInAppMessage inAppMessage) {
    // Uses a custom view for slideups, modals, and full in-app messages.
    // HTML in-app messages and any other types will use the Braze default in-app message view factories
    switch (inAppMessage.getMessageType()) {
      case SLIDEUP:
      case MODAL:
      case FULL:
        // Use a custom view of your choosing
        return createMyCustomInAppMessageView();
      default:
        // Use the default in-app message factories
        final IInAppMessageViewFactory defaultInAppMessageViewFactory = BrazeInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage);
        return defaultInAppMessageViewFactory.createInAppMessageView(activity, inAppMessage);
    }
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageViewFactory : IInAppMessageViewFactory {
  override fun createInAppMessageView(activity: Activity, inAppMessage: IInAppMessage): View {
    // Uses a custom view for slideups, modals, and full in-app messages.
    // HTML in-app messages and any other types will use the Braze default in-app message view factories
    when (inAppMessage.messageType) {
      MessageType.SLIDEUP, MessageType.MODAL, MessageType.FULL ->
        // Use a custom view of your choosing
        return createMyCustomInAppMessageView()
      else -> {
        // Use the default in-app message factories
        val defaultInAppMessageViewFactory = BrazeInAppMessageManager.getInstance().getDefaultInAppMessageViewFactory(inAppMessage)
        return defaultInAppMessageViewFactory!!.createInAppMessageView(activity, inAppMessage)
      }
    }
  }
}
```
{% endtab %}
{% endtabs %}

### Étape 2 : Demander à Braze d’utiliser votre fabrique d’animation de message in-app

Une fois que votre `IInAppMessageViewFactory` est créé, appelez `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` pour demander à `BrazeInAppMessageManager`
d’utiliser votre `IInAppMessageViewFactory` personnalisée au lieu de la fabrique de vue par défaut.

{% alert tip %}
Nous vous recommandons de configurer votre `IInAppMessageViewFactory` dans votre `Application.onCreate()` avant d’autres appels à Braze. Cette opération permet de définir la fabrique de vue personnalisée avant l'affichage de tout message in-app.
{% endalert %}

#### Implémenter une interface de vue Braze

L'affichage des messages in-app de `slideup` met en œuvre les éléments suivants [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html). Les vues des messages de type `full` et `modal` mettent en œuvre [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html). La mise en œuvre de l'une de ces classes permet à Braze d'ajouter des récepteurs de clics à votre vue personnalisée, le cas échéant. Toutes les classes de vues de Braze étendent la classe [`View`](http://developer.android.com/reference/android/view/View.html) d'Android.

Implémenter `IInAppMessageView` permet de définir une partie de votre vue personnalisée comme étant cliquable. L'implémentation de [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) vous permet de définir des vues de boutons de messages et de boutons de fermeture.

## Fabrique d’animation personnalisée

Les messages in-app ont un comportement d’animation prédéfini. Les messages `Slideup` glissent dans l’écran et les messages `full` et `modal` arrivent et disparaissent en fondu. Si vous souhaitez définir des comportements d’animation personnalisés pour vos messages in-app, Braze le rend possible en configurant une fabrique d’animation personnalisée.

### Étape 1 : Implémenter une fabrique d’animation de messages in-app

Créez une classe qui implémente [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html):

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageAnimationFactory implements IInAppMessageAnimationFactory {

  @Override
  public Animation getOpeningAnimation(IInAppMessage inAppMessage) {
    Animation animation = new AlphaAnimation(0, 1);
    animation.setInterpolator(new AccelerateInterpolator());
    animation.setDuration(2000L);
    return animation;
  }

  @Override
  public Animation getClosingAnimation(IInAppMessage inAppMessage) {
    Animation animation = new AlphaAnimation(1, 0);
    animation.setInterpolator(new DecelerateInterpolator());
    animation.setDuration(2000L);
    return animation;
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageAnimationFactory : IInAppMessageAnimationFactory {
  override fun getOpeningAnimation(inAppMessage: IInAppMessage): Animation {
    val animation: Animation = AlphaAnimation(0, 1)
    animation.interpolator = AccelerateInterpolator()
    animation.duration = 2000L
    return animation
  }

  override fun getClosingAnimation(inAppMessage: IInAppMessage): Animation {
    val animation: Animation = AlphaAnimation(1, 0)
    animation.interpolator = DecelerateInterpolator()
    animation.duration = 2000L
    return animation
  }
}
```
{% endtab %}
{% endtabs %}

### Étape 2 : Demander à Braze d’utiliser votre fabrique d’animation de message in-app

Une fois que votre `IInAppMessageAnimationFactory` est créé, appelez `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` pour demander à `BrazeInAppMessageManager`
d’utiliser votre `IInAppMessageAnimationFactory` personnalisée au lieu de la fabrique d’animation par défaut.

Nous vous recommandons de définir votre `IInAppMessageAnimationFactory` dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze. Cette opération permet de définir la fabrique d'animation personnalisée avant l'affichage de tout message in-app.

## Écouteur d’action personnalisé de message in-app HTML

Le SDK Braze a une classe `DefaultHtmlInAppMessageActionListener` par défaut utilisée si aucun écouteur personnalisé n’est défini et entreprend automatiquement l’action appropriée. Si vous avez besoin d’un contrôle plus important sur la manière dont un utilisateur interagit avec différents boutons à l’intérieur d’un message in-app HTML personnalisé, implémentez une classe `IHtmlInAppMessageActionListener` personnalisée.

### Étape 1 : Implémenter un écouteur d’action de message in-app HTML personnalisé

Créez une classe qui implémente [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html).

Les fonctions de rappel dans votre `IHtmlInAppMessageActionListener` seront appelées lorsque l’utilisateur initie l’une des actions suivantes dans le message in-app HTML :

- Clique sur le bouton Fermer
- Déclenche un événement personnalisé
- Clique sur une URL dans le message in-app HTML

{% tabs %}
{% tab JAVA %}
```java
public class CustomHtmlInAppMessageActionListener implements IHtmlInAppMessageActionListener {
  private final Context mContext;

  public CustomHtmlInAppMessageActionListener(Context context) {
    mContext = context;
  }

  @Override
  public void onCloseClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
  }

  @Override
  public boolean onCustomEventFired(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show();
    return true;
  }

  @Override
  public boolean onNewsfeedClicked(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Newsfeed button pressed. Ignoring.", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }

  @Override
  public boolean onOtherUrlAction(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom url pressed: " + url + " . Ignoring", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomHtmlInAppMessageActionListener(private val mContext: Context) : IHtmlInAppMessageActionListener {

    override fun onCloseClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle) {
        Toast.makeText(mContext, "HTML In App Message closed", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
    }

    override fun onCustomEventFired(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom event fired. Ignoring.", Toast.LENGTH_LONG).show()
        return true
    }

    override fun onNewsfeedClicked(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Newsfeed button pressed. Ignoring.", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }

    override fun onOtherUrlAction(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom url pressed: $url . Ignoring", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }
}
```
{% endtab %}
{% endtabs %}

### Étape 2 : Demander à Braze d’utiliser votre écouteur d’action de message in-app HTML

Une fois que votre `IHtmlInAppMessageActionListener` est créé, appelez `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` pour demander à `BrazeInAppMessageManager` d’utiliser votre `IHtmlInAppMessageActionListener` personnalisé au lieu de l’écouteur d’action par défaut.

Nous vous recommandons de définir votre `IHtmlInAppMessageActionListener` dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze. Cela permet d'activer l'écouteur d'action personnalisé avant l'affichage de tout message in-app :

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(new CustomHtmlInAppMessageActionListener(context));
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(CustomHtmlInAppMessageActionListener(context))
```
{% endtab %}
{% endtabs %}

## Fabrique de wrapper de vue personnalisé

Le `BrazeInAppMessageManager` gère automatiquement le positionnement du modèle de message in-app dans la hiérarchie de vue d’activité existante par défaut en utilisant [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html). Si vous devez personnaliser la manière dont les messages in-app sont placés dans la hiérarchie de vue, vous devez utiliser une [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) personnalisée.

### Étape 1 : Implémenter une fabrique de wrapper de messages in-app

Créez une classe qui implémente [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) et qui renvoie un [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html).

Cette fabrique est appelée immédiatement après la création de la vue de message in-app. La façon la plus simple d’implémenter un [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) personnalisé est d’étendre le [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) par défaut :

{% tabs %}
{% tab JAVA %}
```java
public class CustomInAppMessageViewWrapper extends DefaultInAppMessageViewWrapper {
  public CustomInAppMessageViewWrapper(View inAppMessageView,
                                       IInAppMessage inAppMessage,
                                       IInAppMessageViewLifecycleListener inAppMessageViewLifecycleListener,
                                       BrazeConfigurationProvider brazeConfigurationProvider,
                                       Animation openingAnimation,
                                       Animation closingAnimation, View clickableInAppMessageView) {
    super(inAppMessageView,
        inAppMessage,
        inAppMessageViewLifecycleListener,
        brazeConfigurationProvider,
        openingAnimation,
        closingAnimation,
        clickableInAppMessageView);
  }

  @Override
  public void open(@NonNull Activity activity) {
    super.open(activity);
    Toast.makeText(activity.getApplicationContext(), "Opened in-app message", Toast.LENGTH_SHORT).show();
  }

  @Override
  public void close() {
    super.close();
    Toast.makeText(mInAppMessageView.getContext().getApplicationContext(), "Closed in-app message", Toast.LENGTH_SHORT).show();
  }
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
class CustomInAppMessageViewWrapper(inAppMessageView: View,
                                    inAppMessage: IInAppMessage,
                                    inAppMessageViewLifecycleListener: IInAppMessageViewLifecycleListener,
                                    brazeConfigurationProvider: BrazeConfigurationProvider,
                                    openingAnimation: Animation,
                                    closingAnimation: Animation, clickableInAppMessageView: View) : 
    DefaultInAppMessageViewWrapper(inAppMessageView, 
        inAppMessage, 
        inAppMessageViewLifecycleListener, 
        brazeConfigurationProvider, 
        openingAnimation, 
        closingAnimation, 
        clickableInAppMessageView) {

  override fun open(activity: Activity) {
    super.open(activity)
    Toast.makeText(activity.applicationContext, "Opened in-app message", Toast.LENGTH_SHORT).show()
  }

  override fun close() {
    super.close()
    Toast.makeText(mInAppMessageView.context.applicationContext, "Closed in-app message", Toast.LENGTH_SHORT).show()
  }
}
```
{% endtab %}
{% endtabs %}

### Étape 2 : Demander à Braze d’utiliser votre fabrique de wrapper de vue personnalisé

Une fois que votre [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) est créé, appelez [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) pour demander à `BrazeInAppMessageManager` d’utiliser votre [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) personnalisée au lieu de la fabrique de wrapper par défaut.

Nous vous recommandons de définir votre [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze. Cette opération permet de définir la fabrique de wrapper de vue personnalisée avant l'affichage de tout message in-app :

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapper());
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapper())
```
{% endtab %}
{% endtabs %}

