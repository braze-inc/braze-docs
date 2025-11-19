---
nav_title: Daten der Kampagne exportieren
article_title: Daten der Kampagne exportieren
page_order: 0
page_type: reference
description: "In diesem Referenzartikel erfahren Sie, wie Sie Kampagnenergebnisse aus Singlechannel-, Multichannel- oder Multivarianten-Kampagnen exportieren können. In diesem Artikel erfahren Sie auch, wie Sie Nutzerdaten von den Empfänger:innen exportieren können."
tool: 
  - Campaigns
  - Reports
  
---

# Daten der Kampagne exportieren

> Wählen Sie auf der Seite **Kampagnen** des Dashboards die gewünschte Kampagne aus und scrollen Sie nach unten zu den historischen Performance-Diagrammen, die Sie exportieren können.<br><br>Auf dieser Seite erfahren Sie, wie Sie die Ergebnisdaten von Singlechannel-, Multichannel- und Multivarianten-Kampagnen sowie die Nutzerdaten der Empfänger:innen exportieren können.

## Kampagnen mit mehreren Kanälen

Bei Multichannel-Kampagnen hängen die Daten, die exportiert werden können, davon ab, welche Messaging-Kanäle Sie verwendet haben. Hier finden Sie eine Liste aller Daten, die aus einer Kampagne exportiert werden können, die iOS Push-, Android Push-, E-Mail- und In-App-Nachrichten verwendet hat:

- Gesendete Nachrichten nach Datum
    - Gesendete Nachrichten insgesamt
    - Über die Kanäle der Kampagne gesendete Nachrichten (kann Push-, E-Mail- und In-App-Nachrichten umfassen)
- E-Mail Nachrichten Engagement nach Datum
    - Anzahl der zugestellten E-Mails
    - Anzahl der gesendeten E-Mails
    - Anzahl der geöffneten E-Mails
    - Anzahl E-Mail-Klicks
    - Anzahl E-Mail Bounces
    - Anzahl der als Spam gemeldeten E-Mails
- In-App Nachrichten Engagement nach Datum
    - Anzahl der gesendeten In-App-Nachrichten
    - In-App-Nachricht-Impressionen
    - Anzahl der Klicks auf In-App-Nachrichten
- iOS Push Engagement nach Datum
    - Anzahl der gesendeten iOS Push-Benachrichtigungen
    - Öffnungen gesamt
    - Direkte Öffnungen
    - Absprünge
- Android Push Engagement nach Datum
    - Anzahl der gesendeten Push-Benachrichtigungen für Android
    - Öffnungen gesamt
    - Direkte Öffnungen
    - Absprünge

## Multivariate Kampagnen

Für Multivariaten-Kampagnen, die nur einen Messaging-Kanal verwenden, können Sie Daten exportieren, die zeigen, wie jede Variante im Laufe der Zeit in den Analysen des jeweiligen Messaging-Kanals abgeschnitten hat. Sie können diese Daten nach Statistik oder nach Variante der Nachricht gruppiert anzeigen.

Die Ergebnisse der Push-Kampagnen enthalten Diagramme für die folgenden Analysen:

- Gesendete Nachrichten nach Datum für jede Variante
- Konversionen nach Datum für jede Variante
- Eindeutige Empfänger:innen nach Datum für jede Variante
- Öffnet nach Datum für jede Variante
- Direkte Öffnungen nach Datum für jede Variante
- Absprünge nach Datum für jede Variante

Die Ergebnisse von E-Mail Kampagnen enthalten Diagramme für die folgenden Analytics:

- Anzahl zugestellt nach Datum für jede Variante
- Anzahl der Sendungen nach Datum für jede Variante
- Öffnet nach Datum für jede Variante
- Klicks nach Datum für jede Variante
- Absprünge nach Datum für jede Variante
- Spam-Berichte nach Datum für jede Variante

Die Ergebnisse der In-App-Nachricht-Kampagnen enthalten Diagramme für die folgenden Analysen:

- Gesendet nach Datum für jede Variante
- Impressionen nach Datum für jede Variante
- Klicks nach Datum für jede Variante

## Empfänger:innen der Kampagne

Sie können Nutzerdaten für alle Empfänger:innen einer Kampagne als CSV-Datei exportieren. Wählen Sie dazu den Button **Nutzerdaten** im Bereich **Kampagnendetails** aus.

{% alert note %}
Sie können den Button **Nutzerdaten** nicht sehen? Um Nutzerdaten zu exportieren, benötigen Sie die Berechtigung [Berechtigungen]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#limited-and-team-role-permissions) **Nutzerdaten exportieren** für diesen Workspace.
{% endalert %}

\![Nutzerdaten-Dropdown auf der Seite Kampagnendetails]({% image_buster /assets/img/campaign_export_example.png %})

Die CSV-Ausgabe enthält Nutzerprofil-Daten für jeden Empfänger:innen der Kampagne. Braze erstellt den Bericht im Hintergrund und mailt ihn an die Nutzer:innen, die gerade angemeldet sind.

Wenn Sie Ihre [Amazon S3-Anmeldedaten]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) mit Braze verknüpft haben, wird die CSV-Datei auch in Ihr S3-Bucket hochgeladen. Andernfalls wird der Ihnen gemailte Link in einigen Stunden ablaufen.

Die exportierte Datei enthält dieselben Felder mit Nutzerdaten, die auch enthalten sind, wenn Sie [Nutzerdaten für ein Segment exportieren]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_app_usage_data/#exporting-app-usage-data). Wenn Sie zusätzlich zu diesen Datenfeldern die Option „Alle Empfänger:innen exportieren“ wählen, enthält die exportierte Datei auch die folgenden Daten für jede:n Nutzer:in:

- Name der erhaltenen Kampagnenvariante
- API ID der empfangenen Kampagnen-Variante
- Ob Nutzer:in der Kontrollgruppe ist

{% alert tip %}
Hilfe bei CSV- und API-Exporten finden Sie unter [Fehlerbehebung bei Exporten]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

