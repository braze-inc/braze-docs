---
nav_title: Usando códigos
article_title: Usando códigos de promoção
page_order: 0.2
description: "Aprenda como usar códigos de promoção e visualizar o uso para suas campanhas e Canvases."
---

# Usando códigos de promoção

> Aprenda como usar códigos de promoção e visualizar o uso para suas campanhas e Canvases.

## Pré-requisitos

Antes de usar códigos de promoção, você precisará [criar uma lista de códigos de promoção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/).

## Usando códigos de promoção

Para enviar um código de promoção em uma mensagem, selecione **Copiar Snippet** ao lado da lista de códigos de promoção [que você criou anteriormente]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#create).

![Uma opção para copiar o snippet para colar em sua mensagem.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Cole os snippets de código em uma de suas mensagens no Braze, e use [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para inserir um dos códigos de promoção exclusivos da sua lista. Esse código é marcado como enviado, garantindo que nenhuma outra mensagem envie o mesmo código.

![Uma mensagem de exemplo "Presenteie-se com algo legal nesta primavera com nossa oferta exclusiva" seguida pelo snippet de código.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### Através das etapas do Canvas

Quando um snippet de código é usado em uma campanha ou Canvas com mensagens multicanal, cada usuário recebe um código exclusivo. Em um Canvas com várias etapas que referenciam códigos de promoção, um usuário recebe um novo código para cada etapa que ele entra.

Para atribuir um código de promoção em um Canvas e reutilizá-lo em etapas:

1. Atribua o código de promoção como um atributo personalizado na primeira etapa (Atualização do Usuário).
2. Use Liquid em etapas posteriores para referenciar esse atributo personalizado em vez de gerar um novo código.

Quando um usuário se qualifica para um código em vários canais, ele recebe o mesmo código em cada canal. Por exemplo, se eles recebem mensagens por e-mail e push, o mesmo código é enviado para ambos. Os relatórios também refletem um único código.

{% alert note %}
Se não houver códigos de promoção disponíveis, mensagens de teste ou ao vivo que dependem de códigos não são enviadas.
{% endalert %}

### Campanhas de mensagens no app {#promotion-codes-iam-campaigns}

Após criar uma [campanha de mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), você pode inserir um [trecho de lista de códigos de promoção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes-1) no corpo da mensagem no app. Os códigos de promoção nas mensagens no app são deduzidos e usados apenas quando um usuário aciona a exibição da mensagem no app.

### Mensagens de teste

Envios de teste e envios de e-mail do grupo de teste usam códigos de promoção, a menos que solicitado de outra forma. Entre em contato com o gerente da sua conta Braze para atualizar o comportamento deste recurso para que os códigos de promoção não sejam usados durante os envios de teste e envios de e-mail do grupo de teste.

### Com extras de mensagem para Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Salvando códigos de promoção nos perfis de usuário {#save-to-profile}

Para fazer referência ao mesmo código de promoção em mensagens subsequentes, o código deve ser salvo no perfil do usuário como um atributo personalizado. Isso pode ser feito através de um [passo de Atualização de Usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) que atribui o código de desconto a um atributo personalizado, como "Código Promocional", diretamente antes de um passo de Mensagem.

Primeiro, selecione o seguinte para cada campo no passo de Atualização de Usuário:

- **Nome do Atributo:** Código Promocional
- **Ação:** Atualizar
- **Valor da Chave:** O trecho de código Liquid do código de promoção, como {% raw %}`{% promotion('spring25') %}`{% endraw %}

Em segundo lugar, adicione o atributo personalizado (neste exemplo, {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}) a uma mensagem. O código de desconto está modelado.

## Visualizando o uso do código de promoção

Você pode encontrar a contagem de códigos restantes na coluna **Restante** da lista de códigos de promoção na página **Códigos de Promoção**.

![Um exemplo de um código de promoção com códigos não utilizados.]({% image_buster /assets/img/promocodes/promocode11.png %})

Este código de contagem também pode ser encontrado ao revisitar uma página de lista de códigos de promoção pré-existente. Você também pode exportar códigos não utilizados como um arquivo CSV. 

![Um código de promoção chamado "Venda da Black Friday" com 992 códigos restantes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Envios multicanal e de canal único

Para campanhas de envio único e multicanal e canvas, todos os códigos de promoção referenciados no Liquid de uma mensagem são deduzidos para serem usados **antes** que a mensagem seja enviada para garantir que ocorra o seguinte:

- Os mesmos códigos de promoção são usados em todos os canais em uma mensagem multicanal.
- Códigos de promoção extras não são utilizados se uma mensagem falhar ou abortar.

Se um usuário tiver duas listas de códigos de promoção referenciadas em uma mensagem que é dividida por uma tag de lógica condicional Liquid, todos os códigos de promoção ainda são deduzidos, independentemente de qual fluxo condicional o usuário segue.

Se um usuário insere uma nova etapa do canva ou reentra em um canva, e o snippet do código de promoção Liquid é aplicado novamente para uma mensagem a esse usuário, um novo código de promoção é usado.

### Exemplo

No exemplo a seguir, ambas as listas de códigos de promoção `vip-deal` e `regular-deal` são deduzidas. Aqui está o Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

A Braze recomenda fazer o upload de mais códigos de promoção do que você estima usar. Se uma lista de códigos de promoção expirar ou ficar sem códigos de promoção, as mensagens subsequentes são abortadas.

{% alert tip %}
**Aqui está uma analogia de como os códigos de promoção são usados na Braze.** <br><br>Imagine que enviar sua mensagem é como enviar uma carta no correio. Você entrega a carta a um funcionário, e ele vê que sua carta deve incluir um cupom. O atendente puxa o primeiro cupom da pilha e o adiciona ao envelope. O funcionário envia a carta, mas por algum motivo, a carta se perde no correio (e o cupom também está agora perdido). <br><br>Neste cenário, a Braze é o carteiro, e seu código de promoção é o cupom. Não podemos recuperá-lo depois que ele foi retirado da pilha de códigos de promoção, independentemente do resultado do webhook.
{% endalert %}
