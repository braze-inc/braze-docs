---
nav_title: Content Optimizer
article_title: Schritt „Content Optimizer Agent"
alias: "/content_optimizer_step/"
page_order: 5
description: "Mit dem Schritt „Content Optimizer Agent" können Sie mehrere Versionen von Inhaltskomponenten in einem einzigen Schritt konfigurieren und testen. Er unterstützt Sie dabei, mit verschiedenen Inhaltsvariationen zu experimentieren und optimiert diese im Laufe der Zeit automatisch in Richtung der Kombinationen mit der besten Performance."
page_type: reference

---

# Schritt „Content Optimizer Agent"

> Mit dem Schritt „Content Optimizer Agent" können Sie mehrere Versionen von Inhaltskomponenten in einem einzigen Schritt konfigurieren und testen. Er unterstützt Sie dabei, mit verschiedenen Inhaltsvariationen zu experimentieren und optimiert diese im Laufe der Zeit automatisch in Richtung der Kombinationen mit der besten Performance. Eine Einführung finden Sie unter [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
Der Content Optimizer befindet sich derzeit in der Beta-Phase. Für Unterstützung beim Einstieg wenden Sie sich bitte an Ihren Customer-Success-Manager.
{% endalert %}

## Erstellen eines Schritts „Content Optimizer"

Um optimale Ergebnisse zu erzielen, verwenden Sie den Content Optimizer-Agenten in Canvases, in denen Nutzer:innen den Schritt nach und nach über einen längeren Zeitraum betreten. Sollten alle Nutzer:innen gleichzeitig den Schritt betreten, hat der Agent keine Zeit, aus den ersten Ergebnissen zu lernen.

### 1. Schritt: Einen Schritt hinzufügen

Ziehen Sie die Komponente **Content Optimizer** aus der Seitenleiste per Drag-and-Drop oder wählen Sie den <i class="fas fa-plus-circle"></i> Plus-Button am unteren Rand eines Schritts und dann **Content Optimizer** aus.

### 2. Schritt: Erstellen Sie Ihre Basisnachricht

Die Basisnachricht ist der Ausgangspunkt für Ihren Schritt. Varianten für jede Inhaltskomponente werden dynamisch auf Grundlage der Kombinationen eingefügt, die auf dem Tab **Content Optimizer-Einstellungen** definiert sind.

{% alert note %}
Während der Beta-Phase wird ausschließlich E-Mail als Kanal unterstützt.
{% endalert %}

Wählen Sie auf dem Tab **Messaging-Kanäle** die Option **E-Mail** aus und erstellen Sie Ihre Basis-E-Mail-Nachricht. Weitere Informationen finden Sie in unserem speziellen [E-Mail]({{site.baseurl}}/user_guide/message_building_by_channel/email)-Abschnitt.

