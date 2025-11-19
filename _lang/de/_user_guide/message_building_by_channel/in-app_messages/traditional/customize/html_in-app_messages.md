---
nav_title: HTML In-App-Nachrichten
article_title: Benutzerdefinierte HTML-In-App-Nachrichten
page_order: 0
page_type: reference
description: "Dieser Artikel bietet einen Überblick über angepasste In-App-Nachrichten, einschließlich JavaScript-Methoden, Button-Tracking und Verwendung der interaktiven HTML-Vorschau in Braze."
channel:
  - in-app messages
---

# Benutzerdefinierte HTML-In-App-Nachrichten {#custom-html-messages}

> Während unsere Standard-In-App-Nachrichten auf vielfältige Weise angepasst werden können, haben Sie mit Nachrichten, die mit HTML, CSS und JavaScript entworfen und erstellt wurden, eine noch größere Kontrolle über das Aussehen und die Wirkung Ihrer Kampagnen. Mit einer einfachen Zusammenstellung können Sie angepasste Funktionen und ein individuelles Branding freischalten, das Ihren Bedürfnissen entspricht. 

In-App-Nachrichten im HTML-Format ermöglichen eine größere Kontrolle über das Aussehen einer Nachricht, einschließlich der folgenden Möglichkeiten:

- Benutzerdefinierte Schriftarten und Stile
- Videos
- Mehrere Bilder
- On-Click-Verhalten
- Interaktive Komponenten
- Benutzerdefinierte Animationen

