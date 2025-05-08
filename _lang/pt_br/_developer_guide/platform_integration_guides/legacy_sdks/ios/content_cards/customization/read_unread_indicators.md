---
nav_title: Indicadores de Leitura e Não Lida
article_title: Indicadores de Leitura e Não Lida do cartão de conteúdo para iOS
platform: iOS
page_order: 4
description: "Este artigo de referência cobre os indicadores de leitura e não leitura do iOS e como implementá-los em seus Cartões de Conteúdo."
channel:
  - content cards

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Indicadores de leitura e não lidos

## Desativando o indicador não visualizado

![Dois cartões de conteúdo exibidos lado a lado. O cartão à esquerda tem uma linha azul na parte inferior, indicando que não foi visto. O cartão à direita não tem uma linha azul, indicando que já foi visto.]({% image_buster /assets/img/braze-content-cards-seen-unseen-behavior.png %}){: style="max-width:80%"}

Você pode optar por desativar a linha azul na parte inferior do cartão, que indica se o cartão foi visualizado ou não, configurando a propriedade `disableUnviewedIndicator` em `ABKContentCardsTableViewController` para `YES`.

## Personalizando o indicador não visualizado

O indicador não visualizado pode ser acessado através da propriedade `unviewedLineView` da classe `ABKBaseContentCardCell`. Se você usar implementações de `UITableViewCell`, acesse a propriedade antes que a célula seja desenhada.

Por exemplo, para definir a cor do indicador não visualizado para vermelho:

{% tabs %}
{% tab OBJECTIVE C %}

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
