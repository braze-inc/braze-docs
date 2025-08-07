---
nav_title: Comportamento
article_title: Personalização do comportamento dos cartões de conteúdo
page_order: 2
description: "Este guia de implementação aborda a alteração do comportamento dos cartões de conteúdo, a adição de extras como pares de chave/valor à sua carga útil e receitas de personalizações comuns."
channel:
  - content cards
platform:
  - Android
  - FireOS
  - Swift
  - Web
---

# Personalização do comportamento dos cartões de conteúdo

> Este guia de implementação aborda a alteração do comportamento dos cartões de conteúdo, a adição de extras como pares de chave/valor à sua carga útil e receitas de personalizações comuns. Para obter a lista completa dos tipos de cartões de conteúdo, consulte [Sobre cartões de conteúdo]({{site.baseurl}}/developer_guide/content_cards/). 

## Pares de valores chave

O Braze o capacita a enviar cargas úteis de dados extras por meio de cartões de conteúdo para dispositivos de usuários usando pares de valores-chave. Eles podem ajudá-lo a rastrear métricas internas, atualizar o conteúdo do app e personalizar propriedades. [Adicione pares de valores-chave usando o dashboard]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create#step-4-configure-additional-settings-optional). 
 
{% alert note %}
Não recomendamos o envio de valores JSON aninhados como pares de valores-chave. Em vez disso, achate o JSON antes de enviá-lo.
{% endalert %}

{% tabs %}
{% tab Android %}

Os pares de valores-chave são armazenados em objetos <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/#-2118252107%2FProperties%2F-1725759721" target="_blank">`card`</a> como `extras`. Eles podem ser usados para enviar dados para baixo junto com um cartão para tratamento posterior pelo aplicativo. Chamada <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.cards/-card/extras.html" target="_blank">`card.extras`</a> para acessar esses valores.

{% endtab %}
{% tab swift %}

Os pares de valores-chave são armazenados em objetos <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard" target="_blank">`card`</a> como `extras`. Eles podem ser usados para enviar dados para baixo junto com um cartão para tratamento posterior pelo aplicativo. Chamada <a href="https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcard/data-swift.struct/extras" target="_blank">`card.extras`</a> para acessar esses valores.

{% endtab %}
{% tab web %}

Os pares de valores-chave são armazenados em objetos <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html" target="_blank">`card`</a> como `extras`. Eles podem ser usados para enviar dados para baixo junto com um cartão para tratamento posterior pelo aplicativo. Ligue para `card.extras` para acessar esses valores.

{% endtab %}
{% endtabs %}

{% alert tip %}
É importante que suas equipes de marketing e de desenvolvimento coordenem quais pares de valores-chave serão usados (por exemplo, `feed_type = brand_homepage`), pois todos os pares de valores-chave que os profissionais de marketing inserirem no dashboard do Braze devem corresponder exatamente aos pares de valores-chave que os desenvolvedores criam na lógica do app.
{% endalert %}

## Cartões de conteúdo como conteúdo suplementar

