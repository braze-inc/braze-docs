---
nav_title: Agenten konzipieren
article_title: Agenten konzipieren
page_order: 3
description: "Erfahren Sie, wie Sie einen BrazeAI Decisioning Studio Go-Agenten entwerfen, einschließlich Definition der Zielgruppen, Dimensionen und Go-spezifischen Einschränkungen."
---

# Agenten konzipieren

> Dieser Artikel behandelt die Gestaltung Ihres Decisioning Studio Go-Agenten, einschließlich der Definition Ihrer Zielgruppe, der Auswahl von Dimensionen und des Verständnisses der Go-spezifischen Funktionen und Einschränkungen.

Grundlegende Konzepte zu Entscheidungsagenten – einschließlich Metriken, Dimensionen, Aktionsbanken und Einschränkungen – finden Sie unter [„Entscheidungsagenten entwerfen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/)“.

## Funktionen von Go im Vergleich zu Pro

Decisioning Studio Go ist eine Self-Service-Plattform mit im Vergleich zu Decisioning Studio Pro optimierten Funktionen. Das Verständnis dieser Unterschiede unterstützt Sie dabei, einen effektiven Agenten im Rahmen von Go zu entwickeln.

| Fähigkeit | Entscheidungsstudio Go | Entscheidungsstudio Pro |
|-----------|----------------------|------------------------|
| **Erfolgsmetriken** | Nur Klicks | Alle Geschäftsmetriken (Umsatz, Konversionen oder ARPU) |
| **Format** | Begrenzte Aktionsbank | Unbegrenzte Dimensionen |
| **CEPs unterstützt** | Braze, SFMC, Klaviyo | Jeder CEP (nativ und angepasst) |
| **Kundendaten** | Nur Engagement | Alle 1P-Daten |
| **Einrichtung** | Selbstbedienung | Unterstützung für KI-Entscheidungsdienste |
| **Versuchsgruppen** | Gehen Sie + Zufallssteuerung + optional BAU | Vollständig anpassbar |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Entwerfen Ihres Go-Agenten

Bei der Entwicklung eines Decisioning Studio Go-Agenten treffen Sie Entscheidungen in den folgenden Bereichen:

### Schritt 1: Definieren Sie Ihre Zielgruppe

Ihre Zielgruppe besteht aus der Gruppe der Kund:innen, mit denen der Agent in Kontakt treten wird. In Go werden Zielgruppen in Ihrem CEP definiert:

{% tabs %}
{% tab Braze %}

**Zielgruppe in Braze definieren:**

1. Erstellen Sie in Braze ein Segment, das die Kund:innen definiert, die der Agent ansprechen soll.
2. Wählen Sie bei der Konfiguration Ihres Experimentators im Decisioning Studio Go-Portal dieses Segment als Zielgruppe aus.

{% alert tip %}
Bitte erwägen Sie, ein spezielles Segment für Ihren Decisioning Studio Go-Experimentator zu erstellen, um Ihre Tests isoliert und messbar zu halten.
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

**Zielgruppe in SFMC definieren:**

1. Konfigurieren Sie eine Datenerweiterung, die Ihre Zielgruppe enthält.
2. Bitte stellen Sie sicher, dass diese Datenerweiterung täglich mit den neuesten Kundendaten aktualisiert wird.
3. Bitte referenzieren Sie bei der Konfiguration Ihres Experimentators diese Daten-Erweiterung im Decisioning Studio Go-Portal.

{% endtab %}
{% tab Klaviyo %}

**Zielgruppe in Klaviyo definieren:**

1. Erstellen Sie in Klaviyo ein Segment, das Ihre Zielgruppe definiert.
2. Bitte wählen Sie dieses Segment aus, wenn Sie Ihren Experimentator im Decisioning Studio Go-Portal konfigurieren.

{% endtab %}
{% endtabs %}

### Schritt 2: Bitte wählen Sie Ihre Maße aus.

