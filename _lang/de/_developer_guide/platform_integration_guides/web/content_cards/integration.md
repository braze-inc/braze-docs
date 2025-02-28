---
nav_title: Integration
article_title: Content Card Integration für das Web
page_order: 0
platform: Web
channel: content cards
page_type: reference
description: "Dieser Artikel beschreibt die Content-Card-Integration für das Web und befasst sich mit Content-Card-Datenmodellen, Standard-Feed-UI-Optionen und zusätzlichen Karten-Methoden."
search_rank: 1
---

# Integration von Inhaltskarten

> Dieser Artikel beschreibt die Content-Card-Integration für das Web und befasst sich mit Content-Card-Datenmodellen, Standard-Feed-UI-Optionen und zusätzlichen Karten-Methoden.

{% multi_lang_include archive/web-v4-rename.md %}

Das Braze Web SDK enthält eine Content-Card-Feed-UI, um den Integrationsvorgang zu beschleunigen. Wenn Sie stattdessen lieber Ihre eigene Benutzeroberfläche erstellen möchten, lesen Sie die [Anleitung zur Anpassung von Inhaltskarten]({{site.baseurl}}/developer_guide/customization_guides/content_cards).

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

## Datenmodell der Inhaltskarte {#data-models}

Das Content-Cards-Datenmodell ist im Web SDK verfügbar.

Das Braze Web SDK bietet drei Arten von Content-Cards: [ImageOnly](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html), [CaptionedImage](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.captionedimage.html) und [ClassicCard](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.classiccard.html). Jeder Typ erbt gemeinsame Eigenschaften von einem Basismodell [Card](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) und hat die folgenden zusätzlichen Eigenschaften.

Informationen zum Abonnieren von Kartendaten finden Sie unter [Logging-Analysen]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics).

### Basisinhalt Kartenmodelleigenschaften - Karte

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

### Eigenschaften der Inhaltskarte nur für Bilder - ImageOnly

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

### Eigenschaften von Content-Cards des Typs "Bildunterschrift" – CaptionedImage

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

### Eigenschaften der Classic Content Card - ClassicCard

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

Wenn Sie eine angepasste Integration für Content-Cards verwenden, müssen Sie [Impressionen protokollieren]({{site.baseurl}}/developer_guide/customization_guides/content_cards/logging_analytics/), wenn eine Kontrollgruppen-Karte gesehen worden wäre. Achten Sie darauf, dass Sie bei der Protokollierung der Impressionen in einem A/B-Test auch die Kontrollgruppen-Karten berücksichtigen. Diese Karten sind leer, und obwohl sie von den Benutzern nicht gesehen werden, sollten Sie dennoch Eindrücke protokollieren, um zu vergleichen, wie sie im Vergleich zu Nicht-Kontrollkarten abschneiden.

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

{% alert note %}
Möchten Sie fortfahren? Wenn Sie die Grundlagen von Content Cards verstanden haben, lesen Sie die [Anleitung zur Anpassung von Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards), um mit der Anpassung zu beginnen.
{% endalert %}
