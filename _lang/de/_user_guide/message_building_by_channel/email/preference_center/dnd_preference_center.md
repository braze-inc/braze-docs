---
nav_title: Drag-and-Drop-E-Mail-Einstellungscenter
article_title: Drag-and-Drop-E-Mail-Einstellungscenter
alias: "/dnd_preference_center/"
description: "Hier erfahren Sie, wie Sie mit dem Drag-and-Drop-Editor ein Präferenzzentrum für E-Mails erstellen."
page_order: 2
---

# Erstellen Sie ein E-Mail-Einstellungscenter per Drag-and-Drop

> Mit dem Drag-and-Drop-Editor können Sie ein Präferenzzentrum erstellen und anpassen. So bestimmen Sie wer welche Mitteilungen erhält. Bis zu 50 Präferenzzentren pro Workspace sind möglich.

## Schritt 1: Präferenzzentrum für E-Mails erstellen

Erstellen Sie ein Präferenzcenter, indem Sie zu **Zielgruppe** > **Abonnements** > **E-Mail-Präferenzcenter** navigieren.

Hier wird eine Liste der benutzerdefinierten Einstellungszentren angezeigt. Wählen Sie **Neu erstellen**, um ein neues Einstellungszentrum zu erstellen, oder wählen Sie den Namen eines bestehenden, um Änderungen vorzunehmen.

![Eine Liste der benutzerdefinierten Einstellungszentren mit Name, Beschreibung, Typ, Status, Datum der letzten Bearbeitung und Erstellung durch den Benutzer.][1]

## Schritt 2: Präferenzzentrum benennen

Die Namen der Präferenzzentren dürfen nur alphanumerische Zeichen, Bindestriche oder Unterstriche enthalten. Der Name, den Sie angeben, bestimmt die Syntax des generierten Liquid-Tags. 

Dieses Liquid-Tag kann in alle ausgehenden E-Mail-Kampagnen oder Canvas-Schritte eingefügt werden und leitet Benutzer zum Einstellungscenter.

![Ein Beispiel für Liquid für ein Präferenzzentrum.][2]

## Schritt 3: Hinzufügen von Abonnementgruppen zum Präferenzcenter

Wählen Sie **Editor starten**, um mit der Gestaltung Ihres Einstellungscenters im Drag-and-Drop-Editor zu beginnen.

### Verfügbare Abonnementgruppen definieren

Um festzulegen, welche Abonnementgruppen im Einstellungscenter angezeigt werden sollen, klicken Sie auf die Schaltfläche **\+ Abonnementgruppen hinzufügen**, um ein Modal zu öffnen, in dem die gewünschten Abonnementgruppen ausgewählt werden können. Nach der Auswahl klicken Sie auf die Schaltfläche **Abonnementgruppen hinzufügen**, um sie dem Einstellungscenter hinzuzufügen.

Sie können die ausgewählten Abo-Gruppen weiter konfigurieren, wenn Sie den Smartblock auswählen und die Blockeigenschaften anpassen.
- Anpassen der Reihenfolge der Abonnementgruppen
- Zusätzliche Abonnementgruppen hinzufügen oder entfernen
- Beschreibungen einbeziehen
- Fügen Sie ein Kontrollkästchen **Alle abonnieren** hinzu oder entfernen Sie es, um den Benutzer für alle in diesem Block angezeigten Abonnementgruppen zu registrieren.
- Fügen Sie ein Kontrollkästchen **Von allen abmelden** hinzu oder entfernen Sie es. Dadurch wird der Benutzer von allen in diesem Block angezeigten Abonnementgruppen abgemeldet.

![Ein Beispiel für ein Präferenzzentrum mit den Optionen, alle Nachrichten, Werbung, Newsletter und wöchentliche E-Mails zu abonnieren oder sich von allen abzumelden.][3]{: style="max-width:38%;"} ![][4]{: style="max-width:45%;"}

Der Button **Von allen abmelden** unten kann nicht entfernt werden und bewirkt, dass man [von allen Nachrichten abgemeldet wird]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states).

## Schritt 4: Passen Sie das Einstellungscenter mit dem Drag-and-Drop-Editor an

### Gemeinsame Stile festlegen

Auf der Registerkarte **Gemeinsame Stile** können Sie festlegen, dass bestimmte Stile auf alle relevanten Blöcke in Ihrem Einstellungscenter angewendet werden sollen. Die hier festgelegten Stile werden auf die gesamte Nachricht angewendet, außer wenn Sie sie bei einem bestimmten Block außer Kraft setzen. Um die Gestaltung zu vereinfachen, können Sie die Stile auf Seitenebene einrichten, bevor Sie sie auf Blockebene anpassen.

![Ein Beispiel für gängige Stileinstellungen für Text, Schaltflächen und Links.][5]{: style="max-width:45%;"}

{% alert tip %}
Um zu den gemeinsamen Stilen zurückzukehren, klicken Sie bei den Blockeigenschaften auf das "X". Nun wählen Sie den Nachrichtencontainer, den "X"-Button oder den Hintergrund aus.
{% endalert %}

## Komponenten des Präferenzzentrums per Drag-and-Drop verschieben

Der Drag-and-Drop-Editor vereinfacht die Erstellung von Präferenzzentren mit Zeilen und Blöcken. Alle Blöcke müssen in einer Reihe platziert werden.

{% tabs %}
{% tab Zeilen %}

Zeilen sind Struktureinheiten, die den horizontalen Aufbau eines Abschnitts der Nachricht mit Hilfe von Zellen definieren.

![Möglichkeit zur Auswahl der Zeilenart in Ihrer Nachricht.]({% image_buster /assets/img/preference_center/preference_center6.png %}){: style="max-width:45%;"}

