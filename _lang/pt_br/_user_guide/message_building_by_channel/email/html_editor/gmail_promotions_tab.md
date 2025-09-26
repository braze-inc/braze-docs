---
nav_title: Configuração de promoções do Gmail
article_title: Configuração de promoções do Gmail
page_order: 8
description: "Este artigo de referência aborda como usar a Braze para ajudar a criar o cartão de promoções para celular do Gmail a partir de sua campanha de e-mail."
channel:
  - email

---

# Configuração da promoção do Gmail

> A [guia Promoções do Gmail para mobile](https://developers.google.com/gmail/promotab/) permite que os profissionais de marketing enviem mais informações por meio de anotações em um "cartão", em vez de apenas a linha de assunto ou as informações do pré-cabeçalho. O Braze tem uma ferramenta integrada para ajudá-lo a criar o cartão de sua campanha de e-mail.

## Pré-requisito

Primeiro, encaminhe seus domínios e subdomínios para a equipe de divulgação da guia Promoções do Google em <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> para serem adicionados à lista de permissões do Gmail. Isso permite que você use qualquer recurso que mostre imagens ricas, como o carrossel de produtos da guia Promoções do Gmail.

## Criando o cartão com a Braze

Siga estas etapas para criar um cartão promocional do Gmail para uma campanha de e-mail. Observe que navegar para fora da seção **Conteúdo** no editor redefinirá os campos e as informações na guia **Promoção do Gmail**. Conclua a configuração de seu cartão promocional e copie o HTML gerado para não perder seu código HTML.

1. [Crie sua campanha de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) e selecione o **Editor de HTML** como sua experiência de edição.
2. Acesse a seção **Conteúdo** no editor de HTML e selecione a guia **Promoção do Gmail**.
3. Preencha os campos em **Basic Information (Informações básicas)** e clique em **Generate HTML Code (Gerar código HTML**). Isso ajudará a gerar o script para o seu cartão de guia de promoção do Gmail na seção **Copiar e colar código HTML em `<Head>`**. <br> ![Um exemplo de como criar um cartão.]({% image_buster /assets/img/create-gmail-promo.png %})
4. Escolha se deseja incluir apenas uma oferta de desconto, cartões promocionais ou ambos em seu cartão de promoção do Gmail. <br> ![Opções para incluir uma oferta de desconto e cartões promocionais.]({% image_buster /assets/img_archive/gmail_promo_discount.png %}){: style="max-width:70%;"}
5. Copie e cole o script no elemento `<head>` do HTML de seu e-mail.

{% alert warning %}
O script Promoções só será exibido se o seu e-mail aparecer na guia Promoções do Gmail. Atualmente, o Gmail usa algoritmos para determinar o destino de seu e-mail. No entanto, se um usuário marcar seu e-mail como uma promoção, o algoritmo do Gmail será ignorado, e seu e-mail será automaticamente colocado na guia Promoções daqui para frente.
{% endalert %}

### Inclusão de uma oferta de desconto

A configuração de uma oferta de desconto permite que você especifique as datas válidas para um desconto. Depois de determinar sua oferta de desconto, selecione uma data e hora de início. Você tem a opção de encerrar sua oferta de desconto em um momento específico ou optar por nunca encerrá-la.

![Opções para especificar o valor da oferta, o código e a data e hora de início de uma oferta de desconto.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

### Personalização do carrossel de produtos

Os cartões promocionais em seu carrossel de produtos são úteis para fornecer imagens para sua oferta. Você também pode personalizar as variáveis do carrossel de produtos e incluir até dez prévias de imagens, sendo que cada imagem é única.

![Um exemplo de um carrossel de produtos de uma empresa chamada Motto com o título de e-mail "Nossas meias mais vendidas estão em promoção", com três imagens de meias e seus preços com desconto.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

| Variável personalizável | Descrição |
|---|---|
| URL de imagem | O URL de sua imagem. Cada imagem em seu carrossel de produtos deve ter um URL exclusivo e usar a mesma proporção (4:5, 1:1, 1,91:1). |
| URL de destino | O link para sua promoção. |
| Título | (opcional) Descrição de uma ou duas frases para a promoção. É exibido sob a imagem prévia. |
| Moeda | (opcional) A moeda do preço. |
| Preço | O preço da promoção. |
| Valor do desconto | O valor descontado do preço original. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Recomendamos fazer upload das imagens de seus produtos na biblioteca de mídia e, em seguida, copiar e colar os URLs nos campos apropriados. Somente formatos de imagem estática (PNG e JPEG) são aceitos. Alguns formatos de imagem (GIF) farão upload, mas não serão exibidos como esperado.
{% endalert %}

### Práticas recomendadas

Em geral, siga as [práticas recomendadas pelo Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
Embora seja possível usar o Liquid nesse script, sugerimos que você teste o envio de mensagens o máximo possível para evitar erros.
{% endalert %}

#### Incorporação de imagens

O Gmail obteve melhores resultados com imagens fortes relacionadas à mensagem de e-mail. O Gmail não recomenda o uso de um design somente de texto, pois esse espaço foi projetado para trazer a linguagem visual, que é vital para o envio de e-mail marketing, para a prévia. Não use imagens com texto cortado nem repita imagens em várias campanhas.

#### Descrição das ofertas

O Gmail não sugere o uso de frases ou expressões, como "Compre 1 e leve 1 grátis" ou "Descontos em todos os shorts e camisetas", pois elas podem ser cortadas, deixar de chamar a atenção e competir com a linha de assunto. Esse espaço deve ser usado apenas para engajar seus clientes com suas mensagens, portanto, evite qualquer linguagem semelhante a "Abra este e-mail agora" ou "Clique aqui para ver as ofertas". É melhor evitar a repetição de sua linha de assunto.

## Perguntas frequentes

### Por que minha mensagem promocional não está exibindo o cartão de promoção ou o carrossel de produtos na caixa de entrada do usuário final?

Há muitos fatores que determinam se o carrossel de produtos será mostrado na guia Promoção do Gmail.

Todas as imagens na anotação ainda precisam passar por um filtro de qualidade. Para que o carrossel de produtos seja preenchido, é crucial que todas as imagens na anotação estejam na proporção de imagem recomendada, com alta qualidade ou imagens de produtos em close-up de alta resolução. As imagens devem conter pouco ou nenhum texto (de preferência). O filtro de qualidade também filtra conteúdo inadequado, portanto, as imagens devem ser adequadas para famílias, usuários e crianças.

Além disso, o Gmail tem um limite de densidade de quantos carrosséis de produtos aparecem na guia Promoção do Gmail de um usuário. Por exemplo, se um usuário se inscreve em muitas marcas que usam carrossel de produtos em seus e-mails de promoção, o Gmail acaba limitando o número de carrosséis de produtos exibidos.

Devido às normas de privacidade e segurança do Google, os e-mails com anotações devem ser amplamente enviados para que a anotação funcione. É recomendável lançar uma campanha e enviá-la a pelo menos 100 destinatários para que o sistema do Google a detecte como um "envio em massa". Os URLs das imagens não podem variar entre os destinatários.

### Como os cliques em um cartão de promoção ou carrossel de produtos são rastreados?

O Braze ou qualquer outro ESP não pode inserir rastreamento de links nos links da seção de cabeçalho. Isso significa que os cliques não podem ser rastreados em um cartão de promoção ou carrossel de produtos.

### Existe uma maneira de ver quantos usuários receberam um carrossel de produtos?

O Gmail determina quando e para quem exibir o cartão, portanto, não há garantia de que todos os destinatários verão o carrossel de produtos.

