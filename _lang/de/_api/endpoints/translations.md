---
nav_title: Übersetzungen
article_title: Übersetzung Endpunkte
search_tag: Endpoint
page_order: 9
layout: dev_guide

description: "Diese Landing Page listet die Braze-Übersetzungsendpunkte auf."
page_type: landing

guide_top_header: "Übersetzung Endpunkte"
guide_top_text: "Verwenden Sie die Braze-Übersetzungsendpunkte, um Übersetzungen in Ihren Kampagnen und Canvases zu verwalten und zu aktualisieren."

guide_featured_title: "Endpunkte der Kampagne"
guide_featured_list:
  - name: "GET: Übersetzung für eine Kampagne anzeigen"
    link: /docs/api/endpoints/translations/campaigns/get_translation_campaign/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Alle Übersetzungen für eine Kampagne anzeigen"
    link: /docs/api/endpoints/translations/campaigns/get_bulk_translations_campaigns/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Übersetzung in einer Kampagne aktualisieren"
    link: /docs/api/endpoints/translations/campaigns/put_update_translation_campaign/
    image: /assets/img/braze_icons/target-04.svg

guide_menu_title: "Canvas endpoints"
guide_menu_list:
  - name: "GET: Übersetzung für ein Canvas anzeigen"
    link: /docs/api/endpoints/translations/canvas/get_translation_canvas/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Alle Übersetzungen für ein Canvas anzeigen"
    link: /docs/api/endpoints/translations/canvas/get_bulk_translations_canvases/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "PUT: Übersetzung in einem Canvas aktualisieren"
    link: /docs/api/endpoints/translations/canvas/put_update_translation_canvas/
    image: /assets/img/braze_icons/target-04.svg
  
guide_menu_title2: "Email template endpoints"
guide_menu_list2:
  - name: "GET: Quelle ansehen Übersetzung"
    link: /docs/api/endpoints/translations/email_templates/get_view_source_template/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: Ansichtsspezifische Übersetzung und Lokalisierung"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_locale_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "GET: Alle Übersetzungen und Lokalisierungen anzeigen"
    link: /docs/api/endpoints/translations/email_templates/get_view_translation_template/
    image: /assets/img/braze_icons/target-04.svg
  - name: "PUT: Update von Übersetzungen in einer E-Mail-Vorlage"
    link: /docs/api/endpoints/translations/email_templates/put_update_template/
    image: /assets/img/braze_icons/target-04.svg

---

{% alert important %}
Die Braze-Übersetzungsendpunkte befinden sich derzeit im Early Access. Wenden Sie sich an Ihren Braze-Kundenbetreuer, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}

## Wie unsere Übersetzungsendpunkte funktionieren

Unsere Übersetzungsendpunkte arbeiten mit [mehrsprachiger Komposition]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/), bei der eine Nachricht je nach Nutzer:innen in verschiedenen Versionen wiedergegeben werden kann.

### Voraussetzungen

Bevor Sie diese Endpunkte verwenden, müssen Sie [Ihre Gebietsschemata hinzufügen]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).

### Wie Sie Ihre Übersetzungen testen

Es gibt zwei Möglichkeiten, die Übersetzungsunterstützung mithilfe der API und des Braze-Dashboards für Kampagnen, Canvase (einschließlich einzelner Schritte) und E-Mail-Templates zu validieren:

- Während der Komposition (vor dem Start)
- Nach der Markteinführung (anhand von Entwürfen nach der Markteinführung)

Bevor Sie das Update von Übersetzungen testen, müssen Sie:

1. [Fügen Sie Ihre Lokalisierungen hinzu]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#add-a-locale).
2. Erstellen Sie eine Nachricht und verwenden Sie gegebenenfalls Tags für die Übersetzung.
3. Speichern Sie die Nachricht.
4. Wählen Sie die einzubeziehenden Lokalisierungen aus.
