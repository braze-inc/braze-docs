---
nav_title: Indicadores no leídos y leídos
article_title: Indicadores de tarjetas de contenido leídas y no leídas para iOS
platform: iOS
page_order: 4
description: "Este artículo de referencia cubre los indicadores no leídos y leídos de iOS y cómo implementarlos en tus tarjetas de contenido."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Indicadores no leídos y no leídos

## Desactivar el indicador de no visto

![Dos tarjetas de contenido expuestas una al lado de la otra. La tarjeta de la izquierda tiene una línea azul en la parte inferior, lo que indica que no ha sido vista. La tarjeta de la derecha no tiene una línea azul, lo que indica que ya ha sido vista.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: style="max-width:80%"}

Puedes elegir desactivar la línea azul en la parte inferior de la tarjeta, que indica si la tarjeta ha sido vista o no, configurando la propiedad `disableUnviewedIndicator` en `ABKContentCardsTableViewController` a `YES`.

## Personalizar el indicador de no visto

Se puede acceder al indicador no visto a través de la propiedad `unviewedLineView` de la clase `ABKBaseContentCardCell`. Si utilizas implementaciones de `UITableViewCell`, debes acceder a la propiedad antes de que se dibuje la celda.

Por ejemplo, para establecer el color del indicador de no visto en rojo:

{% tabs %}
{% tab OBJETIVO-C %}

```objc
((ABKBaseContentCardCell *)cell).unviewedLineView.backgroundColor = [UIColor redColor];
```

{% endtab %}
{% tab swift %}

```swift
(card as? ABKBaseContentCardCell).unviewedLineView.backgroundColor = UIColor.red
```

{% endtab %}
{% endtabs %}
