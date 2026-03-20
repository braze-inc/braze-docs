---
nav_title: Nutzerdefinierte Erinnerungsnachrichten
article_title: Nutzerdefinierte Erinnerungsnachrichten
page_order: 5
page_type: reference
description: "Dieser Referenzartikel erklärt, wie Sie Braze Landing-Pages, angepasste Attribute und Kampagnen nutzen können, um Nutzer:innen die Registrierung für personalisierte Erinnerungsnachrichten zu bevorstehenden Ereignissen oder Terminen zu ermöglichen."
---

# Nutzerdefinierte Erinnerungsnachrichten

> Verwenden Sie Braze [Landing-Pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/), angepasste Attribute und Kampagnen, um Nutzer:innen die Wahl zu lassen, wann sie Erinnerungsnachrichten zu bevorstehenden Ereignissen oder Terminen erhalten möchten. Dieser Ansatz ermöglicht es nicht-technischen Braze-Nutzer:innen, Inhalte für Erinnerungs-Registrierungsseiten zu erstellen und zu bearbeiten, während die von Nutzer:innen ausgewählten Präferenzen die Segmentierung, das Targeting und die Personalisierung über alle Ihre Braze-gestützten Nachrichten hinweg steuern können.

Mit diesem Ansatz können Sie:

- Nutzer:innen das Datum ihrer Erinnerungsnachricht relativ zu einem bevorstehenden Ereignis selbst auswählen lassen.
- Präferenzen direkt von Nutzer:innen über eine Braze Landing-Page erfassen und in Nutzerprofile schreiben – kein zusätzliches Backend erforderlich.
- Nachrichten an den von Nutzer:innen gewählten Daten senden, sodass Nachrichten relevant und einwilligungsbasiert bleiben.
- Den Anwendungsfall mit zusätzlichen Braze-Features erweitern, wie z. B. Nachrichtenverzögerungen, Follow-up-Retargeting und A/B-Tests.

## Voraussetzungen

Um diese Anleitung abzuschließen, benötigen Sie:

| Anforderung | Beschreibung |
| --- | --- |
| Zugang zu Landing-Pages | Zugang und Berechtigungen zum Erstellen von [Landing-Pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) in Braze. |
| HTML- und JavaScript-Kenntnisse | Grundlegende Vertrautheit mit HTML und JavaScript zur Anpassung Ihrer Landing-Page. Nur für [Option B](#option-b-personal-dates-custom-code-block) erforderlich. |
| Liquid-Kenntnisse | Grundlegende Vertrautheit mit [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) für die Erstellung personalisierter Variablen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 1. Schritt: Landing-Page erstellen und aus einer Nachricht verlinken

Erstellen Sie zunächst eine [Braze Landing-Page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/). Erstellen Sie dann eine Nachricht (z. B. eine E-Mail), die Nutzer:innen zur Landing-Page verlinkt.

{% raw %}
Um die Aktivität auf der Landing-Page automatisch mit dem Nutzerprofil der Empfänger:in zu verknüpfen, verwenden Sie den `{% landing_page_url %}` Liquid-Tag, wenn Sie aus einer Braze-Nachricht auf die Seite verlinken. Zum Beispiel:

```html
<a href="{% landing_page_url your-page-url-handle %}">Sign up for reminders</a>
```
{% endraw %}

Wenn Nutzer:innen auf diesen Link klicken, identifiziert Braze sie automatisch, sodass alle übermittelten Präferenzen in ihr bestehendes Profil geschrieben werden – keine manuellen URL-Parameter erforderlich. Eine vollständige Anleitung finden Sie unter [Nutzer:innen über ein Formular tracken]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users/).

## 2. Schritt: Präferenzen auf der Landing-Page erfassen

Wie Sie Nutzerpräferenzen erfassen, hängt davon ab, ob Sie gemeinsame Termine oder persönliche Termine sammeln. Wählen Sie die Option, die zu Ihrem Anwendungsfall passt.

