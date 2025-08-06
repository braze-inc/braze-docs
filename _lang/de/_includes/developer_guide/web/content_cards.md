{% multi_lang_include archive/web-v4-rename.md %}

## Voraussetzungen

Bevor Sie Content-Cards verwenden können, müssen Sie in Ihre App [das Braze Web SDK integrieren]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web). Es ist jedoch keine zusätzliche Einrichtung erforderlich. Wenn Sie stattdessen Ihr eigenes UI erstellen möchten, lesen Sie die [Anleitung zur Anpassung von Content-Cards]({{site.baseurl}}/developer_guide/content_cards/).

## Standard-Feed UI

Um die integrierte Content Cards UI zu verwenden, müssen Sie angeben, wo der Feed auf Ihrer Website angezeigt werden soll. 

In diesem Beispiel möchten wir den Content-Card-Feed in `<div id="feed"></div>` platzieren. Wir verwenden drei Buttons, um den Feed auszublenden, einzublenden oder umzuschalten (d. h. je nach aktuellem Status aus- oder einzublenden).

```html

<button id="toggle" type="button">Toggle Cards Feed</button>
<button id="hide" type="button">Hide Cards Feed</button>
<button id="show" type="button">Show Cards Feed</button>

<nav>
    <h1>Your Personalized Feed</h1>
    <div id="feed"></div>
</nav>

<script> 
   const toggle = document.getElementById("toggle");
   const hide = document.getElementById("hide");
   const show = document.getElementById("show");
   const feed = document.getElementById("feed");
    
   toggle.onclick = function(){
      braze.toggleContentCards(feed);    
   }
    
   hide.onclick = function(){
      braze.hideContentCards();
   }
    
   show.onclick = function(){
      braze.showContentCards(feed);    
   }
</script>
```

Wenn Sie die Methoden `toggleContentCards(parentNode, filterFunction)` und `showContentCards(parentNode, filterFunction)` verwenden und keine Argumente angeben, werden alle Inhaltskarten in einer Seitenleiste mit fester Position auf der rechten Seite der Seite angezeigt. Andernfalls wird der Feed in der angegebenen Option `parentNode` platziert.

|Parameter | Beschreibung |
|---|---|
|`parentNode` | Der HTML-Knoten, in den die Inhaltskarten gerendert werden sollen. Wenn der übergeordnete Knoten bereits eine Braze Content-Cards-Ansicht als direktes untergeordnetes Element hat, werden die vorhandenen Content-Cards ersetzt. Sie sollten zum Beispiel `document.querySelector(".my-container")` verwenden.|
|`filterFunction` | Eine Filter- oder Sortierfunktion für Karten, die in dieser Ansicht angezeigt werden. Aufgerufen mit dem Array von `Card` Objekten, sortiert nach `{pinned, date}`. Erwartet die Rückgabe eines Arrays von sortierten `Card` Objekten, die für diesen Benutzer dargestellt werden sollen. Wenn Sie diese Option auslassen, werden alle Karten angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

In der [SDK-Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) finden Sie weitere Informationen zum Umschalten von Content-Cards.

## Kartentypen und Eigenschaften

Das Content-Cards-Datenmodell ist im Internet SDK verfügbar und bietet die folgenden Content-Card-Typen: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) und [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Jeder Typ erbt gemeinsame Eigenschaften von einem Basismodell [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) und hat die folgenden zusätzlichen Eigenschaften.

{% alert tip %}
Um Content-Card-Daten zu protokollieren, siehe [Logging Analytics]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/).
{% endalert %}

### Basis-Kartenmodell

Alle Inhaltskarten haben diese gemeinsamen Eigenschaften:

|Eigenschaft|Beschreibung|
|---|---|
| `expiresAt` | Der UNIX-Zeitstempel des Verfallszeitpunkts der Karte.|
| `extras`| (Optional) Schlüssel-Wert-Paar-Daten, formatiert als String-Objekt mit einem Wert-String. |
| `id` | (Optional) Die ID der Karte. Dies wird zu Analysezwecken zusammen mit den Ereignissen an Braze zurückgemeldet. |
| `pinned` | Diese Eigenschaft zeigt an, ob die Karte im Dashboard als "angeheftet" eingerichtet wurde.|
| `updated` | Der UNIX-Zeitstempel, wann diese Karte zuletzt geändert wurde. |
| `viewed` | Diese Eigenschaft zeigt an, ob der Benutzer die Karte angesehen hat oder nicht.|
| `isControl` | Diese Eigenschaft ist `true`, wenn eine Karte eine "Kontrollgruppe" innerhalb eines A/B-Tests ist.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Nur Bild

[ImageOnly-Karten](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) sind anklickbare Bilder in voller Größe.

|Eigenschaft|Beschreibung|
|---|---|
| `aspectRatio` | Das Seitenverhältnis des Kartenbildes und dient als Hinweis, bevor das Laden des Bildes abgeschlossen ist. Beachten Sie, dass die Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
| `categories` | Diese Eigenschaft dient lediglich der Organisation in Ihrer benutzerdefinierten Implementierung; diese Kategorien können im Dashboard Composer festgelegt werden. |
| `clicked` | Diese Eigenschaft zeigt an, ob diese Karte jemals auf diesem Gerät angeklickt wurde. |
| `created` | Der UNIX-Zeitstempel der Erstellungszeit der Karte von Braze. |
| `dismissed` | Diese Eigenschaft zeigt an, ob diese Karte abgewiesen wurde. |
| `dismissible` | Diese Eigenschaft gibt an, ob der Benutzer die Karte aus der Ansicht entfernen kann. |
| `imageUrl` | Die URL des Bildes der Karte.|
| `linkText` | Der Anzeigetext für die URL. |
| `url` | Die URL, die geöffnet wird, nachdem Sie auf die Karte geklickt haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bildunterschrift

[CaptionedImage-Karten](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) sind anklickbare Bilder in voller Größe mit begleitendem beschreibendem Text.

|Eigenschaft|Beschreibung|
|---|---|
| `aspectRatio` | Das Seitenverhältnis des Kartenbildes und dient als Hinweis, bevor das Laden des Bildes abgeschlossen ist. Beachten Sie, dass die Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
| `categories` | Diese Eigenschaft dient lediglich der Organisation in Ihrer benutzerdefinierten Implementierung; diese Kategorien können im Dashboard Composer festgelegt werden. |
| `clicked` | Diese Eigenschaft zeigt an, ob diese Karte jemals auf diesem Gerät angeklickt wurde. |
| `created` | Der UNIX-Zeitstempel der Erstellungszeit der Karte von Braze. |
| `dismissed` | Diese Eigenschaft zeigt an, ob diese Karte abgewiesen wurde. |
| `dismissible` | Diese Eigenschaft gibt an, ob der Benutzer die Karte aus der Ansicht entfernen kann. |
| `imageUrl` | Die URL des Bildes der Karte.|
| `linkText` | Der Anzeigetext für die URL. |
| `title` | Der Titeltext für diese Karte. |
| `url` | Die URL, die geöffnet wird, nachdem Sie auf die Karte geklickt haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Klassisch

Das [ClassicCard-Modell](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html) kann ein Bild ohne Text oder einen Text mit Bild enthalten.

|Eigenschaft|Beschreibung|
|---|---|
| `aspectRatio` | Das Seitenverhältnis des Kartenbildes und dient als Hinweis, bevor das Laden des Bildes abgeschlossen ist. Beachten Sie, dass die Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
| `categories` | Diese Eigenschaft dient lediglich der Organisation in Ihrer benutzerdefinierten Implementierung; diese Kategorien können im Dashboard Composer festgelegt werden. |
| `clicked` | Diese Eigenschaft zeigt an, ob diese Karte jemals auf diesem Gerät angeklickt wurde. |
| `created` | Der UNIX-Zeitstempel der Erstellungszeit der Karte von Braze. |
| `description` | Der Text für diese Karte. |
| `dismissed` | Diese Eigenschaft zeigt an, ob diese Karte abgewiesen wurde. |
| `dismissible` | Diese Eigenschaft gibt an, ob der Benutzer die Karte aus der Ansicht entfernen kann. |
| `imageUrl` | Die URL des Bildes der Karte.|
| `linkText` | Der Anzeigetext für die URL. |
| `title` | Der Titeltext für diese Karte. |
| `url` | Die URL, die geöffnet wird, nachdem Sie auf die Karte geklickt haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Kontrollgruppe

