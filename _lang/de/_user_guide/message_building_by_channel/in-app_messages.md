---
nav_title: "In-App-Nachrichten"
article_title: In-App-Nachrichten
page_order: 2
alias: /in-app_messages/
layout: dev_guide
guide_top_header: "In-App-Nachrichten"
guide_top_text: "In-App-Nachrichten helfen Ihnen, Inhalte an Ihre Nutzer:innen zu übermitteln, ohne sie mit einer Push-Benachrichtigung zu unterbrechen, denn diese Nachrichten werden nicht außerhalb der App des Nutzers zugestellt und stören nicht den Startbildschirm. <br><br>Angepasste und maßgeschneiderte In-App-Nachrichten verbessern das Nutzererlebnis und helfen Ihrer Zielgruppe, den größten Nutzen aus Ihrer App zu ziehen. Mit einer Vielzahl von Layouts und Anpassungswerkzeugen, aus denen Sie wählen können, binden In-App-Nachrichten Ihre Nutzer mehr als je zuvor. Sie sind kontextbezogen, haben eine geringere Dringlichkeit und werden zugestellt, wenn der Nutzer:innen in Ihrer App aktiv ist. Beispiele für In-App-Nachrichten finden Sie in unseren <a href='https://www.braze.com/customers'>Kund:in-Storys</a>."
description: "Auf dieser Landing Page finden Sie alles rund um In-App-Nachrichten. Hier finden Sie Artikel über die Erstellung von In-App-Nachrichten, den Drag-and-Drop-Editor, die Anpassung Ihrer Nachrichten, die Berichterstattung und vieles mehr."
channel:
  - in-app messages
search_rank: 5
guide_featured_title: "Beliebte Artikel"
guide_featured_list:
- name: "Drag-and-Drop-Editor"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Klassischer Editor"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Kreative Details"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/
  image: /assets/img/braze_icons/brush-02.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: "Testen"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/testing/
  image: /assets/img/braze_icons/beaker-02.svg
- name: "Berichterstattung"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: "Dark Mode"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/dark-mode/
  image: /assets/img/braze_icons/phone-02.svg
- name: "App Store Bewertungsaufforderung"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/ios_app_rating_prompt/
  image: /assets/img/braze_icons/star-01.svg
- name: "Einfache Umfrage"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey/
  image: /assets/img/braze_icons/bar-chart-07.svg
- name: "Lokale in Nachrichten"
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: "Bewährte Praktiken"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "FAQ"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Braze Lernkurse]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} Potenzielle Anwendungsfälle

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

![Slideup In-App-Nachricht, die am unteren Rand des App-Bildschirms erscheint. Das Slide-Up enthält ein Symbolbild und eine kurze Nachricht.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Modal %}

Modals erscheinen in der Mitte des Bildschirms des Geräts mit einem Overlay, das sie von Ihrer App im Hintergrund abhebt. Sie eignen sich perfekt, um Ihren Nutzern ganz unaufdringlich vorzuschlagen, von einem Verkauf oder einer Werbeaktion zu profitieren.

![Modale In-App-Nachricht, die in der Mitte einer App und Website als Dialog erscheint. Das Modal enthält ein Bild, eine Kopfzeile, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Fullscreen %}

Vollbildnachrichten sind genau das, was Sie erwarten - sie nehmen den gesamten Bildschirm des Geräts ein! Dieser Nachrichtentyp eignet sich hervorragend, wenn Sie die Aufmerksamkeit Ihrer Nutzer wirklich benötigen, z. B. bei obligatorischen App-Updates.

![In-App-Nachricht im Vollbildmodus, die den Bildschirm einer App einnimmt. Die Nachricht im Vollbildmodus enthält ein großes Bild, eine Kopfzeile, einen Nachrichtentext und zwei Buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

Zusätzlich zu diesen vorgefertigten Templates für Nachrichten können Sie Ihr Messaging auch mit angepassten HTML In-App-Nachrichten, Web-Modals mit CSS oder Web-Formularen zur Erfassung von E-Mails anpassen. Weitere Informationen finden Sie unter [Anpassung]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Mehr Ressourcen

Bevor Sie mit der Erstellung Ihrer eigenen In-App-Nachrichten-Kampagnen beginnen - oder In-App-Nachrichten in einer Multikanal-Kampagne verwenden - empfehlen wir Ihnen dringend, sich unseren [Leitfaden zur Vorbereitung von In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/) anzusehen. Dieser Leitfaden behandelt Fragen zu Targeting, Content und Konversion, die Sie bei der Erstellung von In-App-Nachrichten berücksichtigen sollten.
