{% multi_lang_include archive/web-v4-rename.md %}

## Voraussetzungen

Bevor Sie Content-Cards verwenden können, müssen Sie [das Braze Web SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) in Ihre App integrieren. Es ist jedoch keine zusätzliche Einrichtung erforderlich. Wenn Sie stattdessen Ihr eigenes UI erstellen möchten, lesen Sie die [Anleitung zur Anpassung von Content-Cards]({{site.baseurl}}/developer_guide/content_cards/).

## Standard-Feed-UI

Um die integrierte Content-Cards-UI zu verwenden, müssen Sie angeben, wo der Feed auf Ihrer Website angezeigt werden soll. 

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

Wenn Sie die Methoden `toggleContentCards(parentNode, filterFunction)` und `showContentCards(parentNode, filterFunction)` verwenden und keine Argumente angeben, werden alle Content-Cards in einer Seitenleiste mit fester Position auf der rechten Seite der Seite angezeigt. Andernfalls wird der Feed in der angegebenen Option `parentNode` platziert.

|Parameter | Beschreibung |
|---|---|
|`parentNode` | Der HTML-Knoten, in den die Content-Cards gerendert werden sollen. Wenn der übergeordnete Knoten bereits eine Braze Content-Cards-Ansicht als direktes untergeordnetes Element hat, werden die vorhandenen Content-Cards ersetzt. Sie sollten zum Beispiel `document.querySelector(".my-container")` übergeben.|
|`filterFunction` | Eine Filter- oder Sortierfunktion für Karten, die in dieser Ansicht angezeigt werden. Wird mit dem Array von `Card`-Objekten aufgerufen, sortiert nach `{pinned, date}`. Erwartet die Rückgabe eines Arrays von sortierten `Card`-Objekten, die für diese:n Nutzer:in dargestellt werden sollen. Wenn Sie diese Option auslassen, werden alle Karten angezeigt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

In der [SDK-Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards) finden Sie weitere Informationen zum Umschalten von Content-Cards.

## Content-Cards im Internet testen

Sie können Ihre Content-Cards-Integration mit den Entwicklertools Ihres Browsers testen.

1. Erstellen Sie eine Content-Card-Kampagne und richten Sie sie auf Ihre:n Testnutzer:in aus.
2. Melden Sie sich auf der Website an, auf der Ihre Web-SDK-Integration eingerichtet ist.
3. Öffnen Sie die Browser-Konsole. In Chrome rechtsklicken Sie auf die Seite, wählen Sie **Untersuchen** und dann den Tab **Konsole**.
4. Führen Sie diese Befehle in der Konsole aus:
   - `window.braze.getCachedContentCards()`
   - `window.braze.toggleContentCards()`

## Kartentypen und Eigenschaften

