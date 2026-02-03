---
nav_title: "In-App-Nachrichten"
article_title: In-App-Nachrichten
page_order: 2
alias: /in-app_messages/
description: "Auf dieser Landing Page finden Sie alles rund um In-App-Nachrichten. Hier finden Sie Artikel über die Erstellung von In-App-Nachrichten, den Drag-and-Drop-Editor, die Anpassung Ihrer Nachrichten, die Berichterstattung und vieles mehr."
channel:
  - in-app messages
search_rank: 5
---

# [![Braze Lernkurse]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} In-App-Nachrichten

> In-App-Nachrichten helfen Ihnen, Inhalte an Ihre Nutzer:innen zu übermitteln, ohne sie mit einer Push-Benachrichtigung zu unterbrechen, denn diese Nachrichten werden nicht außerhalb der App des Nutzers zugestellt und stören nicht den Startbildschirm. 

Angepasste und maßgeschneiderte In-App-Nachrichten verbessern das Nutzererlebnis und helfen Ihrer Zielgruppe, den größten Nutzen aus Ihrer App zu ziehen. Mit einer Vielzahl von Layouts und Anpassungswerkzeugen, aus denen Sie wählen können, binden In-App-Nachrichten Ihre Nutzer mehr als je zuvor. Sie sind kontextbezogen, haben eine geringere Dringlichkeit und werden zugestellt, wenn der Nutzer:innen in Ihrer App aktiv ist. Beispiele für In-App-Nachrichten finden Sie in unseren [Kund:in-Storys](https://www.braze.com/customers/).

## Anwendungsfälle

Mit dem reichhaltigen Angebot an Content, der In-App-Nachrichten bieten, können Sie diesen Kanal für eine Vielzahl von Anwendungsfällen nutzen:

| Anwendungsfall | Erklärung |
| --- | --- |
| Push-Priming | Führen Sie eine [Push-Priming-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) mit einer reichhaltigen In-App-Nachricht durch, um Ihren Kunden die Vorteile einer Push-Erlaubnis für Ihre App oder Website zu verdeutlichen, und fordern Sie sie auf, die Push-Erlaubnis zu erteilen.
| Verkäufe und Aktionen | Verwenden Sie modale In-App-Nachrichten, um Kund:innen mit visuell ansprechenden Medien zu begrüßen, die statische Aktionscodes oder Angebote enthalten. Ermutigen Sie sie zu Käufen oder Konversionen, die sie sonst nicht getätigt hätten. |
| Förderung zur Annahme von Features | Ermuntern Sie Ihre Kunden, andere Teile Ihrer App zu nutzen oder einen Service in Anspruch zu nehmen. |
| Hochgradig personalisierte Kampagnen | Platzieren Sie In-App-Nachrichten als das Erste, was Ihre Kunden sehen, wenn sie Ihre App oder Website betreten. Fügen Sie einige Features zur Personalisierung von Braze hinzu, wie z. B. [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), um Nutzer:innen zum Handeln zu bewegen und so Ihre Reichweite zu erhöhen.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Andere Anwendungsfälle, die Sie in Betracht ziehen sollten, sind die folgenden:

- Neue Features in der App
- App-Verwaltung
- Bewertungen
- App Upgrades oder Updates
- Werbegeschenke und Verlosungen

## Standard Nachrichtentypen

Die folgenden Registerkarten zeigen, wie es aussieht, wenn Ihre Benutzer eine unserer standardmäßigen In-App-Nachrichtenarten öffnen - aufklappbare, modale und bildschirmfüllende In-App-Nachrichten.

{% tabs %}
{% tab Slideup %}

Slide-up-Nachrichten erscheinen normalerweise am oberen und unteren Rand des App-Bildschirms (Sie können dies beim Erstellen Ihrer Nachricht einstellen). Diese sind ideal, um Ihre Benutzer über neue Nutzungsbedingungen, Cookies und andere Informationen zu informieren.

![Slideup-In-App-Nachricht, die am unteren Rand des App-Bildschirms angezeigt wird. Das Slide-Up enthält ein Symbolbild und eine kurze Nachricht.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Modals erscheinen in der Mitte des Bildschirms des Geräts mit einem Overlay, das sie von Ihrer App im Hintergrund abhebt. Sie eignen sich perfekt, um Ihren Nutzern ganz unaufdringlich vorzuschlagen, von einem Verkauf oder einer Werbeaktion zu profitieren.

![Modale In-App-Nachricht, die in der Mitte einer App und Website als Dialogfeld angezeigt werden. Das Modal enthält ein Bild, eine Kopfzeile, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fullscreen %}

Vollbildnachrichten sind genau das, was Sie erwarten - sie nehmen den gesamten Bildschirm des Geräts ein! Dieser Nachrichtentyp eignet sich hervorragend, wenn Sie die Aufmerksamkeit Ihrer Nutzer wirklich benötigen, z. B. bei obligatorischen App-Updates.

![Bildschirmfüllende In-App-Nachricht, die einen App-Bildschirm einnimmt. Die Nachricht im Vollbildmodus enthält ein großes Bild, eine Kopfzeile, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Zusätzlich zu diesen Standard-Nachrichten-Templates können Sie Ihr Messaging mit angepassten HTML In-App-Nachrichten, Web-Modals mit CSS oder Web-Formularen zur Erfassung von E-Mails weiter anpassen. Weitere Informationen finden Sie unter [Anpassung]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Templates für In-App-Nachrichten

In-App-Nachrichten werden als Template für In-App-Nachrichten zugestellt, wenn die Option **Kampagnen-Zulässigkeit vor der Anzeige neu bewerten** ausgewählt ist oder wenn einer der folgenden Liquid-Tags in der Nachricht vorhanden ist:

- `canvas_entry_properties`
- `connected_content`
- SMS-Variablen wie z.B. {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Das bedeutet, dass das Gerät beim Start der Sitzung den Auslöser dieser In-App-Nachricht anstelle der gesamten Nachricht empfängt. Wenn die:der Nutzer:in die In-App-Nachricht triggert, wird ihr:sein Gerät eine Anfrage an das Netzwerk stellen, um die eigentliche Nachricht abzurufen.

{% alert note %}
Die Nachricht wird nicht zugestellt, wenn das Gerät keinen Internetzugang hat. Die Nachricht wird möglicherweise nicht zugestellt, wenn die Liquid-Logik zu lange braucht, um sie aufzulösen.
{% endalert %}

## Verhalten abbrechen

Bei Braze kommt es zu einem Abbruch, wenn ein Nutzer:innen eine Aktion durchführt, die ihn für den Empfang einer Nachricht qualifiziert, er die Nachricht aber nicht erhält, weil die Logik von Liquid ihn als nicht qualifiziert markiert. Zum Beispiel:

1. Sam führt eine Aktion aus, die eine E-Mail Kampagne triggern soll.
2. Der Textkörper der E-Mail enthält eine Liquid-Logik, die besagt, dass diese E-Mail nicht gesendet werden soll, wenn ein angepasstes Attribut einen Wert von weniger als 50 hat.
3. Sams angepasste Attribute haben eine Punktzahl von 20.
4. Braze erkennt, dass Sam diese E-Mail nicht erhalten sollte, und die E-Mail wird abgebrochen.
5. Ein Abbruchereignis wird protokolliert.

Da es sich bei In-App-Nachrichten jedoch um einen Pull-Kanal handelt, funktionieren Abbrüche bei ihnen etwas anders.

### Abbruchverhalten von In-App-Nachricht

In-App-Nachrichten werden beim Start der Sitzung vom Gerät abgerufen und auf dem Gerät zwischengespeichert, so dass die Nachricht dem Nutzer:in unabhängig von der Qualität der Internetverbindung sofort zugestellt werden kann. Wenn ein Nutzer:innen zum Beispiel fünf In-App-Nachrichten innerhalb seiner Sitzung erhält, bekommt er alle fünf Nachrichten bei Sitzungsbeginn. Die Nachrichten werden lokal zwischengespeichert und erscheinen, wenn ihre definierten Trigger-Ereignisse eintreten (Sitzungsstart, Nutzer:innen klickt auf einen Button, der ein angepasstes Event protokolliert, oder anderes).

Mit anderen Worten: Die Logik, die bestimmt, ob wir eine In-App-Nachricht abbrechen sollen, tritt auf **, bevor** der Trigger eingetreten ist. Um dies zu demonstrieren, nehmen wir an, Sam aus dem E-Mail-Beispiel hat Push-Benachrichtigungen abonniert.

1. Sam beginnt eine Sitzung, indem er eine von Braze betriebene App auf seinem Telefon startet.
2. Basierend auf den Zielgruppen-Kriterien der aktiven Kampagnen im Workspace könnte Sam für fünf verschiedene Kampagnen in Frage kommen. Alle FIVE werden auf ihr Telefon gezogen und zwischengespeichert.
3. Sam **hat keine** Aktionen durchgeführt, die diese Nachrichten triggern würden, aber sie könnten diese Nachrichten in der Sitzung empfangen.
4. Das Liquid in zwei der In-App-Nachrichten verfügt über Regeln, die Sam vom Erhalt der Nachricht ausschließen (z.B. weil sein angepasstes Attribut für die Punktzahl nicht hoch genug ist).
5. Sam erhält die beiden In-App-Nachrichten, die sie ausschließen, nicht, aber die anderen drei Nachrichten.
6. Es werden keine Abbruchereignisse protokolliert.

Braze protokolliert in Sams Fall keine Abbruchereignisse, da dies nicht unserer Definition eines Abbruchs entspricht; Sam **hat** keine Aktionen durchgeführt, die die Nachrichten triggern würden. Bei In-App-Nachrichten führen die Nutzer:innen den Trigger nie aus, bevor Braze feststellt, dass sie die Nachricht nicht sehen sollen.

#### Templates für den Abbruch von In-App-Nachrichten

[In-App-Nachrichten mit Templates](#templated-in-app-messages) zwingen das SDK dazu, neu zu bewerten, ob eine Nachricht angezeigt werden soll, wenn das triggernde Ereignis eintritt. Dies hat ein anderes Abbruchverhalten. Betrachten wir zur Veranschaulichung dieses Beispiel:

1. Sam beginnt eine Braze-Sitzung, indem er eine von Braze betriebene App auf seinem Telefon startet.
2. Die Zielgruppen-Kriterien der aktiven Kampagnen besagen, dass Sam für eine In-App-Nachricht mit Template in Frage kommt, so dass die Trigger-Informationen ohne die Nutzlast der Nachricht an ihr Gerät gesendet werden.
3. Sam wählt einen Button aus, der ein angepasstes Event protokolliert und damit die Template In-App-Nachricht triggert.
4. Das Gerät von Sam stellt eine Anfrage an das Netzwerk, um die In-App-Nachricht abzurufen.
5. Die Liquid-Logik der Nachricht führt zu einem Abbruch, so dass Braze dies als Abbruch protokolliert; Sam hat die Aktion triggern vor dieser Auswertung durchgeführt.

##### Vergleich des Abbruchverhaltens von In-App-Nachricht

Diese Tabelle vergleicht die In-App-Nachrichten, die Sam erhalten hat:

| In-App-Nachricht | Verhalten abbrechen |
| --- | --- |
| Standard | Ein Abbruchereignis wurde nicht protokolliert, weil Sam keine Aktionen durchgeführt hat, die eine Nachricht triggern würden.<br><br>Standard In-App-Nachrichten protokollieren keine Abbrüche, da die Definition eines Abbruchs lautet: "Habe die Nachricht nicht gesehen, obwohl ich die Aktion getriggert habe." Da In-App-Nachrichten dem Gerät zugestellt werden, bevor die Aktionen getriggert werden, macht es keinen Sinn, In-App-Nachrichten aufgrund der Liquid-Logik als ausgelassen zu betrachten. |
| Templated | Ein Abbruchereignis wurde protokolliert, weil Sam die Aktion triggern ausgeführt hat, um die In-App-Nachricht zu triggern, aber einen Abbruch im Liquid-Templating erhalten hat. <br><br>Das Protokoll der In-App-Nachrichten bricht ab, weil die Liquid-Auswertung nach der Durchführung der triggernden Aktion erfolgt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Mehr Ressourcen

Bevor Sie mit der Erstellung Ihrer eigenen In-App-Nachrichten-Kampagnen beginnen - oder In-App-Nachrichten in einer Multikanal-Kampagne verwenden - empfehlen wir Ihnen dringend, sich unseren [Leitfaden zur Vorbereitung von In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/) anzusehen. Dieser Leitfaden behandelt Fragen zu Targeting, Content und Konversion, die Sie bei der Erstellung von In-App-Nachrichten berücksichtigen sollten.
