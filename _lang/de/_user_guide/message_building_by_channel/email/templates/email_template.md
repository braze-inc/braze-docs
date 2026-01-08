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

Als Nächstes können Sie aus vorgefertigten Braze Templates wählen, ein neues Template erstellen oder ein bestehendes Template (einfach oder [mobil responsiv]({{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates)) bearbeiten.

![Eine E-Mail-Vorlage für den Frühjahrsverkauf eines Unternehmens mit der Möglichkeit, den Drag-and-Drop-Editor oder den HTML-Editor auszuwählen oder aus Braze-Vorlagen auszuwählen.]({% image_buster /assets/img/email_templates/template2.png %})

{% alert note %}
Vorhandene benutzerdefinierte HTML-Vorlagen müssen mit dem Drag-and-Drop-Editor neu erstellt werden.
{% endalert %}

## Schritt 3: Passen Sie Ihr Template an

Nachdem Sie Ihr Kundenerlebnis ausgewählt haben, haben Sie nun die Opportunity, Ihre E-Mail-Template kreativ anzupassen. Sie können HTML verwenden, um Ihr Branding im HTML-Editor zu erstellen und zu emulieren, oder eine Vielzahl von [kreativen Details]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) im Drag-and-Drop-Editor einfügen.

### Einschließlich eines Links zum Abmelden

Wenn Sie bei der Gestaltung Ihrer E-Mail-Vorlage keinen Abmeldelink einfügen, wird Braze Sie auffordern, diesen in Ihre E-Mail einzufügen, da er in allen Marketing-E-Mails gesetzlich vorgeschrieben ist. Sie können diesen Link zum Abmelden als Fußzeile am Ende Ihrer E-Mails einfügen, indem Sie den Liquid-Tag {% raw %}``${email_footer}``{% endraw %} verwenden oder in Ihrer Template [die Fußzeile anpassen]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer).

## Schritt 4: Prüfen Sie auf E-Mail-Fehler

E-Mail-Fehler werden auf der Registerkarte **Verfassen** des Nachrichten-Workflows angezeigt. Fehler hindern Sie am Vorankommen. "Warnungen" sind Hinweise, die Ihnen helfen sollen, die besten Praktiken zu befolgen. Je nach Ihrem Unternehmen können Sie sie auch ignorieren.

