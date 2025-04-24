---
nav_title: Doppeltes Opt-in für SMS
article_title: Doppeltes Opt-in für SMS
description: "Dieser Referenzartikel befasst sich mit der SMS-Doppel-Opt-in-Funktion und erklärt, wie Sie die Funktion aktivieren, Opt-in-Schlüsselwörter und Antwortnachrichten auswählen und Benutzer in den SMS-Doppel-Opt-in-Workflow durch Abonnementaktualisierungen einbeziehen, die in der REST-API, im SDK und in den Aktualisierungen des Einstellungscenters erfolgen."
page_type: reference
page_order: 2
channel:
  - SMS
---

# Doppeltes Opt-in für SMS

> Mit dem Feature „Doppeltes Opt-In für SMS“ können Sie Nutzer:innen auffordern, ihre Opt-in-Absicht explizit zu bestätigen, bevor sie SMS-Nachrichten erhalten können. So können Sie sich auf die Nutzer konzentrieren, die sich wahrscheinlich mit SMS beschäftigen oder beschäftigt sind.

Wenn das SMS-Double-Opt-In aktiviert ist, erhalten die Nutzer eine SMS-Nachricht, in der sie um ihre ausdrückliche Zustimmung gebeten werden, bevor sie von Ihren Kampagnen oder Canvases angeschrieben werden können. 

Obwohl dies keine ausdrückliche Vorschrift des Telephone Consumer Protection Act von 1991 (TCPA) ist, empfiehlt Braze, dass Sie eine doppelte Zustimmung für SMS konfigurieren, um zu bestätigen, dass die Benutzer wissen, dass sie Teil Ihres SMS-Programms sind und damit einverstanden sind. Weitere Informationen zur SMS-Compliance finden Sie unter [SMS-Gesetze, -Vorschriften und -Missbrauchsprävention]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/).

## „Doppeltes Opt-in für SMS“-Workflows

Die Benutzer können ihre ausdrückliche Zustimmung durch ausgehende oder eingehende SMS-Nachrichten erteilen.

### Ausgehende SMS mit doppeltem Opt-in

Wenn ein:e Nutzer:in seine oder ihre Telefonnummer angibt, erhält er oder sie eine SMS-Nachricht, in der er oder sie um Zustimmung gebeten wird.

