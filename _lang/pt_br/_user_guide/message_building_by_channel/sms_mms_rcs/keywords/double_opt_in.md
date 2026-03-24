---
nav_title: Aceitação dupla
article_title: Aceitação dupla
description: "Este artigo de referência cobre o recurso de dupla aceitação e explica como ativar o recurso, selecionar palavras-chave de aceitação e mensagens de resposta, e inserir usuários no fluxo de trabalho de dupla aceitação por meio de atualizações de inscrição que ocorrem nas atualizações da API REST, SDK e central de preferências."
page_type: reference
page_order: 2
channel:
  - SMS
  - MMS
  - RCS
---

# Aceitação dupla

> O recurso de dupla aceitação exige que os usuários confirmem explicitamente sua intenção de aceitação antes que possam receber mensagens SMS, MMS ou RCS. Isso foca o envio de mensagens em usuários engajados e apoia as melhores práticas de conformidade.

Quando a dupla aceitação está ativada, os usuários recebem uma mensagem que solicita seu consentimento explícito antes que possam ser contatados por suas campanhas ou canvases. 

Embora não seja um requisito explícito da Lei de Proteção ao Consumidor por Telefone de 1991 (TCPA), a Braze recomenda que você configure a dupla aceitação para confirmar que os usuários estão cientes e consentindo em fazer parte do seu programa de SMS, MMS ou RCS. Para mais informações sobre conformidade, veja [Leyes, regulamentos e prevenção de abusos para SMS, MMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

## Fluxos de trabalho de dupla aceitação

A dupla aceitação permite que você obtenha consentimento explícito por meio de campanhas de aceitação de entrada e saída.

### Saída

Quando um usuário fornece seu número de telefone, ele recebe uma mensagem que solicita seu consentimento.

![Captura de tela da mensagem SMS de saída com a marca enviando a seguinte mensagem: "Bem-vindo às atualizações de texto da MARCA! 1 mensagem por semana para as últimas ofertas. Responda Y para aceitar.", os usuários respondendo com "Y", e a marca respondendo com "Obrigado! Agora você está aceitando os alertas da marca. Aqui está um código promocional (SMS10) para ganhar 10% de desconto em sua primeira compra!"]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### Entrada

Quando um usuário envia uma mensagem que contém uma palavra-chave de aceitação, ele recebe uma mensagem que solicita seu consentimento.

![Captura de tela de mensagem SMS de entrada em que um usuário envia "JOIN" e recebe a resposta "Reply Y to confirm you want to JOIN our SMS program". 3msg/semana, envie uma mensagem de texto STOP a qualquer momento para interromper os envios e, em seguida, resonda com "Y".]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Ativando a dupla aceitação

Para ativar a dupla aceitação, acesse a tabela **Palavras-chave Globais** no grupo de inscrições aplicável e clique em **Editar** na **Categoria de Palavra-chave de Aceitação**. Em seguida, selecione seu método de aceitação**(Opt-In** ou **Double Opt-In**). A seleção de **Double Opt-In** expandirá a página para mostrar [campos configuráveis](#configurable-fields) adicionais.

![A seção Método de aceitação tem dois métodos de aceitação para escolher: Aceitação e Dupla Aceitação.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Campos configuráveis {#configurable-fields}

| Categoria   |    Campos    | Descrição   
| ----------- |----------- |---------------- 
| Pedido de aceitação | Palavras-chave | Essas são as palavras-chave que um usuário pode enviar por texto para indicar a intenção de aceitação. `START` é uma palavra-chave obrigatória. Esse pedido de aceitação também será enviado ao usuário quando o status da inscrição for atualizado pelas fontes listadas na seção [Fontes de inscrição](#subscription-sources).
| | Mensagem de resposta | Essa é a resposta inicial que um usuário receberá depois de enviar uma mensagem de texto com uma palavra-chave de aceitação (por exemplo, "Reply Y to confirm you want to receive messages from this number. Msg&Data As taxas podem ser aplicadas.” )
| Dupla confirmação de aceitação | Palavras-chave | Essas são as palavras-chave com as quais um usuário pode responder para confirmar sua intenção de aceitação. É necessário ter pelo menos uma palavra-chave. Essas palavras-chave devem ser especificadas no campo **Opt-In Prompt Reply Message**.
| | Mensagem de resposta | Esta é a resposta de confirmação que um usuário receberá após confirmar explicitamente sua aceitação e agora pode ser contatado. O status do grupo de inscrições do usuário será definido como `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário recebe um pedido de aceitação, ele tem 30 dias para confirmar sua intenção de aceitação. Se um usuário quiser se inscrever após a janela de 30 dias, ele precisará enviar uma palavra-chave de aceitação para iniciar novamente o fluxo de trabalho de dupla aceitação.

![Os campos configuráveis têm duas seções, Opt-In Prompt e Double Opt-In Confirmation, cada uma com os campos Keywords e Reply Message.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Status do grupo de inscrições

Somente após o usuário completar o fluxo de trabalho de dupla aceitação é que seu [status do grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/) é atualizado para `Subscribed`. Se o usuário iniciar o fluxo de trabalho, mas não o completar, ele permanece `Unsubscribed` e não pode receber mensagens desse grupo de inscrições.

Os usuários também podem ser inseridos no fluxo de trabalho de dupla aceitação se forem [inscritos de outras fontes]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (por exemplo, API REST, SDK).

## Fontes de inscrição {#subscription-sources}

Os usuários também podem entrar no fluxo de trabalho de dupla aceitação por meio de atualizações de inscrição que ocorrem fora das mensagens de entrada. Essas fontes incluem atualizações da API REST, do SDK e do centro de preferências. Quando um usuário entra no fluxo de trabalho de dupla aceitação por meio dessas fontes, ele receberá a **Mensagem de Resposta do Pedido de Aceitação**.

Cada fonte de inscrição tem um comportamento de registro diferente, conforme descrito na tabela a seguir.

Origem    | Comportamento de registro de aceitação dupla   
----------- | -----------
SDK | Os usuários entrarão automaticamente no fluxo de trabalho de dupla aceitação quando se inscreverem através do SDK da Braze.
API REST | Os usuários podem ser inseridos no fluxo de trabalho quando o status da inscrição é definido através de `/subscription/status/set`, `/v2/subscription/status/set` ou `/users/track` e o parâmetro opcional `use_double_opt_in_logic` é passado como `true` (por exemplo, [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "inscrito", "use_double_opt_in_logic": true}]). Se este parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de dupla aceitação.
Shopify | Os usuários não serão inseridos no fluxo de trabalho de dupla aceitação quando seu status de inscrição for definido pela nossa integração com Shopify.
Importação de usuários | Os usuários não serão inseridos no fluxo de trabalho de dupla aceitação quando seu status de inscrição for definido pela importação de usuário.
[Central de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | Os usuários entrarão automaticamente no fluxo de trabalho de dupla aceitação quando se inscreverem através de uma central de preferências.
Etapa de atualização de usuário | Os usuários podem ser inseridos no fluxo de trabalho de dupla aceitação quando seu status de inscrição é definido através da etapa de Atualização de Usuário e o parâmetro opcional `use_double_opt_in_logic` é passado como `true`. Se este parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de dupla aceitação.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Suporte multilíngue
Para mensagens de entrada, a dupla aceitação é suportada para todos os idiomas definidos no grupo de inscrições. Isso significa que você pode definir suas respostas automáticas em diferentes idiomas e o Braze enviará a resposta automática associada a um idioma específico quando uma palavra-chave correspondente for recebida.

Os usuários que entram no fluxo de trabalho de dupla aceitação através de atualizações de inscrição que ocorrem fora de mensagens de entrada (por exemplo, SDK, API REST, Shopify) receberão apenas as palavras-chave em inglês.

