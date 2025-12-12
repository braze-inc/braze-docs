---
nav_title: Opt-in &amp; Opt-out Schlüsselwörter
article_title: SMS Opt-In/Opt-Out Schlüsselwörter
page_order: 0
description: "Dieser Artikel beschreibt, wie Braze wichtige Keywords für Opt-In- und Opt-Out bei SMS-Nachrichten verarbeitet."
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# Schlüsselwörter für Opt-In und Opt-Out

> Die Vorschriften verlangen, dass es Antworten auf alle Opt-In-, Opt-Out- und Hilfe/Info-Schlüsselwortantworten gibt. Braze verarbeitet automatisch die folgenden _exakten Ein-Wort-Nachrichten, wobei Groß- und Kleinschreibung nicht berücksichtigt werden_. Dabei wird der [Status der Abonnementgruppe]({{site.baseurl}}/sms_rcs_subscription_groups/) für den Benutzer und die zugehörige Telefonnummer bei allen eingehenden Anfragen automatisch aktualisiert.

## Schlüsselwort-Übersicht

Braze verarbeitet die folgenden Schlüsselwörter automatisch und aktualisiert den Status der Abonnementgruppe für die Rufnummer bei allen eingehenden Anfragen. Beachten Sie, dass diese Standardschlüsselwörter und -antworten auch angepasst werden können. 

| Typ | Schlüsselwort | Ändern |
\|-|-------|---|
|Opt-In| `START`<br> `YES`<br> `UNSTOP` | Jede eingehende Anfrage mit einem dieser `Opt-In` Schlüsselwörter führt zu einer Änderung des Abonnementgruppenstatus auf `subscribed`. Außerdem kann der Pool der Absender, die mit dieser Abo-Gruppe verbunden sind, nun eine SMS, MMS oder RCS Nachricht an diese Kund:in senden (je nachdem, welche Art von Messaging die Absender unterstützen). <br><br>Der Benutzer erhält die von Ihnen definierte automatische Opt-In-Antwort.  |
|Opt-Out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Jede eingehende Anfrage mit einem dieser `Opt-Out` Schlüsselwörter führt zu einer Änderung des Abonnementgruppenstatus auf `unsubscribed`. Außerdem kann der Nummernpool, der mit dieser Abo-Gruppe verbunden ist, keine Nachrichten mehr an diese Kund:in senden.<br><br>Der Benutzer erhält die von Ihnen definierte automatische Opt-Out-Antwort. |
| Hilfe | `HELP`<br> `INFO` | Der Benutzer erhält die von Ihnen definierte automatische Hilfeantwort. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Es wird nur die **exakte Ein-Wort-Nachricht** verarbeitet (Groß- und Kleinschreibung wird nicht berücksichtigt). Schlüsselwörter wie `STOP PLEASE` werden ignoriert, es sei denn, [Fuzzy Opt-Out]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/) ist aktiviert.

Wenn ein Empfänger die Schlüsselwörter `HELP` oder `INFO` verwendet, wird automatisch eine Antwort ausgelöst. Die Standard-Antwort für diese automatischen Nachrichten wird während Ihres [Onboarding]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process) und der Beschaffung der Telefonnummer festgelegt. Beachten Sie, dass Sie die Antworten auch nach dem Onboarding ändern können.

{% alert tip %}
Möchten Sie die Opt-Out-Verarbeitung erweitern? Dann probieren Sie [Fuzzy Opt-Out]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/). Die Funktion versucht Opt-Out-Absichten zu erkennen, auch wenn eine eingehende Nachricht mit keinem Opt-Out-Schlüsselwort übereinstimmt.
{% endalert %}

