{% multi_lang_include developer_guide/prerequisites/android.md %} Il vous sera également nécessaire de [configurer les messages in-app]({{site.baseurl}}/developer_guide/in_app_messages).

## Configuration des écouteurs personnalisés du gestionnaire

{% tabs %}
{% tab global listener %}
Bien que l'écouteur `BrazeInAppMessageManager` puisse gérer automatiquement l'affichage et le cycle de vie des messages in-app, vous devrez implémenter un écouteur de gestionnaire personnalisé si vous souhaitez personnaliser entièrement vos messages.
{% endtab %}

{% tab html listener %}
Le SDK Braze dispose d'une classe `DefaultHtmlInAppMessageActionListener` par défaut, utilisée lorsqu'aucun écouteur personnalisé n'est défini. Elle prend automatiquement les mesures appropriées. Si vous avez besoin de davantage de contrôle sur la manière dont un utilisateur interagit avec les différents boutons d'un message in-app HTML personnalisé, implémentez une classe `IHtmlInAppMessageActionListener` personnalisée.

Cet écouteur s'applique __aux deux types__ de messages : ceux créés avec du HTML personnalisé et ceux créés à l'aide de l'éditeur par glisser-déposer (DnD). Il ne s'applique pas aux IAM traditionnels. Les IAM traditionnels sont les types de messages intégrés de Braze, rendus par le SDK (par exemple, contextuel, fenêtre modale et plein écran), créés dans le compositeur de messages in-app d'origine à l'aide de dispositions prédéfinies. Contrairement aux IAM HTML personnalisés et DnD, ils ne passent pas par le flux de l'écouteur d'actions HTML.

Si vous définissez un `IHtmlInAppMessageActionListener` personnalisé, sa logique remplacera le comportement de clic par défaut pour _tous_ les messages DnD. Assurez-vous que votre équipe marketing en est informée, car cela peut affecter leurs campagnes de manière inattendue.
{% endtab %}
{% endtabs %}

### Étape 1 : Implémenter l'écouteur de gestionnaire personnalisé

{% tabs %}
{% tab global listener %}
#### Étape 1.1 : Implémenter `IInAppMessageManagerListener` 

Créez une classe qui implémente [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html).

Les rappels de votre `IInAppMessageManagerListener` seront également appelés à différents moments du cycle de vie des messages in-app. Par exemple, si vous définissez un écouteur de gestionnaire personnalisé lorsqu'un message in-app est reçu de Braze, la méthode [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) sera appelée. Si votre implémentation de cette méthode renvoie [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html), cela indique à Braze que le message in-app sera traité par l'application hôte et ne doit pas être affiché par Braze. Si la valeur [`InAppMessageOperation.DISPLAY_NOW`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-p-l-a-y_-n-o-w/index.html) est renvoyée, Braze tentera d'afficher le message in-app. Utilisez cette méthode si vous choisissez d'afficher le message in-app de manière personnalisée.

`IInAppMessageManagerListener` comprend également des méthodes déléguées pour les clics sur les messages et les boutons, utiles par exemple pour intercepter un message lorsqu'un bouton ou un message est cliqué afin d'effectuer un traitement supplémentaire.

#### Étape 1.2 : S'intégrer aux méthodes du cycle de vie de la vue IAM (facultatif)

L'interface [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) comporte des méthodes liées à la vue des messages in-app, appelées à des moments distincts du cycle de vie de cette vue. Ces méthodes sont appelées dans l'ordre suivant :

1. [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html) : Appelée juste avant l'ajout du message in-app à la vue de l'activité. Le message in-app n'est pas encore visible pour l'utilisateur à ce moment-là.
2. [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) : Appelée juste après l'ajout du message in-app à la vue de l'activité. Le message in-app est désormais visible pour l'utilisateur.
3. [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) : Appelée juste avant la suppression du message in-app de la vue de l'activité. Le message in-app est toujours visible pour l'utilisateur à ce moment-là.
4. [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html) : Appelée juste après la suppression du message in-app de la vue de l'activité. Le message in-app n'est plus visible pour l'utilisateur.

Notez que la période entre [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) et [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) correspond au moment où le message in-app est affiché à l'écran et visible par l'utilisateur.

{% alert note %}
L'implémentation de ces méthodes n'est pas requise. Elles sont uniquement fournies pour suivre et informer sur le cycle de vie de la vue des messages in-app. Vous pouvez laisser ces implémentations vides.
{% endalert %}
{% endtab %}

{% tab html listener %}
Créez une classe qui implémente [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html).

