---
nav_title: Lytics
article_title: Lytics
description: "Dieser Referenzartikel behandelt die Integration von Braze und Lytics. Lytics ist eine unternehmensweite Kundendatenplattform für Vermarkter, Analysten und Technologen. Diese Integration ermöglicht es Marken, ihre Lytics-Daten direkt mit Braze zu synchronisieren und abzubilden."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lytics][1] ist die Kundendatenplattform (CDP) der Wahl für die nächste Generation kundenorientierter Unternehmen. Die Lösungen Lytics Decision Engine, Conductor und Cloud Connect bieten Vermarktern und Datenteams die Möglichkeit, Identitätsauflösung, Orchestrierung und Kampagnenoptimierung in Echtzeit und auf datenschutzkonforme Weise durchzuführen.

Die Integration von Braze und Lytics bietet eine einheitliche Sicht auf Ihre Kunden, um eine leistungsstarke Personalisierung zu ermöglichen und optimierte Kampagnen mit der nächstbesten Aktionsorchestrierung und Entscheidungsfindung durchzuführen.

Die Integration ermöglicht es Marken,:

- Exportieren Sie Audiences direkt aus Lytics nach Braze
- Senden Sie Ereignisse aus Braze-Kampagnen oder Canvases in Echtzeit an Lytics, um personalisierte Kampagnen durchzuführen und umfassende Benutzerprofile zu erstellen.

## Anwendungsfälle

Verbinden Sie Braze mit Lytics, um E-Mail-, SMS- und Push-Aktivitäten zu [importieren](#importing-data-from-braze-to-lytics) und damit Lytics-Benutzerprofile anzureichern. Wenn Sie Braze und Lytics zusammen verwenden, können Sie auch die kanalübergreifenden, verhaltensgesteuerten Zielgruppen von Lytics [exportieren](#integration), um hochgradig personalisierte Braze Customer Journeys unter Verwendung von Erstanbieterdaten zu erstellen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Lytics Konto | Um die Vorteile dieser Integration zu nutzen, benötigen Sie ein Lytics-Konto. |
| Lytics Kontonummer | Eine Lytics-Kontonummer ist für die Konfiguration der Webhook-Endpunkt-URL erforderlich. |
| Lytics API Token | Ein Lytics REST API Token mit Data Manager Berechtigungen. <br><br> Diese können Sie im Lytics Dashboard unter **Kontoeinstellungen** > **Zugriffstoken** > **Neues Token erstellen** erstellen. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit der Berechtigung `users.track`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Hartlöt-Instanz | Ihre [Braze-Instanz]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). Wenden Sie sich für diese Informationen an Ihren Braze Onboarding Manager, wenn Sie sich nicht sicher sind. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Dieser Abschnitt beschreibt, wie Sie Lytics-Daten nach Braze exportieren.

### Schritt 1: Eine Autorisierung erstellen

Navigieren Sie in Lytics zum Dashboard **Autorisierung** in der **Datenkonsole** in der Navigationsleiste. Wählen Sie **Neue Berechtigung erstellen** und suchen Sie nach **Braze** und wählen Sie es aus.

Geben Sie in der daraufhin erscheinenden Aufforderung **Autorisierung konfigurieren** eine Bezeichnung und eine Beschreibung ein und geben Sie Ihren REST-API-Schlüssel und Ihre Braze-Instanz ein. Wählen Sie **Fertig stellen**, wenn Sie fertig sind.

![][2]{: style="max-width:80%;"}

### Schritt 2: Einen neuen Auftrag erstellen

Navigieren Sie in Lytics zum Dashboard **Jobs** innerhalb der **Datenkonsole** in der Navigationsleiste. Wählen Sie **Neuen Auftrag erstellen**, suchen Sie nach **Braze** und wählen Sie es aus.  Wählen Sie in der daraufhin angezeigten Aufforderung **Auftragstyp auswählen** die Option **Publikum exportieren**.

![][3]{: style="max-width:80%;"}

