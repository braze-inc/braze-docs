---
nav_title: Doppeltes Opt-in
article_title: Doppeltes Opt-In
description: "Dieser Artikel referenziert das Double Opt-in Feature und erklärt, wie Sie das Feature aktivieren, Opt-in-Schlüsselwörter und Antwortnachrichten auswählen und Nutzer:innen in den Double Opt-in-Workflow durch Abo-Updates einbeziehen, die in REST API, SDK und Preference Center Updates vorkommen."
page_type: reference
page_order: 2
channel:
  - SMS
  - MMS
  - RCS
---

# Doppeltes Opt-in

> Mit dem Double Opt-in Feature können Sie Nutzer:innen auffordern, ihre Opt-in Absicht explizit zu bestätigen, bevor sie SMS-, MMS- oder RCS-Nachrichten erhalten können. Auf diese Weise können Sie sich auf Nutzer:innen konzentrieren, die sich wahrscheinlich auf dem Kanal engagieren oder engagiert sind, und bewährte Verfahren zur Einhaltung von Richtlinien befolgen.

Wenn Double Opt-in aktiviert ist, erhalten Nutzer:innen eine Nachricht, in der sie um ihre ausdrückliche Zustimmung gebeten werden, bevor sie von Ihren Kampagnen oder Canvase Nachrichten erhalten können. 

