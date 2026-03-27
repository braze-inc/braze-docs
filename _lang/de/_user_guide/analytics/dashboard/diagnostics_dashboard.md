---
nav_title: Diagnose-Dashboard für Messaging
article_title: Diagnose-Dashboard für Messaging
description: "Dieser Referenzartikel behandelt das Dashboard für die Nachrichten-Diagnose, das Ihnen dabei hilft, zu verstehen, warum Nachrichten aus Ihren Kampagnen oder Canvases möglicherweise nicht wie erwartet versendet wurden."
alias: /ccdd/
page_order: 4.5
toc_headers: h2
---

# Diagnose-Dashboard für Messaging

> Das Dashboard **„Messaging Diagnostics"** bietet eine detaillierte Aufschlüsselung der Ergebnisse des Nachrichtenversands, sodass Sie Trends erkennen und potenzielle Probleme in Ihrer Messaging-Konfiguration diagnostizieren können. Dieses Dashboard kann Ihnen dabei helfen, zu verstehen, warum Nachrichten aus Ihren Kampagnen oder Canvases möglicherweise nicht wie erwartet versendet wurden.

{% alert important %}
Das Dashboard **„Messaging Diagnostics"** befindet sich derzeit in der Early-Access-Phase. Wenden Sie sich an Ihren Customer-Success-Manager, wenn Sie an einer Teilnahme am Early Access interessiert sind.
{% endalert %}

## Wichtige Konzepte

### Gesendet und zugestellt

Es ist wichtig zu verstehen, dass dieses Dashboard darüber berichtet, wie Braze eine Nachricht intern verarbeitet hat – und nicht über den endgültigen Zustellstatus der Nachricht.

Eine Nachricht, die in diesem Dashboard als „gesendet" markiert ist, bedeutet, dass Braze die Nachricht erfolgreich verarbeitet und versendet hat. Für die meisten Kanäle bedeutet dies, dass Braze die Nachricht an den entsprechenden externen Versandpartner weitergeleitet hat. Es wird jedoch keine Garantie für die endgültige Zustellung an das Gerät der Nutzer:innen übernommen. 

Wenn Braze eine Nachricht „versendet", kann die endgültige Zustellung von externen Diensten abhängen. Beachten Sie die folgenden Beispiele für jeden Kanal.

| Kanal | Beispiel für die endgültige Zustellung |
| --- | --- |
| Content-Cards | Die Karte wurde versendet und kann eingesehen werden. |
| E-Mail | Braze übermittelt die Nachricht an einen E-Mail-Anbieter (ESP). Der ESP ist dann für die endgültige Zustellung verantwortlich. Dieser ESP kann beispielsweise einen „Bounce" (Absprung) melden, wenn die E-Mail-Adresse ungültig ist oder der Posteingang voll ist. |
| In-App-Nachrichten | Die Nachricht wurde den Nutzer:innen angezeigt. |
| LINE | Die Nachricht wurde erfolgreich an einen Versandpartner übergeben. |
| Push | Braze übermittelt die Nachricht an den entsprechenden Dienst für Push-Benachrichtigungen (wie beispielsweise den Apple Push Notification Service für iOS oder Firebase Cloud Messaging für Android). Dieser Dienst ist für die endgültige Zustellung der Benachrichtigung an das Gerät verantwortlich. |
| SMS/MMS/RCS | Braze übermittelt die Nachricht an ein SMS-Gateway (wie Twilio). Dieses Gateway ist für die endgültige Zustellung an den Mobilfunkanbieter verantwortlich. |
| Webhooks | Die Webhook-Anfrage wurde erfolgreich durchgeführt und hat eine `2xx`-Antwort zurückgegeben. |
| WhatsApp | Die Nachricht wurde erfolgreich an einen Versandpartner übergeben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

### Aktualität der Daten

