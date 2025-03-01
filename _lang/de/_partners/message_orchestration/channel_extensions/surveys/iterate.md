---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Iterate, die es Ihnen ermöglicht, Kundendaten durch Umfragen anzureichern, um zusätzliche Erkenntnisse zu gewinnen."
page_type: partner
search_tag: Partner

---

# Iterate

> [Iterate](https://iteratehq.com) macht es Ihnen leicht, von Ihren Kunden zu lernen. Es bietet intelligente, benutzerfreundliche Recherchetools, die wie Ihre Marke aussehen und sich anfühlen.

Die Integration von Iterate mit Braze ermöglicht es Ihnen, Iterate-Umfragen nativ und nahtlos in Ihr Produkt oder Ihre Kampagnen einzubinden. Umfrageantworten können als benutzerdefinierte Benutzerattribute in Braze aufgezeichnet werden. So können Sie sich ein vollständiges Bild von Ihren Benutzern machen oder leistungsstarke neue Zielgruppen und Segmente erstellen.

Wenn Sie das Braze SDK in Ihrer App oder Website installiert haben, können Sie die in Braze verfügbaren Segmentierungs- und Targeting-Tools verwenden, um Umfragen über In-App-Nachrichten an einen bestimmten Teil Ihrer Zielgruppe auf der Grundlage eines beliebigen Auslösers oder benutzerdefinierten Segments zu versenden. Iterate-Umfragen können auch direkt in Ihre E-Mail-Kampagnen eingebettet oder als Links in Ihre Push-Kampagnen oder andere Kampagnentypen eingebunden werden.

## Voraussetzungen

| Anforderung | Herkunft |
|---|---|
|Konto iterieren | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Iterate-Konto](https://iteratehq.com). |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. Um Umfragen über In-App-Nachrichten von Braze zu versenden, benötigen Sie außerdem die Genehmigung `kpi.mau.data_series`.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.|
| Braze REST Endpunkt  | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz][6] ab. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Anwendungsfälle

Mit Iterate können Sie fast jede Art von Daten erfassen. Dazu gehören persönliche Daten (Name, Alter, E-Mail), Leistungsdaten (NPS, Kundenzufriedenheit, Sternebewertungen), Vorlieben (bevorzugtes Gerät, bevorzugte Häufigkeit der Kommunikation) oder Persönlichkeit (Lieblingsbuch, Lieblingshund oder Lieblingskatze). Was Sie fragen, bleibt ganz Ihnen überlassen, ebenso wie die Art der Daten, die Sie sammeln wollen, oder die Zielgruppen, die Sie aufbauen wollen.

## Integration

### Die ersten Schritte: Verbinden Sie Braze mit Iterate

Melden Sie sich bei Ihrem Iterate-Konto an und fügen Sie Ihren Braze REST-Endpunkt und Ihren REST-API-Schlüssel auf der Seite **Unternehmenseinstellungen** hinzu.

### Umfragen als In-App-Nachricht bereitstellen

#### Schritt 1: Erstellen Sie Ihre Umfrage

Bevor Sie Ihre Umfrage erstellen, schalten Sie in den Iterate-Einstellungen die Option **Umfragen mit In-App-Nachrichten aktivieren** ein.

Als nächstes erstellen Sie eine neue Umfrage in Iterate und fügen die entsprechenden Fragen hinzu. Gegebenenfalls können Sie auch eine Aufforderungsmeldung einfügen, die vor der Umfrage angezeigt wird. Wählen Sie als Umfragetyp **Senden über Braze In-App Nachricht**.

Sobald Ihre Umfrage abgeschlossen ist, kopieren Sie auf der Registerkarte **Veröffentlichen** das Code-Snippet unter **Kopieren und fügen Sie Ihren Einbettungscode ein**.

#### Schritt 2: Teilen Sie Ihre Umfrage

