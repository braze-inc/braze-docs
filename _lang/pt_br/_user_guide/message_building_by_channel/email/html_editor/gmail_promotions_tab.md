---
nav_title: Configuração de promoções do Gmail
article_title: Configuração de promoções do Gmail
page_order: 8
description: "Este artigo de referência aborda como usar a Braze para ajudar a criar o cartão de promoções para celular do Gmail a partir de sua campanha de e-mail."
channel:
  - email
toc_headers: h2
---

# Configuração da promoção do Gmail

> A [guia Promoções do Gmail para mobile](https://developers.google.com/gmail/promotab/) permite que os profissionais de marketing enviem mais informações por meio de anotações em um "cartão", em vez de apenas a linha de assunto ou as informações do pré-cabeçalho. A Braze tem uma ferramenta integrada para ajudar você a criar o cartão a partir da sua campanha de e-mail.

## Pré-requisito

Primeiro, encaminhe seus domínios e subdomínios para a equipe de divulgação da guia Promoções do Google em <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> para serem adicionados à lista de permissões do Gmail. Isso permite que você use qualquer recurso que mostre imagens ricas, como o carrossel de produtos da guia Promoções do Gmail.

## Criando o cartão com a Braze

Siga estas etapas para criar um cartão promocional do Gmail para uma campanha de e-mail. Observe que navegar para fora da seção **Conteúdo** no editor redefinirá os campos e as informações na guia **Promoção do Gmail**. Conclua a configuração do seu cartão promocional e copie o HTML gerado para não perder seu código HTML.

### Etapa 1: Criar uma campanha de e-mail

Primeiro, [crie sua campanha de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) e selecione o **editor de código HTML** como sua experiência de edição.

### Etapa 2: Adicione detalhes ao cartão de promoção do Gmail

Em seguida, acesse a seção **Conteúdo** do editor de HTML e selecione a guia **Promoção do Gmail**. Preencha os campos em **Informações Básicas** e selecione **Gerar Código HTML**. Isso ajudará a gerar o script para o seu cartão da guia Promoções do Gmail na seção **Copiar e colar código HTML em `<Head>`**.

![Um exemplo de como criar um cartão.]({% image_buster /assets/img/create-gmail-promo.png %})

### Etapa 3: Personalize seu cartão de promoção do Gmail

Escolha se deseja incluir uma oferta de desconto, cartão de oferta, cartão de promoção ou todas as opções para seu cartão de promoção do Gmail.

{% tabs %}
{% tab Discount offer %}

A configuração de uma oferta de desconto permite que você especifique as datas válidas para um desconto. 

1. Selecione o botão **Oferta de Desconto**.
2. Em **Oferta**, insira um resumo curto para o desconto. Um exemplo é "20% de desconto".
3. Em **Código**, adicione o código de promoção que o usuário precisa aplicar no checkout.
4. Em seguida, selecione a data e hora de início para a oferta de desconto.
5. Determine se a oferta de desconto deve terminar em um horário específico ou nunca terminar.

![Opções para especificar o valor da oferta, o código e a data e hora de início de uma oferta de desconto.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Deal Cards %}

Use Cartões de Oferta para fornecer informações importantes sobre a oferta diretamente no topo do corpo dos e-mails. Isso permite que os destinatários entendam rapidamente os detalhes da oferta e tomem uma ação. Por exemplo, você pode usar Cartões de Oferta para promover ofertas por tempo limitado e reduzir a necessidade de os usuários procurarem detalhes dentro dos e-mails.

1. Selecione o botão **Cartão de Oferta**.
2. Em **Oferta**, insira um resumo curto para o desconto. Um exemplo é "20% de desconto em todos os sapatos".
3. (opcional) Em **Código**, adicione o código de promoção que o usuário precisa aplicar no checkout.
4. Insira pelo menos uma das seguintes URLs. 
-  **URL da Página de Oferta:** A URL para a landing page da oferta específica. Isso cria um botão "Compre agora" (ou similar). Recomendamos fornecer esta URL para o seu Cartão de Oferta. 
- **URL da Página Inicial do Comerciante:** A URL para a sua página inicial principal. Use este campo apenas se uma URL específica da página de oferta não estiver disponível.
5. (opcional) Adicione uma data de início para a oferta.
6. Determine se a oferta deve terminar em um horário específico ou nunca terminar.

![Opções para especificar o valor da oferta, código e data e hora de início para um Cartão de Oferta.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Promotion cards %}

Os cartões promocionais no seu carrossel de produtos são úteis para fornecer imagens para sua oferta. Você também pode personalizar as variáveis do carrossel de produtos e incluir até dez prévias de imagens, sendo que cada imagem é única.

1. Selecione o botão **Cartões de Promoção**.
2. Selecione **Adicionar cartão de promoção**. Cada imagem no seu carrossel de produtos deve ter uma URL exclusiva e usar a mesma proporção (4:5, 1:1, 1.91:1).
3. Inclua uma URL de imagem.
4. Em **URL de Destino**, adicione o link para sua promoção.

{% alert tip %}
Recomendamos fazer upload das imagens do seu produto para a biblioteca de mídia e, em seguida, copiar e colar as URLs nos campos apropriados. Apenas formatos de imagem estáticos (PNG e JPEG) são aceitos. Alguns formatos de imagem (GIF) farão upload, mas não serão exibidos como esperado.
{% endalert %}

{: start="5"}
5. Personalize seu cartão de promoção adicionando um título, moeda, preço e valor de desconto.

| Propriedade personalizável | Descrição |
|---|---|
| Título | (opcional) Descrição de uma ou duas frases para a promoção. É exibido sob a imagem de prévia. |
| Moeda | (opcional) A moeda do preço. |
| Preço | O preço da promoção. |
| Valor do desconto | O valor descontado do preço original. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Um exemplo de um carrossel de produtos de uma empresa chamada Motto com o título de e-mail "Nossas meias mais vendidas estão em promoção", com três imagens de meias e seus preços com desconto.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### Etapa 4: Gere e cole o código HTML

Após criar seu cartão de promoção do Gmail, selecione **Gerar código HTML**. Copie e cole o script no elemento `<head>` do HTML do seu e-mail. 

{% alert tip %}
Para o editor de arrastar e soltar, copie e cole o código HTML gerado na seção [tags de cabeçalho personalizadas]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#custom-head-tags) em **Configurações de Envio**.
{% endalert %}

{% alert warning %}
O script de Promoções só será exibido se o seu e-mail aparecer na guia Promoções do Gmail. Atualmente, o Gmail usa algoritmos para determinar o destino do seu e-mail. No entanto, se um usuário marcar seu e-mail como promoção, o algoritmo do Gmail será ignorado e seu e-mail será automaticamente direcionado para a guia Promoções dali em diante.
{% endalert %}

## Medindo os cartões do Gmail

O Gmail não retorna análise de dados sobre esses cartões, e prestadores de serviço de e-mail (ESPs) como a Braze não podem inserir seu próprio rastreamento de links nos links da seção de cabeçalho (incluindo cartões de promoção e carrosséis de produtos). No entanto, você pode adicionar parâmetros UTM ou códigos exclusivos às URLs durante a configuração. Esses parâmetros permitem que você rastreie o engajamento usando suas próprias análises de site ou rastreamento de conversões, porque o rastreamento faz parte da própria URL — não é inserido pelo ESP. O rastreamento de cliques em nível de ESP não está disponível para esses links.

### Incorpore imagens

O Gmail obteve melhores resultados com imagens fortes relacionadas à mensagem de e-mail. O Gmail não recomenda o uso de um design somente com texto, pois esse espaço foi projetado para trazer a linguagem visual, que é vital para o e-mail marketing, para a prévia. Não use imagens com texto cortado nem repita imagens em várias campanhas.

### Descreva ofertas

O Gmail não sugere o uso de frases ou expressões, como "Compre 1 e leve 1 grátis" ou "Descontos em todos os shorts e camisetas", pois elas podem ser cortadas, deixar de chamar a atenção e competir com a linha de assunto. Esse espaço deve ser usado apenas para engajar seus clientes com suas mensagens, portanto, evite qualquer linguagem semelhante a "Abra este e-mail agora" ou "Clique aqui para ver as ofertas". É melhor evitar a repetição da sua linha de assunto.

## Melhores práticas

Em geral, siga estas [melhores práticas recomendadas pelo Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
Embora seja possível usar o Liquid nesse script, sugerimos fortemente que você teste o envio de mensagens o máximo possível para evitar erros.
{% endalert %}

### Visualize sua anotação

Use a [ferramenta de prévia](https://developers.google.com/workspace/gmail/promotab/preview) para visualizar sua anotação. Observe que enviar um e-mail de teste para si mesmo não funcionará para anotações, pois sua anotação só é renderizada se o e-mail for enviado para um número significativo de destinatários. Certifique-se de enviar o e-mail final (com suas URLs de imagem) para pelo menos 100 destinatários do Gmail.

Não use o Google Workspace para enviar e-mails com anotações. Use apenas domínios de e-mail na lista de permissões para enviar anotações para um grande grupo de destinatários.

### Siga as diretrizes de imagem

Verifique se suas imagens seguem estas diretrizes:
- Use imagens de alta qualidade e alta resolução.
- Todas as imagens anotadas devem usar a mesma proporção. As proporções suportadas incluem: 4:5, 1:1, 1.91:1.
- Use tamanhos de imagem corretos. O mínimo é 256x256; o máximo é 4096x4096 pixels.

O Gmail recomenda evitar:
- Uso excessivo de texto nas suas imagens
- Uso de imagens que são apenas ícones
- Uso de imagens com máscaras arredondadas
- Uso de URLs de imagem personalizadas

### Registre-se com DMARC

Para que suas anotações sejam renderizadas corretamente, confirme que os domínios enviados estão registrados com DMARC e que todas as políticas estão ativadas.


## Perguntas frequentes

### Por que minha mensagem promocional não está exibindo o cartão de promoção ou o carrossel de produtos na caixa de entrada do usuário final?

Existem muitos fatores que determinam se o carrossel de produtos será exibido na guia Promoções do Gmail.

Todas as imagens na anotação ainda precisam passar por um filtro de qualidade. Para que o carrossel de produtos seja preenchido, todas as imagens na anotação devem estar na proporção de imagem recomendada e ser imagens de produtos em close-up, de alta qualidade e alta resolução. As imagens devem conter pouco ou nenhum texto. O filtro de qualidade também filtra conteúdo inadequado, portanto, as imagens devem ser adequadas para famílias, usuários e crianças.

Além disso, o Gmail tem um limite de densidade sobre quantos carrosséis de produtos aparecem na guia Promoções do Gmail de um usuário. Por exemplo, se um usuário se inscrever em muitas marcas que usam carrosséis de produtos em seus e-mails de promoção, o Gmail eventualmente impõe um limite sobre quantos carrosséis de produtos são exibidos.

Devido às normas de privacidade e segurança do Google, os e-mails com anotações devem ser amplamente enviados para que a anotação funcione. É recomendável lançar uma campanha e enviá-la para pelo menos 100 destinatários para que o sistema do Google a detecte como um "envio em massa". As URLs das imagens não podem variar entre os destinatários.

### Como os cliques em um cartão de promoção ou carrossel de produtos são rastreados?

A Braze ou qualquer outro ESP não consegue inserir rastreamento de links nos links da seção de cabeçalho. Isso significa que os cliques não podem ser rastreados em um cartão de promoção ou carrossel de produtos.

### Existe uma maneira de ver quantos usuários receberam um carrossel de produtos?

O Gmail determina quando e para quem exibir o cartão, portanto, não há garantia de que todos os destinatários verão o carrossel de produtos.

### Por que não vejo anotações na minha guia Promoções do Gmail?

Anotações não são suportadas para o Google Workspace. Para visualizar anotações, você pode criar um endereço de e-mail pessoal com o Gmail.

Observe que as anotações não são exibidas na guia **Primária** ou em qualquer outra guia no app móvel do Gmail. As anotações não serão exibidas após um usuário abrir um e-mail ou se você estiver usando o tipo de anotação `DiscountOffer` e o tempo e a data já tiverem expirado.