Les rappels de votre `IHtmlInAppMessageActionListener` seront appelés lorsque l'utilisateur effectue l'une des actions suivantes dans le message in-app HTML :

- Clic sur le bouton de fermeture
- Déclenchement d'un événement personnalisé
- Clic sur une URL dans le message in-app HTML

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

### Étape 2 : Indiquer à Braze d'utiliser l'écouteur de gestionnaire personnalisé

{% tabs %}
{% tab global listener %}
Après avoir créé votre `IInAppMessageManagerListener`, appelez `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` pour indiquer à `BrazeInAppMessageManager`
d'utiliser votre `IInAppMessageManagerListener` personnalisé au lieu de l'écouteur par défaut. Effectuez cette opération dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze, afin que l'écouteur personnalisé soit défini avant l'affichage de tout message in-app.

#### Modifier les messages in-app avant l'affichage

Lorsqu'un nouveau message in-app est reçu alors qu'un autre est déjà affiché, le nouveau message est placé en haut de la pile et pourra être affiché ultérieurement.

En revanche, si aucun message in-app n'est actuellement affiché, la méthode déléguée suivante de `IInAppMessageManagerListener` sera appelée :

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

La valeur de retour de `InAppMessageOperation()` permet de contrôler le moment où le message doit être affiché. L'utilisation recommandée de cette méthode consiste à retarder les messages dans certaines parties de l'application en renvoyant `DISPLAY_LATER` lorsque les messages in-app perturberaient l'expérience sur l'application de l'utilisateur.

| Valeur de retour `InAppMessageOperation` | Comportement |
| -------------------------- | -------- |
| `DISPLAY_NOW` | Le message s'affiche |
| `DISPLAY_LATER` | Le message est renvoyé dans la pile et affiché à la prochaine occasion |
| `DISCARD` | Le message est supprimé |
| `null` | Le message est ignoré. Cette méthode ne doit **PAS** renvoyer `null` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Pour plus de détails, consultez [`InAppMessageOperation`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html).

{% alert tip %}
Si vous choisissez de `DISCARD` le message in-app et de le remplacer par votre propre vue de message in-app, vous devrez enregistrer manuellement les clics et les impressions.
{% endalert %}

Sur Android, cela se fait en appelant `logClick` et `logImpression` sur les messages in-app, et `logButtonClick` sur les messages in-app immersifs.

{% alert tip %}
Une fois qu'un message in-app a été placé dans la pile, vous pouvez demander sa récupération et son affichage à tout moment en appelant [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html). Cette méthode demande à Braze d'afficher le prochain message in-app disponible dans la pile.
{% endalert %}
{% endtab %}

{% tab html listener %}
Une fois votre `IHtmlInAppMessageActionListener` créé, appelez `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` pour indiquer à `BrazeInAppMessageManager` d'utiliser votre `IHtmlInAppMessageActionListener` personnalisé à la place de l'écouteur d'action par défaut.

Nous vous recommandons de définir votre `IHtmlInAppMessageActionListener` dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze. Cela permet de configurer l'écouteur d'action personnalisé avant l'affichage de tout message in-app :

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

## Configuration de fabriques personnalisées

Il est possible de remplacer un certain nombre de comportements par défaut à l'aide d'objets de fabriques personnalisés. Ces derniers peuvent être enregistrés auprès du SDK Braze selon vos besoins pour obtenir les résultats souhaités. Toutefois, si vous décidez de remplacer une fabrique, vous devrez probablement déléguer explicitement au comportement par défaut ou réimplémenter la fonctionnalité fournie par défaut par Braze. L'extrait de code suivant illustre comment fournir des implémentations personnalisées des interfaces `IInAppMessageViewFactory` et `IInAppMessageViewWrapperFactory`.

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
{% tab view %}
Les types de messages in-app de Braze sont suffisamment polyvalents pour couvrir la plupart des cas d'utilisation personnalisés. Cependant, si vous souhaitez définir entièrement l'apparence visuelle de vos messages in-app au lieu d'utiliser un type par défaut, Braze vous permet de le faire en définissant une fabrique de vues personnalisée.
{% endtab %}

{% tab view wrapper %}
Par défaut, `BrazeInAppMessageManager` gère automatiquement le positionnement du modèle de message in-app dans la hiérarchie de vues de l'activité existante en utilisant [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html). Si vous devez personnaliser la manière dont les messages in-app sont placés dans la hiérarchie de vues, utilisez une [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) personnalisée.
{% endtab %}