Die Häufigkeit, mit der die Daten in diesem Dashboard aktualisiert werden, kann je nach Systemauslastung schwanken. Die Aktualisierungshäufigkeit kann nicht garantiert werden, liegt jedoch in den meisten Fällen bei unter einer Stunde.

## Konfiguration des Dashboards

Sie können auf das Diagnose-Dashboard zugreifen, indem Sie zu **Analytics** > **Dashboard Builder** navigieren und **Messaging Diagnostics** aus der Liste der von Braze erstellten Dashboards auswählen.

Um das Dashboard auszuführen und Ihre Daten anzuzeigen:

1. Wählen Sie entweder **Kampagnen** oder **Canvase** als Quelle für Ihre Dashboard-Berichte aus. 
2. Wählen Sie eine oder mehrere Kampagnen oder Canvase aus.
3. Wählen Sie **Dashboard ausführen**, um die Daten für die von Ihnen ausgewählten Filter zu laden.

![Beispiel für eine Kampagnen- und Canvas-Diagnose vom 25. bis 31. Mai 2025 für eine Willkommensserie-Kampagne.]({% image_buster /assets/img/campaign_canvas_dashboard_example.png %}){: style="max-width:90%;"}

## Interpretation der Daten

{% alert note %}
Das Dashboard zeigt nur die Daten der letzten 7 Tage an. 
{% endalert %}

### Zusammenfassungskacheln

Am oberen Rand der Seite befinden sich wichtige Zusammenfassungskacheln für den ausgewählten Zeitraum, die Folgendes anzeigen:

- **Gesamtzahl der Abbrüche:** Die Gesamtzahl der Nachrichten, die abgebrochen wurden. Dies schließt Canvas-Zielgruppenmitglieder ein, die das Canvas nicht betreten oder das Canvas verlassen haben, weil bei einem Schritt ein Fehler aufgetreten ist oder sie die Ausstiegskriterien erfüllt haben, während sie ein Ausstiegsereignis ausgeführt haben.
- **Nachrichtenversand:** Die Gesamtzahl der Nachrichten, die Braze erfolgreich verarbeitet und versendet hat. 
  - **E-Mail, SMS/MMS/RCS, WhatsApp, LINE und Push:** Die Nachricht wurde erfolgreich an einen Versandpartner übergeben.  
  - **Webhooks:** Die Webhook-Anfrage wurde erfolgreich durchgeführt und hat eine `2xx`-Antwort zurückgegeben.  
  - **Content-Cards:** Die Karte wurde versendet und kann eingesehen werden.    
  - **In-App-Nachrichten:** Die Nachricht wurde den Nutzer:innen angezeigt.

### Nachrichtenergebnisse im Zeitverlauf

Dieses Zeitreihen-Chart zeigt eine tägliche Aufschlüsselung der verschiedenen Gründe, aus denen eine Nachricht abgebrochen oder Nutzer:innen aus einem Canvas entfernt wurden. Dieses Chart zeigt nicht die Anzahl der Sendungen an.  

{% alert note %}
Um die Übersichtlichkeit des Charts zu gewährleisten, werden Abbruch- oder Entfernungsgründe mit null Vorkommen im ausgewählten Zeitraum nicht im Chart angezeigt.
{% endalert %}

### Aufschlüsselung der Nachrichtenergebnisse

Dieses Chart zeigt die Aufschlüsselung aller Nachrichtenergebnisse innerhalb des ausgewählten Zeitraums. Es bietet einen umfassenden Überblick über:
- Die Gesamtzahl der Sendungen als Anteil aller Ergebnisse.  
- Die proportionale Aufschlüsselung der einzelnen Abbruch- und Entfernungsgründe. So können Sie schnell die häufigsten Gründe identifizieren, warum Nachrichten nicht gesendet werden.

### Abbruch-Ergebnisse

Die folgenden Definitionen erläutern die im Dashboard angezeigten Abbruch-Ergebnisse. Die Ergebnisse sind nach Kategorien gruppiert, um die Suche nach dem gewünschten Ergebnis zu erleichtern.