Der Content Optimizer-Agent verwendet die in dieser Variante angegebenen Sendeeinstellungen (wie die E-Mail-Domain und die Antwortadresse), um alle Nachrichten zu versenden. Sie können entweder mit einem neuen Design beginnen oder ein vorhandenes Template für diese Nachricht auswählen. Überlegen Sie in diesem Schritt, welche Komponenten der Nachricht Sie optimieren möchten. Diese definieren Sie in [Schritt 4](#step-4).

Unterstützte Komponenten zur Optimierung umfassen:

- Betreff
- Body-Kopfzeile
- Body-Inhalt
- Primäre CTA

### 3. Schritt: Zustellungseinstellungen festlegen

Auf dem Tab **Zustellungseinstellungen** können Sie festlegen, ob der Schritt intelligentes Timing oder Zustellungsvalidierungen verwenden soll. Weitere Informationen finden Sie unter [Zustellungseinstellungen bearbeiten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) im Schritt „Nachricht".

### 4. Schritt: Inhaltskomponenten und Varianten hinzufügen {#step-4}

Inhaltskomponenten sind die einzelnen Elemente Ihrer Nachricht, die Sie testen möchten – beispielsweise verschiedene Betreffzeilen, Überschriften, Fließtexte oder primäre Handlungsaufforderungen. Mit diesen Komponenten können Sie mehrere Versionen einer Nachricht erstellen und diese im Laufe der Zeit automatisch auf Grundlage der Performance optimieren.

Sie können bis zu drei Inhaltskomponenten pro Schritt und bis zu fünf Varianten pro Komponente hinzufügen, was insgesamt 125 eindeutige Inhaltskombinationen ergibt.

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten in der Schnittstelle des Content Optimizers. Die Schnittstelle zeigt auswählbare Komponenten wie Betreff, Body-Kopfzeile, Body-Inhalt und primäre CTA an, die jeweils über Felder zur Eingabe verschiedener Varianten verfügen.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Schritt 4.1: Inhaltskomponenten konfigurieren

So konfigurieren Sie Komponenten:

1. Gehen Sie zum Tab **Content Optimizer-Einstellungen**.
2. Wählen Sie aus, welche Komponenten Sie optimieren möchten. Unterstützte Optionen:
  - Betreff
  - Body-Kopfzeile
  - Body-Inhalt
  - Primäre CTA
3. Definieren Sie für jede ausgewählte Komponente eine Reihe alternativer Versionen dieses Inhalts (Varianten). Verwenden Sie klare, eindeutige Varianten, die sich in Tonfall, Struktur oder Inhalt unterscheiden. Dies hilft dem Content Optimizer, die leistungsstärksten Inhalte effektiver zu identifizieren. Sie können:
  - Ihre eigenen Varianten manuell erstellen.
  - KI-generierte Vorschläge nutzen, um schnell neue Optionen zu erkunden.

![Die Schnittstelle der Content Optimizer-Einstellungen zeigt Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten für die E-Mail-Optimierung an. Jede Komponente verfügt über Eingabefelder für verschiedene Varianten. Der sichtbare Text umfasst Komponentennamen und Felder zur Eingabe von Variantentext.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Schritt 4.2: Liquid zu Ihrer Nachricht hinzufügen

Nachdem Sie mindestens zwei Varianten für jede Komponente definiert haben, kopieren Sie den zugehörigen Liquid-Tag für jede Komponente und fügen Sie ihn an der entsprechenden Stelle in Ihrer Basisnachricht ein.

- Wenn Sie beispielsweise die Betreffzeile optimieren möchten, fügen Sie den {% raw %}`{% message_component "Subject" %}`{% endraw %}-Tag in das Betrefffeld des E-Mail-Editors ein.
- Sie können auch Komponenten-Tags in längere Texte einfügen, um nur einen Teil der Komponente zu testen. Beispiel: {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Optionen zum Hinzufügen und Konfigurieren von Inhaltskomponenten wie Betreff, Body-Kopfzeile, Body-Inhalt und primäre CTA. Jede Komponente verfügt über Felder zur Eingabe verschiedener Varianten.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Wenn Sie für eine ausgewählte Inhaltskomponente keinen Liquid-Tag hinzufügen, wird auf dem Tab **Content Optimizer-Einstellungen** eine Warnung und auf dem Tab **Messaging-Kanäle** ein Fehler angezeigt. Das Canvas kann erst gestartet werden, wenn alle ausgewählten Komponenten ordnungsgemäß zu Ihrer Basisnachricht hinzugefügt wurden.

Während das Canvas ausgeführt wird, kombiniert der Agent Varianten aus verschiedenen Komponenten, um unterschiedliche Inhaltskombinationen zu generieren. Im Laufe der Zeit werden leistungsstärkere Kombinationen für die Zustellung priorisiert, sodass Sie die Performance ohne manuelle Eingriffe verbessern können.

#### Liquid-Referenz

| Komponente | Liquid-Snippet |
| --- | --- | 
| Betreff | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| Body-Kopfzeile | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Body-Inhalt | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| Primäre CTA | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 5. Schritt: Optimierungsereignis auswählen

Das Optimierungsereignis bestimmt, wie der Content Optimizer-Agent die Performance bewertet und den Traffic im Laufe der Zeit auf Inhaltskombinationen verteilt.

Für E-Mails können Sie für eines der folgenden Ereignisse optimieren. Der Agent nutzt Öffnungen und Klicks, die innerhalb von 7 Tagen nach dem Versand einer Nachricht registriert werden, um die Zustellung auf leistungsstärkere Inhaltskombinationen zu verlagern.

| Ereignis | Beschreibung | Anwendungsfälle |
| --- | --- | --- |
| Öffnungen | Optimiert für Kombinationen, die Empfänger:innen dazu veranlassen, die E-Mail zu öffnen. | Testen von Betreffzeilen oder Steigerung der Sichtbarkeit |
| Klicks | Optimiert für Kombinationen, die Engagement mit Links fördern. Bot-Klicks oder von Braze erkannte Klicks zum Abmelden sind nicht enthalten. | Steigerung von Traffic, Engagement oder Konversion über Links |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Das von Ihnen ausgewählte Optimierungsereignis gilt für alle Inhaltskomponenten in diesem Schritt.

## Best Practices

- Generell empfehlen wir, mehr als eine Komponente für den Schritt „Content Optimizer" zu testen.
- Wenn Sie für Klicks optimieren, beziehen Sie Betreffzeilen in Ihre Tests ein, da stärkere Betreffzeilen zu mehr Öffnungen beitragen und somit mehr Möglichkeiten für Klicks schaffen können.
- Wenn Sie für Öffnungen optimieren, konzentrieren Sie Ihre Tests auf die Betreffzeile.

## Analytics

Um die Performance zu überprüfen, öffnen Sie das Analytics-Panel auf Schritt-Ebene, um die Metriken nach Inhaltsvariante und Gesamtkombinationsleistung anzuzeigen. Der Schritt „Content Optimizer" verwendet [dieselben Analytics wie der Schritt „Nachricht"]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics).

![Content Optimizer Analytics für drei Buttons und den prozentualen Anteil der Sendezuweisung, die einen Aufwärtstrend aufweisen.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

## Fehlerbehebung

| Problem | Beschreibung | Lösung |
| --- | --- | --- |
| Fehlende Liquid-Tags | Wenn Sie eine Inhaltskomponente (wie Betreff oder CTA) hinzufügen, jedoch den entsprechenden Liquid-Tag nicht in Ihre Basisnachricht einfügen, wird Folgendes angezeigt: <br>- Eine Warnung auf dem Tab **Content Optimizer-Einstellungen** <br>- Ein Fehler auf dem Tab **Messaging-Kanäle** | Kopieren Sie das Liquid-Snippet, das unter jeder Komponente auf dem Tab **Content Optimizer-Einstellungen** angezeigt wird, und fügen Sie es an der entsprechenden Stelle in Ihre Nachricht ein. |
| Verwaiste Liquid-Tags | Wenn Sie eine Inhaltskomponente löschen, den zugehörigen Liquid-Tag jedoch in der Basisnachricht belassen, wird die Nachricht beim Versand möglicherweise nicht wie erwartet dargestellt. | Entfernen Sie alle nicht verwendeten `message_component`-Tags aus Ihrer Basisnachricht, bevor Sie sie starten. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }