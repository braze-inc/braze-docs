{% multi_lang_include developer_guide/prerequisites/android.md %} Vous devrez également [configurer les messages in-app]({{site.baseurl}}/developer_guide/in_app_messages).

## Gérer les paramètres des gestionnaires personnalisés

{% tabs %}
{% tab auditeur global %}
Bien que l'écouteur `BrazeInAppMessageManager` puisse gérer automatiquement l'affichage et le cycle de vie des messages in-app, vous devrez mettre en œuvre un écouteur de gestionnaire personnalisé si vous souhaitez personnaliser entièrement vos messages.
{% endtab %}

{% tab auditeur html %}
Le SDK Braze a une classe `DefaultHtmlInAppMessageActionListener` par défaut utilisée si aucun écouteur personnalisé n’est défini et entreprend automatiquement l’action appropriée. Si vous avez besoin d’un contrôle plus important sur la manière dont un utilisateur interagit avec différents boutons à l’intérieur d’un message in-app HTML personnalisé, implémentez une classe `IHtmlInAppMessageActionListener` personnalisée.
{% endtab %}
{% endtabs %}

### Étape 1 : Mise en œuvre de l'écouteur du gestionnaire personnalisé

{% tabs %}
{% tab auditeur global %}
#### Étape 1.1 : Mettre en œuvre `IInAppMessageManagerListener` 

Créez une classe qui implémente [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html).

Les rappels de votre site `IInAppMessageManagerListener` seront également appelés à différents moments du cycle de vie des messages in-app. Par exemple, si vous définissez un gestionnaire personnalisé listener lorsqu'un message in-app est reçu de Braze, la méthode [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) sera appelée. Si votre implémentation de cette méthode renvoie [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html)cela indique à Braze que le message in-app sera traité par l'application hôte et ne doit pas être affiché par Braze. Si le message [`InAppMessageOperation.DISPLAY_NOW`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-p-l-a-y_-n-o-w/index.html) est renvoyé, Braze tentera d'afficher le message in-app. Cette méthode doit être utilisée si vous choisissez d’afficher le message in-app de manière personnalisée.

`IInAppMessageManagerListener` comprend également des méthodes de délégation pour les clics sur les messages et les boutons, qui peuvent être utilisées dans des cas tels que l'interception d'un message lorsqu'un bouton ou un message est cliqué en vue d'un traitement ultérieur.

#### Étape 1.2 : Accrocher les méthodes de cycle de vie des vues IAM (facultatif)

L'interface [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) comporte des méthodes d'affichage de messages in-app appelées à des moments distincts du cycle de vie de l'affichage de messages in-app. Ces méthodes sont appelées dans l’ordre suivant :

1. [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html): Appelé juste avant que le message in-app ne soit ajouté à la vue de l'activité. Le message in-app n’est pas encore visible pour l’utilisateur à ce moment-là.
2. [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html): Appelé juste après l'ajout du message in-app à la vue de l'activité. Le message in-app est maintenant visible pour l’utilisateur.
3. [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html): Appelé juste avant que le message in-app ne soit supprimé de la vue de l'activité. Le message in-app est toujours visible pour l’utilisateur à ce moment-là.
4. [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html): Appelé juste après que le message in-app a été supprimé de la vue de l'activité. Le message in-app n’est plus visible pour l’utilisateur à ce moment-là.

Notez que le temps entre [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) et [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) est le moment où l'envoi de messages in-app est à l'écran, visible par l'utilisateur.

{% alert note %}
L’implémentation de ces méthodes n’est pas requise. Ils ne sont fournis que pour suivre et informer le cycle de vie de l'envoi des messages in-app. Vous pouvez laisser ces implémentations de méthodes vides.
{% endalert %}
{% endtab %}

{% tab auditeur html %}
Créez une classe qui implémente [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html).

Les fonctions de rappel dans votre `IHtmlInAppMessageActionListener` seront appelées lorsque l’utilisateur initie l’une des actions suivantes dans le message in-app HTML :

- Clique sur le bouton Fermer
- Déclenche un événement personnalisé
- Clique sur une URL dans le message in-app HTML

