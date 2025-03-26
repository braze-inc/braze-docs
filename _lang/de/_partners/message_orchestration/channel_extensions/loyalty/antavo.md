---
nav_title: Antavo
article_title: Antavo Loyalty Cloud
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Antavo, ein Treueprogramm der nächsten Generation, das über die Belohnung von Einkäufen hinausgeht."
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Antavo Loyalty Cloud

> [Antavo](https://antavo.com/) ist ein Anbieter von SaaS-Technologien zur Kundenbindung für Unternehmen, der umfassende Kundenbindungsprogramme entwickelt, um die Markenliebe zu fördern und das Kundenverhalten zu ändern.

Die Integration von Antavo und Braze ermöglicht es Ihnen, Daten aus Treueprogrammen zu nutzen, um personalisierte Kampagnen zu erstellen und so das Kundenerlebnis zu verbessern. Antavo unterstützt die Synchronisierung von Loyalitätsdaten zwischen den beiden Plattformen - dies ist eine einseitige Datensynchronisierung von Antavo zu Braze. Die Integration unterstützt das `external_id` Braze-Feld, das Feld, mit dem Antavo die ID des Treue-Mitglieds synchronisiert.

## Voraussetzungen

| ANFORDERUNG          | BESCHREIBUNG                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| Antavo-Konto       | Sie benötigen ein [Antavo-Konto](https://antavo.com/) mit aktivierter Braze-Integration, um die Vorteile dieser Partnerschaft zu nutzen.                                                |
| Braze REST API Schlüssel   | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen.<br><br>Um einen neuen API-Schlüssel im Braze Dashboard zu erstellen, gehen Sie zu **Einstellungen** > **API-Schlüssel** und klicken Sie auf **Neuen API-Schlüssel erstellen**.  |
| Braze REST Endpunkt  | [Ihre REST-Endpunkt-URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.                |
| Braze App Kennung | Der Schlüssel zu Ihrer App-Kennung. <br><br>Um diesen Schlüssel im Braze Dashboard zu finden, gehen Sie zu **Einstellungen** > **API-Schlüssel** und suchen Sie den Abschnitt **Identifizierung**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Verbinden Sie Braze in Antavo

Gehen Sie in Antavo zu **Module** > **Braze** und klicken Sie auf **Konfigurieren**. Wenn Sie zum ersten Mal die Konfigurationsseite für die Braze-Integration in Antavo aufrufen, werden Sie aufgefordert, die beiden Systeme zu verbinden.

Legen Sie die folgenden Nachweise vor:

- **Instanz-URL:** Der Braze REST-Endpunkt der Instanz, für die Sie provisioniert werden.
- **API Token (Bezeichner):** Der REST-API-Schlüssel von Braze, den Antavo beim Senden von Anfragen an Braze verwenden soll.
- **App-Identifikator:** Die Braze App-Kennung.

Nachdem Sie die Anmeldedaten eingegeben haben, klicken Sie auf **Verbinden**.

![Verbinden Sie den Braze-Bildschirm in Antavo mit der Instanz-URL, dem API-Token und dem App-Identifikator.][1]

### Schritt 2: Konfigurieren Sie die Feldzuordnung

Nachdem die Verbindung hergestellt wurde, werden Sie in Antavo automatisch zur Seite **Felder synchronisieren** weitergeleitet, um die Feldsynchronisierung zwischen den beiden Systemen zu konfigurieren.   Sie können diese Seite jederzeit über **Module** > **Braze** erreichen.

So konfigurieren Sie die Feldzuordnung in Antavo:

1. Klicken Sie auf **Neues Feld hinzufügen** <i class="fas fa-plus" alt=""></i>.
2. Verwenden Sie das Dropdown-Feld, um das Antavo **Loyalty-Feld** auszuwählen, das Sie mit Braze synchronisieren möchten.
3. Geben Sie das **Remote-Feld** ein, das das entsprechende benutzerdefinierte Attribut in Braze darstellt, in das die Daten eingefügt werden sollen.  

{% alert note %}
Sie finden Ihre Liste der benutzerdefinierten Attribute in Braze unter **Dateneinstellungen** > **Benutzerdefinierte Attribute**. Wenn das Feld, das Sie eingeben, nicht in Braze definiert ist, wird bei der ersten Synchronisierung automatisch ein neues Feld erzeugt.
{% endalert %}

{:start="4"}
4\. Um weitere Feldpaarungen hinzuzufügen, wiederholen Sie die Schritte 1-3.
5\. Um ein Feld aus der Liste der synchronisierten Daten zu entfernen, klicken Sie auf <i class="fa-solid fa-rectangle-xmark" title="Löschen"></i> am Ende der Zeile.
6\. Klicken Sie auf **Speichern**.

Wenn sich ein Wert der konfigurierten Felder in Antavo ändert, wird nicht nur die Synchronisierung dieses einzelnen Wertes ausgelöst, sondern jedes Feld, das der Feldzuordnung hinzugefügt wurde, wird in die Anfrage aufgenommen.

![Seite Felder synchronisieren in Antavo.][2]

{% alert important %}
Um den Verbrauch von Datenpunkten zu minimieren, empfehlen wir, nur die Felder zuzuordnen, die in Braze bearbeitet werden sollen.
{% endalert %}

#### Unterstützte Datentypen

Die Integration unterstützt alle benutzerdefinierten [Attributdatentypen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) von Braze, nämlich: Zahl (Integer, Float), String, Array, Boolean, Objekt, Array von Objekten und Datum.

![Lötprofil mit verschiedenen benutzerdefinierten Attributen.][3]

Die Datenfelder werden auf der Grundlage der konfigurierten Feldzuordnung ausgefüllt.

## Trigger

Zusätzlich zur Konfiguration der Feldzuordnung bietet die Integration weitere Möglichkeiten durch Funktionen, die in Antavos [Workflows-Tool](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629) integriert sind. Alle benutzerdefinierten [Attributdatentypen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) und benutzerdefinierten [Ereigniseigenschaftstypen]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#expected-format) von Braze können auch über Workflows synchronisiert werden.

### Gelegentliches Synchronisieren von Treuedaten

Verwenden Sie diese Option, wenn die Daten nicht in Treuefeldern in Antavo gespeichert sind oder wenn die Daten nicht in die Liste der zugeordneten Felder aufgenommen werden. Die Synchronisierung der angeforderten Daten wird ausgelöst, wenn die konfigurierten Workflow-Kriterien erfüllt sind.

Besuchen Sie die Schritt-für-Schritt-Anleitung, um zu erfahren, wie Sie die Synchronisierung von [Treuedaten in Bezug auf den letzten Kauf](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase) konfigurieren.

### Synchronisierung von Treueprogramm-Ereignissen

Verwenden Sie von Antavo synchronisierte Ereignisse, um Treue-Mitglieder in aktionsbasierte Braze Canvases einzutragen. Die Integration kann alle Antavo-Ereignisse (einschließlich Kaufereignisse) synchronisieren, die in Braze als benutzerdefinierte Ereignisse erscheinen.

Lesen Sie die Schritt-für-Schritt-Anleitung, um zu erfahren, wie Sie die Synchronisierung des [Anmeldeereignisses für das Treueprogramm](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) und die Synchronisierung des [Ereignisses für das Sammeln von Vorteilen für das Treueprogramm](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) konfigurieren.

[1]: {% image_buster /assets/img/antavo/connect_braze.png %}
[2]: {% image_buster /assets/img/antavo/data_field_mapping.png %}
[3]: {% image_buster /assets/img/antavo/braze_profile.png %}