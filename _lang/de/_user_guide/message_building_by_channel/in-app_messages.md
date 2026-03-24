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

# [![Braze-Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} In-App-Nachrichten

> In-App-Nachrichten ermöglichen es Ihnen, Ihren Nutzern Inhalte zukommen zu lassen, ohne sie mit Push-Benachrichtigungen zu stören, da diese Nachrichten nicht außerhalb der App des Nutzers angezeigt werden und nicht auf dessen Startbildschirm erscheinen. 

Angepasste und maßgeschneiderte In-App-Nachrichten verbessern das Nutzererlebnis und helfen Ihrer Zielgruppe, den größten Nutzen aus Ihrer App zu ziehen. Mit einer Vielzahl von Layouts und Anpassungswerkzeugen, aus denen Sie wählen können, binden In-App-Nachrichten Ihre Nutzer mehr als je zuvor. Sie werden im Kontext angezeigt, haben eine geringere Dringlichkeit und werden zugestellt, wenn die Nutzer:innen in Ihrer App aktiv sind. Beispiele für In-App-Nachrichten finden Sie in unseren [Kundenberichten](https://www.braze.com/customers/).

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

![Slideup-In-App-Nachricht, die am unteren Rand des App-Bildschirms angezeigt wird. Das Slide-up enthält ein Symbolbild und eine kurze Nachricht.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

Modals erscheinen in der Mitte des Bildschirms des Geräts mit einem Overlay, das sie von Ihrer App im Hintergrund abhebt. Sie eignen sich perfekt, um Ihren Nutzern ganz unaufdringlich vorzuschlagen, von einem Verkauf oder einer Werbeaktion zu profitieren.

![Modale In-App-Nachricht, die in der Mitte einer App und Website als Dialogfeld angezeigt werden. Das Modal enthält ein Bild, eine Kopfzeile, einen Text für die Nachricht und zwei Buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Fullscreen %}

Vollbildnachrichten sind genau das, was Sie erwarten - sie nehmen den gesamten Bildschirm des Geräts ein! Dieser Nachrichtentyp eignet sich hervorragend, wenn Sie die Aufmerksamkeit Ihrer Nutzer wirklich benötigen, z. B. bei obligatorischen App-Updates.

![Bildschirmfüllende In-App-Nachricht, die einen App-Bildschirm einnimmt. Die Vollbild-Nachricht umfasst ein großes Bild, eine Kopfzeile, den Text der Nachricht und zwei Buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% endtabs %}

Zusätzlich zu diesen Standard-Nachrichten-Templates können Sie Ihre Nachrichten auch mithilfe von benutzerdefinierten HTML-In-App-Nachrichten, Web-Modalen mit CSS oder Web-E-Mail-Erfassungsformularen weiter anpassen. Weitere Informationen finden Sie unter [Anpassung]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Templates für In-App-Nachrichten

In-App-Nachrichten werden als vordefinierte In-App-Nachrichten zugestellt, wenn **die Option „Kampagnenberechtigung vor der Anzeige erneut prüfen“** ausgewählt ist oder wenn ein der folgenden Liquid-Tags in der Nachricht vorhanden ist:

- `canvas_entry_properties`
- `connected_content`
- SMS-Variablen wie z.B. {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Dies bedeutet, dass das Gerät zu Beginn der Sitzung den Auslöser dieser In-App-Nachricht anstelle der gesamten Nachricht empfängt. Wenn die:der Nutzer:in die In-App-Nachricht triggert, wird ihr:sein Gerät eine Anfrage an das Netzwerk stellen, um die eigentliche Nachricht abzurufen.

{% alert note %}
Die Nachricht wird nicht zugestellt, wenn das Gerät keinen Internetzugang hat. Die Nachricht wird möglicherweise nicht zugestellt, wenn die Liquid-Logik zu lange für die Auflösung benötigt.
{% endalert %}

## Abbrechen

Bei Braze kommt es zu einem Abbruch, wenn eine Nutzer:in eine Aktion ausführt, die sie zum Empfang einer Nachricht berechtigt, sie die Nachricht jedoch nicht erhält, weil sie aufgrund der Liquid-Logik als nicht berechtigt markiert ist. Zum Beispiel:

1. Herr Sam führt eine Aktion durch, die eine E-Mail-Kampagne triggern sollte.
2. Der Text der E-Mail enthält eine Liquid-Logik, die besagt, dass diese E-Mail nicht versendet werden soll, wenn die Punktzahl eines angepassten Attributs unter 50 liegt.
3. Die benutzerdefinierte Bewertung der angepassten Attribute von Herrn Sam beträgt 20.
4. Braze erkennt, dass Sam diese E-Mail nicht erhalten sollte, und die E-Mail wird abgebrochen.
5. Ein Abbruchereignis wird protokolliert.

Da In-App-Nachrichten jedoch ein Pull-Kanal sind, funktionieren Abbrüche bei ihnen etwas anders.

### Verhalten beim Abbruch einer In-App-Nachricht

In-App-Nachrichten werden zu Beginn der Sitzung vom Gerät abgerufen und auf dem Gerät zwischengespeichert, sodass die Nachricht unabhängig von der Qualität der Internetverbindung sofort an den Nutzer:in zugestellt werden kann. Wenn ein Nutzer:in beispielsweise fünf In-App-Nachrichten innerhalb seiner Sitzung erhält, werden ihm alle fünf zu Beginn der Sitzung angezeigt. Die Nachrichten werden lokal zwischengespeichert und erscheinen, wenn die definierten Auslöseereignisse eintreten (Sitzungsstart, Nutzer:in klickt auf einen Button, der ein angepasstes Event protokolliert, oder andere).

Mit anderen Worten: Die Entscheidung, ob eine In-App-Nachricht abgebrochen werden soll, wird getroffen**, bevor** der Auslöser eintritt. Um dies zu veranschaulichen, nehmen wir an, dass Sam aus dem E-Mail-Beispiel Push-Benachrichtigungen abonniert hat.

1. Herr Sam beginnt eine Sitzung, indem er eine von Braze unterstützte App auf seinem Smartphone startet.
2. Basierend auf den Zielgruppen-Kriterien der aktiven Kampagnen im Workspace könnte Herr Sam für fünf verschiedene Kampagnen in Frage kommen. Alle fünf werden auf ihr Telefon heruntergeladen und zwischengespeichert.
3. Herr Sam **hat keine** Aktionen durchgeführt, die diese Nachrichten triggern würden, jedoch könnten sie diese Nachrichten in der Sitzung erhalten.
4. Die Flüssigkeit in zwei der In-App-Nachrichten enthält Regeln, die Sam vom Empfang der Nachricht ausschließen (z. B. weil sein angepasstes Attribut „Punktzahl“ nicht hoch genug ist).
5. Sam erhält die beiden In-App-Nachrichten, die ihn ausschließen, nicht, jedoch werden ihm die anderen drei Nachrichten übermittelt.
6. Es werden keine Abbruchereignisse protokolliert.

Braze protokolliert in Sams Fall keine Abbruchereignisse, da dies nicht unserer Definition eines Abbruchs entspricht; Sam **hat **keine Aktionen durchgeführt, die die Nachrichten ausgelöst hätten. Bei In-App-Nachrichten führen Nutzer:innen den Auslöser nie tatsächlich aus, bevor Braze feststellt, dass sie die Nachricht nicht sehen sollten.

#### Standardmäßiges Verhalten beim Abbrechen von In-App-Nachrichten

[Vorlagenbasierte In-App-Nachrichten](#templated-in-app-messages) veranlassen das SDK dazu, erneut zu prüfen, ob eine Nachricht angezeigt werden soll, wenn das auslösende Ereignis eintritt. Dies weist ein abweichendes Abbruchverhalten auf. Zur Veranschaulichung betrachten wir das folgende Beispiel:

1. Herr Sam startet eine Braze-Sitzung, indem er eine von Braze unterstützte App auf seinem Smartphone öffnet.
2. Die Zielgruppenkriterien der aktiven Kampagnen zeigen, dass Sam für eine vorgefertigte In-App-Nachricht in Frage kommen könnte, sodass die Auslöseinformationen ohne die Nachrichtennutzlast an sein Gerät gesendet werden.
3. Sam wählt einen Button aus, der ein angepasstes Event protokolliert und die vordefinierte In-App-Nachricht triggert.
4. Das Gerät von Sam sendet eine Netzwerkanfrage, um die In-App-Nachricht abzurufen.
5. Die Liquid-Logik der Nachricht führt zu einem Abbruch, daher protokolliert Braze dies als Abbruch. Sam hat die Aktion zum Triggern vor dieser Auswertung durchgeführt.

##### Vergleich des Abbruchverhaltens von In-App-Nachrichten

Diese Tabelle vergleicht die In-App-Nachrichtenflüsse, die Sam erlebt hat:

| In-App-Nachricht | Abbrechen |
| --- | --- |
| Standard | Ein Abbruchereignis wurde nicht protokolliert, da Sam keine Aktionen durchgeführt hat, die eine Nachricht ausgelöst hätten.<br><br>Standardmäßige In-App-Nachrichten protokollieren keine Abbruchvorgänge, da ein Abbruch als „die Nachricht wurde trotz Ausführung der Aktion zum Triggern nicht angezeigt“ definiert ist. Da In-App-Nachrichten an das Gerät zugestellt werden, bevor die Aktionen getriggert werden, ist es nicht sinnvoll, In-App-Nachrichten aufgrund der Liquid-Logik als ausgelassen zu betrachten. |
| Template | Ein Abbruchereignis wurde protokolliert, da Sam die Aktion triggert hat, um die vorlagenbasierte In-App-Nachricht zu triggern, jedoch einen Abbruch in der Liquid-Vorlage erhalten hat. <br><br>Vorlagenbasierte In-App-Nachrichten werden abgebrochen, da die Liquid-Auswertung erst nach der Aktion, die den Trigger auslöst, erfolgt. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Mehr Ressourcen

Bevor Sie mit der Erstellung Ihrer eigenen In-App-Nachrichten-Kampagnen beginnen - oder In-App-Nachrichten in einer Multikanal-Kampagne verwenden - empfehlen wir Ihnen dringend, sich unseren [Leitfaden zur Vorbereitung von In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/) anzusehen. Dieser Leitfaden behandelt Fragen zu Targeting, Content und Konversion, die Sie bei der Erstellung von In-App-Nachrichten berücksichtigen sollten.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}
