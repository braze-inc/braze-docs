---
nav_title: Diagnose-Dashboard für Messaging
article_title: Diagnose-Dashboard für Messaging
description: "Dieser Referenzartikel behandelt das Dashboard für die Nachrichten-Diagnose, das Ihnen dabei hilft, zu verstehen, warum Nachrichten aus Ihren Kampagnen oder Canvases möglicherweise nicht wie erwartet versendet wurden."
alias: /ccdd/
page_order: 4.5
---

# Diagnose-Dashboard für Messaging

> Das Dashboard **„Messaging Diagnostics“** bietet eine detaillierte Aufschlüsselung der Ergebnisse des Nachrichtenversands, sodass Sie Trends erkennen und potenzielle Probleme in Ihrer Messaging-Konfiguration diagnostizieren können. Dieses Dashboard kann Ihnen dabei helfen, zu verstehen, warum Nachrichten aus Ihren Kampagnen oder Canvases möglicherweise nicht wie erwartet versendet wurden.

{% alert important %}
Das Dashboard **„Messaging Diagnostics“** befindet sich derzeit in der Early-Access-Phase. Bitte wenden Sie sich an Ihren Customer-Success-Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind.
{% endalert %}

## Wichtige Konzepte

### Versandt und zugestellt

Es ist wichtig zu verstehen, dass dieses Dashboard darüber berichtet, wie Braze eine Nachricht intern verarbeitet hat, und nicht über den endgültigen Zustellstatus der Nachricht.

Eine Nachricht, die in diesem Dashboard als „gesendet“ markiert ist, bedeutet, dass Braze die Nachricht erfolgreich verarbeitet und versendet hat. Für die meisten Kanäle bedeutet dies, dass Braze die Nachricht an den entsprechenden externen Versandpartner weitergeleitet hat. Es wird jedoch keine Garantie für die endgültige Zustellung an das Gerät der Nutzer:innen übernommen. 

Wenn Braze eine Nachricht „versendet“, kann die endgültige Zustellung von externen Diensten abhängig sein. Bitte beachten Sie die folgenden Beispiele für jeden Kanal.

| Kanal | Beispiel für die endgültige Zustellung |
| --- | --- |
| Content-Cards | Die Karte wurde versendet und kann nun eingesehen werden. |
| E-Mail | Braze übermittelt die Nachricht an einen E-Mail-Anbieter (ESP). Der ESP ist dann für die endgültige Zustellung verantwortlich. Dieses ESP kann beispielsweise einen „Bounce“ melden, wenn die E-Mail-Adresse ungültig ist oder der Posteingang voll ist. |
| In-App-Nachrichten | Die Nachricht wurde den Nutzern angezeigt. |
| LINE | Die Nachricht wurde erfolgreich an einen sendenden Partner übergeben. |
| Push | Braze übermittelt die Nachricht an den entsprechenden Dienst für Push-Benachrichtigungen (wie beispielsweise den Apple Push Notification Service für iOS oder Firebase Cloud Messaging für Android). Dieser Dienst ist für die endgültige Zustellung der Benachrichtigung an das Gerät verantwortlich. |
| SMS/MMS/RCS | Braze übermittelt die Nachricht an ein SMS-Gateway (wie Twilio). Dieses Gateway ist für die endgültige Zustellung an den Mobilfunkanbieter verantwortlich. |
| Webhooks | Die Webhook-Anfrage wurde erfolgreich durchgeführt und hat eine`2xx`Antwort zurückgegeben. |
| WhatsApp | Die Nachricht wurde erfolgreich an einen sendenden Partner übergeben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

### Aktualität der Daten

Die Häufigkeit der Updates der Daten in diesem Dashboard kann je nach Systemauslastung schwanken. Die Häufigkeit der Updates kann nicht garantiert werden, jedoch erfolgt diese in den meisten Fällen innerhalb einer Stunde.

## Konfiguration des Dashboards

Sie können auf das Diagnose-Dashboard zugreifen, indem Sie zu **„Analytics“** > **„Dashboard Builder“** navigieren und **„Messaging Diagnostics“** aus der Liste der von Braze erstellten Dashboards auswählen.

Um das Dashboard auszuführen und Ihre Daten anzuzeigen:

1. Bitte wählen Sie entweder **„Kampagnen“** oder **„Canvases“** als Quelle für Ihre Dashboard-Berichte aus. 
2. Bitte wählen Sie eine oder mehrere Kampagnen oder Canvases aus.
3. Bitte wählen Sie **„Dashboard ausführen“,** um die Daten für die von Ihnen ausgewählten Filter zu laden.