{% tab animation %}
Les messages in-app ont un comportement d'animation prédéfini. Les messages `Slideup` glissent dans l'écran, tandis que les messages `full` et `modal` apparaissent et disparaissent en fondu. Si vous souhaitez définir des comportements d'animation personnalisés pour vos messages in-app, Braze vous permet de le faire en configurant une fabrique d'animation personnalisée.
{% endtab %}
{% endtabs %}

### Étape 1 : Implémenter la fabrique

{% tabs %}
{% tab view %}
Créez une classe qui implémente [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) :

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

{% tab view wrapper %}
Créez une classe qui implémente [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) et qui renvoie un [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html).

Cette fabrique est appelée immédiatement après la création de la vue du message in-app. La façon la plus simple d'implémenter un [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) personnalisé est d'étendre le [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) par défaut :

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
Créez une classe qui implémente [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html) :

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

### Étape 2 : Indiquer à Braze d'utiliser la fabrique

{% tabs %}
{% tab view %}
Une fois votre `IInAppMessageViewFactory` créée, appelez `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` pour indiquer à `BrazeInAppMessageManager`
d'utiliser votre `IInAppMessageViewFactory` personnalisée au lieu de la fabrique de vues par défaut.

{% alert tip %}
Nous vous recommandons de configurer votre `IInAppMessageViewFactory` dans votre `Application.onCreate()` avant tout autre appel à Braze. Cela permet de définir la fabrique de vues personnalisée avant l'affichage de tout message in-app.
{% endalert %}

#### Fonctionnement

La vue des messages in-app de type `slideup` implémente [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html). Les vues des messages de type `full` et `modal` implémentent [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html). L'implémentation de l'une de ces classes permet à Braze d'ajouter des écouteurs de clics à votre vue personnalisée, le cas échéant. Toutes les classes de vues de Braze étendent la classe [`View`](http://developer.android.com/reference/android/view/View.html) d'Android.

Implémenter `IInAppMessageView` vous permet de définir une partie de votre vue personnalisée comme cliquable. Implémenter [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) vous permet de définir des vues de boutons de message et un bouton de fermeture.
{% endtab %}

{% tab view wrapper %}
Une fois votre [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) créé, appelez [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) pour indiquer à `BrazeInAppMessageManager` d'utiliser votre [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) personnalisée à la place de la fabrique de wrapper de vues par défaut.