Wenn Sie den standardmäßigen Content-Card-Feed verwenden, werden Impressionen und Klicks automatisch getrackt.

Wenn Sie eine angepasste Integration für Content-Cards verwenden, müssen Sie [Impressionen protokollieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/), wenn eine Kontrollgruppen-Karte gesehen worden wäre. Achten Sie darauf, dass Sie bei der Protokollierung der Impressionen in einem A/B-Test auch die Kontrollgruppen-Karten berücksichtigen. Diese Karten sind leer, und obwohl sie von den Benutzern nicht gesehen werden, sollten Sie dennoch Eindrücke protokollieren, um zu vergleichen, wie sie im Vergleich zu Nicht-Kontrollkarten abschneiden.

Um festzustellen, ob sich eine Content-Card in der Kontrollgruppe für einen A/B-Test befindet, prüfen Sie die Eigenschaft `card.isControl` (Web SDK v4.5.0+) oder prüfen Sie, ob die Karte eine Instanz des Typs `ControlCard` ist (`card instanceof braze.ControlCard`).

## Karten-Methoden

|Methode | Beschreibung |
|---|---|
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| Protokolliert ein Abdruckereignis für die angegebene Liste von Karten. Dies ist erforderlich, wenn Sie eine angepasste Benutzeroberfläche und nicht die Braze-Benutzeroberfläche verwenden.|
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| Protokolliert ein Klickereignis für eine bestimmte Karte. Dies ist erforderlich, wenn Sie eine angepasste Benutzeroberfläche und nicht die Braze-Benutzeroberfläche verwenden.| 
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| Zeigen Sie die Content-Cards des Nutzers an. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| Blenden Sie alle derzeit angezeigten Braze-Inhaltskarten aus. | 
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| Zeigen Sie die Content-Cards des Nutzers an. | 
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)|Holen Sie sich alle aktuell verfügbaren Karten von der letzten Aktualisierung der Inhaltskarten.|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| Abonnieren Sie Content-Card-Updates. <br> Der Abonnenten-Callback wird immer dann aufgerufen, wenn Content-Cards aktualisiert werden. | 
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)|Blenden Sie die Karte programmatisch aus (verfügbar in v2.4.1).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Weitere Einzelheiten finden Sie in der [SDK-Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html)

## Google Tag Manager:in verwenden

Google Tag Manager funktioniert, indem das [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (eine Version unseres Web-SDK) direkt in den Code Ihrer Website injiziert wird. Das bedeutet, dass alle SDK-Methoden genauso verfügbar sind, als hätten Sie das SDK ohne Google Tag Manager integriert, außer bei der Implementierung von Content Cards.

### Content-Cards einrichten

{% tabs local %}
{% tab Google Tag Manager %}
Für eine Standardintegration des Content Card Feeds können Sie ein **benutzerdefiniertes HTML-Tag** im Google Tag Manager verwenden. Fügen Sie Ihrem angepassten HTML-Tag Folgendes hinzu, um den standardmäßigen Content-Card-Feed zu aktivieren:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Tag-Konfiguration eines angepassten HTML-Tags, das den Content-Card-Feed anzeigt, im Google Tag Manager.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab manuell %}
Um das Erscheinungsbild von Content-Cards und ihres Feeds stärker anpassen zu können, können Sie Content-Cards direkt in Ihre native Website integrieren. Hierfür gibt es zwei Möglichkeiten: Sie können die Standard-Feed-Benutzeroberfläche verwenden oder eine benutzerdefinierte Feed-Benutzeroberfläche erstellen.

#### Standard-Feed

