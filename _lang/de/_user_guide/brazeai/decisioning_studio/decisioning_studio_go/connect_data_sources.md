---
nav_title: Datenquellen verbinden
article_title: Datenquellen verbinden
page_order: 1
description: "Erfahren Sie, wie BrazeAI Decisioning Studio Go über Ihre Customer-Engagement-Plattform eine Verbindung zu Ihren Kundendaten herstellt."
---

# Datenquellen verbinden

> BrazeAI Decisioning Studio™ Go verbindet sich mit Ihren Kundendaten über Ihre Customer-Engagement-Plattform (CEP). Dieser Artikel erklärt, welche Daten verwendet werden und wie die Verbindung funktioniert.

## Wie Go auf Kundendaten zugreift

Im Gegensatz zu Decisioning Studio Pro, das direkte Datenintegrationen mit verschiedenen Quellen unterstützt, greift Decisioning Studio Go über Ihr CEP auf Kundendaten zu. Dies bedeutet:

- **Daten zur Zielgruppe** werden direkt aus Segmenten oder Listen gezogen, die in Ihrem CEP (Braze oder Salesforce Marketing Cloud) definiert sind, und können nur bestimmte vordefinierte Attribute enthalten (keine 1P-Daten).
- **Daten zum Engagement** (Öffnungen, Klicks, Sendungen) werden durch automatisierte Abfragen oder native Integrationen mit Ihrem CEP erfasst.
- **Es ist keine zusätzliche Einrichtung der Daten-Pipeline** erforderlich, die über das hinausgeht, was Sie in Ihrem CEP konfigurieren.

## Unterstützte Integrationsmuster

Decisioning Studio Go unterstützt die folgenden CEPs für den Zugriff auf Daten:

| CEP | Zielgruppe Quelle | Engagement-Daten |
|-----|-----------------|-----------------|
| **Braze** | Segmente | Braze-Currents exportieren |
| **Salesforce Marketing Cloud** | Daten Erweiterungen | SQL-Abfrage-Automatisierung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Datenanforderungen der CEP

{% tabs %}
{% tab Braze %}

### Braze Daten Anforderungen

Für die Integration von Braze ist Decisioning Studio Go erforderlich:

1. **Braze Currents**: Sie müssen Braze-Currents aktiviert und konfiguriert haben, um Daten über das Engagement in Decisioning Studio Go zu exportieren. Dies erlaubt es dem Agenten, aus den Antworten der Kund:in zu lernen.

2. **Segmentieren Sie den Zugang**: Der API-Schlüssel, den Sie erstellen, muss die Berechtigung haben, auf Segmente zuzugreifen, die Ihre Zielgruppe definieren.

3. **Nutzerprofil-Daten**: Alle Attribute des Nutzerprofils oder angepasste Attribute, die der Agent berücksichtigen soll, müssen über die Braze API zugänglich sein.

{% alert important %}
Stellen Sie sicher, dass Ihr Braze-Currents-Export die Daten aller Kampagnen enthält, mit denen Sie vergleichen möchten (einschließlich BAU-Kampagnen).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### SFMC Daten Anforderungen

Für Salesforce Marketing Cloud Integrationen benötigt Decisioning Studio Go:

1. **Daten-Erweiterungen**: Ihre Zielgruppe muss in einer Datenerweiterung definiert sein, auf die Decisioning Studio Go zugreifen kann. Verwenden Sie den SubscriberKey als primären Bezeichner für Nutzer:innen.
2. **Tracking Events Zugriff**: Solange das installierte App-Paket die automatisierte End-to-End-Einrichtung unterstützt, ist keine zusätzliche Konfiguration erforderlich. 

Die Datenerweiterungen und SQL-Anfragen werden im Rahmen der [Orchestrierung]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) konfiguriert.

{% endtab %}
{% endtabs %}

## Bewährte Praktiken

- **Halten Sie die Daten frisch**: Stellen Sie sicher, dass Ihre Segmente und Kundendaten regelmäßig aktualisiert werden (mindestens täglich), damit der Agent mit aktuellen Informationen arbeitet.
- **Fügen Sie relevante Attribute hinzu**: Überlegen Sie, welche Kundenmerkmale Einfluss darauf haben könnten, welche Nachrichten ankommen - Demografie, Verlauf des Engagements, Kaufverhalten und Lebenszyklusphase sind allesamt wertvolle Signale.

## Nächste Schritte

Da Sie nun wissen, wie Go eine Verbindung zu Daten herstellt, können Sie Ihre CEP-Integration einrichten:

- [Orchestrierung einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

