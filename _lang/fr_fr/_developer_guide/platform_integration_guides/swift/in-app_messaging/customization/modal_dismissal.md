---
nav_title: Rejet modal
article_title: Rejet de message in-app modal pour iOS
platform: Swift
page_order: 7
description: "Cet article de référence explique le rejet de la messagerie in-app modale pour le SDK Swift."
channel:
  - in-app messages
---

# Rejet modal

> Pour activer les rejets par touché extérieur, vous pouvez modifier la propriété `dismissOnBackgroundTap` de la structure `Attributes` du type de message in-app que vous souhaitez personnaliser. 

Par exemple, si vous souhaitez activer cette fonctionnalité pour les messages in-app de type fenêtre modale, vous pouvez configurer ce qui suit :

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIF-C %}

La personnalisation via `Attributes` n'est pas disponible en Objective-C.

{% endtab %}
{% endtabs %}

La valeur par défaut est `false`. Cela détermine si le message in-app modal sera rejeté lorsque l’utilisateur touche à l’extérieur du message in-app.

| `DismissModalOnOutsideTap` | Description |
|----------|-------------|
| `true`         | Les messages in-app modaux seront rejetés par touche extérieure.     |
| `false`        | Par défaut, les messages in-app modaux ne seront rejetés par touche extérieure. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus de détails sur la personnalisation des messages in-app, consultez cet [article](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization).