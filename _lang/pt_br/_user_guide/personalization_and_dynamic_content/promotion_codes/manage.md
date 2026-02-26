---
nav_title: Uso de códigos
article_title: Uso de códigos promocionais
page_order: 0.2
description: "Saiba como usar códigos promocionais e visualizar o uso em suas campanhas e Canvas."
---

# Uso de códigos promocionais

> Saiba como usar códigos promocionais e visualizar o uso em suas campanhas e Canvas.

## Pré-requisitos

Antes de poder usar os códigos promocionais, você precisará [criar uma lista de códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/).

## Uso de códigos promocionais

Para enviar um código promocional em uma mensagem, selecione **Copy Snippet** ao lado da lista de códigos promocionais [criada anteriormente]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#create).

![Uma opção para copiar o snippet e colá-lo em sua mensagem.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Cole os trechos de código em uma de suas mensagens no Braze e, em seguida, use [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para inserir um dos códigos promocionais exclusivos de sua lista. Esse código é marcado como enviado, garantindo que nenhuma outra mensagem envie o mesmo código.

![Um exemplo de mensagem "Treat yourself to something nice this spring with our exclusive offer" (Presenteie-se com algo agradável nesta primavera com nossa oferta exclusiva) seguido do trecho de código.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### Etapas do Canva

Quando um snippet de código é usado em uma campanha ou no Canva com mensagens em vários canais, cada usuário recebe um código exclusivo. Em um Canva com várias etapas que fazem referência a códigos promocionais, o usuário recebe um novo código para cada etapa em que entra.

Para atribuir um código de promoção em um Canva e reutilizá-lo em todas as etapas:

1. Atribua o código de promoção como um atributo personalizado na primeira etapa (Atualização do usuário).
2. Use o Liquid em etapas posteriores para fazer referência a esse atributo personalizado em vez de gerar um novo código.

Quando um usuário se qualifica para um código em vários canais, ele recebe o mesmo código em cada canal. Por exemplo, se eles receberem mensagens por e-mail e push, o mesmo código será enviado para ambos. Os relatórios também refletem um único código.

{% alert note %}
Se não houver códigos promocionais disponíveis, as mensagens de teste ou ao vivo que dependem de códigos não serão enviadas.
{% endalert %}

### Campanhas de mensagens no app {#promotion-codes-iam-campaigns}

Depois de criar uma [campanha de mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), você pode inserir um [snippet de lista de códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes-1) no corpo da mensagem da mensagem no app. Os códigos promocionais em mensagens no app são deduzidos e usados somente quando um usuário dispara a exibição da mensagem no app.

### Envio de mensagens de teste

Os envios de teste e os envios de e-mail de grupos de teste usam códigos promocionais, a menos que seja solicitado o contrário. Entre em contato com o gerente da sua conta Braze para atualizar o comportamento deste recurso para que os códigos de promoção não sejam usados durante os envios de teste e envios de e-mail do grupo de teste.

### Com extras de mensagens para Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Salvar códigos promocionais nos perfis de usuário {#save-to-profile}

Para fazer referência ao mesmo código de promoção em mensagens subsequentes, o código deve ser salvo no perfil do usuário como um atributo personalizado. Isso pode ser feito por meio de uma [etapa de atualização do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) que atribui o código de desconto a um atributo personalizado, como "Código promocional", diretamente antes de uma etapa de mensagem.

Primeiro, selecione o seguinte para cada campo na etapa Atualização do usuário:

- **Nome da atribuição:** Código promocional
- **Ação:** Atualizar
- **Valor-chave:** O trecho de código Liquid do código promocional, como {% raw %}`{% promotion('spring25') %}`{% endraw %}

Em segundo lugar, adicione o atributo personalizado (neste exemplo, {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}) a uma mensagem. O código de desconto é modelado em.

## Visualização do uso do código promocional

Você pode encontrar a contagem de códigos restantes na coluna **Remanescente** da lista de códigos promocionais na página **Códigos promocionais**.

![Um exemplo de um código promocional com códigos não utilizados.]({% image_buster /assets/img/promocodes/promocode11.png %})

Este código de contagem também pode ser encontrado ao revisitar uma página de lista de códigos de promoção pré-existente. Também é possível exportar códigos não utilizados como um arquivo CSV. 

![Um código promocional chamado "Black Friday Sale" com 992 códigos restantes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Envios multicanal e de canal único

Para campanhas de envio único e multicanal e canvas, todos os códigos de promoção referenciados no Liquid de uma mensagem são deduzidos para serem usados **antes** que a mensagem seja enviada para garantir que ocorra o seguinte:

- Os mesmos códigos de promoção são usados em todos os canais em uma mensagem multicanal.
- Códigos de promoção extras não são utilizados se uma mensagem falhar ou abortar.

Se um usuário tiver duas listas de códigos promocionais referenciadas em uma mensagem que é dividida por uma tag de lógica condicional Liquid, todos os códigos promocionais ainda serão deduzidos, independentemente do fluxo condicional que o usuário seguir.

Se um usuário entrar em uma nova etapa do Canva ou entrar novamente em um Canvas, e o snippet Liquid do código promocional for aplicado novamente a uma mensagem para esse usuário, um novo código promocional será usado.

### Exemplo

No exemplo a seguir, ambas as listas de códigos promocionais `vip-deal` e `regular-deal` são deduzidas. Aqui está o Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

O Braze recomenda fazer upload de mais códigos promocionais do que os que você estima usar. Se uma lista de códigos promocionais expirar ou ficar sem códigos promocionais, as mensagens subsequentes serão abortadas.

{% alert tip %}
**Aqui está uma analogia de como os códigos de promoção são usados na Braze.** <br><br>Imagine que enviar sua mensagem é como enviar uma carta no correio. Você entrega a carta a um funcionário, e ele vê que sua carta deve incluir um cupom. O atendente puxa o primeiro cupom da pilha e o adiciona ao envelope. O funcionário envia a carta, mas por algum motivo, a carta se perde no correio (e o cupom também está agora perdido). <br><br>Nesse cenário, o Braze é o funcionário dos correios, e seu código promocional é o cupom. Não podemos recuperá-lo depois de ter sido retirado da pilha de códigos promocionais, independentemente do resultado do webhook.
{% endalert %}