Nous vous recommandons de définir votre [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze. Cela permet de définir la fabrique de wrapper de vues personnalisée avant l'affichage de tout message in-app :

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
Une fois votre `IInAppMessageAnimationFactory` créée, appelez `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` pour indiquer à `BrazeInAppMessageManager`
d'utiliser votre `IInAppMessageAnimationFactory` personnalisée au lieu de la fabrique d'animation par défaut.

Nous vous recommandons de définir votre `IInAppMessageAnimationFactory` dans votre [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) avant tout autre appel à Braze. Cela permet de définir la fabrique d'animation personnalisée avant l'affichage de tout message in-app.
{% endtab %}
{% endtabs %}

## Styles personnalisés

Les éléments d'interface de Braze sont dotés d'un aspect par défaut conforme aux directives de l'interface standard d'Android, offrant ainsi une expérience fluide. Cet article de référence décrit les styles personnalisés pour les messages in-app de votre application Android ou FireOS.

### Définition d'un style par défaut

Vous pouvez consulter les styles par défaut dans le fichier [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml) du SDK Braze :

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

Si vous le souhaitez, vous pouvez remplacer ces styles pour créer un aspect mieux adapté à votre application.

Pour remplacer un style, copiez-le dans son intégralité dans le fichier `styles.xml` de votre projet et apportez vos modifications. Le style entier doit être copié dans votre fichier `styles.xml` local pour que tous les attributs soient correctement définis. Notez que ces styles personnalisés concernent les modifications d'éléments individuels de l'interface, et non les modifications globales de dispositions. Les modifications au niveau de la disposition doivent être gérées avec des vues personnalisées.

{% alert note %}
Vous pouvez personnaliser certaines couleurs directement dans votre campagne Braze sans modifier le XML. N'oubliez pas que les couleurs définies dans le tableau de bord de Braze ont priorité sur celles définies ailleurs.
{% endalert %}

### Personnalisation de la police

Vous pouvez définir une police personnalisée en la plaçant dans le répertoire `res/font`. Pour l'utiliser, remplacez le style du texte du message, des en-têtes et du texte des boutons, puis utilisez l'attribut `fontFamily` pour indiquer à Braze d'utiliser votre famille de polices personnalisée.

Par exemple, pour mettre à jour la police du texte des boutons de message in-app, remplacez le style `Braze.InAppMessage.Button` et référencez votre famille de polices personnalisée. La valeur de l'attribut doit pointer vers une famille de polices dans votre répertoire `res/font`.

Voici un exemple tronqué avec une famille de polices personnalisée `my_custom_font_family`, référencée sur la dernière ligne :

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Outre le style `Braze.InAppMessage.Button` pour le texte des boutons, le style du texte du message est `Braze.InAppMessage.Message` et celui des en-têtes est `Braze.InAppMessage.Header`. Si vous souhaitez utiliser votre famille de polices personnalisée pour l'ensemble du texte des messages in-app, vous pouvez définir votre famille de polices sur le style `Braze.InAppMessage`, qui est le style parent de tous les messages in-app.

{% alert important %}
Comme pour les autres styles personnalisés, le style entier doit être copié dans votre fichier `styles.xml` local pour que tous les attributs soient correctement définis.
{% endalert %}

## Fermeture des messages

### Balayer pour fermer les messages contextuels

Par défaut, les messages in-app contextuels peuvent être fermés d'un geste de balayage. La direction du balayage dépend de la position du message contextuel :

- **Balayage vers la gauche ou la droite :** ferme le message contextuel, quelle que soit sa position.
- **Message contextuel depuis le bas :** un balayage de haut en bas ferme le message. Un balayage de bas en haut ne le ferme pas.
- **Message contextuel depuis le haut :** un balayage de bas en haut ferme le message. Un balayage de haut en bas ne le ferme pas.

Ce comportement de balayage est intégré au [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) par défaut et s'applique uniquement aux messages in-app contextuels. Les messages in-app modaux et plein écran ne prennent pas en charge le balayage pour fermer. Pour personnaliser ce comportement, vous pouvez implémenter une [fabrique de wrappers de vues personnalisée](#android_setting-custom-factories).

{% alert note %}
Appuyer en dehors d'un message contextuel ne le ferme pas par défaut. Ce comportement diffère de celui des messages modaux, qui peuvent être configurés pour se fermer lors d'un appui en dehors de la fenêtre. Pour les messages contextuels, utilisez le geste de balayage ou le bouton de fermeture.
{% endalert %}

### Désactiver la fermeture via le bouton Retour

Par défaut, le bouton Retour matériel ferme les messages in-app de Braze. Ce comportement peut être désactivé message par message via [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html). 

Dans l'exemple suivant, `disable_back_button` est une paire clé-valeur personnalisée définie sur le message in-app qui indique si le bouton Retour doit pouvoir fermer le message :

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
Si cette fonctionnalité est désactivée, le comportement par défaut du bouton Retour matériel de l'activité hôte sera utilisé à la place. Cela peut entraîner la fermeture de l'application plutôt que celle du message in-app affiché.
{% endalert %}

### Activer la fermeture par appui en dehors du message

Par défaut, la fermeture de la fenêtre modale par un appui en dehors de celle-ci est définie sur `false`. Définir cette valeur sur `true` entraînera la fermeture du message in-app modal lorsque l'utilisateur appuie en dehors du message. Ce comportement peut être activé en appelant :

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

## Personnalisation de l'orientation

Pour définir une orientation fixe pour un message in-app, commencez par [définir un écouteur de gestionnaire personnalisé pour les messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners). Ensuite, mettez à jour l'orientation de l'objet `IInAppMessage` dans la méthode déléguée `beforeInAppMessageDisplayed()` :

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

Sur les tablettes, les messages in-app s'affichent dans le style d'orientation préféré de l'utilisateur, quelle que soit l'orientation réelle de l'écran.

## Désactiver le thème sombre {#android-in-app-message-dark-theme-customization}

Par défaut, la méthode `beforeInAppMessageDisplayed()` de `IInAppMessageManagerListener` vérifie les paramètres système et active conditionnellement le thème sombre sur le message à l'aide du code suivant :

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

Pour modifier ce comportement, vous pouvez appeler [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) à n'importe quelle étape du processus de pré-affichage afin d'implémenter votre propre logique conditionnelle.

## Personnalisation de l'invite d'évaluation Google Play

En raison des limitations et restrictions imposées par Google, les invites d'évaluation Google Play personnalisées ne sont actuellement pas prises en charge par Braze. Si certains utilisateurs ont réussi à intégrer ces invites, d'autres ont constaté de faibles taux de réussite en raison des [quotas de Google Play](https://developer.android.com/guide/playcore/in-app-review#quotas). L'intégration se fait à vos risques et périls. Consultez la documentation sur les [invites d'évaluation in-app de Google Play](https://developer.android.com/guide/playcore/in-app-review).