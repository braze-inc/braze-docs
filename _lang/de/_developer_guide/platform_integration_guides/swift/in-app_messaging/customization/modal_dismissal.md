---
nav_title: Ausblenden von Modalen
article_title: Modale Beendigung von In-App-Nachrichten für iOS
platform: Swift
page_order: 7
description: "Dieser Referenzartikel beschreibt das Ausblenden von modalen In-App-Nachrichten für das Swift SDK."
channel:
  - in-app messages
---

# Ausblenden von Modalen

> Um Ausblendungen durch Tippen außerhalb des Fensters zu aktivieren, können Sie die Eigenschaft `dismissOnBackgroundTap` in der Struktur `Attributes` des In-App-Nachrichtentyps ändern, den Sie anpassen möchten. 

Wenn Sie beispielsweise dieses Feature für modale In-App-Nachrichten mit Bildern aktivieren möchten, können Sie Folgendes konfigurieren:

{% tabs %}
{% tab schnell %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

Die Anpassung über `Attributes` ist in Objective-C nicht möglich.

{% endtab %}
{% endtabs %}

Der Standardwert ist `false`. Hierdurch wird festgelegt, ob die modale In-App-Nachricht ausgeblendet wird, wenn der Nutzer auf eine Stelle außerhalb der In-App-Nachricht tippt.

| `DismissModalOnOutsideTap` | Beschreibung |
|----------|-------------|
| `true`         | Modale In-App-Nachrichten werden ausgeblendet, wenn auf eine Stelle außerhalb des Fensters getippt wird.     |
| `false`        | Standardmäßig werden modale In-App-Nachrichten beim Tippen auf eine Stelle außerhalb des Fensters nicht ausgeblendet. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Einzelheiten zur Anpassung von In-App-Nachrichten finden Sie in diesem [Artikel](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).