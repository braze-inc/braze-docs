---
nav_title: Agenten konzipieren
article_title: Agenten konzipieren
page_order: 3
description: "Erfahren Sie, wie Sie Ihren Decisioning Studio Pro-Agenten mit dem Team von KI Serviceleistungen; Dienste entwerfen, einschließlich Definition der Zielgruppe, Erfolgsmetriken und Dimensionen."
---

# Agenten konzipieren

> Der erste Schritt bei der Einrichtung eines Agenten ist die Zusammenarbeit mit unserem Team von KI Decisioning Serviceleistungen; Dienste; Dienste, um Ihren Agenten zu entwerfen. Dieser Artikel behandelt die wichtigsten Design-Entscheidungen und wie Sie Ihre Zielgruppe definieren.

Grundlegende Konzepte zu Entscheidungsagenten - einschließlich Metriken für den Erfolg, Dimensionen, Aktionsbanken und Einschränkungen - finden Sie unter [Designing Decisioning Agents]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/designing_decisioning_agents/).

## Wichtige Designentscheidungen

In Zusammenarbeit mit dem Team der KI Decisioning Serviceleistungen; Dienste; Dienste treffen Sie die folgenden Entscheidungen:

| Entscheidung | Beschreibung | Beispiele |
|----------|-------------|----------|
| **Erfolgsmetrik** | Was wird der Agent maximieren, wenn er das Customer-Engagement personalisiert? | Umsatz, LTV, ARPU, Konversionen, Bindung |
| **Zielgruppe** | Für wen trifft der Decisioning Studio Agent Entscheidungen über das Customer-Engagement? | Alle Kunden, Treue-Mitglieder, Abonnent:innen mit Risiko |
| **Experiment Gruppen** | Wie sollten die randomisierten kontrollierten Studien von Decisioning Studio aufgebaut sein? | Decisioning Studio, Zufallssteuerung, BAU, Holdout |
| **Format** | Welche Entscheidungen sollte der Agent personalisieren? | Tageszeit, Betreffzeile, Häufigkeit, Angebote, Kanal |
| **Optionen** | Mit welchen Optionen kann der Agent arbeiten? | Spezielle Templates, Angebote, Zeitfenster |
| **Einschränkungen** | Welche Entscheidungen sollte der Agent *niemals* treffen? | Geografische Beschränkungen, Budgetgrenzen, Regeln für die Förderfähigkeit |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Jede dieser Entscheidungen hat Auswirkungen darauf, wie viel zusätzlichen Umsatz der Agent möglicherweise generieren kann, und wie schnell. Unser Team für KI Serviceleistungen; Dienste wird mit Ihnen zusammenarbeiten, um einen Agenten zu entwickeln, der einen maximalen Wert generiert und dabei alle Ihre Geschäftsregeln beachtet.

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_pro_agent_design.png %})

## Definieren Sie Ihre Zielgruppe

Zielgruppen für Anwendungsfälle werden in der Regel in einer Customer-Engagement-Plattform (wie Braze oder Salesforce Marketing Cloud) definiert und dann an den Decisioning Studio-Agenten gesendet. Der Agent teilt dann die Kund:in in Behandlungsgruppen ein, um randomisierte, kontrollierte Studien durchführen zu können.

### Behandlungsgruppen

| Gruppe | Beschreibung |
|-------|-------------|
| **Studio für Entscheidungsfindung** | Kunden, die KI-optimierte Empfehlungen erhalten |
| **Zufallssteuerung** | Kund:innen, die zufällig ausgewählte Optionen erhalten (Basislinienvergleich) |
| **Business-as-Usual (optional)** | Kunden, die die aktuelle Marketing-Journey erhalten (zum Vergleich mit der bestehenden Performance) |
| **Überbrückung (optional)** | Kund:innen, die keine Mitteilungen erhalten (um die Wirkung der Kampagne insgesamt zu messen) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Konfigurieren Sie Ihre Zielgruppe

{% tabs %}
{% tab Braze %}

**Konfigurieren Sie die Zielgruppe in Braze:**

1. Erstellen Sie ein Segment für Ihre Zielgruppe, die Sie targeting möchten.
2. Geben Sie die Segment ID an Ihr Team von KI Decisioning Serviceleistungen; Dienste; Dienste weiter.

