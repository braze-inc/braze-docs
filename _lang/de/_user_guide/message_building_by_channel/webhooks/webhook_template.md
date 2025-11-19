---
nav_title: Erstellen einer Webhook-Vorlage
article_title: Erstellen einer Webhook-Vorlage
page_order: 2
tool:
  - Templates
channel:
  - webhooks
description: "In diesem Referenzartikel erfahren Sie, wie Sie Webhook-Templates für die spätere Verwendung in der Braze-Plattform erstellen und anpassen können."

---

# Erstellen einer Webhook-Vorlage

> Während Sie Ihre Webhooks erstellen und anpassen, können Sie Webhook-Vorlagen für die spätere Verwendung innerhalb der Braze-Plattform erstellen und nutzen. Auf diese Weise können Sie konsequent eine Vielzahl von Webhooks für Ihre verschiedenen Kampagnen erstellen.

## Schritt 1: Rufen Sie den Editor für Webhook-Vorlagen auf

Gehen Sie im Dashboard von Braze zu **Vorlagen** > **Webhook-Vorlagen**.

![Die Seite "Webhook-Vorlagen" mit vorgefertigten und gespeicherten Webhook-Templates.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## Schritt 2: Wählen Sie Ihre Vorlage

Von hier aus können Sie eine neue Vorlage erstellen, eine der vorgefertigten Webhook-Vorlagen verwenden oder eine vorhandene Vorlage bearbeiten.

Wenn Sie z.B. [LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line) als Nachrichtenkanal verwenden, können Sie mehrere Webhooks einrichten, indem Sie die vorgefertigten Vorlagen für **LINE Carousel** oder **LINE Image** verwenden.

## Schritt 3: Template-Details ausfüllen

1. Geben Sie Ihrer Webhook-Vorlage einen eindeutigen Namen.
2. (Optional) Fügen Sie eine Beschreibung der Vorlage hinzu, um zu erklären, wie diese Vorlage verwendet werden soll.
3. Fügen Sie bei Bedarf [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) und [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) hinzu, um die Suche nach Ihrer Vorlage zu erleichtern und zu filtern.

## Schritt 4: Template erstellen

1. Geben Sie die Webhook-URL ein.
2. Wählen Sie die HTTP-Methode.
3. Fügen Sie einen Anfragetext hinzu. Dies kann entweder ein **JSON-Schlüssel/Wert-Paar** oder **Rohtext** sein.
4. (Optional) Fügen Sie einen Anfragekopf hinzu. Dies kann für Ihr Webhook-Ziel erforderlich sein.

![Der Tab "Zusammenstellen" beim Erstellen eines Webhook Templates. Verfügbare Felder sind die Webhook-URL, die HTTP-Methode, der Anfragetext und die Anfrage-Header. Sie können auch Sprachen hinzufügen.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## Schritt 5: Testen Sie Ihre Vorlage

Um zu sehen, wie Ihr Webhook aussieht, bevor Sie ihn an Ihre Benutzer senden, können Sie auf der Registerkarte **Test** einen Test-Webhook senden. Hier können Sie auswählen, ob Sie eine Vorschau der Nachricht als zufälliger Benutzer, bestehender Nutzer:innen oder angepasster Nutzer:innen sehen möchten.

## Schritt 6: Template speichern

Speichern Sie Ihr Template, indem Sie **Template speichern** auswählen. Jetzt können Sie diese Vorlage für jede beliebige Kampagne verwenden.

{% alert note %}
Änderungen an einer bestehenden Vorlage werden in Kampagnen, die mit früheren Versionen dieser Vorlage erstellt wurden, nicht berücksichtigt.
{% endalert %}

## Verwaltung Ihrer Vorlagen

Sie können Webhook-Templates [duplizieren und archivieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/), um Ihre Liste der Templates besser zu organisieren und zu verwalten.

Erfahren Sie mehr über die Erstellung und Verwaltung von Vorlagen und kreativen Inhalten in [Vorlagen und Medien]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

