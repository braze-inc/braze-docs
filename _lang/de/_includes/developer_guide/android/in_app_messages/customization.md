{% multi_lang_include developer_guide/prerequisites/android.md %} Außerdem müssen Sie [In-App-Nachrichten einrichten]({{site.baseurl}}/developer_guide/in_app_messages).

## Angepasste Manager-Listener einstellen

{% tabs %}
{% tab global listener %}
Während der `BrazeInAppMessageManager`-Listener die Anzeige und den Lebenszyklus von In-App-Nachrichten automatisch verarbeiten kann, müssen Sie einen angepassten Manager-Listener implementieren, wenn Sie Ihre Nachrichten vollständig anpassen möchten.
{% endtab %}

{% tab html listener %}
Das Braze SDK verfügt über die Standardklasse `DefaultHtmlInAppMessageActionListener`. Sie wird verwendet, wenn kein angepasster Listener definiert ist, und führt automatisch die entsprechenden Aktionen durch. Wenn Sie mehr Kontrolle darüber benötigen, wie Nutzer:innen mit verschiedenen Buttons in einer angepassten HTML-In-App-Nachricht interagieren, implementieren Sie eine angepasste Klasse des Typs `IHtmlInAppMessageActionListener`.

Dieser Listener gilt für __beide__ Nachrichtentypen – sowohl für Nachrichten, die mit angepasstem HTML erstellt wurden, als auch für Nachrichten, die mit dem Drag-and-Drop-Editor (DnD) erstellt wurden. Er gilt nicht für traditionelle IAMs. Traditionelle IAMs sind die integrierten, vom SDK gerenderten Nachrichtentypen von Braze (z. B. Slideup, Modal und Full), die im ursprünglichen Nachrichten-Editor für In-App-Nachrichten mit vordefinierten Layouts erstellt werden. Im Gegensatz zu angepassten HTML- und DnD-IAMs durchlaufen sie nicht den HTML-Aktions-Listener-Flow.

Wenn Sie einen angepassten `IHtmlInAppMessageActionListener` festlegen, überschreibt dessen Logik das Standard-Klickverhalten für _alle_ DnD-Nachrichten. Bitte stellen Sie sicher, dass Ihr Marketing-Team darüber informiert ist, da dies deren Kampagnen auf unerwartete Weise beeinflussen kann.
{% endtab %}
{% endtabs %}

### 1. Schritt: Implementieren Sie den angepassten Manager-Listener

{% tabs %}
{% tab global listener %}
#### Schritt 1.1: Implementieren Sie `IInAppMessageManagerListener` 

Erstellen Sie eine Klasse, die [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) implementiert.

