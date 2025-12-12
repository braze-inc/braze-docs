---
nav_title: Farbprofile und CSS-Templates
article_title: Farbprofile und CSS-Vorlagen für In-App-Nachrichten
page_order: 4
page_type: reference
description: "Dieser Artikel bietet einen Überblick über die Farbprofile für In-App-Nachrichten und CSS-Vorlagen."
channel:
  - in-app messages
---

# Farbprofile und CSS-Vorlagen {#reusable-color-profiles}

> Sie können Vorlagen für In-App-Nachrichten und In-Browser-Nachrichten auf dem Dashboard speichern, um schnell neue Kampagnen und Nachrichten in Ihrem Stil zu erstellen. 

Gehen Sie zu **Vorlagen** > **In-App Nachrichtenvorlagen**.

Auf dieser Seite können Sie entweder vorhandene Vorlagen bearbeiten oder auf **\+ Erstellen** klicken und **Farbprofil** oder **CSS-Vorlage** wählen, um neue Vorlagen für Ihre In-App-Nachrichten zu erstellen.

## Farbprofil

Sie können das Farbschema Ihrer Nachrichtenvorlage anpassen, indem Sie entweder einen HEX-Farbcode eingeben oder auf das farbige Feld klicken und eine Farbe mit dem Farbwähler auswählen.

Klicken Sie auf **Farbprofil speichern**, wenn Sie fertig sind.

### Farbprofile verwalten

Sie können Vorlagen auch [duplizieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) und [archivieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/)! Erfahren Sie mehr über die Erstellung und Verwaltung von Templates und kreativen Inhalten in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## CSS-Template {#in-app-message-templates}

Sie können ein komplettes CSS-Template für Ihre [modale In-App-Nachricht](#web-modal-css) anpassen.

Benennen und kennzeichnen Sie Ihre CSS-Vorlage und wählen Sie dann, ob sie als Standardvorlage verwendet werden soll oder nicht. Sie können Ihr eigenes CSS in das vorgesehene Feld schreiben. Dieses Feld ist bereits mit dem in der Nachrichtenvorschau gezeigten CSS ausgefüllt. Sie können es nach Belieben an Ihre Bedürfnisse anpassen.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

Wie Sie sehen, können Sie alles bearbeiten, von der Hintergrundfarbe bis zu Schriftgröße und -gewicht und vieles mehr.

### CSS-Vorlagen verwalten

Sie können Vorlagen auch [duplizieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) und [archivieren]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/)! Erfahren Sie mehr über die Erstellung und Verwaltung von Templates und kreativen Inhalten in [Templates & Media]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Modal mit CSS (nur Web) {#web-modal-css}

Wenn Sie sich für ein reines Web-Modal mit CSS-Meldung entscheiden, können Sie Ihre eigene Vorlage anwenden oder Ihr eigenes CSS in den dafür vorgesehenen Bereich schreiben. Dieses Feld ist bereits mit dem in der Nachrichtenvorschau gezeigten CSS ausgefüllt. Sie können es jedoch nach Belieben leicht an Ihre Bedürfnisse anpassen.

Wenn Sie Ihre eigene Vorlage verwenden möchten, klicken Sie auf **Vorlage anwenden** und wählen Sie aus der Galerie der In-App-Nachrichtenvorlagen. Wenn Sie keine Optionen haben, können Sie eine [CSS-Vorlage]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css/#in-app-message-templates) mit dem CSS-Vorlagenersteller hochladen.


