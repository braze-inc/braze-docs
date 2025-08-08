{% multi_lang_include developer_guide/prerequisites/android.md %} Sie müssen auch [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/in_app_messages/setup/?sdktab=android).

## Angepasste Manager:in Hörer einstellen

{% tabs %}
{% tab globaler Hörer %}
Während der `BrazeInAppMessageManager` Listener die Anzeige und den Lebenszyklus von In-App-Nachrichten automatisch verarbeiten kann, müssen Sie einen angepassten Manager:in implementieren, wenn Sie Ihre Nachrichten vollständig anpassen möchten.
{% endtab %}

{% tab html Listener %}
Das Braze SDK verfügt über die Standardklasse `DefaultHtmlInAppMessageActionListener`. Sie wird verwendet, wenn kein angepasster Listener definiert ist, und führt automatisch die entsprechenden Aktionen durch. Wenn Sie mehr Kontrolle darüber benötigen, wie ein Nutzer mit verschiedenen Buttons in einer angepassten HTML-In-App-Nachricht interagiert, implementieren Sie eine angepasste Klasse des Typs `IHtmlInAppMessageActionListener`.
{% endtab %}
{% endtabs %}

### Schritt 1: Implementieren Sie den angepassten Manager:in Hörer

{% tabs %}
{% tab globaler Hörer %}
#### Schritt 1.1: Implementieren Sie `IInAppMessageManagerListener` 

Erstellen Sie eine Klasse, die [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) implementiert.