{% alert note %}
Für Braze können wir mehrere Segmente einlesen und sie zur Erstellung der Zielgruppe kombinieren. Decisioning Studio kann ein Segment für eine Business-as-Usual-Vergleichskampagne aufnehmen. Alle diese Muster sind akzeptabel.
{% endalert %}

{% endtab %}
{% tab SFMC %}

**Konfigurieren Sie Zielgruppen in Salesforce Marketing Cloud:**

1. Konfigurieren Sie eine SFMC-Datenerweiterung(en) für Ihre Zielgruppe und geben Sie die ID der Datenerweiterung an
2. Richten Sie das installierte SFMC-Paket für die API-Integration mit den entsprechenden Berechtigungen ein, die von Decisioning Studio benötigt werden.
3. Stellen Sie sicher, dass diese Datenerweiterung täglich aktualisiert wird, da Decisioning Studio die neuesten verfügbaren inkrementellen Daten verwendet.

Stellen Sie dem Team der Braze Serviceleistungen die ID der Erweiterung und den API-Schlüssel zur Verfügung. Sie unterstützen Sie bei den nächsten Schritten zur Aufnahme von Kundendaten.

{% endtab %}
{% tab Klaviyo %}

**Definieren Sie die Zielgruppe in Klaviyo:**

1. Erstellen Sie ein Segment der Zielgruppe
2. Generieren Sie einen privaten API-Schlüssel und stellen Sie diesen dem Braze AI Decisioning Team zur Verfügung
3. Stellen Sie dem Team von Braze Serviceleistungen; Dienste die Segment ID und den API-Schlüssel zur Verfügung

In der [Dokumentation von Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) finden Sie weitere Informationen zu diesen Schritten.

{% endtab %}
{% tab Other Platforms %}

**Google-Cloudspeicher**

Wenn die Zielgruppe derzeit nicht in Braze, SFMC oder Klaviyo gespeichert ist, dann ist der nächste beste Schritt die Konfiguration eines automatisierten Exports direkt in einen von Braze kontrollierten Bucket der Google Cloud Serviceleistungen; Dienste.

Ob dies möglich ist, entnehmen Sie bitte der Dokumentation Ihrer MarTech Plattform. So bietet mParticle beispielsweise eine [native Integration mit Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/). In diesem Fall können wir Ihnen einen GCS Bucket zur Verfügung stellen, in den Sie die Daten der Zielgruppe exportieren können.

Es gibt ähnliche Seiten für:
- [Twilio Segmente](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

{% endtab %}
{% endtabs %}

## Profi-Fähigkeiten

Decisioning Studio Pro bietet die volle Leistungsfähigkeit der KI-Entscheidungsfindung:

| Fähigkeit | Details |
|------------|---------|
| **Jede Erfolgsmetrik** | Optimieren Sie für Umsatz, Konversionen, ARPU, LTV oder andere geschäftliche KPIs. |
| **Unbegrenzte Dimensionen** | Personalisieren Sie über Angebot, Kanal, Zeitpunkt, Häufigkeit, Kreativität und mehr |
| **Jede CEP** | Native Integrationen mit Braze, SFMC, Klaviyo + angepasste Integrationen für jede Plattform |
| **KI Decisioning Dienste** | Engagierte Unterstützung durch das Data Science Team von Braze |
| **Fortschrittliches Experimentdesign** | Vollständig anpassbare Behandlungsgruppen und Holdouts |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Bewährte Praktiken

Einige bewährte Verfahren für die Gestaltung von Decisioning Studio-Agenten:

1. **Maximieren Sie den Datenreichtum**: Je mehr Informationen die Agenten über Ihre Kund:innen haben, desto besser wird ihre Performance sein.
2. **Diversifizieren Sie Aktionen**: Je vielfältiger die Aktionen sind, die der Agent durchführen kann, desto mehr kann er seine Strategie für jeden Nutzer:innen personalisieren.
3. **Beschränkungen minimieren**: Je weniger Beschränkungen für Ihre Agenten, desto besser. Einschränkungen sollten so gestaltet sein, dass sie die Geschäftsregeln respektieren und gleichzeitig das Experimentieren durch Agenten so weit wie möglich zulassen.

## Nächste Schritte

Sobald die wichtigsten Designentscheidungen getroffen sind, können wir mit dem Start beginnen:

- [Starten Sie Ihren Agenten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/launch_your_agent/)