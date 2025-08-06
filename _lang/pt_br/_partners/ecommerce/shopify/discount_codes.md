---
nav_title: Códigos de desconto exclusivos 
article_title: Envio de códigos de desconto exclusivos
alias: /shopify_discount_codes/
page_order: 6
description: "Este artigo de referência aborda um caso de uso enviado pela comunidade sobre o uso de códigos promocionais do Braze com o Shopify Bulk Discount Code Bot para enviar códigos de desconto exclusivos por meio de suas campanhas e Canvas."
---

# Envio de códigos de desconto exclusivos por meio da Shopify

> Esse caso de uso enviado pela comunidade mostra como usar [os códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/) do Braze com o Shopify Bulk Discount Code Bot para gerar códigos de desconto exclusivos para suas campanhas e Canvas. Os códigos de desconto exclusivos ajudam a evitar a exploração de códigos promocionais genéricos.

{% alert important %}
Essa é uma integração enviada pela comunidade e não é diretamente suportada pela Braze. O Bot de código de desconto em massa é suportado diretamente pela Shopify. Somente os códigos promocionais do Braze são suportados pelo Braze.
{% endalert %}

## Solicitações

| Requisito | Descrição |
| --- | --- |
| Configurar uma loja da Shopify | Confirme que você já configurou [uma loja do Shopify com o Braze]({{site.baseurl}}/shopify_overview/). |
| Instale o aplicativo Bulk Discount Code Bot | Baixe o aplicativo [Bulk Discount Code Bot](https://apps.shopify.com/bulk-discount-generator) na loja de aplicativos da Shopify. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Geração de códigos de desconto exclusivos

### Etapa 1: Configure seus códigos de desconto

Use o Bot de código de desconto em massa para configurar seus códigos de desconto com base no número de códigos a serem gerados, no comprimento do código, no valor do desconto e muito mais.

![As opções de configuração para um conjunto de descontos.][1]

### Etapa 2: Exportar seus códigos

Encontre seu conjunto de descontos na barra de pesquisa do Bulk Discount Code Bot e selecione **Export Codes** > **Download Codes** para baixar um arquivo CSV para a pasta Downloads.

![Barra de pesquisa com um menu suspenso que exibe o conjunto de descontos e uma linha de botões para seleção.][2]{: style="max-width:70%;"}

No arquivo CSV, exclua a linha 1 para remover o cabeçalho da coluna "Promo". Isso evitará que "Promo" se torne um código de desconto no Braze.

![Um fluxograma que mostra a remoção do cabeçalho da linha "Promo" em um arquivo CSV.][3]{: style="max-width:60%;"}

### Etapa 3: Adicione seus códigos de desconto ao Braze

No Braze, acesse **Data Settings** > **Promotion Codes** > **Create Promotion Code List** e [configure sua lista de códigos de desconto]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/#creating-a-promotion-code-list). Verifique se você corresponde à data de expiração que foi configurada pelo Bulk Discounts Code Bot.

Em seguida, faça upload de seu arquivo CSV e selecione **Save List (Salvar lista**).

### Etapa 4: Adicione seus códigos de desconto a uma campanha no Braze ou a uma etapa do Canva

Se quiser usar seus códigos de desconto exclusivos em uma campanha de envio único ou se não se importar que os usuários recebam vários códigos exclusivos em diferentes campanhas ou etapas do Canva, copie o snippet Liquid do código da lista de códigos promocionais que você salvou.

![Um trecho de código Liquid com um botão para copiá-lo.][4]{: style="max-width:60%;"}

Cole o snippet do Liquid em uma campanha ou etapa do Canva. 

![Um GIF mostrando o snippet do Liquid sendo adicionado a uma etapa do Canva.][5]

Se quiser que os usuários recebam um único código de desconto exclusivo, não importa quantas vezes o código de desconto seja referenciado em campanhas ou Canvas, crie uma etapa [de Atualização do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) diretamente antes da primeira etapa de Mensagens que atribua o código de desconto a um atributo personalizado, como "Código promocional".

{% alert tip %}
Você também pode [criar um atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) acessando **Configurações de dados** > Atributos personalizados.
{% endalert %}

Na etapa Atualização do usuário, faça o seguinte para cada campo:
- **Nome da atribuição:** Selecione **o código promocional**.
- **Ação:** Selecione **Update (Atualizar**).
- **Valor-chave:** Cole o trecho de código do Liquid.

![Uma etapa de atualização do usuário que atualiza uma atribuição de "Código promocional" com o snippet do Liquid.][6]

Agora, você pode adicionar o atributo personalizado {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} a qualquer mensagem, e o código de desconto será modelado.

## Comportamento do código de desconto

{% details Campanha multicanal ou etapa do Canva %}

Quando um snippet de código de desconto é usado em uma campanha multicanal ou etapa do Canva, os usuários sempre recebem um código exclusivo. Se um usuário for elegível para receber um código por mais de um canal, ele receberá o mesmo código em cada canal. Em outras palavras, um usuário elegível receberia apenas um código em todas as mensagens enviadas por essa campanha ou etapa do Canva.

{% enddetails %}

{% details Diferentes etapas do Canva ou campanhas separadas %}

Quando um código de desconto é referenciado por várias etapas no mesmo Canvas ou por campanhas separadas, um usuário elegível receberá vários códigos promocionais exclusivos (um código para cada etapa do Canva ou campanha).

{% enddetails %}

[1]: {% image_buster /assets/img/Shopify/configure_discount_codes.png %}
[2]: {% image_buster /assets/img/Shopify/export_discount_codes.png %}
[3]: {% image_buster /assets/img/Shopify/edited_codes_csv.png %}
[4]: {% image_buster /assets/img/Shopify/liquid_code_snippet.png %}
[5]: {% image_buster /assets/img/Shopify/liquid_promo_code.gif %}
[6]: {% image_buster /assets/img/Shopify/user_update_step.png %}