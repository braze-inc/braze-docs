---
nav_title: Zeitabhängige Funktionalitäten
article_title: Zeitbasierte Funktionalitäten für Canvas
page_order: 1
tools: Canvas
page_type: reference
description: "Dieser Referenzartikel behandelt Definitionen, Zeitzonen und Beispiele für zeitbasierte Funktionen für Canvas."

---

# Zeitbasierte Funktionalitäten für Canvas

> Dieser Referenzartikel behandelt die zeitbasierten Funktionen von Canvas, um Sie bei Strategien und der Fehlerbehebung zu unterstützen und häufige Fragen zu beantworten. 

## Zeitplan-Delay

{% alert important %}
Ab dem 28\. Februar 2023 können Sie keine Canvase mehr mit dem Original-Editor erstellen oder duplizieren. Dieser Abschnitt dient als Referenz, wenn Sie den Zeitplan eines vorhandenen Canvas bearbeiten, der mit dem ursprünglichen Canvas-Workflow erstellt wurde. Für zeitbasierte Funktionen für den Canvas Flow-Workflow sehen Sie sich die [Delay-Komponente]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) an.
{% endalert %}

### Sofort senden

| Definition |  Zeitzone |
| --- | --- |
| Senden Sie die Nachricht sofort, nachdem der Nutzer:innen den vorherigen Schritt erhalten hat, oder, wenn dies der erste Schritt ist, sofort, nachdem der Nutzer:innen den Canvas betreten hat. | -- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][1]

### Senden nach X Tagen

| Definition |  Zeitzone |
| --- | --- |
| Nachricht nach einer Verzögerung senden. Sie können eine Verzögerung in Sekunden, Minuten, Stunden, Tagen oder Wochen angeben.  | -- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][2]

### Senden am nächsten [Wochentag] um X Uhr

| Definition |  Zeitzone |
| --- | --- |
| Senden Sie die Nachricht am nächsten angegebenen Wochentag zu einer bestimmten Uhrzeit.  | Wählen Sie zwischen der **lokalen Zeit des Benutzers** oder der **Firmenzeit** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Nehmen wir zum Beispiel an, Sie wählen „Am nächsten Samstag um 15:15 Uhr senden“ aus. Wenn ein Benutzer den Canvas an einem Samstag betritt, würde er diese Nachricht am nächsten Samstag in sieben Tagen erhalten. Wenn sie an einem Freitag einsteigen, wäre der nächste Samstag in einem Tag.

![][3]

### In X Kalendertagen um Y Uhr senden

| Definition |  Zeitzone |
| --- | --- |
| Senden Sie Nachrichten in einer bestimmten Anzahl von Tagen zu einer bestimmten Zeit. | Wählen Sie zwischen der **lokalen Zeit des Benutzers** oder der **Firmenzeit** |

Canvas berechnet den Delay als `day of the week` + `calendar days` und addiert dann die `time`. Nehmen wir zum Beispiel an, eine Canvas-Komponente wird am Montag um 21:00 Uhr gesendet und der nächste Schritt ist für „Senden in 1 Tag um 9:00 Uhr“ geplant. Diese Nachricht wird am Dienstag um 9 Uhr zugestellt, da der Canvas die Verzögerung als `Monday` + `1 calendar day` berechnet und dann `9 am` hinzufügt.

![][4]

### Intelligentes Timing

| Definition | Zeitzone |
| ---------- | ----- |
| [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) berechnet den optimalen Sendezeitpunkt auf der Grundlage einer statistischen Analyse der bisherigen Interaktionen Ihrer Nutzer mit Ihren Nachrichten (auf der Basis der einzelnen Kanäle) und der App. | Wenn Sie **eine bestimmte Zeit** als [Fallback]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options) auswählen, wird diese in der Ortszeit des Nutzers:innen gesendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][5]

## Globales Frequency-Capping

| Definition | Zeitzone |
| --- | --- |
| Begrenzen Sie, wie oft jeder Benutzer die Leinwand innerhalb eines bestimmten Zeitrahmens erhalten soll, der in Minuten, Tagen, Wochen (sieben Tagen) und Monaten gemessen werden kann. | Die Ortszeit des Benutzers. Wenn die Zeitzone eines Benutzers nicht eingestellt ist, wird auf die Zeitzone des Unternehmens zurückgegriffen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

[Die Frequenzbegrenzung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping) basiert auf Kalendertagen, nicht auf einem 24-Stunden-Zeitraum. Das bedeutet, dass Sie die Häufigkeit des Versendens von maximal einer Kampagne pro Tag begrenzen können. Wenn ein Benutzer jedoch um 23 Uhr seiner Ortszeit eine Nachricht erhält, kann er eine Stunde später (um Mitternacht des nächsten Kalendertages) eine weitere Nachricht erhalten.

![][6]

{% alert note %}
Wenn Sie die richtigen [Nutzerberechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) haben, um Canvase zu genehmigen, sehen Sie den Schritt [**Zusammenfassung**]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_approval/#using-approvals) im Workflow.
{% endalert %}


[1]: {% image_buster /assets/img_archive/schedule_delay_immediately.png %}
[2]: {% image_buster /assets/img_archive/schedule_delay_after.png %}
[3]: {% image_buster /assets/img_archive/schedule_delay_next.png %}
[4]: {% image_buster /assets/img_archive/schedule_delay_in.png %}
[5]: {% image_buster /assets/img_archive/schedule_delay_intelligent.png %}
[6]: {% image_buster /assets/img_archive/schedule_frequency_capping.png %}