Die Callbacks in Ihrem `IInAppMessageManagerListener` werden ebenfalls an verschiedenen Punkten im Lebenszyklus der In-App-Nachricht aufgerufen. Wenn Sie beispielsweise einen angepassten Manager-Listener festlegen und eine In-App-Nachricht von Braze empfangen wird, wird die Methode [`beforeInAppMessageDisplayed()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-displayed.html) aufgerufen. Wenn Ihre Implementierung dieser Methode [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-c-a-r-d/index.html) zurückgibt, signalisiert dies Braze, dass die In-App-Nachricht von der Host-App verarbeitet wird und nicht von Braze angezeigt werden soll. Wenn [`InAppMessageOperation.DISPLAY_NOW`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/-d-i-s-p-l-a-y_-n-o-w/index.html) zurückgegeben wird, versucht Braze, die In-App-Nachricht anzuzeigen. Diese Methode sollte verwendet werden, wenn die In-App-Nachricht auf angepasste Art und Weise angezeigt werden soll.

`IInAppMessageManagerListener` enthält auch Delegate-Methoden für Klicks auf Nachrichten und Buttons, die z. B. dazu verwendet werden können, eine Nachricht abzufangen, wenn ein Button oder eine Nachricht angeklickt wird, um sie weiter zu verarbeiten.

#### Schritt 1.2: Einbindung in IAM-View-Lebenszyklusmethoden (optional)

Die Schnittstelle [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) verfügt über View-Methoden für In-App-Nachrichten, die an verschiedenen Punkten im Lebenszyklus der In-App-Nachrichten-View aufgerufen werden. Diese Methoden werden in der folgenden Reihenfolge aufgerufen:

1. [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html): Wird aufgerufen, kurz bevor die In-App-Nachricht zur View der Activity hinzugefügt wird. Die In-App-Nachricht ist zu diesem Zeitpunkt für die Nutzer:innen noch nicht sichtbar.
2. [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html): Wird aufgerufen, kurz nachdem die In-App-Nachricht zur View der Activity hinzugefügt wurde. Die In-App-Nachricht ist jetzt für die Nutzer:innen sichtbar.
3. [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html): Wird aufgerufen, kurz bevor die In-App-Nachricht aus der View der Activity entfernt wird. Die In-App-Nachricht ist zu diesem Zeitpunkt für die Nutzer:innen noch sichtbar.
4. [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html): Wird aufgerufen, kurz nachdem die In-App-Nachricht aus der View der Activity entfernt wurde. Die In-App-Nachricht ist zu diesem Zeitpunkt für die Nutzer:innen nicht mehr sichtbar.

Beachten Sie, dass die Zeit zwischen [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) und [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) die Zeitspanne ist, in der die In-App-Nachrichten-View auf dem Bildschirm für die Nutzer:innen sichtbar ist.

{% alert note %}
Die Implementierung dieser Methoden ist nicht erforderlich. Sie werden nur zum Tracking und zur Information über den Lebenszyklus der In-App-Nachrichten-View bereitgestellt. Sie können diese Methodenimplementierungen leer lassen.
{% endalert %}
{% endtab %}

{% tab html listener %}
Erstellen Sie eine Klasse, die [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html) implementiert.

Die Callbacks in Ihrem `IHtmlInAppMessageActionListener` werden immer dann aufgerufen, wenn Nutzer:innen eine der folgenden Aktionen innerhalb der HTML-In-App-Nachricht auslösen:

- Klick auf den Schließen-Button
- Auslösen eines angepassten Events
- Klick auf eine URL in einer HTML-In-App-Nachricht

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

### 2. Schritt: Weisen Sie Braze an, den angepassten Manager-Listener zu verwenden

{% tabs %}
{% tab global listener %}
Nachdem Sie `IInAppMessageManagerListener` erstellt haben, rufen Sie `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` auf, um `BrazeInAppMessageManager` anzuweisen, Ihren angepassten `IInAppMessageManagerListener` anstelle des Standard-Listeners zu verwenden. Tun Sie dies in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze, damit der angepasste Listener gesetzt wird, bevor In-App-Nachrichten angezeigt werden.

#### Ändern von In-App-Nachrichten vor der Anzeige

Wenn eine neue In-App-Nachricht eingeht und bereits eine In-App-Nachricht angezeigt wird, wird die neue Nachricht oben auf dem Stack abgelegt und kann zu einem späteren Zeitpunkt angezeigt werden.

Wenn jedoch keine In-App-Nachricht angezeigt wird, wird die folgende Delegate-Methode in `IInAppMessageManagerListener` aufgerufen:

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

Mit dem Rückgabewert von `InAppMessageOperation()` kann gesteuert werden, wann die Nachricht angezeigt werden soll. Die empfohlene Verwendung dieser Methode ist, Nachrichten in bestimmten Teilen der App zu verzögern, indem `DISPLAY_LATER` zurückgegeben wird, wenn In-App-Nachrichten das App-Erlebnis der Nutzer:innen beeinträchtigen würden.

| Rückgabewert `InAppMessageOperation` | Verhalten |
| -------------------------- | -------- |
| `DISPLAY_NOW` | Die Nachricht wird angezeigt |
| `DISPLAY_LATER` | Die Nachricht wird an den Stack zurückgegeben und bei der nächsten Gelegenheit angezeigt |
| `DISCARD` | Die Nachricht wird verworfen |
| `null` | Die Nachricht wird ignoriert. Diese Methode sollte **NICHT** `null` zurückgeben |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Weitere Informationen finden Sie unter [`InAppMessageOperation`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html).

{% alert tip %}
Wenn Sie sich für `DISCARD` entscheiden und die In-App-Nachricht durch Ihre eigene View ersetzen, müssen Sie die Klicks und Impressionen der In-App-Nachricht manuell protokollieren.
{% endalert %}

Unter Android wird dies durch den Aufruf von `logClick` und `logImpression` bei In-App-Nachrichten und `logButtonClick` bei immersiven In-App-Nachrichten erreicht.

{% alert tip %}
Sobald eine In-App-Nachricht im Stack platziert wurde, können Sie jederzeit [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html) aufrufen, damit sie abgerufen und angezeigt wird. Mit dieser Methode wird Braze aufgefordert, die nächste verfügbare In-App-Nachricht aus dem Stack anzuzeigen.
{% endalert %}
{% endtab %}

{% tab html listener %}
Nachdem Sie `IHtmlInAppMessageActionListener` erstellt haben, rufen Sie `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` auf, um `BrazeInAppMessageManager` anzuweisen, Ihren angepassten `IHtmlInAppMessageActionListener` anstelle des Standard-Aktions-Listeners zu verwenden.

Wir empfehlen, Ihren `IHtmlInAppMessageActionListener` in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze zu setzen. Dadurch wird der angepasste Aktions-Listener festgelegt, bevor eine In-App-Nachricht angezeigt wird:

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

## Angepasste Factories einrichten

Sie können eine Reihe von Standardeinstellungen durch angepasste Factory-Objekte überschreiben. Diese können nach Bedarf beim Braze SDK registriert werden, um die gewünschten Ergebnisse zu erzielen. Wenn Sie sich jedoch entscheiden, eine Factory zu überschreiben, müssen Sie wahrscheinlich explizit auf den Standard zurückgreifen oder die vom Braze-Standard bereitgestellte Funktionalität neu implementieren. Das folgende Code-Snippet veranschaulicht, wie Sie angepasste Implementierungen der Schnittstellen `IInAppMessageViewFactory` und `IInAppMessageViewWrapperFactory` bereitstellen können.

{% tabs local %}
{% tab Kotlin %}
**Arten von In-App-Nachrichten**<br>

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
**Arten von In-App-Nachrichten**<br> 

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
Die in Braze verfügbaren Typen von In-App-Nachrichten sind vielseitig genug, um die meisten angepassten Anwendungsfälle abzudecken. Wenn Sie jedoch das visuelle Erscheinungsbild Ihrer In-App-Nachrichten vollständig selbst definieren möchten, anstatt einen Standardtyp zu verwenden, ermöglicht Braze dies durch das Festlegen einer angepassten View-Factory.
{% endtab %}

{% tab view wrapper %}
`BrazeInAppMessageManager` platziert das In-App-Nachrichten-Modell mit [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) standardmäßig automatisch in der bestehenden View-Hierarchie der Activity. Wenn Sie die Platzierung der In-App-Nachrichten in der View-Hierarchie anpassen müssen, sollten Sie eine angepasste [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) verwenden.
{% endtab %}

{% tab animation %}
In-App-Nachrichten haben ein voreingestelltes Animationsverhalten. `Slideup`-Nachrichten gleiten in den Bildschirm hinein; `full`- und `modal`-Nachrichten werden ein- und ausgeblendet. Wenn Sie angepasste Animationsverhalten für Ihre In-App-Nachrichten definieren möchten, ermöglicht Braze dies durch die Einrichtung einer angepassten Animations-Factory.
{% endtab %}
{% endtabs %}

### 1. Schritt: Implementieren Sie die Factory

{% tabs %}
{% tab view %}
Erstellen Sie eine Klasse, die [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) implementiert:

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
Erstellen Sie eine Klasse, die [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) implementiert und einen [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) zurückgibt.

Diese Factory wird unmittelbar nach der Erstellung der In-App-Nachrichten-View aufgerufen. Der einfachste Weg, einen angepassten [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) zu implementieren, besteht darin, den standardmäßigen [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) zu erweitern:

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
Erstellen Sie eine Klasse, die [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html) implementiert:

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

### 2. Schritt: Weisen Sie Braze an, die Factory zu verwenden

{% tabs %}
{% tab view %}
Nachdem Ihre `IInAppMessageViewFactory` erstellt wurde, rufen Sie `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` auf, um `BrazeInAppMessageManager` anzuweisen, Ihre angepasste `IInAppMessageViewFactory` anstelle der standardmäßigen View-Factory zu verwenden.

{% alert tip %}
Wir empfehlen, Ihre `IInAppMessageViewFactory` in Ihrem `Application.onCreate()` vor allen anderen Aufrufen von Braze zu setzen. Dadurch wird die angepasste View-Factory festgelegt, bevor eine In-App-Nachricht angezeigt wird.
{% endalert %}

#### Funktionsweise

Die Slideup-In-App-Nachrichten-View implementiert [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html). Die Nachrichten-Views vom Typ `full` und `modal` implementieren [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html). Wenn Sie eine dieser Klassen implementieren, kann Braze Ihrer angepassten View bei Bedarf Klick-Listener hinzufügen. Alle Braze-View-Klassen erweitern die Android-Klasse [`View`](http://developer.android.com/reference/android/view/View.html).

Durch die Implementierung von `IInAppMessageView` können Sie einen bestimmten Teil Ihrer angepassten View als anklickbar definieren. Durch die Implementierung von [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) können Sie Views für Nachrichten-Buttons sowie eine View für einen Schließen-Button definieren.
{% endtab %}

{% tab view wrapper %}
Nachdem Ihr [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) erstellt ist, rufen Sie [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) auf, um `BrazeInAppMessageManager` anzuweisen, Ihre angepasste [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) anstelle der Standard-View-Wrapper-Factory zu verwenden.

Wir empfehlen, Ihre [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze zu setzen. Dadurch wird die angepasste View-Wrapper-Factory festgelegt, bevor eine In-App-Nachricht angezeigt wird:

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
Nachdem Ihre `IInAppMessageAnimationFactory` erstellt wurde, rufen Sie `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` auf, um `BrazeInAppMessageManager` anzuweisen, Ihre angepasste `IInAppMessageAnimationFactory` anstelle der standardmäßigen Animations-Factory zu verwenden.

Wir empfehlen, Ihre `IInAppMessageAnimationFactory` in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze zu setzen. Dadurch wird die angepasste Animations-Factory festgelegt, bevor eine In-App-Nachricht angezeigt wird.
{% endtab %}
{% endtabs %}

## Angepasste Stile

Die UI-Elemente von Braze sind standardmäßig so gestaltet, dass sie den Standard-UI-Richtlinien von Android entsprechen und ein nahtloses Erlebnis bieten. Dieser Referenzartikel behandelt angepasste Stile für In-App-Nachrichten in Ihrer Android- oder FireOS-Anwendung.

### Einstellen eines Standard-Stils

Sie können die Standardstile in der [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml)-Datei des Braze SDK einsehen:

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

Wenn Sie möchten, können Sie diese Stile überschreiben, um ein Erscheinungsbild zu schaffen, das besser zu Ihrer App passt.

Um einen Stil zu überschreiben, kopieren Sie ihn vollständig in die Datei `styles.xml` Ihres Projekts und nehmen Sie die gewünschten Änderungen vor. Der gesamte Stil muss in Ihre lokale `styles.xml`-Datei kopiert werden, damit alle Attribute korrekt gesetzt werden. Beachten Sie, dass diese angepassten Stile für Änderungen an einzelnen UI-Elementen gedacht sind, nicht für umfassende Änderungen an Layouts. Änderungen auf Layout-Ebene müssen mit angepassten Views gehandhabt werden.

{% alert note %}
Sie können einige Farben direkt in Ihrer Braze-Kampagne anpassen, ohne die XML-Datei zu ändern. Beachten Sie, dass die im Braze-Dashboard eingestellten Farben die an anderer Stelle festgelegten Farben überschreiben.
{% endalert %}

### Anpassen der Schriftart

Sie können eine angepasste Schriftart festlegen, indem Sie die Schriftart im Verzeichnis `res/font` ablegen. Um sie zu verwenden, überschreiben Sie den Stil für Nachrichtentext, Überschriften und Button-Text und verwenden Sie das Attribut `fontFamily`, um Braze anzuweisen, Ihre angepasste Schriftfamilie zu verwenden.

Wenn Sie beispielsweise die Schriftart für den Button-Text Ihrer In-App-Nachricht aktualisieren möchten, überschreiben Sie den Stil `Braze.InAppMessage.Button` und referenzieren Sie Ihre angepasste Schriftfamilie. Der Attributwert sollte auf eine Schriftfamilie in Ihrem Verzeichnis `res/font` verweisen.

Hier ist ein verkürztes Beispiel mit einer angepassten Schriftfamilie `my_custom_font_family`, auf die in der letzten Zeile verwiesen wird:

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Neben dem Stil `Braze.InAppMessage.Button` für den Button-Text ist der Stil für den Nachrichtentext `Braze.InAppMessage.Message` und der Stil für die Nachrichtenüberschriften `Braze.InAppMessage.Header`. Wenn Sie Ihre angepasste Schriftfamilie für alle In-App-Nachrichtentexte verwenden möchten, können Sie Ihre Schriftfamilie auf den Stil `Braze.InAppMessage` setzen, der der übergeordnete Stil für alle In-App-Nachrichten ist.

{% alert important %}
Wie bei anderen angepassten Stilen muss der gesamte Stil in Ihre lokale `styles.xml`-Datei kopiert werden, damit alle Attribute korrekt gesetzt werden.
{% endalert %}

## Schließen von Nachrichten

### Durch Wischen Slideup-Nachrichten schließen

Standardmäßig können Slideup-In-App-Nachrichten durch eine Wischgeste geschlossen werden. Die Richtung des Wischens hängt von der Position des Slideups ab:

- **Nach links oder rechts wischen:** Schließt das Slideup unabhängig von seiner Position.
- **Slideup von unten:** Durch Wischen von oben nach unten wird die Nachricht geschlossen. Durch Wischen von unten nach oben wird sie nicht geschlossen.
- **Slideup von oben:** Durch Wischen von unten nach oben wird die Nachricht geschlossen. Durch Wischen von oben nach unten wird sie nicht geschlossen.

Dieses Wischverhalten ist standardmäßig in [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) integriert und gilt ausschließlich für Slideup-In-App-Nachrichten. Modale und vollständige In-App-Nachrichten unterstützen das Wegwischen nicht. Um dieses Verhalten anzupassen, können Sie eine [angepasste View-Wrapper-Factory](#android_setting-custom-factories) implementieren.

{% alert note %}
Durch Antippen außerhalb einer Slideup-Nachricht wird diese standardmäßig nicht geschlossen. Dieses Verhalten unterscheidet sich von modalen Nachrichten, die für das Schließen durch Tippen außerhalb konfiguriert werden können. Bei Slideups können Sie die Nachricht durch Wischen oder über den Schließen-Button ausblenden.
{% endalert %}

### Deaktivieren des Schließens über die Zurück-Taste

Standardmäßig werden In-App-Nachrichten von Braze mit der Hardware-Zurück-Taste geschlossen. Dieses Verhalten kann für jede einzelne Nachricht über [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html) deaktiviert werden. 

Im folgenden Beispiel ist `disable_back_button` ein angepasstes Schlüssel-Wert-Paar, das in der In-App-Nachricht festgelegt ist und angibt, ob die Nachricht über die Zurück-Taste geschlossen werden kann:

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
Wenn diese Funktion deaktiviert ist, wird stattdessen das Standardverhalten der Zurück-Taste der Host-Activity verwendet. Dies kann dazu führen, dass die Zurück-Taste die Anwendung statt der angezeigten In-App-Nachricht schließt.
{% endalert %}

### Aktivieren des Schließens durch Tippen außerhalb

Standardmäßig ist das Schließen des Modals durch Antippen außerhalb auf `false` eingestellt. Wenn Sie diesen Wert auf `true` setzen, wird die modale In-App-Nachricht geschlossen, wenn Nutzer:innen auf eine Stelle außerhalb der In-App-Nachricht tippen. Dieses Verhalten kann durch folgenden Aufruf aktiviert werden:

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

## Anpassen der Ausrichtung

Um eine feste Ausrichtung für eine In-App-Nachricht festzulegen, [richten Sie zunächst einen angepassten In-App-Nachrichten-Manager-Listener ein]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners). Aktualisieren Sie anschließend die Ausrichtung des `IInAppMessage`-Objekts in der Delegate-Methode `beforeInAppMessageDisplayed()`:

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

Bei Tablet-Geräten werden In-App-Nachrichten in der von den Nutzer:innen bevorzugten Ausrichtung angezeigt, unabhängig von der tatsächlichen Bildschirmausrichtung.

## Deaktivieren des dunklen Designs {#android-in-app-message-dark-theme-customization}

Standardmäßig prüft `beforeInAppMessageDisplayed()` von `IInAppMessageManagerListener` die Systemeinstellungen und aktiviert bedingt das Styling für das dunkle Design der Nachricht mit dem folgenden Code:

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

Um dies zu ändern, können Sie [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) in jedem Schritt des Voranzeigeprozesses aufrufen, um Ihre eigene bedingte Logik zu implementieren.

## Anpassen der Google Play-Bewertungsaufforderung

Aufgrund der von Google festgelegten Beschränkungen und Einschränkungen werden angepasste Google Play-Bewertungsaufforderungen derzeit nicht von Braze unterstützt. Während einige Nutzer:innen diese Aufforderungen erfolgreich integrieren konnten, waren die Erfolgsquoten bei anderen aufgrund der [Google Play-Quoten](https://developer.android.com/guide/playcore/in-app-review#quotas) gering. Die Integration erfolgt auf Ihr eigenes Risiko. Weitere Informationen finden Sie in der Dokumentation zu den [In-App-Bewertungsaufforderungen von Google Play](https://developer.android.com/guide/playcore/in-app-review).