Erstellen Sie in Braze eine neue In-App-Messaging-Kampagne, wählen Sie als Messaging-Typ **Custom Code** und fügen Sie Ihr Code-Snippet in die Nachricht ein. Wählen Sie als Nächstes die Option **Auf Benutzer warten, um zu beenden** als Verhalten bei einem Klick auf die Nachricht.

Richten Sie Ihre Kampagne wie jede andere In-App-Kampagne ein, indem Sie eine Übermittlungsmethode wählen und eine Zielgruppe anvisieren.

### Stellen Sie Umfragen per E-Mail oder Push-Funktion bereit.

#### Schritt 1: Erstellen Sie Ihre Umfrage

Erstellen Sie eine neue E-Mail- oder Link-Umfrage in Iterate und fügen Sie relevante Fragen hinzu. Nachdem Sie die Fragen geschrieben und den Entwurf angepasst haben, wählen Sie **Umfrage senden > Integrationen > Braze**.

Sie sehen dann die Konfigurationsoptionen zum Senden von Antworten an Braze. Aktivieren Sie die Integration, um das Senden von Antworten für diese Umfrage an Braze zu ermöglichen. 

#### Schritt 2: Teilen Sie Ihre Umfrage

Ihre Umfrage kann auf zwei Arten geteilt werden: indem Sie die erste Frage in Ihre Nachricht einbetten oder einen direkten Link zur Umfrage auf der Iterate-Plattform einfügen.

![Link-Optionen iterieren][2]

- **Den Code einbetten**
  - Kopieren Sie das Code-Snippet unter **E-Mail-Einbettungscode** im Abschnitt Braze-Integration auf der Registerkarte **Umfrage senden**. Fügen Sie den Code in den HTML-Code Ihrer Braze-E-Mail an der Stelle ein, an der der Anfang der Umfrage erscheinen soll. 
  - Wenn Sie Probleme mit der Darstellung der Umfragefragen haben oder wenn sie falsch formatiert sind, müssen Sie im Message Composer auf die Registerkarte **Sendeinformationen** gehen und die Option **Inline-CSS** deaktivieren.
- **Einen Link einfügen**
  - Kopieren Sie den Link unter **Umfrage-Link** im Abschnitt Braze-Integration auf der Registerkarte **Umfrage senden**. Beachten Sie, dass die im Link {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} enthaltene Flüssigkeit beim Senden automatisch für jeden Benutzer ersetzt wird.

### Die nächsten Schritte: Erstellen Sie Folgekampagnen

Wenn Benutzer antworten, sehen Sie, wie ihre Profile in Echtzeit mit Daten gefüllt werden. Diese Daten können verwendet werden, um Benutzer zu segmentieren und personalisierte Folgekampagnen zu versenden. Wenn Sie zum Beispiel die Frage "Gefallen Ihnen unsere Produkte?" gestellt haben, könnten Sie Segmente von Benutzern erstellen, die das benutzerdefinierte Benutzerattribut `Do you enjoy our products?` haben und mit "Ja" oder "Nein" geantwortet haben, und diese Benutzer gezielt ansprechen.

## Braze benutzerdefinierte Ereignisse

Wenn ein Benutzer eine Umfrage beantwortet, löst Iterate ein benutzerdefiniertes Ereignis in Braze mit dem Namen `survey-question-response` aus. Mit benutzerdefinierten Ereignissen können Sie eine beliebige Anzahl und Art von Folgekampagnen auslösen.

## Benutzerattributnamen anpassen

Das Benutzerattribut, das für eine Frage erstellt wird, ist standardmäßig dasselbe wie die Eingabeaufforderung.
In einigen Fällen möchten Sie dies vielleicht anpassen. Klicken Sie dazu im Schritt **Umfrage erstellen** auf das Dropdown-Menü **Benutzerattributnamen anpassen** und geben Sie die gewünschten Namen ein.

[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[2]: {% image_buster /assets/img/iterate.png %}