#### Inhalt und Darstellung

| Abbruch-Ergebnis | Erklärung |
| ---- | ---- |
| Content-Card abgelaufen | Die Content-Card ist abgelaufen, bevor die Nutzer:innen sie sehen konnten. |
| Content-Card ungültig | Die Content-Card wies Fehler auf und wurde nicht an die Nutzer:innen gesendet. Einige häufige Gründe hierfür sind: {::nomarkdown}<ul><li> Die maximale Größe wurde überschritten (2 KB). </li><li> Das Ablaufdatum ist ungültig. </li><li> Die Nachricht enthält ungültige Zeichen. </li></ul>{:/} |
| Connected-Content fehlgeschlagen | Braze hat versucht, die Nachricht zu senden, jedoch ist Connected-Content nach Erreichen der maximalen Anzahl an Wiederholungsversuchen (Standardwert ist fünf) fehlgeschlagen. **Hinweis:** Diese Zahl gibt die Anzahl der Nachrichten an, die aufgrund des Erreichens der maximalen Wiederholungsversuche abgebrochen wurden, nicht die Gesamtzahl der fehlgeschlagenen Connected-Content-Anfragen. |
| Zeitüberschreitung beim Rendern von In-App-Nachrichten | Nach mehreren Wiederholungsversuchen konnte Liquid nicht gerendert werden und es kam zu einer Zeitüberschreitung. |
| Liquid-Abbruch | Der [abort_message]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages)-Liquid-Tag wurde aufgerufen, daher wurde der Versand abgebrochen. |
| Zeitüberschreitung beim Liquid-Rendering | Das Rendern des Liquid-Templates hat zu lange gedauert. Tritt am häufigsten bei Bannern, In-App-Nachrichten und E-Mails auf. |
| Liquid-Syntaxfehler | Das Liquid-Template wies einen Parsing-Fehler auf, daher wurde die Nachricht abgebrochen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Kampagnen- und Canvas-Status

| Abbruch-Ergebnis | Erklärung |
| ---- | ---- |
| Verzögerungsschritt fehlgeschlagen | Der [Verzögerungsschritt]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) ist fehlgeschlagen, was dazu führte, dass die Nutzer:innen das Canvas verlassen mussten. Dieser Fehler kann auftreten, wenn: {::nomarkdown}<ul><li> Die Variable, die dem personalisierten Verzögerungsschritt übergeben wurde, leer war oder einen ungültigen Typ hatte. </li><li> Die Verzögerung die maximal zulässige Dauer innerhalb des Canvas überschreitet.</li></ul>{:/} |
| Ausnahme-Event oder Ausstiegsereignis | Die Nutzer:innen waren zuvor berechtigt, die Nachricht zu empfangen, haben jedoch entweder {::nomarkdown}<ul><li> ein <a href="/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-3-select-exception-events">Ausnahme-Event</a> für eine aktionsbasierte Kampagne ausgeführt, sodass die Nachricht abgebrochen wurde, oder </li><li> die Canvas-<a href="/docs/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#setting-up-exit-criteria">Ausstiegskriterien</a> erfüllt, sodass sie während der Journey ausgeschlossen wurden.</li></ul>{:/} |
| Inaktive Kampagne | Die Kampagne wurde gestoppt, während die Nachricht noch in der Übermittlung war, und daher abgebrochen. |
| Inaktives Canvas | Das Canvas wurde beendet, bevor die Nutzer:innen die Journey begonnen haben. |
| Inaktiver Canvas-Schritt | Dies kann im Canvas auftreten, wenn: {::nomarkdown}<ul><li> Der Canvas-Schritt gelöscht wurde. </li> <li>Das Canvas angehalten wurde, wodurch alle Schritte inaktiv werden. </li></ul>{:/} |
| Volumenlimit erreicht | Die Kampagne hat das festgelegte Volumenlimit erreicht, daher wurde der Versand abgebrochen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Rate-Limiting und Zeitsteuerung