![Beispiel für eine Kampagnen- und Canvas-Diagnose vom 25\. bis 31\. Mai 2025 für eine Willkommensserie-Kampagne.]({% image_buster /assets/img/campaign_canvas_dashboard_example.png %}){: style="max-width:90%;"}

## Interpretation der Daten

{% alert note %}
Das Dashboard zeigt nur die Daten der letzten 7 Tage an.
{% endalert %}

### Zusammenfassungsfelder

Am oberen Rand der Seite befinden sich wichtige Zusammenfassungsfelder für den Zeitraum, den Sie ausgewählt haben, die Folgendes anzeigen:

- **Gesamtzahl der Abbrüche:** Die Gesamtzahl der Nachrichten, die abgebrochen wurden. Dies schließt Canvas-Zielgruppenmitglieder ein, die Canvas nicht betreten oder Canvas verlassen haben, weil sie einen Canvas-Schritt erlebt oder die Ausstiegskriterien erfüllt haben, während sie ein Ausstiegsereignis durchgeführt haben.
- **Nachricht wird gesendet:** Die Gesamtzahl der Nachrichten, die Braze erfolgreich verarbeitet und versendet hat. 
  - **E-Mail, SMS/MMS/RCS, WhatsApp, LINE und Push-Benachrichtigungen:** Die Nachricht wurde erfolgreich an einen sendenden Partner übergeben.  
  - **Webhooks:** Die Webhook-Anfrage wurde erfolgreich durchgeführt und hat eine`2xx`Antwort zurückgegeben.  
  - **Content-Cards:** Die Karte wurde versendet und kann nun eingesehen werden.    
  - **In-App-Nachrichten:** Die Nachricht wurde dem Nutzer:in angezeigt.

### Nachrichtenergebnisse im Zeitverlauf

Dieses Zeitreih-Chart zeigt eine tägliche Aufschlüsselung der verschiedenen Gründe, aus denen eine Nachricht abgebrochen oder eine Nutzer:in aus einem Canvas entfernt wurde. Dieses Chart zeigt nicht die Anzahl der Sendungen an.  

{% alert note %}
Um die Übersichtlichkeit des Charts zu gewährleisten, werden Abbruch- oder Ausfallgründe, die in dem von Ihnen ausgewählten Zeitraum nicht vorgekommen sind, nicht im Chart angezeigt.
{% endalert %}

### Aufschlüsselung der Ergebnisse der Nachrichten

Dieses Chart zeigt die Aufschlüsselung aller Nachrichtenergebnisse innerhalb des von Ihnen ausgewählten Zeitraums. Es bietet einen umfassenden Überblick über:
- Die Gesamtzahl der Sendungen als Anteil aller Ergebnisse.  
- Die proportionale Aufschlüsselung der einzelnen Abbruch- und Abbruchgründe. Dies unterstützt Sie dabei, die häufigsten Gründe, warum Nachrichten nicht gesendet werden, schnell zu identifizieren.

### Ergebnisse abbrechen

Die folgenden Definitionen erläutern die im Dashboard angezeigten Abbruch-Ergebnisse. Die Ergebnisse sind nach Kategorien gruppiert, um die Suche nach dem gewünschten Ergebnis zu vereinfachen.

#### Inhalt und Darstellung

| Ergebnis abbrechen | Erklärung |
| ---- | ---- |
| Content-Card abgelaufen | Die Content-Card ist abgelaufen, bevor die Nutzer:innen sie sehen konnten. |
| Content-Card ungültig | Die Content-Card wies Fehler auf und wurde nicht an den Nutzer:in gesendet. Einige häufige Gründe hierfür sind: {::nomarkdown}<ul><li> Die maximale Größe wurde überschritten (2 KB). </li><li> Das Ablaufdatum ist ungültig. </li><li> Die Nachricht enthält ungültige Zeichen. </li></ul>{:/} |
| Connected-Content nicht erfolgreich | Braze hat versucht, die Nachricht zu senden, jedoch ist Connected-Content nach Erreichen der maximalen Anzahl an Wiederholungsversuchen (Standardwert ist fünf) fehlgeschlagen. |
| Zeitüberschreitung beim Rendern von In-App-Nachrichten | Nach mehreren Wiederholungsversuchen konnte Liquid nicht gerendert werden und es kam zu einer Zeitüberschreitung. |
| Liquid abort | Der[abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages)Liquid-Tag wurde aufgerufen, daher wurde die Übertragung abgebrochen. |
| Zeitüberschreitung bei der Liquid-Wiedergabe | Das Rendern des Liquid-Templates hat zu lange gedauert. Am wahrscheinlichsten bei Bannern, In-App-Nachrichten und E-Mails. |
| Liquid-Syntaxfehler | Das Liquid-Template wies einen Parsing-Fehler auf, daher wurde die Nachricht abgebrochen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Kampagne und Canvas

