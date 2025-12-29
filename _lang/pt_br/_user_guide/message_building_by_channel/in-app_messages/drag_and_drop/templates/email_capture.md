---
nav_title: Formulário de inscrição por e-mail
article_title: Formulário de Inscrição por E-mail
alias: "/email_capture/"
page_order: 2
description: "Esta página cobre como criar um formulário de inscrição por e-mail com o editor de arrastar e soltar mensagens no aplicativo."
---

# Formulário de inscrição por e-mail

> Use o modelo de mensagem no aplicativo de inscrição por e-mail para coletar endereços de e-mail dos usuários e aumentar seus grupos de assinatura.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Criando um formulário de inscrição por e-mail

### Passo 1: Escolha seu modelo

Ao criar uma mensagem no aplicativo com arrastar e soltar, selecione **Inscrição por e-mail** como seu modelo, depois selecione **Construir mensagem**. Este modelo é suportado tanto para aplicativos móveis quanto para navegadores da web.

\![O editor de mensagens no aplicativo com o modelo para um formulário de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### Passo 2: Configure os estilos da sua mensagem

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Passo 3: Personalize seu componente de inscrição por e-mail

Para começar a construir seu formulário de inscrição por e-mail, selecione o elemento de captura de e-mail no editor. Por padrão, os endereços de e-mail coletados terão o grupo de assinatura global **Inscrito**. Para inscrever usuários em grupos de assinatura específicos, consulte [Atualizando estados de assinatura de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Você pode personalizar o texto do espaço reservado e o texto do rótulo do elemento de captura de e-mail.

\![O editor de mensagens no aplicativo com um menu lateral para personalizar o elemento de captura de e-mail.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### Validação de e-mail

Se o usuário inserir um endereço de e-mail que inclua quaisquer caracteres especiais não aceitos, ele verá um indicador de erro genérico e não poderá enviar o formulário. Esta mensagem de erro não é personalizável. Você pode visualizar o comportamento do erro na aba **Pré-visualização & Teste** e no seu dispositivo de teste. Saiba mais sobre como a Braze formata endereços de e-mail em [Validação de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

### Passo 4: Adicione linguagem de isenção de responsabilidade (opcional)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Passo 5: Estilize sua mensagem

Personalize a aparência do seu formulário de inscrição usando os [componentes de mensagem no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) de arrastar e soltar.

## Analisando os resultados

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Melhores práticas

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}

