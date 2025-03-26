---
nav_title: Angepasste Stile
article_title: In-App-Nachricht Angepasster Stile für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "Dieser referenzierte Artikel behandelt das angepasste Stile für In-App-Nachrichten für Ihre Android- oder FireOS-Anwendung."
channel:
  - in-app messages

---

# Angepasste Stile

> Die UI-Elemente von Braze sind standardmäßig so gestaltet, dass sie den Standard-UI-Richtlinien von Android entsprechen und ein nahtloses Erlebnis bieten. Dieser referenzierte Artikel behandelt das angepasste Stile für In-App-Nachrichten für Ihre Android- oder FireOS-Anwendung.

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

## Eigene Schriftart

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

## Einstellen einer festen Ausrichtung

Um eine feste Ausrichtung für eine In-App-Nachricht festzulegen, [legen Sie zunächst einen angepassten In-App-Nachrichten-Manager-Listener fest]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/). Rufen Sie dann `setOrientation()` für das Objekt `IInAppMessage` in der Delegiertenmethode `beforeInAppMessageDisplayed()` auf:

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