| Ergebnis abbrechen | Erklärung |
| ---- | ---- |
| Verzögerungsschrittfehler | Der [Schritt „Verzögerung“]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) ist fehlgeschlagen, was dazu führte, dass die Nutzer:innen die Canvas verlassen mussten. Dieser Fehler kann auftreten, wenn: {::nomarkdown}<ul><li> Die Variable, die dem personalisierten Verzögerungsschritt übergeben wurde, war leer oder hatte einen ungültigen Typ. </li><li> Die Verzögerung überschreitet die maximal zulässige Dauer innerhalb von Canvas.</li></ul>{:/} |
| Ausnahme-Event oder Beendigungsereignis | Die Nutzer:in war zuvor berechtigt, die Nachricht zu empfangen, aber entweder {::nomarkdown}<ul><li> ein <a href="/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-3-select-exception-events">Ausnahme-Event</a> für eine aktionsbasierte Kampagne durchgeführt, sodass die Nachricht abgebrochen wurde, oder </li><li> erfüllten die Canvas<a href="/docs/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#setting-up-exit-criteria">-Ausstiegskriterien,</a> sodass sie während der Reise ausgeschlossen wurden.</li></ul>{:/} |
| Inaktive Kampagne | Die Kampagne wurde während der Übermittlung der Nachricht unterbrochen und daher abgebrochen. |
| Inaktive Canvas | Das Canvas wurde beendet, bevor die Nutzer:in die Reise begonnen hat. |
| Inaktiver Canvas-Schritt | Dies kann im Canvas auftreten, wenn: {::nomarkdown}<ul><li> Der Canvas-Schritt wurde entfernt. </li> <li>Canvas wurde angehalten, wodurch alle Schritte inaktiv werden. </li></ul>{:/} |
| Begrenzte Auflage | Die Kampagne hat das festgelegte Volumenlimit erreicht, daher wurde der Versand abgebrochen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Rate-Limiting und Zeitsteuerung

| Ergebnis abbrechen | Erklärung |
| ---- | ---- |
| Frequency-Capping | Die Nutzer:innen haben bereits die maximale Anzahl an Nachrichten erhalten, die gemäß den[ Frequency-Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping)-Regeln Ihres Workspaces zulässig ist, daher wurde der Versand abgebrochen. |
| Ruhezeiten abbrechen | Für die Kampagne oder den Canvas-Schritt wurde die Funktion „Ruhezeiten“ aktiviert, wobei als Fallback die Option **„Nachricht abbrechen“** festgelegt wurde. Die Nutzer:innen haben die Kampagne während der Ruhezeiten ausgelöst oder den Canvas-Schritt aufgerufen, sodass die Nachricht abgebrochen wurde. Dies führt jedoch nicht zum Verlassen des Canvas durch die Nutzer:innen. |
| Rate-Limits über 72 Stunden | Die Nachricht wurde aufgrund von [Rate-Limits]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) bei[ der Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) länger als 72 Stunden zurückgehalten, sodass der Versand abgebrochen wurde. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Teilnahmeberechtigung und Profil der Nutzer:innen

