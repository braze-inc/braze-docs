---
nav_title: Registro de e-mail com desconto
article_title: Registro de e-mail com desconto
alias: "/email_discount/"
page_order: 3
description: "Esta página de referência aborda como usar o editor de arrastar e soltar de mensagens no aplicativo para criar um formulário de inscrição de e-mail que oferece um desconto para novos assinantes."
---

# Registro de e-mail com desconto

> Use o editor de arrastar e soltar de mensagens no aplicativo para criar um formulário de inscrição de e-mail que ofereça um desconto para novos assinantes.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Criação de um formulário de inscrição de e-mail com um desconto

### Etapa 1: Escolha seu modelo

Ao criar uma mensagem in-app do tipo arrastar e soltar, selecione **Inscrição por e-mail com desconto de boas-vindas** para o seu modelo e, em seguida, selecione **Criar mensagem**. Esse modelo é compatível com aplicativos móveis e navegadores da Web.

\![O editor de mensagens no aplicativo com o modelo de um formulário de inscrição de e-mail com desconto.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_discount.png %})

### Etapa 2: Configure seus estilos de mensagem

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Etapa 3: Personalize seu componente de registro de e-mail

Para começar a criar seu formulário de inscrição por e-mail, selecione o elemento de captura de e-mail no editor. Por padrão, os endereços de e-mail coletados terão o grupo de assinatura global **Subscribed**. Para incluir usuários em grupos de assinatura específicos, consulte [Atualização de estados de assinatura de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Você pode personalizar o texto do espaço reservado e o texto do rótulo do elemento de captura de e-mail.

\![O editor de mensagens no aplicativo com um menu lateral para personalizar o elemento de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field.png %})

#### Validação de e-mail

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Etapa 4: Adicionar linguagem de isenção de responsabilidade (opcional)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Etapa 5: Estilize sua mensagem

Personalize a aparência de seu formulário de inscrição e desconto usando os [componentes de mensagem no aplicativo do]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) tipo arrastar e soltar.

## Análise dos resultados

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Práticas recomendadas

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}