Dimensionen sind die „Hebel“, die der Mitarbeiter betätigen kann, um das Kundenerlebnis zu personalisieren. Dazu gehören kreative Aspekte wie Betreffzeile und Hero-Bild sowie Aspekte des Versandtyps wie die Häufigkeit von E-Mails oder die Tageszeit. 

{% alert note %}
Die verfügbaren spezifischen Dimensionen hängen von Ihrem CEP und der Konfiguration Ihrer Kampagnen ab. Bitte arbeiten Sie mit den Templates und Inhalten, die Sie in Ihrem CEP eingerichtet haben.
{% endalert %}

### Schritt 3: Bitte konfigurieren Sie Ihre Aktionsbank.

Die Aktionsbank definiert die spezifischen Optionen, aus denen der Agent für jede Dimension auswählen kann. Zum Beispiel:

- **E-Mail-Templates**: Bitte wählen Sie aus, welche Templates der Agent verwenden darf (diese müssen zuvor in Ihrem CEP konfiguriert werden).
- **Betreffzeilen**: Definieren Sie die Varianten der Betreffzeile, die der Agent testen kann.
- **Versandzeiten**: Bitte geben Sie die Zeitfenster an, aus denen der Agent auswählen kann.

### Schritt 4: Versuchsgruppen einrichten

Das Decisioning Studio erstellt automatisch Versuchsgruppen, um die Performance zu messen:

| Gruppe | Beschreibung |
|-------|-------------|
| **Entscheidungsstudio Go** | Kunden, die KI-optimierte Empfehlungen erhalten |
| **Zufällige Steuerung** | Kund:innen, die zufällig ausgewählte Optionen erhalten (Basisvergleich) |
| **Geschäft wie gewohnt (optional)** | Kunden, die Ihre bestehende Kampagne erhalten (im Vergleich zur aktuellen Performance) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
Um einen genauen Vergleich zu gewährleisten, stellen Sie bitte sicher, dass keine Kund:in mehr als einer Versuchsgruppe angehören kann und dass die Kund:innen ohne Verzerrung zufällig den Gruppen zugeordnet werden.
{% endalert %}

## Zu berücksichtigende Einschränkungen

Bitte beachten Sie bei der Entwicklung Ihres Go-Agenten die folgenden Einschränkungen:

- **Nur Klicks**: Go optimiert die Click-through-Raten. Wenn Sie Ihre Umsatzzahlen, Konversionsraten oder andere Metriken optimieren möchten, empfehlen wir Ihnen Decisioning Studio Pro.
- **Begrenzte Abmessungen**: Go unterstützt eine vordefinierte Reihe von Dimensionen. Für benutzerdefinierte Dimensionen oder komplexe Personalisierungen empfehlen wir Decisioning Studio Pro.
- **Drei CEPs**: Go bietet nur eine Integration mit Braze, Salesforce Marketing Cloud und Klaviyo. Für andere Plattformen empfehlen wir Decisioning Studio Pro.

## Bewährte Praktiken

- **Beginnen Sie einfach**: Beginnen Sie mit 2-3 Templates oder Varianten der Betreffzeile. Dies bietet dem Agenten ausreichend Möglichkeiten zum Lernen, während das Experiment überschaubar bleibt.
- **Bitte geben Sie dem Ganzen etwas Zeit**: Der Agent benötigt ausreichende Daten, um zu lernen. Bitte warten Sie mindestens 2 bis 4 Wochen, bevor Sie Schlussfolgerungen zur Performance ziehen.
- **Sorgen Sie für abwechslungsreiche Inhalte**: Bitte stellen Sie sicher, dass Ihre Optionen sich deutlich voneinander unterscheiden. Das Testen geringfügiger Abweichungen liefert möglicherweise keine wesentlichen Insights.
- **Bitte regelmäßig überwachen**: Bitte überprüfen Sie das Decisioning Studio Go-Portal, um den Fortschritt des Experiments und die Metriken zum Engagement zu überwachen.

## Nächste Schritte

Nachdem Sie Ihren Agenten entworfen und im Decisioning Studio Go-Portal konfiguriert haben, können Sie mit dem Start fortfahren:

- [Starten Sie Ihren Agenten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/launch_your_agent/)
