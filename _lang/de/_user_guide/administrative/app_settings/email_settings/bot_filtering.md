---
nav_title: Bot-Filter für E-Mails
article_title: Bot-Filter für E-Mails
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "Dieser Artikel bietet eine Übersicht über Bot-Filter für E-Mails."
---

# Bot-Filter für E-Mails

> Richten Sie in Ihren [E-Mail-Einstellungen]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) einen Bot-Filter ein, um alle mutmaßlichen Maschinen- oder Bot-Klicks auszuschließen. Ein "Bot-Klick" in E-Mails bezieht sich auf einen Klick auf Hyperlinks innerhalb einer E-Mail, die von einem automatisierten Programm generiert wurde. Indem Sie diese Bot-Klicks filtern, können Sie Nachrichten absichtlich triggern und an Empfänger:in zustellen, die engagiert sind.

{% alert important %}
Ab dem 9\. Juli 2025 wird für alle neu erstellten Workspaces die Bot-Filter-Einstellung aktiviert sein, um eine genauere Berichterstattung über Klicks in Braze zu ermöglichen.
{% endalert %}

## Über Bot-Klicks

Braze verfügt über ein Erkennungssystem, das mehrere Eingaben verwendet, um mutmaßliche Bot-Klicks zu identifizieren, die auch als nicht-menschliche Interaktionen (NHI) bezeichnet werden. Bot-Klicks können Ihre Metriken für das Engagement in E-Mails verzerren, indem sie die Klickraten künstlich aufblähen. Dieser Ansatz erlaubt es uns, zwischen echten menschlichen Interaktionen und vermuteten Bot-Aktivitäten zu unterscheiden, um die Integrität der Metriken und Insights zum Engagement bei Klicks zu erhalten.

## Von Bot-Klicks betroffene Metriken

{% alert note %}
Bot-Filter blockieren aktiv mutmaßliche automatisierte Klicks, um die Genauigkeit Ihrer Engagement-Metriken zu verbessern. Scanner und Bots entwickeln sich jedoch im Laufe der Zeit ständig weiter, so dass Braze nicht garantieren kann, dass alle nicht-menschlichen Interaktionen entfernt werden.
{% endalert %}

Die folgenden Metriken von Braze können durch Bot-Klicks beeinflusst werden:

- Klickrate gesamt
- Eindeutige Klickrate
- Effektive Klickrate
- Konversionsrate (wenn "Klicks Kampagne" als Konversions-Event ausgewählt ist)
- Heatmap
- Bestimmte Filter für Segmente

[Features von Braze Intelligence]({{site.baseurl}}/user_guide/brazeai/intelligence), die Klick-Daten zusätzlich zu unseren Erkennungssystemen nutzen, können davon betroffen sein. Wenn Sie diese Einstellung aktivieren, können unsere Erkennungssysteme vorübergehend gestört werden, was zu einem Rückgang der Metriken oder des Inputs führen kann, da mutmaßliche Bot-Klicks ausgeschlossen werden:

- Intelligente Auswahl
- Intelligenter Kanal
- Intelligentes Timing
- Experiment Schritt
    - Gewinnerpfad
    - Personalisierter Pfad
- Kampagne
    - Gewinnervariante
    - Personalisierte Variante
- Geschätzte reale Öffnungsrate

Abmeldungen aufgrund von mutmaßlichen Bot-Klicks sind davon nicht betroffen. Braze wird weiterhin alle Anfragen zum Abmelden wie gewohnt bearbeiten. Wenn Sie möchten, dass Braze diese Abmeldungen blockiert, senden Sie uns ein [Produkt-Feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

## Segmentierungsfilter, die von der Bot-Filterung betroffen sind

Die folgenden [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) können von der Bot-Filterung für Nachrichten per E-Mail betroffen sein:

- [Kampagne oder Canvas mit Tag angeklickt/geöffnet]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [Schritt angeklickt/geöffnet]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-step)
- [Alias in Kampagne angeklickt]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-campaign)
- [Alias in Canvas-Schritt angeklickt]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [Angeklickter Alias in einem beliebigen Kampagnen- oder Canvas-Schritt]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [Zuletzt mit Nachricht engagiert]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#last-engaged-with-message)
- [Intelligenter Kanal]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#intelligent-channel)

## Bot-Filter einschalten

Gehen Sie zu **Einstellungen** > **E-Mail-Voreinstellungen**. Wählen Sie dann **Bot-Klicks entfernen**. Diese Einstellung wird auf der Ebene des Workspaces vorgenommen.

Alle mutmaßlichen Bot-Klicks werden erst entfernt, nachdem die Einstellung aktiviert wurde, und gelten nicht rückwirkend für Metriken in Ihrem Workspace.

![Bot-Filter für E-Mails in den E-Mail-Einstellungen aktiviert.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
Wenn Sie diese Einstellung aktivieren und später wieder deaktivieren, kann Braze keine zuvor entfernten Bot-Aktivitäten in Ihrem Analytics wiederherstellen.
{% endalert %}

## Felder in E-Mail-Klick-Ereignissen für Currents und Snowflake

Braze sendet die Felder `is_suspected_bot_click` und `suspected_bot_click_reason` in Currents und Snowflake für ein E-Mail Klick-Ereignis.

| Feld | Datentyp | Beschreibung |
| `is_suspected_bot_click` | Boolean | Zeigt an, dass es sich um einen mutmaßlichen Bot-Klick handelt. Diese Werte werden als Nullwerte gesendet, bis Sie die Workspace-Einstellung **Klicks der Bots entfernen** aktivieren. Auf diese Weise können Sie programmatisch nachvollziehen, wann in Ihrem Workspace mit dem Filtern von mutmaßlichen Bot-Klicks begonnen wurde, so dass Sie dies genau mit den Daten in Currents und Snowflake vergleichen können. |
| `suspected_bot_click_reason` | Array | Gibt den Grund an, warum es sich um einen mutmaßlichen Bot-Klick handelt. Dieses Feld wird mit Werten wie `user_agent` und `ip_address` gefüllt, auch wenn die Einstellung Workspace für die Bot-Filterung deaktiviert ist. Dieses Feld kann Insights zu den potenziellen Auswirkungen der Aktivierung dieser Einstellung liefern, indem die Anzahl der Klicks, die von mutmaßlichen Bot-Klicks stammen, mit menschlichen Interaktionen verglichen wird. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Häufig gestellte Fragen

### Wie wirkt sich der Bot-Filter auf die Performance meiner Kampagne aus?

Dies hat keinen Einfluss auf die Metriken früherer Kampagnen, die bereits gesendet wurden. Wenn die Bot-Filterung in Ihrem Workspace aktiviert ist, beginnt Braze, mutmaßliche Bot-Klicks aus allen Klicks herauszufiltern. Sie werden vielleicht einen Rückgang der Klickraten feststellen, aber die Klick-Rate ist ein genaueres Abbild des Engagements Ihrer Nutzer:innen bei ihren Nachrichten per E-Mail.

### Wird der Bot-Filter verhindern, dass Bots, die auf den Link zum Abmelden von Braze klicken, sich abmelden können?

Nein. Alle Anfragen zur Abmeldung werden weiterhin bearbeitet.

### Werden Öffnungen von Rechnern bei der Filterung von Klicks durch den Bot berücksichtigt?

Nein.
