---
nav_title: E-Mail-Präferenzen
article_title: E-Mail-Präferenzen
page_type: reference
page_order: 14
description: "Dieser Referenzartikel behandelt E-Mail-Einstellungen im Braze-Dashboard, einschließlich Versandkonfigurationen, Tracking-Pixel zum Öffnen, Anmeldeseite und Fußzeilen und vieles mehr."
tool: Dashboard
channel: email

---

# E-Mail-Präferenzen

> In den E-Mail-Voreinstellungen können Sie spezielle Einstellungen für ausgehende E-Mails vornehmen, z. B. benutzerdefinierte Fußzeilen, benutzerdefinierte Opt-in- und Opt-out-Seiten und vieles mehr. Wenn Sie diese Optionen in Ihre ausgehenden E-Mails aufnehmen, sorgt dies für ein flüssiges und kohärentes Erlebnis für Ihre Nutzer.

Die **E-Mail-Einstellungen** finden Sie unter **Einstellungen** im Dashboard.

## Konfiguration senden

Die E-Mail-Einstellungen im Abschnitt **Sendekonfiguration** bestimmen, welche Details in Ihren E-Mail-Kampagnen enthalten sind. Diese Einstellungen beziehen sich vor allem darauf, was Ihr Benutzer sieht, wenn er eine E-Mail von Braze erhält.

### Einstellungen für ausgehende E-Mails

Bei der Konfiguration Ihrer E-Mail-Einstellungen legen Sie fest, welche Namen und E-Mail-Adressen verwendet werden, wenn Braze E-Mails an Ihre Nutzer:innen versendet.

{% tabs local %}
{% tab Adresse des Anzeigenamens %}

In diesem Abschnitt können Sie die Namen und E-Mail-Adressen hinzufügen, die verwendet werden können, wenn Braze E-Mails an Ihre Benutzer sendet. Die Anzeigernamen und E-Mail-Adressen sind bei der Erstellung Ihrer E-Mail-Kampagne in den Optionen zum **Bearbeiten der Sendeinformationen** verfügbar. Beachten Sie, dass Aktualisierungen der Einstellungen für ausgehende E-Mails sich nicht rückwirkend auf bestehende Sendungen auswirken. 

![]({% image_buster /assets/img/email_settings/display_name_address.png %})

{% endtab %}
{% tab Antwortadresse %}

Wenn Sie in diesem Abschnitt eine E-Mail-Adresse hinzufügen, können Sie diese als Antwortadresse für Ihre E-Mail-Kampagne auswählen. Sie können auch eine E-Mail Adresse zum Standard machen, indem Sie **Standard** auswählen. Diese E-Mail-Adressen sind bei der Erstellung Ihrer E-Mail-Kampagne in den Optionen zum **Bearbeiten von Sendeinformationen** verfügbar.

![]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab BCC-Adresse %}

In diesem Bereich können Sie BCC-Adressen hinzufügen und verwalten, die an ausgehende E-Mail-Nachrichten von Braze angehängt werden können. Wenn Sie eine BCC-Adresse an eine E-Mail-Nachricht anhängen, wird eine identische Kopie der Nachricht, die Ihr Benutzer erhält, an Ihren BCC-Posteingang gesendet. Dies ist ein nützliches Tool, um Kopien von Nachrichten aufzubewahren, die Sie Ihren Benutzern aus Gründen der Compliance oder des Kundensupports geschickt haben. BCC-E-Mails sind in den E-Mail-Berichten und -Analysen nicht enthalten.

{% alert important %}
Wenn Sie eine BCC-Adresse an Ihre Kampagne oder Ihr Canvas anhängen, verdoppeln sich Ihre abrechenbaren E-Mails für die Kampagne oder die Canvas-Komponente, da Braze eine Nachricht an Ihren Nutzer:innen und eine an Ihre BCC-Adresse sendet.
{% endalert %}

