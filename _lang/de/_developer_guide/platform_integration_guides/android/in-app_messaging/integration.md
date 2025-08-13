---
nav_title: Integration
article_title: In-App-Nachricht Integration für Android und FireOS
page_order: 1
platform: 
  - Android
  - FireOS
description: "Dieser Artikel erklärt, wie Sie In-App-Nachrichten in Ihre Android- oder FireOS-App integrieren können."
channel:
  - in-app messages
search_rank: 2
---

# Integration von In-App-Nachrichten

> Dieser Artikel erklärt, wie Sie In-App-Nachrichten in Ihre Android- oder FireOS-App integrieren können.

Mit [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) können Sie Ihren Nutzern Inhalte zukommen lassen, ohne sie mit einer Push-Benachrichtigung zu unterbrechen. Angepasste und maßgeschneiderte In-App-Nachrichten verbessern das Nutzererlebnis und helfen Ihrer Zielgruppe, den größten Nutzen aus Ihrer App zu ziehen. Mit den verschiedenen Layouts und Anpassungswerkzeugen, die Ihnen zur Verfügung stehen, binden In-App-Nachrichten Ihre Nutzer mehr als je zuvor.

Um Beispiele für In-App-Nachrichten zu sehen, sehen Sie sich unsere [Anwendungsbeispiele](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html) an.

## In-App-Nachrichtentypen

