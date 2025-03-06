---
nav_title: "Über In-App-Nachrichten"
article_title: Über In-App-Nachrichten
page_order: 0
page_type: reference
description: "Dieser Referenzartikel gibt einen kurzen Überblick über In-App-Nachrichten, mögliche Anwendungsfälle und Standardnachrichtentypen."
channel:
  - in-app messages
search_rank: 4.9
---

# [![Braze-Lernkurs]](https://learning.braze.com/messaging-channels-in-app-in-browser)([{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"}Über In-App-Nachrichten

> In-App-Nachrichten sind für viele Dinge gut. Sie sind inhaltsreich und haben ein geringeres Gefühl der Dringlichkeit, da diese Nachrichten nicht außerhalb der App des Benutzers zugestellt werden und den Startbildschirm nicht stören. In-App-Nachrichten existieren innerhalb Ihrer App (daher der Name), sind mit einem Kontext versehen und fast nie unerwünscht! Sie werden immer dann zugestellt, wenn der Nutzer:innen in Ihrer App aktiv ist.

Beispiele für In-App-Nachrichten finden Sie in unseren [Fallstudien][1].

## Potenzielle Anwendungsfälle

Mit dem reichhaltigen Angebot an Content, der In-App-Nachrichten bieten, können Sie diesen Kanal für eine Vielzahl von Anwendungsfällen nutzen:

| Anwendungsfall | Erklärung |
| --- | --- |
| Push-Priming | Führen Sie eine [Push-Priming-Kampagne][2] mit einer reichhaltigen In-App-Nachricht durch, um Ihren Kunden die Vorteile einer Push-Erlaubnis für Ihre App oder Website zu verdeutlichen, und fordern Sie sie auf, die Push-Erlaubnis zu erteilen.
| Verkäufe und Aktionen | Verwenden Sie modale In-App-Nachrichten, um Kund:innen mit visuell ansprechenden Medien zu begrüßen, die statische Aktionscodes oder Angebote enthalten. Ermutigen Sie sie zu Käufen oder Konversionen, die sie sonst nicht getätigt hätten. |
| Förderung zur Annahme von Features | Ermuntern Sie Ihre Kunden, andere Teile Ihrer App zu nutzen oder einen Service in Anspruch zu nehmen. |
| Hochgradig personalisierte Kampagnen | Platzieren Sie In-App-Nachrichten als das Erste, was Ihre Kunden sehen, wenn sie Ihre App oder Website betreten. Fügen Sie einige Features zur Personalisierung von Braze hinzu, wie z. B. [Connected-Content][3], um Nutzer:innen zum Handeln zu bewegen und so Ihre Reichweite zu erhöhen.
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

![Slideup-In-App-Nachricht, die am unteren Rand des App-Bildschirms erscheint. Das Slideup enthält ein Symbolbild und eine kurze Nachricht.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Modal %}

Modals werden in der Mitte des Gerätebildschirms mit einer Bildschirmüberlagerung angezeigt, die sie von Ihrer App im Hintergrund abhebt. Sie eignen sich perfekt, um Ihren Nutzern ganz unaufdringlich vorzuschlagen, von einem Verkauf oder einer Werbeaktion zu profitieren.

![Modale In-App-Nachricht, die in der Mitte einer App und Website als Dialogfeld angezeigt wird. Das Modal enthält ein Bild, eine Kopfzeile, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Vollbildschirm %}

Vollbildnachrichten sind genau das, was Sie erwarten - sie nehmen den gesamten Bildschirm des Geräts ein! Dieser Nachrichtentyp eignet sich hervorragend, wenn Sie die Aufmerksamkeit Ihrer Nutzer wirklich benötigen, z. B. bei obligatorischen App-Updates.

![Bildschirmfüllende In-App-Nachricht, die einen App-Bildschirm einnimmt. Die Nachricht im Vollbildmodus enthält ein großes Bild, eine Kopfzeile, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

Zusätzlich zu diesen vorgefertigten Templates für Nachrichten können Sie Ihr Messaging auch mit angepassten HTML In-App-Nachrichten, Web-Modals mit CSS oder Web-Formularen zur Erfassung von E-Mails anpassen. Weitere Informationen finden Sie unter [Anpassung][4].

## Mehr Ressourcen

Bevor Sie mit der Erstellung Ihrer eigenen In-App-Nachrichten-Kampagnen beginnen - oder In-App-Nachrichten in einer Multikanal-Kampagne verwenden - empfehlen wir Ihnen dringend, sich unseren [Leitfaden zur Vorbereitung von In-App-Nachrichten][5] anzusehen. Dieser Leitfaden behandelt Fragen zu Targeting, Content und Konversion, die Sie bei der Erstellung von In-App-Nachrichten berücksichtigen sollten.


[1]: https://www.braze.com/customers
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/
[6]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/