### Option A: Gemeinsame Termine (Drag-and-Drop-Formularblöcke)

Für Ereignisse, bei denen viele Nutzer:innen dasselbe Datum teilen (z. B. Feiertage oder Sportveranstaltungen), verwenden Sie die integrierten [**Checkbox**-Formularblöcke]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks) des Drag-and-Drop-Editors, um Präferenzen zu erfassen. Jede Checkbox setzt nativ ein boolesches angepasstes Attribut (`true` oder `false`) im Profil der Nutzer:in, wenn das Formular abgesendet wird – kein benutzerdefinierter Code erforderlich.

Fügen Sie beispielsweise eine Checkbox mit der Bezeichnung „Super Bowl 2026 Erinnerung" hinzu, die dem angepassten Attribut `super_bowl_2026_reminder` zugeordnet ist. Wenn Nutzer:innen die Checkbox aktivieren und das Formular absenden, setzt Braze:

```
super_bowl_2026_reminder = true
```

Diese booleschen Attribute können dann direkt in [Segment-Filtern]({{site.baseurl}}/user_guide/engagement_tools/segments/) verwendet werden, um Ihre Zielgruppe aufzubauen.

### Option B: Persönliche Termine (Custom-Code-Block)

Für Termine, die für jede:n Nutzer:in einzigartig sind (z. B. Geburtstage oder Jahrestage), verwenden Sie einen [**Custom Code**-Block]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#basic-blocks) auf Ihrer Landing-Page, um das Datum zu erfassen und über die `lpBridge`-API an Braze zu schreiben. Dieser Ansatz bietet Ihnen eine Datumseingabe (oder einen Datumswähler) und ermöglicht es Ihnen, Präferenzen in einem [verschachtelten angepassten Attribut-Array von Objekten]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/array_of_objects/) zu speichern, was die Drag-and-Drop-Formularblöcke nicht unterstützen.

Wenn Nutzer:innen über den {% raw %}`{% landing_page_url %}`{% endraw %} Liquid-Tag ankommen, weiß Braze bereits, wer sie sind, sodass Ihr Skript nur Folgendes tun muss:

1. Auf den Klick des Formular-Absende-Buttons warten.
2. Den Datumswert aus Ihrer benutzerdefinierten Eingabe lesen.
3. Die `lpBridge`-API verwenden, um verschachtelte angepasste Attribute zu setzen und die Daten an Braze zu übertragen.

Speichern Sie diese Präferenzen mithilfe eines verschachtelten angepassten Attribut-Arrays von Objekten. Diese Struktur ermöglicht es Ihnen, mehrere Erinnerungen pro Nutzer:in zu speichern und später abgeleitete Felder hinzuzufügen, wie z. B. `next_reminder_name` oder `last_reminder_date`.

#### Beispielskript

Das folgende Beispielskript deaktiviert das Standard-Button-Verhalten und führt benutzerdefinierte Methoden beim Button-Klick aus. Ersetzen Sie die Element-IDs und Attributwerte durch Ihre eigenen.

```html
<script async="true">
  // Set IDs (as found by inspecting your landing page preview) and success message
  const registerButtonId = "YOUR_BUTTON_ID";
  const messageDivId = "YOUR_MESSAGE_DIV_ID";
  const successMessage = "You're all set! We'll send your reminder.";

  // Wait for page content to load
  document.addEventListener("DOMContentLoaded", () => {
    // Remove the default redirect event from the Braze Message Handler Script
    props[registerButtonId].onclickContract[0].brazeEvents =
      props[registerButtonId].onclickContract[0].brazeEvents.filter(
        (event) => event.eventType !== "REDIRECT"
      );

    const registerButton = document.getElementById(registerButtonId);
    if (registerButton) {
      registerButton.addEventListener("click", async (event) => {
        event.preventDefault();

        // Set the custom attribute (replace with your actual key/value)
        await window.lpBridge.setCustomUserAttribute("key", "value");

        // Flush data to Braze
        await window.lpBridge.requestImmediateDataFlush();

        // Remove the button and update the message
        registerButton.remove();
        const messageDiv = document.getElementById(messageDivId);
        if (messageDiv) {
          messageDiv.innerHTML = successMessage;
        }
      });
    }
  });
</script>
```

