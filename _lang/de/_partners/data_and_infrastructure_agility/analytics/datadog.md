---
nav_title: Datadog
article_title: "Datadog"
description: "Dieser Referenzartikel beschreibt die Partnerschaft mit Braze und Datadog, einem Beobachtungsdienst für Cloud-Anwendungen, der die Überwachung von Servern, Datenbanken, Tools und Diensten über eine SaaS-basierte Datenanalyseplattform ermöglicht."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) ist ein Beobachtungsdienst für Cloud-Anwendungen, der die Überwachung von Servern, Datenbanken, Tools und Diensten über eine SaaS-basierte Datenanalyseplattform ermöglicht.

Die Integration von Braze und Datadog ermöglicht es Kunden, Braze-Daten in Datadog zu sammeln und Alarme zu den von uns gesendeten Daten zu erstellen. Richten Sie zum Beispiel einen Monitor ein und schlagen Sie Alarm, wenn Ihre wöchentliche Newsletter-Kampagne ungewöhnlich viele Nachrichten versendet oder wenn ein Canvas-Schritt, der normalerweise nur einige wenige Nachrichten pro Tag versendet, anfängt, Tausende von Nachrichten zu versenden. 

## Voraussetzungen 

| Anforderung | Beschreibung |
|---|---|
| Datadog-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Datadog-Konto. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Datadog-Schlüssel generieren

In Datadog müssen Sie einen [API-Schlüssel](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys) erstellen. Um einen API-Schlüssel hinzuzufügen, navigieren Sie zu **Organisationseinstellungen** > **API-Schlüssel** > **Neuer Schlüssel**.

### Schritt 2: Schlüssel zu Braze hinzufügen

Navigieren Sie im Braze-Dashboard zu **Partnerintegrationen** > **Technologiepartner** und suchen Sie dann nach **Datadog**. Geben Sie auf der Datadog-Partnerseite den Datadog-API-Schlüssel an. Dadurch wird eine Verbindung hergestellt, die es Braze ermöglicht, Daten an Datadog zu senden.

## Braze Ereignisse

Nachdem die Verbindung integriert wurde, sendet Braze die folgenden Ereignisse an Datadog:

- `braze.messaging.sent` - Die Anzahl der Sendungen

Jedes dieser Ereignisse wird mit Metadaten in Form von Datadog-Tags versehen, die Ihnen Informationen wie z.B.:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (falls verfügbar)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (falls verfügbar)

Diese Ereignisse und Tags können auf der Seite Datadog **Metrics Explorer** überwacht werden. Diese Metriken werden als [Verteilungen](https://docs.datadoghq.com/metrics/distributions/) in DataDog protokolliert. In Anbetracht der Art der Metriken und der Ungenauigkeit der DataDog-Aggregationen und -Rollups versucht Braze nicht, intermittierende Netzwerkfehler oder andere DataDog-API-Fehler, die während der Übertragung auftreten können, zu wiederholen. Das bedeutet, dass diese metrischen Zählungen leicht von den Zählungen abweichen können, die im Braze Dashboard und/oder über Currents angezeigt werden.

![][1]

[1]: {% image_buster /assets/img/datadog.png %}