| Ergebnis abbrechen | Erklärung |
| ---- | ---- |
| Doppelte Bezeichner für Nutzer:innen | Mehrere Nutzer:innen mit einem übereinstimmenden Bezeichner (z. B. externe ID, E-Mail-Adresse, Telefonnummer) waren berechtigt, diese Nachricht zu erhalten. Um doppelte Sendungen an denselben Nutzer:in zu vermeiden, wurde diese Nachricht abgebrochen. |
| Die Nutzer:in hat die Vorabprüfung für den Schritt „Nachricht“ nicht bestanden. | Diese Vorabprüfung wird vor der Validierung der Zustellung durchgeführt. In diesem Fall hat der Nutzer die grundlegende Vorabprüfung für diesen Nachrichtenschritt nicht bestanden (Nutzer:in nicht gefunden oder für den Kanal des Nachrichtenschritts nicht berechtigt). **Hinweis:** Bei einem Mehrkanal-Nachrichtenschritt bedeutet dies, dass die Nutzer:innen nicht gefunden wurden; die Berechtigung für die Kanäle wird hier nur für Einzelkanal-Nachrichtenschritte überprüft. |
| Der Nutzer:in hat die Vorabprüfung für die getriggerte Nachricht nicht bestanden. | Bei einer getriggerten Nachricht führt Braze zunächst eine Reihe grundlegender Vorabprüfungen hinsichtlich der Berechtigung der Zielgruppen, der erneuten Berechtigung und der Berechtigung der Kanäle durch, bevor eine Nachricht erstellt wird, die aufgrund dieses Auslösers versendet wird. |
| Die Nutzer:in ist nicht mehr berechtigt. | Der Nutzer gehörte ursprünglich zur Zielgruppe, entsprach jedoch nicht mehr den Zielgruppenkriterien, bevor Braze die Nachricht versandte oder den Nutzer in Canvas eintrug. Der Zeitraum zwischen dem Zeitpunkt, zu dem die Nutzer:innen erstmals die Kriterien der Zielgruppe erfüllen, und dem Zeitpunkt, zu dem sie aus der Zielgruppe herausfallen, kann auf Verzögerungen zurückzuführen sein, die durch folgende Faktoren verursacht werden: {::nomarkdown}<ul><li>Intelligentes Timing</li><li>Ruhezeiten</li><li>Ortszeit</li><li>Rate-Limits für die Zustellung (gilt nicht für Canvas-Einträge)</li><li>Verzögerungen im Messaging</li></ul>{:/} |
| Die Nutzer:in ist nicht für diesen Schritt berechtigt. | Die Nutzer:innen haben die Canvas verlassen, weil sie die festgelegten [Validierungen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#delivery-validations) für [die]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#delivery-validations) Zustellung der Nachricht nicht erfüllt haben oder weil sie Teil einer [Unterdrückungsliste]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) waren. |
| Nutzer:in ist nicht erneut berechtigt | Die Nutzer:innen waren berechtigt, die Nachricht zu empfangen oder Canvas aufzurufen, jedoch wurde der Versand aufgrund von Einstellungen zur erneuten Berechtigung oder zum erneuten Eingang abgebrochen. Dies kann auftreten, wenn die Nutzer:in die Kampagne bereits erhalten hat oder das Canvas erst kürzlich aufgerufen hat, wenn für diese Nutzer:in bereits eine weitere Sendung für dieselbe Kampagne läuft oder wenn die erneute Berechtigung oder der erneute Eintritt deaktiviert ist. |
| Nutzerprofil nicht gefunden | Die Nutzer:in hat entweder nie existiert oder ist nicht mehr in Braze vorhanden. Einige häufige Fälle sind: {::nomarkdown}<ul><li> Der Nutzer wurde über API-Messaging angesprochen, war jedoch nie in Braze registriert. </li><li>Der Nutzer:in wurde gelöscht, bevor die Nachricht gesendet oder der Canvas-Schritt ausgeführt wurde. </li><li>Der Nutzer:in wurde vor dem Senden der Nachricht mit einem anderen Profil zusammengeführt.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Kanal und Zustellung

| Ergebnis abbrechen | Erklärung |
| ---- | ---- |
| Lieferzeitlimit der Partner | Braze hat 24 Stunden lang versucht, diese Nachricht an Ihren Partner für die Zustellung zu senden, jedoch hat der Partner während des gesamten Zeitfensters temporäre Fehler zurückgegeben. |
| Push-Zugangsdaten sind ungültig | Die [Push-Zugangsdaten]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting/#valid-push-token) für diese App fehlen oder sind ungültig, daher wurde der Versand abgebrochen. Bitte führen Sie ein Update der Zugangsdaten in **den App-Einstellungen** durch. |
| Nutzer:in ist nicht für Android-Push, App oder Gerät aktiviert | Es ist nicht möglich, eine Push-Benachrichtigung an diesen Nutzer:in zu senden. Einige häufige Gründe: {::nomarkdown}<ul><li> Die Nutzer:in hat die App nicht installiert.</li> <li> Die Nutzer:innen verfügen nicht über ein gültiges Push-Token. </li> <li>Der Nutzer verfügt nicht über das erforderliche Gerät für diese Push-Benachrichtigung. </li> <li> Der Nutzer:in hat die Benachrichtigungen für diese App in seinen Einstellungen des Geräts deaktiviert. </li> <li> Die Nutzer:innen haben sich nicht für den Empfang von Push-Benachrichtigungen angemeldet oder diese aktiviert.</li></ul>{:/} |
| Nutzer:in ist nicht für iOS-Push, App oder Gerät aktiviert | Entspricht „Nutzer:in nicht für Android-Push, App oder Gerät aktiviert“ (siehe oben). |
| Nutzer:in ist nicht für Kindle Push, App oder Gerät aktiviert. | Entspricht „Nutzer:in nicht für Android-Push, App oder Gerät aktiviert“ (siehe oben). |
| Nutzer:in ist nicht für Web-Push, App oder Gerät aktiviert. | Entspricht „Nutzer:in nicht für Android-Push, App oder Gerät aktiviert“ (siehe oben). |
| Nutzer:innen sind nicht für Content-Cards aktiviert | Die Nutzer:innen haben keine Apps verwendet, die diese Content-Card enthalten. |
| Nutzer:in ist nicht für E-Mail aktiviert | An diese Nutzer:innen können keine E-Mails gesendet werden. Einige häufige Gründe: {::nomarkdown}<ul><li> Die Nutzer:in hat keine E-Mail-Adresse in ihrem Nutzerprofil angegeben. </li><li> Der Abo-Status der Nutzer:innen schließt sie vom Erhalt dieser E-Mail aus. </li><li> Die E-Mail-Adresse der Nutzer:innen wurde zuvor als ungültig markiert (Hard Bounce). </li><li> Nachrichten, die an diese E-Mail-Adresse gesendet werden, werden durchweg als Spam markiert, daher wurde der Versand abgebrochen.</li></ul>{:/} |
| Nutzer:in ist für LINE nicht aktiviert | Es ist nicht möglich, LINE-Nachrichten an diese Nutzer:innen zu senden. Einige häufige Gründe: {::nomarkdown}<ul><li> Der Nutzer hat keine Telefonnummer in seinem Nutzerprofil angegeben. </li><li> Die Telefonnummer der Nutzer:in wurde aufgrund von Fehlern bei der Zustellung als ungültig markiert. </li><li> Der Abo-Status der Nutzer:innen schließt sie vom Erhalt dieser Nachricht aus. </li><li> Die Nutzer:in verfügt nicht über eine LINE-ID.</li></ul>{:/} |
| Nutzer:innen sind nicht für SMS/MMS/RCS aktiviert | Es können keine SMS-Nachrichten an diese Nutzer:innen gesendet werden. Einige häufige Gründe: {::nomarkdown}<ul><li> Der Nutzer hat keine Telefonnummer in seinem Nutzerprofil angegeben. </li><li> Die Telefonnummer der Nutzer:in wurde aufgrund von Fehlern bei der Zustellung als ungültig markiert. </li><li> Die Telefonnummer der Nutzer:innen hat kein gültigesE.164Format, und Versuche, die Nummer automatisch zu formatieren, sind fehlgeschlagen. </li><li> Der Abo-Status des Nutzers schließt ihn vom Empfang der SMS-Nachricht aus.</li><li>Die Telefonnummer der Nutzer:in befindet sich in einem gesperrten Land.</li></ul>{:/} |
| Nutzer:in ist nicht für WhatsApp aktiviert | Es ist nicht möglich, WhatsApp-Nachrichten an diese Nutzer:innen zu senden. Einige häufige Gründe: {::nomarkdown}<ul><li> Der Nutzer hat keine Telefonnummer in seinem Nutzerprofil angegeben. </li><li> Die Telefonnummer der Nutzer:in wurde aufgrund von Fehlern bei der Zustellung als ungültig markiert. </li><li> Der Abo-Status der Nutzer:innen schließt sie vom Erhalt dieser Nachricht aus. </li><li> Die Nutzer:in verfügt nicht über ein WhatsApp-Konto.</li></ul>{:/} |
| Webhook ist fehlgeschlagen | Der Webhook hat einen nicht erfolgreichen Code (nicht `2xx`) erhalten. Weitere Informationen finden Sie im [Protokoll der Aktivitäten der Nachrichten]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#dev-console-troubleshooting). Protokolle, die älter als 60 Stunden sind, werden gelöscht und sind nicht mehr zugänglich; Webhook-Fehler werden mit einer Häufigkeit von bis zu 20 Protokollen pro Stunde erfasst. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Häufig gestellte Fragen

### Was bedeutet es, wenn eine Vorabprüfung fehlschlägt?

Eine „Vorabprüfung“ bezeichnet eine schnelle, gebündelte Validierungsprüfung, die zu Beginn einer Pipeline-Phase durchgeführt wird (z. B. beim Auslösen einer Nachricht oder beim Senden einer Canvas-Nachricht). Betrachten Sie es als einen vorzeitigen Ausstieg, der auf maximale Geschwindigkeit ausgelegt ist. Anstatt zahlreiche separate, ressourcenintensive Überprüfungen durchzuführen (wie beispielsweise die Validierung jedes einzelnen Details eines Nutzerprofils), fasst Braze mehrere grundlegende Validierungen in einem „ersten Durchgang“ zusammen.

Sollte eine Nutzer:in diese einzelne gebündelte Überprüfung nicht bestehen, wird sie unverzüglich abgelehnt. Dieser gebündelte Ansatz ermöglicht es Braze, große Mengen an Nachrichten mit hoher Geschwindigkeit zu verarbeiten und kann zu einer schnelleren und stabileren Performance Ihrer Kampagnen und Canvases beitragen, indem die Verarbeitungslatenz für jede Nachricht reduziert wird.

### Warum ist die Summe aus _„Total Aborts“_ und _„Message Sends“_ geringer als die von mir erwartete Zielgruppengröße?

Dafür kann es mehrere Gründe geben:

- **Zielgruppenkriterien:** Möglicherweise haben weniger Nutzer:innen als erwartet die Zielgruppenkriterien erfüllt (z. B. weil sie nicht zum Segment gehörten oder nicht über die erforderlichen Attribute verfügten), als die Kampagne oder Canvas gestartet wurde.
- **Verarbeitung läuft:** Nachrichten werden möglicherweise noch verarbeitet. Nutzer:innen befinden sich möglicherweise noch in früheren Schritten des Canvas und haben noch keine Nachrichtenschritte erreicht.
- **Aktualität der Daten:** Die Daten im Dashboard werden in etwa alle 15 Minuten aktualisiert, jedoch kann dies nicht garantiert werden. Die neuesten Daten für diese Kampagne oder Canvas sind möglicherweise noch nicht im Dashboard verfügbar.
- **Grenzfälle:** Es besteht eine geringe Wahrscheinlichkeit, dass Sie auf einen Sonderfall stoßen, der derzeit in diesem Dashboard nicht erfasst ist. Sollten Sie den Verdacht haben, dass dies der Fall ist, wenden Sie sich bitte an [den Braze-Support]({{site.baseurl}}/user_guide/administrative/access_braze/support).

### Warum ist die Summe aus _„Total Aborts“_ und _„Message Sends“_ größer als die Zielgruppe für eine Kampagne und Canvas?

Dies kann aus folgenden Gründen auftreten:

- **Mehrkanal-Nachrichten:** Die Kampagne oder der Canvas-Schritt wurde für den Versand über mehrere Kanäle (wie SMS und E-Mail) konfiguriert. Eine einzelne Nutzer:in kann für einen Kanal (z. B. E-Mail) das Ergebnis „gesendet“ und für einen anderen Kanal (z. B. „Nutzer:in nicht für SMS/MMS/RCS aktiviert“) das Ergebnis „abgebrochen“ erhalten. In diesem Fall würde diese eine Nutzer:in in dem Chart zweimal gezählt werden: einmal als „gesendet“ und einmal als „abgebrochen“.
  - **Beispiel:** Sie senden eine Push-Kampagne an 100 Nutzer:innen, die sowohl iOS als auch Android ansprechen sollen. Wenn eine Nutzer:in nur über ein iOS-Gerät verfügt, erhält sie die iOS-Push-Benachrichtigung („gesendet“), triggert jedoch gleichzeitig einen Abbruch für die Android-Push-Benachrichtigung („Nutzer:in nicht für Android-Push-Benachrichtigungen, App oder Gerät aktiviert“).
- **Mehrere Nachrichten-Schritte (nur Canvas):** Ihr Canvas kann in einem bestimmten Pfad mehrere Nachrichten-Schritte enthalten. Dieses Dashboard fasst alle Ergebnisse zusammen, sodass eine einzelne Nutzer:in mehrfach gezählt werden kann, wenn sie innerhalb des ausgewählten Zeitraums mehrere Schritte des Messaging-Prozesses durchläuft.
- **Testnachrichten:** Durch Test-Sendungen (die im Dashboard gezählt werden) wird die Gesamtzahl höher als die Größe der Zielgruppe. 
