---
nav_title: Benutzerdefinierte Hörer
article_title: Benutzerdefinierte In-App Message Listener für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 3
description: "Dieser Referenzartikel behandelt benutzerdefinierte In-App-Messaging-Listener für Ihre Android- oder FireOS-Anwendung."
channel:
  - in-app messages

---

# Benutzerdefinierte Hörer

> Dieser Referenzartikel behandelt benutzerdefinierte In-App-Messaging-Listener für Ihre Android- oder FireOS-Anwendung.

Bevor Sie In-App-Nachrichten mit angepassten Listenern anpassen, ist es wichtig, sich mit [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html) vertraut zu machen, der den Großteil der In-App-Nachrichten verarbeitet. Wie in [Schritt 1]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/integration/#step-1-braze-in-app-message-manager-registration) des Leitfadens zur Integration von App-Nachrichten beschrieben, ist für die ordnungsgemäße Funktion von In-App-Nachrichten eine Registrierung erforderlich.

`BrazeInAppMessageManager` verwaltet die Anzeige von In-App-Nachrichten auf Android. Er enthält Instanzen von Helper-Klassen zur Verwaltung des Lebenszyklus und der Anzeige von In-App-Nachrichten. Für alle diese Klassen gibt es Standardimplementierungen und die Definition eigener Klassen ist völlig optional. Dadurch können Sie jedoch eine weitere Ebene der Kontrolle über die Anzeige und das Verhalten von In-App-Nachrichten hinzufügen. Diese anpassbaren Klassen umfassen:

