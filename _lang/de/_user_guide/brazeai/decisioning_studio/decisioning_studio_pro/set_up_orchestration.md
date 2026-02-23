---
nav_title: Orchestrierung einrichten
article_title: Orchestrierung einrichten
page_order: 2
description: "Erfahren Sie, wie Sie die Orchestrierung für Decisioning Studio Pro-Agenten konfigurieren, um personalisierte Kommunikation zu ermöglichen."
toc_headers: h2
---

# Orchestrierung einrichten

> Entscheidungsagenten müssen sich mit einer Customer-Engagement-Plattform (CEP) verbinden, um die Kommunikation zu orchestrieren, sobald sie Kundendaten aufgenommen und auf 1:1-Ebene personalisiert haben. Dieser Artikel erklärt, wie Sie die Integration für jeden unterstützten CEP einrichten.

## Unterstützte CEPs

Decisioning Studio Pro unterstützt die folgenden Customer-Engagement-Plattformen:

| CEP | Art der Integration | Komplexität der Einrichtung |
|-----|-----------------|------------------|
| **Braze** | Native API-Integration | Niedrig (empfohlen) |
| **Salesforce Marketing Cloud** | Native API-Ereignisse + Journeys | Medium |
| **Klaviyo** | Native API Ereignisse + Flows | Medium |
| **Andere CEPs** | Angepasst (Empfehlungsdatei) | Hoch |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Wählen Sie unten Ihren CEP aus, um mit der Einrichtung der Integration zu beginnen.

{% tabs %}
{% tab Braze %}

## Einrichten der Braze-Integration

Führen Sie die folgenden Schritte aus, um einen Braze Decisioning Studio-Agenten in die Orchestrierung von Braze zu integrieren (das Team für Serviceleistungen; Dienste von Braze steht Ihnen dabei zur Seite):

### Schritt 1: Einen API-Schlüssel erstellen

Gehen Sie zu **Einstellungen** > **API-Schlüssel**, und erstellen Sie einen neuen Schlüssel mit den folgenden Berechtigungen:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Schritt 2: Richten Sie API-getriggerte Kampagnen ein

Richten Sie eine API-getriggerte Kampagne für jedes Basis Template mit API-Trigger-Eigenschaften für alle optimierten Dimensionen ein.

Eine Basisvorlage ist eine beliebige Vorlage, die der Decisioning Agent für die Orchestrierung von Nachrichten verwenden kann. Ein Decisioning Agent kann über 1 oder mehrere Basis-Templates verfügen. In diesem Fall ist die Auswahl des richtigen Basis-Templates für jeden Kunden eine der Entscheidungen, die der Agent personalisiert.

### Schritt 3: Konfigurieren Sie die Wiederzulassung

Stellen Sie sicher, dass alle API-getriggerten Kampagnen es Nutzern:innen erlauben, sich innerhalb von 15 Minuten wieder zu qualifizieren.

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Obwohl der Decisioning Studio-Agent dieselbe Kampagne nie mehr als einmal pro Tag versendet, möchten Sie die Möglichkeit haben, dieselben Kampagnen zu Testzwecken mehrmals am Tag zu versenden.
{% endalert %}

### Schritt 4: Dynamische Platzhalter hinzufügen

Diese dienen als dynamische Platzhalter für Entscheidungen, die der Decisioning Studio-Agent optimiert.

#### Beispiel 1: E-Mail-Kampagne

Angenommen, der Decisioning Studio-Agent optimiert eine E-Mail Kampagne. Dies könnte wie folgt konfiguriert werden:

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Angenommen, der Agent optimiert die Auswahl der Templates und der Call to Action (CTA)-Nachricht, dann sollte für jedes Template eine API-getriggerte Kampagne erstellt werden, und der CTA-Abschnitt eines Templates könnte wie folgt aussehen:

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Beispiel 2: Push-Kampagne

Angenommen, ein Decisioning Studio-Agent optimiert die Nachricht einer Push-Kampagne. Dies könnte wie folgt konfiguriert werden:

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Das Ergebnis ist die folgende Nachricht:

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Beispiel 3: SMS-Kampagne

Nehmen wir an, der Decisioning Studio-Agent optimiert die Felder einer SMS-Kampagne. Dies könnte wie folgt konfiguriert werden:

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Das Ergebnis ist die folgende Nachricht:

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Einrichten der SFMC-Integration

Decisioning Studio Pro unterstützt die native Integration mit Salesforce Marketing Cloud. Decisioning Studio triggert API-Ereignisse in einer Reise mit Daten, die zum Auffüllen dynamischer Elemente erforderlich sind.

Die Einrichtung der Orchestrierung für SFMC ist sowohl für Decisioning Studio Pro als auch für Decisioning Studio Go ähnlich. Detaillierte Schritte zur Konfiguration der SFMC-Integration finden Sie in den [SFMC-Anweisungen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) in der Dokumentation zu Decisioning Studio Go.

{% endtab %}
{% tab Klaviyo %}

## Einrichten der Klaviyo Integration

Decisioning Studio Pro unterstützt die native Integration mit Klaviyo. Decisioning Studio triggert API-Ereignisse in einem Fluss mit Daten, die zum Auffüllen dynamischer Elemente erforderlich sind.

Die Orchestrierung von Klaviyo ist sowohl für Decisioning Studio Pro als auch für Decisioning Studio Go ähnlich aufgebaut. Detaillierte Schritte zur Konfiguration der Klaviyo Integration finden Sie in den [Klaviyo Anweisungen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) in der Dokumentation zu Decisioning Studio Go.

{% endtab %}
{% tab Other CEPs %}

## Andere CEP-Integrationen einrichten

Decisioning Studio kann mit jeder Customer-Engagement-Plattform integriert werden. Dies kann jedoch einige angepasste Entwicklungsarbeit von Ihrem Team erfordern, da Decisioning Studio die Kommunikation nicht direkt triggern kann.

In diesem Szenario liefert der Agent eine "Empfehlungsdatei" zu. Diese Datei enthält Zeilen für jede Kund:in, mit Spalten, die alle personalisierten Entscheidungen für diese Kund:in angeben.

Zum Beispiel die folgende Empfehlungsdatei:

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Könnte zur Optimierung einer E-Mail Kampagne verwendet werden, die wie die folgende aussieht:

![Diagramm zur Entscheidungsfindung]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Nächste Schritte

Nachdem Sie die Orchestrierung eingerichtet haben, fahren Sie mit der Gestaltung Ihres Agenten fort:

- [Agenten konzipieren]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