Wählen Sie dann eine Berechtigung aus den Optionen **Berechtigung auswählen**.

![][4]{: style="max-width:80%;"}

### Schritt 3: Konfigurieren Sie den Auftrag

Geben Sie in der Eingabeaufforderung **Auftrag konfigurieren** eine Bezeichnung und eine optionale Beschreibung ein. Als Nächstes wählen Sie aus dem Eingabefeld **für die externe Benutzer-ID von Braze** das Feld in Lytics aus, das die externe Benutzer-ID von Braze enthält (`braze_id`). Der nächste Schritt ist der wichtigste: Wählen Sie die Audiences aus, die Sie nach Braze exportieren möchten.

![][5]{: style="max-width:80%;"}

Wählen Sie schließlich die bevorzugte Option für das Kontrollkästchen **Bestehende Benutzer**. Wenn Sie dieses Kästchen aktiviert lassen, werden Benutzer hinzugefügt, die bereits in der ausgewählten Lytics Zielgruppe vorhanden sind. Wenn diese Option nicht aktiviert ist, werden die Benutzer nur dann nach Braze exportiert, wenn sie die Zielgruppe betreten oder verlassen, nachdem der Workflow begonnen hat.

{% alert note %}
Wenn Sie dieses Kontrollkästchen aktivieren, werden alle bestehenden Benutzer der ausgewählten Zielgruppe in Braze aufgenommen. Dies führt dazu, dass für die erste Synchronisierung ein Datenpunkt pro Nutzer und Zielgruppe anfällt.
{% endalert %}

Klicken Sie auf **Fertig stellen**, wenn Sie fertig sind, um den Export zu starten und zu speichern.

![][6]{: style="max-width:80%;"}

Nachdem der Exportauftrag konfiguriert ist, sendet Lytics die ausgewählten Zielgruppen über die native Integration an Braze. Nachfolgend sehen Sie ein Beispiel für eine Audience, das die JSON-Struktur der an Braze gesendeten Audience zeigt.

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

Für alle `external_id`, die im Audience-Export enthalten sind und noch nicht in Braze existieren, wird ein neuer Benutzer in Braze erstellt. 

## Importieren von Daten aus Braze in Lytics

Sie können Audience-Daten mit den folgenden Methoden von Braze nach Lytics importieren:

