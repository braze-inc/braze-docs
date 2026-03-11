---
nav_title: Datenquellen verbinden
article_title: Datenquellen verbinden
page_order: 1
description: "Erfahren Sie, wie BrazeAI Decisioning Studio Go über Ihre Customer-Engagement-Plattform eine Verbindung zu Ihren Kundendaten herstellt."
---

# Datenquellen verbinden

> BrazeAI Decisioning Studio™ Go stellt über Ihre Customer-Engagement-Plattform (CEP) eine Verbindung zu Ihren Kundendaten her. Dieser Artikel erläutert, welche Daten verwendet werden und wie die Verbindung funktioniert.

## Wie Go auf Kundendaten zugreift

Im Gegensatz zu Decisioning Studio Pro, das die direkte Datenintegration mit verschiedenen Quellen unterstützt, greift Decisioning Studio Go über Ihr CEP auf Kundendaten zu. Dies bedeutet:

- **Die Daten der Zielgruppen** werden direkt aus den in Ihrem CEP (Braze, Salesforce Marketing Cloud oder Klaviyo) definierten Segmenten oder Listen abgerufen und können nur bestimmte vordefinierte Attribute enthalten (keine 1P-Daten).
- **Engagement-Daten** (Öffnungen, Klicks, Sendungen) werden durch automatisierte Abfragen oder native Integrationen mit Ihrem CEP erfasst.
- Es ist **keine zusätzliche Einrichtung der Datenpipeline** erforderlich, die über die Konfiguration in Ihrem CEP hinausgeht.

## Unterstützte Muster für die Integration

Decisioning Studio Go unterstützt die folgenden CEPs für den Zugriff auf Daten:

| CEP | Quelle der Zielgruppen | Engagement-Daten |
|-----|-----------------|-----------------|
| **Braze** | Segmente | Braze-Currents exportieren |
| **Salesforce Marketing Cloud** | Datenerweiterungen | Automatisierung von SQL-Anfragen |
| **Klaviyo** | Segmente | Native API-Integration |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Datenanforderungen von CEP

{% tabs %}
{% tab Braze %}

### Anforderungen an Braze-Daten

Für Braze-Integrationen erfordert Decisioning Studio Go Folgendes:

1. **Braze-Currents**: Bitte beachten Sie, dass Braze-Currents aktiviert und konfiguriert sein muss, um Engagement-Daten in Decisioning Studio Go exportieren zu können. Dadurch kann der Mitarbeiter aus den Antworten der Kund:innen lernen.

2. **Segmentzugang**: Der von Ihnen erstellte API-Schlüssel muss über Berechtigungen für den Zugriff auf Segmente verfügen, die Ihre Zielgruppe definieren.

3. **Nutzerprofil-Daten**: Alle Nutzerprofil-Attribute oder angepassten Attribute, die der Agent berücksichtigen soll, müssen über die Braze-API zugänglich sein.

{% alert important %}
Bitte stellen Sie sicher, dass Ihr Braze-Currents-Export Daten aus allen Kampagnen enthält, die Sie vergleichen möchten (einschließlich BAU-Kampagnen).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### SFMC-Datenanforderungen

Für Salesforce Marketing Cloud-Integrationen erfordert Decisioning Studio Go Folgendes:

1. **Datenerweiterungen**: Ihre Zielgruppen müssen in einer Datenerweiterung definiert sein, auf die Decisioning Studio Go zugreifen kann. Verwenden Sie den SubscriberKey als primären Bezeichner für Nutzer:innen.
2. **Zugriff auf Tracking-Ereignisse**: Solange das installierte App-Paket eine End-to-End-Automatisierung der Einrichtung unterstützt, ist keine zusätzliche Konfiguration erforderlich. 

Die Daten-Erweiterungen und SQL-Anfragen werden im Rahmen der [Orchestrierungskonfiguration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) eingerichtet.

{% endtab %}
{% tab Klaviyo %}

### Klaviyo-Datenanforderungen

Für Klaviyo-Integrationen erfordert Decisioning Studio Go Folgendes:

1. **Segmentzugang**: Ihre Zielgruppe muss als Klaviyo-Segment definiert sein, auf das der API-Schlüssel zugreifen kann.
2. **Profildaten**: Der API-Schlüssel muss über Vollzugriff auf Profile verfügen, um Kundenattribute lesen zu können.
3. **Zugriff auf Metriken**: Der API-Schlüssel muss über Vollzugriff auf Metriken und Ereignisse verfügen, um Daten zum Engagement erfassen zu können.

{% endtab %}
{% endtabs %}

## Bewährte Praktiken

- **Daten auf dem neuesten Stand halten**: Bitte stellen Sie sicher, dass Ihre Zielgruppensegmente und Kundendaten regelmäßig (mindestens einmal täglich) aktualisiert werden, damit der Agent mit aktuellen Informationen arbeitet.
- **Bitte relevante Attribute angeben**: Überlegen Sie, welche Kundenmerkmale Einfluss darauf haben könnten, welche Nachrichten Anklang finden – demografische Daten, Engagement-Historie, Kaufverhalten und Lebenszyklusphase sind allesamt wertvolle Indikatoren.

## Nächste Schritte

Nachdem Sie nun verstanden haben, wie Go eine Verbindung zu Daten herstellt, fahren Sie mit der Einrichtung Ihrer CEP-Integration fort:

- [Orchestrierung einrichten]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