![Fehler- und Warnliste aus einer Beispiel-E-Mail.]({% image_buster /assets/img/dnd_compose_error.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Hier finden Sie eine Liste der Fehler, die in unserem Editor berücksichtigt werden:

- Falsche Liquid-Syntax
- [E-Mail-Textkörper größer als 400kb; es wird dringend empfohlen, dass sie weniger als 102kb groß sind.]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/)
- Templates ohne Abmeldelink
- E-Mails mit leerem **Text** oder **Betreff**
- E-Mails ohne Abmeldelink

## Schritt 5: Vorschau und Test Ihrer Nachricht

Nachdem Sie Ihr Template erstellt haben, können Sie es testen, bevor Sie es versenden.

Wählen Sie unten auf dem Übersichtsbildschirm **Vorschau und Test** aus. Hier können Sie eine Vorschau darauf sehen, wie Ihre E-Mail im Posteingang eines Kunden erscheinen wird. Wenn Sie **Vorschau als Benutzer** ausgewählt haben, können Sie Ihre E-Mail als zufälliger Benutzer anzeigen lassen, einen bestimmten Benutzer auswählen oder einen benutzerdefinierten Benutzer erstellen. So können Sie testen, ob Ihre Connected-Content- und Personalisierungsaufrufe wie gewünscht funktionieren. 

Dann können Sie **Vorschau-Link kopieren**, um einen Vorschau-Link zu erzeugen und zu kopieren, der zeigt, wie die E-Mail für einen zufälligen Nutzer:innen aussehen wird. Der Link bleibt sieben Tage lang bestehen, bevor er erneuert werden muss.

Sie können auch zwischen der Desktop-, der Mobil- und der Klartextansicht wechseln, um ein Gefühl dafür zu bekommen, wie Ihre Nachricht in verschiedenen Kontexten erscheinen wird.

{% alert tip %}
Sind Sie neugierig, wie Ihre E-Mails für Nutzer:innen im Dark Mode aussehen? Wählen Sie den Schalter für die **Vorschau im dunklen Modus** im Bereich **Vorschau und Test** (nur im Drag & Drop-Editor).
{% endalert %}

Wenn Sie für eine abschließende Prüfung bereit sind, wählen Sie **Senden testen** und senden Sie eine Testnachricht an sich selbst oder an eine Gruppe von Inhaltstestern, um sicherzustellen, dass Ihre E-Mail auf einer Vielzahl von Geräten und E-Mail-Clients korrekt angezeigt wird.

![Beispiel für eine Vorschau einer E-Mail, die zu Testzwecken verschickt wird.]({% image_buster /assets/img_archive/newEmailTest.png %})

Wenn Sie Probleme mit Ihrer Vorlage sehen oder Änderungen vornehmen möchten, wählen Sie **E-Mail bearbeiten**, um zum Editor zurückzukehren.

## Schritt 6: Template speichern

Speichern Sie Ihr Template, indem Sie **Template speichern** auswählen. Jetzt können Sie diese Vorlage in jeder beliebigen Kampagne oder Canvas-Komponente verwenden. Um auf Ihre Vorlage zuzugreifen, wählen Sie die Bearbeitungsfunktion, mit der Sie sie erstellt haben, und wählen Sie sie dann aus der Liste der verfügbaren Vorlagen aus.

{% alert note %}
Wenn Sie Änderungen an einer bestehenden Vorlage vornehmen, werden diese Änderungen nicht in Kampagnen übernommen, die mit früheren Versionen dieser Vorlage erstellt wurden.
{% endalert %}

### Verwaltung Ihrer Vorlagen

Wenn Sie weitere E-Mail Templates erstellen, können Sie die E-Mail Templates [duplizieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates) und [archivieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates). Erfahren Sie mehr über die Erstellung und Verwaltung Ihrer Bibliothek von Vorlagen und kreativen Inhalten unter [Vorlagen und Medien]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

### Verwendung Ihrer Vorlagen in API-Kampagnen

Um Ihre E-Mail für eine API-Kampagne zu verwenden, benötigen Sie eine `email_template_id`, die Sie am Ende jeder in Braze erstellten E-Mail-Template finden.

![API Bezeichner, der sich am unteren Rand eines E-Mail Templates befindet.]({% image_buster /assets/img/email_templates/template5.png %})

### Kommentare zu E-Mail Templates

Sie können E-Mail-Vorlagen im Drag-and-Drop-Editor gemeinsam bearbeiten und kommentieren. 

1. Wählen Sie den Content-Block oder die Zeile in der E-Mail aus, zu der Sie einen Kommentar abgeben möchten.
2. Wählen Sie das Symbol <i class="fas fa-comment"></i> Kommentar.
3. Geben Sie Ihren Kommentar in der Seitenleiste ein und wählen Sie dann **Senden**.
4. Nachdem Sie Ihre Kommentare eingegeben haben, wählen Sie **Fertig**.
5. Wählen Sie **Template speichern**, um Ihre Kommentare zu speichern.

Nachdem Ihre Vorlage gespeichert wurde, sehen die Benutzer Symbole über nicht beantworteten Kommentaren. Wählen Sie **Auflösen**, um diese Kommentare aufzulösen.

![Ein Template für E-Mails mit dem Kommentar "Sieht gut aus".]({% image_buster /assets/img/email_templates/template_comment.png %})

Antworten auf häufig gestellte Fragen zu E-Mail Templates finden Sie in unseren [FAQ zu Templates]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).

