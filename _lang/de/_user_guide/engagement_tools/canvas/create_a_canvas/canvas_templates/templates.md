---
nav_title: Canvas-Templates
article_title: Canvas-Templates
alias: "/canvas_templates/templates/"
page_order: 0
description: "Dieser referenzierte Artikel beschreibt, wie Sie verfügbare Canvas Templates erstellen."
page_type: reference
---

# Canvas-Templates

> Braze bietet eine Auswahl an Canvas-Templates, die Sie als Referenz und als Best Cases für häufige Anwendungsfälle verwenden können. Diese Vorlagen können zwar nicht bearbeitet werden, aber Sie können sie unter **Vorlagen** > **Lötvorlagen** anzeigen oder in Ihren Leinwänden verwenden.

![Braze-Vorlagen im Bereich Canvas-Vorlagen mit dreizehn verfügbaren Templates.]({% image_buster /assets/img/braze_canvas_templates.png %})

Wählen Sie eine der folgenden Vorlagen aus, die Sie als Referenz oder für Ihr Canvas verwenden können.

## Standard Canvas Templates

{% tabs %}
{% tab Abandoned Intent %}

### Aufgegebene Absicht

Interagieren Sie mit Nutzer:innen in Realtime, um sie zum Kaufabschluss zu bewegen.

Beachten Sie Folgendes, wenn Sie diese Vorlage verwenden:

- Fügen Sie eine bestimmte Zielgruppe hinzu. Derzeit werden die Zielgruppenpfade auf der Basis von „Beliebiger Kauf“ getriggert, aber Sie können dies auf bestimmte Produkte zuschneiden, die Sie ansprechen möchten.
- Bei dieser Vorlage wird davon ausgegangen, dass Sie eine separate Post-Purchase-Journey haben, d. h., dass ein Kauf dazu führt, dass der Benutzer das Canvas verlässt.
- Füllen Sie die Details im Schritt „Zielgruppen-Synchronisierung“ aus.

{% endtab %}
{% tab Back In Stock %}

### Wieder verfügbar

Treiben Sie Käufe an, indem Sie Ihre Nutzer mit personalisierten Nachrichten benachrichtigen, wenn ein Artikel wieder vorrätig ist. Beachten Sie Folgendes, wenn Sie diese Vorlage verwenden:

- Wählen Sie unter **Eingabeplan** einen Katalog aus, den Sie verwenden möchten. So können Sie auf Daten wie Produkte, Rabatte und Werbeaktionen zugreifen, um Ihre Nutzer noch gezielter anzusprechen.
- Fügen Sie unter **Zielgruppe** ein Segment hinzu, um Nutzer anzusprechen, die Interesse an einem bestimmten Artikel bekundet haben.
- Aktualisieren Sie in den Nachrichtenschritten im Canvas das Liquid, um Ihren Katalog zu referenzieren.

{% endtab %}
{% tab Feature Adoption %}

### Übernahme von Features

Senden Sie rechtzeitig personalisierte Nachrichten, um die Vorteile und Nutzungstipps hervorzuheben. Beachten Sie Folgendes, wenn Sie diese Vorlage verwenden:

- Schließen Sie Nutzer:innen aus, die das Feature bereits übernommen haben. Fügen Sie zum Beispiel in **Target Audience** einen Filter für ein angepasstes Event wie "Aktiviertes Feature" hinzu, das bereits stattgefunden hat.
- Um den Schritt „Experimentpfad“ zu verwenden, definieren Sie ein Konversions-Event. Dieses Event sollte das Event sein, das die Annahme eines Features signalisiert.
- Richten Sie den Schritt „Aktionspfad“ im Template mit angepassten Events für „Aktiviertes Feature“ und „Durchgeführte Tour“ ein.
- Richten Sie die angepassten Attribute im Schritt „Nachricht“ mit dem Namen „Feedback-Umfrage“ ein, um die Stimmung des Feedbacks zu erfassen.

{% endtab %}
{% tab Lapsed User %}

### Passive Nutzer:innen

Bringen Sie Nutzer:innen mit Anreizen, die auf ihrem früheren Engagement basieren, zurück zu Ihrer App. Beachten Sie Folgendes, wenn Sie diese Vorlage verwenden:

- Wählen Sie in **Grundlagen** eine bestimmte App aus, für die Sie Conversions verfolgen möchten.
- Fügen Sie im Canvas-Editor bestimmte Apps für die Aktions-Pfade-Schritte hinzu.
- Konfigurieren Sie den Schritt „Zielgruppen-Synchronisierung“ mit den Partnern und Zielgruppen für Ihren Anwendungsfall.

{% endtab %}
{% tab Onboarding %}

### Onboarding

Erstellen Sie Onboarding-Journeys, die eine starke anfängliche Akzeptanz und dauerhafte Beziehungen zu Ihren Nutzer:innen fördern. Beachten Sie Folgendes, wenn Sie diese Vorlage verwenden:

- Im Schritt „Zielgruppenpfade“ mit dem Namen „Zielgruppen-Split“ können Sie die Schlüsselaktionen für interessierte Nutzer:innen anpassen. In dem Template lautet der Filter für das Segment „Hat auf die E-Mail für den Willkommens-E-Mail-Schritt geklickt“.

{% endtab %}
{% tab Post-Purchase Feedback %}

### Feedback nach dem Kauf

Organisieren Sie personalisierte Erlebnisse, mit denen Sie auf Feedback reagieren und eine Beziehung zu Ihren Nutzern aufbauen können. Beachten Sie Folgendes, wenn Sie diese Vorlage verwenden:

- Im ersten Schritt des Canvas-Editors:
    - Geben Sie die benutzerdefinierten Attribute in der In-App-Nachricht an, um die Stimmung des Feedbacks auf der Grundlage der ausgewählten Umfrageoption anzugeben. 
    - Geben Sie für jede Call-to-Action die Attribute der Links an, um zu erfassen, welche Option ausgewählt wurde. Auf diese Attribute wird im nachfolgenden Pfad zur Zielgruppe verwiesen.
- Passen Sie den Zielgruppenpfad mit den Attributen aus dem ersten Schritt dieses Templates an.
- Richten Sie den Schritt „Zielgruppen-Synchronisierung“ mit dem Namen „Retargeting von Anzeigen“ ein.

{% endtab %}
{% endtabs %}

{% alert tip %}
Eine schrittweise Anleitung zur Erstellung eines Beispiel-Canvas mit diesen Braze-Vorlagen finden Sie unter [Verwendung von Braze-Vorlagen]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates).
{% endalert %}

## E-Commerce Canvas Templates

eCommerce Canvas Templates sind speziell auf E-Commerce Marketer zugeschnitten und erleichtern die Umsetzung wichtiger Strategien.

{% multi_lang_include canvas/ecommerce_templates.md %}