{% subtabs %}
{% subtab JAVA %}
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
  public boolean onOtherUrlAction(IInAppMessage inAppMessage, String url, Bundle queryBundle) {
    Toast.makeText(mContext, "Custom url pressed: " + url + " . Ignoring", Toast.LENGTH_LONG).show();
    BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false);
    return true;
  }
}
```
{% endsubtab %}
{% subtab KOTLIN %}
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

    override fun onOtherUrlAction(inAppMessage: IInAppMessage, url: String, queryBundle: Bundle): Boolean {
        Toast.makeText(mContext, "Custom url pressed: $url . Ignoring", Toast.LENGTH_LONG).show()
        BrazeInAppMessageManager.getInstance().hideCurrentlyDisplayingInAppMessage(false)
        return true
    }
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Étape 2 : Demandez à Braze d'utiliser l'écouteur personnalisé du gestionnaire.

{% tabs %}
{% tab auditeur global %}
Après avoir créé `IInAppMessageManagerListener`, appelez `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` pour demander `BrazeInAppMessageManager`
d’utiliser votre `IInAppMessageManagerListener` personnalisé au lieu de l’écouteur par défaut. Faites-le dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze, afin que l'écouteur personnalisé soit activé avant l'affichage de tout message in-app.

#### Modifier les messages in-app avant l’affichage

Lorsqu’un nouveau message in-app est reçu et qu’il y a déjà un message in-app affiché, le nouveau message sera placé sur la partie supérieure de la pile et peut être affiché ultérieurement.

Cependant, s’il n’y a pas de message in-app affiché, la méthode de délégation suivante dans `IInAppMessageManagerListener` sera appelée :

{% subtabs %}
{% subtab JAVA %}
```java
@Override
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endsubtab %}
{% endsubtabs %}

La valeur de retour `InAppMessageOperation()` peut contrôler quand le message doit être affiché. L’utilisation suggérée de cette méthode serait de retarder les messages dans certaines parties de l’application en retournant `DISPLAY_LATER` lorsque les messages in-app perturberaient l’expérience sur l’application de l’utilisateur.

| Valeur de retour `InAppMessageOperation` | Comportement |
| -------------------------- | -------- |
| `DISPLAY_NOW` | Le message s’affiche |
| `DISPLAY_LATER` | Le message sera renvoyé à la pile et affiché à l’occasion suivante |
| `DISCARD` | Le message sera supprimé |
| `null` | Le message sera ignoré. Cette méthode ne doit **PAS** renvoyer `null` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour plus de détails, voir [`InAppMessageOperation`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html).

{% alert tip %}
Si vous choisissez de `DISCARD` le message in-app et de le remplacer par votre vue de message in-app, vous devrez enregistrer manuellement les clics et les impressions de messages in-app.
{% endalert %}

Sur Android, cela est fait en appelant `logClick` et `logImpression` sur les messages in-app et `logButtonClick` sur des messages in-app immersifs.

{% alert tip %}
Une fois qu’un message in-app a été placé sur la pile, vous pouvez demander qu’il soit récupéré et affiché à tout moment en appelant [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html). Cette méthode demande à Braze d’afficher le prochain message in-app disponible dans la pile.
{% endalert %}
{% endtab %}

{% tab auditeur html %}
Une fois votre `IHtmlInAppMessageActionListener` créé, appelez `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` pour demander à `BrazeInAppMessageManager` d'utiliser votre `IHtmlInAppMessageActionListener` personnalisé au lieu de l'écouteur d'action par défaut.

Nous vous recommandons de définir votre `IHtmlInAppMessageActionListener` dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze. Cela permet d'activer l'écouteur d'action personnalisé avant l'affichage de tout message in-app :

