---
nav_title: FAQ
article_title: FAQ zu E-Mail- und Linkvorlagen
page_order: 10

page_type: FAQ
description: "Auf dieser Seite finden Sie häufig gestellte Fragen zu E-Mail-Vorlagen und Linkvorlagen."
tool:
  - Templates
channel: email

---

# Häufig gestellte Fragen

> Auf dieser Seite finden Sie Antworten auf einige häufig gestellte Fragen zu E-Mail-Vorlagen und Linkvorlagen.

## E-Mail-Templates

### Kann ich einen Link "Diese E-Mail in einem Browser anzeigen" zu meinen E-Mails hinzufügen?

Nein, Braze bietet diese Funktion nicht an. Der Grund dafür ist, dass ein immer größerer Teil der E-Mails auf mobilen Geräten und modernen E-Mail-Clients geöffnet wird, die Bilder und Inhalte ohne Probleme darstellen.

**Workaround:** Um dasselbe Ergebnis zu erzielen, können Sie den Inhalt Ihrer E-Mail auf einer externen Landing Page (z. B. Ihrer Website) hosten, die dann von der E-Mail-Kampagne, die Sie erstellen, mit dem **Link-Tool** beim Bearbeiten des E-Mail-Textes verlinkt werden kann.

### Wie erstelle ich einen individuellen Abmeldelink für meine E-Mail-Vorlagen?

Es gibt eine Umleitungsoption für die Abmeldeseite.

Sie könnten den Abmeldelink in der benutzerdefinierten Fußzeile von {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} in einen Link zu Ihrer eigenen Website mit einem Abfrageparameter ändern, der die Benutzer-ID enthält. Ein Beispiel ist:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

Nun können Sie den [Endpunkt`/email/status` ]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) aufrufen, um den Nutzerstatus zu aktualisieren. Weitere Einzelheiten finden Sie in unserer Dokumentation zur [Änderung des E-Mail-Abonnementstatus]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Um diesen neuen Link zu speichern, muss der standardmäßige Braze Abmelde-Tag {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} in der Fußzeile stehen. Das bedeutet, dass Sie den Standardlink einfügen müssen, indem Sie ihn ausblenden, also das Tag entweder in einem Kommentar oder in einem versteckten `<div>`-Tag platzieren.

- **Beispiel für ein Tag in einem Kommentar:** Beispiel für ein Tag in einem Kommentar: `<!-- ${set_user_to_unsubscribed_url} -->`
- **Beispiel für einen Kommentar in einem ausgeblendeten `<div>`-Tag :** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### Was passiert, wenn ich eine E-Mail-Vorlage bearbeite, die gerade in einer Kampagne verwendet wird?

Änderungen, die Sie an einer bestehenden Vorlage vornehmen, werden nicht in Kampagnen übernommen, die mit früheren Versionen dieser Vorlage erstellt wurden. Bei API-Kampagnen, die ein Template im REST-API-Body verwenden, verwendet Braze die aktuelle Version des Templates zum Zeitpunkt des Versands.  

## Linkvorlagen

### Kann ich mehrere Linkvorlagen in meine E-Mail hochladen?

Ja, Sie können so viele Templates in Ihre Nachrichten einfügen, wie Sie möchten. Als bewährte Methode sollten Sie Ihre E-Mails testen, um sicherzustellen, dass die Links nicht länger als 2.000 Zeichen sind, da die meisten Browser die Links kürzen oder abschneiden.

### Wie kann ich eine Vorschau meiner Links mit allen angewendeten Tags anzeigen?

Es gibt mehrere Möglichkeiten, Ihre Links in der Vorschau anzuzeigen. Nachdem Sie die [Linkvorlage]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/) angewendet haben, können Sie eine [Test-E-Mail]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) an sich selbst senden, um alle Links zu sehen. 

Sie können die Links auch über das Vorschaufenster in einer neuen Registerkarte öffnen, um die Links zu sehen. Sie können auch mit dem Mauszeiger über die Links im Vorschaufenster fahren und sie am unteren Rand Ihres Browsers sehen.

### Wie funktioniert das Link-Templating mit Liquid?

Linkvorlagen werden erweitert und zu jeder URL hinzugefügt, bevor eine Liquid-Erweiterung stattfindet. Wenn ein Teil Ihrer URL mit einem Liquid-Snippet generiert wird, empfehlen wir, die URL-Basis und das Fragezeichen (?) fest zu kodieren, damit die Linkvorlagen korrekt erweitert werden. 

Vermeiden Sie es, Fragezeichen in Liquids einzufügen, da das Link-Template dann zunächst ein Fragezeichen (?) und die Liquid-Erweiterung dann noch ein weiteres Fragezeichen einfügt.

## Link-Aliasing

### Wie wirkt sich die Aktivierung des Link-Alias auf meine Inhaltsblöcke und Linkvorlagen aus?

Für alle neu erstellten Content-Blöcke wird das Link-Aliasing auf alle Workspaces angewendet, da es sich um ein Feature auf Unternehmensebene handelt. 

Bestehende Inhaltsblöcke werden nicht verändert, wenn das Link-Aliasing aktiviert ist. Bestehende Linkvorlagen werden zwar nicht geändert, aber der bestehende Linkvorlagenabschnitt in einer Nachricht wird entfernt. Weitere Informationen finden Sie unter [Link-Aliasing in Inhaltsblöcken]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#link-aliasing-in-content-blocks).

### Kann ich Liquid bedingte Logik vollständig innerhalb eines HTML-Anker-Tags verwenden?

Nein, Braze Link-Aliasing erkennt den HTML-Code nicht richtig. 

Wenn eine solche Logik zusammen mit Funktionen verwendet wird, die den HTML-Code analysieren müssen (z. B. ein Preheader oder Link-Templating), kann die Bibliothek, die zum Scannen des HTML-Codes verwendet wird, den Anker-Tag so verändern, dass das richtige `href` nicht als Template verwendet werden kann. Die Bibliothek stellt dann fest, dass der HTML-Code ungültig ist, da er nicht mit dem Liquid-Code übereinstimmt. 

Verwenden Sie stattdessen die Liquid-Logik, die auf jeder Stufe ein vollständiges Anker-Tag enthält. Dies beeinträchtigt die HTML-Analyse nicht, da die Logik mehrere Instanzen von gültigem HTML enthält. Sie können Ihre Logik auch vereinfachen, indem Sie eine Variable zuweisen und dann als Template in das entsprechende Anker-Tag einfügen.