![BCC-Adresse auf dem Tab „E-Mail-Einstellungen“.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Sobald Sie eine Adresse hinzugefügt haben, wird diese beim Verfassen einer E-Mail in Kampagnen oder Canvas-Schritten zur Auswahl gestellt. Wählen Sie **Standard** neben einer Adresse, um diese Adresse beim Starten einer neuen E-Mail-Kampagne oder Canvas-Komponente standardmäßig auszuwählen. Um dies auf der Ebene der Nachricht außer Kraft zu setzen, können Sie beim Einrichten Ihrer Nachricht **Kein BCC** auswählen.

Wenn Sie möchten, dass alle von Braze gesendeten E-Mail-Nachrichten eine BCC-Adresse enthalten, können Sie das Kontrollkästchen **BCC-Adresse für alle Ihre E-Mail-Kampagnen vorschreiben** aktivieren. Dazu müssen Sie eine Standardadresse auswählen, die bei neuen E-Mail-Kampagnen oder Canvas-Schritten automatisch ausgewählt wird. Die Standardadresse wird auch automatisch zu allen Nachrichten hinzugefügt, die über unsere REST API getriggert werden. Es ist nicht erforderlich, die bestehende API-Anfrage zu ändern, um die Adresse einzuschließen.

{% endtab %}
{% endtabs %}

## Tracking-Pixel für Öffnungsrate

[![Braze Learning Kurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

Das Tracking-Pixel für die E-Mail-Öffnung ist ein unsichtbares 1 x 1 px großes Bild, das automatisch in den HTML-Code Ihrer E-Mail eingefügt wird. Dieses Pixel hilft Braze zu erkennen, ob die Endnutzer Ihre E-Mail geöffnet haben. Informationen über die Öffnungsrate von E-Mails können sehr nützlich sein, da sie den Nutzern helfen, effektive Marketingstrategien festzulegen, indem sie die entsprechenden Öffnungsraten verstehen.

### Platzierung des Tracking-Pixels

Standardmäßig wird in Braze das Tracking-Pixel am Ende Ihrer E-Mail angehängt. Für die meisten Nutzer:innen ist dies der ideale Ort, um das Pixel zu platzieren. Das Pixel ist bereits so gestaltet, dass es so wenig visuelle Veränderungen wie möglich verursacht. Unbeabsichtigte visuelle Veränderungen wären am unteren Rand einer E-Mail am wenigsten sichtbar. Dies ist auch der Standard für E-Mail-Anbieter wie SendGrid und SparkPost.

### Ändern des Standorts des Tracking-Pixels

Braze unterstützt derzeit das Überschreiben des Tracking-Pixel für die Standard-Öffnungsrate (das letzte Tag im `<body>` einer E-Mail), um es auf das erste Tag im `<body>` zu verschieben.
  
![][13]{: style="max-width:80%;" }

So ändern Sie den Standort:

1. Gehen Sie in Braze zu **Einstellungen** > **E-Mail-Voreinstellungen**.
2. Klicken Sie auf das Kontrollkästchen unter **Benutzerdefinierte Einstellungen für offene Tracking-Pixel**. 
3. Drücken Sie **Speichern**.

Nach der Speicherung sendet Braze spezielle Anweisungen an den ESP, um das Tracking-Pixel für die Öffnung oben in allen HTML-E-Mails zu platzieren.
  
{% alert important %}
Durch die Aktivierung von SSL wird die URL des Tracking-Pixels mit HTTPS statt mit HTTP verschlüsselt - wenn Ihr SSL falsch konfiguriert ist, kann dies die Wirksamkeit des Tracking-Pixels beeinträchtigen.
{% endalert %}

## Listenabmelde-Header {#list-unsubscribe}

{% alert note %}
Ab dem 15\. Februar 2024 wird der Listenabmelde-Header (mit 1-Klick-Abmeldung) für neue Unternehmen standardmäßig aktiviert sein.
{% endalert %}

Wenn Sie einen Listenabmelde-Header verwenden, können Ihre Empfänger:innen der Mailbox-UI und nicht in der Nachricht einen **Abmelden**-Button von Marketing-E-Mails anzeigen lassen.

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Wenn ein:e Empfänger:in auf **Abmelden** klickt, sendet der Mailbox-Anbieter die Anfrage zum Abmelden an das im Header der E-Mail definierte Ziel.

Die Aktivierung der Listenabmeldung ist eine Best Practice für die Zustellbarkeit und bei einigen der führenden Mailbox-Anbieter eine Voraussetzung. Es ermutigt Endbenutzer, unerwünschte Nachrichten sicher zu entfernen, anstatt die Spam-Schaltfläche in einem E-Mail-Client zu drücken, was der Reputation des Versenders und der Zustellbarkeit von E-Mails abträglich ist.

### Unterstützung für Mailbox-Anbieter

In der folgenden Tabelle finden Sie eine Übersicht über die Unterstützung von Mailbox-Anbietern für den „mailto:“-Header, die URL für die Abmeldung von der Liste und die Abmeldung mit einem Klick [(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| Listenabmelde-Header | Mailto: Header | Listenabmelde-URL | Abmelden mit einem Klick (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | Unterstützt* | Unterstützt | Unterstützt |
| Gmail Mobile | Nicht unterstützt | Nicht unterstützt | Nicht unterstützt |
| Apple Mail | Unterstützt | Nicht unterstützt | Nicht unterstützt |
| Outlook.com | Unterstützt | Nicht unterstützt | Nicht unterstützt |
| Yahoo! Mail | Unterstützt* | Nicht unterstützt | Unterstützt |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_\*Yahoo und Gmail werden die „mailto:“-Header irgendwann veralten lassen und nur noch einen Klick unterstützen._

Die Anzeige der Kopfzeile wird letztendlich vom Mailbox-Anbieter bestimmt. Um zu überprüfen, ob der Listenabmelde-Header in der Roh-E-Mail (Text) für den oder die Empfänger:in in Gmail enthalten ist, gehen Sie wie folgt vor:

1. Wählen Sie in der E-Mail **Original anzeigen** aus. Dies öffnet eine neue Registerkarte mit der Rohfassung der E-Mail und ihren Kopfzeilen.
2. Nach „Liste abmelden“ suchen.

Wenn die Kopfzeile in der Rohfassung der E-Mail enthalten ist, aber nicht angezeigt wird, hat der Mailbox-Anbieter beschlossen, die Option zum Abmelden nicht anzuzeigen. Das bedeutet, dass wir keine weiteren Insights darüber haben, warum der Mailbox-Anbieter die Kopfzeile nicht anzeigt. Die Anzeige der Kopfzeile list-unsubscribe ist letztlich reputationsbasiert. In den meisten Fällen gilt: Je besser der Ruf Ihres Absenders im Posteingang ist, desto unwahrscheinlicher ist es, dass die Kopfzeile list-unsubscribe erscheint.

### E-Mail-Abmelde-Header in Workspaces

![]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Wenn das Feature zum Abmelden von E-Mails aktiviert ist, gilt diese Einstellung für den gesamten Workspace, nicht für die Unternehmensebene. Sie wird zu Kampagnen und Canvases hinzugefügt, die so eingerichtet sind, dass sie an abonnierte oder eingeloggte Benutzer gesendet werden, oder an eingeloggte Benutzer im Schritt **Zielgruppen** der Kampagnen- und Canvas-Ersteller.

Wenn Sie den "Workspace Standard" verwenden, fügt Braze die Kopfzeile zum Abmelden mit einem Klick nicht für Kampagnen hinzu, die als transaktional gelten und so konfiguriert sind, dass sie an alle Nutzer:innen gesendet werden, auch an nicht abgemeldete Nutzer:innen. Um dies außer Kraft zu setzen und die Kopfzeile zum Abmelden mit einem Klick hinzuzufügen, wenn Sie an abgemeldete Nutzer:innen senden, können Sie in den Einstellungen für die Ein-Klick-Liste zum Abmelden auf Nachrichtenebene die Option **Global abmelden aus allen Nachrichten** auswählen.

### Standard-Listenabmelde-Header

{% alert important %}
Google Mail beabsichtigt, dass Absender ab dem 1\. Juni 2024 die Ein-Klick-Abmeldung für alle ihre ausgehenden kommerziellen Werbebotschaften implementieren. Weitere Informationen finden Sie in den [Richtlinien für Absender:innen von Google Mail](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) und in den [FAQ zu den Richtlinien für E-Mail-Absender:innen von Google Mail](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo kündigte einen Zeitplan für die Aktualisierungsanforderungen für Anfang 2024 an. Weitere Informationen finden Sie unter [Mehr Sicherheit, weniger Spam: Durchsetzung von E-Mail-Standards für ein besseres Erlebnis](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Wenn Sie das Feature „Abmelden von Braze“ verwenden möchten, um Abmeldungen direkt zu verarbeiten, wählen Sie **E-Mail-Header für 1-Klick-Abmeldung per Listenabmeldung (Mailto und HTTP) für E-Mails verwenden, die an Abonnent:innen oder angemeldete Nutzer:innen gesendet werden** sowie **Braze Standard** als Standard-Braze-URl und „Mailto“. 

![Option zum automatischen Einfügen eines Listenabmelde-Headers für E-Mails, die an abonnierte oder angemeldete Nutzer:innen gesendet werden.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %}){: style="max-width:80%;"}

Braze unterstützt die folgenden Versionen des list-unsubscribe-Headers:

| Version zum Abbestellen der Liste | Beschreibung | 
| ----- | --- |
| Ein-Klick (RFC 8058) | Bietet eine unkomplizierte Möglichkeit für Empfänger, sich mit einem einzigen Klick von E-Mails abzumelden. Dies ist eine Anforderung von Yahoo und Gmail für Massenversender. |
| URL oder HTTPS zum Abbestellen von Listen | Bietet Empfänger:innen einen Link, der den oder die Empfänger:in auf eine Internetseite leitet, auf der er oder sie sich abmelden kann. |
| Mailto | Gibt eine E-Mail Adresse als Ziel für die Nachricht der Abmeldeanfrage an, die vom Empfänger oder von der Empfängerin an die Marke gesendet werden soll. <br><br> _Um E-Mail-Anfragen Listenabmeldung zu bearbeiten, müssen diese Abmeldeanfragen die E-Mail-Adresse enthalten, die in Braze für den oder die Endnutzer:in, der oder die sich abmeldet, gespeichert ist. Dies kann durch die „Absenderadresse“ der E-Mail, von der aus der oder die Endnutzer:in sich abmeldet, den verschlüsselten Betreff oder den verschlüsselten Textkörper der E-Mail, die der oder die Endnutzer:in erhält und von der er oder sie sich abmeldet, bereitgestellt werden. In einigen wenigen Fällen halten sich einige Anbieter von Posteingängen nicht an das Protokoll [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), was dazu führt, dass die E-Mail Adresse nicht ordnungsgemäß weitergegeben wird. Dies kann dazu führen, dass eine Anfrage zur Abmeldung in Braze nicht bearbeitet werden kann._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Wenn Braze von einem Benutzer über eine der oben genannten Methoden eine Anfrage zur Abmeldung von der Liste erhält, wird der globale E-Mail-Abonnementstatus dieses Benutzers auf abgemeldet gesetzt. Wenn es keine Übereinstimmung gibt, wird Braze diese Anfrage nicht bearbeiten.

### Mit einem Klick abmelden

Die Verwendung von one-click unsubscribe für den list-unsubscribe-Header[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) zielt darauf ab, den Empfängern eine einfache Möglichkeit zu bieten, sich von E-Mails abzumelden.

### Abbestellen der Liste auf Nachrichtenebene mit einem Klick

Die Einstellung für die Listenanmeldung auf Nachrichtenebene mit einem Klick setzt das Feature des Headers zum Abmelden von E-Mails für Workspaces außer Kraft. Wenden Sie das Verhalten zum Abmelden mit einem Klick pro Kampagne oder Canvas-Schritt für die folgenden Zwecke an:

- Fügen Sie eine Braze-Ein-Klick-Abmeldung für eine bestimmte Abo-Gruppe hinzu, um mehrere Marken/Listen innerhalb eines Workspace zu unterstützen.
- Wechseln Sie zwischen der Standard-URL zum Abbestellen von Braze oder einer nutzerdefinierten URL.
- Fügen Sie Ihre eigene URL für die Abmeldung mit einem Klick hinzu
- Bitte entfernen Sie die Option zum Abbestellen dieser Nachricht mit einem Klick.

{% alert note %}
Die Einstellung zum Abbestellen von Nachrichten mit einem Klick ist nur verfügbar, wenn Sie den aktualisierten HTML-Editor verwenden. Wenn Sie den vorherigen HTML-Editor verwenden, wechseln Sie zum aktualisierten HTML-Editor, um diese Funktion zu nutzen.
{% endalert %}

Gehen Sie in Ihrem E-Mail-Editor zu **Sendeeinstellungen** > **Sendeinfo**. Wählen Sie aus den folgenden Optionen:

- **Workspace-Standard verwenden**: Verwendet die Einstellungen für den **E-Mail-Abmeldekopf**, die in den **E-Mail-Einstellungen** festgelegt wurden. Alle Änderungen an dieser Einstellung werden für alle Nachrichten übernommen.
- **Global von allen E-Mails abmelden**: Verwendet den Braze-Standard-Header zum Abmelden mit einem Klick. Für Nutzer:innen, die auf den Button „Abmelden“ klicken, wird der Status ihres globalen E-Mail-Abos auf „Abgemeldet“ gesetzt.
- **Aus bestimmter Abo-Gruppe abmelden**: Verwendet die angegebene Abonnementgruppe. Nutzer:innen, die auf den Button „Abmelden“ klicken, werden aus der ausgewählten Abo-Gruppe abgemeldet.
    - Wenn Sie eine Abonnementgruppe auswählen, fügen Sie unter **Zielgruppen** den Filter **Abonnementgruppe** hinzu, um nur Benutzer anzusprechen, die bei dieser speziellen Gruppe abonniert sind. Die für das Abmelden mit einem Klick ausgewählte Abo-Gruppe muss mit der Abo-Gruppe übereinstimmen, die Sie als Targeting verwenden. Wenn die Abo-Gruppe nicht übereinstimmt, besteht die Gefahr, dass Sie an eine:n Nutzer:in senden, der oder die versucht, sich von einer Abo-Gruppe abzumelden, von der er bereits abgemeldet ist.
- **Anpassen:** Fügt Ihre angepasste URL für die 1-Klick-Abmeldung hinzu, damit Sie Abmeldungen direkt verarbeiten können.
- **Abmelden ausschließen**

{% alert important %}
Das Abmelden mit einem Klick oder andere Abmeldemechanismen sollten nur für Messaging-Nachrichten zu Transaktionen, wie das Zurücksetzen von Passwörtern, Quittungen und Bestätigungs-E-Mails, verwendet werden.
{% endalert %}

Wenn Sie diese Einstellung ändern, wird das Standardverhalten für die Abmeldung von der Liste mit einem Klick in dieser E-Mail außer Kraft gesetzt.

![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Anforderungen

Wenn Sie E-Mails mit Ihrer eigenen benutzerdefinierten Abmeldefunktion versenden, müssen Sie die folgenden Anforderungen erfüllen, um sicherzustellen, dass die von Ihnen eingerichtete Ein-Klick-Abmelde-URL mit RFC 8058 übereinstimmt:

* Die URL muss in der Lage sein, POST-Anfragen zum Abmelden zu verarbeiten.
* Die URL muss mit `https://` beginnen.
* Die URL darf weder eine HTTPS-Weiterleitung noch einen Body zurückgeben. Ein-Klick-Abmeldelinks, die zu einer Landing Page oder einer anderen Art von Webseite führen, entsprechen nicht RFC 8058.
* POST-Anfragen dürfen keine Cookies setzen.

Wählen Sie **Angepasster Listenanmelde-Header**, um Ihren eigenen konfigurierten Endpunkt für das Abmelden mit einem Klick und ein optionales „mailto:“ hinzuzufügen. Braze erfordert eine Eingabe für die URL, um einen angepassten Listenabmelde-Header zu unterstützen, da die HTTP-Funktion zum Abmelden mit einem Klick eine Anforderung von Yahoo und Gmail für Massenabsender ist.

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## E-Mail-Betreffzeilen anhängen

Verwenden Sie das Umschalten, um „[TEST]“ und „[SEED]“ in die Betreffzeilen Ihrer Test- und Seed-E-Mails aufzunehmen. Damit können Sie alle als Test versendeten Kampagnen per E-Mail identifizieren.

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## Standardmäßig Inline-CSS in neuen E-Mails

CSS-Inlining ist eine Technik, die automatisch CSS-Stile für Ihre E-Mails und neuen E-Mails einfügt. Bei einigen E-Mail-Clients kann dies die Darstellung Ihrer E-Mails verbessern.

Die Änderung dieser Einstellung hat keine Auswirkungen auf Ihre bestehenden E-Mail-Nachrichten oder Vorlagen. Sie können diese Vorgabe beim Verfassen von Nachrichten oder Vorlagen jederzeit außer Kraft setzen. Weitere Informationen finden Sie unter [CSS inlining][10].

## Nutzer:innen neu anmelden, wenn sich ihre E-Mail ändert

Sie können Nutzer:innen automatisch neu anmelden, wenn sie ihre E-Mail Adresse ändern. Wenn zum Beispiel ein zuvor abgemeldete:r Nutzer:in des Workspace seine E-Mail-Adresse in eine Adresse ändert, die nicht auf der Abmeldeliste für Braze steht, wird er automatisch wieder angemeldet.

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Abonnementseiten und Fußzeilen

{% tabs local %}
{% tab Benutzerdefinierte Fußzeile %}

Für kommerzielle E-Mails schreibt der [CAN-SPAM Act](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) vor, dass alle kommerziellen E-Mails eine Abmeldeoption enthalten müssen. Mit den benutzerdefinierten Fußzeileneinstellungen können Sie die CAN-SPAM-Vorschriften einhalten und gleichzeitig Ihre Fußzeile für die E-Mail-Abmeldung anpassen. Um die Vorschriften einzuhalten, müssen Sie Ihre benutzerdefinierte Fußzeile zu allen E-Mails hinzufügen, die im Rahmen von Kampagnen für diesen Arbeitsbereich versendet werden.

Beachten Sie die folgenden Anforderungen, wenn Sie eine angepasste Fußzeile für Ihr E-Mail-Messaging erstellen:
- Sie müssen eine URL zum Abmelden und eine physische Postanschrift angeben.
- Sollte weniger als 100 KB betragen.

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

Wenn Sie mehr über die benutzerdefinierte Fußzeile Liquid Templating erfahren möchten, lesen Sie unsere Dokumentation über [benutzerdefinierte Fußzeilen]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Angepasste Abmeldeseite %}

Mit Braze können Sie eine **benutzerdefinierte Abmeldeseite** mit Ihrem eigenen HTML-Code einrichten. Diese Seite wird angezeigt, wenn ein Nutzer:innen am Ende einer E-Mail ausgewählt hat, sich abzumelden. Beachten Sie, dass diese Seite weniger als 750 KB groß sein sollte. 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Erfahren Sie mehr über bewährte Methoden zur Verwaltung von E-Mail-Listen unter [Verwaltung von E-Mail-Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Angepasste Opt-in Seite %}

Sie können eine benutzerdefinierte Opt-in-Seite mit Ihrem eigenen HTML-Code erstellen. Dies in Ihre E-Mails einzubauen, kann besonders dann von Vorteil sein, wenn Sie möchten, dass Ihr Branding und Ihre Nachrichten während des gesamten Lebenszyklus Ihrer Nutzer:innen konsistent bleiben. Beachten Sie, dass diese Seite weniger als 750 KB groß sein sollte. 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Erfahren Sie mehr über bewährte Methoden zur Verwaltung von E-Mail-Listen unter [Verwaltung von E-Mail-Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

## Häufig gestellte Fragen

### Mit einem Klick abmelden

{% details Kann die URL zum Abmelden mit einem Klick (über den Listenabmelde-Header) mit einem Präferenzzentrum verknüpft werden? %}
Nein, das entspricht nicht RFC 8058, d.h. Sie erfüllen nicht die Anforderungen von Yahoo und Gmail für die Abmeldung mit einem Klick.
{% enddetails %}

{% details Warum erhalte ich die Fehlermeldung „Ihr E-Mail-Text enthält keinen Link zum Abmelden“, wenn ich mein Präferenzzentrum zusammenstelle? %}
Ein Präferenzzentrum gilt nicht als Abmeldelink. Ihre E-Mail-Empfänger müssen die Möglichkeit haben, sich von allen kommerziellen E-Mails abzumelden, um CAN-SPAM-konform zu bleiben.
{% enddetails %}


{% details Muss ich frühere E-Mail-Kampagnen und Canvases bearbeiten, um die Einstellung für die Abmeldung mit einem Klick anzuwenden, nachdem ich sie aktiviert habe? %}
Wenn Sie keinen der Anwendungsfälle für die Ein-Klick-Listenabmeldung auf Nachrichtenebene haben, ist keine Aktion erforderlich, solange die Einstellung unter **E-Mail-Einstellungen** aktiviert ist. Braze fügt automatisch die Kopfzeilen für die Abmeldung mit einem Klick zu allen ausgehenden Marketing- und Werbenachrichten hinzu. Wenn Sie jedoch das Verhalten beim Abmelden mit einem Klick pro Nachricht konfigurieren möchten, müssen Sie frühere Kampagnen und Canvas-Schritte mit E-Mail entsprechend aktualisieren.
{% enddetails %}

{% details Ich kann den Listenabmelde-Header und Abmelde-Header mit einem Klick in der ursprünglichen Nachricht oder den Rohdaten sehen, aber warum sehe ich den Button „Abmelden“ nicht in Gmail oder Yahoo? %}
Gmail und Yahoo entscheiden letztendlich, ob die Kopfzeile für die Listenabmeldung oder die Ein-Klick-Abmeldung angezeigt werden soll oder nicht. Bei neuen Absender:innen oder Absender:innen mit geringer Absender-Reputation kann dies gelegentlich dazu führen, dass der Button zum Abmelden nicht angezeigt wird.
{% enddetails %}

{% details Unterstützt die benutzerdefinierte Kopfzeile für die Abmeldung mit einem Klick Liquid? %}
Ja, Liquid und bedingte Logik werden unterstützt, um dynamische URLs zum Abmelden mit einem Klick im Header zuzulassen.
{% enddetails %}

{% alert tip %}
Wenn Sie eine bedingte Logik hinzufügen, vermeiden Sie Ausgabewerte, die Ihrer URL Leerzeichen hinzufügen, da Braze diese Leerzeichen nicht entfernt.
{% endalert %}

### Abbestellen der Liste auf Nachrichtenebene mit einem Klick

{% details Wenn ich die E-Mail-Kopfzeilen für One-Click manuell hinzufüge und die Kopfzeile für die Abmeldung von E-Mails aktiviert habe, was ist dann das erwartete Verhalten? %}
Die E-Mail-Kopfzeilen, die für die Ein-Klick-Liste-Abmeldung hinzugefügt wurden, werden für alle zukünftigen Sendungen dieser Kampagne übernommen.
{% enddetails %}

{% details Warum müssen Abo-Gruppen über verschiedene Varianten von Nachrichten hinweg übereinstimmen, um starten zu können? %}
Bei einer Kampagne mit A/B-Tests sendet Braze einem Benutzer zufällig eine der Varianten. Wenn Sie zwei verschiedene Abonnementgruppen für dieselbe Kampagne festgelegt haben (Variante A ist auf Abonnementgruppe A und Variante B auf Abonnementgruppe B festgelegt), können wir nicht garantieren, dass Benutzer, die nur die Abonnementgruppe B abonniert haben, auch die Variante B erhalten. Es kann ein Szenario geben, in dem Benutzer sich von einer Abonnementgruppe abmelden, aus der sie bereits ausgetreten sind.
{% enddetails %}

{% details Die E-Mail-Header-Einstellung zum Abbestellen des Abonnements ist in den E-Mail-Einstellungen deaktiviert, aber in den Versandinformationen meiner Kampagne ist die Einstellung zum Abbestellen des Abonnements mit einem Klick auf „Workspace-Standard verwenden“ eingestellt. Ist dies ein Fehler? %}
Nein. Wenn die Arbeitsbereichseinstellung deaktiviert ist und die Nachrichteneinstellung auf **Arbeitsbereich-Standard verwenden** gesetzt ist, folgt Braze der Konfiguration in den **E-Mail-Einstellungen**. Das bedeutet, dass wir die Kopfzeile für die Abmeldung mit einem Klick für die Kampagne nicht hinzufügen werden.
{% enddetails %}

{% details Was passiert, wenn eine Abonnementgruppe archiviert wird? Wird dadurch das Abmelden von gesendeten E-Mails mit einem Klick unterbrochen? %}
Wenn eine Abo-Gruppe, auf die in den **Sendeinformationen** für One-Click referenziert wird, archiviert wird, verarbeitet Braze trotzdem Abmeldungen von One-Click. Die Abonnementgruppe wird auf dem Dashboard (Segmentfilter, Benutzerprofil und ähnliche Bereiche) nicht mehr angezeigt.
{% enddetails %}

{% details Ist die Einstellung „Abmelden mit einem Klick“ auch für E-Mail Templates verfügbar? %}
Nein, wir haben derzeit keine Pläne, dies für E-Mail-Templates hinzuzufügen, da diese Templates keiner sendenden Domain zugewiesen sind. Wenn Sie an dieser Funktion für E-Mail-Vorlagen interessiert sind, senden Sie uns Ihr [Produkt-Feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details Überprüft diese Funktion, ob die der benutzerdefinierten Option hinzugefügte URL für die Abmeldung mit einem Klick gültig ist? %}
Nein, wir überprüfen oder validieren keine Links im Braze Dashboard. Stellen Sie sicher, dass Sie Ihre URL vor dem Start ordnungsgemäß testen.
{% enddetails %}


[0]: {% image_buster /assets/img_archive/list_unsub_img1.png %}
[1]: {% image_buster /assets/img/email_settings/outbound_email.png %}
[2]: {% image_buster /assets/img/email_settings/switch.gif %}
[6]: https://learning.braze.com/email-open-tracking-pixel
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/
[13]: {% image_buster /assets/img/open_pixel.png %}
