---
nav_title: Content Optimizer
article_title: Schritt „Contentful Agent“ 
alias: "/content_optimizer_step/"
page_order: 5
description: "Mit dem Schritt „Content Optimizer Agent“ können Sie mehrere Versionen von Inhaltskomponenten in einem einzigen Schritt konfigurieren und testen. Es unterstützt Sie dabei, mit verschiedenen Inhalten zu experimentieren und optimiert diese im Laufe der Zeit automatisch zu den Kombinationen mit der besten Performance."
page_type: reference

---

# Schritt „Contentful Agent“

> Mit dem Schritt „Content Optimizer Agent“ können Sie mehrere Versionen von Inhaltskomponenten in einem einzigen Schritt konfigurieren und testen. Es unterstützt Sie dabei, mit verschiedenen Inhalten zu experimentieren und optimiert diese im Laufe der Zeit automatisch zu den Kombinationen mit der besten Performance. Für eine Einführung, sehen Sie sich [bitte den Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/) an.

{% alert important %}
Der Content Optimizer befindet sich derzeit in der Beta-Phase. Für Unterstützung beim Einstieg wenden Sie sich bitte an Ihren Customer-Success-Manager.
{% endalert %}

## Erstellen eines Schritts „Content Optimizer“

Um optimale Ergebnisse zu erzielen, verwenden Sie den Content Optimizer-Agenten in Canvases, in denen Nutzer:innen den Schritt schrittweise über einen längeren Zeitraum eingeben. Sollten alle Nutzer:innen gleichzeitig den Schritt ausführen, hat der Agent keine Zeit, aus den ersten Ergebnissen zu lernen. 

### Schritt 1: Einen Schritt hinzufügen

Ziehen Sie die Komponente **„Content Optimizer“** aus der Seitenleiste per Drag-and-Drop oder wählen Sie **„Content Optimizer“** über <i class="fas fa-plus-circle"></i>den Button am unteren Rand eines Schritts aus.

### Schritt 2: Erstellen Sie Ihre Basenachricht

Die Basenachricht ist der Ausgangspunkt für Ihren Schritt. Varianten für jede Inhaltskomponente werden dynamisch auf Grundlage der Kombinationen eingefügt, die auf dem Tab **„Einstellungen für den Inhaltsoptimierer“** definiert sind. 

{% alert note %}
Während der Beta-Phase wird ausschließlich E-Mail als Kanal zur Kommunikation unterstützt.
{% endalert %}

Wählen Sie auf der Registerkarte **„Messaging-Kanäle“** **die Option „E-Mail“** aus und erstellen Sie Ihre Basis-E-Mail-Nachricht. Bitte referenzieren Sie unseren speziellen [E-Mail]({{site.baseurl}}/user_guide/message_building_by_channel/email)-Bereich für weitere Informationen. 