Bei der Implementierung der [Standard-Feed-UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui) müssen die Methoden von Braze mit `window.` beginnen. `braze.showContentCards` sollte dann beispielsweise `window.braze.showContentCards` lauten.

#### Benutzerdefinierte Feed UI

Für den Stil des [angepassten Feeds]({{site.baseurl}}/developer_guide/content_cards/creating_cards/) sind die gleichen Schritte durchzuführen wie bei der Integration des SDK ohne GTM. Wenn Sie zum Beispiel die Breite des Content-Card-Feeds anpassen möchten, können Sie Folgendes in Ihre CSS-Datei einfügen:

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Upgraden von Templates {#upgrading}

Um ein Upgrade auf die neueste Version des Braze Web SDK durchzuführen, führen Sie die folgenden drei Schritte im Google Tag Manager-Dashboard aus:

1. **Tag-Template aktualisieren**<br>Rufen Sie die Seite **Vorlagen** in Ihrem Arbeitsbereich auf. Hier sollten Sie ein Symbol sehen, das anzeigt, dass ein Update verfügbar ist.<br><br>![Die Seite mit den Vorlagen zeigt an, dass ein Update verfügbar ist]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Klicken Sie auf dieses Symbol und klicken Sie nach Überprüfung der Änderung auf **Update akzeptieren**.<br><br>![Bildschirm, auf dem ein Vergleich zwischen altem und neuem Tag-Template mit dem Button "Update zustimmen" zu sehen ist]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Versionsnummer aktualisieren**<br>Nachdem Sie das Tag-Template aktualisiert haben, bearbeiten Sie das Braze Initialisierungs-Tag und aktualisieren die SDK-Version auf die neueste Version im Format `major.minor`. Wenn die neueste Version beispielsweise `4.1.2` ist, geben Sie `4.1` ein. Sie können eine Liste der SDK-Versionen in unserem [Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) einsehen.<br><br>![Braze-Template für Initialisierungs-Tags mit einem Eingabefeld zum Ändern der SDK Version]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA und Veröffentlichung**<br>Vergewissern Sie sich, dass die neue SDK-Version funktioniert, indem Sie das [Debugging-Tool](https://support.google.com/tagmanager/answer/6107056?hl=en) von Google Tag Manager verwenden, bevor Sie ein Update für Ihren Tag-Container veröffentlichen.

### Fehlerbehebung {#troubleshooting}

#### Tag-Debugging aktivieren {#debugging}

Jede Braze-Tag-Vorlage verfügt über ein optionales Kontrollkästchen **GTM Tag Debugging**, mit dem Sie Debug-Meldungen in der JavaScript-Konsole Ihrer Webseite protokollieren können.

![Das Debug-Tool von Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### Debugging-Modus aufrufen

Eine weitere Möglichkeit, Ihre Google Tag Manager-Integration zu debuggen, ist die Verwendung der Google-Funktion [Vorschaumodus](https://support.google.com/tagmanager/answer/6107056).

Auf diese Weise können Sie feststellen, welche Werte von der Datenebene Ihrer Webseite an die einzelnen ausgelösten Braze-Tags gesendet werden, und Sie erfahren, welche Tags ausgelöst wurden und welche nicht.

![Seite mit der Zusammenfassung des Braze Initialisierungs-Tags, auf der Sie eine Übersicht über das Tag zusammen mit Informationen zu den getriggerten Tags finden.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### Ausführliche Protokollierung einschalten

Damit der technische Support von Braze während der Tests auf die Protokolle zugreifen kann, können Sie die ausführliche Protokollierung in Ihrer Google Tag Manager-Integration aktivieren. Diese Protokolle erscheinen auf der Registerkarte **Konsole** der [Entwicklertools](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) Ihres Browsers.

Navigieren Sie in der Google Tag Manager-Integration zu Ihrem Braze Initialisierungs-Tag und wählen Sie **Web SDK-Protokollierung aktivieren**.

![Seite mit der Zusammenfassung des Braze Initialisierungs-Tags und der aktivierten Option "Web SDK-Protokollierung aktivieren".]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