Obwohl dies keine ausdrückliche Vorschrift des Telephone Consumer Protection Act von 1991 (TCPA) ist, empfiehlt Braze, ein Double Opt-in zu konfigurieren, um zu bestätigen, dass die Nutzer:innen wissen und zustimmen, an Ihrem SMS-, MMS- oder RCS-Programm teilzunehmen. Weitere Informationen zur Einhaltung von Gesetzen finden Sie unter [Gesetze, Vorschriften und Missbrauchsverhinderung für SMS, MMS und RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

## Double Opt-in Arbeitsabläufe

Mit Double Opt-in können Sie durch eingehende und ausgehende Opt-in Kampagnen eine ausdrückliche Zustimmung erhalten.

### Ausgehend

Wenn ein Nutzer:innen seine Telefonnummer angibt, erhält er eine Nachricht, in der er um seine Zustimmung gebeten wird.

![Screenshot einer ausgehenden SMS Nachricht mit dem Markentext "Willkommen bei BRAND text updates! 1 Nachricht pro Woche mit den neuesten Angeboten. Antworten Sie mit „Y“, um sich anzumelden.“, die Benutzer antworten mit ‚Y‘ und die Marke antwortet mit „Danke!“ Sie haben sich jetzt für BRAND-Benachrichtigungen angemeldet. Hier ist ein Aktionscode SMS10 für 10 % Rabatt auf Ihren ersten Einkauf!"]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### Eingehend

Wenn ein Nutzer:innen eine Nachricht sendet, die ein Opt-in-Schlüsselwort enthält, erhält er eine Nachricht, in der er um seine Zustimmung gebeten wird.

![Screenshot einer eingehenden SMS Nachricht, in der ein Nutzer:in "JOIN" sendet und die Antwort "Antworten Sie mit Y, um zu bestätigen, dass Sie an unserem SMS Programm teilnehmen möchten. 3 Nachrichten/Woche, Text. Sie können jederzeit STOPP sagen, um aufzuhören, und dann mit „J“ antworten.]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Enablement des doppelten Opt-in

Um das Double Opt-in zu aktivieren, gehen Sie zur Tabelle **Globale Schlüsselwörter** in der entsprechenden Abo-Gruppe und klicken Sie in der **Kategorie Opt-in-Schlüsselwort** auf **Bearbeiten**. Wählen Sie dann Ihre Opt-In-Methode**(Opt-In** oder **Double Opt-In**). Wenn Sie **Double Opt-In** wählen, wird die Seite erweitert und zeigt zusätzliche [konfigurierbare Felder](#configurable-fields) an.

![Im Bereich Opt-in-Methode stehen Ihnen zwei Opt-in-Methoden zur Verfügung: Opt-in und Doppeltes Opt-in.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Konfigurierbare Felder {#configurable-fields}

| Kategorie   |    Felder    | Beschreibung   
| ----------- |----------- |---------------- 
| Opt-in-Prompt | Keyword | Dies sind die Keywords, die ein:e Nutzer:in eingeben kann, um seine oder ihre Opt-in-Absicht anzuzeigen. `START` ist ein erforderliches Keyword. Diese Opt-in-Anfrage wird auch an den oder die Nutzer:in gesendet, wenn ihr Abo-Status von Quellen aktualisiert wird, die im Abschnitt [Abo-Quellen](#subscription-sources) aufgeführt sind.
| | Antwortnachricht | Dies ist die erste Antwort, die ein Nutzer erhält, nachdem er ein Opt-in-Schlüsselwort gesimst hat (z. B. "Antworten Sie Y, um zu bestätigen, dass Sie Nachrichten von dieser Nummer erhalten möchten. Msg&Data Es können Gebühren anfallen." )
| Doppelte Opt-in-Bestätigung | Keyword | Dies sind die Keywords, mit denen ein:e Nutzer:in seine oder ihre Opt-in-Absicht bestätigen kann. Mindestens ein Schlüsselwort ist erforderlich. Diese Schlüsselwörter sollten im Feld **Opt-In Prompt Reply Message** angegeben werden.
| | Antwortnachricht | Dies ist die Bestätigungsantwort, die ein Nutzer:innen erhält, nachdem er sein Opt-in ausdrücklich bestätigt hat und nun Nachrichten empfangen kann. Der Status der Abonnementgruppe des Benutzers wird auf `Subscribed` gesetzt.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Wenn ein:e Nutzer:in eine Opt-in-Anfrage erhält, hat er 30 Tage Zeit, seine Opt-in-Absicht zu bestätigen. Wenn ein:e Nutzer:in nach dem 30-Tage-Fenster ein Abonnement abschließen möchte, muss er oder sie ein Opt-in-Keyword eingeben, um den Workflow „Doppeltes Opt-in“ erneut zu starten.

![Die konfigurierbaren Felder haben zwei Abschnitte, Opt-in-Anfrage und doppelte Opt-in-Bestätigung, jeweils mit den Feldern Schlüsselwörter und Antwortnachricht.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Status der Abonnementgruppe

Erst wenn der Nutzer:innen den Double Opt-in-Workflow abgeschlossen hat, wird sein [Abo-Gruppenstatus]({{site.baseurl}}/sms_rcs_subscription_groups/) auf `Subscribed` aktualisiert. Wenn der Nutzer:innen den Workflow beginnt, aber nicht abschließt, bleibt er `Unsubscribed` und kann keine Nachrichten aus dieser Abo-Gruppe erhalten.

Nutzer:in können auch in den Double Opt-in-Workflow aufgenommen werden, wenn sie [aus anderen Quellen]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (z.B. REST API, SDK) [abonniert]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) sind.

## Abo-Quellen {#subscription-sources}

Nutzer:innen können auch durch Updates von Abos, die außerhalb eingehender Nachrichten erfolgen, in den Double Opt-in-Workflow einsteigen. Zu diesen Quellen gehören Updates von der REST API, dem SDK und dem Präferenzzentrum. Wenn ein Nutzer:in den Double Opt-in-Workflow über diese Quellen eintritt, erhält er die **Opt-in-Antwortnachricht**.

Jede Abo-Quelle hat ein anderes Anmeldeverhalten, wie in der folgenden Tabelle beschrieben.

Quelle    | Anmeldeverhalten bei doppeltem Opt-in   
----------- | -----------
SDK | Nutzer:in gelangen automatisch in den Double Opt-in Workflow, wenn sie sich über das Braze SDK angemeldet haben.
REST API | Nutzer:innen können in den Workflow aufgenommen werden, wenn der Abo-Status über `/subscription/status/set`, `/v2/subscription/status/set` oder `/users/track` gesetzt und der optionale Parameter `use_double_opt_in_logic` als `true` übergeben wird (z.B. [{"subscription_group_id": "subscription_group_identifier", "subscription_state": "abonniert", "use_double_opt_in_logic": true}]). Wenn dieser Parameter nicht angegeben wird, werden Nutzer:innen nicht in den Double Opt-in-Workflow aufgenommen.
Shopify | Nutzer:innen werden nicht in den Double Opt-in-Workflow aufgenommen, wenn ihr Abo-Status von unserer Shopify Integration festgelegt wird.
Nutzerimport | Nutzer:innen werden nicht in den Double Opt-in-Workflow aufgenommen, wenn ihr Abo-Status durch Nutzerimport festgelegt wird.
[Präferenz-Center]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | Nutzer:in werden automatisch in den Double Opt-in Workflow aufgenommen, wenn sie sich über ein Preference Center angemeldet haben.
Nutzeraktualisierungs-Schritt | Nutzer:innen können in den Double Opt-in-Workflow aufgenommen werden, wenn ihr Abo-Status über den Schritt User Update gesetzt wird und der optionale Parameter `use_double_opt_in_logic` als `true` übergeben wird. Wenn dieser Parameter nicht angegeben wird, werden Nutzer:innen nicht in den Double Opt-in-Workflow aufgenommen.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Unterstützung mehrerer Sprachen
Für eingehende Nachrichten wird das Double Opt-in für alle in der Abo-Gruppe definierten Sprachen unterstützt. Das bedeutet, dass Sie Ihre Auto-Responses in verschiedenen Sprachen definieren können und Braze die Auto-Response sendet, die mit einer bestimmten Sprache verbunden ist, wenn ein passendes Schlüsselwort empfangen wird.

Nutzer:innen, die in den Double Opt-in-Workflow durch Updates von Abos einsteigen, die außerhalb eingehender Nachrichten erfolgen (z.B. SDK, REST API, Shopify), werden nur die englischen Schlüsselwörter gesendet.