{% subtabs %}
{% subtab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(new CustomHtmlInAppMessageActionListener(context));
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener(CustomHtmlInAppMessageActionListener(context))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Définition des usines personnalisées

Vous pouvez remplacer un certain nombre de valeurs par défaut au moyen d'objets personnalisés. Ces derniers peuvent être enregistrés avec le SDK Braze, selon les besoins, pour obtenir les résultats souhaités. Toutefois, si vous décidez de remplacer une fabrique, vous devrez probablement vous référer explicitement à la fabrique par défaut ou réimplémenter la fonctionnalité fournie par la fabrique par défaut de Braze. L’extrait de code suivant illustre comment fournir des implémentations personnalisées des interfaces `IInAppMessageViewFactory` et `IInAppMessageViewWrapperFactory`.

{% tabs local %}
{% tab Kotlin %}
**Types de messages in-app**<br>

```kotlin
class BrazeDemoApplication : Application(){
 override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener(true, true))
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapperFactory())
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(CustomInAppMessageViewFactory())
  }
}
```
{% endtab %}
{% tab Java %}
**Types de messages in-app**<br> 

```java
public class BrazeDemoApplication extends Application {
  @Override
  public void onCreate{
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener(true, true));
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapperFactory());
    BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory(new CustomInAppMessageViewFactory());
  }
}
```
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab vue %}
Les types de messages in-app de Braze sont suffisamment polyvalents pour couvrir la plupart des cas d'utilisation personnalisés. Cependant, si vous souhaitez définir complètement l’apparence visuelle de vos messages in-app au lieu d’utiliser un type par défaut, Braze rend cela possible en définissant une fabrique de vue personnalisée.
{% endtab %}

{% tab wrapper de visualisation %}
Le `BrazeInAppMessageManager` gère automatiquement le positionnement du modèle de message in-app dans la hiérarchie de vue d’activité existante par défaut en utilisant [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html). Si vous devez personnaliser la manière dont les messages in-app sont placés dans la hiérarchie de vue, vous devez utiliser une [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) personnalisée.
{% endtab %}

{% tab animation %}
Les messages in-app ont un comportement d’animation prédéfini. Les messages `Slideup` glissent dans l’écran et les messages `full` et `modal` arrivent et disparaissent en fondu. Si vous souhaitez définir des comportements d’animation personnalisés pour vos messages in-app, Braze le rend possible en configurant une fabrique d’animation personnalisée.
{% endtab %}
{% endtabs %}

### Étape 1 : Implémenter l'usine

{% tabs %}
{% tab vue %}
Créez une classe qui implémente [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html):

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab wrapper de visualisation %}
Créez une classe qui implémente [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) et qui renvoie un [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html).

Cette fabrique est appelée immédiatement après la création de la vue de message in-app. La façon la plus simple d’implémenter un [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) personnalisé est d’étendre le [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) par défaut :

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab animation %}
Créez une classe qui implémente [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html):

{% subtabs %}
{% subtab JAVA %}
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
{% endsubtab %}
{% subtab KOTLIN %}
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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Étape 2 : Demander à Braze d'utiliser l'usine

{% tabs %}
{% tab vue %}
Une fois que votre `IInAppMessageViewFactory` a été créé, appelez `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` pour donner des instructions. `BrazeInAppMessageManager`
d’utiliser votre `IInAppMessageViewFactory` personnalisée au lieu de la fabrique de vue par défaut.

{% alert tip %}
Nous vous recommandons de configurer votre `IInAppMessageViewFactory` dans votre `Application.onCreate()` avant d’autres appels à Braze. Cette opération permet de définir la fabrique de vue personnalisée avant l'affichage de tout message in-app.
{% endalert %}

#### Fonctionnement

L'affichage des messages in-app de `slideup` met en œuvre les éléments suivants [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html). Les vues des messages de type `full` et `modal` mettent en œuvre [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html). La mise en œuvre de l'une de ces classes permet à Braze d'ajouter des récepteurs de clics à votre vue personnalisée, le cas échéant. Toutes les classes de vues de Braze étendent la classe [`View`](http://developer.android.com/reference/android/view/View.html) d'Android.

Implémenter `IInAppMessageView` permet de définir une partie de votre vue personnalisée comme étant cliquable. L'implémentation de [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) vous permet de définir des vues de boutons de messages et de boutons de fermeture.
{% endtab %}