Der Content Optimizer-Agent verwendet die in dieser Variante angegebenen Sendeeinstellungen (wie die E-Mail-Domäne und die Antwortadresse), um alle Nachrichten zu versenden. Sie können entweder mit einem neuen Design beginnen oder ein vorhandenes Template für diese Nachricht auswählen. Bitte überlegen Sie in diesem Schritt, welche Komponenten der Nachricht Sie optimieren möchten. Sie werden diese in [Schritt 4](#step-4) definieren.

Unterstützte Komponenten zur Optimierung umfassen:

- Betreff
- Körper Kopfzeile
- Körper Inhalt
- Primäre CTA

### Schritt 3: Zustellungseinstellungen festlegen

Auf dem Tab **„Zustellungseinstellungen“** können Sie festlegen, ob der Schritt „intelligentes Timing“ oder Zustellungsvalidierungen verwenden soll. Weitere Informationen referenzieren Sie unter [„Zustellungseinstellungen bearbeiten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings)“ im Schritt „Nachricht“.

### Schritt 4: Inhaltskomponenten und Varianten hinzufügen {#step-4}

Inhaltskomponenten sind die einzelnen Elemente Ihrer Nachricht, die Sie testen möchten, wie beispielsweise verschiedene Betreffzeilen, Überschriften, Fließtexte oder primäre Handlungsaufforderungen. Mit diesen Komponenten können Sie mehrere Versionen einer Nachricht erstellen und diese im Laufe der Zeit automatisch auf der Grundlage der Performance optimieren.

Sie können bis zu drei Inhaltskomponenten pro Schritt und bis zu fünf Varianten pro Komponente hinzufügen, was insgesamt 125 eindeutige Inhaltskombinationen ergibt.

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten in der Schnittstelle des Content Optimizers. Die Schnittstelle zeigt auswählbare Komponenten wie Betreff, Kopfzeile, Textinhalt und primäre CTA an, die jeweils über Felder zur Eingabe verschiedener Varianten verfügen.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Schritt 4.1: Inhaltskomponenten konfigurieren

So konfigurieren Sie Komponenten:

1. Bitte gehen Sie zum Tab **„Einstellungen** für den **Content Optimizer**“.
2. Bitte wählen Sie aus, welche Komponenten Sie optimieren möchten. Unterstützte Optionen:
  - Betreff
  - Körper Kopfzeile
  - Körper Inhalt
  - Primäre CTA
3. Definieren Sie für jede ausgewählte Komponente eine Reihe alternativer Versionen dieses Inhalts (Varianten). Verwenden Sie klare, eindeutige Varianten, die sich in Tonfall, Struktur oder Inhalt unterscheiden. Dies unterstützt den Content Optimizer dabei, die leistungsstärksten Inhalte effektiver zu identifizieren. Sie können:
  - Bitte erstellen Sie Ihre eigenen Varianten manuell.
  - Nutzen Sie KI-generierte Vorschläge, um schnell neue Optionen zu erkunden.

![Die Schnittstelle der Content-Optimierungseinstellungen zeigt Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten für die Optimierung der E-Mail-Kommunikation an. Jede Komponente verfügt über Eingabefelder für die Eingabe verschiedener Varianten. Der sichtbare Text umfasst Komponentennamen und Felder zur Eingabe von Text für Varianten.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Schritt 4.2: Bitte fügen Sie Ihrer Nachricht Liquid hinzu.

Nachdem Sie mindestens zwei Varianten für jede Komponente definiert haben, kopieren Sie bitte das zugehörige Liquid-Tag für jede Variante und fügen Sie es an den entsprechenden Standorten in Ihrer Basismeldung ein.

- Wenn Sie beispielsweise die Betreffzeile optimieren möchten, fügen Sie den{% raw %}`{% message_component "Subject" %}`{% endraw %}Tag in das Betrefffeld des E-Mail-Editors ein.
- Sie können auch Komponenten-Tags in längere Texte einfügen, um nur einen Teil der Komponente zu testen. Beispielsweise: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten wie Betreff, Kopfzeile, Textinhalt und primäre CTA. Jede Komponente verfügt über Felder zur Eingabe verschiedener Varianten.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Wenn Sie für eine ausgewählte Inhaltskomponente keinen Liquid-Tag hinzufügen, wird auf der Registerkarte **„Content Optimizer-Einstellungen“** eine Warnung und auf der Registerkarte **„Messaging-Kanäle“** ein Fehler angezeigt. Das Canvas kann erst gestartet werden, wenn alle ausgewählten Komponenten ordnungsgemäß zu Ihrer Basenachricht hinzugefügt wurden.

Während Canvas ausgeführt wird, kombiniert der Agent Varianten aus verschiedenen Komponenten, um unterschiedliche Inhaltskombinationen zu generieren. Im Laufe der Zeit werden leistungsstärkere Kombinationen für die Zustellung priorisiert, wodurch Sie die Performance ohne manuelle Eingriffe verbessern können.

#### Flüssigkeitsreferenz

| Komponente | Liquid Snippet |
| --- | --- | 
| Betreff | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Körper Kopfzeile | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Körper Inhalt | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| Primäre CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Schritt 5: Optimierungsereignis auswählen

Das Optimierungsereignis bestimmt, wie der Content Optimizer-Agent die Performance bewertet und den Datenverkehr im Laufe der Zeit auf Inhaltskombinationen verteilt. 

Für E-Mails können Sie für eines der folgenden Ereignisse optimieren. Der Agent nutzt Öffnungen und Klicks, die innerhalb von 7 Tagen nach dem Versand einer Nachricht registriert werden, um die Zustellung auf leistungsstärkere Inhaltskombinationen zu verlagern.

| Event | Beschreibung | Anwendungsfälle |
| --- | --- | --- |
| Öffnungen | Optimiert für Kombinationen, die die Empfänger:innen dazu veranlassen, die E-Mail zu öffnen. | Testung von Betreffzeilen oder Bemühungen zur Steigerung der Sichtbarkeit |
| Klicks | Optimiert für Kombinationen, die Engagement mit Links fördern. Bot-Klicks oder von Braze erkannte Klicks zum Abmelden sind nicht enthalten. | Steigerung von Traffic, Engagement oder Konversion über Links |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Die von Ihnen ausgewählte Optimierungsmaßnahme gilt für alle Inhaltskomponenten in diesem Schritt. 

## Analytics

Um die Performance zu überprüfen, öffnen Sie bitte das Analytics-Panel auf Schritt-Ebene, um die Metriken nach Inhaltsvariante und Gesamtkombinationsleistung anzuzeigen. Der Schritt „Content Optimizer“ verwendet [dieselben Analytics wie der Schritt „Nachricht]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics)“.

![Content Optimizer Analytics für drei Buttons und den Prozentsatz der Zuweisung von Sendungen, die einen Aufwärtstrend aufweisen.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

## Fehlersuche

| Fehler | Beschreibung | Behebung |
| --- | --- | --- |
| Fehlende Liquid-Tags | Wenn Sie eine Inhaltskomponente (wie Betreff oder CTA) hinzufügen, jedoch nicht den entsprechenden Liquid-Tag in Ihre Basenachricht einfügen, wird Folgendes angezeigt: <br>\- Eine Warnung auf dem Tab **„Einstellungen für den Inhaltsoptimierer“** <br>\- Ein Fehler auf der Registerkarte **„Messaging-Kanäle“** | Bitte kopieren Sie das Liquid-Snippet, das unter jeder Komponente auf dem Tab **„Content Optimizer-Einstellungen“** angezeigt wird, und fügen Sie es an der entsprechenden Stelle in Ihre Nachricht ein. |
| Verwaiste Liquid-Tags | Wenn Sie eine Inhaltskomponente löschen, jedoch deren Liquid-Tag in der Basismeldung belassen, wird die Nachricht beim Versenden möglicherweise nicht wie erwartet dargestellt. | Bitte entfernen Sie alle nicht verwendeten`message_component`Tags aus Ihrer Basenachricht, bevor Sie sie versenden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

