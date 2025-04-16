---
nav_title: Erstellen einer E-Mail-Vorlage
article_title: Erstellen einer E-Mail-Vorlage
page_order: 0
description: "Dieser Referenzartikel beschreibt, wie Sie E-Mail Templates erstellen, anpassen und verwalten."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# Erstellen einer E-Mail-Vorlage

> Das Braze-Dashboard verfügt über einen E-Mail-Vorlagen-Editor, mit dem Sie maßgeschneiderte, aufmerksamkeitsstarke E-Mails erstellen und zur späteren Verwendung in Kampagnen speichern können. Sie können auch Ihre eigene [HTML-E-Mail-Vorlage]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/) hochladen.

## Schritt 1: Navigieren Sie zum Editor für E-Mail-Vorlagen

Gehen Sie zu **Vorlagen** > **E-Mail-Vorlagen**.

## Schritt 2: Wählen Sie Ihre Bearbeitungserfahrung 

Wählen Sie zwischen dem **Drag-and-Drop-Editor** oder dem **HTML-Editor** für Ihre Bearbeitung. 

Als Nächstes können Sie aus vorgefertigten Braze-Vorlagen wählen, eine neue Vorlage erstellen oder eine vorhandene Vorlage bearbeiten (einfach oder [mobile responsive][8]).

![Eine E-Mail-Template für den Frühjahrsverkauf eines Unternehmens mit der Möglichkeit, den Drag-and-Drop-Editor oder den HTML-Editor auszuwählen oder aus Braze-Templates auszuwählen.][2]

{% alert note %}
Vorhandene benutzerdefinierte HTML-Vorlagen müssen mit dem Drag-and-Drop-Editor neu erstellt werden.
{% endalert %}

## Schritt 3: Passen Sie Ihr Template an

Nachdem Sie Ihr Kundenerlebnis ausgewählt haben, haben Sie nun die Opportunity, Ihre E-Mail-Template kreativ anzupassen. Sie können HTML verwenden, um Ihr Branding im HTML-Editor zu erstellen und zu emulieren, oder eine Vielzahl von [kreativen Details]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) im Drag-and-Drop-Editor einfügen.

### Einschließlich eines Links zum Abmelden

Wenn Sie bei der Gestaltung Ihrer E-Mail-Vorlage keinen Abmeldelink einfügen, wird Braze Sie auffordern, diesen in Ihre E-Mail einzufügen, da er in allen Marketing-E-Mails gesetzlich vorgeschrieben ist. Sie können diesen Link zum Abmelden als Fußzeile am Ende Ihrer E-Mails einfügen, indem Sie den Liquid-Tag {% raw %}``${email_footer}``{% endraw %} verwenden oder in Ihrer Template [die Fußzeile anpassen]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer).

## Schritt 4: Prüfen Sie auf E-Mail-Fehler

E-Mail-Fehler werden auf der Registerkarte **Verfassen** des Nachrichten-Workflows angezeigt. Fehler hindern Sie am Vorankommen. "Warnungen" sind Hinweise, die Ihnen helfen sollen, die besten Praktiken zu befolgen. Je nach Ihrem Unternehmen können Sie sie auch ignorieren.