Die Callbacks in Ihrer `IInAppMessageManagerListener` werden ebenfalls an verschiedenen Punkten im Lebenszyklus der In-App-Nachricht aufgerufen. Wenn Sie zum Beispiel einen angepassten Manager-Listener für den Empfang einer In-App-Nachricht von Braze festlegen, wird die Methode `beforeInAppMessageDisplayed()` aufgerufen. Wenn Ihre Implementierung dieser Methode [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html#27659854%2FClasslikes%2F-1725759721) zurückgibt, weiß Braze, dass die In-App-Nachricht von der Host-App verarbeitet wird und nicht von Braze angezeigt werden sollte. Wir `InAppMessageOperation.DISPLAY_NOW` zurückgegeben, versucht Braze, die In-App-Nachricht anzuzeigen. Diese Methode sollte verwendet werden, wenn die In-App-Nachricht auf angepasste Art und Weise angezeigt werden soll.

`IInAppMessageManagerListener` enthält auch Delegate-Methoden für Klicks auf Nachrichten und Buttons, die z.B. dazu verwendet werden können, eine Nachricht abzufangen, wenn ein Button oder eine Nachricht angeklickt wird, um sie weiter zu verarbeiten.

#### Schritt 1.2: Einbindung in IAM-Lebenszyklusmethoden (optional)

Die Schnittstelle [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) verfügt über Anzeigemethoden für In-App-Nachrichten, die an verschiedenen Punkten im Lebenszyklus der In-App-Nachrichten-Anzeige aufgerufen werden. Diese Methoden werden in der folgenden Reihenfolge aufgerufen:

1. [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html): Wird aufgerufen, kurz bevor die In-App-Nachricht zur Ansicht der Aktivität hinzugefügt wird. Für den Nutzer ist die In-App-Nachricht zu diesem Zeitpunkt noch nicht sichtbar.
2. [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html): Wird aufgerufen, kurz nachdem die In-App-Nachricht zur Ansicht der Aktivität hinzugefügt wurde. Die In-App-Nachricht ist jetzt für den Nutzer sichtbar.
3. [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html): Wird aufgerufen, kurz bevor die In-App-Nachricht aus der Ansicht der Aktivität entfernt wird. Für den Nutzer ist die In-App-Nachricht zu diesem Zeitpunkt noch sichtbar.
4. [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html): Wird aufgerufen, kurz nachdem die In-App-Nachricht aus der Ansicht der Aktivität entfernt wurde. Die In-App-Nachricht ist zu diesem Zeitpunkt für den Benutzer nicht mehr sichtbar.

Beachten Sie, dass die Zeit zwischen [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) und [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) die Zeit ist, in der die In-App-Nachricht für den Nutzer:innen auf dem Bildschirm sichtbar ist.

{% alert note %}
Die Anwendung dieser Methoden ist nicht erforderlich. Sie werden nur zum Tracking und zur Information über den Lebenszyklus der In-App-Nachricht bereitgestellt. Sie können diese Methodenimplementierungen leer lassen.
{% endalert %}
{% endtab %}

{% tab html Listener %}
Erstellen Sie eine Klasse, die [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html) implementiert.

Die Callbacks in Ihrem `IHtmlInAppMessageActionListener` werden immer dann aufgerufen, wenn der Benutzer eine der folgenden Aktionen innerhalb der HTML-In-App-Nachricht auslöst:

- Klickt auf den Schließen-Button
- Löst ein angepasstes Event aus
- Klicks auf eine URL in einer HTML-In-App-Nachricht

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
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Schritt 2: Weisen Sie Braze an, den angepassten Manager:in Listener zu verwenden

{% tabs %}
{% tab globaler Hörer %}
Nachdem Sie `IInAppMessageManagerListener` erstellt haben, rufen Sie `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` auf, um anzuweisen `BrazeInAppMessageManager`
um Ihren eigenen `IInAppMessageManagerListener` anstelle des Standard-Hörers zu verwenden. Tun Sie dies in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze, damit der angepasste Hörer eingestellt wird, bevor In-App-Nachrichten angezeigt werden.

#### Ändern von In-App-Nachrichten vor der Anzeige

Wenn eine neue In-App-Nachricht eingeht und bereits eine In-App-Nachricht angezeigt wird, wird die neue Nachricht oben auf dem Stapel abgelegt und kann zu einem späteren Zeitpunkt angezeigt werden.

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

Mit dem Rückgabewert `InAppMessageOperation()` kann gesteuert werden, wann die Nachricht angezeigt werden soll. Die Verwendung dieser Methode empfiehlt sich, wenn Nachrichten in bestimmten Teilen der App verzögert werden sollen, indem `DISPLAY_LATER` zurückgegeben wird, wenn In-App-Nachrichten das App-Erlebnis des Nutzers beeinträchtigen würden.

| Rückgabewert `InAppMessageOperation` | Verhalten |
| -------------------------- | -------- |
| `DISPLAY_NOW` | Die Nachricht wird angezeigt |
| `DISPLAY_LATER` | Die Nachricht wird an den Stack zurückgegeben und bei der nächsten Gelegenheit angezeigt. |
| `DISCARD` | Die Nachricht wird verworfen. |
| `null` | Die Nachricht wird ignoriert. Diese Methode sollte **NICHT** zurückgeben `null` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Weitere Informationen finden Sie unter [`InAppMessageOperation.java`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html).

{% alert tip %}
Wenn Sie sich für `DISCARD` entscheiden und Ihre In-App-Nachrichten-Ansicht verwenden, müssen Sie die Klicks und Impressionen der In-App-Nachricht manuell protokollieren.
{% endalert %}

Unter Android wird dies durch den Aufruf von `logClick` und `logImpression` bei In-App-Nachrichten und `logButtonClick` bei immersiven In-App-Nachrichten erreicht.

{% alert tip %}
Sobald eine In-App-Nachricht im Stack platziert wurde, können Sie jederzeit [`BrazeInAppMessageManager.getInstance().requestDisplayInAppMessage()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/request-display-in-app-message.html) aufrufen, damit sie abgerufen und angezeigt wird. Mit dieser Methode wird Braze aufgefordert, die nächste verfügbare In-App-Nachricht aus dem Stack anzuzeigen.
{% endalert %}
{% endtab %}

{% tab html Listener %}
Nachdem Sie `IHtmlInAppMessageActionListener` erstellt haben, rufen Sie `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` auf, um `BrazeInAppMessageManager` anzuweisen, Ihren angepassten `IHtmlInAppMessageActionListener` anstelle des Standard-Aktionshörers zu verwenden.

Wir empfehlen, Ihre `IHtmlInAppMessageActionListener` in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze zu setzen. Dadurch wird der angepasste Aktions-Listener festgelegt, bevor eine In-App-Nachricht angezeigt wird:

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

## Anpassen von Fabriken

Sie können eine Reihe von Standards durch angepasste Fabrikobjekte außer Kraft setzen. Diese können nach Bedarf mit dem Braze SDK registriert werden, um die gewünschten Ergebnisse zu erzielen. Wenn Sie sich jedoch entscheiden, eine Fabrik zu überschreiben, müssen Sie wahrscheinlich explizit auf den Standard zurückgreifen oder die vom Braze-Standard bereitgestellten Funktionen neu implementieren. Der folgende Code-Snippet veranschaulicht, wie Sie angepasste Implementierungen der Schnittstellen `IInAppMessageViewFactory` und `IInAppMessageViewWrapperFactory` bereitstellen können.

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
{% tab ansehen %}
Die in Braze verfügbaren Typen von In-App-Nachrichten sind vielseitig genug, um die meisten angepassten Anwendungsfälle abzudecken. Wenn Sie jedoch das visuelle Erscheinungsbild Ihrer In-App-Nachrichten selbst definieren möchten, anstatt einen Standardtyp zu verwenden, haben Sie dazu in Braze die Möglichkeit, indem Sie eine angepasste Ansichts-Factory festlegen.
{% endtab %}

{% tab view wrapper %}
`BrazeInAppMessageManager` platziert das In-App-Nachrichten-Modell mit [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html)standardmäßig automatisch in der bestehende Hierarchie der Aktivitätsansicht. Wenn Sie die Platzierung der In-App-Nachrichten in der Ansichtshierarchie anpassen müssen, sollte Sie eine angepasste [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) verwenden.
{% endtab %}

{% tab Animation %}
In-App-Nachrichten haben ein voreingestelltes Animationsverhalten. `Slideup` Nachrichten gleiten in den Bildschirm hinein; `full` und `modal` Nachrichten werden ein- und ausgeblendet. Wenn Sie benutzerdefinierte Animationsverhalten für Ihre In-App-Nachrichten definieren möchten, ermöglicht Braze dies durch die Einrichtung einer benutzerdefinierten Animationsfabrik.
{% endtab %}
{% endtabs %}

### Schritt 1: Implementieren Sie die Fabrik

{% tabs %}
{% tab ansehen %}
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

Diese Factory wird unmittelbar nach der Erstellung der In-App-Nachrichten-Ansicht aufgerufen. Der einfachste Weg, einen angepassten [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) zu implementieren, besteht darin, einfach den standardmäßigen [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) zu erweitern:

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

{% tab Animation %}
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

### Schritt 2: Weisen Sie Braze an, die Werkseinstellungen zu verwenden

{% tabs %}
{% tab ansehen %}
Nachdem Ihr `IInAppMessageViewFactory` erstellt wurde, rufen Sie `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` an, um die `BrazeInAppMessageManager`
Ihre angepasste `IInAppMessageViewFactory` anstelle der standardmäßigen Ansichts-Factory zu verwenden.

{% alert tip %}
Wir empfehlen Ihnen, Ihre `IInAppMessageViewFactory` in Ihrem `Application.onCreate()` vor allen anderen Aufrufen von Braze einzustellen. Dadurch wird die angepasste Ansichts-Factory festgelegt, bevor eine In-App-Nachricht angezeigt wird.
{% endalert %}

#### Funktionsweise

Die In-App-Nachricht `slideup` implementiert [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html). Die Nachrichtenansichten vom Typ `full` und `modal` implementieren [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html). Wenn Sie eine dieser Klassen implementieren, kann Braze Ihrer benutzerdefinierten Ansicht bei Bedarf Click-Listener hinzufügen. Alle Braze-Ansichtsklassen erweitern die Android [`View`](http://developer.android.com/reference/android/view/View.html) Klasse.

Durch die Implementierung von `IInAppMessageView` können Sie einen bestimmten Teil Ihrer angepassten Ansicht als anklickbar definieren. Durch die Implementierung von [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) können Sie Ansichten für Nachrichten-Buttons sowie eine Ansicht für einen Schließen-Button zu definieren.
{% endtab %}

{% tab view wrapper %}
Nachdem Ihr [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) erstellt ist, rufen Sie [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) auf, um `BrazeInAppMessageManager` anzuweisen, Ihre angepasste [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) anstelle des Standard View Wrappers zu verwenden.

Wir empfehlen die Einstellung Ihrer [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze zu setzen. Dadurch wird die angepasste View Wrapper-Factory festgelegt, bevor eine In-App-Nachricht angezeigt wird.

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
{% tab Animation %}
Nach dem Erstellen von `IInAppMessageAnimationFactory` rufen Sie `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` auf, um `BrazeInAppMessageManager` anzuweisen,
Ihre angepasste `IInAppMessageAnimationFactory` anstelle der standardmäßigen Animations-Factory zu verwenden.

Wir empfehlen, Ihre `IInAppMessageAnimationFactory` in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze zu setzen. Dadurch wird die angepasste Animations-Factory festgelegt, bevor eine In-App-Nachricht angezeigt wird.
{% endtab %}
{% endtabs %}

## Angepasste Stile

Die UI-Elemente von Braze sind standardmäßig so gestaltet, dass sie den Standard-UI-Richtlinien von Android entsprechen und ein nahtloses Erlebnis bieten. Dieser referenzierte Artikel behandelt das angepasste Stile für In-App-Nachrichten für Ihre Android- oder FireOS-Anwendung.

### Einstellen eines Standard-Stils

Sie können die Standard Stile in der [`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml)-Datei im Braze SDK:

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

Um einen Stil zu überschreiben, kopieren Sie ihn in seiner Gesamtheit in die Datei `styles.xml` Ihres Projekts und nehmen Sie die gewünschten Änderungen vor. Der gesamte Stil muss in Ihre lokale `styles.xml`-Datei kopiert werden, damit alle Attribute korrekt gesetzt werden. Beachten Sie, dass diese angepassten Stile für Änderungen an einzelnen UI-Elementen gedacht sind, nicht für umfassende Änderungen an Layouts. Änderungen auf Layout-Ebene müssen mit angepassten Ansichten gehandhabt werden.

{% alert note %}
Sie können einige Farben direkt in Ihrer Braze Kampagne anpassen, ohne die XML-Datei zu ändern. Denken Sie daran, dass die im Braze-Dashboard eingestellten Farben die Farben überschreiben, die Sie an anderer Stelle eingestellt haben.
{% endalert %}

### Anpassen der Schriftart

Braze erlaubt das Anpassen einer angepassten Schriftart mit Hilfe der [Schriftfamilienführung]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization). Um sie zu verwenden, überschreiben Sie den Stil für Nachrichtentext, Überschriften und Button-Text und verwenden das Attribut `fontFamily`, um Braze anzuweisen, Ihre angepasste Schriftfamilie zu verwenden.

