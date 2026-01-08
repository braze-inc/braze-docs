---
nav_title: Link-Templates
article_title: Link-Vorlagen
page_order: 4
description: "Dieser Artikel beschreibt, wie Sie verschiedene Arten von Linkvorlagen in Ihren E-Mails erstellen können."
tool:
  - Templates
channel:
  - email

---

# Link-Templates

> Mit Link-Templates können Sie dynamische und wiederverwendbare Links für Ihre E-Mail-Kampagnen erstellen, indem Sie Parameter anhängen oder URLs voranstellen. So können Sie die URLs Ihrer Kampagnen und Nachrichten einheitlich gestalten. 

{% alert note %}
Linkvorlagen sind eine optionale Funktion. Wenn **E-Mail-Link-Vorlagen** in der Rubrik **Vorlagen** fehlen, wenden Sie sich an Ihren Kundenbetreuer, um die Funktion zu aktivieren.
{% endalert %}

## Funktionsweise

Linkvorlagen werden am häufigsten in den folgenden Anwendungsfällen verwendet:

- Anhängen von Google Analytics-Abfrageparametern an alle Links in einer bestimmten E-Mail-Nachricht
- Voranstellen einer URL an alle Links in einer bestimmten E-Mail-Nachricht

Nehmen wir an, Sie starten eine E-Mail-Kampagne für ein neues Produkt. Sie können eine Link-Template verwenden, die Nutzer:innen auf die Produktseite leitet, und den Link personalisieren, um den Namen Ihres Nutzers oder einen bestimmten Aktionscode einzuschließen. So können Sie verfolgen, wie viele Nutzer auf den Link geklickt und einen Kauf getätigt haben. Auf diese Weise können Sie Ihre Links konsistent gestalten und Ihre Analytics besser tracken.

## Erstellen einer Link-Template

Sie können eine unbegrenzte Anzahl von Linkvorlagen erstellen, um Ihre verschiedenen Anforderungen zu erfüllen. Um eine Link-Template zu erstellen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Vorlagen** > **E-Mail-Link-Vorlagen**. 
2. Wählen Sie **E-Mail-Link-Template erstellen**.
3. Geben Sie Ihrer Link-Template einen Namen.
4. (Optional) Fügen Sie eine Beschreibung, ein Team oder einen Tag hinzu, um Details über die Link-Vorlage hinzuzufügen.
5. (Optional) Wählen Sie das Umschalten, um die Link-Vorlage automatisch zu Links in E-Mail Kampagnen und Canvase hinzuzufügen. Dies gilt für das Hinzufügen eines neuen Links zu einer neuen oder bestehenden E-Mail.

Es gibt zwei Arten von Linkvorlagen, die Sie erstellen können:

- [Link-Vorlage, die vor einer URL eingefügt wird](#prepend-link-template)
- [Link-Vorlage, die nach einer URL eingefügt wird](#append-link-template)

Wenn Sie Linkvorlagen und [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) verwenden, darf Liquid nur innerhalb des Body-Tags hinzugefügt werden, um eine konsistente Darstellung zu gewährleisten.

### Voranstellen: Eine Link-Template erstellen, die vor einer URL eingefügt wird {#prepend-link-template}

Um einen String oder eine URL vor den Links in Ihrer E-Mail-Nachricht einzufügen, gehen Sie wie folgt vor

1. Erstellen Sie eine neue Link-Template.
2. Setzen Sie die **Template-Position** auf **Vor URL**. 
3. Geben Sie einen String ein, der Ihrer URL immer vorangestellt wird. 

Die **Vorschau des Templates** dient dazu, Ihnen ein Beispiel dafür zu geben, wie das Link-Template vor einer URL eingefügt wird.

![Felder Template Position, Prepend URL und Template Preview für das Einfügen von Link Templates vor einer URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Anhängen: Eine Link-Template erstellen, die nach einer URL eingefügt wird {#append-link-template}

Wenn Sie Abfrageparameter nach einer URL in Ihrer E-Mail-Nachricht hinzufügen möchten:

1. Erstellen Sie eine neue Link-Template.
2. Setzen Sie die **Template-Position** auf **Nach URL**. 
3. Geben Sie die Abfrageparameter (`value=example`) am Ende jeder URL an. Sie können mehrere Parameter an das Ende einer URL anhängen.

![Template-Position, Abfrageparameter und Template-Vorschau-Felder für den Prozess des Einfügens von Link-Templates nach einer URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Linkvorlagen in E-Mail-Kampagnen verwenden

Nachdem Sie Ihre Linkvorlagen eingerichtet haben, können Sie die Vorlage auswählen, die Sie in Ihrer E-Mail verwenden möchten.

- **HTML-Editor:** Gehen Sie auf die Registerkarte **Linkverwaltung** unter dem Abschnitt **Inhalt**. Wählen Sie **Linkvorlage hinzufügen**, wählen Sie Ihre Linkvorlage und wählen Sie **Hinzufügen**.

{% alert important %}
Um auf die Registerkarte **Linkverwaltung** im aktualisierten HTML-E-Mail-Editor zugreifen zu können, müssen Sie das Link-Aliasing aktiviert haben. Um das Link-Aliasing zu aktivieren, wenden Sie sich an Ihren Kundenbetreuer.
{% endalert %}

- **Drag-and-Drop-Editor:** Wählen Sie **Inhalt** > Registerkarte **Linkverwaltung**. Wählen Sie dann **Linkvorlage hinzufügen**. Um im Drag&Drop-Editor auf Linkvorlagen zugreifen zu können, müssen Sie das [Link-Aliasing]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/) aktiviert haben.

![Link Management Tab im Drag-and-Drop-Editor mit einer Beispielliste von Link-Templates.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Linkvorlagen werden nicht auf reinen Text angewendet. Das bedeutet, dass Currents möglicherweise Klicks anzeigt, die nicht die Parameter aus den Linkvorlagen enthalten, da diese Klicks möglicherweise aus der reinen Textversion der E-Mail stammen.
{% endalert %}

Wenn Sie auf der Registerkarte **Linkverwaltung** Linkvorlagen hinzufügen, scrollen Sie nach rechts, um die von Ihnen hinzugefügten Vorlagen anzuzeigen. Wenn bestehende Links in einer E-Mail bereits mit einem Link-Template versehen sind, wird bei neu hinzugefügten Links standardmäßig auch das Link-Template hinzugefügt.

## Verwalten von Link-Templates

Sie können auch Link-Templates [duplizieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/). Erfahren Sie mehr über die Erstellung und Verwaltung von Templates und kreativen Inhalten in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert important %}
Die Archivierung von Vorlagen ist derzeit nicht für Linkvorlagen verfügbar.
{% endalert %}

## Häufig gestellte Fragen

Antworten auf häufig gestellte Fragen zu Link-Templates finden Sie auf unserer Seite [Templates FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).

