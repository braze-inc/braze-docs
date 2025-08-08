---
nav_title: Antavo
article_title: Antavo Loyalty Cloud
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Antavo, ein Kundenbindungs-Programm der nächsten Generation, das über die Belohnung von Einkäufen hinausgeht."
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Antavo Loyalty Cloud

> [Antavo](https://antavo.com/) ist ein Anbieter von SaaS-Technologien zur Kundenbindung in Unternehmen, der umfassende Kundenbindungs-Programme entwickelt, um die Markenliebe zu fördern und das Kundenverhalten zu ändern.

_Diese Integration wird von Antavo gepflegt._

## Über die Integration

Die Integration von Antavo und Braze erlaubt es Ihnen, Daten aus Treueprogrammen zu nutzen, um personalisierte Kampagnen zu erstellen und so das Kundenerlebnis zu verbessern. Antavo unterstützt die Synchronisierung von Loyalitätsdaten zwischen den beiden Plattformen - es handelt sich dabei um eine einseitige Datensynchronisierung von Antavo zu Braze. Die Integration unterstützt das Feld `external_id` Braze, das Antavo zur Synchronisierung der ID des Treue-Mitglieds verwendet.

## Voraussetzungen

| Anforderung          | Beschreibung                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| Antavo-Konto       | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Antavo-Konto](https://antavo.com/) mit aktivierter Braze-Integration.                                                |
| Braze REST API-Schlüssel   | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen: `users.track`, `events.list`, `events.data_series`, und `events.get`.<br><br>Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.  |
| Braze REST Endpunkt  | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.                |
| Bezeichner der App Braze | Ihr Bezeichner für die App. <br><br>Um diesen Schlüssel im Braze-Dashboard zu finden, gehen Sie zu **Einstellungen** > **API-Schlüssel** und suchen Sie den Abschnitt **Identifizierung**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Braze in Antavo verbinden

Gehen Sie in Antavo zu **Module** > **Braze** und klicken Sie auf **Konfigurieren**. Wenn Sie zum ersten Mal die Konfigurationsseite für die Integration von Braze in Antavo aufrufen, werden Sie über die Schnittstelle aufgefordert, die beiden Systeme miteinander zu verbinden.

Geben Sie die folgenden Zugangsdaten an:

- **Instanz-URL:** Der Braze REST-Endpunkt der Instanz, für die Sie bereitgestellt werden.
- **API Token (Bezeichner):** Der REST API-Schlüssel von Braze, den Antavo beim Senden von Anfragen an Braze verwenden sollte.
- **App Bezeichner:** Der Bezeichner der App von Braze.

Nachdem Sie die Zugangsdaten eingegeben haben, klicken Sie auf **Verbinden**.

![Verbinden Sie den Braze-Bildschirm in Antavo mit der Instanz-URL, dem API-Token und dem Bezeichner der App.]({% image_buster /assets/img/antavo/connect_braze.png %})

### Schritt 2: Konfigurieren Sie die Abbildung von Feldern

Nachdem die Verbindung hergestellt wurde, werden Sie in Antavo automatisch zur Seite **Felder synchronisieren** weitergeleitet, um die Feldsynchronisierung zwischen den beiden Systemen zu konfigurieren.   Sie können diese Seite jederzeit über **Module** > **Braze** erreichen.

So konfigurieren Sie die Abbildung von Feldern in Antavo:

1. Klicken Sie auf **Neues Feld hinzufügen** <i class="fas fa-plus" alt=""></i>.
2. Wählen Sie aus dem Dropdown-Feld das Antavo **Loyalty-Feld** aus, das Sie mit Braze synchronisieren möchten.
3. Geben Sie das **Remote-Feld** ein, das das entsprechende angepasste Attribut in Braze darstellt, in das die Daten eingefügt werden sollen.  

{% alert note %}
Sie finden Ihre Liste der angepassten Attribute in Braze unter **Dateneinstellungen** > **Angepasste Attribute**. Wenn das Feld, das Sie eingeben, nicht in Braze definiert ist, wird bei der ersten Synchronisierung automatisch ein neues Feld erzeugt.
{% endalert %}

{:start="4"}
4\. Um weitere Feldpaarungen hinzuzufügen, wiederholen Sie die Schritte 1-3.
5\. Um ein Feld aus der Liste der synchronisierten Daten zu entfernen, klicken Sie auf <i class="fa-solid fa-rectangle-xmark" title="Löschen"></i> am Ende der Zeile.
6\. Klicken Sie auf **Speichern**.

Wenn sich ein Wert der konfigurierten Felder in Antavo ändert, wird nicht nur die Synchronisierung dieses einzelnen Wertes ausgelöst, sondern jedes Feld, das der Abbildung hinzugefügt wurde, wird in die Anfrage aufgenommen.

![Seite Felder synchronisieren in Antavo.]({% image_buster /assets/img/antavo/data_field_mapping.png %})

{% alert important %}
Um den Verbrauch von Datenpunkten zu minimieren, empfehlen wir, nur die Felder abzubilden, die in Braze bearbeitet werden sollen.
{% endalert %}

#### Unterstützte Datentypen

Die Integration unterstützt alle angepassten [Attribut-Daten von]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) Braze, nämlich: Zahl (Integer, Gleitkommazahl), String, Array, Boolean, Objekt, Objekt-Array und Datum.

![Braze Profil mit verschiedenen angepassten Attributen.]({% image_buster /assets/img/antavo/braze_profile.png %})

Die Datenfelder werden auf der Grundlage der konfigurierten Abbildung der Felder ausgefüllt.

## Trigger

Neben der Konfiguration der Abbildung von Feldern bietet die Integration weitere Möglichkeiten durch Features, die in Antavos [Workflows-Tool](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629) integriert sind. Alle angepassten [Attribut-Datentypen von]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) Braze und die [Datentypen für]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#expected-format) angepasste Event-Eigenschaften können ebenfalls über Workflows synchronisiert werden.

### Gelegentliches Synchronisieren von Treuedaten

Verwenden Sie diese Option, wenn die Daten nicht in Treuefeldern in Antavo gespeichert sind oder wenn die Daten nicht zur Liste der abgebildeten Felder hinzugefügt werden. Die Synchronisierung der angefragten Daten wird ausgelöst, wenn die konfigurierten Workflow-Kriterien erfüllt sind.

Besuchen Sie die Schritt-für-Schritt-Anleitung, um zu erfahren, wie Sie die Synchronisierung von [Treue-Daten in Bezug auf den letzten Kauf](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase) konfigurieren.

### Synchronisierung von Ereignissen des Kundenbindungs-Programms

Verwenden Sie von Antavo synchronisierte Ereignisse, um Treue-Mitglieder in aktionsbasierte Braze Canvase einzutragen. Die Integration kann alle Antavo Events (einschließlich Kauf-Events) synchronisieren, die in Braze als angepasste Events erscheinen.

Besuchen Sie die Schritt-für-Schritt-Anleitung, um zu erfahren, wie Sie die Synchronisierung des [Anmeldeereignisses für das Kundenbindungs-Programm](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) und die Synchronisierung des [Ereignisses für das Sammeln von Vorteilen für das Kundenbindungs-Programm](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) konfigurieren.