Wenn Sie beispielsweise die Schriftart für den Text Ihres In-App-Nachricht-Buttons aktualisieren möchten, überschreiben Sie den Stil `Braze.InAppMessage.Button` und referenzieren Ihre angepasste Schriftfamilie. Der Wert des Attributs sollte auf eine Schriftfamilie in Ihrem Verzeichnis `res/font` verweisen.

Hier ist ein verkürztes Beispiel mit einer benutzerdefinierten Schriftfamilie, `my_custom_font_family`, auf die in der letzten Zeile verwiesen wird:

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

Neben dem Stil `Braze.InAppMessage.Button` für den Text der Buttons ist der Stil für den Text der Nachrichten `Braze.InAppMessage.Message` und der Stil für die Kopfzeilen der Nachrichten `Braze.InAppMessage.Header`. Wenn Sie Ihre angepasste Schriftfamilie für alle möglichen In-App-Nachrichten verwenden möchten, können Sie Ihre Schriftfamilie auf den Stil `Braze.InAppMessage` setzen, der der übergeordnete Stil für alle In-App-Nachrichten ist.

{% alert important %}
Wie bei anderen angepassten Stilen muss der gesamte Stil in Ihre lokale `styles.xml` Datei kopiert werden, damit alle Attribute korrekt gesetzt werden.
{% endalert %}