Wenn eine Zeile ausgewählt ist, können Sie im Bereich Spaltenanpassung die gewünschte Anzahl von Spalten hinzufügen oder entfernen, um verschiedene Inhaltselemente nebeneinander anzuordnen. Die Größe der Spalten können Sie mit dem Schieberegler anpassen.

![Möglichkeit zur Anpassung von Spalteneigenschaften wie Hintergrundfarbe, Rahmenstil, Rahmenradius und Padding.]({% image_buster /assets/img/preference_center/preference_center7.png %}){: style="max-width:45%;"}

Formatieren Sie die Zeilen- und Spalteneigenschaften, bevor Sie die Blöcke in den Zeilen formatieren. Sie können die Abstände und die Ausrichtung an vielen Stellen anpassen. Wenn Sie also von der Basis ausgehen, ist es einfacher, sie nach und nach zu bearbeiten.

{% endtab %}
{% tab Blöcke %}

Blöcke stehen für verschiedene Arten von Nachrichteninhalten. Ziehen Sie eine Zeile in ein bestehendes Zeilensegment, das sich automatisch an die Zellenbreite anpasst.

![Möglichkeit zur Auswahl von Blöcken einschließlich Titel, Absatz, Button, Bild und Abstandshalter.]({% image_buster /assets/img/preference_center/preference_center8.png %}){: style="max-width:45%;"}

Jeder Block hat eigene Einstellungen etwa zum Padding. Das Bedienfeld auf der rechten Seite wechselt automatisch zu einem Styling-Bedienfeld für das ausgewählte Inhaltselement. Weitere Informationen finden Sie unter [Editor-Blockeigenschaften]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).

Wenn Sie den Block Benutzerdefinierter Code in Ihrem Einstellungscenter verwenden, werden Inline-Frames möglicherweise nicht im benutzerdefinierten Code generiert, wenn sie an Ihre Benutzer ausgeliefert werden.

{% endtab %}
{% endtabs %}

## Schritt 5: Bestätigungsseite anpassen

Vergessen Sie nicht, die Bestätigungsseite anzupassen! Sie können diese Seite bearbeiten, indem Sie oben im Fenster des Drag-and-Drop-Editors **Bestätigungsseite** wählen. Diese Seite wird den Benutzern angezeigt, nachdem sie ihre Einstellungen über das Einstellungscenter aktualisiert haben. Die oben genannten Gestaltungsmöglichkeiten gelten auch für diese Seite.

![Ein Beispiel für eine Bestätigungsseite, um mitzuteilen, dass die Einstellungen des Benutzers aktualisiert wurden.][9]{: style="max-width:65%;"}

## Schritt 6: Präferenzzentrum prüfen und einführen

Sie können eine Vorschau Ihres Einstellungszentrums anzeigen, indem Sie im Editor die Registerkarte **Vorschau** wählen. Die Testfunktion ist jedoch deaktiviert. Nachdem Sie Ihr Einstellungscenter bearbeitet haben, können Sie den Editor schließen, indem Sie auf die Schaltfläche **Fertig** klicken.

Sie sehen eine Vorschau sowohl des Einstellungszentrums als auch der Bestätigungsseite. Wählen Sie **Als Entwurf speichern**, um später zu diesem Einstellungscenter zurückzukehren, oder wenn Sie zufrieden sind, wählen Sie **Einstellungscenter starten**.

Wenn Sie das Präferenzzentrum starten, müssen Sie seinen Namen bestätigen, da er danach nicht mehr geändert werden kann. Wenn Sie den Namen bestätigt haben, wird das Präferenzzentrum gestartet und ist einsatzbereit.

## Das Präferenzzentrum verwenden

{% multi_lang_include preference_center_warning.md %}

Um einen Link zum Einstellungscenter in Ihren E-Mails zu platzieren, kopieren Sie das Liquid-Tag des gewünschten Einstellungscenters, indem Sie auf das Symbol **Liquid kopieren** klicken.

![Option "Liquid kopieren" in der Zeile eines Präferenzzentrums][10]{: style="max-width:75%;"}

Fügen Sie das Liquid-Tag an der gewünschten Stelle in Ihrer E-Mail ein, ähnlich wie die [Abmelde-URLs]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#adding-a-custom-unsubscribe-link) eingefügt werden.

## Fehler beheben

Tritt ein Fehler auf, wenn ein Benutzer in einem Einstellungscenter die Option **Speichern** wählt, wird ihm die folgende Standardfehlermeldung angezeigt, die im Editor nicht angepasst oder gestaltet werden kann. Fehlermeldungen können auf diesen Seiten aber weiterhin lokalisiert werden. 

![Eine Fehlermeldung mit dem Hinweis "Beim Speichern Ihrer Einstellungen ist ein Problem aufgetreten. Bitte versuchen Sie es erneut."][11]{: style="max-width:55%;"}

[1]: {% image_buster /assets/img/preference_center/preference_center1.png %}
[2]: {% image_buster /assets/img/preference_center/preference_center2.png %}
[3]: {% image_buster /assets/img/preference_center/preference_center3.png %}
[4]: {% image_buster /assets/img/preference_center/preference_center4.png %}
[5]: {% image_buster /assets/img/preference_center/preference_center5.png %}
[6]: {% image_buster /assets/img/preference_center/preference_center6.png %}
[7]: {% image_buster /assets/img/preference_center/preference_center7.png %}
[8]: {% image_buster /assets/img/preference_center/preference_center8.png %}
[9]: {% image_buster /assets/img/preference_center/preference_center9.png %}
[10]: {% image_buster /assets/img/preference_center/preference_center10.png %}
[11]: {% image_buster /assets/img/preference_center/preference_center11.png %} 
