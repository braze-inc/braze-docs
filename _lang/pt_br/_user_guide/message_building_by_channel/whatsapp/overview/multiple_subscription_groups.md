---
nav_title: Várias contas comerciais
article_title: Várias contas comerciais e números de telefone do WhatsApp
page_order: 2
description: "Este artigo de referência aborda as etapas para adicionar contas e números de telefone do WhatsApp Business."
page_type: reference
channel:
  - WhatsApp
---

# Várias contas e números de telefone do WhatsApp Business

> Você pode adicionar várias contas do WhatsApp Business e grupos de assinatura (e números de telefone) a cada espaço de trabalho. <br><br>Cada grupo de assinatura é conectado a um único número de telefone, portanto, não é possível conectar o mesmo número de telefone a vários grupos de assinatura ou conectar vários números de telefone a um grupo de assinatura.

## Várias contas do WhatsApp Business 

Ter várias contas do WhatsApp Business é útil se você quiser enviar mensagens do WhatsApp para usuários em um espaço de trabalho do Braze que tenha várias marcas. Isso ocorre porque cada conta comercial opera separadamente no WhatsApp e tem seu próprio número de telefone, modelo de mensagem e classificação de qualidade.

As contas comerciais aninhadas no mesmo Meta Business Manager também compartilharão o gerenciamento de permissões de acesso do usuário e os catálogos (ainda não suportados no Braze).

Diagrama do ecossistema Braze e WhatsApp, mostrando como os espaços de trabalho e as contas do WhatsApp Business se conectam entre si: você pode conectar um grupo de assinatura a um número de telefone, várias contas do WhatsApp Business a um espaço de trabalho e um espaço de trabalho a vários portfólios do Meta Business.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### Como adicionar uma conta do WhatsApp Business

Você pode adicionar até 10 contas do WhatsApp Business por espaço de trabalho. As contas comerciais podem ser aninhadas em diferentes Meta Business Managers. Para adicionar uma conta:

1. Vá para **Technology Partners** > **WhatsApp** e selecione **Add WhatsApp Business Account**. 

Seção Integração de mensagens do WhatsApp com opções para adicionar uma conta comercial ou adicionar um grupo e um número de assinatura.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. Percorra o fluxo de trabalho de registro. Para obter um passo a passo detalhado, consulte a [inscrição incorporada no WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

{% alert important %}
Seu número de telefone deve atender a todos os requisitos de qualquer número de telefone do WhatsApp, inclusive não estar registrado em nenhuma outra conta do WhatsApp.
{% endalert %}

## Vários grupos de assinatura e números de telefone

Os modelos de mensagens são compartilhados entre todos os números de telefone da mesma conta do WhatsApp Business. Para obter detalhes sobre os grupos de assinatura do WhatsApp, consulte [Grupos de assinatura]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).

Cada número de telefone do WhatsApp aparecerá como um bate-papo separado do WhatsApp para os usuários. Cada número de telefone em uma conta do WhatsApp Business opera independentemente um do outro, portanto, eles podem ter os mesmos valores ou valores diferentes para o seguinte: 
- Nome de exibição 
- Status 
- Índice de qualidade 
- Limite de mensagens 

### Adição de um grupo de assinaturas e de um número de telefone

Você pode adicionar até 20 grupos de assinatura (e números de telefone de envio) por conta do WhatsApp Business. Para adicionar um grupo de assinatura e um número de telefone:

1. Vá para **Technology Partners** > **WhatsApp** e selecione **Add Subscription Group and Number**.

Seção Integração de mensagens do WhatsApp com opções para adicionar uma conta comercial ou adicionar um grupo e um número de assinatura.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. Percorra o fluxo de trabalho de registro. <br><br> Na etapa **Select your WhatsApp Business Account (Selecione sua conta do** WhatsApp Business), selecione sua conta existente do WhatsApp Business e adicione um novo número de telefone. Esse número deve atender a todos os requisitos de qualquer número de telefone do WhatsApp, inclusive não estar registrado em nenhuma outra conta do WhatsApp.

### Remoção de um grupo de assinaturas e de um número de telefone 

1. Acesse **Audience** > **Subscriptions** ( **Público** > **Assinaturas** ) e arquive o grupo de assinaturas.
2. Vá para o gerenciador do Meta Business e exclua o número de telefone.