Um die Element-IDs für Ihre Landing-Page-Komponenten zu finden, öffnen Sie die Vorschau Ihrer Seite, rechtsklicken Sie und wählen Sie **Untersuchen** in Ihrem Browser. Suchen Sie die IDs für die Button- und Nachrichtenkomponenten im HTML.

## 3. Schritt: Erinnerungsnachrichten einrichten und auslösen

Nachdem Sie angepasste Attribute über die Landing-Page erfasst haben, erstellen Sie Kampagnen, um Nutzer:innen über bevorstehende Ereignisse zu benachrichtigen.

### Option A: Gemeinsame Termine {#step-3-option-a-shared-dates}

Wenn Sie boolesche angepasste Attribute verwendet haben (Option A in [2. Schritt](#option-a-shared-dates-dnd-form-blocks)), verwenden Sie dieses Attribut als Segment-Filter, um die Zielgruppe für Ihre Erinnerungsnachricht aufzubauen. Erstellen Sie dann eine neue Kampagne, die vor dem Ereignis geplant ist, um diese Gruppe mit Ihrem gewählten Inhalt anzusprechen.

### Option B: Persönliche Termine {#step-3-option-b-personal-dates}

Wenn Sie verschachtelte angepasste Attribute verwendet haben (Option B in [2. Schritt](#option-b-personal-dates-custom-code-block)), verwenden Sie den Zielgruppen-Filter **Verschachteltes angepasstes Attribut**, um alle Nutzer:innen auszuwählen, die ein Erinnerungsdatum innerhalb eines bestimmten Fensters haben – zum Beispiel in zwei Tagen.

Um Erinnerungen fortlaufend zu senden, richten Sie eine täglich wiederkehrende Kampagne ein, sodass jeden Tag Nutzer:innen mit bevorstehenden Erinnerungen, die in Ihr Fenster fallen, ihre Nachrichten erhalten.

## 4. Schritt: Integration überprüfen

Überprüfen Sie nach Abschluss der Einrichtung Ihre Integration:

1. Senden Sie sich selbst einen Link zur Landing-Page und füllen Sie das Formular aus.
2. Navigieren Sie zu Ihrem Nutzerprofil im Braze-Dashboard und bestätigen Sie, dass das angepasste Attribut angezeigt wird.
3. Senden Sie eine Test-Erinnerungsnachricht an Ihr Profil und überprüfen Sie, ob alle personalisierten Details korrekt dargestellt werden.
4. Überwachen Sie die Ergebnisse genau, wenn Sie Ihre Kampagne starten.

## Hinweise

- Ein detailliertes Beispiel zum Senden von Nachrichten basierend auf datumsbasierten angepassten Attributen finden Sie im E-Mail-Anwendungsfall im [REST API Messaging-Leitfaden]({{site.baseurl}}/developer_guide/rest_api/messaging/).
- Wenn Sie eine Landing-Page duplizieren oder Felder ersetzen, ändern sich die Komponenten-IDs. Aktualisieren Sie Ihren Custom-Code-Block, um die neuen IDs widerzuspiegeln.
- Verschachtelte angepasste Attribute verbrauchen [Datenpunkte]({{site.baseurl}}/user_guide/data/infrastructure/data_points/) für jeden Schlüssel im Array von Objekten. Das Aktualisieren eines angepassten Attribut-Objekts auf null verbraucht ebenfalls einen Datenpunkt.
- Der in dieser Anleitung vorgestellte Code dient als anschauliches Beispiel. Testen Sie allen Code und alle Komponenten gründlich in Ihrer Umgebung, bevor Sie sie in die Produktion überführen.