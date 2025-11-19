---
nav_title: Estúdio IAM
article_title: Estúdio IAM
description: "Este artigo de referência descreve a parceria entre o Braze e o IAM Studio, uma plataforma de personalização de mensagens que permite criar experiências ricas e personalizadas no app e fornecê-las por meio do Braze."
alias: /partners/iam_studio/
page_type: partner
search_tag: Partner

---

# Estúdio IAM

> [O IAM Studio](https://www.inappmessage.com) é uma plataforma de personalização de mensagens sem código que permite criar experiências no app ricas e personalizadas e fornecê-las por meio do Braze.

_Esta integração é mantida pelo IAM Studio.\*s._

## Sobre a integração

Com a integração do Braze e do IAM Studio, você pode inserir facilmente modelos de mensagens no app personalizáveis em suas mensagens no app do Braze, oferecendo substituição de imagem, modificação de texto, configurações de deep linking, atributos personalizados e configurações de eventos. Usando o IAM Studio, é possível reduzir o tempo de produção de mensagens e dedicar mais tempo ao planejamento de conteúdo. 

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do IAM Studio | É necessário ter uma [conta do IAM Studio](https://www.inappmessage.com/register) para usar essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso

- Incentivar a compra de mercadorias
- Coleta de informações do usuário
- Aumentar o cadastro de associados
- Informações sobre a emissão de cupons

## Integração

### Etapa 1: Escolha um modelo

Escolha um modelo de mensagem no app que você deseja usar na galeria de modelos de mensagens no app

![A galeria de modelos do IAM Studio mostra diferentes modelos, como "modal de slide em carrossel", "modal de ícone simples", "modal de imagem completa" e mais.]({% image_buster /assets/img/iam_studio/iam_template_gallery.png %})

### Etapa 2: Personalizar o modelo

Primeiro, personalize a imagem, o texto e o botão para seu conteúdo. Certifique-se de conectar o **Deeplink** para a imagem e o botão.

{% tabs local %}
{% tab Imagem %}
![A interface de usuário do IAM Studio mostra as opções para personalizar a imagem. Essas opções incluem a imagem, o raio da imagem e a imagem escurecida.]({% image_buster /assets/img/iam_studio/iam_customize_image.png %})
{% endtab %}
{% tab Texto %}
![A interface de usuário do IAM Studio mostra as opções para personalizar o título e o subtítulo da mensagem. Essas opções incluem texto, formatação e fonte.]({% image_buster /assets/img/iam_studio/iam_customize_text.png %})
{% endtab %}
{% tab Botão %}
![A interface de usuário do IAM Studio mostra as opções para personalizar os botões principal, esquerdo e direito. Essas opções incluem cor, deep link, texto e formatação.]({% image_buster /assets/img/iam_studio/iam_customize_button.png %})
{% endtab %}
{% endtabs %}

Em seguida, crie sua mensagem personalizada no app adicionando fontes personalizadas e usando Liquid tags. Para ativar o registro e o rastreamento, selecione **Log data and track user behavior** (Registrar dados e rastrear o comportamento do usuário).

{% tabs local %}
{% tab Fontes %}
![A interface de usuário do IAM Studio mostra as opções para adicionar Liquid. Essas opções incluem a criação de frases personalizadas.]({% image_buster /assets/img/iam_studio/iam_custom_font.png %})
{% endtab %}
{% tab Liquid %}
![A interface do usuário do IAM Studio mostrando as opções para personalizar o registro de eventos/atributos. Essas opções incluem o registro do comportamento do usuário.]({% image_buster /assets/img/iam_studio/iam_liquid.png %})
{% endtab %}
{% tab Registro e rastreamento %}
![A interface de usuário do IAM Studio mostra as opções para personalizar a fonte. Essas opções incluem a possibilidade de o usuário personalizar o estilo da fonte.]({% image_buster /assets/img/iam_studio/iam_tracking_logging.png %})
{% endtab %}
{% endtabs %}

### Etapa 3: Exportar o modelo

Uma vez concluída a edição, exporte o modelo clicando em **Exportar**. Após a exportação, o código HTML da mensagem no app será gerado. Copie esse código clicando no botão **Copiar código**. 

![]({% image_buster /assets/img/iam_studio/export_iam_code.png %}){: style="max-width:45%;"}

### Etapa 4: Use o código no Braze 

Navegue até o Braze e, em sua mensagem no app com código personalizado, cole o código personalizado na caixa de **entrada HTML**. Certifique-se de testar sua mensagem para verificar se ela está sendo exibida corretamente.

![]({% image_buster /assets/img/iam_studio/braze_campaign_editor.png %}){: style="max-width:85%;"}


