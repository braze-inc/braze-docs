---
nav_title: Registro incorporado
article_title: Registro incorporado no WhatsApp
page_order: 0
description: "Este artigo de referência fornece um passo a passo do fluxo de trabalho de registro incorporado do WhatsApp no Braze."
page_type: reference
channel:
  - WhatsApp
---

# Registro incorporado no WhatsApp

> Este artigo de referência fornece um passo a passo do fluxo de trabalho de registro incorporado do WhatsApp no Braze.

O fluxo de trabalho de registro incorporado do WhatsApp é acessado quando você [integra o WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) pela primeira vez ao seu espaço de trabalho no Braze e quando você [adiciona uma conta do WhatsApp Business]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/) a uma integração existente do WhatsApp.

{% alert note %}
Você pode adicionar [várias contas do WhatsApp Business](({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups/)) a um espaço de trabalho do Braze. No entanto, cada conta específica do WhatsApp Business pode ser adicionada a apenas um espaço de trabalho do Braze.
{% endalert %}

## Acessando o fluxo de trabalho

Vá para **Partner Integrations** > **Technology Partners** e, em seguida, pesquise e selecione **WhatsApp**. Sua próxima seleção depende do seu caso de uso:

- Se você estiver integrando o WhatsApp ao seu espaço de trabalho, selecione **Begin Integration (Iniciar integração**). <br><br>Página de parceiro do WhatsApp com um botão para iniciar a integração.]({% image_buster /assets/img/whatsapp/whatsapp1.png %}){: style="max-width:80%;"}<br><br>
- Se estiver adicionando uma conta do WhatsApp Business a uma integração existente do WhatsApp, selecione **Adicionar conta do WhatsApp Business**. <br><br>\!["Integração de mensagens do WhatsApp" com opções para adicionar uma conta comercial do WhatsApp ou um grupo e número de assinatura.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %}){: style="max-width:80%;"}

O fluxo de trabalho a partir daqui é o mesmo para ambos os casos de uso.

## Fluxo de trabalho de inscrição incorporado ao WhatsApp

1. Na janela de login do Meta (Facebook), selecione **Login como** ou **Continuar**. <br><br>\![Meta janela de login.]({% image_buster /assets/img/whatsapp/login_screen.png %}){: style="max-width:60%;"}<br><br>
2. Leia as permissões que você compartilhará com o Braze e, em seguida, selecione **Get Started (Iniciar)**. <br><br>Lista de permissões que você compartilhará com o Braze para a integração.]({% image_buster /assets/img/whatsapp/get_started.png %}){: style="max-width:50%;"}<br><br>
3. No menu suspenso **Portfólio** de negócios, selecione seu portfólio de negócios e, em seguida, selecione **Avançar**. Isso se conecta à sua conta do WhatsApp Business, portanto, se você não vir o portfólio de negócios esperado, verifique suas permissões.<br><br>\![Uma janela com campos para inserir suas informações comerciais, incluindo o nome do portfólio comercial.]({% image_buster /assets/img/whatsapp/business_info.png %}){: style="max-width:50%;"}<br><br>
4. Selecione o seguinte para os campos suspensos e, em seguida, selecione **Next**.
- **Escolha uma conta do WhatsApp Business**: Criar uma conta comercial do WhatsApp
- **Crie ou selecione um perfil do WhatsApp Business**: Criar um novo perfil comercial no WhatsApp <br><br>\![Campos para especificar se você está escolhendo ou criando uma conta e um perfil do WhatsApp Business.]({% image_buster /assets/img/whatsapp/create_select_waba.png %}){: style="max-width:50%;"}<br><br>
5. Forneça os seguintes dados e selecione **Next**.
- Nome da conta comercial do WhatsApp
- Nome de exibição da empresa no WhatsApp
- Categoria <br><br>\![Campos para fornecer detalhes para a nova conta do WhatsApp Business.]({% image_buster /assets/img/whatsapp/waba_details.png %}){: style="max-width:50%;"}<br><br>
6. Digite seu número de telefone e escolha entre **Mensagem de texto** ou **Chamada telefônica**. Esse número deve atender a todos os requisitos de qualquer número de telefone do WhatsApp, inclusive não estar registrado em nenhuma outra conta do WhatsApp. <br><br>\![Campos para adicionar um número de telefone.]({% image_buster /assets/img/whatsapp/add_phone_number.png %}){: style="max-width:50%;"}<br><br>
7. Digite seu código de autenticação de dois fatores e selecione **Next (Avançar**). <br><br>\![Um campo de entrada para um código de autenticação de dois fatores.]({% image_buster /assets/img/whatsapp/two_factor.png %}){: style="max-width:50%;"}<br><br>
8. Revise as permissões que sua conta do WhatsApp Business receberá e, em seguida, selecione **Continuar**. <br><br>\![Lista de permissões solicitadas pela conta do WhatsApp Business.]({% image_buster /assets/img/whatsapp/permissions.png %}){: style="max-width:50%;"}<br><br>
9. Você está pronto! <br><br>Janela dizendo que você está pronto para começar a enviar mensagens para as pessoas.]({% image_buster /assets/img/whatsapp/finish.png %}){: style="max-width:50%;"}

