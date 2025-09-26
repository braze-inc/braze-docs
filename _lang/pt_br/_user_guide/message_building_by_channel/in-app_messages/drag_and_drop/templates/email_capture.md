---
nav_title: Formulário de inscrição de e-mail
article_title: Formulário de inscrição de e-mail
alias: "/email_capture/"
page_order: 2
description: "Esta página aborda como criar um formulário de envio de e-mail com o editor de arrastar e soltar mensagens no app."
---

# Formulário de inscrição de e-mail

> Use o modelo de mensagem no app de arrastar e soltar para fazer a inscrição por e-mail para coletar os endereços de e-mail dos usuários e aumentar seus grupos de inscrições.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Criação de um formulário de envio de e-mail

### Etapa 1: Escolha seu modelo

Ao criar uma mensagem no app do tipo arrastar e soltar, selecione **Envio de e-mail** para seu modelo e, em seguida, selecione **Criar mensagem**. Esse modelo é compatível tanto com apps móveis quanto com navegadores da Web.

![O editor de mensagens no app com o modelo de um formulário de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### Etapa 2: Configure seus estilos de mensagens

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Etapa 3: Personalize o componente de envio de e-mail

Para começar a criar seu formulário de envio de e-mail, selecione o elemento de captura de e-mail no editor. Por padrão, os endereços de e-mail coletados terão o grupo de inscrições global **Subscribed (Inscrito**). Para fazer a aceitação de usuários em grupos de inscrições específicos, consulte [Atualização de estados de envio de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Você pode personalizar o texto do espaço reservado e o texto do rótulo do elemento de captura de e-mail.

![O editor de mensagens no app com um menu lateral para personalizar o elemento de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### Validação de e-mail

Se o usuário inserir um endereço de e-mail que inclua caracteres especiais não aceitos, ele verá um indicador de erro genérico e não poderá enviar o formulário. Essa mensagem de erro não pode ser enviada de mensagens personalizadas. É possível visualizar o comportamento do erro na guia **Preview & Test** e em seu dispositivo de teste. Saiba mais sobre como a Braze formata endereços de e-mail em [Validação de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

### Etapa 4: Adicionar linguagem de isenção de responsabilidade (opcional)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Etapa 5: Estilize sua mensagem

Personalize a aparência do seu formulário de inscrição usando os [componentes de mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) do tipo arrastar e soltar.

## Análise dos resultados

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Práticas recomendadas

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}