![Liste der Fehler und Warnungen aus einer Beispiel E-Mail.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

Hier finden Sie eine Liste der Fehler, die in unserem Editor berücksichtigt werden:

- Falsche Liquid-Syntax
- [E-Mail-Textkörper größer als 400kb; es wird dringend empfohlen, dass diese weniger als 102kb groß sind][7]
- Templates ohne Abmeldelink
- E-Mails mit leerem **Text** oder **Betreff**
- E-Mails ohne Abmeldelink

## Schritt 5: Vorschau und Test Ihrer Nachricht

Nachdem Sie Ihr Template erstellt haben, können Sie es testen, bevor Sie es versenden.

Klicken Sie am unteren Rand des Übersichtsbildschirms auf **Vorschau und Test**. Hier können Sie eine Vorschau darauf sehen, wie Ihre E-Mail im Posteingang eines Kunden erscheinen wird. Wenn Sie **Vorschau als Benutzer** ausgewählt haben, können Sie Ihre E-Mail als zufälliger Benutzer anzeigen lassen, einen bestimmten Benutzer auswählen oder einen benutzerdefinierten Benutzer erstellen. So können Sie testen, ob Ihre Connected-Content- und Personalisierungsaufrufe wie gewünscht funktionieren.

Sie können auch zwischen der Desktop-, der Mobil- und der Klartextansicht wechseln, um ein Gefühl dafür zu bekommen, wie Ihre Nachricht in verschiedenen Kontexten erscheinen wird.

Wenn Sie für eine abschließende Prüfung bereit sind, wählen Sie **Senden testen** und senden Sie eine Testnachricht an sich selbst oder an eine Gruppe von Inhaltstestern, um sicherzustellen, dass Ihre E-Mail auf einer Vielzahl von Geräten und E-Mail-Clients korrekt angezeigt wird.

![Beispiel für eine Vorschau einer E-Mail, die zu Testzwecken versendet wird.][6]

Wenn Sie Probleme mit Ihrer Vorlage feststellen oder Änderungen vornehmen möchten, klicken Sie auf **E-Mail bearbeiten**, um zum Editor zurückzukehren.

## Schritt 6: Speichern Sie Ihr Template

Stellen Sie sicher, dass Sie Ihre Template speichern, indem Sie auf **Template speichern** klicken. Jetzt können Sie diese Vorlage in jeder beliebigen Kampagne oder Canvas-Komponente verwenden. Um auf Ihre Vorlage zuzugreifen, wählen Sie die Bearbeitungsfunktion, mit der Sie sie erstellt haben, und wählen Sie sie dann aus der Liste der verfügbaren Vorlagen aus.

{% alert note %}
Wenn Sie Änderungen an einer bestehenden Vorlage vornehmen, werden diese Änderungen nicht in Kampagnen übernommen, die mit früheren Versionen dieser Vorlage erstellt wurden.
{% endalert %}

### Verwaltung Ihrer Vorlagen

Wenn Sie weitere E-Mail Templates erstellen, können Sie die E-Mail Templates [duplizieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates) und [archivieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates). Erfahren Sie mehr über die Erstellung und Verwaltung Ihrer Bibliothek von Vorlagen und kreativen Inhalten unter [Vorlagen und Medien]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

### Verwendung Ihrer Vorlagen in API-Kampagnen

Um Ihre E-Mail für eine API-Kampagne zu verwenden, benötigen Sie eine `email_template_id`, die Sie am Ende jeder in Braze erstellten E-Mail-Template finden.

![API Bezeichner, der sich am unteren Rand eines E-Mail Templates befindet.][5]

### Kommentare zu E-Mail Templates

Sie können E-Mail-Vorlagen im Drag-and-Drop-Editor gemeinsam bearbeiten und kommentieren. 

1. Klicken Sie auf den Inhaltsblock oder die Zeile in der E-Mail, zu der Sie einen Kommentar abgeben möchten.
2. Wählen Sie das Symbol <i class="fas fa-comment"></i> Kommentar.
3. Geben Sie Ihren Kommentar in der Seitenleiste ein und klicken Sie dann auf **Absenden**.
4. Nachdem Sie Ihre Kommentare eingegeben haben, klicken Sie auf **Fertig**.
5. Klicken Sie auf **Vorlage speichern**, um Ihre Kommentare zu speichern.

Nachdem Ihre Vorlage gespeichert wurde, sehen die Benutzer Symbole über nicht beantworteten Kommentaren. Wählen Sie **Auflösen**, um diese Kommentare aufzulösen.

![Ein Kommentar in einer E-Mail-Template, der lautet "Sieht gut aus".][10]

Antworten auf häufig gestellte Fragen zu E-Mail-Vorlagen finden Sie in unseren [Vorlagen FAQ][9].

[1]: {% image_buster /assets/img/dnd_compose_error.png %}
[2]: {% image_buster /assets/img/email_templates/template2.png %}
[3]: {% image_buster /assets/img/email_templates/template3.png %}
[4]: {% image_buster /assets/img/email_templates/template4.png %}
[5]: {% image_buster /assets/img/email_templates/template5.png %}
[6]: {% image_buster /assets/img_archive/newEmailTest.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[8]: {{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[10]: {% image_buster /assets/img/email_templates/template_comment.png %}
