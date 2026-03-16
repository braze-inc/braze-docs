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
Um HTML-In-App-Nachrichten über das Web-SDK zu aktivieren, müssen Sie die`allowUserSuppliedJavascript`Initialisierungsoption an Braze übermitteln, beispielsweise .`braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})` Dies dient der Sicherheit, da HTML-In-App-Nachrichten JavaScript ausführen können. Daher muss ein Website-Administrator sie aktivieren.
{% endalert %}

## JavaScript-Brücke {#javascript-bridge}

{% include javascript_bridge/reference.md %}

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

![Interagieren Sie mit der HTML-Vorschau, indem Sie durch die Seiten wischen.]({% image_buster /assets/img/iam-beta-javascript-preview.gif %})

{% alert tip %}
Alle `brazeBridge`-JavaScript-Methoden, die Sie in Ihrem HTML-Code verwenden, werden die Nutzerprofile während der Vorschau im Dashboard nicht aktualisieren.
{% endalert %}

### SDK-Anforderungen {#supported-sdk-versions}

Um die HTML-Vorschau für In-App-Nachrichten nutzen zu können, müssen Sie auf die folgenden Braze-SDK-Mindestversionen upgraden:

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

{% alert warning %}
Da dieser Nachrichtentyp nur von bestimmten neueren SDK-Versionen empfangen werden kann, erhalten Nutzer:innen, die nicht unterstützte SDK-Versionen verwenden, die Nachricht nicht. Überlegen Sie sich, ob Sie diesen Nachrichtentyp übernehmen wollen, nachdem Sie einen großen Teil Ihrer Nutzerbasis erreicht haben, oder ob Sie nur diejenigen Nutzer ansprechen wollen, deren App-Version neuer ist als die Anforderungen. Erfahren Sie mehr über das [Filtern nach der neuesten App-Version]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).
{% endalert %}

### Erstellen einer Kampagne {#instructions}

Die Nutzer Ihrer mobilen App müssen auf die unterstützten SDK-Versionen upgraden, um eine In-App-Nachricht **mit angepasstem Code** zu empfangen. Wir empfehlen Ihnen, [die Nutzer:innen dazu anzuhalten]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/), ihre mobilen Apps zu aktualisieren, bevor Sie Kampagnen starten, die von neueren Braze-SDK-Versionen abhängen.

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

1. Durch die Medienbibliothek zu einer Kampagne hinzugefügte Assets ermöglichen die Anzeige Ihrer Nachrichten auch dann, wenn der Nutzer:in offline ist oder über eine schlechte Internetverbindung verfügt.
2. Auf Braze hochgeladene Assets können kampagnenübergreifend wiederverwendet werden.

##### Hinzufügen von Asset-Dateien

Sie können neue oder bereits vorhandene Assets zu Ihrer Kampagne hinzufügen.

Um neue Assets zu Ihrer Kampagne hinzuzufügen, verwenden Sie den Drag-and-Drop-Bereich, um eine Datei hochzuladen. Assets, die in diesem Bereich hinzugefügt werden, werden auch automatisch der Bibliothek hinzugefügt. Um Assets hinzuzufügen, die Sie bereits in die Medienbibliothek hochgeladen haben, wählen Sie **Aus Medienbibliothek hinzufügen** aus.

Nachdem Sie Ihre Assets hinzugefügt haben, werden sie im Bereich **Assets für diese Kampagne** angezeigt. 

Wenn der Dateiname eines Assets mit dem eines lokalen HTML-Assets übereinstimmt, wird es automatisch ersetzt (zum Beispiel wird `cat.png`hochgeladen und`<img src="cat.png" />`ist vorhanden). 

Andernfalls bewegen Sie den Mauszeiger über ein Asset aus der Liste und wählen <i class="fas fa-copy"></i> **Kopieren**, um die URL der Datei in Ihre Zwischenablage zu kopieren. Fügen Sie dann die kopierte Asset-URL in Ihren HTML-Code ein, wie Sie es normalerweise tun, wenn Sie auf ein entferntes Asset verweisen.

### HTML-Editor

Änderungen, die Sie im HTML-Code vornehmen, werden automatisch im Vorschaufenster angezeigt, während Sie tippen. Alle [`brazeBridge` JavaScript](#bridge)-Methoden, die Sie in Ihrem HTML-Code verwenden, werden die Nutzerprofile während der Vorschau im Dashboard nicht aktualisieren.

{% alert tip %}
Sie können im HTML-Editor die Option <i class="fa-solid fa-magnifying-glass"></i>**„Suchen“** auswählen, um Ihren Code zu durchsuchen.
{% endalert %}

### Button-Tracking {#button-tracking-improvements}

Sie können die Performance innerhalb Ihrer In-App-Nachricht mit angepasstem Code mit Hilfe der [`brazeBridge.logClick(button_id)`]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)-JavaScript-Methode verfolgen. Die vollständige Referenz finden Sie oben unter [„JavaScript Bridge-Methoden](#bridge)“.

{% alert note %}
Diese Methode des Button-Trackings ersetzt die früheren Methoden des automatischen Klick-Tracking (wie z. B. `?abButtonId=0`), die nun entfernt wurden.
{% endalert %}

### Rückwärts inkompatible Änderungen {#backward-incompatible-changes}

1. Die auffälligste inkompatible Änderung bei diesem neuen Nachrichtentyp sind die SDK-Anforderungen. Nutzern:innen, deren App-SDK nicht die [Mindestanforderungen an die SDK-Version](#supported-sdk-versions) erfüllt, wird die Nachricht nicht angezeigt.
2. Der `braze://close`-Deeplink, der bisher in mobilen Apps unterstützt wurde, wurde zugunsten von JavaScript `brazeBridge.closeMessage()` entfernt. Dies ist für plattformübergreifende HTML-Nachrichten zulässig, da das Internet keine Deeplinks unterstützt.
3. Das automatische Tracking von Klicks, bei dem `?abButtonId=0` für Button IDs verwendet wurde, und das Tracking von "Body Clicks" bei Close Buttons wurden entfernt. Die folgenden Code-Beispiele zeigen, wie Sie Ihren HTML-Code so ändern, dass er unsere neuen JavaScript-Methoden zur Klickverfolgung verwendet:

   | Vor | Nach |
   |:-------- |:------------|
   |<code>&lt;a href="<mem_52e1714a-f29a-4d30-9f54-ca52e321bf80/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick();brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_51e064cb-ed01-4387-acbb-f2a0c2420bbd/>"&gt;Close Button&lt;/a&gt;</code>|<code>&lt;a href="#" onclick="brazeBridge.logClick('0');brazeBridge.closeMessage()"&gt;Close Button&lt;/a&gt;</code>|
   |<code>&lt;a href="<mem_ef9ac2bf-abd8-45a6-ac64-c99b68cae8f3/>">Track button 1&lt;/a&gt;</code>|<code>&lt;a href="<mem_5bf39b0b-da2c-40bd-815d-ac55aaabf3f0/>" onclick="brazeBridge.logClick('0')"&gt;Track button 1&lt;/a&gt;</code>|
   |<code>&lt;script&gt;<br>location.href = "<mem_010dd0e3-c63d-45dc-b2db-b45e77b651fe/>"<br>&lt;/script&gt;</code>|<code>&lt;script&gt;<br>window.addEventListener("ab.BridgeReady", function(){<br>&nbsp;&nbsp;brazeBridge.logClick("1");<br>&nbsp;&nbsp;brazeBridge.closeMessage();<br>});<br>&lt;/script&gt;</code>|

