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

> Aproveite os sistemas avançados de IA do Meta para enviar suas mensagens de marketing para mais usuários que têm maior probabilidade de se envolver com elas, aumentando significativamente a capacidade de entrega e o envolvimento com as mensagens.

As mensagens do WhatsApp com entrega otimizada são enviadas usando a nova [API Marketing Messages Lite](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) da Meta, que oferece desempenho superior em comparação com a API tradicional da nuvem. Esse novo pipeline de envio ajuda você a alcançar melhor os usuários que valorizam e desejam receber suas mensagens.

Os benefícios do uso da entrega otimizada incluem:

- **Limites de mensagens dinâmicas:** A nova API oferece limites de mensagens mais dinâmicos por usuário, permitindo que mensagens de marketing de alto envolvimento (aquelas com maior probabilidade de serem lidas ou clicadas) alcancem mais usuários.
- **Capacidade de entrega otimizada:** Você pode esperar taxas de entrega mais baixas, mas taxas de envolvimento mais altas para as mensagens entregues, pois a IA avançada do Meta otimizará para os usuários que ele espera que valorizem e se envolvam com a mensagem. 
- **Resultados comprovados:** Na Índia, as mensagens identificadas como mais propensas a serem lidas ou clicadas tiveram até 9% mais mensagens entregues em comparação com o envio por meio da API da nuvem.
- **Entrega direcionada:** A IA avançada do Meta identifica mensagens de alto engajamento e as envia para mais usuários, permitindo que você envie a mensagem certa para mais pessoas certas no WhatsApp.

### Disponibilidade regional

A disponibilidade e os recursos de otimização da entrega otimizada dependem da região do número de telefone comercial e do usuário. Para saber mais, consulte [Disponibilidade geográfica de recursos](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features). 

## Configuração de entrega otimizada

1. No Braze, vá para **Partner Integrations** > **Technology Partners** > **WhatsApp**.
2. Na seção **Otimize seu envio com entrega otimizada**, selecione **a configuração Atualizar** para acionar o [fluxo de trabalho de inscrição incorporado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

A seção Integração de mensagens do WhatsApp com uma opção para otimizar o envio com entrega otimizada.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3\. Depois que a entrega otimizada for ativada, os detalhes de sua conta no **WhatsApp Business Account Management** exibirão o status da entrega otimizada.

Seção WhatsApp Business Account Management com um grupo de assinatura listado que tenha um status de número Ativo.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

Como alternativa, você pode ativar a entrega otimizada diretamente no gerenciador do WhatsApp e, em seguida, começar a enviar no Braze.

### Solução de problemas em sua configuração

- **Erro geral:** Se algo der errado durante a atualização, esse banner de erro será exibido e o aconselhará a entrar [em contato com o Suporte]({{site.baseurl}}/braze_support/).
- **Erro não elegível:** Se você estiver restrito pelo Meta, esse banner de erro será exibido: "Pelo menos uma conta do WhatsApp Business é restrita pela Meta. As contas devem estar em situação regular para fazer o upgrade." Isso não pode ser descartado até que o problema seja resolvido.

## Uso de entrega otimizada em campanhas e Canvases

A entrega otimizada deve ser usada para **mensagens de marketing**. O Braze removerá automaticamente a opção de entrega otimizada para **mensagens de utilidade, autenticação, serviço e resposta**, que devem continuar a ser enviadas por meio da API da nuvem, que é a configuração padrão. 

### Seleção do método de entrega

1. Na etapa de composição do Braze WhatsApp para uma campanha ou uma mensagem do Canvas, vá para a guia **Configurações**.
2. Na seção **Delivery method** **(** **Método de entrega** ), a caixa de seleção **Optimized Delivery (Recommended) (Entrega otimizada (Recomendada))** será marcada por padrão se a sua WhatsApp Business Account (WABA) estiver ativada. Se você não quiser usar a entrega otimizada para essa mensagem específica, desmarque a caixa de seleção.
- Se você selecionar a entrega otimizada, mas ela não estiver disponível, a mensagem voltará automaticamente para o método da API da nuvem.

Compositor de mensagens com uma guia de visualização que tem uma caixa de seleção para selecionar a entrega otimizada.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})