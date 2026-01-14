---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Iterate, die es Ihnen erlaubt, Kundendaten durch Umfragen anzureichern, um zusätzliche Insights zu gewinnen."
page_type: partner
search_tag: Partner

---

# Iterate

> [Iterate](https://iteratehq.com) macht es Ihnen leicht, von Ihren Kund:innen zu lernen, indem es intelligente, nutzer:innenfreundliche Recherchetools anbietet, die aussehen und sich anfühlen wie Ihre Marke.

_Diese Integration wird von Iterate gepflegt._

## Über die Integration

Die Integration von Iterate in Braze erlaubt es Ihnen, Umfragen von Iterate nativ und nahtlos in Ihrem Produkt oder Ihren Kampagnen bereitzustellen. Umfragen können als angepasste Attribute in Braze aufgezeichnet werden, was es Ihnen erlaubt, sich ein vollständiges Bild von Ihren Nutzer:innen zu machen oder leistungsstarke neue Zielgruppen und Segmente zu erstellen.

Mit dem in Ihrer App oder Website installierten Braze SDK können Sie die in Braze verfügbaren Segmentierungs- und Targeting-Tools nutzen, um Umfragen über In-App-Nachrichten an einen bestimmten Teil Ihrer Zielgruppe zuzustellen, der auf einem beliebigen Auslöser oder angepassten Segment basiert. Iterate Umfragen können auch direkt in Ihre E-Mail Kampagnen eingebettet oder als Link in Ihre Push- oder andere Kampagnen eingebunden werden.

## Voraussetzungen

| Anforderung | Herkunft |
|---|---|
|Konto iterieren | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Iterate-Konto](https://iteratehq.com). |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Um Umfragen über In-App-Nachrichten von Braze zu versenden, benötigen Sie außerdem die Berechtigung `kpi.mau.data_series`.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.|
| Braze REST Endpunkt  | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Anwendungsfälle

Mit Iterate können Sie nahezu alle Arten von Daten erfassen. Von persönlichen Daten (Name, Alter, E-Mail) über Performance-Daten (NPS, Kundenzufriedenheit, Sternebewertungen) bis hin zu Präferenzen (bevorzugtes Gerät, bevorzugte Kommunikationsfrequenz) oder Persönlichkeit (Lieblingsbuch, -hund oder -katze). Was Sie fragen, bleibt ganz Ihnen überlassen, ebenso wie die Art der Daten, die Sie erfassen oder Zielgruppen, die Sie aufbauen möchten.

## Integration

### Die ersten Schritte: Verbinden Sie Braze mit Iterate

Melden Sie sich bei Ihrem Iterate-Konto an und fügen Sie Ihren Braze REST Endpunkt und Ihren REST API-Schlüssel auf der Seite **Unternehmenseinstellungen** hinzu.

### Stellen Sie Umfragen als In-App-Nachricht zu

#### Schritt 1: Erstellen Sie Ihre Umfrage

Bevor Sie Ihre Umfrage erstellen, schalten Sie in den Iterate-Einstellungen die Option **In-App-Nachricht-Umfragen aktivieren** um.

Als nächstes erstellen Sie eine neue Umfrage in Iterate und fügen die relevanten Umfragen hinzu. Bei Bedarf können Sie auch eine Nachricht einfügen, die vor der Umfrage angezeigt wird. Wählen Sie als Umfragetyp **Senden über Braze In-App-Nachrichten** aus.

Sobald Ihre Umfrage abgeschlossen ist, kopieren Sie auf dem Tab **Veröffentlichen** den Code Snippet unter **Kopieren und fügen Sie Ihren Einbettungscode ein**.

#### Schritt 2: Teilen Sie Ihre Umfrage

Erstellen Sie in Braze eine neue In-App Messaging-Kampagne, wählen Sie als Messaging-Typ **Custom Code** aus und fügen Sie Ihren Code-Snippet in die Nachricht ein. Als nächstes wählen Sie für das Verhalten bei einem Klick auf die Nachricht **Warten, bis der Nutzer:innen die Nachricht aufhebt**.

Richten Sie Ihre Kampagne wie jede andere In-App-Messaging-Kampagne ein, indem Sie eine Zustellung wählen und eine Zielgruppe anvisieren.

### Stellen Sie Umfragen per E-Mail oder Push zu

#### Schritt 1: Erstellen Sie Ihre Umfrage

Erstellen Sie eine neue E-Mail- oder Link-Umfrage in Iterate und fügen Sie relevante Umfragen hinzu. Nachdem Sie die Fragen geschrieben und das Design angepasst haben, wählen Sie **Umfrage senden > Integrationen > Braze.**

Sie sehen dann die Konfigurationsoptionen zum Senden von Antworten an Braze. Schalten Sie die Integration ein, um das Senden von Antworten für diese Umfrage an Braze zu ermöglichen. 

#### Schritt 2: Teilen Sie Ihre Umfrage

Ihre Umfrage kann auf zwei Arten weitergegeben werden: indem Sie die erste Frage in Ihre Nachricht einbetten oder einen direkten Link zur Umfrage auf der Iterate-Plattform einfügen.

![Iterate Link-Optionen]({% image_buster /assets/img/iterate.png %})

- **Den Code einbetten**
  - Kopieren Sie den Code-Snippet unter **E-Mail-Einbettungscode** im Abschnitt Integration von Braze auf dem Tab **Umfrage senden**. Fügen Sie den Code in den HTML-Code Ihrer Braze E-Mail an der Stelle ein, an der der Anfang der Umfrage erscheinen soll. 
  - Wenn Sie Probleme mit der Darstellung der Umfragen haben oder wenn diese falsch formatiert sind, müssen Sie im Nachrichten-Editor auf den Tab **Sendeinfo** gehen und die Option **Inline CSS** deaktivieren.
- **Einen Link einfügen**
  - Kopieren Sie den Link unter **Umfrage-Link** im Abschnitt Integration von Braze auf dem Tab **Umfrage senden**. Beachten Sie, dass das Liquid, das im Link {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} enthalten ist, für jeden Nutzer:innen beim Senden automatisch ersetzt wird.

### Nächste Schritte: Aufbau von Nachfolgekampagnen

Wenn Nutzer:innen antworten, werden ihre Profile mit Echtzeitdaten aufgefüllt. Diese Daten können verwendet werden, um Nutzer:innen zu segmentieren und personalisierte Kampagnen zu versenden. Wenn Sie beispielsweise die Frage "Gefallen Ihnen unsere Produkte?" gestellt haben, könnten Sie Segmente von Nutzer:innen erstellen, die das angepasste Attribut `Do you enjoy our products?` haben und mit "Ja" oder "Nein" geantwortet haben, und diese Nutzer:innen als Zielgruppe zusammenstellen.

## Angepasste Events brauen

Wenn ein Nutzer:in eine Umfrage antwortet, triggert Iterate ein angepasstes Event innerhalb von Braze namens `survey-question-response`. Mit angepassten Events können Sie eine beliebige Anzahl und Art von Folgekampagnen triggern.

## Namen von Nutzer:innen-Attributen anpassen

Standardmäßig ist das für eine Frage angelegte Nutzer:in-Attribut dasselbe wie die Eingabeaufforderung.
In einigen Fällen möchten Sie dies vielleicht anpassen. Klicken Sie dazu im Schritt **Umfrage erstellen** auf die Dropdown-Liste **Namen der Nutzer:innen anpassen** und geben Sie die gewünschten angepassten Namen ein.


