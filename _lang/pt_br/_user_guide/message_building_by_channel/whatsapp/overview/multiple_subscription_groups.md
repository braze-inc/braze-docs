---
nav_title: Várias contas comerciais 
article_title: Várias contas e números de telefone do WhatsApp Business
page_order: 2
description: "Este artigo de referência aborda as etapas para adicionar contas e números de telefone do WhatsApp Business."
page_type: reference
channel:
  - WhatsApp
---

# Várias contas e números de telefone do WhatsApp Business

> É possível adicionar várias contas do WhatsApp Business e grupos de inscrições (e números de telefone) a cada espaço de trabalho. <br><br>Cada grupo de inscrições está conectado a um único número de telefone, portanto, não é possível conectar o mesmo número de telefone a vários grupos de inscrições ou conectar vários números de telefone a um grupo de inscrições.

## Várias contas do WhatsApp Business 

Ter várias contas do WhatsApp Business é útil se você quiser enviar mensagens do WhatsApp para usuários em um espaço de trabalho do Braze que tenha várias marcas. Isso ocorre porque cada conta comercial opera separadamente no WhatsApp e tem seu próprio número de telefone, modelo de mensagem e classificação de qualidade.

As contas comerciais aninhadas no mesmo Meta Business Manager também compartilharão o gerenciamento de permissões de acesso do usuário e os catálogos (ainda não suportados da Braze).

![Diagrama do ecossistema Braze e WhatsApp, mostrando como os espaços de trabalho e contas do WhatsApp Business se conectam: você pode conectar um grupo de inscrições a um número de telefone, várias contas do WhatsApp Business a um espaço de trabalho e um espaço de trabalho a vários Portfólios de Negócios da Meta.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### Como adicionar uma conta do WhatsApp Business

Você pode adicionar até 10 contas do WhatsApp Business por espaço de trabalho. As contas comerciais podem ser aninhadas em diferentes Gerenciadores de Negócios da Meta. Para adicionar uma conta:

1. Acessar **Parceiros de Tecnologia** > **WhatsApp** e selecionar **Adicionar Conta do WhatsApp Business**. 

![Seção de Integração de Mensagens do WhatsApp com opções para adicionar uma conta comercial ou adicionar um grupo de inscrições e número.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. Acesse o fluxo de trabalho de inscrição. Para obter um passo a passo detalhado, consulte a [inscrição incorporada no WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

{% alert important %}
Seu número de telefone deve atender a todos os requisitos de qualquer número de telefone do WhatsApp, inclusive não estar registrado em nenhuma outra conta do WhatsApp.
{% endalert %}

## Vários grupos de inscrições e números de telefone

Os modelos de mensagens são compartilhados entre todos os números de telefone na mesma conta do WhatsApp Business. Para obter detalhes sobre os grupos de inscrições do WhatsApp, consulte [Grupos de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).

Cada número de telefone do WhatsApp aparecerá como um bate-papo separado do WhatsApp para os usuários. Cada número de telefone em uma conta do WhatsApp Business opera independentemente um do outro, portanto, eles podem ter os mesmos valores ou valores diferentes para o seguinte: 
- Nome de exibição 
- Status 
- Índice de qualidade 
- Limite de envio de mensagens 

### Adição de um grupo de inscrições e de um número de telefone

É possível adicionar até 20 grupos de inscrições (e enviar números de telefone) por conta do WhatsApp Business. Para adicionar um grupo de inscrições e um número de telefone:

1. Acessar **Parceiros de Tecnologia** > **WhatsApp** e selecionar **Adicionar Grupo de Inscrições e Número**.

![Seção de Integração de Mensagens do WhatsApp com opções para adicionar uma conta comercial ou adicionar um grupo de inscrições e número.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. Acesse o fluxo de trabalho de inscrição. <br><br> Na etapa **Select your WhatsApp Business Account (Selecione sua conta do** WhatsApp Business), selecione sua conta existente do WhatsApp Business e adicione um novo número de telefone. Esse número deve atender a todos os requisitos de qualquer número de telefone do WhatsApp, inclusive não estar registrado em nenhuma outra conta do WhatsApp.

### Remoção de um grupo de inscrições e de um número de telefone 

1. Acesse **Público** > **Inscrições** e arquive o grupo de inscrições.
2. Acesse o gerenciador do Meta Business e exclua o número de telefone.