| Abbruch-Ergebnis | Erklärung |
| ---- | ---- |
| Frequency-Capping | Die Nutzer:innen haben bereits die maximale Anzahl an Nachrichten erhalten, die gemäß den [Frequency-Capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-frequency-capping)-Regeln Ihres Workspaces zulässig ist, daher wurde der Versand abgebrochen. |
| Ruhezeiten-Abbruch | Für die Kampagne oder den Canvas-Schritt waren Ruhezeiten aktiviert, wobei als Fallback **Nachricht abbrechen** festgelegt war. Die Nutzer:innen haben die Kampagne während der Ruhezeiten getriggert oder den Canvas-Nachrichtenschritt aufgerufen, sodass die Nachricht abgebrochen wurde. Dies führt jedoch nicht dazu, dass die Nutzer:innen das Canvas verlassen. |
| Rate-Limiting über 72 Stunden | Die Nachricht wurde aufgrund von [Rate-Limits bei der Zustellgeschwindigkeit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) länger als 72 Stunden zurückgehalten, sodass der Versand abgebrochen wurde. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Teilnahmeberechtigung und Nutzerprofil

| Abbruch-Ergebnis | Erklärung |
| ---- | ---- |
| Doppelter Nutzerbezeichner | Mehrere Nutzer:innen mit einem übereinstimmenden Bezeichner (z. B. externe ID, E-Mail-Adresse, Telefonnummer) waren berechtigt, diese Nachricht zu erhalten. Um doppelte Sendungen an dieselben Nutzer:innen zu vermeiden, wurde diese Nachricht abgebrochen. |
| Nutzer:in hat die Vorabprüfung für den Nachrichtenschritt nicht bestanden | Diese Vorabprüfung wird vor den Zustellvalidierungen durchgeführt. In diesem Fall haben die Nutzer:innen die grundlegende Vorabprüfung für diesen Nachrichtenschritt nicht bestanden (Nutzer:in nicht gefunden oder für den Kanal des Nachrichtenschritts nicht berechtigt). **Hinweis:** Bei einem Mehrkanal-Nachrichtenschritt bedeutet dies, dass die Nutzer:innen nicht gefunden wurden; die Kanalberechtigung wird hier nur für Einzelkanal-Nachrichtenschritte überprüft. |
| Nutzer:in hat die Vorabprüfung für die getriggerte Nachricht nicht bestanden | Bei einer getriggerten Nachricht führt Braze zunächst eine Reihe grundlegender Vorabprüfungen hinsichtlich der Zielgruppenberechtigung, der erneuten Berechtigung und der Kanalberechtigung durch, bevor eine Nachricht erstellt wird, die aufgrund dieses Triggers versendet wird. |
| Nutzer:in ist nicht mehr berechtigt | Die Nutzer:innen gehörten ursprünglich zur Zielgruppe, entsprachen jedoch nicht mehr den Zielgruppenkriterien, bevor Braze die Nachricht versandte oder die Nutzer:innen in das Canvas eintrug. Der Zeitraum zwischen dem erstmaligen Erfüllen der Zielgruppenkriterien und dem Herausfallen aus der Zielgruppe kann auf Verzögerungen durch folgende Faktoren zurückzuführen sein: {::nomarkdown}<ul><li>Intelligentes Timing</li><li>Ruhezeiten</li><li>Ortszeit</li><li>Rate-Limits für die Zustellgeschwindigkeit (gilt nicht für Canvas-Eintritte)</li><li>Verzögerungen in der Messaging-Pipeline</li></ul>{:/} |
| Nutzer:in ist nicht für diesen Schritt berechtigt | Die Nutzer:innen haben das Canvas verlassen, weil sie die festgelegten [Zustellvalidierungen]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#delivery-validations) für den Nachrichtenschritt nicht erfüllt haben oder weil sie Teil einer [Unterdrückungsliste]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) waren. |
| Nutzer:in ist nicht erneut berechtigt | Die Nutzer:innen waren berechtigt, die Nachricht zu empfangen oder das Canvas aufzurufen, jedoch wurde der Versand aufgrund von Einstellungen zur erneuten Berechtigung oder zum erneuten Eintritt abgebrochen. Dies kann auftreten, wenn die Nutzer:innen die Kampagne bereits erhalten haben oder das Canvas erst kürzlich aufgerufen haben, wenn für diese Nutzer:innen bereits eine weitere Sendung für dieselbe Kampagne läuft oder wenn die erneute Berechtigung oder der erneute Eintritt deaktiviert ist. |
| Nutzerprofil nicht gefunden | Die Nutzer:innen haben entweder nie existiert oder sind nicht mehr in Braze vorhanden. Einige häufige Fälle sind: {::nomarkdown}<ul><li> Die Nutzer:innen wurden über API-Messaging angesprochen, waren jedoch nie in Braze registriert. </li><li>Die Nutzer:innen wurden gelöscht, bevor die Nachricht gesendet oder der Canvas-Schritt ausgeführt wurde. </li><li>Die Nutzer:innen wurden vor dem Senden der Nachricht mit einem anderen Profil zusammengeführt.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Kanal und Zustellung

