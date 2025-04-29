---
nav_title: Zeitabhängige Funktionalitäten für Kampagnen
article_title: Zeitabhängige Funktionalitäten für Kampagnen
page_order: 2
tool: Campaigns
page_type: reference
description: "Dieser Referenzartikel behandelt zeitbasierte Funktionen für Kampagnen wie die geplante Zustellung, intelligentes Timing und aktionsbasierte Zustellung."

---
# Zeitbasierte Funktionalitäten für Kampagnen

> Wenn Sie Kampagnen verwenden, können Sie die Zeitplanoptionen nutzen, um Ihre Zielgruppe zu erreichen. Zu diesen zeitbasierten Funktionen gehören Kampagnen, die auf geplante Zustellung und aktionsbasierte Zustellung eingestellt sind.

{% alert tip %}
Wenn Sie mehr über die Bereitstellung von Kampagnen erfahren möchten, besuchen Sie unseren speziellen Braze Learning-Kurs [zur Kampagneneinrichtung](https://learning.braze.com/campaign-setup-delivery-targeting-conversions).
{% endalert %}

## Geplante Lieferung

Dieser Abschnitt befasst sich mit der zeitlichen Planung und den Zustellungsoptionen für Kampagnen für [geplante Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/).

### Zu bestimmter Zeit senden

| Definition | Zeitzone |
| ---------- | --------- |
| Senden Sie Nachrichten zu einer bestimmten Uhrzeit, an einem bestimmten Kalenderdatum. | Die Zeitzone des Unternehmens. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Eine Kampagne mit der Option „Zu einer bestimmten Zeit senden“ ausgewählt, um einmalig ab 9 Uhr am 13\. Juli 2021 zu senden.][2]

### Intelligentes Timing

| Definition | Zeitzone |
| ---------- | --------- |
| Die optimale Zeit des Benutzers. Jeder Nutzer erhält die Kampagne zu dem Zeitpunkt, zu dem er sie am ehesten nutzen würde. Wenn Sie mehr erfahren möchten, lesen Sie [Intelligentes Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/). | Wenn Sie eine bestimmte Zeit als [Fallback]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options) auswählen, wird diese in der Ortszeit des Nutzers oder der Nutzerin gesendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Eine Kampagne mit der Option "Intelligentes Timing", die einmal zur optimalen Zeit am 13\. Juli 2021 versendet wird, mit einer benutzerdefinierten Ausweichzeit von 9 Uhr für Benutzer, deren Profile nicht genügend Daten enthalten, um eine optimale Zeit zu berechnen.][3]

### Kampagnen an Nutzer:innen in ihrer Ortszeitzone senden

| Definition | Zeitzone |
| ---------- | --------- |
| Ermöglicht Ihnen die Zustellung von Nachrichten an ein Segment, das auf der [individuellen Zeitzone]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery) eines Benutzers basiert. | Die Ortszeit des Benutzers. Wenn die Zeitzone eines Benutzers nicht eingestellt ist, wird auf die Zeitzone des Unternehmens zurückgegriffen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Eine Kampagne mit der Option „Zu einem bestimmten Zeitpunkt senden“, die so eingestellt ist, dass sie am 13\. Juli 2021 um 9 Uhr morgens gesendet wird, wobei das Kontrollkästchen „Kampagne an Nuzter:innen in ihrer lokalen Zeitzone senden“ aktiviert ist.][4]

### Nutzer:innen dürfen sich erneut für den Erhalt der Kampagne qualifizieren

| Definition | Zeitzone |
| ---------- | --------- |
| Legen Sie fest, wann ein:e Nutzer:in nach einer Nachricht dieser Kampagne wieder für den Empfang der Kampagne zugelassen wird. [Mehr erfahren]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/). | -- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Eine Kampagne mit dem ausgewählten Kontrollkästchen „Nutzer:innen dürfen sich erneut für den Erhalt der Kampagne qualifizieren“.][5]

## Aktionsbasierte Zustellung

Dieser Abschnitt behandelt die Zeitplanverzögerung und die Zustellungsoptionen für [aktionsbasierte Zustellungskampagnen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

### Zeitplan-Delay

{% alert important %}
Denken Sie bei der Wahl der Delay-Dauer daran, dass Ihre Nutzer:innen Ihre Kampagne nicht erhalten, wenn Sie einen Delay einstellen, der länger ist als die [Dauer der Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration).
{% endalert %}

#### Kampagne sofort senden

| Definition | Zeitzone |
| ---------- | --------- |
| Nachricht senden, unmittelbar nachdem der oder die Nutzer:in die Trigger-Aktion durchgeführt hat. | -- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Zeitplanverzögerung so einstellen, dass die Kampagne sofort nach Eintreten des Trigger-Events gesendet wird.][6]

#### Kampagne nach X Tagen senden

| Definition | Zeitzone |
| ---------- | --------- |
| Nachricht nach einer Verzögerung senden. Sie können eine Verzögerung in Sekunden, Minuten, Stunden, Tagen oder Wochen angeben. Für [In-App-Nachricht-Kampagnen]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about) können Sie eine Verzögerung von bis zu zwei Stunden einstellen. | -- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Zeitplanverzögerung so festlegen, dass Kampagnen einen Tag nach Eintreten des Trigger-Events gesendet werden.][7]

#### Kampagne am nächsten [Wochentag] um X Uhr senden