Benutzerdefinierte HTML-Nachrichten können die Methoden von [JavaScript Bridge](#javascript-bridge) verwenden, um Ereignisse zu protokollieren, benutzerdefinierte Attribute zu setzen, die Nachricht zu schließen und vieles mehr! In unserem [GitHub-Repository](https://github.com/braze-inc/in-app-message-templates) finden Sie detaillierte Anleitungen zur Verwendung und Anpassung von HTML-In-App-Nachrichten für Ihre Bedürfnisse sowie eine Reihe von HTML5-Vorlagen für In-App-Nachrichten, die Ihnen den Einstieg erleichtern.

{% alert note %}
Um In-App-Nachrichten im HTML-Format über das Web SDK zu aktivieren, müssen Sie Braze die Initialisierungsoption `allowUserSuppliedJavascript` zur Verfügung stellen, zum Beispiel `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Dies dient der Sicherheit, da HTML-In-App-Nachrichten JavaScript ausführen können. Daher muss ein Website-Administrator sie aktivieren.
{% endalert %}

## JavaScript-Brücke {#javascript-bridge}

HTML-In-App-Nachrichten für Web-, Android-, iOS- und Swift-SDKs unterstützen eine JavaScript-„Bridge“ zur Verbindung mit dem Braze-SDK, sodass Sie angepassten Braze-Aktionen triggern können, wenn Nutzer:innen auf Elemente mit Links klicken oder auf andere Weise mit Ihrem Content interagieren. Diese Methoden existieren mit der globalen Variable `brazeBridge` oder `appboyBridge`.

{% alert important %}
Braze empfiehlt Ihnen, die globale Variable `brazeBridge` zu verwenden. Die globale Variable `appboyBridge` ist veraltet, wird aber für bestehende Benutzer weiterhin funktionieren. Wenn Sie `appboyBridge` verwenden, empfehlen wir Ihnen eine Migration auf `brazeBridge`. <br><br> `appboyBridge` wurde in den folgenden SDK-Versionen veraltet:
- Web: [3.3.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/web/changelog/#330)
- Android: [14.0.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog/#1400)
- iOS: [4.2.0+]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog/#420)
{% endalert %}

Um zum Beispiel ein angepasstes Attribut und ein angepasstes Event zu protokollieren und dann die Nachricht zu schließen, könnten Sie das folgende JavaScript in Ihrer HTML-In-App-Nachricht verwenden:

```html
<button id="button">Set Favorite Color</button>
<script>
// Wait for the `brazeBridge` ready event, "ab.BridgeReady"
window.addEventListener("ab.BridgeReady", function(){
  // Event handler when the button is clicked
  document.querySelector("#button").onclick = function(){
    // Track Button 1 clicks for analytics
    // Note: This requires Android SDK v8.0.0, Web SDK v2.5.0, Swift SDK v5.4.0, and iOS SDK v3.23.0
    brazeBridge.logClick("0");
    // Set the user's custom attribute
    brazeBridge.getUser().setCustomUserAttribute("favorite color", "blue");
    // Track a custom event
    brazeBridge.logCustomEvent("completed survey");
    // Send the enqueued data to Braze
    brazeBridge.requestImmediateDataFlush();
    // Close this in-app message
    brazeBridge.closeMessage();
  };
}, false);
</script>
```

### JavaScript Bridge-Methoden {#bridge}

Die folgenden JavaScript-Methoden werden in Braze HTML-In-App-Nachrichten unterstützt:

<style>
/* Makes first column wider */
#article-main > table:first-of-type > tbody > tr td:first-child {
    min-width: 470px !important;
}
/* Makes code column smaller font */
#article-main > table:first-of-type > tbody > tr td:first-child code {
    font-size:12px !important;
}
#article-main > table:first-of-type td {
  word-break: break-word;
}
</style>

{% alert note %}
Sie können Liquid nicht referenzieren, um <code>customAttributes</code> in JavaScript Bridge-Methoden einzufügen.
{% endalert %}

{% multi_lang_include archive/appboyBridge.md %}

## Link-basierte Aktionen

Zusätzlich zu benutzerdefiniertem JavaScript können die SDKs von Braze auch Analysedaten mit diesen praktischen URL-Kürzeln senden. Beachten Sie, dass bei diesen Abfrageparametern und URL-Schemata die Groß- und Kleinschreibung zu beachten ist.

### Verfolgung von Schaltflächenklicks (veraltet)

{% alert warning %}
Die Verwendung von `abButtonID` wird in [HTML mit Vorschau]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#html-upload-with-preview/) Nachrichtenarten nicht unterstützt. Weitere Informationen finden Sie in unserer [Upgrade-Anleitung]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/preview/#backward-incompatible-changes).
{% endalert %}

Um Klicks auf Buttons für In-App-Nachrichtenanalysen zu protokollieren, können Sie `abButtonId` als Abfrageparameter zu jedem Deeplink, jeder Umleitungs-URL oder jedem Ankerelement `<a>` hinzufügen. Verwenden Sie `?abButtonId=0`, um einen „Button 1“-Klick zu protokollieren, und `?abButtonId=1`, um einen „Button 2“-Klick zu protokollieren.

Wie bei anderen URL-Parametern sollte der erste Parameter mit einem Fragezeichen `?` beginnen, während nachfolgende Parameter durch ein kaufmännisches Und `&` getrennt werden sollten.

#### Beispiel-URLs

- `https://example.com/?abButtonId=0` - Button 1-Klick
- `https://example.com/?abButtonId=1` - Button 2-Klick
- `https://example.com/?utm_source=braze&abButtonId=0` - Schaltfläche 1 Klick mit anderen vorhandenen URL-Parametern
- `myApp://deep-link?page=home&abButtonId=1` - Mobiler Deeplink mit Button 2-Klick
- `<a href="https://example.com/?abButtonId=1">` - Ankerelement `<a>` mit Klick auf Button 2

{% alert note %}
In-App-Nachrichten unterstützen nur Klicks auf Schaltfläche 1 und Schaltfläche 2. URLs, die keine dieser beiden Button-IDs angeben, werden als allgemeine „Text-Klicks“ protokolliert.
{% endalert %}

### Link in neuem Fenster öffnen (nur für Handys)

Um Links außerhalb Ihrer App in einem neuen Fenster zu öffnen, legen Sie `?abExternalOpen=true` fest. Die Nachricht wird vor dem Öffnen des Links gelöscht.

Für Deeplinking öffnet Braze Ihre URL unabhängig vom Wert von `abExternalOpen`.

### Als Deeplink öffnen (nur mobil)

Wenn Braze Ihren HTTP- oder HTTPS-Link als Deeplink behandeln soll, legen Sie `?abDeepLink=true` fest.

Wenn dieser Parameter für den Abfrage-String nicht vorhanden oder auf `false` festgelegt ist, versucht Braze, den Internet-Link in einem internen Webbrowser innerhalb der Host-App zu öffnen.

### In-App-Nachricht schließen

Um eine In-App-Nachricht zu schließen, können Sie die `brazeBridge.closeMessage()`-Javascript-Methode verwenden.

Zum Beispiel: `<a onclick="brazeBridge.closeMessage()" href="#">Close</a>` schließt die In-App-Nachricht.

## HTML-Upload mit Vorschau

Wenn Sie angepasste In-App-Nachrichten im HTML-Format erstellen, können Sie eine Vorschau Ihres interaktiven Content direkt in Braze anzeigen. 

Das Nachrichtenvorschaufenster des Editors zeigt eine realistische Vorschau, die das in Ihrer Nachricht enthaltene JavaScript wiedergibt. Sie können Ihre benutzerdefinierten Nachrichten im Vorschaufenster ansehen und mit ihnen interagieren, indem Sie sich durch die Paginierung klicken, Formulare oder Umfragen absenden, JavaScript-Animationen ansehen und vieles mehr!

![Interaktion mit der HTML-Vorschau durch Wischen durch die Seiten.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Alle `brazeBridge`-JavaScript-Methoden, die Sie in Ihrem HTML-Code verwenden, werden die Nutzerprofile während der Vorschau im Dashboard nicht aktualisieren.
{% endalert %}

### SDK-Anforderungen {#supported-sdk-versions}

Um die HTML-Vorschau für In-App-Nachrichten nutzen zu können, müssen Sie auf die folgenden Braze-SDK-Mindestversionen upgraden:

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
Da dieser Nachrichtentyp nur von bestimmten neueren SDK-Versionen empfangen werden kann, werden Nutzer:innen mit nicht unterstützten SDK-Versionen die Nachricht nicht erhalten. Überlegen Sie sich, ob Sie diesen Nachrichtentyp übernehmen wollen, nachdem Sie einen großen Teil Ihrer Nutzerbasis erreicht haben, oder ob Sie nur diejenigen Nutzer ansprechen wollen, deren App-Version neuer ist als die Anforderungen. Erfahren Sie mehr über das [Filtern nach der neuesten App-Version]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### Erstellen einer Kampagne {#instructions}

Die Nutzer:innen Ihrer mobilen App müssen auf die unterstützten SDK-Versionen upgraden, um eine In-App-Nachricht **mit angepasstem Code** zu erhalten. Wir empfehlen Ihnen, [die Nutzer:innen dazu anzuhalten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/), ihre mobilen Apps zu aktualisieren, bevor Sie Kampagnen starten, die von neueren Braze-SDK-Versionen abhängen.

#### Asset-Dateien

Bei der Erstellung von In-App-Nachricht mit angepasstem Code mit HTML-Upload können Sie Kampagnen-Assets in die [Mediathek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) hochladen, um sie in Ihrer Nachricht zu referenzieren.

Die folgenden Dateitypen werden für den Upload unterstützt:

| Dateityp        | Dateierweiterung                    |
| :--------------- | :-------------------------------- |
| Schriftart-Dateien       | `.ttf`, `.woff`, `.otf`, `.woff2` |
| SVG-Bilder       | `.svg`                            |
| JavaScript-Dateien | `.js`                             |
| CSS-Dateien        | `.css`                            |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze empfiehlt das Hochladen von Assets in die Medienbibliothek aus zwei Gründen:

1. Assets, die einer Kampagne über die Mediathek hinzugefügt werden, ermöglichen es, dass Ihre Nachrichten auch dann angezeigt werden, wenn der Benutzer offline ist oder eine schlechte Internetverbindung hat.
2. Auf Braze hochgeladene Assets können kampagnenübergreifend wiederverwendet werden.

##### Hinzufügen von Asset-Dateien

Sie können neue oder bereits vorhandene Assets zu Ihrer Kampagne hinzufügen.

Um neue Assets zu Ihrer Kampagne hinzuzufügen, verwenden Sie den Drag-and-Drop-Bereich, um eine Datei hochzuladen. Assets, die in diesem Bereich hinzugefügt werden, werden auch automatisch der Bibliothek hinzugefügt. Um Assets hinzuzufügen, die Sie bereits in die Medienbibliothek hochgeladen haben, wählen Sie **Aus Medienbibliothek hinzufügen** aus.

Nachdem Sie Ihre Assets hinzugefügt haben, werden sie im Bereich **Assets für diese Kampagne** angezeigt. 

Wenn der Dateiname eines Assets mit dem eines lokalen HTML-Assets übereinstimmt, wird es automatisch ersetzt (z. B. wenn `cat.png` hochgeladen wird und `<img src="cat.png" />` existiert). 

Andernfalls bewegen Sie den Mauszeiger über ein Asset aus der Liste und wählen <i class="fas fa-copy"></i> **Kopieren**, um die URL der Datei in Ihre Zwischenablage zu kopieren. Fügen Sie dann die kopierte Asset-URL in Ihren HTML-Code ein, wie Sie es normalerweise tun, wenn Sie auf ein entferntes Asset verweisen.


### HTML-Editor

Änderungen, die Sie im HTML-Code vornehmen, werden automatisch im Vorschaufenster angezeigt, während Sie tippen. Alle [`brazeBridge` JavaScript](#bridge)-Methoden, die Sie in Ihrem HTML-Code verwenden, werden die Nutzerprofile während der Vorschau im Dashboard nicht aktualisieren.

{% alert tip %}
Sie können <i class="fa-solid fa-magnifying-glass"></i> **Suche** im HTML-Editor auswählen, um in Ihrem Code zu suchen!
{% endalert %}

### Button-Tracking {#button-tracking-improvements}

Sie können die Performance innerhalb Ihrer In-App-Nachricht mit angepasstem Code mit Hilfe der [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)-JavaScript-Methode verfolgen. Dies erlaubt Ihnen das programmatische Tracking von „Button 1“, „Button 2“ und „Text-Klicks“ mit `brazeBridge.logClick('0')`, `brazeBridge.logClick('1')` bzw. `brazeBridge.logClick()`.

| Klicks     | Methode                       |
| ---------- | ---------------------------- |
| Button 1   | `brazeBridge.logClick('0')` |
| Button 2   | `brazeBridge.logClick('1')` |
| Text-Klick | `brazeBridge.logClick()`    |
| Angepasstes Button-Tracking |`brazeBridge.logClick('your custom name here')`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Diese Methode des Button-Trackings ersetzt die früheren Methoden des automatischen Klick-Tracking (wie z. B. `?abButtonId=0`), die nun entfernt wurden.
{% endalert %}

Sie können mehrere Button-Klick-Ereignisse pro Impression tracken. Um eine Nachricht zu schließen und einen Klick auf Button 2 zu protokollieren, können Sie zum Beispiel Folgendes verwenden:

```html
<a href="#" onclick="brazeBridge.logClick('1');brazeBridge.closeMessage()">✖</a>
``` 

Sie können auch neue benutzerdefinierte Schaltflächennamen verfolgen - bis zu 100 einzigartige Namen pro Kampagne. Zum Beispiel: `brazeBridge.logClick('blue button')` oder `brazeBridge.logClick('viewed carousel page 3')`.

{% alert tip %}
Wenn Sie JavaScript-Methoden innerhalb eines `onclick` Attributs verwenden, schließen Sie String-Werte in einfache Anführungszeichen ein, um Konflikte mit dem HTML-Attribut mit doppelten Anführungszeichen zu vermeiden.
{% endalert %}

#### Beschränkungen

- Sie können bis zu 100 eindeutige Button IDs pro Kampagne haben.
- Schaltflächen-IDs können jeweils bis zu 255 Zeichen lang sein.
- Schaltflächen-IDs dürfen nur Buchstaben, Zahlen, Leerzeichen, Bindestriche und Unterstriche enthalten.

### Rückwärts inkompatible Änderungen {#backward-incompatible-changes}

1. Die auffälligste inkompatible Änderung bei diesem neuen Nachrichtentyp sind die SDK-Anforderungen. Nutzern:innen, deren App-SDK nicht die [Mindestanforderungen an die SDK-Version](#supported-sdk-versions) erfüllt, wird die Nachricht nicht angezeigt.
<br>

2. Der `braze://close`-Deeplink, der bisher in mobilen Apps unterstützt wurde, wurde zugunsten von JavaScript `brazeBridge.closeMessage()` entfernt. Dies ist für plattformübergreifende HTML-Nachrichten zulässig, da das Internet keine Deeplinks unterstützt.

3. Das automatische Tracking von Klicks, bei dem `?abButtonId=0` für Button IDs verwendet wurde, und das Tracking von "Body Clicks" bei Close Buttons wurden entfernt. Die folgenden Code-Beispiele zeigen, wie Sie Ihren HTML-Code so ändern, dass er unsere neuen JavaScript-Methoden zur Klickverfolgung verwendet:

   | Vor | Nach |
   |:-------- |:------------|
   |<code><a href="braze://close">Close Button</a></code>|<code><a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()">Schließen Button</a></code>|
   |<code><a href="braze://close?abButtonId=0">Close Button</a></code>|<code><a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()">Schließen Button</a></code>|
   |<code><a href="app://deeplink?abButtonId=0">Track Button 1</a></code>|<code><a href="app://deeplink" onclick="brazeBridge.logClick('0')">Track Button 1</a></code>|
   |<code><script><br>location.href = "braze://close?abButtonId=1"<br></script></code>|<code><script><br>window.addEventListener("ab.BridgeReady", function(){<br>  brazeBridge.logClick("1");<br>  brazeBridge.closeMessage();<br>});<br></script></code>|

