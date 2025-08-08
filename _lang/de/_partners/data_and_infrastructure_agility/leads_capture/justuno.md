---
nav_title: Justuno
article_title: Justuno
description: "Erfahren Sie, wie Sie Justuno mit Braze integrieren können, damit Sie Kundendaten auf beiden Plattformen nutzen können, um personalisierte Erlebnisse für alle Zielgruppen zu schaffen."

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> [Justuno](https://www.justuno.com/) ermöglicht es Ihnen, mit dynamischen Segmenten ein vollständig optimiertes Besuchererlebnis für alle Ihre Zielgruppen zu schaffen und bietet das fortschrittlichste Targeting, das es gibt - und das alles, ohne die Geschwindigkeit der Website zu beeinträchtigen oder die Entwicklungsarbeit zu erhöhen. Analysieren Sie Konversionsraten, indem Sie angepasste Analytics wie die Anzahl der erstellten Profile, die Rate der wiederkehrenden Besucher und die Seiten pro Sitzung anzeigen, um einen Marketing-Vorteil in Ihrer Branche zu erhalten. Justuno ermöglicht es Ihnen, den Umsatz pro Besucher zu steigern, sinnvolles Kund:in-Engagement zu schaffen und Ihr Geschäft auszubauen. Optimieren Sie die gesamte Zielgruppe von End-to-End mit einer vernetzten Plattform.

## Anwendungsfälle

Braze erlaubt es jedem Marketer, beliebige Datenmengen aus beliebigen Quellen zu sammeln und zu verarbeiten, so dass Sie von einer Plattform aus kreativ und kanalübergreifend in Echtzeit mit Ihren Kunden in Kontakt treten können.

Die Integration von Justuno und Braze bietet Ihnen das Beste aus beiden Welten. Sie können die in Braze gespeicherten Kundendaten mit den in Justuno gespeicherten Besucher- und Kundendaten kombinieren und personalisierte Erlebnisse für alle Zielgruppen schaffen. Dies erhöht die Effektivität Ihrer Marketing Kampagnen und Customer-Engagement STEIGERN.

## Voraussetzungen

| Braze Rest API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track` und `custom_attributes.get`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST-Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) ab.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration von Justuno mit Braze

### Schritt 1: Angepasste Attribute in Braze erstellen

Um Nutzer:innen-Attribute von Justuno mit Braze zu synchronisieren, müssen Sie diese Attribute in Braze erstellen, falls Sie dies nicht bereits getan haben. Gehen Sie dazu zu **Dateneinstellungen** > **Angepasste Attribute** und erstellen Sie dann Ihre angepassten Attribute. Eine vollständige Anleitung finden Sie unter [Anpassen von Attributen in Braze]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/).

### Schritt 2: Hinzufügen der App Braze zu Justuno

#### Schritt 2.1: Fügen Sie es zu Ihrem Konto hinzu

Um die Braze App zu Ihrem Justuno-Konto hinzuzufügen, gehen Sie zu **Kontoeinstellungen** > **Apps**, suchen Sie dann nach der Braze App und wählen Sie sie aus.

![Die Seite "Apps verbinden" in Justuno mit der App Braze in der Liste der Suchergebnisse.]({% image_buster /assets/img/justuno/search-for-braze.png %})

Geben Sie den API-Schlüssel und die Basis-URL ein [, die Sie zuvor erstellt haben](#prerequisites), und wählen Sie dann **Verbinden**.

![Das Braze-Authentifizierungs-Popup-Fenster, das nach einem Braze-API-Schlüssel und der Basis-URL fragt.]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### Schritt 2.2: Fügen Sie es Ihrem Arbeitsablauf hinzu

Um die App Braze zu Ihrem [Justuno-Workflow](https://hub.justuno.com/knowledge/workflows-overview) hinzuzufügen, ziehen Sie die Aktion **Mit App synchronisieren** per Drag-and-Drop in Ihren Workflow und wählen Sie dann **App auswählen** > **Braze**.

![Die Option "App auswählen" befindet sich bei der Aktion "Mit App synchronisieren".]({% image_buster /assets/img/justuno/select-app.png %}){: style="max-width:45%;"}

### Schritt 3: Verbinden Sie Ihre Abo-Gruppen von Braze

Um Profildaten von Justuno an eine bestimmte E-Mail- oder SMS-Abonnementgruppe von Braze zu senden, müssen Sie deren ID in der Braze App in Ihrem Justuno-Workflow hinzufügen.

| ID Typ                          | Erforderlich? | Beschreibung                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| Braze SMS Abo-Gruppe ID  | Ja       | Diese ID wird verwendet, um SMS-Zustimmungen von Nutzer:innen-Profilen zu sammeln. Wenn in Justuno keine ID eingegeben wird, haben die Profile keine Zustimmung, wenn Justuno dieses Profil an Braze pusht. |
| Braze E-Mail-Abonnementgruppen-ID | Kein:e        | Wenn diese ID nicht in Justuno eingegeben wird, sendet Justuno die Daten des Profils an Braze als Nutzer:in ohne zugehörige Abo-Gruppen. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Schritt 3.1: Finden Sie die IDs in Braze

So finden Sie diese IDs im Braze-Dashboard:

1. Gehen Sie zu **Publikum** > **Abonnements**.
2. Notieren Sie sich für jede Abo-Gruppe die ID, die sich in der Spalte ID befindet.

#### Schritt 3.2: Fügen Sie die IDs zur Braze App hinzu

Öffnen Sie in Ihrem Justuno-Workflow die Braze App und geben Sie dann die IDs für die einzelnen Abo-Gruppen ein.

![Die Braze App geöffnet in einem Justuno-Workflow mit der Option, E-Mail- und SMS-Abo-Gruppen-IDs hinzuzufügen.]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### Schritt 4: Konfigurieren Sie Ihre Attribute

Die folgenden Attribute werden automatisch von Justuno mit Braze synchronisiert:

- E-Mail  
- Telefon  
- Vorname  
- Nachname  
- Sprache  
- Geschlecht  
- Land

Um zusätzliche Attribute zu synchronisieren:

1. Wählen Sie in der Braze App innerhalb Ihres Workflows **Andere Eigenschaft synchronisieren**.
    ![Die Braze App wurde in einem Justuno-Workflow geöffnet und zeigt die Option "Eine andere Eigenschaft synchronisieren" an.]({% image_buster /assets/img/justuno/sync-another-property.png %}){: style="max-width:55%;"}
2. Wählen Sie die Attribute von Braze, die Sie synchronisieren möchten.
3. Gleichen Sie die Eigenschaften in Justuno mit ihren Entsprechungen in Braze ab (z. B. soziale Handles, Geburtstag, Einkaufspräferenzen, Antworten auf Umfragen und ähnliches). Denken Sie daran, dass diese Eigenschaften als Daten von 0 Parteien oder als Daten von 1 Partei betrachtet werden. Wenn Sie mehr erfahren möchten, besuchen Sie [Justuno: Datenerfassung für Besucher](https://www.justuno.com/guides/zero-first-party-data/).
4. Wählen Sie im Workflow Builder die Option **Speichern**, **Vorschau** oder **Veröffentlichen** Ihres Workflows.
    ![Das Menü "Veröffentlichen" öffnete sich mit den Optionen zum Speichern, zur Vorschau oder zum Anzeigen des Versionsverlaufs.]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## Was Sie wissen sollten

- Sie müssen die ID der Abo-Gruppe manuell in den Einstellungen der App eingeben.  
- Die folgenden Daten von Braze werden **nicht unterstützt**: Objekt, Objekt-Array.  
- Eine implizite SMS-Einwilligung liegt vor, wenn das SMS-Einwilligungsfeld von Justuno nicht verwendet wird.  
- Die explizite SMS-Zustimmung wird respektiert, wenn das Justuno-Design das Zustimmungsfeld enthält.
