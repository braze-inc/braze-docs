---
nav_title: Mensagens do WhatsApp com entrega otimizada
article_title: Mensagens do WhatsApp com entrega otimizada
page_order: 1
description: "Este artigo de referência aborda as etapas envolvidas na construção e criação de uma mensagem do WhatsApp com entrega otimizada."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Mensagens do WhatsApp com entrega otimizada

> Aumente a entregabilidade e o engajamento alcançando mais usuários certos no WhatsApp com uma entrega dinâmica e baseada no engajamento.

As mensagens do WhatsApp com entrega otimizada são enviadas usando a [API de mensagens de marketing](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp) da Meta [para WhatsApp](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp) (MM API para WhatsApp), que oferece entrega dinâmica e baseada em engajamento. Isso significa que suas mensagens de alto engajamento (por exemplo, aquelas com maior probabilidade de serem lidas e clicadas) podem alcançar mais usuários que provavelmente se envolverão com elas. O WhatsApp considera suas mensagens de alto engajamento se elas forem esperadas, relevantes e oportunas e, portanto, mais propensas a serem lidas e clicadas. 

As marcas podem esperar uma entregabilidade igual ou maior com o MM API para WhatsApp, em comparação com o Cloud API. Na Índia, as mensagens de marketing com alto engajamento tiveram até 9% mais mensagens entregues em comparação com a Cloud API, de acordo com a Meta. Note que a API do MM para WhatsApp ainda não garante 100% de entregabilidade.

### Disponibilidade regional

A disponibilidade e os recursos de otimização da entrega otimizada dependem da região do número de telefone comercial e do usuário. Para saber mais, consulte [Disponibilidade geográfica de recursos](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features). 

## Configuração de entrega otimizada

1. No Braze, acesse **Partner Integrations** > **Technology Partners** > **WhatsApp**.
2. Na seção **Otimize seu envio com entrega otimizada**, selecione **a configuração Upgrade** para disparar o [fluxo de trabalho de inscrição incorporado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

![A seção Integração de mensagens do WhatsApp com uma opção para otimizar o envio com entrega otimizada.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3\. Depois que a capacitação da entrega otimizada for ativada, os detalhes de sua conta no **WhatsApp Business Account Management** exibirão o status da entrega otimizada.

![Seção Gerenciamento de contas do WhatsApp Business com um grupo de inscrições listado que tenha um status de número Ativo.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

Como alternativa, você pode ativar a entrega otimizada diretamente no gerenciador do WhatsApp e, em seguida, começar a enviar no Braze.

### Solução de problemas em sua configuração

- **Erro geral:** Se algo der errado durante o upgrade, este banner de erro será exibido e o aconselhará a entrar [em contato com o Suporte]({{site.baseurl}}/braze_support/).
- **Erro não elegível:** Se você estiver restrito pelo Meta, esse banner de erro será exibido: "Pelo menos uma conta do WhatsApp Business é restrita pela Meta. As contas devem estar em situação regular para fazer upgrade." Isso não pode ser descartado até que o problema seja resolvido.

## Uso de entrega otimizada em campanhas e telas

A entrega otimizada deve ser usada para **mensagens de marketing**. O Braze removerá automaticamente a opção de entrega otimizada para **mensagens de utilitário, autenticação, serviço e resposta**, que devem continuar a ser enviadas por meio da API da nuvem, que é a configuração padrão. 

### Seleção do método de entrega

1. Na etapa do criador de mensagens do Braze WhatsApp para uma campanha ou uma mensagem do Canva, vá para a guia **Configurações**.
2. Na seção **Método de entrega**, a caixa de seleção para **Entrega otimizada (Recomendada)** será marcada por padrão se a sua WhatsApp Business Account (WABA) estiver ativada. Se não quiser usar a entrega otimizada para essa mensagem específica, desmarque a caixa de seleção.
- Se você selecionar o envio otimizado, mas ele não estiver disponível, a mensagem voltará automaticamente para o método da API da nuvem.

![Criador de mensagens com uma guia prévia que tem uma caixa de seleção para selecionar a entrega otimizada.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})

### Redirecionamento de usuários em outros canais do Braze 

Como a MM API para WhatsApp não oferece 100% de entregabilidade, é importante entender como redirecionar os usuários que talvez não tenham recebido sua mensagem em outros canais. 

Para redirecionar os usuários, recomendamos criar um segmento de usuários que não receberam uma mensagem específica. Para fazer isso, filtre pelo código de erro `131049`, que indica que uma mensagem de modelo de marketing não foi enviada devido à aplicação do limite de modelo de marketing por usuário do WhatsApp. Você pode fazer isso usando o Braze Currents ou as extensões de segmento do SQL:

- **Braze Currents:** Exporte eventos de falha de mensagens usando o Braze Currents. Em seguida, é possível usar esses dados para atualizar um atributo personalizado no perfil do usuário (como `whatsapp_failed_last_msg: true`), que pode ser usado como um filtro para sua campanha de redirecionamento.
- **Extensões de segmento do SQL:** Se tiver acesso a esse recurso, poderá usar o SQL para consultar os registros de falhas de mensagens e criar um segmento desses usuários e, em seguida, direcionar esse segmento para um canal diferente.
