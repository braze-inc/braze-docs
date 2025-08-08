# Anwendungsfälle erstellen

> Erfahren Sie, wie Sie einen OfferFit-Anwendungsfall erstellen, damit Sie personalisierte Experimente automatisieren und Ergebnisse wie Konversionen, Bindung oder Umsatz optimieren können - ohne manuelle A/B-Tests.

{% multi_lang_include offerfit/alert_multi_platform_support.md %}

## Über Anwendungsfälle

Ein Anwendungsfall ist eine angepasste Konfiguration für die KI-Entscheidungsmaschine von OfferFit, die auf ein bestimmtes Geschäftsziel zugeschnitten ist.

Sie könnten zum Beispiel einen Anwendungsfall für Wiederholungskäufe erstellen, um die Konversionen nach einem Erstverkauf zu erhöhen. Sie definieren die Zielgruppe und die Nachricht in Braze, während OfferFit täglich Experimente durchführt und automatisch verschiedene Kombinationen von Produktangeboten, Zeitpunkt und Häufigkeit der Nachrichten für jeden Kunden testet. Mit der Zeit lernt OfferFit, was am besten funktioniert, und orchestriert personalisierte Sendungen über Braze, um die Wiederkaufsraten zu maximieren.

Um einen guten Anwendungsfall zu erstellen, werden Sie:

- Wählen Sie eine Erfolgsmetrik für OfferFit, auf die Sie optimieren möchten, z. B. Umsatz, Konversionen oder ARPU.
- Legen Sie fest, welche Dimensionen getestet werden sollen, z. B. Angebot, Betreffzeile, Kreativität, Kanal oder Sendezeitpunkt.
- Wählen Sie die Optionen für jede Dimension aus, z. B. E-Mail oder SMS oder tägliche oder wöchentliche Häufigkeit.

![Beispieldiagramm eines OfferFit Anwendungsfalls für Empfehlungen per E-Mail.]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## Beispielhafte Anwendungsfälle

Hier sind einige Beispiele für Anwendungsfälle, die Sie mit OfferFit erstellen können. Ihre KI-Entscheidungsagenten lernen aus jeder Kundeninteraktion und wenden diese Insights auf die Aktionen des nächsten Tages an.

{% multi_lang_include offerfit/sample_use_cases.md %}

## Erstellen eines Anwendungsfalls

### Voraussetzungen

Bevor Sie einen Anwendungsfall erstellen können, müssen Sie [OfferFit by Braze integrieren]({{site.baseurl}}/developer_guide/offerfit/integration).

### Schritt 1: Kontakt zu OfferFit

Das Team der KI Expert Serviceleistungen; Dienste; Dienste von OfferFit wird eng mit Ihnen zusammenarbeiten, um Ihren OfferFit-Anwendungsfall zu erfassen, zu entwerfen und zu erstellen. Wenn Sie es noch nicht getan haben, sollten Sie [Kontakt aufnehmen](https://offerfit.ai/book-now) und den Anfang machen.

Sie führen die folgenden Schritte gemeinsam durch, um einen angepassten Anwendungsfall zu erstellen, der für Sie geeignet ist.

### Schritt 2: Entwerfen Sie Ihren Anwendungsfall

Gemeinsam mit dem Team der KI Expert Serviceleistungen; Dienste von OfferFit werden Sie definieren:

- eine Zielgruppe, 
- die zu optimierende geschäftliche Metrik, 
- die Aktionen für den KI-Entscheidungsagenten von OfferFit, und 
- alle First-Party-Daten von Kund:in, die der Agent nutzen sollte, um Ihre Geschäftsergebnisse zu verbessern. 

Wenn der Entwurf steht, wird das Team mit Ihnen zusammenarbeiten, um alle zusätzlichen Integrationsanforderungen zu ermitteln und zu erfüllen.

### Schritt 3: Richten Sie Ihre Zustellungsplattform ein

Als nächstes hilft Ihnen das KI Expert Service Team bei der Einrichtung Ihrer Plattform für die Automatisierung des Marketings. OfferFit funktioniert zwar am besten mit Braze, aber auch eine Reihe anderer Plattformen werden unterstützt. Wenden Sie sich an Ihr KI Expert Service Team, um weitere Ressourcen zu erhalten.

{% tabs local %}
{% tab Braze %}
So richten Sie Braze ein:

1. Erstellen Sie eine [Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) oder ein [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=api-triggered%20delivery#step-2b-determine-your-canvas-entry-schedule). OfferFit verwendet diese Zustellung, um 1:1 personalisierte Aktivierungsereignisse an die Nutzer:innen Ihrer definierten Zielgruppe zu senden.
2. Stellen Sie sicher, dass Sie keine [Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) von Braze einbeziehen, damit OfferFit stattdessen die dedizierte Kontrollgruppe sein kann.
3. Abhängig von Ihren Dimensionen können Sie Liquid-Tags in Ihren kreativen Inhalten konfigurieren, um Ihr Messaging dynamisch mit OfferFit-Empfehlungen aufzufüllen. OfferFit übergibt über die Braze API kundenspezifische Inhalte an die Liquid-Tags in Ihren Templates.
{% endtab %}
{% endtabs %}

### Schritt 4: Starten und überwachen

Nach dem Start Ihres Anwendungsfalls wird Ihr Team von KI Expert Serviceleistungen; Dienste; Dienste diesen weiterhin überwachen und auf das von Ihnen vereinbarte Design abstimmen. Sie helfen Ihnen auch dabei, Anpassungen, Erweiterungen oder Änderungen am Anwendungsfall vorzunehmen, falls erforderlich.
