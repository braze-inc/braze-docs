---
nav_title: Aceitação dupla
article_title: Aceitação dupla
description: "Este artigo de referência aborda o recurso de aceitação dupla e explica como ativar o recurso, selecionar palavras-chave de aceitação e mensagens de resposta e inserir usuários no fluxo de trabalho de aceitação dupla por meio de atualizações de inscrição que ocorrem na API REST, no SDK e nas atualizações da Central de Preferências."
page_type: reference
page_order: 2
channel:
  - SMS
  - MMS
  - RCS
---

# Aceitação dupla

> O recurso de aceitação dupla permite exigir que os usuários confirmem explicitamente sua intenção de aceitação antes de receberem mensagens SMS, MMS ou RCS. Isso o ajuda a adaptar seu foco aos usuários que provavelmente estarão engajados ou estão engajados com o canal e a seguir as práticas recomendadas de conformidade.

Quando a aceitação dupla está ativada, os usuários recebem uma mensagem que solicita seu consentimento explícito antes de receberem mensagens de suas campanhas ou Canvas. 

Embora não seja um requisito explícito da Lei de Proteção ao Consumidor de Telefone de 1991 (TCPA), a Braze recomenda que você configure a aceitação dupla para confirmar que os usuários estão cientes e consentem em fazer parte do seu programa de SMS, MMS ou RCS. Para saber mais sobre conformidade, consulte [Leis, regulamentos e prevenção de abusos para SMS, MMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

## Fluxos de trabalho de aceitação dupla

O opt-in duplo permite que você obtenha consentimento explícito por meio de campanhas de aceitação de entrada e saída.

### Saída

Quando um usuário fornece seu número de telefone, ele recebe uma mensagem que solicita seu consentimento.

![Captura de tela da mensagem SMS de saída com a marca enviando a seguinte mensagem: "Bem-vindo às atualizações de texto da MARCA! 1 mensagem por semana para as últimas ofertas. Responda Y para aceitar.", os usuários respondendo com "Y", e a marca respondendo com "Obrigado! Agora você está aceitando os alertas da marca. Aqui está um código promocional SMS10 para 10% de desconto em sua primeira compra!"]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### Entrada

Quando um usuário envia uma mensagem que contém uma palavra-chave de aceitação, ele recebe uma mensagem que solicita seu consentimento.

![Captura de tela de mensagem SMS de entrada em que um usuário envia "JOIN" e recebe a resposta "Reply Y to confirm you want to JOIN our SMS program". 3msg/semana, envie uma mensagem de texto STOP a qualquer momento para STOP e, em seguida, envie a mensagem de texto de volta "Y".]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Ativando a aceitação dupla

Para ativar a aceitação dupla, acesse a tabela **Global Keywords (Palavras-chave globais** ) no grupo de inscrições aplicável e clique em **Edit (Editar** ) na **categoria Opt-In Keyword (Palavra-chave de aceitação**). Em seguida, selecione seu método de aceitação**(Opt-In** ou **Double Opt-In**). A seleção de **Double Opt-In** expandirá a página para mostrar [campos configuráveis](#configurable-fields) adicionais.

![A seção Método de aceitação tem dois métodos de aceitação para escolher: Aceitação e Dupla Aceitação.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Campos configuráveis {#configurable-fields}

| Categoria   |    Campos    | Descrição   
| ----------- |----------- |---------------- 
| Pedido de aceitação | Palavras-chave | Essas são as palavras-chave que um usuário pode enviar por texto para indicar a intenção de aceitação. `START` é uma palavra-chave obrigatória. Esse pedido de aceitação também será enviado ao usuário quando o status da inscrição for atualizado pelas fontes listadas na seção [Fontes de inscrição](#subscription-sources).
| | Mensagem de resposta | Essa é a resposta inicial que um usuário receberá depois de enviar uma mensagem de texto com uma palavra-chave de aceitação (por exemplo, "Reply Y to confirm you want to receive messages from this number. Podem ser aplicadas taxas de Msg&Data." )
| Dupla confirmação de aceitação | Palavras-chave | Essas são as palavras-chave com as quais um usuário pode responder para confirmar sua intenção de aceitação. É necessário ter pelo menos uma palavra-chave. Essas palavras-chave devem ser especificadas no campo **Opt-In Prompt Reply Message**.
| | Mensagem de resposta | Essa é a resposta de confirmação que um usuário receberá depois de ter confirmado explicitamente sua aceitação e agora pode receber mensagens. O status do grupo de inscrições do usuário será definido como `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário recebe um pedido de aceitação, ele tem 30 dias para confirmar sua intenção de aceitação. Se um usuário quiser se inscrever após a janela de 30 dias, ele precisará enviar uma palavra-chave de aceitação para iniciar novamente o fluxo de trabalho de dupla aceitação.

![Os campos configuráveis têm duas seções, Opt-In Prompt e Double Opt-In Confirmation, cada uma com os campos Keywords e Reply Message.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Status do grupo de inscrições

Somente depois que o usuário concluir o fluxo de trabalho de aceitação dupla, [o status do grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/) será atualizado para `Subscribed`. Se o usuário iniciar o fluxo de trabalho, mas não o concluir, ele permanecerá em `Unsubscribed` e não poderá receber mensagens desse grupo de inscrições.

Os usuários também podem ser inseridos no fluxo de trabalho de aceitação dupla se estiverem [inscritos em outras fontes]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (por exemplo, API REST, SDK).

## Fontes de inscrição {#subscription-sources}

Os usuários também podem entrar no fluxo de trabalho de aceitação dupla por meio de atualizações de inscrição que ocorrem fora das mensagens de entrada. Essas fontes incluem atualizações da API REST, do SDK e do centro de preferências. Quando um usuário entrar no fluxo de trabalho de aceitação dupla por meio dessas fontes, ele receberá a **mensagem de resposta do pedido de aceitação**.

Cada fonte de inscrição tem um comportamento de registro diferente, conforme descrito na tabela a seguir.

Origem    | Comportamento de registro de aceitação dupla   
----------- | -----------
SDK | Os usuários entrarão automaticamente no fluxo de trabalho de aceitação dupla quando se inscreverem por meio do Braze SDK.
API REST | Os usuários podem ser inseridos no fluxo de trabalho quando o status da inscrição é definido por meio de `/subscription/status/set`, `/v2/subscription/status/set` ou `/users/track` e o parâmetro opcional `use_double_opt_in_logic` é passado como `true` (por exemplo, [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). Se esse parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de aceitação dupla.
Shopify | Os usuários não serão inseridos no fluxo de trabalho de aceitação dupla quando o status da inscrição for definido por nossa integração com o Shopify.
Importação de usuários | Os usuários não serão inseridos no fluxo de trabalho de aceitação dupla quando seu status de inscrição for definido pela Importação de usuário.
[Central de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | Os usuários entrarão automaticamente no fluxo de trabalho de aceitação dupla quando se inscreverem por meio de uma Central de Preferências.
Etapa de atualização de usuário | Os usuários podem ser inseridos no fluxo de trabalho de aceitação dupla quando seu status de inscrição é definido por meio da etapa Atualização do usuário e o parâmetro opcional `use_double_opt_in_logic` é passado como `true`. Se esse parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de aceitação dupla.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Suporte multilíngue
Para mensagens de entrada, a aceitação dupla é compatível com todos os idiomas definidos no grupo de inscrições. Isso significa que você pode definir suas respostas automáticas em diferentes idiomas e o Braze enviará a resposta automática associada a um idioma específico quando uma palavra-chave correspondente for recebida.

Os usuários que entram no fluxo de trabalho de aceitação dupla por meio de atualizações de inscrição que ocorrem fora das mensagens de entrada (por exemplo, SDK, REST API, Shopify) receberão apenas as palavras-chave em inglês.