![]({% image_buster /assets/img/cc_implementation/supplementary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0;"}

Você pode combinar perfeitamente os cartões de conteúdo em um feed existente, permitindo que os dados de vários feeds sejam carregados simultaneamente. Isso cria uma experiência coesa e harmoniosa com os cartões de conteúdo Braze e o conteúdo de feed existente.

O exemplo à direita mostra um feed com uma lista híbrida de itens que são preenchidos por meio de dados de localização e cartões de conteúdo fornecidos pelo Braze. Com isso, talvez não seja possível distinguir os cartões de conteúdo mesclados ao conteúdo existente.

### Pares de valores-chave disparados pela API

As [campanhas disparadas por API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) são uma boa estratégia a ser empregada quando os valores de um cartão dependem de fatores externos para determinar o conteúdo a ser exibido para o usuário. Por exemplo, para exibir conteúdo suplementar, defina pares de valores-chave usando o Liquid. É preciso saber qual é o `class_type` no momento da configuração.

![Os pares de valores-chave para o caso de uso de cartões de conteúdo suplementar. Neste exemplo, diferentes aspectos do cartão, como "tile_id", "tile_deeplink" e "tile_title", são definidos usando o Liquid.]({% image_buster /assets/img/cc_implementation/supplementary_content.png %}){: style="max-width:60%;"}

## Cartões de conteúdo como conteúdo interativo
![Um cartão de conteúdo interativo mostrando uma promoção de 50% aparece no canto inferior esquerdo da tela. Após ser clicado, uma promoção será aplicada ao carrinho.]({% image_buster /assets/img/cc_implementation/discount2.png %}){: style="border:0;"}{: style="float:right;max-width:45%;border:0;margin-left:15px;"} 

Os cartões de conteúdo podem ser aproveitados para criar experiências dinâmicas e interativas para seus usuários. No exemplo à direita, temos um pop-up de cartão de conteúdo que aparece no checkout, oferecendo aos usuários promoções de última hora. Cartões bem posicionados como esse são uma ótima maneira de dar aos usuários um "empurrãozinho" em direção a ações específicas. 

Os pares de valores-chave para esse caso de uso incluem `discount_percentage` definido como o valor do desconto desejado e `class_type` definido como `coupon_code`. Esses pares de valores-chave permitem filtrar e exibir cartões de conteúdo específicos do tipo na tela de checkout. Para saber mais sobre o uso de pares de valores-chave para gerenciar vários feeds, consulte [Personalização do feed padrão do cartão de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).
<br>
<br>

![]({% image_buster /assets/img/cc_implementation/discount.png %}){: style="max-width:80%;"} 

## Emblemas de cartões de conteúdo

![Uma tela inicial do iPhone mostrando um app de amostra do Braze chamado Swifty com um emblema vermelho exibindo o número 7]({% image_buster /assets/img/cc_implementation/ios-unread-badge.png %}){: style="max-width:35%;float:right;margin-left:15px;border:none;"}

Os emblemas são ícones pequenos, ideais para chamar a atenção do usuário. O uso de emblemas para alertar o usuário sobre o novo conteúdo do Content Card pode atrair os usuários de volta ao seu app e aumentar as sessões.

### Exibir o número de cartões de conteúdo não lidos como um emblema

Você pode exibir o número de cartões de conteúdo não lidos que seu usuário tem como um emblema no ícone do seu app. 

{% tabs %}
{% tab Android %}

Você pode solicitar o número de cartões não lidos a qualquer momento, ligando para o telefone:

{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).getContentCardUnviewedCount();
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).contentCardUnviewedCount
```

{% endsubtab %}
{% endsubtabs %}

Em seguida, você pode usar essas informações para exibir um emblema que indica quantos cartões de conteúdo não lidos existem. Para saber mais, consulte a <a href="https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/get-content-card-unviewed-count.html" target="_blank">documentação de referência do SDK</a>.


{% endtab %}
{% tab swift %}

O exemplo a seguir usa `braze.contentCards` para solicitar e exibir o número de cartões de conteúdo não lidos. Depois que o app é fechado e a sessão do usuário termina, esse código solicita uma contagem de cartões, filtrando o número de cartões com base na propriedade `viewed`.

{% subtabs %}
{% subtab Swift %}

```swift
func applicationDidEnterBackground(_ application: UIApplication)
```

Nesse método, implemente o seguinte código, que atualiza ativamente a contagem de emblemas enquanto o usuário visualiza os cartões durante uma determinada sessão:

```swift
let unreadCards = AppDelegate.braze?.contentCards.cards.filter { $0.viewed == false }
UIApplication.shared.applicationIconBadgeNumber = unreadCards?.count ?? 0
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
(void)applicationDidEnterBackground:(UIApplication *)application
```

Nesse método, implemente o seguinte código, que atualiza ativamente a contagem de emblemas enquanto o usuário visualiza os cartões durante uma determinada sessão:

```objc
NSInteger unreadCardCount = 0;
for (BRZContentCardRaw *card in AppDelegate.braze.contentCards.cards) {
  if (card.viewed == NO) {
    unreadCardCount += 1;
  }
}
[UIApplication sharedApplication].applicationIconBadgeNumber = unreadCardCount;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab web %}

Você pode solicitar o número de cartões não lidos a qualquer momento, ligando para o telefone:

```javascript
braze.getCachedContentCards().getUnviewedCardCount();
```

Em seguida, você pode usar essas informações para exibir um emblema que indica quantos cartões de conteúdo não lidos existem. Para saber mais, consulte a <a href="https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.contentcards.html" target="_blank">documentação de referência do SDK</a>.

{% endtab %}
{% endtabs %}


