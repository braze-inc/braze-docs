---
nav_title: Shopify Standard-Integration mit Tagging von Drittanbietern
article_title: "Shopify Standard-Integration mit Tagging von Drittanbietern"
description: "Dieser referenzierte Artikel beschreibt, wie Sie die standardmäßige Shopify Integration mit einem Tagging-Tool eines Drittanbieters einrichten."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration_third_party_tagging/
page_order: 2
---

# Shopify Standard-Integration mit Tagging-Tool von Drittanbietern

> Diese Seite führt Sie durch die Verwendung von Tools von Drittanbietern, wie Google Tag Manager, mit der [Shopify-Standardintegration]({{site.baseurl}}/shopify_standard_integration/), um das Braze Web SDK zu initialisieren und zu laden.

Für Shopify Online-Shops empfehlen wir die Verwendung der Standard-Integrationsmethode von Braze, um die Braze SDKs auf Ihrer Website zu unterstützen. Wir verstehen jedoch, dass Sie vielleicht lieber ein Drittanbieter-Tool wie Google Tag Manager:in verwenden möchten. Wenn Sie sich dafür entscheiden, ein Tool eines Drittanbieters mit dem Shopify Konnektor von Braze zu verwenden, denken Sie daran, dass die Braze Integration und die App embed das SDK während des Bestellvorgangs verwalten werden.

## Anforderungen

- **Konsistenter API-Schlüssel zwischen Ihrem Drittanbieter-Tool und dem Shopify Konnektor:** Der API-Schlüssel muss sowohl in Braze als auch in Ihrem Drittanbieter-Tool konsistent sein. Dadurch wird die Erstellung doppelter Nutzer:innen verhindert und die Kompatibilität zwischen verschiedenen SDKs aufrechterhalten. 
  - **API-Schlüssel-Standort:** Nach dem Onboarding über den Standardintegrationspfad erstellt die Integration automatisch eine Braze Web App mit dem Namen "Shopify". Rufen Sie den API-Schlüssel innerhalb der Integration ab, der mit der Konfiguration Ihres Drittanbieter-Tools verwendet wird. 
- **Konsistente SDK-Versionen zwischen Ihrem Drittanbieter-Tool und dem Shopify Konnektor:** Die SDK-Version muss in Ihrem Drittanbieter-Tool `5.4` sein. Die Verwendung einer falschen Versionsnummer kann zu Inkompatibilitätsproblemen führen, da einige SDK-Methoden in älteren Versionen möglicherweise nicht vorhanden sind.
- **Konsistentes SDK-Initialisierungs-Timing:** In Ihren Shopify Standardeinstellungen für die Integration können Sie die SDKs auswählen, die entweder beim Start der Sitzung oder bei der Anmeldung eines Kontos initialisiert werden sollen. Diese Einstellung sollte zwischen Ihrem Drittanbieter-Tool und Braze konsistent sein. Inkonsistenzen könnten zu nachgelagerten Problemen für die Nutzer:innen und die Synchronisierung der Daten führen. 

{% alert note %}
Wir empfehlen die ausschließliche Verwendung der Standard-Integrationsmethode und nicht die Verwendung in Verbindung mit Tag-Managern von Drittanbietern, da dies zu Konflikten zwischen dem Braze SDK und Tools von Drittanbietern führen kann. Wenn Sie ein Tool eines Drittanbieters verwenden, testen Sie, ob alles wie erwartet funktioniert.
{% endalert %}

## Einrichten der Integration mit einem Drittanbieter-Tool

Wenn Sie von den angegebenen Schritten abweichen, kann dies zu unerwarteten Problemen führen, halten Sie sich also genau an die Anweisungen.

1. Befolgen Sie die vorgegebenen Schritte zur [Einrichtung der Shopify Standard-Integration]({{site.baseurl}}/shopify_standard_integration/). Markieren Sie beim [Enablement von Braze Web SDKs]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-2-enable-braze-web-sdks) das Kästchen, das angibt, dass Sie ein Tool eines Drittanbieters verwenden, um das Braze Web SDK zu Ihrer Shopify-Website hinzuzufügen.

!["Braze SDK-Einstellungen" mit einem Kontrollkästchen, um anzugeben, dass Sie ein Tool eines Drittanbieters verwenden werden, um das Braze Web SDK hinzuzufügen.]({% image_buster /assets/img/Shopify/third_party_enable.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Gehen Sie zu **Einstellungen** > **App-Einstellungen**, wählen Sie die **Shopify** Web-App aus und kopieren Sie dann den **API-Schlüssel für Shopify im Internet**.
3\. Fügen Sie den API-Schlüssel in die Web-SDK-Konfiguration Ihres Drittanbieter-Tools ein und setzen Sie die SDK-Version auf `5.4`.

## Erfassen von Shopify Daten und Synchronisieren von Nutzer:innen

Solange das Internet SDK im Frontend Ihrer Shopify-Website über ein Tool eines Drittanbieters zugänglich ist, wird die Standard-Integration die Shopify-Daten erfassen und die Nutzer:innen wie erwartet synchronisieren.

## Überlegungen und Haftungsausschlüsse

- **Initialisierungseinstellungen:** Wenn Sie Ihre Initialisierungseinstellungen über Ihr Drittanbieter-Tool ändern, kann die Synchronisierung von Nutzer:in und Daten beeinträchtigt werden. Wenn Sie sich zum Beispiel dafür entscheiden, Ihr SDK zu initialisieren, wenn ein Cookie-Zustimmungsformular akzeptiert wird, erhält Braze kein Tracking für anonyme Nutzer:innen oder Daten, bis der Nutzer zustimmt. 
- **Das direkte Setzen von Attributen über `dataLayer` wird nicht unterstützt:** Verwenden Sie `window.braze` anstelle von `dataLayer`, um Attribute festzulegen.
- **Potenzielle doppelte Nutzer:innen:** Wenn der API-Schlüssel in Braze und Ihrem Drittanbieter-Tool nicht übereinstimmt, werden möglicherweise doppelte Nutzer:innen erstellt.
- **SDK-Inkompatibilität:** Die Verwendung einer falschen Versionsnummer kann zu Problemen mit SDK-Methoden führen.