Braze bietet mehrere Standard In-App-Nachrichtentypen, die jeweils mit Nachrichten, Bildern, [Font Awesome-Symbolen](https://fontawesome.com/icons?d=gallery&p=2), Klick-Aktionen, Analytics, editierbarem Styling und Farbschemata angepasst werden können. Die derzeit verfügbaren Typen sind:

- [`Slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html)
- [`Modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html)
- [`Full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html)
- [`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html)

Es ist auch möglich, Ihre eigene [angepasste In-App-Nachricht-Ansicht]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/#custom-view-factory) zu definieren.

Alle In-App-Nachrichten implementieren die [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html) Schnittstelle, die das grundlegende Verhalten und die Eigenschaften aller In-App-Nachrichten definiert. [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html) ist eine abstrakte Klasse, die `IInAppMessage` implementiert und die grundlegende Implementierung von In-App-Nachrichten bereitstellt. Alle In-App-Nachrichten-Klassen sind Unterklassen von `InAppMessageBase`.

Darüber hinaus gibt es eine Unterschnittstelle von `IInAppMessage` namens [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html), die Klick-Aktions- und Analytics [Enablement-Buttons](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) sowie Kopfzeilentext und einen Schließen-Button hinzufügt.

{% alert important %}
Bei In-App-Nachrichten mit Buttons wird die `clickAction` der Nachricht ebenfalls in die endgültige Nutzlast aufgenommen, wenn die Klickaktion vor dem Hinzufügen des Button-Textes hinzugefügt wird.
{% endalert %}

[`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html) ist eine abstrakte Klasse, die `IInAppMessageImmersive` implementiert und die grundlegende Implementierung von `immersive` In-App-Nachrichten bereitstellt. `Modal`-In-App-Nachrichten sind eine Unterklasse von `InAppMessageImmersiveBase`.

In-App-Nachrichten im HTML-Format sind [`InAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html)-Instanzen, die [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html) implementieren, eine weitere Unterklasse von `IInAppMessage`.

### Erwartete Verhaltensweisen nach Nachrichtentyp

So sieht es aus, wenn Ihre Nutzer eine unserer standardmäßigen In-App-Nachrichten öffnen.

{% tabs local %}
{% tab Slideup %}
[`Slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) In-App-Nachrichten werden so genannt, weil sie vom oberen oder unteren Bildschirmrand nach oben oder unten gleiten. Sie bedecken nur einen kleinen Teil des Bildschirms und bieten eine effektive und unaufdringliche Möglichkeit zur Nachrichtenübermittlung.

![Eine In-App-Nachricht, die vom unteren Rand des Telefondisplays herabgleitet, zeigt an: "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird die gleiche In-App-Nachricht in der unteren rechten Ecke einer Internetseite angezeigt.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}
[`Modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchsichtigen Feld eingerahmt. Für kritischere Nachrichten können sie mit zwei Click-Action- und Analytics-fähigen Buttons ausgestattet werden.

![Eine Modal-In-App-Nachricht in der Mitte des Telefondisplays mit dem Text "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird die gleiche In-App-Nachricht in der Mitte einer Webseite angezeigt.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Vollbild %}
[`Full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html)-In-App-Nachrichten sind nützlich, um den Inhalt und die Wirkung Ihrer Nutzer-Kommunikation zu maximieren. Die obere Hälfte einer In-App-Nachricht von `full` enthält ein Bild, die untere Hälfte Text und bis zu zwei Click-Action- und Analytics-fähigen Buttons.

![Eine In-App-Nachricht im Vollbildmodus, die über den gesamten Bildschirm des Telefons angezeigt wird und lautet: "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird dieselbe In-App-Nachricht weitgehend in der Mitte einer Internetseite angezeigt.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endtab %}
{% tab Benutzerdefiniertes HTML %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html)-In-App-Nachrichten sind nützlich, um vollständig angepasste Nutzerinhalte zu erstellen. Benutzerdefinierte HTML-In-App-Nachrichten werden in `WebView` angezeigt und können optional andere Rich-Content-Inhalte wie Bilder und Schriftarten enthalten, sodass Sie die volle Kontrolle über das Aussehen und die Funktionalität der Nachrichten haben. <br><br>Android In-App-Nachrichten unterstützen eine JavaScript `brazeBridge` Schnittstelle, um Methoden des Braze Web SDK aus Ihrem HTML-Code heraus aufzurufen. Weitere Informationen finden Sie in unseren <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/">Best Practices</a>.

![Eine HTML-In-App-Nachricht mit einem Karussell von Inhalten und interaktiven Buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Die Anzeige angepasster In-App-Nachrichten im HTML-Format in einem iFrame wird derzeit auf den Plattformen iOS und Android nicht unterstützt.
{% endalert %} 

{% endtab %}
{% endtabs %}

#### Definition angepasster In-App-Nachrichtentypen

Das In-App-Nachricht-Objekt `slideup` erweitert [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).
Die Nachrichten vom Typ `full` und `modal` erweitern [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html). Durch die Erweiterung einer dieser Klassen haben Sie die Möglichkeit, Ihre lokal generierten In-App-Nachrichten um angepasste Funktionen zu erweitern.

## Integration {#in-app-messaging-integration}

### Schritt 1: Braze In-App-Nachricht Manager Registrierung

Die Anzeige von In-App-Nachrichten wird von der Klasse [`BrazeInAppMessageManager`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/index.html) verwaltet. Jede Aktivität in Ihrer App muss bei `BrazeInAppMessageManager` registriert sein, damit sie In-App-Nachricht-Ansichten zur Ansichtshierarchie hinzufügen kann. Es gibt zwei Möglichkeiten, dies zu erreichen:

#### Integration von Callbacks für den Aktivitätslebenszyklus (empfohlen)

Die [Callback-Integration für den Aktivitätslebenszyklus]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) verarbeitet die Registrierung von In-App-Nachrichten automatisch; eine zusätzliche Integration ist nicht erforderlich. Dies ist die empfohlene Integration für die Registrierung von In-App-Nachrichten.

#### Manuelle Registrierung von In-App-Nachrichten

{% alert warning %}
Wenn Sie die Integration des Aktivitätslebenszyklus durchgeführt haben, sollten Sie *keine* manuelle Integration von In-App-Nachrichten vornehmen.
{% endalert %}

Als Erstes in Ihrem [`Application.onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate())-Aufruf [`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html):

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

Als Nächstes wird in jeder Aktivität, in der In-App-Nachrichten angezeigt werden können, [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) bei `onResume()` der jeweiligen Aktivität aufgerufen:

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

Und schließlich wird bei jeder Aktivität, in der [`registerInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/register-in-app-message-manager.html) aufgerufen wurde, [`unregisterInAppMessageManager()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/unregister-in-app-message-manager.html) bei `onPause()` der jeweiligen Aktivität aufgerufen:

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

### Schritt 2: In-App-Nachricht Manager Blockliste (optional)

In Ihrer Integration können Sie festlegen, dass bestimmte Aktivitäten in Ihrer App keine In-App-Nachrichten anzeigen sollen. Die [Integration von Callbacks in den Aktivitätslebenszyklus]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android) bietet eine einfache Möglichkeit, dies zu erreichen.

Der folgende Code fügt der Blockliste für die Registrierung von In-App-Nachrichten zwei Aktivitäten hinzu: `SplashActivity` und `SettingsActivity`:

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


