---
nav_title: Registro de e-mail com oferta
article_title: Registro de e-mail com oferta especial
alias: "/email_offer/"
page_order: 5
description: "Esta página aborda como usar o editor de arrastar e soltar mensagens no aplicativo para criar sua lista de e-mails, oferecendo um desconto especial na inscrição."
---

# Registro de e-mail com oferta especial

> Use o editor de arrastar e soltar mensagens no aplicativo para criar sua lista de e-mails, oferecendo um desconto especial na inscrição.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Criar um formulário de inscrição de e-mail com uma oferta especial

### Etapa 1: Escolha seu modelo

Ao criar uma mensagem in-app do tipo arrastar e soltar, selecione **Inscrição por e-mail com oferta especial** como modelo e, em seguida, selecione **Criar mensagem**. Esse modelo é compatível com aplicativos móveis e navegadores da Web.

\![O editor de mensagens no aplicativo com o modelo para um formulário de inscrição de e-mail com uma oferta especial.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_offer.png %})

### Etapa 2: Configure seus estilos de mensagem

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Etapa 3: Personalize seu componente de registro de e-mail

Para começar a criar seu formulário de inscrição por e-mail, selecione a página **de inscrição por e-mail** e, em seguida, selecione o elemento de captura de e-mail no editor. Por padrão, os endereços de e-mail coletados terão o grupo de assinatura global **Subscribed**. Para incluir usuários em grupos de assinatura específicos, consulte [Atualização dos estados de assinatura de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Você pode personalizar o texto do espaço reservado e o texto do rótulo do elemento de captura de e-mail.

\![O editor de mensagens no aplicativo com um menu lateral para personalizar o elemento de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_offer.png %})

#### Validação de e-mail

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Etapa 4: Adicionar linguagem de isenção de responsabilidade (opcional)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Etapa 5: Estilize sua mensagem

Personalize a aparência de sua oferta especial usando os [componentes de mensagem no aplicativo do]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) tipo arrastar e soltar.

## Análise dos resultados

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Práticas recomendadas

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}



