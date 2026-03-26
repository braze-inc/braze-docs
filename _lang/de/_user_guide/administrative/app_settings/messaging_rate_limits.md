---
nav_title: Workspace-Messaging-Rate-Limits
article_title: Workspace-Messaging-Rate-Limits
alias: /workspace_messaging_rate_limits/
page_type: reference
description: "Dieser Referenzartikel beschreibt Workspace-Messaging-Rate-Limits und wie sie mit Ihren Nachrichten zusammenwirken."
page_order: 10
---

# Workspace-Messaging-Rate-Limits

> Verwenden Sie Workspace-Messaging-Rate-Limits, um die Zustellrate Ihrer ausgehenden Nachrichten von Ihrer Plattform zu regulieren und sicherzustellen, dass Ihre Nutzer:innen die Nachrichten erhalten, die sie benötigen.

{% alert important %}
Workspace-Messaging-Rate-Limits werden schrittweise eingeführt. Möglicherweise sehen Sie diese Einstellungen noch nicht in Ihrem Dashboard.
{% endalert %}

## So funktioniert es

Workspace-Messaging-Rate-Limits gelten für die Gesamtheit der in Ihrem Workspace gesendeten Nachrichten. Indem Sie ein Rate-Limit auf Workspace-Ebene festlegen und optimieren, können Sie den ausgehenden Datenverkehr Ihrer Braze-Nachrichten besser kontrollieren und potenzielle Lastspitzen vermeiden, die die Server-Performance beeinträchtigen könnten.
{% alert note %}
Beachten Sie, dass Nachrichten, die über API-Messaging-Endpunkte wie `/messages/send` und `/messages/schedule/create` gesendet werden, ebenfalls gezählt werden und von Workspace-Messaging-Rate-Limits betroffen sind.
{% endalert %}
Die Gesamtzahl der pro Minute gesendeten Nachrichten überschreitet nicht die konfigurierten Workspace-Rate-Limits. Es gibt keine bestimmte Reihenfolge, welche Kampagnen in den ersten Minuten im Vergleich zu den späteren Minuten versendet werden.

Nehmen wir zum Beispiel an, Sie haben ein Workspace-Messaging-Rate-Limit von 100.000 Nachrichten pro Minute, und die folgenden Nachrichten werden alle um 12:00 Uhr verarbeitet:

| Kampagne   | Anzahl der Nachrichten | Sendezeit |
|------------|-----------------------|-----------|
| Kampagne 1 | 100.000               | 12:00 Uhr |
| Kampagne 2 | 100.000               | 12:00 Uhr |
| Kampagne 3 | 100.000               | 12:00 Uhr |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Die Nachrichten werden über ein 3-Minuten-Intervall versendet.

Nachrichten werden parallel verarbeitet. Bei der Verarbeitung werden Nachrichten nach dem Prinzip „Wer zuerst kommt, mahlt zuerst" eingeplant, um das Workspace-Messaging-Rate-Limit einzuhalten. Das bedeutet, dass im obigen Beispiel die pro Minute gesendeten Nachrichten eine variierende Mischung aus Kampagne 1, 2 und 3 sind, die zusammen 100.000 ergeben.

![Beispiel, wie Nachrichten für die drei Kampagnen versendet werden.]({% image_buster /assets/img/workspace_messaging_rate_limits2.png %})

Betrachten Sie das nächste Beispiel mit einem Workspace-Messaging-Rate-Limit von 100.000 Nachrichten pro Minute und den folgenden eingerichteten Nachrichten:

| Kampagne   | Anzahl der Nachrichten | Sendezeit |
|------------|-----------------------|-----------|
| Kampagne 1 | 1.000.000             | 9:00 Uhr  |
| Kampagne 2 | 1.000.000             | 9:05 Uhr  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Der erwartete Versandplan und die pro Minute gesendeten Nachrichten sehen wie folgt aus:

