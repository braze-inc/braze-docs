---
nav_title: Duplo opt-in
article_title: Dupla adesão
description: "Este artigo de referência aborda o recurso de opt-in duplo e explica como ativar o recurso, selecionar palavras-chave de opt-in e mensagens de resposta e inserir usuários no fluxo de trabalho de opt-in duplo por meio de atualizações de assinatura que ocorrem na API REST, SDK e atualizações do centro de preferências."
page_type: reference
page_order: 2
channel:
  - SMS
  - MMS
  - RCS
---

# Duplo opt-in

> O recurso de opt-in duplo permite que você exija que os usuários confirmem explicitamente sua intenção de opt-in antes de poderem receber mensagens SMS, MMS ou RCS. Isso o ajuda a adaptar seu foco aos usuários que provavelmente estarão envolvidos ou estão envolvidos com o canal e a seguir as práticas recomendadas de conformidade.

Quando o double opt-in está ativado, os usuários recebem uma mensagem que solicita seu consentimento explícito antes de receberem mensagens de suas campanhas ou Canvases. 

Embora não seja um requisito explícito da Lei de Proteção ao Consumidor de Telefone de 1991 (TCPA), a Braze recomenda que você configure o double opt-in para confirmar que os usuários estão cientes e consentem em fazer parte do seu programa de SMS, MMS ou RCS. Para obter mais informações sobre conformidade, consulte [Leis, regulamentos e prevenção de abuso para SMS, MMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

## Fluxos de trabalho de opt-in duplo

O opt-in duplo permite que você obtenha consentimento explícito por meio de campanhas de opt-in de entrada e saída.

### Saída

Quando um usuário fornece seu número de telefone, ele recebe uma mensagem que solicita seu consentimento.

Captura de tela da mensagem SMS de saída com a mensagem de texto da marca: "Welcome to BRAND text updates! 1 mensagem por semana para as últimas ofertas. Reply Y to opt-in.", os usuários respondendo com "Y", e a marca respondendo com "Thanks! Agora você optou por receber os alertas da BRAND. Aqui está um código promocional SMS10 para 10% de desconto em sua primeira compra!"]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### Inbound

Quando um usuário envia uma mensagem que contém uma palavra-chave opt-in, ele recebe uma mensagem que solicita seu consentimento.

Screenshot of inbound SMS message where a user sends "JOIN" and receives the response "Reply Y to confirm you want to JOIN our SMS program. 3msg/semana, envie uma mensagem de texto STOP a qualquer momento para STOP e, em seguida, envie a mensagem de texto de volta "Y".]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Ativação de double opt-in