{% tab wrapper de visualisation %}
Après la création de votre [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) est créé, appelez [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) afin d'indiquer à `BrazeInAppMessageManager` d'utiliser votre [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) au lieu de l'usine de wrapper de vue par défaut.

Nous vous recommandons de définir votre [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze. Cette opération permet de définir la fabrique de wrapper de vue personnalisée avant l'affichage de tout message in-app :

{% subtabs %}
{% subtab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(new CustomInAppMessageViewWrapper());
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory(CustomInAppMessageViewWrapper())
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab animation %}
Une fois que votre `IInAppMessageAnimationFactory` est créé, appelez `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` pour demander à `BrazeInAppMessageManager`
d’utiliser votre `IInAppMessageAnimationFactory` personnalisée au lieu de la fabrique d’animation par défaut.

Nous vous recommandons de définir votre `IInAppMessageAnimationFactory` dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze. Cette opération permet de définir la fabrique d'animation personnalisée avant l'affichage de tout message in-app.
{% endtab %}
{% endtabs %}

## Styles personnalisés

Les éléments de l’IU de Braze sont dotés d’un aspect et d’une convivialité par défaut qui correspondent aux directives de l’IU standard d’Android et offrent une expérience transparente. Cet article de référence décrit les styles de messagerie in-app personnalisés pour votre application Android ou FireOS.

### Définir un style par défaut

Vous pouvez voir ces styles par défaut dans le fichier [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) du SDK Braze :

```xml
  <style name="Braze"/>
  <style name="Braze.InAppMessage"/>
  <style name="Braze.InAppMessage.Header">
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:padding">0.0dp</item>
    <item name="android:background">@android:color/transparent</item>
    <item name="android:textColor">@color/com_braze_inappmessage_header_text</item>
    <item name="android:textSize">20.0sp</item>
    <item name="android:lineSpacingMultiplier">1.3</item>
    <item name="android:gravity">center</item>
    <item name="android:textStyle">bold</item>
    <item name="android:layout_centerHorizontal">true</item>
  </style>
```

Si vous préférez, vous pouvez écraser ces styles pour créer un aspect et une convivialité qui conviennent mieux à votre application.

Pour remplacer un style, copiez-le dans son intégralité dans le fichier `styles.xml` dans votre projet et apportez des modifications. Le style entier doit être copié sur votre fichier `styles.xml` local pour que tous les attributs soient correctement définis. Notez que ces styles personnalisés sont destinés aux modifications apportées à des éléments individuels de l’IU et non à des modifications globales sur les mises en page. Les modifications au niveau de la disposition doivent être gérées avec des vues personnalisées.

{% alert note %}
Vous pouvez personnaliser certaines couleurs directement dans votre campagne Braze sans modifier le XML. N'oubliez pas que les couleurs définies dans le tableau de bord de Braze remplacent celles que vous avez définies ailleurs.
{% endalert %}

### Personnalisation de la police de caractères

Vous pouvez définir une police personnalisée en l'emplacement/localisation de la police dans le répertoire `res/font`. Pour l’utiliser, remplacez le style du texte du message, des en-têtes et du texte du bouton et utilisez l’attribut `fontFamily` pour indiquer à Braze d’utiliser votre famille de polices personnalisée.

Par exemple, pour mettre à jour la police sur le texte du bouton du message in-app, remplacez le style `Braze.InAppMessage.Button` et faites référence à votre famille de polices personnalisée. La valeur d’attribut doit pointer vers une famille de polices dans votre répertoire `res/font`.

Voici un exemple tronqué avec une famille de polices personnalisées `my_custom_font_family`, référencé sur la dernière ligne :

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Mis à part le style `Braze.InAppMessage.Button` pour le texte du bouton, le style du texte du message est `Braze.InAppMessage.Message` et le style pour les en-têtes de messages est `Braze.InAppMessage.Header`. Si vous souhaitez utiliser votre famille de polices personnalisée pour l’ensemble du texte du message in-app, vous pouvez configurer votre famille de polices sur le style `Braze.InAppMessage`, qui est le style parent pour tous les messages in-app.

{% alert important %}
Comme pour les autres styles personnalisés, le style entier doit être copié sur votre fichier `styles.xml` local pour que tous les attributs soient correctement définis.
{% endalert %}

## Envois de messages

### Désactivation des renvois par le bouton de retour

Par défaut, le bouton de retour arrière du matériel rejette les messages in-app de Braze. Ce comportement peut être désactivé au niveau de chaque message via l'option [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html). 

Dans l’exemple suivant, `disable_back_button` est une paire clé-valeur personnalisée définie pour le message in-app qui indique si le message doit autoriser le bouton de retour arrière à rejeter le message :

{% tabs %}
{% tab JAVA %}
```java
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(new DefaultInAppMessageManagerListener() {
  @Override
  public void beforeInAppMessageViewOpened(View inAppMessageView, IInAppMessage inAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage);
    final Map<String, String> extras = inAppMessage.getExtras();
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false);
    }
  }

  @Override
  public void afterInAppMessageViewClosed(IInAppMessage inAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage);
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true);
  }
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener(object : DefaultInAppMessageManagerListener() {
  override fun beforeInAppMessageViewOpened(inAppMessageView: View, inAppMessage: IInAppMessage) {
    super.beforeInAppMessageViewOpened(inAppMessageView, inAppMessage)
    val extras = inAppMessage.extras
    if (extras != null && extras.containsKey("disable_back_button")) {
      BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(false)
    }
  }

  override fun afterInAppMessageViewClosed(inAppMessage: IInAppMessage) {
    super.afterInAppMessageViewClosed(inAppMessage)
    BrazeInAppMessageManager.getInstance().setBackButtonDismissesInAppMessageView(true)
  }
})
```
{% endtab %}
{% endtabs %}

{% alert note %}
Notez que si cette fonctionnalité est désactivée, le comportement par défaut du bouton de retour arrière du matériel de l’activité hôte sera utilisé. Cela peut entraîner la fermeture de l’application par le bouton de retour arrière plutôt celle du message in-app.
{% endalert %}

### Permettre les licenciements en dehors des robinets

Par défaut, la fermeture de la fenêtre modale à l'aide d'une touche extérieure est réglée sur `false`. Définir cette valeur sur `true` entraînera le rejet du message in-app modal lorsque l’utilisateur touche en dehors du message in-app. Ce comportement peut être activé en appelant :

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

## Personnaliser l'orientation

Pour définir une orientation fixe pour un message in-app, [définissez d'abord un écouteur personnalisé de gestionnaire de messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners). Ensuite, mettez à jour l'orientation de l'objet `IInAppMessage` dans la méthode de délégation `beforeInAppMessageDisplayed()`:

{% tabs %}
{% tab JAVA %}
```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
  inAppMessage.setOrientation(Orientation.PORTRAIT);
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  // Set the orientation to portrait
  inAppMessage.orientation = Orientation.PORTRAIT
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

Pour les tablettes, les messages in-app apparaissent dans le style d’orientation préféré de l’utilisateur, quelle que soit l’orientation réelle de l’écran.

## Désactivation du thème sombre {#android-in-app-message-dark-theme-customization}

Par défaut, `IInAppMessageManagerListener`'s `beforeInAppMessageDisplayed()` vérifie les paramètres du système et active de manière conditionnelle le style "dark theme" sur le message avec le code suivant :

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

Pour changer cela, vous pouvez appeler [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) à n'importe quelle étape du processus de pré-affichage pour mettre en œuvre votre propre logique conditionnelle.

## Personnalisation de l'invite d'évaluation de Google Play

En raison des limitations et des restrictions définies par Google, les demandes de critique de Google Play personnalisées ne sont actuellement pas prises en charge par Braze. Si certains utilisateurs ont réussi à intégrer ces invites avec succès, d'autres ont affiché de faibles taux de réussite en raison des [quotas de Google Play.](https://developer.android.com/guide/playcore/in-app-review#quotas) Intégrez à vos risques et périls. Reportez-vous à la documentation sur les [invites de révision in-app de Google Play.](https://developer.android.com/guide/playcore/in-app-review)