- [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) - [Angepasste Verwaltung der Anzeige und des Verhaltens von In-App-Nachrichten](#custom-manager-listener)
- [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) - [Erstellung von angepassten In-App-Nachrichten-Ansichten](#custom-view-factory)
- [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html) - [Definieren Sie benutzerdefinierte Animationen für In-App-Nachrichten](#custom-animation-factory)
- [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html) - [Benutzerdefinierte Verwaltung der Anzeige und des Verhaltens von HTML-In-App-Nachrichten](#custom-html-in-app-message-action-listener)
- [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) - [Angepasste Verwaltung der Interaktion bei der Hierarchie von In-App-Nachrichten-Ansichten](#custom-view-wrapper-factory)

{% alert note %}
Dieser Artikel enthält Informationen zum News Feed, der nicht mehr verwendet wird. Braze empfiehlt Kunden, die unser News Feed-Tool verwenden, auf unseren Nachrichtenkanal Content Cards umzusteigen - er ist flexibler, anpassbarer und zuverlässiger. Weitere Informationen finden Sie im [Migrationsleitfaden]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/).
{% endalert %}

## Benutzerdefinierter Manager-Listener

`BrazeInAppMessageManager` verwaltet automatisch die Anzeige und den Lebenszyklus von In-App-Nachrichten. Wenn Sie mehr Kontrolle über den Lebenszyklus einer Nachricht benötigen, können Sie einen benutzerdefinierten Manager-Listener einrichten, der es Ihnen ermöglicht, das In-App-Nachrichtenobjekt an verschiedenen Punkten im Lebenszyklus der In-App-Nachricht zu empfangen. So können Sie die Anzeige der Nachricht selbst steuern, die weitere Verarbeitung vornehmen, auf das Benutzerverhalten reagieren, die [Extras]({{site.baseurl}}/developer_guide/platform_integration_guides/android/news_feed/customization/key_value_pairs/) des Objekts verarbeiten und vieles mehr.

### Schritt 1: Manager-Listenener für In-App-Nachrichten implementieren

Erstellen Sie eine Klasse, die [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) implementiert.

Die Callbacks im `IInAppMessageManagerListener` werden an verschiedenen Punkten im Lebenszyklus der In-App-Nachricht aufgerufen.

Wenn Sie zum Beispiel einen angepassten Manager-Listener für den Empfang einer In-App-Nachricht von Braze festlegen, wird die Methode `beforeInAppMessageDisplayed()` aufgerufen. Wenn Ihre Implementierung dieser Methode [`InAppMessageOperation.DISCARD`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-operation/index.html#27659854%2FClasslikes%2F-1725759721) zurückgibt, weiß Braze, dass die In-App-Nachricht von der Host-App verarbeitet wird und nicht von Braze angezeigt werden sollte. Wir `InAppMessageOperation.DISPLAY_NOW` zurückgegeben, versucht Braze, die In-App-Nachricht anzuzeigen. Diese Methode sollte verwendet werden, wenn die In-App-Nachricht auf angepasste Art und Weise angezeigt werden soll.

`IInAppMessageManagerListener` enthält außerdem Delegate-Methoden für Klicks auf die Nachricht oder einen der Buttons. Ein üblicher Anwendungsfall wäre das Abfangen einer Nachricht, wenn zur weiteren Verarbeitung auf einen Button oder eine Nachricht geklickt wird.

### Schritt 2: Einbindung in die Lebenszyklus-Methoden der Nachrichtenansicht in der App (optional)

Die Schnittstelle [`IInAppMessageManagerListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/index.html) verfügt über Anzeigemethoden für In-App-Nachrichten, die an verschiedenen Punkten im Lebenszyklus der In-App-Nachrichten-Anzeige aufgerufen werden. Diese Methoden werden in der folgenden Reihenfolge aufgerufen:

- [`beforeInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-opened.html): Wird aufgerufen, kurz bevor die In-App-Nachricht zur Ansicht der Aktivität hinzugefügt wird. Für den Nutzer ist die In-App-Nachricht zu diesem Zeitpunkt noch nicht sichtbar.
- [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html): Wird aufgerufen, kurz nachdem die In-App-Nachricht zur Ansicht der Aktivität hinzugefügt wurde. Die In-App-Nachricht ist jetzt für den Nutzer sichtbar.
- [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html): Wird aufgerufen, kurz bevor die In-App-Nachricht aus der Ansicht der Aktivität entfernt wird. Für den Nutzer ist die In-App-Nachricht zu diesem Zeitpunkt noch sichtbar.
- [`afterInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-closed.html): Wird aufgerufen, kurz nachdem die In-App-Nachricht aus der Ansicht der Aktivität entfernt wurde. Die In-App-Nachricht ist zu diesem Zeitpunkt für den Benutzer nicht mehr sichtbar.

Die Zeit zwischen [`afterInAppMessageViewOpened`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/after-in-app-message-view-opened.html) und [`beforeInAppMessageViewClosed`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-in-app-message-manager-listener/before-in-app-message-view-closed.html) entspricht der Zeit, in der die In-App-Nachricht auf dem Bildschirm für den Nutzer sichtbar ist.

{% alert note %}
Die Anwendung dieser Methoden ist nicht erforderlich. Sie werden lediglich bereitgestellt, um den Lebenszyklus von In-App-Nachrichten zu verfolgen und zu melden. Es ist funktional akzeptabel, diese Methodenimplementierungen leer zu lassen.
{% endalert %}

### Schritt 3: Braze zur Verwendung Ihres Manager-Listeners für In-App-Nachrichten auffordern

Nach dem Erstellen von `IInAppMessageManagerListener` rufen Sie `BrazeInAppMessageManager.getInstance().setCustomInAppMessageManagerListener()` auf, um `BrazeInAppMessageManager` anzuweisen,
um Ihren eigenen `IInAppMessageManagerListener` anstelle des Standard-Hörers zu verwenden.

Wir empfehlen, Ihre `IInAppMessageManagerListener` in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze zu setzen. Dadurch wird der angepasste Listener festgelegt, bevor eine In-App-Nachricht angezeigt wird.

#### Ändern von In-App-Nachrichten vor der Anzeige

Wenn eine neue In-App-Nachricht eingeht und bereits eine In-App-Nachricht angezeigt wird, wird die neue Nachricht oben auf dem Stapel abgelegt und kann zu einem späteren Zeitpunkt angezeigt werden.

Wenn jedoch keine In-App-Nachricht angezeigt wird, wird die folgende Delegate-Methode in `IInAppMessageManagerListener` aufgerufen:

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

### Schritt 4: Dark Mode-Design anpassen (optional) {#android-in-app-message-dark-theme-customization}

In der Standardlogik `IInAppMessageManagerListener` werden in `beforeInAppMessageDisplayed()` die Systemeinstellungen überprüft, wobei der Dark Mode-Stil mit folgendem Code bedingt aktiviert wird:

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

Wenn Sie Ihre eigene bedingte Logik verwenden möchten, können Sie [`enableDarkTheme`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-themeable/enable-dark-theme.html) in jedem beliebigen Schritt des Prozesses vor der Anzeige aufrufen.

## Angepasste Ansichts-Factory

Die in Braze verfügbaren Typen von In-App-Nachrichten sind vielseitig genug, um die meisten angepassten Anwendungsfälle abzudecken. Wenn Sie jedoch das visuelle Erscheinungsbild Ihrer In-App-Nachrichten selbst definieren möchten, anstatt einen Standardtyp zu verwenden, haben Sie dazu in Braze die Möglichkeit, indem Sie eine angepasste Ansichts-Factory festlegen.

### Schritt 1: Implementieren einer Ansichts-Factory für In-App-Nachrichten

Erstellen Sie eine Klasse, die [`IInAppMessageViewFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-factory/index.html) implementiert:

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

### Schritt 2: Braze zur Verwendung Ihrer Ansichts-Factory für In-App-Nachrichten auffordern

Nach dem Erstellen von `IInAppMessageViewFactory` rufen Sie `BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewFactory()` auf, um `BrazeInAppMessageManager` anzuweisen,
Ihre angepasste `IInAppMessageViewFactory` anstelle der standardmäßigen Ansichts-Factory zu verwenden.

{% alert tip %}
Wir empfehlen Ihnen, Ihre `IInAppMessageViewFactory` in Ihrem `Application.onCreate()` vor allen anderen Aufrufen von Braze einzustellen. Dadurch wird die angepasste Ansichts-Factory festgelegt, bevor eine In-App-Nachricht angezeigt wird.
{% endalert %}

#### Implementieren einer Braze Ansichts-Schnittstelle

Die In-App-Nachricht `slideup` implementiert [`IInAppMessageView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-view/index.html). Die Nachrichtenansichten vom Typ `full` und `modal` implementieren [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html). Wenn Sie eine dieser Klassen implementieren, kann Braze Ihrer benutzerdefinierten Ansicht bei Bedarf Click-Listener hinzufügen. Alle Braze-Ansichtsklassen erweitern die Android [`View`](http://developer.android.com/reference/android/view/View.html) Klasse.

Durch die Implementierung von `IInAppMessageView` können Sie einen bestimmten Teil Ihrer angepassten Ansicht als anklickbar definieren. Durch die Implementierung von [`IInAppMessageImmersiveView`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.views/-i-in-app-message-immersive-view/index.html) können Sie Ansichten für Nachrichten-Buttons sowie eine Ansicht für einen Schließen-Button zu definieren.

## Angepasste Animations-Factory

In-App-Nachrichten haben ein voreingestelltes Animationsverhalten. `Slideup` Nachrichten gleiten in den Bildschirm hinein; `full` und `modal` Nachrichten werden ein- und ausgeblendet. Wenn Sie benutzerdefinierte Animationsverhalten für Ihre In-App-Nachrichten definieren möchten, ermöglicht Braze dies durch die Einrichtung einer benutzerdefinierten Animationsfabrik.

### Schritt 1: Implementieren einer Animations-Factory für In-App-Nachrichten

Erstellen Sie eine Klasse, die [`IInAppMessageAnimationFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-animation-factory/index.html) implementiert:

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

### Schritt 2: Braze zur Verwendung Ihrer Ansichts-Factory für In-App-Nachrichten auffordern

Nach dem Erstellen von `IInAppMessageAnimationFactory` rufen Sie `BrazeInAppMessageManager.getInstance().setCustomInAppMessageAnimationFactory()` auf, um `BrazeInAppMessageManager` anzuweisen,
Ihre angepasste `IInAppMessageAnimationFactory` anstelle der standardmäßigen Animations-Factory zu verwenden.

Wir empfehlen, Ihre `IInAppMessageAnimationFactory` in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze zu setzen. Dadurch wird die angepasste Animations-Factory festgelegt, bevor eine In-App-Nachricht angezeigt wird.

## Benutzerdefinierter HTML-Aktionshörer für In-App-Nachrichten

Das Braze SDK verfügt über die Standardklasse `DefaultHtmlInAppMessageActionListener`. Sie wird verwendet, wenn kein angepasster Listener definiert ist, und führt automatisch die entsprechenden Aktionen durch. Wenn Sie mehr Kontrolle darüber benötigen, wie ein Nutzer mit verschiedenen Buttons in einer angepassten HTML-In-App-Nachricht interagiert, implementieren Sie eine angepasste Klasse des Typs `IHtmlInAppMessageActionListener`.

### Schritt 1: Implementieren Sie einen benutzerdefinierten HTML-Aktionslistener für In-App-Nachrichten

Erstellen Sie eine Klasse, die [`IHtmlInAppMessageActionListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage.listeners/-i-html-in-app-message-action-listener/index.html) implementiert.

Die Callbacks in Ihrem `IHtmlInAppMessageActionListener` werden immer dann aufgerufen, wenn der Benutzer eine der folgenden Aktionen innerhalb der HTML-In-App-Nachricht auslöst:

- Klickt auf den Schließen-Button
- Löst ein angepasstes Event aus
- Klicks auf eine URL in einer HTML-In-App-Nachricht

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

### Schritt 2: Braze zur Verwendung Ihres Aktions-Listeners für HTML-In-App-Nachrichten auffordern

Nach dem Erstellen von `IHtmlInAppMessageActionListener` rufen Sie `BrazeInAppMessageManager.getInstance().setCustomHtmlInAppMessageActionListener()` auf, um `BrazeInAppMessageManager` anzuweisen, Ihren angepassten `IHtmlInAppMessageActionListener` anstelle des standardmäßigen Aktions-Listeners zu verwenden.

Wir empfehlen, Ihre `IHtmlInAppMessageActionListener` in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze zu setzen. Dadurch wird der angepasste Aktions-Listener festgelegt, bevor eine In-App-Nachricht angezeigt wird:

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

## Angepasste View Wrapper-Factory

`BrazeInAppMessageManager` platziert das In-App-Nachrichten-Modell mit [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html)standardmäßig automatisch in der bestehende Hierarchie der Aktivitätsansicht. Wenn Sie die Platzierung der In-App-Nachrichten in der Ansichtshierarchie anpassen müssen, sollte Sie eine angepasste [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) verwenden.

### Schritt 1: Implementieren einer View Wrapper-Factory für In-App-Nachrichten

Erstellen Sie eine Klasse, die [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) implementiert und einen [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) zurückgibt.

Diese Factory wird unmittelbar nach der Erstellung der In-App-Nachrichten-Ansicht aufgerufen. Der einfachste Weg, einen angepassten [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) zu implementieren, besteht darin, einfach den standardmäßigen [`DefaultInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-default-in-app-message-view-wrapper/index.html) zu erweitern:

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

### Schritt 2: Braze zur Verwendung Ihrer angepassten View Wrapper-Factory auffordern

Nach dem Erstellen von [`IInAppMessageViewWrapper`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper/index.html) rufen Sie [`BrazeInAppMessageManager.getInstance().setCustomInAppMessageViewWrapperFactory()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-in-app-message-manager-base/set-custom-in-app-message-view-factory.html) auf, um `BrazeInAppMessageManager` anzuweisen, Ihre angepasste [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) anstelle der standardmäßigen View Wrapper-Factory zu verwenden.

Wir empfehlen die Einstellung Ihrer [`IInAppMessageViewWrapperFactory`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-i-in-app-message-view-wrapper-factory/index.html) in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) vor allen anderen Aufrufen von Braze zu setzen. Dadurch wird die angepasste View Wrapper-Factory festgelegt, bevor eine In-App-Nachricht angezeigt wird.

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