Para ativar o opt-in duplo, vá para a tabela **Global Keywords (Palavras-chave globais** ) no grupo de assinatura aplicável e clique em **Edit (Editar** ) na **categoria Opt-In Keyword (Palavra-chave de opt-in**). Em seguida, selecione seu método de opt-in**(Opt-In** ou **Double Opt-In**). A seleção de **Double Opt-In** expandirá a página para mostrar [campos configuráveis](#configurable-fields) adicionais.

\![A seção Opt-In Method tem dois métodos de opt-in para escolher: Opt-In e Double Opt-In.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Campos configuráveis {#configurable-fields}

| Categoria   |    Campos    | Descrição   
| ----------- |----------- |---------------- 
| Prompt de adesão | Palavras-chave | Essas são as palavras-chave que um usuário pode enviar por texto para indicar a intenção de opt-in. `START` é uma palavra-chave obrigatória. Esse prompt de aceitação também será enviado ao usuário quando o status da assinatura for atualizado pelas fontes listadas na seção [Fontes de assinatura](#subscription-sources).
| | Mensagem de resposta | Essa é a resposta inicial que um usuário receberá depois de enviar uma mensagem de texto com uma palavra-chave de aceitação (por exemplo, "Reply Y to confirm you want to receive messages from this number. Msg&Data Podem ser aplicadas tarifas." )
| Confirmação de opt-in duplo | Palavras-chave | Essas são as palavras-chave com as quais um usuário pode responder para confirmar sua intenção de adesão. É necessário ter pelo menos uma palavra-chave. Essas palavras-chave devem ser especificadas no campo **Opt-In Prompt Reply Message**.
| | Mensagem de resposta | Essa é a resposta de confirmação que um usuário receberá depois de ter confirmado explicitamente sua adesão e agora pode receber mensagens. O status do grupo de assinatura do usuário será definido como `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário recebe um prompt de opt-in, ele tem 30 dias para confirmar sua intenção de opt-in. Se um usuário quiser se inscrever após a janela de 30 dias, ele precisará enviar uma palavra-chave de opt-in para iniciar novamente o fluxo de trabalho de opt-in duplo.

\![Os campos configuráveis têm duas seções, Opt-In Prompt e Double Opt-In Confirmation, cada uma com os campos Keywords e Reply Message.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Status do grupo de assinatura

Somente depois que o usuário concluir o fluxo de trabalho de opt-in duplo é que [o status do grupo de assinatura]({{site.baseurl}}/sms_rcs_subscription_groups/) será atualizado para `Subscribed`. Se o usuário iniciar o fluxo de trabalho, mas não o concluir, ele permanecerá em `Unsubscribed` e não poderá receber mensagens desse grupo de assinatura.

Os usuários também podem ser inseridos no fluxo de trabalho de opt-in duplo se estiverem [inscritos em outras fontes]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (por exemplo, API REST, SDK).

## Fontes de assinatura {#subscription-sources}

Os usuários também podem entrar no fluxo de trabalho de double opt-in por meio de atualizações de assinatura que ocorrem fora das mensagens de entrada. Essas fontes incluem atualizações da API REST, do SDK e do centro de preferências. Quando um usuário entra no fluxo de trabalho de opt-in duplo por meio dessas fontes, ele receberá a **mensagem de resposta do prompt de opt-in**.

Cada fonte de assinatura tem um comportamento de registro diferente, conforme descrito na tabela a seguir.

Fonte    | Comportamento de registro de opt-in duplo   
----------- | -----------
SDK | Os usuários entrarão automaticamente no fluxo de trabalho de double opt-in quando se inscreverem por meio do Braze SDK.
API REST | Os usuários podem ser inseridos no fluxo de trabalho quando o status da assinatura é definido por meio de `/subscription/status/set`, `/v2/subscription/status/set` ou `/users/track` e o parâmetro opcional `use_double_opt_in_logic` é passado como `true` (por exemplo, [{"subscription_group_id": "subscription_group_identifier", "subscription_state": "subscribed", "use_double_opt_in_logic": true}]). Se esse parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de opt-in duplo.
Shopify | Os usuários não serão inseridos no fluxo de trabalho de opt-in duplo quando seu status de assinatura for definido por nossa integração com o Shopify.
Importação do usuário | Os usuários não serão inseridos no fluxo de trabalho de opt-in duplo quando o status da assinatura for definido por User Import.
[Centro de preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | Os usuários entrarão automaticamente no fluxo de trabalho de adesão dupla quando se inscreverem por meio de um centro de preferências.
Etapa de atualização do usuário | Os usuários podem ser inseridos no fluxo de trabalho double opt-in quando seu status de assinatura é definido por meio da etapa Atualização do usuário e o parâmetro opcional `use_double_opt_in_logic` é passado como `true`. Se esse parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de opt-in duplo.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Suporte a vários idiomas
Para mensagens de entrada, o opt-in duplo é compatível com todos os idiomas definidos no grupo de assinatura. Isso significa que você pode definir suas respostas automáticas em diferentes idiomas e o Braze enviará a resposta automática associada a um idioma específico quando uma palavra-chave correspondente for recebida.

Os usuários que entrarem no fluxo de trabalho de opt-in duplo por meio de atualizações de assinatura que ocorrem fora das mensagens de entrada (por exemplo, SDK, API REST, Shopify) receberão apenas as palavras-chave em inglês.