## Entlassungen von Nachrichten

### Deaktivieren des Zurück-Buttons

Standardmäßig werden In-App-Nachrichten von Braze mit der Zurück-Taste ausgeblendet. Dieses Verhalten kann für jede einzelne Nachricht deaktiviert werden über [`BrazeInAppMessageManager.setBackButtonDismissesInAppMessageView()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-back-button-dismisses-in-app-message-view.html). 

Im folgenden Beispiel ist `disable_back_button` ein angepasstes Schlüssel-Wert-Paar, das in der In-App-Nachricht festgelegt ist und angibt, ob die Nachricht über die Zurück-Taste ausgeblendet werden kann:

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
Hinweis: Wenn diese Funktion deaktiviert ist, wird stattdessen das Standardverhalten der Zurück-Taste der Host-Aktivität verwendet. Dies kann dazu führen, dass durch die Zurück-Taste die Anwendung statt der angezeigten In-App-Nachricht geschlossen wird.
{% endalert %}

### Enablement von Entlassungen von außen

Standardmäßig ist das Schließen des Modals durch Antippen von außen auf `false` eingestellt. Wenn Sie diesen Wert auf `true` setzen, wird die modale In-App-Nachricht ausgeblendet, wenn der Nutzer auf eine Stelle außerhalb der In-App-Nachricht tippt. Dieses Verhalten kann durch folgenden Aufruf umgeschaltet werden:

```java
BrazeInAppMessageManager.getInstance().setClickOutsideModalViewDismissInAppMessageView(true)
```

## Anpassen der Ausrichtung

Um eine feste Ausrichtung für eine In-App-Nachricht festzulegen, [legen Sie zunächst einen angepassten In-App-Nachrichten-Manager-Listener fest]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners). Rufen Sie dann `setOrientation()` für das Objekt `IInAppMessage` in der Delegiertenmethode `beforeInAppMessageDisplayed()` auf:

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

Bei Tablet-Geräten werden In-App-Nachrichten in der vom Nutzer bevorzugten Ausrichtung angezeigt, unabhängig von der tatsächlichen Bildschirmausrichtung.

## Deaktivieren des dunklen Themas {#android-in-app-message-dark-theme-customization}

Standardmäßig prüft `IInAppMessageManagerListener`'s `beforeInAppMessageDisplayed()` die Systemeinstellungen und aktiviert bedingt das Dark Theme Styling für die Nachricht mit dem folgenden Code:

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

Aufgrund der von Google festgelegten Beschränkungen und Einschränkungen werden angepasste Google Play-Bewertungsaufforderungen derzeit nicht von Braze unterstützt. Während einige Nutzer:innen diese Aufforderungen erfolgreich integrieren konnten, waren die Erfolgsquoten bei anderen aufgrund der [Google Play-Quoten](https://developer.android.com/guide/playcore/in-app-review#quotas) gering. Die Integration erfolgt auf Ihr eigenes Risiko. Lesen Sie die Dokumentation zu den [In-App-Bewertungsaufforderungen von Google Play](https://developer.android.com/guide/playcore/in-app-review).