Das Content-Cards-Datenmodell ist im Web SDK verfügbar und bietet die folgenden Content-Card-Typen: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) und [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Jeder Typ erbt gemeinsame Eigenschaften von einem Basismodell [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) und hat die folgenden zusätzlichen Eigenschaften.

{% alert tip %}
Um Content-Card-Daten zu protokollieren, siehe [Analytics protokollieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/).
{% endalert %}

### Basis-Kartenmodell

Alle Content-Cards haben diese gemeinsamen Eigenschaften:

|Eigenschaft|Beschreibung|
|---|---|
| `expiresAt` | Der Unix-Zeitstempel des Verfallszeitpunkts der Karte.|
| `extras`| (Optional) Schlüssel-Wert-Paar-Daten, formatiert als String-Objekt mit einem Wert-String. |
| `id` | (Optional) Die ID der Karte. Diese wird zu Analytics-Zwecken zusammen mit den Events an Braze zurückgemeldet. |
| `pinned` | Diese Eigenschaft zeigt an, ob die Karte im Dashboard als „angeheftet" eingerichtet wurde.|
| `updated` | Der Unix-Zeitstempel, wann diese Karte zuletzt geändert wurde. |
| `viewed` | Diese Eigenschaft zeigt an, ob die:der Nutzer:in die Karte angesehen hat oder nicht.|
| `isControl` | Diese Eigenschaft ist `true`, wenn eine Karte eine „Kontrollgruppe" innerhalb eines A/B-Tests ist.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Nur Bild

[ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)-Karten sind anklickbare Bilder in voller Größe.

|Eigenschaft|Beschreibung|
|---|---|
| `aspectRatio` | Das Seitenverhältnis des Kartenbildes, das als Hinweis dient, bevor das Laden des Bildes abgeschlossen ist. Beachten Sie, dass diese Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
| `categories` | Diese Eigenschaft dient lediglich der Organisation in Ihrer angepassten Implementierung; diese Kategorien können im Dashboard Composer festgelegt werden. |
| `clicked` | Diese Eigenschaft zeigt an, ob diese Karte jemals auf diesem Gerät angeklickt wurde. |
| `created` | Der Unix-Zeitstempel der Erstellungszeit der Karte von Braze. |
| `dismissed` | Diese Eigenschaft zeigt an, ob diese Karte abgewiesen wurde. |
| `dismissible` | Diese Eigenschaft gibt an, ob die:der Nutzer:in die Karte aus der Ansicht entfernen kann. |
| `imageUrl` | Die URL des Bildes der Karte.|
| `linkText` | Der Anzeigetext für die URL. |
| `url` | Die URL, die geöffnet wird, nachdem auf die Karte geklickt wurde. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bildunterschrift

[CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html)-Karten sind anklickbare Bilder in voller Größe mit begleitendem beschreibendem Text.

|Eigenschaft|Beschreibung|
|---|---|
| `aspectRatio` | Das Seitenverhältnis des Kartenbildes, das als Hinweis dient, bevor das Laden des Bildes abgeschlossen ist. Beachten Sie, dass diese Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
| `categories` | Diese Eigenschaft dient lediglich der Organisation in Ihrer angepassten Implementierung; diese Kategorien können im Dashboard Composer festgelegt werden. |
| `clicked` | Diese Eigenschaft zeigt an, ob diese Karte jemals auf diesem Gerät angeklickt wurde. |
| `created` | Der Unix-Zeitstempel der Erstellungszeit der Karte von Braze. |
| `dismissed` | Diese Eigenschaft zeigt an, ob diese Karte abgewiesen wurde. |
| `dismissible` | Diese Eigenschaft gibt an, ob die:der Nutzer:in die Karte aus der Ansicht entfernen kann. |
| `imageUrl` | Die URL des Bildes der Karte.|
| `linkText` | Der Anzeigetext für die URL. |
| `title` | Der Titeltext für diese Karte. |
| `url` | Die URL, die geöffnet wird, nachdem auf die Karte geklickt wurde. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Klassisch

Das [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html)-Modell kann ein Bild ohne Text oder einen Text mit Bild enthalten.

|Eigenschaft|Beschreibung|
|---|---|
| `aspectRatio` | Das Seitenverhältnis des Kartenbildes, das als Hinweis dient, bevor das Laden des Bildes abgeschlossen ist. Beachten Sie, dass diese Eigenschaft unter bestimmten Umständen nicht übermittelt werden kann. |
| `categories` | Diese Eigenschaft dient lediglich der Organisation in Ihrer angepassten Implementierung; diese Kategorien können im Dashboard Composer festgelegt werden. |
| `clicked` | Diese Eigenschaft zeigt an, ob diese Karte jemals auf diesem Gerät angeklickt wurde. |
| `created` | Der Unix-Zeitstempel der Erstellungszeit der Karte von Braze. |
| `description` | Der Fließtext für diese Karte. |
| `dismissed` | Diese Eigenschaft zeigt an, ob diese Karte abgewiesen wurde. |
| `dismissible` | Diese Eigenschaft gibt an, ob die:der Nutzer:in die Karte aus der Ansicht entfernen kann. |
| `imageUrl` | Die URL des Bildes der Karte.|
| `linkText` | Der Anzeigetext für die URL. |
| `title` | Der Titeltext für diese Karte. |
| `url` | Die URL, die geöffnet wird, nachdem auf die Karte geklickt wurde. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Kontrollgruppe

Wenn Sie den standardmäßigen Content-Card-Feed verwenden, werden Impressionen und Klicks automatisch getrackt.

Wenn Sie eine angepasste Integration für Content-Cards verwenden, müssen Sie [Impressionen protokollieren]({{site.baseurl}}/developer_guide/content_cards/logging_analytics/), wenn eine Kontrollgruppen-Karte gesehen worden wäre. Achten Sie darauf, dass Sie bei der Protokollierung der Impressionen in einem A/B-Test auch die Kontrollgruppen-Karten berücksichtigen. Diese Karten sind leer, und obwohl sie von den Nutzer:innen nicht gesehen werden, sollten Sie dennoch Impressionen protokollieren, um zu vergleichen, wie sie im Vergleich zu Nicht-Kontrollkarten abschneiden.

Um festzustellen, ob sich eine Content-Card in der Kontrollgruppe für einen A/B-Test befindet, prüfen Sie die Eigenschaft `card.isControl` (Web SDK v4.5.0+) oder prüfen Sie, ob die Karte eine Instanz des Typs `ControlCard` ist (`card instanceof braze.ControlCard`).

## Karten-Methoden

### Standard-Feed-Methoden

Verwenden Sie diese Methoden, wenn Sie Content-Cards mit dem standardmäßigen Braze-Feed-UI anzeigen:

|Methode | Beschreibung |
|---|---|
|[`showContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#showcontentcards)| Zeigt den standardmäßigen Content-Cards-Feed an. Rendert Karten in ein bereitgestelltes `parentNode`-HTML-Element oder als Seitenleiste mit fester Position auf der rechten Seite der Seite, wenn kein Element angegeben wird. Akzeptiert eine optionale `filterFunction`, um Karten vor der Anzeige zu sortieren oder zu filtern. |
|[`hideContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#hidecontentcards)| Blendet den standardmäßigen Content-Cards-Feed aus, wenn er gerade angezeigt wird. |
|[`toggleContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#togglecontentcards)| Zeigt den standardmäßigen Content-Cards-Feed an, wenn er ausgeblendet ist, oder blendet ihn aus, wenn er sichtbar ist. Wenn Sie mehrere Content-Card-Feeds gleichzeitig anzeigen müssen, verwenden Sie stattdessen `showContentCards` und `hideContentCards`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Methoden für angepasste Feeds

Verwenden Sie diese Methoden, wenn Sie Ihr eigenes Content-Card-UI erstellen:

|Methode | Beschreibung |
|---|---|
|[`subscribeToContentCardsUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetocontentcardsupdates)| Registriert eine Callback-Funktion, die aufgerufen wird, wenn Content-Cards für die:den aktuelle:n Nutzer:in aktualisiert werden, z. B. beim Sitzungsstart. Verwenden Sie dies als primäre Methode, um Kartendaten für Ihren angepassten Feed zu erhalten. Muss vor `openSession()` aufgerufen werden, um Updates bei der ersten Sitzung zu erhalten. |
|[`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards)| Gibt alle aktuell verfügbaren Karten von der letzten Content-Cards-Aktualisierung zurück. Verwenden Sie dies, um Karten beim Seitenaufruf sofort anzuzeigen, ohne auf eine neue Serveranfrage zu warten, z. B. wenn die:der Nutzer:in während einer aktiven Sitzung zu einer Seite zurückkehrt. |
|[`requestContentCardsRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh)| Fordert eine sofortige Aktualisierung der Content-Cards von den Braze-Servern an. Standardmäßig werden Karten beim Sitzungsstart und beim erneuten Öffnen des Standard-Feeds aktualisiert. Verwenden Sie dies, um eine Aktualisierung zu anderen Zeitpunkten zu erzwingen, z. B. nach einer bestimmten Nutzeraktion. Beachten Sie die [Rate-Limits]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/feed/#rate-limit). |
|[`logContentCardImpressions`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardimpressions)| Protokolliert Impression-Events für ein Array von Karten. Rufen Sie dies auf, wenn Karten gerendert und für die:den Nutzer:in sichtbar sind. Erforderlich für genaues Kampagnen-Reporting bei Verwendung eines angepassten UI, da Impressionen außerhalb des Standard-Feeds nicht automatisch getrackt werden. |
|[`logContentCardClick`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcontentcardclick)| Protokolliert ein Klick-Event für eine einzelne Karte. Rufen Sie dies auf, wenn eine:ein Nutzer:in mit einer Karte in Ihrem angepassten UI interagiert. Erforderlich für genaues Kampagnen-Reporting, da Klicks außerhalb des Standard-Feeds nicht automatisch getrackt werden. |
|[`handleBrazeAction`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#handlebrazeaction)| Verarbeitet die URL einer Karte und führt die konfigurierte Klick-Aktion aus, einschließlich Braze-Aktionen (`brazeActions://`-URLs) und Standard-URL-Navigation. Rufen Sie dies in Ihrem Karten-Klick-Handler auf, um sicherzustellen, dass im Braze-Dashboard konfigurierte Klick-Verhaltensweisen ausgeführt werden. |
|[`dismissCard`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html#dismisscard)| Blendet eine Karte programmatisch aus und entfernt sie aus dem Feed der:des Nutzers:in. Verwenden Sie dies, um Nutzer:innen das Ausblenden von Karten in Ihrem angepassten UI zu ermöglichen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Einzelheiten finden Sie in der [SDK-Referenzdokumentation](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html).

## Best Practices

### Methoden in der richtigen Reihenfolge aufrufen

Bei angepassten Feeds werden Content-Cards nur beim Sitzungsstart aktualisiert, wenn `subscribeToContentCardsUpdates()` vor `openSession()` aufgerufen wird. Rufen Sie Ihre Braze-Methoden in dieser Reihenfolge auf:

```javascript
import * as braze from "@braze/web-sdk";

// Step 1: Initialize the SDK
braze.initialize("YOUR-API-KEY", { baseUrl: "YOUR-SDK-ENDPOINT" });

// Step 2: Subscribe to card updates
braze.subscribeToContentCardsUpdates((updates) => {
  const cards = updates.cards;
  renderCards(cards);
});

// Step 3: Identify the user
braze.changeUser("USER_ID");

// Step 4: Start the session
braze.openSession();
```

### Gecachte Karten verwenden, um Inhalte über Seitenladevorgänge hinweg beizubehalten

Da `subscribeToContentCardsUpdates()` seinen Callback nur bei neuen Updates aufruft (z. B. beim Sitzungsstart), können Karten aus Ihrem angepassten Feed verschwinden, wenn eine:ein Nutzer:in die Seite während einer Sitzung aktualisiert. Um dies zu verhindern, verwenden Sie `getCachedContentCards()`, um Karten sofort aus dem lokalen Cache zu rendern, zusammen mit Ihrem Abo für neue Updates:

```javascript
import * as braze from "@braze/web-sdk";

function renderCards(cards) {
  const container = document.getElementById("content-cards");
  container.textContent = "";
  const displayedCards = [];

  cards.forEach(card => {
    if (card instanceof braze.ClassicCard || card instanceof braze.CaptionedImage) {
      const cardElement = document.createElement("div");

      const h3 = document.createElement("h3");
      h3.textContent = card.title || "";
      cardElement.appendChild(h3);

      const p = document.createElement("p");
      p.textContent = card.description || "";
      cardElement.appendChild(p);

      if (card.imageUrl) {
        const img = document.createElement("img");
        img.src = card.imageUrl;
        img.alt = card.title || "";
        cardElement.appendChild(img);
      }

      if (card.url) {
        cardElement.addEventListener("click", () => {
          braze.logContentCardClick(card);
          braze.handleBrazeAction(card.url);
        });
      }

      container.appendChild(cardElement);
      displayedCards.push(card);
    }
  });

  if (displayedCards.length > 0) {
    braze.logContentCardImpressions(displayedCards);
  }
}

// Display cached cards immediately
const cached = braze.getCachedContentCards();
if (cached && cached.cards.length > 0) {
  renderCards(cached.cards);
}

// Subscribe to future updates
braze.subscribeToContentCardsUpdates((updates) => {
  renderCards(updates.cards);
});
```

### Analytics für angepasste Feeds protokollieren

Bei Verwendung eines angepassten UI werden Impressionen, Klicks und Ausblendungen nicht automatisch getrackt. Sie müssen jedes Event manuell protokollieren:

- **Impressionen:** Rufen Sie `logContentCardImpressions([card1, card2, ...])` mit einem Array von Kartenobjekten auf, wenn Karten für die:den Nutzer:in sichtbar werden.
- **Klicks:** Rufen Sie `logContentCardClick(card)` auf, wenn eine:ein Nutzer:in mit einer Karte interagiert.
- **Klick-Verhalten:** Rufen Sie `handleBrazeAction(card.url)` auf, um die konfigurierte Klick-Aktion der Karte auszuführen (z. B. Navigation zu einer URL oder Protokollierung eines angepassten Events).

{% alert warning %}
Das an `logContentCardClick()` übergebene Argument muss ein originales Braze-`Card`-Objekt sein. Wenn Sie die Kartendaten transformieren oder rekonstruieren (z. B. durch Serialisierung und Deserialisierung), werden Klicks nicht protokolliert und Sie sehen den Fehler: „card must be a Card object."
{% endalert %}

## Google Tag Manager verwenden

Google Tag Manager funktioniert, indem das [Braze CDN]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (eine Version unseres Web SDK) direkt in den Code Ihrer Website eingespeist wird. Das bedeutet, dass alle SDK-Methoden genauso verfügbar sind, als hätten Sie das SDK ohne Google Tag Manager integriert – außer bei der Implementierung von Content-Cards.

### Content-Cards einrichten

{% tabs local %}
{% tab google tag manager %}
Für eine Standardintegration des Content-Card-Feeds können Sie ein **Custom HTML**-Tag im Google Tag Manager verwenden. Fügen Sie Ihrem Custom-HTML-Tag Folgendes hinzu, um den standardmäßigen Content-Card-Feed zu aktivieren:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Tag-Konfiguration im Google Tag Manager eines Custom-HTML-Tags, das den Content-Card-Feed anzeigt.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})
{% endtab %}

{% tab manual %}
Um das Erscheinungsbild von Content-Cards und ihres Feeds stärker anpassen zu können, können Sie Content-Cards direkt in Ihre native Website integrieren. Hierfür gibt es zwei Möglichkeiten: Sie können die Standard-Feed-UI verwenden oder eine angepasste Feed-UI erstellen.

{% subtabs local %}
{% subtab standard feed %}
Bei der Implementierung der [Standard-Feed-UI]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui) müssen die Methoden von Braze mit `window.` beginnen. `braze.showContentCards` sollte dann beispielsweise `window.braze.showContentCards` lauten.
{% endsubtab %}

{% subtab custom feed %}
Für den Stil des [angepassten Feeds]({{site.baseurl}}/developer_guide/content_cards/creating_cards/) sind die gleichen Schritte durchzuführen wie bei der Integration des SDK ohne GTM. Wenn Sie zum Beispiel die Breite des Content-Card-Feeds anpassen möchten, können Sie Folgendes in Ihre CSS-Datei einfügen:

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Templates upgraden {#upgrading}

Um ein Upgrade auf die neueste Version des Braze Web SDK durchzuführen, führen Sie die folgenden drei Schritte im Google Tag Manager-Dashboard aus:

1. **Tag-Template aktualisieren**<br>Rufen Sie die Seite **Templates** in Ihrem Workspace auf. Hier sollten Sie ein Symbol sehen, das anzeigt, dass ein Update verfügbar ist.<br><br>![Templates-Seite zeigt an, dass ein Update verfügbar ist]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Klicken Sie auf dieses Symbol und klicken Sie nach Überprüfung der Änderung auf **Update akzeptieren**.<br><br>![Ein Bildschirm, der die alten und neuen Tag-Templates vergleicht, mit einem Button „Update akzeptieren"]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Versionsnummer aktualisieren**<br>Nachdem Sie das Tag-Template aktualisiert haben, bearbeiten Sie das Braze-Initialisierungs-Tag und aktualisieren die SDK-Version auf die neueste Version im Format `major.minor`. Wenn die neueste Version beispielsweise `4.1.2` ist, geben Sie `4.1` ein. Sie können eine Liste der SDK-Versionen in unserem [Changelog](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) einsehen.<br><br>![Braze-Initialisierungs-Template mit einem Eingabefeld zum Ändern der SDK-Version]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **QA und Veröffentlichung**<br>Vergewissern Sie sich, dass die neue SDK-Version funktioniert, indem Sie das [Debugging-Tool](https://support.google.com/tagmanager/answer/6107056?hl=en) von Google Tag Manager verwenden, bevor Sie ein Update für Ihren Tag-Container veröffentlichen.

### Fehlerbehebung {#troubleshooting}

#### Tag-Debugging aktivieren {#debugging}

Jedes Braze-Tag-Template verfügt über ein optionales Kontrollkästchen **GTM Tag Debugging**, mit dem Sie Debug-Nachrichten in der JavaScript-Konsole Ihrer Webseite protokollieren können.

![Das Debugging-Tool von Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

#### Debugging-Modus aufrufen

Eine weitere Möglichkeit, Ihre Google Tag Manager-Integration zu debuggen, ist die Verwendung der Google-Funktion [Vorschaumodus](https://support.google.com/tagmanager/answer/6107056).

Auf diese Weise können Sie feststellen, welche Werte von der Datenebene Ihrer Webseite an die einzelnen ausgelösten Braze-Tags gesendet werden, und Sie erfahren, welche Tags ausgelöst wurden und welche nicht.

![Die Übersichtsseite des Braze-Initialisierungs-Tags bietet eine Übersicht über das Tag, einschließlich Informationen darüber, welche Tags ausgelöst wurden.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

#### Tag-Reihenfolge für angepasste Events überprüfen {#tag-sequencing}

Wenn angepasste Events oder andere Aktionen nicht in Braze protokolliert werden, ist eine häufige Ursache eine Race-Condition, bei der ein Aktions-Tag (z. B. **Custom Event** oder **Purchase**) vor dem **Braze-Initialisierungs**-Tag ausgelöst wird. Um dies zu beheben, konfigurieren Sie die [Tag-Reihenfolge](https://support.google.com/tagmanager/answer/6238868) in GTM:

1. Öffnen Sie das Aktions-Tag, das nicht korrekt protokolliert wird.
2. Wählen Sie unter **Erweiterte Einstellungen** > **Tag-Reihenfolge** die Option **Ein Tag, das vor \[diesem Tag\] ausgelöst wird**.
3. Wählen Sie Ihr **Braze-Initialisierungs**-Tag als Setup-Tag.

Dies stellt sicher, dass das SDK vollständig initialisiert ist, bevor Aktions-Tags versuchen, Daten an Braze zu senden.

#### Ausführliche Protokollierung aktivieren

Um detaillierte Protokolle für die Fehlerbehebung zu erfassen, können Sie die ausführliche Protokollierung in Ihrer Google Tag Manager-Integration aktivieren. Diese Protokolle erscheinen im Tab **Konsole** der [Entwicklertools](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) Ihres Browsers.

Navigieren Sie in Ihrer Google Tag Manager-Integration zu Ihrem Braze-Initialisierungs-Tag und wählen Sie **Enable Web SDK Logging**.

![Die Übersichtsseite des Braze-Initialisierungs-Tags mit der aktivierten Option „Enable Web SDK Logging".]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md