---
nav_title: Geplante Lieferung
article_title: Geplante Lieferung
page_order: 0
page_type: reference
description: "Dieser Referenzartikel beschreibt die Unterschiede zwischen den zeitbasierten Planungsoptionen für die Zustellung von Kampagnen."
tool: Campaigns

---

# Geplante Lieferung

> Kampagnen, die mit zeitgesteuerter Zustellung versendet werden, werden an bestimmten Tagen zugestellt.

## Option 1: Senden, sobald die Kampagne gestartet ist

Wenn Sie sich dafür entscheiden, eine Nachricht zu versenden, sobald sie gestartet wurde, beginnt der Versand Ihrer Nachricht, sobald Sie die Erstellung Ihrer Kampagne abgeschlossen haben.

![Der Abschnitt "Zustellung" mit ausgewählter Option "Geplant" und dem Zeitplan für den Versand, sobald die Kampagne gestartet ist.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Diese Art von Zeitplan ist für einmalige Kampagnen gedacht, die Sie sofort versenden möchten, wie z. B. Nachrichten über ein aktuelles Event. Eine Sport-App kann mit dieser Option zum Beispiel Push-Benachrichtigungen über Spielstandsaktualisierungen planen. Außerdem können Sie mit dieser Option Testnachrichten, die nur an Sie selbst oder Ihr Team gerichtet sind, sofort versenden. 

Wenn Sie vorhaben, die Kampagne zu bearbeiten und nach dem Test erneut zu versenden, müssen Sie das Kontrollkästchen aktivieren, das die Nutzer:innen für den Erhalt der Kampagne [erneut qualifiziert]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/). Standardmäßig sendet Braze eine Kampagne nur einmal an eine:n Nutzer:in, es sei denn, dieses Kästchen ist aktiviert.

## Option 2: Zu bestimmter Zeit senden

Wenn Sie eine Kampagne für einen bestimmten Zeitraum planen, können Sie die Tage und Uhrzeiten festlegen, an denen Ihre Kampagne gesendet wird. Sie können eine Nachricht einmalig, täglich, wöchentlich oder monatlich zu einer bestimmten Tageszeit versenden und festlegen, wann Ihre Kampagne beginnen und enden soll. Dieses Enddatum ist inklusive, d. h. die letzte Sendung wird am Enddatum erfolgen. 

Wenn Sie die Option **Geplante Zustellung** wählen und sich nicht für den Versand zur Ortszeit des Benutzers entscheiden, wird Ihre Kampagne gemäß der Zeitzone versendet, die Sie auf der Seite **Unternehmenseinstellungen** angegeben haben.

![Die Zeitplan-Optionen für den Versand einer Kampagne zu einer bestimmten Zeit.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Kampagnen für die lokale Zeitzone

Sie können die Nachricht in den lokalen Zeitzonen der Nutzer übermitteln, damit die Mitglieder Ihres internationalen Publikums keine Benachrichtigung zu ungünstigen Zeiten erhalten. Kampagnen für die Ortszeit müssen 24 Stunden vorher in den Zeitplan eingebracht werden, um sicherzustellen, dass Nutzer:innen aus allen Zeitzonen sie erhalten können. Lesen Sie die [FAQ zu Kampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign/), um zu verstehen, wie Kampagnen zur Ortszeit funktionieren und welche Regeln für die Zustellung gelten.

Segmente, die mit Kampagnen für Ortszeiten angesprochen werden, sollten mindestens ein 2-Tage-Fenster enthalten, um Nutzer:innen aus allen Zeitzonen einzubeziehen. Wenn Ihre Kampagne beispielsweise für den Versand am Abend geplant ist, aber nur ein Zeitfenster von 1 Tag hat, könnten einige Nutzer:innen aus dem Segment herausfallen, wenn ihre Zeitzone erreicht wird. Beispiele für Filter, die ein 2-Tage-Fenster erzeugen, sind "zuletzt verwendet vor mehr als 1 Tag" und "zuletzt verwendet vor weniger als 3 Tagen" oder "zuerst gekauft vor mehr als 7 Tagen" und "zuerst gekauft vor weniger als 9 Tagen".

### Anwendungsfälle

Festgelegte Zeitpläne eignen sich am besten für im Voraus geplante Nachrichten und wiederkehrende Kampagnen, wie Onboarding und Bindung, die regelmäßig für alle qualifizierten Nutzer:innen laufen.

## Option 3: Intelligentes Timing

[Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) ermöglicht es Ihnen, jedem Nutzer:innen eine Kampagne zu einer anderen Zeit zuzustellen. Braze berechnet die Zeit jedes einzelnen Nutzers auf der Grundlage der Zeit, in der dieser Nutzer typischerweise mit Ihrer App und ihren Benachrichtigungen interagiert. Sie können optional festlegen, dass Kampagnen mit intelligentem Timing nur während eines bestimmten Teils des Tages gesendet werden. Wenn Sie beispielsweise Nutzer:innen über eine Aktion benachrichtigen, die um Mitternacht endet, möchten Sie vielleicht, dass Ihre Nachrichten bis spätestens 22 Uhr versendet werden.

![Die zeitbasierten Planungsoptionen für die Verwendung von Intelligent Timing, um eine Kampagne zu der bei allen Nutzer:innen beliebtesten Zeit für die Nutzung der App zu versenden.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Regeln für die Zustellung

Da die optimale Zeit eines Benutzers ein beliebiger Zeitpunkt innerhalb von 24 Stunden sein kann, müssen alle Intelligent Timing-Kampagnen 24 Stunden im Voraus geplant werden. Darüber hinaus verpassen Nachrichten mit einem 1-Tages-Fenster, ähnlich wie bei zeitlich festgelegten Kampagnen, Nutzer, die aus dem Segment herausfallen, bevor ihre optimale Zeit in ihrer Zeitzone erreicht ist. Segmente für Kampagnen mit intelligentem Timing sollten mindestens ein 3-Tage-Fenster enthalten, um dies zu berücksichtigen.

Wenn das Profil eines Benutzers nicht über genügend Daten verfügt, um eine optimale Zeit zu berechnen, können Sie eine Backup-Methode wählen, um entweder während der beliebtesten Zeit für die Nutzung der App durch alle Benutzer zu senden oder eine benutzerdefinierte Ausweichzeit festzulegen. 

### Anwendungsfälle

Kampagnen mit intelligentem Timing eignen sich am besten für einmalige und wiederkehrende Nachrichten, bei denen eine gewisse Flexibilität in Bezug auf die Zustellung gegeben ist, z. B. wenn sie sich nicht gut für Eilmeldungen oder zeitlich begrenzte Ankündigungen eignen.

