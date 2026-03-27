---
nav_title: Angepasster Code und JavaScript-Brücke
article_title: Angepasster Code und JavaScript-Brücke für Banner
page_order: 2
page_type: reference
description: "Erfahren Sie, wie Sie angepasstes HTML in Bannern und die JavaScript-Brücke verwenden können, um Klicks zu protokollieren und Braze-Aktionen zu triggern."
channel:
  - banners
---

# Angepasster Code und JavaScript-Brücke für Banner

> Wenn Sie den Editor-Block **„Benutzerdefinierter Code**-Editor“ im Banner-Composer verwenden, müssen Sie innerhalb Ihres angepassten HTML-Codes aufrufen`brazeBridge.logClick()`, um Klicks zu protokollieren. Banner verwenden dieselbe JavaScript-Brücke wie HTML-In-App-Nachrichten, daher gelten dieselben Methoden und Muster.

Wenn Sie in Ihrem Banner-Design angepasstes HTML verwenden, kann das Braze SDK nicht automatisch Klick-Listener an Elemente innerhalb Ihres angepassten Codes anhängen. Sie müssen alle anklickbaren Elemente (Links, Buttons und Ähnliches), die Sie im Analytics-Tool der Kampagne verfolgen möchten, explizit aufrufen`brazeBridge.logClick()`.

Um beispielsweise einen Klick zu protokollieren, wenn eine Nutzer:in in Ihrem angepassten HTML auf einen Button tippt:

```html
<button onclick="brazeBridge.logClick()">
  Click me
</button>
```

Die vollständige JavaScript-Bridge-Referenz, einschließlich aller verfügbaren Methoden und Optionen für Klick-Tracking, finden Sie im folgenden Abschnitt.

## JavaScript-Brücke {#javascript-bridge}

{% include javascript_bridge/reference.md %}