| Abbruch-Ergebnis | Erklärung |
| ---- | ---- |
| Zeitüberschreitung bei der Partnerzustellung | Braze hat 24 Stunden lang versucht, diese Nachricht an Ihren Zustellpartner zu senden, jedoch hat der Partner während des gesamten Zeitfensters temporäre Fehler zurückgegeben. |
| Push-Zugangsdaten ungültig | Die [Push-Zugangsdaten]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting/#valid-push-token) für diese App fehlen oder sind ungültig, daher wurde der Versand abgebrochen. Aktualisieren Sie Ihre Zugangsdaten in den **App-Einstellungen**. |
| Nutzer:in ist nicht für Android-Push, App oder Gerät aktiviert | Es ist nicht möglich, eine Push-Benachrichtigung an diese Nutzer:innen zu senden. Einige häufige Gründe: {::nomarkdown}<ul><li> Die Nutzer:innen haben die App nicht installiert.</li> <li> Die Nutzer:innen verfügen nicht über ein gültiges Push-Token. </li> <li>Die Nutzer:innen verfügen nicht über das erforderliche Gerät für diese Push-Benachrichtigung. </li> <li> Die Nutzer:innen haben die Benachrichtigungen für diese App in ihren Geräteeinstellungen deaktiviert. </li> <li> Die Nutzer:innen haben sich nicht für den Empfang von Push-Benachrichtigungen angemeldet oder diese aktiviert.</li></ul>{:/} |
| Nutzer:in ist nicht für iOS-Push, App oder Gerät aktiviert | Entspricht dem Abbruch-Ergebnis „Nutzer:in nicht für Android-Push, App oder Gerät aktiviert". |
| Nutzer:in ist nicht für Kindle-Push, App oder Gerät aktiviert | Entspricht dem Abbruch-Ergebnis „Nutzer:in nicht für Android-Push, App oder Gerät aktiviert". |
| Nutzer:in ist nicht für Web-Push, App oder Gerät aktiviert | Entspricht dem Abbruch-Ergebnis „Nutzer:in nicht für Android-Push, App oder Gerät aktiviert". |
| Nutzer:in ist nicht für Content-Cards aktiviert | Die Nutzer:innen haben keine Apps verwendet, die diese Content-Card enthalten. |
| Nutzer:in ist nicht für E-Mail aktiviert | An diese Nutzer:innen können keine E-Mails gesendet werden. Einige häufige Gründe: {::nomarkdown}<ul><li> Die Nutzer:innen haben keine E-Mail-Adresse in ihrem Nutzerprofil hinterlegt. </li><li> Der Abo-Status der Nutzer:innen schließt sie vom Erhalt dieser E-Mail aus. </li><li> Die E-Mail-Adresse der Nutzer:innen wurde zuvor als ungültig markiert (Hard Bounce). </li><li> Nachrichten an diese E-Mail-Adresse werden durchweg als Spam markiert, daher wurde der Versand abgebrochen.</li></ul>{:/} |
| Nutzer:in ist nicht für LINE aktiviert | Es ist nicht möglich, LINE-Nachrichten an diese Nutzer:innen zu senden. Einige häufige Gründe: {::nomarkdown}<ul><li> Die Nutzer:innen haben keine Telefonnummer in ihrem Nutzerprofil hinterlegt. </li><li> Die Telefonnummer der Nutzer:innen wurde aufgrund von Zustellfehlern als ungültig markiert. </li><li> Der Abo-Status der Nutzer:innen schließt sie vom Erhalt dieser Nachricht aus. </li><li> Die Nutzer:innen verfügen nicht über eine LINE-ID.</li></ul>{:/} |
| Nutzer:in ist nicht für SMS/MMS/RCS aktiviert | Es können keine SMS-Nachrichten an diese Nutzer:innen gesendet werden. Einige häufige Gründe: {::nomarkdown}<ul><li> Die Nutzer:innen haben keine Telefonnummer in ihrem Nutzerprofil hinterlegt. </li><li> Die Telefonnummer der Nutzer:innen wurde aufgrund von Zustellfehlern als ungültig markiert. </li><li> Die Telefonnummer der Nutzer:innen hat kein gültiges E.164-Format, und Versuche, die Nummer automatisch zu formatieren, sind fehlgeschlagen. </li><li> Der Abo-Status der Nutzer:innen schließt sie vom Empfang der SMS-Nachricht aus.</li><li>Die Telefonnummer der Nutzer:innen befindet sich in einem gesperrten Land.</li></ul>{:/} |
| Nutzer:in ist nicht für WhatsApp aktiviert | Es ist nicht möglich, WhatsApp-Nachrichten an diese Nutzer:innen zu senden. Einige häufige Gründe: {::nomarkdown}<ul><li> Die Nutzer:innen haben keine Telefonnummer in ihrem Nutzerprofil hinterlegt. </li><li> Die Telefonnummer der Nutzer:innen wurde aufgrund von Zustellfehlern als ungültig markiert. </li><li> Der Abo-Status der Nutzer:innen schließt sie vom Erhalt dieser Nachricht aus. </li><li> Die Nutzer:innen verfügen nicht über ein WhatsApp-Konto.</li></ul>{:/} |
| Webhook fehlgeschlagen | Der Webhook hat einen nicht erfolgreichen Antwortcode (nicht `2xx`) erhalten. Weitere Informationen finden Sie im [Nachrichtenaktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#dev-console-troubleshooting). Protokolle, die älter als 60 Stunden sind, werden gelöscht und sind nicht mehr zugänglich; Webhook-Fehler werden mit bis zu 20 Protokolleinträgen pro Stunde erfasst. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Häufig gestellte Fragen

### Was bedeutet es, wenn eine „Vorabprüfung" fehlschlägt?

Eine „Vorabprüfung" bezeichnet eine schnelle, gebündelte Validierungsprüfung, die ganz zu Beginn einer Pipeline-Phase durchgeführt wird (z. B. beim Triggern einer Nachricht oder beim Senden eines Canvas-Nachrichtenschritts). Stellen Sie es sich als einen vorzeitigen Ausstieg vor, der auf maximale Geschwindigkeit ausgelegt ist. Anstatt zahlreiche separate, ressourcenintensive Überprüfungen durchzuführen (wie beispielsweise die Validierung jedes einzelnen Details eines Nutzerprofils), fasst Braze mehrere grundlegende Validierungen in einem „ersten Durchgang" zusammen.

Wenn Nutzer:innen diese gebündelte Überprüfung nicht bestehen, werden sie sofort abgelehnt. Dieser gebündelte Ansatz ermöglicht es Braze, große Mengen an Nachrichten mit hoher Geschwindigkeit zu verarbeiten, und kann zu einer schnelleren und stabileren Performance Ihrer Kampagnen und Canvase beitragen, indem die Verarbeitungslatenz für jede Nachricht reduziert wird.

### Was bedeutet ein „sonstiges" Abbruch-Ergebnis?

Hierbei handelt es sich um Abbrüche, die keiner der bestehenden Braze-Kategorien zugeordnet werden konnten. Wenn Sie einen großen Anteil an Abbrüchen mit diesem Ergebnis feststellen, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administrative/access_braze/support) für weitere Unterstützung.

