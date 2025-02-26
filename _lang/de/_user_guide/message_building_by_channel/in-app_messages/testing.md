---
nav_title: Testen
article_title: Testen von In-App-Nachrichten
page_order: 4.5
description: "Dieser Referenzartikel behandelt den Wert des Testens Ihrer In-App-Nachrichten, erklärt, wie Sie sie testen können, und enthält eine Checkliste der Dinge, die Sie vor dem Versand beachten sollten."
channel:
  - in-app messages
  
---

# Testen von In-App-Nachrichten

> Es ist äußerst wichtig, dass Sie Ihre In-App-Nachrichten immer testen, bevor Sie Ihre Kampagnen versenden. Unsere Vorschau- und Testfunktionen bieten zwei Möglichkeiten, einen Blick auf Ihre In-App-Nachrichten zu werfen. Sie können Ihre Nachricht in der Vorschau anzeigen, um sie beim Verfassen zu visualisieren, und eine Testnachricht an Ihr Gerät oder das Gerät eines bestimmten Benutzers senden. Wir empfehlen Ihnen, beides in Anspruch zu nehmen.

## Vorschau

Sie können eine Vorschau Ihrer In-App-Nachricht sehen, während Sie sie verfassen. So können Sie sich ein Bild davon machen, wie Ihre endgültige Nachricht aus der Sicht des Benutzers aussehen wird.

{% alert warning %}
In der **Vorschau** ist die Ansicht Ihrer Nachricht möglicherweise nicht mit der tatsächlichen Darstellung auf dem Gerät des Benutzers identisch. Wir empfehlen immer, eine Testnachricht an ein Gerät zu senden, um sicherzustellen, dass Ihre Medien, Texte, Personalisierung und benutzerdefinierten Attribute korrekt generiert werden.
{% endalert %}

### Vorschau auf die Generierung von In-App-Nachrichten

Zeigen Sie in der Vorschau an, wie Ihre Nachricht bei einem zufälligen Benutzer, einem bestimmten Benutzer oder einem benutzerdefinierten Benutzer aussehen wird - die beiden letzteren sind besonders nützlich, wenn Ihre Nachricht eine Personalisierung oder mehrere Sprachen enthält. Sie können auch eine Vorschau der Nachrichten für mobile Geräte oder Tablets anzeigen lassen, um eine bessere Vorstellung davon zu bekommen, was die Nutzer erleben werden.

![Tab "Verfassen" beim Erstellen einer In-App-Nachricht mit einer Vorschau, wie die Nachricht aussehen wird. Ein:e Nutzer:in ist nicht ausgewählt, so dass das im Body-Bereich hinzugefügte Liquid so angezeigt wird, wie es ist.][1]

Braze verfügt über drei Generationen von In-App-Nachrichten. Sie können genau festlegen, an welche Geräte Ihre Nachrichten gesendet werden sollen, je nachdem, welche Generation sie unterstützen.

![Umschalten zwischen den Generationen bei der Vorschau einer In-App-Nachricht.][2]{: height="50%" width="50%"}

## Testen

{% alert warning %}
Um einen Test entweder an [Inhaltstestgruppen]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) oder einzelne Nutzer:innen zu senden, muss Push auf Ihren Testgeräten vor dem Senden aktiviert werden. <br><br>Sie müssen zum Beispiel Push auf Ihrem iOS-Gerät aktiviert haben, um auf die Benachrichtigung zu tippen, bevor die Testnachricht angezeigt wird.
{% endalert %}

### Nachrichtenvorschau als Nutzer:in anzeigen

Auf der Registerkarte **Test** können Sie auch eine Vorschau der Nachrichten anzeigen, als ob Sie ein Benutzer wären. Sie können eine:n bestimmte:n oder zufällige:n Nutzer:in auswählen oder eine:n angepasste:n Nutzer:in erstellen.

![Tab Testen beim Erstellen einer In-App-Nachricht. "Vorschau der Nachricht als Nutzer:in" ist auf "Angepasster Nutzer" eingestellt, wobei die verfügbaren Felder des Profils als konfigurierbare Optionen erscheinen.][3]

### Test-Checkliste

- Werden die Bilder und Medien angezeigt und verhalten sie sich wie erwartet?
- Funktioniert das Liquid wie erwartet? Haben Sie einen [Standardattribut-Wert ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) für den Fall vorgesehen, dass das Liquid keine Informationen liefert?
- Ist Ihr Text klar, prägnant und korrekt?
- Zeigen Ihre Schaltflächen dem Benutzer, wohin er gehen soll?

[1]: {%image_buster /assets/img/in-app-message-preview.png %}
[2]: {% image_buster /assets/img/iam-generations.gif %}
[3]: {% image_buster /assets/img/iam-user-preview.png %}