![Screenshot einer ausgehenden SMS-Nachricht mit der Marken-SMS „Willkommen bei den Marken-SMS-Updates! 1 Nachricht pro Woche mit den neuesten Angeboten. Antworten Sie mit „Y“, um sich anzumelden.“, die Benutzer antworten mit ‚Y‘ und die Marke antwortet mit „Danke!“ Sie haben sich jetzt für BRAND-Benachrichtigungen angemeldet. Hier ist ein Aktionscode SMS10 für 10 % Rabatt auf Ihren ersten Einkauf!"][2]{:style="max-width:40%;"}

### Eingehende SMS mit doppeltem Opt-in

Wenn ein:e Nutzer:in eine SMS-Nachricht sendet, die ein Opt-in-Keyword enthält, wird ihm eine SMS-Nachricht gesendet, in der er oder sie um seine Zustimmung gebeten wird.

![Screenshot einer eingehenden SMS-Nachricht, bei der ein:e Nutzer:in „Antworten Sie mit „J“, um zu bestätigen, dass Sie unserem SMS-Programm BEITRETEN möchten“ erhält. 3 Nachrichten/Woche, Text. Sie können jederzeit STOPP sagen, um aufzuhören, und dann mit „J“ antworten.][1]{:style="max-width:40%;"}

## SMS-Double-Opt-In aktivieren

Um das SMS-Double-Opt-In zu aktivieren, navigieren Sie zur Tabelle **SMS Global Keywords** in der entsprechenden Abonnementgruppe und klicken Sie auf **Bearbeiten** in der **Kategorie Opt-In Keyword**. Wählen Sie dann Ihre Opt-In-Methode**(Opt-In** oder **Double Opt-In**). Wenn Sie **Double Opt-In** wählen, wird die Seite erweitert und zeigt zusätzliche [konfigurierbare Felder](#configurable-fields) an.

![Im Bereich „Opt-in-Methode“ stehen Ihnen zwei Opt-in-Methoden zur Verfügung: Opt-in und Doppeltes Opt-in.][3]{:style="max-width:50%;"}

### Konfigurierbare Felder {#configurable-fields}

| Kategorie   |    Felder    | Beschreibung   
| ----------- |----------- |---------------- 
| Opt-in-Prompt | Keyword | Dies sind die Keywords, die ein:e Nutzer:in eingeben kann, um seine oder ihre Opt-in-Absicht anzuzeigen. `START` ist ein erforderliches Keyword. Diese Opt-in-Anfrage wird auch an den oder die Nutzer:in gesendet, wenn ihr Abo-Status von Quellen aktualisiert wird, die im Abschnitt [Abo-Quellen](#subscription-sources) aufgeführt sind.
| | Antwortnachricht | Dies ist die erste Antwort, die ein Nutzer erhält, nachdem er ein Opt-in-Schlüsselwort gesimst hat (z. B. "Antworten Sie Y, um zu bestätigen, dass Sie Nachrichten von dieser Nummer erhalten möchten. Msg&Data Gebühren können anfallen." )
| Doppelte Opt-in-Bestätigung | Keyword | Dies sind die Keywords, mit denen ein:e Nutzer:in seine oder ihre Opt-in-Absicht bestätigen kann. Mindestens ein Schlüsselwort ist erforderlich. Diese Schlüsselwörter sollten im Feld **Opt-In Prompt Reply Message** angegeben werden.
| | Antwortnachricht | Dies ist die Bestätigungsantwort, die ein:e Nutzer:in erhält, nachdem sein oder ihre Opt-in ausdrücklich bestätigt wurde und er oder sie nun per SMS benachrichtigt werden kann. Der Status der Abonnementgruppe des Benutzers wird auf `Subscribed` gesetzt.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Wenn ein:e Nutzer:in eine Opt-in-Anfrage erhält, hat er 30 Tage Zeit, seine Opt-in-Absicht zu bestätigen. Wenn ein:e Nutzer:in nach dem 30-Tage-Fenster ein Abonnement abschließen möchte, muss er oder sie ein Opt-in-Keyword eingeben, um den Workflow „Doppeltes Opt-in“ erneut zu starten.

![Die konfigurierbaren Felder haben zwei Abschnitte, Opt-in-Anfrage und „Doppeltes Opt-in“-Bestätigung, jeweils mit den Feldern „Keywords“ und „Antwortnachricht“.][4]

## Status der Abonnementgruppe

Erst wenn der Benutzer den SMS-Double-Opt-In-Workflow abgeschlossen hat, wird der [Status]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) seiner [Abonnementgruppe]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) auf `Subscribed` aktualisiert. Wenn der Benutzer den Workflow beginnt, ihn aber nicht abschließt, bleibt er `Unsubscribed` und kann keine SMS-Nachrichten von dieser Abonnementgruppe erhalten.

Nutzer:in können auch in den Workflow „Doppeltes Opt-in für SMS“ aufgenommen werden, wenn sie [von anderen Quellen abonniert werden]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (z.B. REST API, SDK).

## Abo-Quellen {#subscription-sources}

Nutzer:innen können auch über Abo-Updates, die außerhalb eingehender SMS-Nachrichten erfolgen, in den Workflow „Doppeltes Opt-in für SMS“ aufzurufen. Zu diesen Quellen gehören Updates von der REST API, dem SDK und dem Präferenzzentrum. Wenn ein:e Nutzer:in über diese Quellen den Workflow „Doppeltes Opt-in für SMS“ aufruft, erhält er oder sie die **Opt-in-Anfrage-Antwortnachricht**.

Jede Abo-Quelle hat ein anderes Anmeldeverhalten, wie in der folgenden Tabelle beschrieben.

Quelle    | Anmeldeverhalten bei doppeltem Opt-in   
----------- | -----------
SDK | Nutzer:innen werden automatisch in den Workflow „Doppeltes Opt-in für SMS“ aufgenommen, wenn sie sich über das Braze-SDK anmelden.
REST API | Nutzer:innen können in den Workflow aufgenommen werden, wenn der Abo-Status über `/subscription/status/set`, `/v2/subscription/status/set` oder `/users/track` gesetzt wird und der optionale Parameter `use_double_opt_in_logic` als `true` übergeben wird (zum Beispiel [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). Wenn Sie diesen Parameter nicht angeben, werden die Nutzer:innen nicht in den Workflow „Doppeltes Opt-in für SMS“ aufgenommen.
Shopify | Nutzer:innen werden nicht in den Workflow „Doppeltes Opt-in für SMS“ aufgenommen, wenn ihr Abo-Status von unserer Shopify-Integration gesetzt wird.
Nutzerimport | Nutzer:innen werden nicht in den Workflow „Doppeltes Opt-in für SMS“ aufgenommen, wenn ihr Abo-Status durch Nutzerimport gesetzt wird.
[Präferenzzentrum]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | Nutzer:in werden automatisch in den Workflow „Doppeltes Opt-in für SMS“ aufgenommen, wenn sie sich über ein Präferenzzentrum angemeldet haben.
Nutzeraktualisierungs-Schritt | Nutzer:innen können in den Workflow „Doppeltes Opt-in für SMS“ aufgenommen werden, wenn ihr Abo-Status über den Schritt „Nutzeraktualisierung“ gesetzt wird und der optionale Parameter `use_double_opt_in_logic` als `true` übergeben wird. Wenn Sie diesen Parameter nicht angeben, werden die Nutzer:innen nicht in den Workflow „Doppeltes Opt-in für SMS“ aufgenommen.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Unterstützung mehrerer Sprachen
Für eingehende Nachrichten wird SMS-Double-Opt-In für alle in der Abonnementgruppe definierten Sprachen unterstützt. Das bedeutet, dass Sie Ihre Auto-Responses in verschiedenen Sprachen definieren können und Braze die Auto-Response sendet, die mit einer bestimmten Sprache verbunden ist, wenn ein passendes Schlüsselwort empfangen wird.

Nutzer:innen, die in den Workflow „Doppeltes Opt-in für SMS“ durch Updates von Abos einsteigen, die außerhalb eingehender Nachrichten erfolgen (z. B. SDK, REST API, Shopify), erhalten nur die englischen Keywords.

[1]: {% image_buster /assets/img/double_opt_in_inbound.png %}
[2]: {% image_buster /assets/img/double_opt_in_outbound.png %}
[3]: {% image_buster /assets/img/double_opt_in_method.png %}
[4]: {% image_buster /assets/img/double_opt_in_fields.png %}