### Warum ist die Summe aus _Gesamtzahl der Abbrüche_ und _Nachrichtenversand_ geringer als die erwartete Zielgruppengröße?

Dafür kann es mehrere Gründe geben:

- **Zielgruppenkriterien:** Möglicherweise haben weniger Nutzer:innen als erwartet die Zielgruppenkriterien erfüllt (z. B. weil sie nicht zum Segment gehörten oder nicht über die erforderlichen Attribute verfügten), als die Kampagne oder das Canvas gestartet wurde.
- **Verarbeitung läuft:** Nachrichten werden möglicherweise noch aktiv verarbeitet. Nutzer:innen befinden sich möglicherweise noch in früheren Schritten des Canvas und haben noch keine Nachrichtenschritte erreicht.
- **Aktualität der Daten:** Die Daten im Dashboard werden etwa alle 15 Minuten aktualisiert, dies kann jedoch nicht garantiert werden. Die neuesten Daten für diese Kampagne oder dieses Canvas sind möglicherweise noch nicht im Dashboard verfügbar.
- **Grenzfälle:** Es besteht eine geringe Wahrscheinlichkeit, dass Sie auf einen Sonderfall stoßen, der derzeit in diesem Dashboard nicht erfasst ist. Sollten Sie den Verdacht haben, dass dies der Fall ist, wenden Sie sich an den [Braze-Support]({{site.baseurl}}/user_guide/administrative/access_braze/support).

