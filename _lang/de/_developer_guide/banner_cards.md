---
page_order: 2.2
nav_title: Banner-Cards
article_title: Banner-Cards
description: "Auf dieser Landing Page finden Sie alles über Banner Cards, einschließlich Artikeln über die Erstellung von Banner Cards und Anwendungsfälle."
channel:
- Banners
---

# Banner-Cards

> Mit Banner Cards können Sie personalisierte Nachrichten für Ihre Nutzer:innen erstellen und gleichzeitig die Reichweite Ihrer anderen Kanäle, wie E-Mail oder Push-Benachrichtigungen, erhöhen. Ähnlich wie bei [Content-Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about) können Sie die Karten direkt in Ihre App oder Website einbetten und so ein natürliches Engagement für die Nutzer:innen schaffen.

{% alert important %}
Banner-Cards befinden sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Braze Account Manager, wenn Sie an der Early-Access-Phase teilnehmen möchten.
{% endalert %}

## Anwendungsfälle

Da Banner Cards nie ablaufen und jedes Mal, wenn ein Nutzer:innen eine neue Sitzung beginnt, automatisch personalisiert werden, eignen sie sich hervorragend für:

- Hervorhebung von Featured Content
- Benachrichtigung der Nutzer:innen über bevorstehende Ereignisse
- Austausch von Updates zu Kundenbindungs-Programmen

## Über Banner Cards

### Ablauf der Karte

Standardmäßig laufen Banner Cards nicht ab. Sie können jedoch bei Bedarf ein Enddatum festlegen.

### Platzierungs-IDs {#placement-ids}

Die Platzierung von Bannerkarten ist für jeden Workspace eindeutig und kann für 10 Kampagnen in einem einzigen Workspace verwendet werden. Darüber hinaus muss jeder Workspace mit einer eindeutigen ID versehen werden. Sie erstellen Platzierungen und weisen ihnen IDs zu, wenn Sie [eine Kampagne für Banner Cards erstellen]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/) oder [Banner Cards in Ihre App einbetten]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/).

{% alert important %}
Vermeiden Sie die Änderung von Platzierungs-IDs nach dem Start einer Banner Card Kampagne.
{% endalert %}

### Priorität der Karte {#card-priority}

Wenn mehrere Kampagnen auf dieselbe ID referenzieren, werden die Karten in der Reihenfolge ihrer Priorität angezeigt. Standardmäßig sind neu erstellte Bannerkarten auf mittel eingestellt, aber Sie können [die Priorität manuell]({{site.baseurl}}/developer_guide/banner_cards/creating_banner_cards/#set-card-priority) auf hoch, mittel oder niedrig setzen. Wenn mehrere Karten die gleiche Prioritätsstufe haben, wird die neueste Karte zuerst angezeigt.

### Metriken

Dies sind die wichtigsten Metriken der Banner Card. Eine vollständige Liste der Metriken, Definitionen und Berechnungen finden Sie im [Bericht Metriken Glossar]({{site.baseurl}}/user_guide/data/report_metrics/).

| Metrisch | Definition |
| --- | --- |
| [Impressionen gesamt]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-impressions) | Die Anzahl, wie oft die Nachricht geladen wurde und auf dem Bildschirm eines Nutzers:innen erscheint, unabhängig von der vorherigen Interaktion (wird einem Nutzer:innen z.B. eine Nachricht zweimal angezeigt, so wird sie zweimal gezählt). |
| [Eindeutige Impressionen]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-impressions) | Die Gesamtzahl der Nutzer:innen, die eine bestimmte Nachricht an einem Tag erhalten und angesehen haben. Jede Nutzer:in wird nur einmal gezählt. |
| [Klicks gesamt]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-clicks) | Die Gesamtzahl (und der Prozentsatz) der Nutzer:innen, die innerhalb der zugestellten Nachricht geklickt haben, unabhängig davon, ob derselbe Nutzer:innen mehrfach geklickt hat. |
| [Eindeutige Klicks]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-clicks) | Die eindeutige Anzahl der Empfänger:innen, die mindestens einmal innerhalb einer Nachricht geklickt haben und wird gemessen durch [`dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/). Jede Nutzer:in wird nur einmal gezählt. |
| [Primäre Konversionen]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event) | Die Anzahl, wie oft ein definiertes Ereignis nach der Interaktion mit oder dem Betrachten einer empfangenen Nachricht aus einer Braze-Kampagne aufgetreten ist. Dieses definierte Event wird von Ihnen bei der Erstellung der Kampagne festgelegt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Nächste Schritte

Jetzt, da Sie über Banner Cards Bescheid wissen, sind Sie bereit für die nächsten Schritte:

- [Erstellen von Banner Card Kampagnen]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/)
- [Bannerkarten in Ihre App einbinden]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/)
