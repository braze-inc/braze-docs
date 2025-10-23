# Agenten erstellen

> Erfahren Sie, wie Sie einen Agenten für BrazeAI Decisioning Studio™ erstellen, damit Sie personalisierte Experimente automatisieren und Ergebnisse wie Konversionen, Bindung oder Umsatz optimieren können – ohne manuelle A/B-Tests.

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## Über Agenten

Ein KI-Entscheidungsagent ist eine angepasste Konfiguration die BrazeAI™ Decisioning Engine, die auf ein bestimmtes Geschäftsziel zugeschnitten ist.

Sie könnten zum Beispiel einen Agenten für Wiederholungskäufe erstellen, um die Konversionen nach einem Erstverkauf zu erhöhen. Sie definieren die Zielgruppe und die Nachricht in Braze, während Ihre Decisioning-Studio-Agenten täglich Experimente durchführen und dabei automatisch verschiedene Kombinationen von Produktangeboten, Zeitpunkt und Häufigkeit der Nachrichten für individuelle Kund:innen testen. Mit der Zeit lernt Braze AI™, was am besten funktioniert, und orchestriert personalisierte Sendungen über Braze, um die Wiederkaufsraten zu maximieren.

So erstellen Sie einen guten Agenten:

- Wählen Sie eine Erfolgsmetrik für BrazeAI™ zur Optimierung aus, z. B. Umsatz, Konversionen oder ARPU.
- Legen Sie fest, welche Dimensionen getestet werden sollen, z. B. Angebot, Betreffzeile, Kreativität, Kanal oder Sendezeitpunkt.
- Wählen Sie die Optionen für jede Dimension aus, z. B. E-Mail oder SMS oder tägliche oder wöchentliche Häufigkeit.

![Example diagram of a decisioning studio agent for referral emails.]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## Beispiel-Agenten

Hier sind einige Beispiele für Agenten, die Sie mit BrazeAI Decisioning Studio™ erstellen können. Ihre KI-Entscheidungsagenten lernen aus jeder Kundeninteraktion und wenden diese Insights auf die Aktionen des nächsten Tages an.

{% multi_lang_include decisioning_studio/sample_agents.md %}

## Agenten erstellen

### Voraussetzungen

Bevor Sie einen Agenten erstellen können, müssen Sie [das BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/integration) integrieren.

### Schritt 1: AI Expert Services kontaktieren

Das Team von AI Expert Services wird eng mit Ihnen zusammenarbeiten, um Ihren Entscheidungsagenten zu konzipieren und zu erstellen. Wenn Sie es noch nicht getan haben, sollten Sie [Kontakt aufnehmen](https://www.braze.com/get-started/) und den Anfang machen.

Sie werden die folgenden Schritte gemeinsam ausführen, um einen angepassten Agenten zu erstellen, der genau auf Sie zugeschnitten ist.

### Schritt 2: Agenten konzipieren

Zusammen mit dem Team von AI Expert Services definieren Sie:

- eine Zielgruppe, 
- die zu optimierende geschäftliche Metrik, 
- die Aktionen für den BrazeAI™-Entscheidungsagenten und 
- alle First-Party-Kundendaten, die der Agent nutzen sollte, um Ihre Geschäftsergebnisse zu verbessern. 

Wenn der Entwurf steht, wird das Team mit Ihnen zusammenarbeiten, um alle zusätzlichen Integrationsanforderungen zu ermitteln und zu erfüllen.

### Schritt 3: Richten Sie Ihre Zustellungsplattform ein

Als nächstes hilft Ihnen das Team von AI Expert Services bei der Einrichtung Ihrer Plattform für die Automatisierung des Marketings. Das Decisioning Studio funktioniert zwar am besten mit Braze, aber auch eine Reihe anderer Plattformen werden unterstützt. Wenden Sie sich an Ihr Team von AI Expert Services, um weitere Ressourcen zu erhalten.

{% tabs local %}
{% tab Braze %}
So richten Sie Braze ein:

1. Erstellen Sie eine [Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) oder ein [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=api-triggered%20delivery#step-2b-determine-your-canvas-entry-schedule). BrazeAI Decisioning Studio™ verwendet diese Zustellung, um personalisierte 1:1-Aktivierungs-Events an die Nutzer:innen in Ihrer definierten Zielgruppe zu senden.
2. Achten Sie darauf, dass Sie keine [Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) für Braze einschließen, damit BrazeAI™ stattdessen die dedizierte Kontrollgruppe sein kann.
3. Abhängig von Ihren Dimensionen können Sie Liquid-Tags in Ihren kreativen Inhalten konfigurieren, um Ihr Messaging dynamisch mit BrazeAI™-Empfehlungen aufzufüllen. BrazeAI™ übergibt dann über die Braze API kundenspezifische Inhalte an die Liquid-Tags in Ihren Templates.
{% endtab %}
{% endtabs %}

### Schritt 4: Starten und überwachen

Nach dem Start Ihres Agenten wird das Team von AI Expert Services ihn weiterhin überwachen und auf das von Ihnen vereinbarte Design abstimmen. Sie helfen Ihnen auch bei Anpassungen, Erweiterungen oder Änderungen des Agenten, falls erforderlich.
