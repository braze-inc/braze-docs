---
nav_title: Workspace-Zeitzonen
article_title: Zeitzonen für den Versand von Nachrichten im Workspace
alias: /workspace_time_zones/
page_order: 3
description: "Dieser Referenzartikel beschreibt, wie Sie verschiedene Zeitzonen für Ihre Braze-Workspaces konfigurieren können, um Teams, die an verschiedenen geografischen Standorten tätig sind, mehr Kontrolle über den Zeitplan für Kampagnen und Canvas zu ermöglichen."
---

# Zeitzonen für den Workspace zum Versenden von Nachrichten

> Mit den Zeitzonen für Workspaces können Administratoren spezifische Zeitzonen für einzelne Workspaces festlegen. Dadurch werden geplante Kampagnen und Canvases (die weder die Ortszeit noch intelligentes Timing verwenden) entsprechend der für den Workspace festgelegten Zeitzone versendet und nicht entsprechend der übergeordneten Zeitzone des Unternehmens.

{% multi_lang_include early_access_beta_alert.md feature='Workspace time zones' %}

Standardmäßig übernimmt ein neuer Workspace die für Ihr Unternehmen festgelegte Zeitzone. Administratoren können diese Standard-Einstellung für einen oder mehrere Workspaces mit Zeitzonen für Workspaces überschreiben. Wenn für einen Workspace eine Zeitzone festgelegt wird, referenzieren geplante Kampagnen und Canvases innerhalb dieses Workspaces für ihre Versandzeiten diese neue Zeitzone.

Wenn beispielsweise die Zeitzone eines Workspaces auf PST eingestellt ist und eine Kampagne innerhalb dieses Workspaces für den Versand um 15:00 Uhr PST im Zeitplan steht, wird sie um 15:00 Uhr PST zugestellt. Dies gilt auch dann, wenn die Zeitzone Ihres Unternehmens abweicht (z. B. EST, wo 15 Uhr PST 18 Uhr EST entspricht).

## Zeitzonen im Workspace verwalten

Wenn Sie Administrator sind, können Sie auf die Zeitzonen des Workspace-Arbeitsbereichs zugreifen und diese verwalten, indem Sie zu **„Einstellungen“** > **„Admin-Einstellungen“** > **„Zeitzonen des Workspace-Arbeitsbereichs“** navigieren.

Hier können Sie eine Liste aller Ihrer Workspaces, deren eingestellte Zeitzone und den Zeitpunkt der letzten Bearbeitung der Zeitzone einsehen. Bitte nutzen Sie die Suchleiste, um bestimmte Workspaces anhand ihres Namens zu finden.

![Seite „Zeitzonen für Workspaces“ mit einer Liste der Workspaces, ihren jeweiligen Zeitzonen und dem Zeitpunkt der letzten Bearbeitung der Zeitzonen.]({% image_buster /assets/img/workspaces/time_zones/workspace_time_zones_page.png %})

### Einstellung der Zeitzone 

{% alert note %}
Es kann einige Minuten dauern, bis die Updates der Zeitzonen wirksam werden.
{% endalert %}

{% tabs %}
{% tab Single workspace %}
1. Bitte suchen Sie den gewünschten Workspace in der Liste.
2. Bitte wählen Sie das Symbol **„Bearbeiten“** neben dem Namen des Workspaces.

![Button „Bearbeiten“ neben dem Namen eines Workspaces.]({% image_buster /assets/img/workspaces/time_zones/single_edit_icon.png %})

{: start="3"}
3\. Bitte wählen Sie im Dropdown-Menü die gewünschte Zeitzone für diesen Workspace aus.
4\. Wählen Sie **Speichern**.

![Dropdown-Menü mit ausgewählter Zeitzone GMT.]({% image_buster /assets/img/workspaces/time_zones/edit_single_workspace.png %})
{% endtab %}
{% tab Multiple workspaces %}

Sie können eine bestimmte Zeitzone auf mehrere Workspaces gleichzeitig anwenden, indem Sie wie folgt vorgehen:

1. Bitte wählen Sie die Kontrollkästchen neben allen Workspaces aus, die Sie aktualisieren möchten.
2. Bitte wählen Sie **„Zeitzone bearbeiten**“.
3. Bitte wählen Sie aus dem Dropdown-Menü eine Zeitzone aus, die auf alle ausgewählten Workspaces angewendet werden soll.

![Seite „Zeitzonen für Workspaces“ mit mehreren ausgewählten Workspaces und einem Button „Zeitzone bearbeiten“.]({% image_buster /assets/img/workspaces/time_zones/bulk_edit_workspace_time_zone.png %})

{: start="4"}
4\. Wählen Sie **Speichern**. 

{% endtab %}
{% endtabs %}

## Auswirkungen auf Kampagnen und Canvases

{% alert important %}
Bitte informieren Sie die zuständigen Teams und Beteiligten innerhalb jedes Workspaces über etwaige Änderungen der Zeitzone, um Unklarheiten hinsichtlich der Zeitpläne für Kampagnen zu vermeiden.
{% endalert %}

- **Ortszeit und intelligente Zeitkampagnen:** Kampagnen und Canvases, die die Ortszeit der Nutzer:innen oder [das intelligente Timing]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/#option-3-intelligent-timing) für die Zustellung verwenden, funktionieren weiterhin wie bisher und werden nicht von den Zeitzonen des Workspace beeinflusst.
- **Geplante Kampagnen und Canvases:** Alle geplanten Kampagnen oder Canvas-Inhalte, die nicht die Ortszeit der Nutzer:innen oder die intelligente Zeit für die Zustellung verwenden, werden nun auf Grundlage der ausgewählten Zeitzone des Workspace-Arbeitsbereichs versendet.
- **Kampagnen, die vor einer Zeitzonenänderung im Zeitplan standen:** Wenn Sie eine Kampagne oder Canvas vor der Änderung der Zeitzone des Workspace geplant haben, behält Braze die ursprüngliche Sendezeit bei und plant sie nicht neu. Wenn beispielsweise eine Kampagne so eingestellt ist, dass sie um 19:00 Uhr PST versendet wird, und die Zeitzone des Workspace auf EST geändert wird, wird die Kampagne weiterhin um 19:00 Uhr PST versendet (was nun 22:00 Uhr EST entspricht). Das System referenziert weiterhin die ursprüngliche Zeit, interpretiert diese jedoch anhand der neuen Zeitzone des Workspace.

## Auswirkungen auf datumsbasierte Zielgruppen-Filter

Wenn die Zeitzone eines Workspaces aktualisiert wird, werden Zielgruppen-Filter, die ausschließlich auf Datumskriterien basieren (ohne Angabe einer bestimmten Uhrzeit), anhand der Grenzen der neuen Zeitzone neu bewertet.

Für Filter wie „Zuletzt angepasstes Event X nach“ verwendet Braze die Zeitzone des Workspace, um den Beginn und das Ende des Kalendertags zu bestimmen. Durch Ändern dieser Einstellung wird der Stichtag 23:59 Uhr für das jeweilige Datum verschoben.

### Beispiel

A Workspace updates its time zone from Eastern Time (EST) to Pacific Time (PST).

- **Vorherige Anmeldefrist:** 23:59 Uhr EST
- **Neue Annahmeschlusszeit:** 23:59 Uhr PST (das entspricht 2:59 Uhr EST am folgenden Tag)

Nach dieser Änderung wird eine Nutzer:in, die das angepasste Event am 6\. März 2026 um 22:00 Uhr PST (das entspricht 1:00 Uhr EST am 7\. März 2026) ausführt, nun in die Zielgruppe aufgenommen, da sie innerhalb der PST-Kalendergrenze für dieses Datum liegt.

## Abweichungen melden

Die Zeitzonen im Workspace ermöglichen eine präzise Steuerung des Versands von Kampagnen. Bitte beachten Sie jedoch, dass es während der frühen Zugangsphase zu dieser Funktion zu möglichen Abweichungen bei der Berichterstellung kommen kann. Bitte überprüfen Sie die Datenpunkte und beachten Sie die Zeitzone, wenn Sie Berichte für Workspaces mit spezifischen Zeitzonenüberschreibungen analysieren.