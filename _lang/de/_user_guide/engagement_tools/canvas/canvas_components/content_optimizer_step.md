---
nav_title: Content Optimizer
article_title: Content Optimizer Agent Schritt 
alias: "/content_optimizer_step/"
page_order: 5
description: "Mit dem Agentenschritt Content Optimizer können Sie mehrere Versionen von Inhaltskomponenten in einem einzigen Schritt konfigurieren und testen. Es hilft Ihnen beim Experimentieren mit Inhaltsvariationen und optimiert im Laufe der Zeit automatisch in Richtung der leistungsstärksten Kombinationen."
page_type: reference

---

# Content Optimizer Agent Schritt

> Mit dem Agentenschritt Content Optimizer können Sie mehrere Versionen von Inhaltskomponenten in einem einzigen Schritt konfigurieren und testen. Es hilft Ihnen beim Experimentieren mit Inhaltsvariationen und optimiert im Laufe der Zeit automatisch in Richtung der leistungsstärksten Kombinationen. Eine Einführung finden Sie unter [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
Content Optimizer befindet sich derzeit in der Beta-Phase. Wenn Sie Hilfe benötigen, wenden Sie sich an Ihren Customer-Success-Manager:in.
{% endalert %}

## Erstellen eines Content Optimizer Schritts

Die besten Ergebnisse erzielen Sie, wenn Sie den Agenten Content Optimizer in Canvase verwenden, wo die Nutzer:innen den Schritt nach und nach eingeben. Wenn alle Nutzer:innen den Schritt auf einmal eingeben, hat der Agent keine Zeit, aus den ersten Ergebnissen zu lernen. 

### Schritt 1: Einen Schritt hinzufügen

Ziehen Sie die Komponente **Content Optimizer** per Drag-and-Drop aus der Seitenleiste, oder wählen Sie den <i class="fas fa-plus-circle"></i> plus Button am Ende eines Schrittes und wählen Sie **Content Optimizer**.

### Schritt 2: Erstellen Sie Ihre Basisnachricht

Die Basisnachricht ist der Ausgangspunkt für Ihren Schritt. Varianten für jede Inhaltskomponente werden dynamisch eingefügt, basierend auf den Kombinationen, die im Tab **Einstellungen für Content Optimizer** definiert sind. 

{% alert note %}
Während der Beta-Phase ist E-Mail der einzige unterstützte Kanal.
{% endalert %}

Wählen Sie auf dem Tab **Messaging-Kanäle** die Option **E-Mail** und erstellen Sie Ihre Basisnachricht. Hilfe finden Sie in unserem speziellen Bereich für [E-Mails]({{site.baseurl}}/user_guide/message_building_by_channel/email). 

Der Content Optimizer Agent verwendet die in dieser Variante angegebenen Sendeeinstellungen (wie die E-Mail Domain und die Antwort-E-Mail Adresse), um alle Nachrichten zu versenden. Sie können entweder mit einem neuen Entwurf beginnen oder ein bestehendes Template für diese Nachricht auswählen. Überlegen Sie bei diesem Schritt, für welche Komponenten der Nachricht Sie optimieren möchten. Sie werden diese in [Schritt 4](#step-4) definieren.

Zu den unterstützten Komponenten für die Optimierung gehören:

- Betreff
- Körper Kopfzeile
- Körper Inhalt
- Primäre CTA

### Schritt 3: Einstellungen für die Zustellung festlegen

Auf dem Tab **Zustellungseinstellungen** können Sie angeben, ob der Schritt Intelligentes Timing oder Zustellungsvalidierungen verwenden soll. Weitere Einzelheiten finden Sie unter [Einstellungen für die Zustellung]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) im Schritt Nachricht [bearbeiten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings).

### Schritt 4: Inhaltskomponenten und Varianten hinzufügen {#step-4}

Inhaltskomponenten sind die einzelnen Elemente Ihrer Nachricht, die Sie testen möchten, wie z.B. verschiedene Betreffzeilen, Überschriften, Textkörper oder primäre Handlungsaufforderungen. Diese Komponenten erlauben es Ihnen, mehrere Versionen einer Nachricht zu erstellen und automatisch auf der Grundlage der Performance im Laufe der Zeit zu optimieren.

Sie können bis zu drei Inhaltskomponenten pro Schritt und bis zu fünf Varianten pro Komponente hinzufügen, was insgesamt 125 eindeutige Inhaltskombinationen ermöglicht.

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten in der Schnittstelle des Content Optimizer. Die Schnittstelle zeigt auswählbare Komponenten wie Betreff, Body Header, Body Content und Primary CTA, jeweils mit Feldern zur Eingabe verschiedener Varianten.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Schritt 4.1: Konfigurieren Sie Inhaltskomponenten

So konfigurieren Sie Komponenten:

1. Gehen Sie zum Tab **Content Optimizer Einstellungen**.
2. Wählen Sie die Komponenten, die Sie optimieren möchten. Unterstützte Optionen:
  - Betreff
  - Körper Kopfzeile
  - Körper Inhalt
  - Primäre CTA
3. Definieren Sie für jede ausgewählte Komponente eine Reihe von alternativen Versionen dieses Inhalts (Varianten). Verwenden Sie klare, deutliche Varianten, die sich in Ton, Struktur oder Inhalt unterscheiden. So kann Content Optimizer die Top-Performer besser identifizieren. Sie können:
  - Schreiben Sie Ihre eigenen Varianten manuell.
  - Nutzen Sie die von der KI generierten Vorschläge, um schnell neue Optionen zu erkunden.

![Die Schnittstelle für die Einstellungen des Content Optimizer zeigt Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten für die Optimierung von E-Mails. Jede Komponente hat Eingabefelder für die Eingabe verschiedener Varianten. Der sichtbare Text umfasst Komponentennamen und Felder für die Eingabe von Variantestext.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Schritt 4.2: Liquid zu Ihrer Nachricht hinzufügen

Nachdem Sie mindestens zwei Varianten für jede Komponente definiert haben, kopieren Sie den zugehörigen Liquid-Tag für jede Komponente und fügen ihn an dem entsprechenden Standort in Ihrer Basis Nachricht ein.

- Wenn Sie zum Beispiel die Betreffzeile optimieren, fügen Sie den Tag {% raw %}`{% message_component "Subject" %}`{% endraw %} in das Betrefffeld des E-Mail Composers ein.
- Sie können auch Tags für Komponenten in längeren Text einfügen, um nur einen Teil der Komponente zu testen. Zum Beispiel: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten wie Betreff, Body Header, Body Content und Primary CTA. Jede Komponente verfügt über Felder zur Eingabe verschiedener Varianten.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Wenn Sie für eine ausgewählte Inhaltskomponente kein Liquid-Tag hinzufügen, wird auf dem Tab **Einstellungen für die Inhaltsoptimierung** eine Warnung und auf dem Tab **Messaging-Kanäle** ein Fehler angezeigt. Das Canvas kann erst dann gestartet werden, wenn alle ausgewählten Komponenten ordnungsgemäß zu Ihrer Basisnachricht hinzugefügt wurden.

Während der Ausführung des Canvas mischt der Agent die Varianten der einzelnen Komponenten, um verschiedene Inhaltskombinationen zu erzeugen. Im Laufe der Zeit werden leistungsstärkere Kombinationen für die Zustellung priorisiert, so dass Sie die Performance ohne manuelle Eingriffe verbessern können.

#### Liquid referenzieren

| Komponente | Liquid Snippet |
| --- | --- | 
| Betreff | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Körper Kopfzeile | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Körper Inhalt | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| Primäre CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 5: Optimierungsereignis auswählen

Das Optimierungsereignis legt fest, wie der Content Optimizer Agent die Performance bewertet und den Datenverkehr im Laufe der Zeit den Inhaltskombinationen zuweist. 

Für E-Mail können Sie auf eines der folgenden Ereignisse optimieren. Der Agent verwendet Öffnungen und Klicks, die innerhalb von 7 Tagen nach dem Versand einer Nachricht registriert werden, um die Zustellung auf leistungsstärkere Inhaltskombinationen zu verlagern.

| Event | Beschreibung | Anwendungsfälle |
| --- | --- | --- |
| Öffnungen | Optimiert für Kombinationen, die Empfänger:innen dazu bringen, die E-Mail zu öffnen. | Testen Sie Betreffzeilen oder versuchen Sie, die Sichtbarkeit zu erhöhen |
| Klicks | Optimiert für Kombinationen, die das Engagement mit Links fördern. Enthält keine Bot-Klicks oder von Braze erkannte Klicks zum Abmelden. | Mehr Traffic, Engagement oder Konversion durch Links |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Ihr ausgewähltes Optimierungsereignis gilt für alle Inhaltskomponenten in diesem Schritt. 

## Analytics

Um die Performance zu überprüfen, öffnen Sie das Analytics Panel auf Schrittebene, um die Metriken nach Variante des Inhalts und die Gesamtperformance der Kombination zu sehen. Der Schritt Content Optimizer verwendet die gleichen Analytics wie der Schritt Messaging. Einzelheiten finden Sie unter [Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics) im Schritt Nachrichten.  

## Fehlersuche

| Fehler | Beschreibung | Behebung |
| --- | --- | --- |
| Fehlende Liquid-Tags | Wenn Sie eine Inhaltskomponente (z.B. Betreff oder CTA) hinzufügen, aber den entsprechenden Liquid-Tag nicht in Ihre Basisnachricht einfügen, werden Sie sehen: <br>\- Eine Warnung auf dem Tab **Inhaltsoptimierungseinstellungen**  <br>\- Ein Fehler auf dem Tab **Messaging-Kanäle**  | Kopieren Sie das Liquid Snippet, das unter jeder Komponente im Tab **Einstellungen für die Inhaltsoptimierung** angezeigt wird, und fügen Sie es an der entsprechenden Stelle Ihrer Nachricht ein. |
| Verwaiste Liquid-Tags | Wenn Sie eine Inhaltskomponente löschen, aber ihren Liquid-Tag in der Basisnachricht belassen, wird die Nachricht beim Versand möglicherweise nicht wie erwartet dargestellt. | Entfernen Sie alle unbenutzten `message_component` Tags aus Ihrer Basis Nachricht, bevor Sie diese starten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

