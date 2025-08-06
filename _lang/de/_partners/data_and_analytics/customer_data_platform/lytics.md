---
nav_title: Lytics
article_title: Lytics
description: "Dieser referenzierte Artikel behandelt die Integration von Braze und Lytics. Lytics ist eine unternehmensweite Kundendaten-Plattform für Marketer, Analysten und Technologen. Diese Integration erlaubt es Marken, ihre Lytics Daten direkt mit Braze zu synchronisieren und abzubilden."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lytics](https://www.lytics.com/) ist die Customer Data Platform (CDP) der Wahl für die nächste Generation von kundenorientierten Unternehmen. Die Lösungen Lytics Decision Engine, Conductor und Cloud Connect bieten Marketern und Datenteams die Opportunity, Identitätsauflösung, Orchestrierung und Kampagnen-Optimierung in Echtzeit und unter Wahrung des Datenschutzes durchzuführen.

_Diese Integration wird von Lytics gepflegt._

## Über die Integration

Die Integration von Braze und Lytics bietet eine einheitliche Sicht auf Ihre Kund:innen, um eine leistungsstarke Personalisierung zu ermöglichen und optimierte Kampagnen mit der nächstbesten Orchestrierung und Entscheidungsfindung zu fahren.

Die Integration lässt Marken zu:

- Exportieren Sie Zielgruppen direkt aus Lytics nach Braze
- Senden Sie Ereignisse aus Braze-Kampagnen oder Canvase in Realtime an Lytics, um personalisierte Kampagnen durchzuführen und umfassende Nutzer:innen-Profile zu erstellen.

## Anwendungsfälle

Verbinden Sie Braze mit Lytics, um E-Mail-, SMS- und Push-Aktivitäten zu [importieren](#importing-data-from-braze-to-lytics), um Lytics Nutzerprofile anzureichern. Wenn Sie Braze und Lytics zusammen verwenden, können Sie auch die kanalübergreifenden, verhaltensgestützten Zielgruppen von Lytics [exportieren](#integration), um anhand von First-Party-Daten hochgradig personalisierte Customer Journeys von Braze zu erstellen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Lytics Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein Lytics-Konto. |
| Lytics Kontonummer | Für die Konfiguration der Webhook-Endpunkt-URL ist eine Lytics-Kontonummer erforderlich. |
| Lytics API-Token | Ein Lytics REST API Token mit Data Manager:in Berechtigungen. <br><br> Dieses kann im Dashboard von Lytics unter **Kontoeinstellungen** > **Zugriffstoken** > **Neues Token erstellen** erstellt werden. |
| Braze REST API-Schlüssel | Ein REST API-Schlüssel von Braze mit der Berechtigung `users.track`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze-Instanz | Ihre [Braze-Instanz]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). Wenden Sie sich für diese Informationen an Ihren Braze Manager:in, wenn Sie sich nicht sicher sind. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

In diesem Abschnitt wird beschrieben, wie Sie Lytics-Daten nach Braze exportieren.

### Schritt 1: Eine Autorisierung erstellen

Navigieren Sie in Lytics zum Dashboard **Autorisierung** innerhalb der **Datenkonsole** in der Navigationsleiste. Wählen Sie **Neue Berechtigung erstellen**, suchen Sie nach **Braze** und wählen Sie es aus.

Geben Sie in der daraufhin erscheinenden Aufforderung **Autorisierung konfigurieren** eine Bezeichnung und eine Beschreibung ein und geben Sie Ihren REST API-Schlüssel und Ihre Braze-Instanz ein. Wählen Sie **Fertigstellen**, wenn Sie fertig sind.

![]({% image_buster /assets/img/lytics/braze_authorization.png %}){: style="max-width:80%;"}

### Schritt 2: Einen neuen Auftrag erstellen

Navigieren Sie in Lytics zum Dashboard **Jobs** innerhalb der **Datenkonsole** in der Navigationsleiste. Wählen Sie **Neuen Auftrag erstellen**, suchen Sie nach **Braze** und wählen Sie es aus.  In der daraufhin angezeigten Aufforderung **Auftragstyp auswählen** wählen Sie **Zielgruppe exportieren**.

![]({% image_buster /assets/img/lytics/braze_jobtype.png %}){: style="max-width:80%;"}

Wählen Sie dann eine Berechtigung aus den Optionen **Berechtigung auswählen** aus.

![]({% image_buster /assets/img/lytics/braze_jobauth.png %}){: style="max-width:80%;"}

### Schritt 3: Konfigurieren Sie den Auftrag

Geben Sie in der Eingabeaufforderung **Auftrag konfigurieren** eine Bezeichnung und optional eine Beschreibung ein. Als Nächstes wählen Sie aus dem **Eingabefeld für die externe ID von Braze** das Feld in Lytics aus, das die externe ID von Braze enthält (`braze_id`). Der nächste Schritt ist der wichtigste: Wählen Sie die Zielgruppen aus, die Sie nach Braze exportieren möchten.

![]({% image_buster /assets/img/lytics/braze_job.png %}){: style="max-width:80%;"}

Wählen Sie schließlich die gewünschte Option für das Kontrollkästchen **Bestehende Nutzer:innen**. Wenn Sie dieses Kästchen aktiviert lassen, werden Nutzer:innen hinzugefügt, die bereits in der ausgewählten Lytics Zielgruppe vorhanden sind. Wenn diese Option nicht markiert ist, werden Nutzer:innen nur dann nach Braze exportiert, wenn sie die Zielgruppe nach Beginn des Workflows betreten oder verlassen.

{% alert note %}
Wenn Sie dieses Kästchen markieren, werden alle vorhandenen Nutzer:innen der ausgewählten Zielgruppe in Braze gepusht. Dies führt dazu, dass bei der ersten Synchronisierung ein Datenpunkt pro Nutzer:innen und Zielgruppen anfällt.
{% endalert %}

Klicken Sie abschließend auf **Fertig stellen**, um den Export zu starten und zu speichern.

![]({% image_buster /assets/img/lytics/braze_backfill.png %}){: style="max-width:80%;"}

Nachdem der Exportauftrag konfiguriert wurde, sendet Lytics die ausgewählten Zielgruppen über die native Integration an Braze. Nachfolgend sehen Sie eine Beispielzielgruppe, die die JSON-Struktur der an Braze gesendeten Zielgruppe zeigt.

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

Für jede `external_id`, die in dem Zielgruppe-Export enthalten ist und noch nicht in Braze existiert, wird ein neuer Nutzer:innen in Braze erstellt. 

## Importieren von Daten aus Braze in Lytics

Sie können Zielgruppendaten aus Braze mit den folgenden Methoden in Lytics importieren:

- [Webhooks verwenden](#using-webhooks)
- [Aus einer CSV-Datei](#from-a-csv-file)

### Webhooks verwenden

#### Schritt 1: Erstellen Sie ein Lytics API Token

Navigieren Sie zum Lytics-Kontomenü in der linken unteren Ecke, indem Sie Ihren Kontonamen auswählen, und wählen Sie im Dropdown-Menü **Zugriffstoken** aus. Als nächstes wählen Sie **API Token erstellen**

![]({% image_buster /assets/img/lytics/create_token.png %}){: style="max-width:80%;"}

Geben Sie einen Namen, eine optionale Beschreibung und eine Gültigkeitsdauer für den Token ein. Schalten Sie als nächstes den Bereich **Manager:** in für API-Berechtigungen um und klicken Sie auf **Token generieren**. Kopieren Sie den Token und bewahren Sie ihn an einem sicheren Ort auf.

![]({% image_buster /assets/img/lytics/data_manager.png %}){: style="max-width:80%;"}

#### Schritt 2: Konfigurieren Sie die Webhook-URL von Lytics

Die Lytics-Webhook-URL wird von Braze verwendet, um eine Nachricht von Braze an die Lytics-API zu senden. Diese Nachricht kann zur Personalisierung Ihrer Kampagnen in Lytics oder zur Anreicherung Ihres Lytics Kundenprofils verwendet werden. Die folgenden zwei Parameter müssen in der Webhook-URL von Lytics hinzugefügt werden:

- Lytics Kontonummer
- Lytics API-Token

Konfigurieren Sie die URL Ihres Webhooks wie folgt:

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

Ersetzen Sie `<ACCOUNT-NUMBER>` durch Ihre Kontonummer und `<LYTICS-API-TOKEN>` durch Ihr Lytics API-Token.

#### Schritt 3: Erstellen Sie einen Webhook auf Braze 

Erstellen Sie in Braze eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). Fügen Sie die Webhook-URL von Lytics in das Feld **Webhook-URL** ein.

Nachdem Sie den Typ der Anfrage (HTTP `POST` Methode) definiert und die restlichen Webhook-Details konfiguriert haben, ist Ihr Webhook bereit zum Testen und Bereitstellen. Hier sehen Sie einen Beispieltext für die POST-Anfrage nach der Konfiguration des Webhooks in Braze:

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "John",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@email.com",
  "braze_id": "xxxxxx" 
}
```

### Aus einer CSV-Datei

Dieser Abschnitt beschreibt, wie Sie Nutzerdaten von Braze aus einem Segment in Lytics importieren.

#### Schritt 1: Eine Autorisierung erstellen

Navigieren Sie in Lytics zum Dashboard **Autorisierung** innerhalb der **Datenkonsole** in der Navigationsleiste. Wählen Sie **Neue Autorisierung erstellen** und suchen Sie nach **angepassten Integrationen** und wählen Sie diese aus.

Wählen Sie die bevorzugte Art der SFTP-Autorisierung auf der Grundlage Ihrer Geschäfts- und Sicherheitsanforderungen aus. Die folgenden Autorisierungstypen werden für den Import von Dateien in Lytics über SFTP unterstützt:

- Client SFTP Server Autorisierung
- Client SFTP Server Autorisierung mit PGP Private Key
- Lytics Managed SFTP Server Autorisierung

Public Key SFTP-Autorisierungen gelten nur für den SFTP-Export.

![]({% image_buster /assets/img/lytics/authorization_method.png %}){: style="max-width:80%;"}

Geben Sie in der daraufhin erscheinenden Eingabeaufforderung **Autorisierung konfigurieren** eine Bezeichnung und eine Beschreibung ein und vervollständigen Sie die restlichen Konfigurationsanforderungen. Klicken Sie auf **Fertig stellen**, wenn Sie fertig sind.

#### Schritt 2: Exportieren Sie Ihre Daten zur Segmentierung nach CSV

Navigieren Sie in Braze zu **Zielgruppe** > **Segmente**. Suchen Sie das Segment, das Sie exportieren möchten, und wählen Sie dann <i class="fas fa-gear" aria-label="Einstellungen"></i> und dann **CSV Benutzerdaten exportieren**. Sie können bis zu 500.000 Nutzer:innen in ein Segment exportieren. Weitere Informationen finden Sie unter [Exportieren von Segmentdaten in CSV]({{site.baseurl}}/user_guide/data/export_braze_data/segment_data_to_csv/).

#### Schritt 3: Einen CSV-Importauftrag konfigurieren

Navigieren Sie in Lytics zum Dashboard **Jobs** innerhalb der **Datenkonsole** in der Navigationsleiste. Wählen Sie **Neuer Auftrag erstellen** und suchen Sie nach und wählen Sie **Angepasste Integrationen**.

Wählen Sie dann den Auftragstyp aus. Um Braze CSV-Dateien in Lytics zu importieren, wählen Sie als Auftragstyp **CSV-Import** aus.

![]({% image_buster /assets/img/lytics/configure_job.png %}){: style="max-width:80%;"}

Geben Sie schließlich eine Bezeichnung und eine optionale Beschreibung für den Auftrag ein und konfigurieren Sie alle anderen erforderlichen Details. Klicken Sie auf **Fertig stellen**, um den Auftrag zu starten und zu speichern.