| Definition | Zeitzone |
| ---------- | --------- |
| Senden Sie die Nachricht am nächsten angegebenen Wochentag zu einer bestimmten Uhrzeit. | Wählen Sie zwischen der **lokalen Zeit des Benutzers** oder der **Firmenzeit** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Nehmen wir zum Beispiel an, Sie wählen „Am nächsten Samstag um 15:15 Uhr senden“ aus. Wenn ein:e Nutzer:in den Trigger-Event an einem Samstag durchführt, würde er oder sie diese Nachricht am nächsten Samstag in sieben Tagen erhalten. Wenn sie an einem Freitag einsteigen, wäre der nächste Samstag in einem Tag.

![][8]

#### In X Kalendertagen um Y senden

| Definition | Zeitzone |
| ---------- | --------- |
| Senden Sie Nachrichten in einer bestimmten Anzahl von Tagen zu einer bestimmten Zeit. | Wählen Sie zwischen der **lokalen Zeit des Benutzers** oder der **Firmenzeit** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze berechnet die Verzögerung als `day of the week` + `calendar days` und addiert dann die `time`. Nehmen wir zum Beispiel an, der oder die Nutzer:in führt das Trigger-Event am Montag um 21 Uhr aus und der Zeitplan ist auf „Kampagne in 1 Tag um 9 Uhr senden“ eingestellt. Diese Nachricht wird am Dienstag um 9 Uhr zugestellt, da Braze die Verzögerung als `Monday` + `1 calendar day` berechnet und dann `9 am` hinzufügt.

![][9]

### Ruhezeiten

| Definition | Zeitzone |
| ---------- | --------- |
| Verhindern Sie den Versand von Nachrichten während bestimmter Stunden. Wenn eine Nachricht während der Ruhezeiten ausgelöst wird, können Sie wählen, ob Sie die Nachricht abbrechen oder zum nächsten verfügbaren Zeitpunkt senden möchten (z. B. am Ende der Ruhezeiten). | Die Ortszeit des Benutzers. Wenn die Zeitzone eines Benutzers nicht eingestellt ist, wird auf die Zeitzone des Unternehmens zurückgegriffen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Eine Kampagne mit aktivierten Stillen Stunden. In diesem Beispiel werden Nachrichten zwischen 12 Uhr und 8 Uhr morgens in der Ortszeit des Nutzers oder der Nutzerin nicht gesendet. Wenn eine Nachricht während der Ruhezeiten getriggert wird, wird die Nachricht zur nächsten verfügbaren Zeit gesendet.][10]

### Zulassen, dass Nutzer:innen erneut für Kampagnen qualifiziert werden

| Definition | Zeitzone |
| ---------- | --------- |
| Legen Sie fest, wann ein: Nutzer:in nach einer Nachricht dieser Kampagne für den Empfang der Kampagne [erneut qualifiziert]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) wird. | -- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Eine Kampagne mit dem ausgewählten Kontrollkästchen „Nutzer:innen dürfen sich erneut für den Erhalt der Kampagne qualifizieren“.][5]

### Globales Frequency-Capping

| Definition | Zeitzone |
| ---------- | --------- |
| Begrenzen Sie, wie oft jeder Benutzer die Kampagne innerhalb eines bestimmten Zeitrahmens erhalten soll, der in Minuten, Tagen, Wochen (7 Tage) und Monaten gemessen werden kann. Weitere Informationen finden Sie unter [Frequenzkappung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping). | Die Ortszeit des Benutzers. Wenn die Zeitzone eines Benutzers nicht eingestellt ist, wird auf die Zeitzone des Unternehmens zurückgegriffen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Standardmäßig ist das Frequency-Capping für neue Canvase ausgeschaltet. Frequency-Capping wird auf der Schritt-Ebene angewendet, nicht auf der Canvas-Entry-Ebene.

Die Frequenzbegrenzung basiert auf Kalendertagen, nicht auf einem 24-Stunden-Zeitraum. Das bedeutet, dass Sie die Häufigkeit des Versendens von maximal einer Kampagne pro Tag begrenzen können. Wenn ein Benutzer jedoch um 23 Uhr seiner Ortszeit eine Nachricht erhält, kann er eine Stunde später (um Mitternacht des nächsten Kalendertages) eine weitere Nachricht erhalten. 

## Konversionsfrist

| Definition | Zeitzone |
| ---------- | --------- |
| Die maximale Zeitspanne, die zwischen dem Erhalt einer Kampagne durch eine:n Nutzer:in und der Ausführung der zugewiesenen Aktion vergehen darf, damit diese als Konversion gewertet wird. Weitere Informationen finden Sie unter [Konvertierungsereignisse]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/). | -- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



[2]: {% image_buster /assets/img_archive/time_designated.png %}
[3]: {% image_buster /assets/img_archive/time_intelligent_timing.png %}
[4]: {% image_buster /assets/img_archive/time_local.png %}
[5]: {% image_buster /assets/img_archive/time_reeligibility.png %}
[6]: {% image_buster /assets/img_archive/time_delay_immediately.png %}
[7]: {% image_buster /assets/img_archive/time_delay_after.png %}
[8]: {% image_buster /assets/img_archive/time_delay_on_the_next.png %}
[9]: {% image_buster /assets/img_archive/time_delay_in.png %}
[10]: {% image_buster /assets/img_archive/time_quiet_hours.png %}