### Warum ist die Summe aus _Gesamtzahl der Abbrüche_ und _Nachrichtenversand_ größer als die Zielgruppe einer Kampagne oder eines Canvas?

Dies kann aus folgenden Gründen auftreten:

- **Mehrkanal-Nachrichten:** Die Kampagne oder der Canvas-Schritt wurde für den Versand über mehrere Kanäle konfiguriert (z. B. SMS und E-Mail). Einzelne Nutzer:innen können für einen Kanal (z. B. E-Mail) das Ergebnis „gesendet" und für einen anderen Kanal (z. B. „Nutzer:in nicht für SMS/MMS/RCS aktiviert") das Ergebnis „abgebrochen" erhalten. In diesem Fall würden diese Nutzer:innen im Chart zweimal gezählt: einmal als „gesendet" und einmal als „abgebrochen".
  - **Beispiel:** Sie senden eine Push-Kampagne an 100 Nutzer:innen und sprechen dabei sowohl iOS als auch Android an. Wenn Nutzer:innen nur über ein iOS-Gerät verfügen, erhalten sie die iOS-Push-Benachrichtigung („gesendet"), triggern jedoch gleichzeitig einen Abbruch für die Android-Push-Benachrichtigung („Nutzer:in nicht für Android-Push, App oder Gerät aktiviert").
- **Mehrere Nachrichtenschritte (nur Canvas):** Ihr Canvas kann in einem bestimmten Pfad mehrere Nachrichtenschritte enthalten. Dieses Dashboard fasst alle Ergebnisse zusammen, sodass einzelne Nutzer:innen mehrfach gezählt werden können, wenn sie innerhalb des ausgewählten Zeitraums mehrere Nachrichtenschritte durchlaufen.
- **Testnachrichten:** Durch Testsendungen (die im Dashboard mitgezählt werden) kann die Gesamtzahl höher ausfallen als die Zielgruppengröße.