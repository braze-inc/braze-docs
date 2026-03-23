---
nav_title: Indicadores de lido e não lido
article_title: Indicadores de lido e não lido do cartão de conteúdo para iOS
platform: iOS
page_order: 4
description: "Este artigo de referência cobre os indicadores de lido e não lido do iOS e como implementá-los nos seus Cartões de conteúdo."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Indicadores de lido e não lido

## Desativando o indicador de não visualizado

![Dois cartões de conteúdo exibidos lado a lado. O cartão à esquerda tem uma linha azul na parte inferior, indicando que não foi visto. O cartão à direita não tem uma linha azul, indicando que já foi visto.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: style="max-width:80%"}

Você pode optar por desativar a linha azul na parte inferior do cartão, que indica se o cartão foi visualizado ou não, configurando a propriedade `disableUnviewedIndicator` em `ABKContentCardsTableViewController` para `YES`.

## Personalizando o indicador de não visualizado

O indicador de não visualizado pode ser acessado através da propriedade `unviewedLineView` da classe `ABKBaseContentCardCell`. Se você usar implementações de `UITableViewCell`, acesse a propriedade antes que a célula seja desenhada.

Por exemplo, para definir a cor do indicador de não visualizado como vermelho:

{% tabs %}
{% tab OBJECTIVE-C %}

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