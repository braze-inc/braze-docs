---
nav_title: Envio de e-mail com confirmação
article_title: Envio de e-mail com página de confirmação
alias: "/email_confirmation_page/"
page_order: 6
description: "Esta página aborda como usar o editor de arrastar e soltar de mensagens no app para criar um formulário de envio de e-mail que tenha uma página de confirmação."
---

# Inscrição para e-mail com página de confirmação

> Use o editor de arrastar e soltar mensagens no app para criar um formulário de envio de e-mail com uma página de confirmação.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Criação de um formulário de envio de e-mail com uma página de confirmação

### Etapa 1: Escolha seu modelo

Ao criar uma mensagem no app do tipo arrastar e soltar, selecione **Envio de e-mail com página de confirmação** como modelo e, em seguida, selecione **Criar mensagem**. Esse modelo é compatível tanto com apps móveis quanto com navegadores da Web.

![O editor de mensagens no app com o modelo para um formulário de envio de e-mail com página de confirmação.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %})

### Etapa 2: Configure seus estilos de mensagens

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Etapa 3: Personalize o componente de envio de e-mail

Para começar a criar seu formulário de envio de e-mail, selecione o elemento de captura de e-mail no editor. Por padrão, os endereços de e-mail coletados terão o grupo de inscrições global **Subscribed (Inscrito**). Para fazer a aceitação de usuários em grupos de inscrições específicos, consulte [Atualização de estados de envio de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Você pode personalizar o texto do espaço reservado e o texto do rótulo do elemento de captura de e-mail.

![O editor de mensagens no app com um menu lateral para personalizar o elemento de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %})

#### Validação de e-mail

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Etapa 4: Adicionar linguagem de isenção de responsabilidade (opcional)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Etapa 5: Estilize sua mensagem

Personalize a aparência do seu formulário de envio de e-mail e da página de confirmação usando os [componentes de mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) do tipo arrastar e soltar.

## Análise dos resultados

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Melhores práticas

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}


