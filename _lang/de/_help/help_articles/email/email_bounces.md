---
nav_title: E-Mail-Rückläufer (Bounce)
article_title: E-Mail-Rückläufer (Bounce)
page_order: 0
page_type: solution
description: "Dieser Hilfeartikel erläutert den Unterschied zwischen Hard Bounces und Soft Bounces."
channel: email
---

# E-Mail Bounces

Was tun Sie, wenn eine Nachricht aus Ihrer E-Mail-Kampagne von den E-Mail-Adressen Ihrer Benutzer zurückgeschickt wird? Lassen Sie uns zunächst die beiden Arten von E-Mail-Bounces definieren und beheben: Hard Bounces und Soft Bounces. 

## Hartes Aufprallen

{% multi_lang_include metrics.md metric='Hard Bounce' %}

Weitere Informationen finden Sie unter [Harter Aufprall]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#hard-bounce).

## Weiche Sprünge

{% multi_lang_include metrics.md metric='Soft Bounce' %} 

Wenn eine E-Mail einen Soft Bounce erhält, versuchen wir es normalerweise innerhalb von 72 Stunden erneut, aber die Anzahl der Wiederholungsversuche variiert von Empfänger zu Empfänger.

Soft Bounces werden zwar nicht in Ihrer Kampagnenanalyse erfasst, aber Sie können die Soft Bounces im [Nachrichtenaktivitätsprotokoll][3] überwachen. Hier können Sie auch den Grund für die Soft Bounces sehen und mögliche Diskrepanzen zwischen den "Sendungen" und "Zustellungen" für Ihre E-Mail-Kampagnen nachvollziehen.

Wenn Sie mehr über die Verwaltung Ihrer E-Mail-Abonnements und -Kampagnen erfahren möchten, lesen Sie die [Best Practices für E-Mails][2].

Brauchen Sie noch Hilfe? Öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).

_Zuletzt aktualisiert am 2\. Mai 2024_

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices
[3]: {{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/