- [Webhooks verwenden](#using-webhooks)
- [Aus einer CSV-Datei](#from-a-csv-file)

### Webhooks verwenden

#### Schritt 1: Ein Lytics API-Token erstellen

Navigieren Sie zum Lytics-Kontomenü in der linken unteren Ecke, indem Sie Ihren Kontonamen auswählen, und wählen Sie im Dropdown-Menü **Zugriffstoken**. Als nächstes wählen Sie **API Token erstellen**

![][7]{: style="max-width:80%;"}

Geben Sie einen Namen, eine optionale Beschreibung und eine Gültigkeitsdauer des Tokens ein. Als nächstes schalten Sie den **Datenverwaltungsbereich** für API-Berechtigungen um und klicken auf **Token generieren**. Kopieren Sie den Token und bewahren Sie ihn an einem sicheren Ort auf.

![][8]{: style="max-width:80%;"}

#### Schritt 2: Konfigurieren Sie die Lytics Webhook-URL

Die Lytics Webhook-URL wird von Braze verwendet, um eine Nachricht von Braze an die Lytics-API zu senden. Diese Nachricht kann verwendet werden, um Ihre Kampagnen in Lytics zu personalisieren oder um Ihr Lytics-Kundenprofil zu bereichern. Die folgenden zwei Parameter müssen in der Lytics Webhook-URL hinzugefügt werden:

- Lytics Kontonummer
- Lytics API-Token

Konfigurieren Sie Ihre Webhook-URL wie folgt:

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

Ersetzen Sie `<ACCOUNT-NUMBER>` durch Ihre Kontonummer und `<LYTICS-API-TOKEN>` durch Ihr Lytics API-Token.

#### Schritt 3: Einen Webhook auf Braze erstellen 

Erstellen Sie in Braze eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). Fügen Sie die Lytics Webhook-URL in das Feld **Webhook-URL** ein.

Nachdem Sie den Anfragetyp (HTTP `POST` Methode) definiert und den Rest der Webhook-Details konfiguriert haben, ist Ihr Webhook bereit zum Testen und Bereitstellen. Hier sehen Sie ein Beispiel für den Text der POST-Anfrage nach der Konfiguration des Webhooks in Braze:

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

Dieser Abschnitt beschreibt, wie Sie Braze-Benutzerdaten aus einem Segment in Lytics importieren.

#### Schritt 1: Eine Autorisierung erstellen

Navigieren Sie in Lytics zum Dashboard **Autorisierung** in der **Datenkonsole** in der Navigationsleiste. Wählen Sie **Neue Berechtigung erstellen** und suchen Sie nach **benutzerdefinierten Integrationen** und wählen Sie diese aus.

Wählen Sie die bevorzugte Art der SFTP-Autorisierung auf der Grundlage Ihrer Geschäfts- und Sicherheitsanforderungen. Die folgenden Autorisierungstypen werden für den Import von Dateien in Lytics über SFTP unterstützt:

- Client SFTP Server Autorisierung
- Client-SFTP-Server-Autorisierung mit privatem PGP-Schlüssel
- Lytics Managed SFTP-Server-Autorisierung

SFTP-Autorisierungen für öffentliche Schlüssel gelten nur für den SFTP-Export.

![][9]{: style="max-width:80%;"}

Geben Sie in der daraufhin erscheinenden Eingabeaufforderung **Autorisierung konfigurieren** eine Bezeichnung und eine Beschreibung ein und vervollständigen Sie die restlichen Konfigurationsanforderungen. Klicken Sie auf **Fertig stellen**, wenn Sie fertig sind.

#### Schritt 2: Exportieren Sie Ihre Segmentdaten nach CSV

Navigieren Sie in Braze zu **Zielgruppe** > **Segmente**. Suchen Sie das Segment, das Sie exportieren möchten, und wählen Sie dann <i class="fas fa-gear" aria-label="Einstellungen"></i> und dann **CSV-Benutzerdaten exportieren**. Sie können bis zu 500.000 Benutzer in ein Segment exportieren. Weitere Informationen finden Sie unter [Exportieren von Segmentdaten nach CSV]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv).

#### Schritt 3: Einen CSV-Importauftrag konfigurieren

Navigieren Sie in Lytics zum Dashboard **Jobs** innerhalb der **Datenkonsole** in der Navigationsleiste. Wählen Sie **Neuen Auftrag erstellen**, suchen Sie nach **benutzerdefinierten Integrationen** und wählen Sie diese aus.

Wählen Sie dann den Auftragstyp aus. Um Braze CSV-Dateien in Lytics zu importieren, wählen Sie als Auftragstyp **CSV importieren**.

![][10]{: style="max-width:80%;"}

Geben Sie schließlich eine Bezeichnung und eine optionale Beschreibung für den Auftrag ein und konfigurieren Sie alle anderen erforderlichen Details. Klicken Sie auf **Fertig stellen**, um den Auftrag zu starten und zu speichern.

[1]: https://www.lytics.com/
[2]: {% image_buster /assets/img/lytics/braze_authorization.png %}
[3]: {% image_buster /assets/img/lytics/braze_jobtype.png %}
[4]: {% image_buster /assets/img/lytics/braze_jobauth.png %}
[5]: {% image_buster /assets/img/lytics/braze_job.png %}
[6]: {% image_buster /assets/img/lytics/braze_backfill.png %}
[7]: {% image_buster /assets/img/lytics/create_token.png %}
[8]: {% image_buster /assets/img/lytics/data_manager.png %}
[9]: {% image_buster /assets/img/lytics/authorization_method.png %}
[10]: {% image_buster /assets/img/lytics/configure_job.png %}





