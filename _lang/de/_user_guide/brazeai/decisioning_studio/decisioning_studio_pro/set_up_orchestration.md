---
nav_title: Orchestrierung einrichten
article_title: Orchestrierung einrichten
page_order: 2
description: "Erfahren Sie, wie Sie die Orchestrierung für Decisioning Studio Pro-Agenten konfigurieren, um personalisierte Kommunikation zu ermöglichen."
toc_headers: h2
---

# Orchestrierung einrichten

> Entscheidungsträger müssen sich mit einer Customer-Engagement-Plattform (CEP) verbinden, um die Orchestrierung der Kommunikation durchzuführen, sobald sie Kundendaten erfasst und auf einer 1:1-Ebene personalisiert haben. Dieser Artikel erläutert, wie Sie die Integration für jedes unterstützte CEP einrichten.

## Unterstützte CEPs

Decisioning Studio Pro unterstützt die folgenden Customer-Engagement-Plattformen:

| CEP | Art der Integration | Komplexität der Einrichtung |
|-----|-----------------|------------------|
| **Braze** | Native API-Integration | Niedrig (empfohlen) |
| **Salesforce Marketing Cloud** | Native API-Ereignisse + Journeys | Medium |
| **Klaviyo** | Native API-Ereignisse + Flows | Medium |
| **Andere CEPs** | Angepasst (Empfehlungsdatei) | Hoch |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Bitte wählen Sie unten Ihren CEP aus, um mit der Integration zu beginnen.

{% tabs %}
{% tab Braze %}

## Einrichtung der Braze-Integration

Bitte befolgen Sie die folgenden Schritte für die Integration eines Braze Decisioning Studio-Agenten in die Funktionen der Orchestrierung von Braze (das Serviceteam von Braze steht Ihnen dabei gerne zur Verfügung):

### Schritt 1: Einen API-Schlüssel erstellen

Bitte gehen Sie zu **„Einstellungen“** > **„API-Schlüssel“** und erstellen Sie einen neuen Schlüssel mit den folgenden Berechtigungen:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Schritt 2: API-gesteuerte Kampagnen einrichten

Richten Sie für jede Basisvorlage eine API-gesteuerte Kampagne mit API-Trigger-Eigenschaften für alle optimierten Dimensionen ein.

Eine Basisvorlage ist jedes Template, das der Entscheidungsagent zur Orchestrierung von Nachrichten verwenden kann. Ein Entscheidungsträger kann über eine oder mehrere Basis-Templates verfügen. In diesem Fall ist die Auswahl des geeigneten Templates für jeden Kund:in eine der Entscheidungen, die der Entscheidungsträger individuell personalisiert.

### Schritt 3: Wiederzulassung konfigurieren

Bitte stellen Sie sicher, dass alle API-gesteuerten Kampagnen es den Nutzer:innen ermöglichen, innerhalb von 15 Minuten wieder teilnahmeberechtigt zu werden.

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Obwohl der Decisioning Studio-Agent dieselbe Kampagne niemals mehr als einmal pro Tag versendet, ist es wünschenswert, dieselben Kampagnen zu Testzwecken mehrmals am Tag versenden zu können.
{% endalert %}

### Schritt 4: Dynamische Platzhalter hinzufügen

Diese dienen als dynamische Platzhalter für Entscheidungen, die der Decisioning Studio-Agent optimiert.

#### Beispiel 1: E-Mail-Kampagne

Angenommen, der Decisioning Studio-Agent optimiert eine E-Mail-Kampagne. Dies könnte wie folgt konfiguriert werden:

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Angenommen, der Agent optimiert die Auswahl der Templates und die Call-to-Action-Nachricht (CTA), dann sollte für jedes Template eine API-gesteuerte Kampagne erstellt werden, und der CTA-Abschnitt eines Templates könnte wie folgt aussehen:

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Beispiel 2: Push-Kampagne

Angenommen, ein Decisioning Studio-Agent optimiert die Nachricht einer Push-Kampagne. Dies könnte wie folgt konfiguriert werden:

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Dies führt zu folgender Nachricht:

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Beispiel 3: SMS-Kampagne

Angenommen, der Decisioning Studio-Agent optimiert die Felder in einer SMS-Kampagne. Dies könnte wie folgt konfiguriert werden:

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Dies führt zu folgender Nachricht:

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Einrichtung der SFMC-Integration

Decisioning Studio Pro unterstützt die native Integration mit Salesforce Marketing Cloud. Das Decisioning Studio triggert API-Ereignisse in einer Journey, wobei die erforderlichen Daten zum Ausfüllen dynamischer Elemente bereitgestellt werden.

Die Orchestrierungskonfiguration für SFMC ist für Decisioning Studio Pro und Decisioning Studio Go identisch. Detaillierte Schritte zur Konfiguration der SFMC-Integration finden Sie in den [SFMC-Anweisungen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) in der Dokumentation zu Decisioning Studio Go.

{% endtab %}
{% tab Klaviyo %}

## Einrichtung der Klaviyo-Integration

Decisioning Studio Pro unterstützt die native Integration mit Klaviyo. Das Decisioning Studio triggert API-Ereignisse in einem Ablauf, wobei die erforderlichen Daten zum Ausfüllen dynamischer Elemente bereitgestellt werden.

Die Orchestrierungskonfiguration für Klaviyo ist sowohl für Decisioning Studio Pro als auch für Decisioning Studio Go ähnlich. Detaillierte Schritte zur Konfiguration der Klaviyo-Integration finden Sie in den [Klaviyo-Anweisungen]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) in der Dokumentation zu Decisioning Studio Go.

{% endtab %}
{% tab Other CEPs %}

## Einrichtung weiterer CEP-Integrationen

Decisioning Studio kann mit jeder Customer-Engagement-Plattform integriert werden. Dies kann jedoch einige individuelle technische Anpassungen durch Ihr Team erfordern, da Decisioning Studio die Kommunikation nicht direkt triggern kann.

In diesem Fall wird der Agent eine „Empfehlungsdatei“ zugestellt. Diese Datei enthält Zeilen für jeden Kunden mit Spalten, die alle personalisierten Entscheidungen für diesen Kunden anzeigen.

Beispielsweise die folgende Empfehlungsdatei:

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Kann zur Optimierung einer E-Mail-Kampagne verwendet werden, die wie folgt aussieht:

![Entscheidungsdiagramm]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Nächste Schritte

Nachdem Sie die Orchestrierung eingerichtet haben, fahren Sie mit der Gestaltung Ihres Agenten fort:

- [Agenten konzipieren]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