- Kampagne 1 würde von 9:00 bis 9:10 Uhr eingeplant, mit 100.000 Nachrichten pro Minute.
- Kampagne 2 würde 5 Minuten nach ihrer ursprünglichen Versandzeit eingeplant, von 9:10 bis 9:20 Uhr, mit 100.000 Nachrichten pro Minute.

![Beispiel, wie Nachrichten pro Minute für die zwei Kampagnen versendet werden.]({% image_buster /assets/img/workspace_messaging_rate_limits1.png %})

{% alert note %}
Nachdem Sie das Workspace-Messaging-Rate-Limit festgelegt haben, können Sie es erhöhen. Allerdings verwendet jede Nachricht, die vor der Erhöhung bereits verarbeitet wurde, das zuvor festgelegte Limit.
{% endalert %}

## Ihr Workspace-Messaging-Rate-Limit festlegen

1. Gehen Sie im Braze-Dashboard zu **Einstellungen** > **Workspace-Einstellungen** > **Workspace-Messaging-Rate-Limits**.
2. Wählen Sie **+ Rate-Limit hinzufügen** und dann einen Messaging-Kanal aus.
3. Geben Sie unter **Messages pro Minute** das Rate-Limit ein.
4. Wählen Sie **Speichern**.

## Wissenswertes

Das Rate-Limit wird auf den Versand angewendet, also auf den Beginn des Sendeversuchs. Wenn es Schwankungen in der Zeit gibt, die für den Abschluss des Versands benötigt wird, kann die Zahl der abgeschlossenen Sendungen in einigen Minuten das Rate-Limit leicht überschreiten. Über die Zeit gleicht sich die Zahl der Sendungen pro Minute auf nicht mehr als das Rate-Limit aus.

Wenn eine Kampagne oder ein Canvas ein eigenes Rate-Limit hat und ein Rate-Limit auf Workspace-Ebene gilt, werden beide angewendet. Wenn eine Kampagne beispielsweise ein Rate-Limit von 500.000 hat, aber aufgrund von Workspace-Rate-Limits zu diesem Zeitpunkt nur 100.000 Nachrichten pro Minute senden kann, greift das Workspace-Rate-Limit.

Braze versucht, die Nachrichtenversendungen gleichmäßig über die Minute zu verteilen, kann dies aber nicht garantieren. Wenn Sie beispielsweise eine Kampagne mit einem Rate-Limit von 500.000 Nachrichten pro Minute haben, versuchen wir, die 500.000 Nachrichten gleichmäßig über die Minute zu verteilen (etwa 8.400 Nachrichten pro Sekunde), aber es kann Abweichungen in der Rate pro Sekunde geben.

Beachten Sie, dass Sie weiterhin individuelle Rate-Limits in Ihren Kampagnen und Canvasen festlegen können. Diese werden unabhängig von Workspace-Messaging-Rate-Limits angewendet.

### Nachrichten, die nicht in den Workspace-Messaging-Rate-Limits enthalten sind

- Nachrichten, die über [Transaktions-E-Mail-Kampagnen]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign) gesendet werden, sind nicht in den Workspace-Messaging-Rate-Limits enthalten. Das bedeutet, sie unterliegen eigenen Rate-Limits und werden nicht auf festgelegte Workspace-Messaging-Rate-Limits angerechnet.
- Nachrichten an [Seed-Gruppen]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab#seed-groups) und [Testsendungen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages) sind nicht in den Workspace-Messaging-Rate-Limits enthalten. Das bedeutet, sie unterliegen keinen Rate-Limits und werden nicht auf festgelegte Workspace-Messaging-Rate-Limits angerechnet.
- Automatische SMS-Antworten sind nicht in den Workspace-Messaging-Rate-Limits enthalten. Das bedeutet, sie unterliegen keinen Rate-Limits und werden nicht auf festgelegte Workspace-Messaging-Rate-Limits angerechnet.