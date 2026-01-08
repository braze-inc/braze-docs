---
nav_title: Configuração de promoções do Gmail
article_title: Configuração de Promoções do Gmail
page_order: 8
description: "Este artigo de referência cobre como usar o Braze para ajudá-lo a construir o cartão de promoções móveis do Gmail a partir da sua campanha de e-mail."
channel:
  - email

---

# Configuração de promoção do Gmail

> A [aba de Promoções móveis do Gmail](https://developers.google.com/gmail/promotab/) permite que os profissionais de marketing enviem mais informações por meio de anotações em um "cartão" em vez de apenas na linha de assunto ou nas informações do cabeçalho. O Braze possui uma ferramenta integrada para ajudá-lo a construir o cartão a partir da sua campanha de e-mail.

## Pré-requisito

Primeiro, encaminhe seus domínios e subdomínios para a equipe de outreach da aba de Promoções do Google em <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> para ser adicionado à lista de permissões do Gmail. Isso permite que você use qualquer recurso que mostre imagens ricas, como o carrossel de produtos para a aba de Promoções do Gmail.

## Construindo o cartão com o Braze

Siga estas etapas para construir um cartão de promoção do Gmail para uma campanha de e-mail. Observe que navegar para fora da seção **Conteúdo** no editor redefinirá os campos e informações na aba **Promoção do Gmail**. Complete a configuração do seu cartão de promoção e copie o HTML gerado para não perder seu código HTML.

### Passo 1: Crie uma campanha de e-mail

Primeiro, [crie sua campanha de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) e selecione o **editor de código HTML** como sua experiência de edição.

### Passo 2: Adicione detalhes ao cartão de Promoção do Gmail

Em seguida, vá para a seção **Conteúdo** do editor HTML e selecione a aba **Promoção do Gmail**. Preencha os campos sob **Informações Básicas**, depois selecione **Gerar Código HTML**. Isso ajudará a gerar o script para seu cartão da aba Promoções do Gmail na seção **Copie e Cole o código HTML em `<Head>`**.

\![Um exemplo de como construir um cartão.]({% image_buster /assets/img/create-gmail-promo.png %})

### Passo 3: Personalize seu cartão de Promoção do Gmail

Escolha se deseja incluir uma oferta de desconto, cartão de oferta, cartão de promoção ou todas as opções para seu cartão de Promoção do Gmail.

{% tabs %}
{% tab Discount offer %}

Configurar uma oferta de desconto permite que você especifique as datas válidas para um desconto. 

1. Selecione o botão **Oferta de Desconto**.
2. Para **Oferta**, insira um resumo curto para o desconto. Um exemplo é "20% de desconto".
3. Para **Código**, adicione o código promocional que um usuário precisa aplicar no checkout.
4. Em seguida, selecione a data e hora de início para a oferta de desconto.
5. Determine se a oferta de desconto deve terminar em um horário específico ou nunca terminar.

\![Opções para especificar o valor da oferta, código e data e hora de início para uma oferta de desconto.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Deal Cards %}

Use Cartões de Oferta para fornecer informações chave sobre a oferta diretamente no topo dos corpos de e-mail. Isso permite que os destinatários entendam rapidamente os detalhes da oferta e tomem uma ação. Por exemplo, você pode usar Cartões de Oferta para promover ofertas por tempo limitado e reduzir a necessidade de os usuários procurarem detalhes dentro dos e-mails.

1. Selecione o botão **Cartão de Oferta**.
2. Para **Oferta**, insira um resumo curto para o desconto. Um exemplo é "20% de desconto em todos os sapatos".
3. (opcional) Para **Código**, adicione o código promocional que um usuário precisa aplicar no checkout.
4. Insira pelo menos uma das seguintes URLs. 
-  **Página da Oferta URL:** A URL para a página de destino da oferta específica. Isso cria um botão "Compre agora" (ou similar). Recomendamos fornecer esta URL para seu Cartão de Oferta. 
- **URL da Página Inicial do Comerciante:** A URL para sua página inicial principal. Use este campo apenas se uma URL específica da página da oferta não estiver disponível.
5. (opcional) Adicione uma data de início para a oferta.
6. Determine se a oferta deve terminar em um horário específico ou nunca terminar.

\![Opções para especificar o valor da oferta, código e data e hora de início para um Cartão de Oferta.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Promotion cards %}

Os cartões promocionais em seu carrossel de produtos são úteis para fornecer imagens para sua oferta. Você também pode personalizar variáveis em seu carrossel de produtos e incluir até dez pré-visualizações de imagens, onde cada imagem é única.

1. Selecione o botão **Cartões Promocionais**.
2. Selecione **Adicionar cartão promocional**. Cada imagem em seu carrossel de produtos deve ter uma URL única e usar a mesma proporção (4:5, 1:1, 1.91:1).
3. Inclua uma URL de imagem.
4. Para **URL de Destino**, adicione o link para sua promoção.

{% alert tip %}
Recomendamos fazer upload das suas imagens de produto para a biblioteca de mídia, depois copiar e colar as URLs nos campos apropriados. Apenas formatos de imagem estáticos (PNG e JPEG) são aceitos. Alguns formatos de imagem (GIF) serão carregados, mas não serão exibidos como esperado.
{% endalert %}

{: start="5"}
5\. Personalize seu cartão de promoção adicionando um título, moeda, preço e valor de desconto.

| Propriedade personalizável | Descrição |
|---|---|
| Título | (opcional) Uma ou duas frases de descrição para a promoção. Exibe abaixo da imagem de pré-visualização. |
| Moeda | (opcional) A moeda do preço. |
| Preço | O preço da promoção. |
| Valor do Desconto | O valor descontado do preço original. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\![Um exemplo de um carrossel de produtos de uma empresa chamada Motto com o título do e-mail "Nossas meias mais vendidas estão em promoção", com três imagens de meias e seus preços com desconto.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### Passo 4: Gere e cole o código HTML

Após construir seu cartão de promoção do Gmail, selecione **Gerar código HTML**. Copie e cole o script no elemento `<head>` do HTML do seu e-mail.

{% alert warning %}
O script de Promoções só aparece se seu e-mail cair na aba Promoções do Gmail. Atualmente, o Gmail usa algoritmos para determinar onde seu e-mail será entregue. No entanto, se um usuário marcar seu e-mail como promoção, o algoritmo do Gmail será ignorado, e seu e-mail automaticamente cairá na aba Promoções a partir de então.
{% endalert %}

## Melhores práticas

Em geral, siga estas [melhores práticas recomendadas pelo Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
Embora você possa usar Liquid dentro deste script, sugerimos fortemente que você teste suas mensagens o máximo possível para evitar um erro.
{% endalert %}

### Incorpore imagens

O Gmail teve melhores resultados com imagens fortes relacionadas à mensagem do e-mail. O Gmail não recomenda usar um design apenas de texto, pois este espaço foi projetado para trazer uma linguagem visual, que é vital para o marketing por e-mail, à pré-visualização. Não use imagens com texto cortado ou repita imagens em várias campanhas.

### Descreva ofertas

O Gmail não sugere usar frases ou sentenças, como "Você pode comprar 1 e levar 1 grátis ou descontos em todos os shorts e camisetas", pois isso pode ser cortado, não chamar mais a atenção e competir com a linha de assunto. Este espaço deve ser usado apenas para engajar seus clientes com sua mensagem, então evite qualquer linguagem semelhante a "Abra este e-mail agora" ou "Clique aqui para ofertas". É melhor evitar repetir sua linha de assunto.

## Perguntas frequentes

### Por que minha mensagem promocional não está exibindo o cartão de promoção ou o carrossel de produtos na caixa de entrada do usuário final?

Existem muitos fatores que determinam se o carrossel de produtos será exibido na aba Promoções do Gmail.

Todas as imagens na anotação ainda precisam passar por um filtro de qualidade. Para que o carrossel de produtos seja preenchido, é crucial que todas as imagens na anotação estejam na proporção de aspecto de imagem recomendada, imagens de produtos de alta qualidade ou alta resolução em close-up. As imagens devem conter pouco ou nenhum texto (preferencialmente). O filtro de qualidade também filtra conteúdo inadequado, então as imagens devem ser familiares, amigáveis para o usuário e para crianças.

Além disso, o Gmail tem um limite de densidade sobre quantos carrosséis de produtos aparecem na aba Promoções do Gmail de um usuário. Por exemplo, se um usuário se inscreve em muitas marcas que usam carrosséis de produtos em seu e-mail promocional, o Gmail eventualmente coloca um limite sobre quantos carrosséis de produtos são mostrados.

Devido às regulamentações de privacidade e segurança do Google, e-mails com anotações devem ser amplamente enviados para que a anotação funcione. É recomendável lançar uma campanha e enviá-la para pelo menos 100 destinatários para que o sistema do Google a detecte como um "envio em massa." Os URLs das imagens não podem variar entre os destinatários.

### Como os cliques em um cartão promocional ou carrossel de produtos são rastreados?

Braze ou qualquer outro ESP não consegue inserir rastreamento de links nos links na seção de cabeçalho. Isso significa que os cliques não podem ser rastreados em um cartão promocional ou carrossel de produtos.

### Há uma maneira de ver quantos usuários receberam um carrossel de produtos?

O Gmail determina quando e para quem exibir o cartão, então não há garantia de que todos os destinatários verão o carrossel de produtos.

