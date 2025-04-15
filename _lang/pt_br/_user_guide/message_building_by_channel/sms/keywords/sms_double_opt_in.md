---
nav_title: Dupla aceitação de SMS
article_title: Dupla aceitação de SMS
description: "Este artigo de referência aborda o recurso de dupla aceitação de SMS e explica como ativar o recurso, selecionar palavras-chave de aceitação e mensagens de resposta e inserir usuários no fluxo de trabalho de dupla aceitação de SMS por meio de atualizações de inscrição que ocorrem na API REST, no SDK e nas atualizações da Central de Preferências."
page_type: reference
page_order: 2
channel:
  - SMS
---

# Aceitação dupla de SMS

> O recurso de dupla aceitação de SMS permite exigir que os usuários confirmem explicitamente sua intenção de aceitação antes de receberem mensagens SMS. Isso o ajuda a adaptar seu foco aos usuários que provavelmente estarão engajados ou que estão engajados com o SMS.

Quando a aceitação dupla de SMS está ativada, os usuários recebem uma mensagem SMS que solicita seu consentimento explícito antes do envio de mensagens por suas campanhas ou Canvas. 

Embora não seja um requisito explícito da Lei de Proteção ao Consumidor de Telefone de 1991 (TCPA), a Braze recomenda configurar a aceitação dupla de SMS para confirmar que os usuários estão cientes e consentem em fazer parte do seu programa de SMS. Para saber mais sobre a conformidade com SMS, consulte [as leis, os regulamentos e a prevenção de abuso de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/).

## Fluxos de trabalho de aceitação dupla de SMS

Os usuários podem fornecer seu consentimento explícito por meio de mensagens SMS enviadas ou recebidas.

### Dupla aceitação de SMS de saída

Quando um usuário fornece seu número de telefone, ele recebe uma mensagem SMS que solicita seu consentimento.

![Captura de tela da mensagem SMS de saída com a marca enviando a seguinte mensagem: "Bem-vindo às atualizações de texto da MARCA! 1 mensagem por semana para as últimas ofertas. Responda Y para aceitar.", os usuários respondendo com "Y", e a marca respondendo com "Obrigado! Agora você está aceitando os alertas da marca. Aqui está um código promocional (SMS10) para ganhar 10% de desconto em sua primeira compra!"][2]{:style="max-width:40%;"}

### Dupla aceitação de SMS de entrada

Quando um usuário envia uma mensagem SMS que contém uma palavra-chave de aceitação, ele recebe uma mensagem SMS que solicita seu consentimento.

![Captura de tela de mensagem SMS de entrada em que um usuário envia "JOIN" e recebe a resposta "Reply Y to confirm you want to JOIN our SMS program". 3msg/semana, envie uma mensagem de texto STOP a qualquer momento para interromper os envios e, em seguida, resonda com "Y".][1]{:style="max-width:40%;"}

## Ativando a aceitação dupla de SMS

Para ativar a aceitação dupla de SMS, navegue até a tabela **SMS Global Keywords (Palavras-chave globais de SMS** ) no grupo de inscrições aplicável e clique em **Edit (Editar** ) na **categoria Opt-In Keyword (Palavra-chave de aceitação**). Em seguida, selecione seu método de aceitação**(Opt-In** ou **Double Opt-In**). A seleção de **Double Opt-In** expandirá a página para mostrar [campos configuráveis](#configurable-fields) adicionais.

![A seção Método de aceitação tem dois métodos de aceitação para escolher: Aceitação e Dupla Aceitação.][3]{:style="max-width:50%;"}

### Campos configuráveis {#configurable-fields}

| Categoria   |    Campos    | Descrição   
| ----------- |----------- |---------------- 
| Pedido de aceitação | Palavras-chave | Essas são as palavras-chave que um usuário pode enviar por texto para indicar a intenção de aceitação. `START` é uma palavra-chave obrigatória. Esse pedido de aceitação também será enviado ao usuário quando o status da inscrição for atualizado pelas fontes listadas na seção [Fontes de inscrição](#subscription-sources).
| | Mensagem de resposta | Essa é a resposta inicial que um usuário receberá depois de enviar uma mensagem de texto com uma palavra-chave de aceitação (por exemplo, "Reply Y to confirm you want to receive messages from this number. Podem ser aplicadas taxas de Msg&Data." )
| Dupla confirmação de aceitação | Palavras-chave | Essas são as palavras-chave com as quais um usuário pode responder para confirmar sua intenção de aceitação. É necessário ter pelo menos uma palavra-chave. Essas palavras-chave devem ser especificadas no campo **Opt-In Prompt Reply Message**.
| | Mensagem de resposta | Essa é a resposta de confirmação que o usuário receberá depois de ter confirmado explicitamente sua aceitação e agora pode receber envios de mensagens por SMS. O status do grupo de inscrições do usuário será definido como `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Quando um usuário recebe um pedido de aceitação, ele tem 30 dias para confirmar sua intenção de aceitação. Se um usuário quiser se inscrever após a janela de 30 dias, ele precisará enviar uma palavra-chave de aceitação para iniciar novamente o fluxo de trabalho de dupla aceitação.

![Os campos configuráveis têm duas seções, Opt-In Prompt e Double Opt-In Confirmation, cada uma com os campos Keywords e Reply Message.][4]

## Status do grupo de inscrições

Somente depois que o usuário concluir o fluxo de trabalho de aceitação dupla do SMS, [o status do grupo de inscrições]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) será atualizado para `Subscribed`. Se o usuário iniciar o fluxo de trabalho, mas não o concluir, ele permanecerá em `Unsubscribed` e não poderá receber mensagens SMS desse grupo de inscrições.

Os usuários também podem ser inseridos no fluxo de trabalho de aceitação dupla de SMS se estiverem [inscritos em outras fontes]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group#how-users-sms-subscription-groups-get-set) (por exemplo, API REST, SDK).

## Fontes de inscrição {#subscription-sources}

Os usuários também podem entrar no fluxo de trabalho de aceitação dupla de SMS por meio de atualizações de inscrição que ocorrem fora das mensagens SMS recebidas. Essas fontes incluem atualizações da API REST, do SDK e do centro de preferências. Quando um usuário entrar no fluxo de trabalho de dupla aceitação de SMS por meio dessas fontes, ele receberá a **mensagem de resposta do pedido de aceitação**.

Cada fonte de inscrição tem um comportamento de registro diferente, conforme descrito na tabela a seguir.

Origem    | Comportamento de registro de aceitação dupla   
----------- | -----------
SDK | Os usuários entrarão automaticamente no fluxo de trabalho de aceitação dupla de SMS quando se inscreverem por meio do SDK da Braze.
API REST | Os usuários podem ser inseridos no fluxo de trabalho quando o status da inscrição é definido por meio de `/subscription/status/set`, `/v2/subscription/status/set` ou `/users/track` e o parâmetro opcional `use_double_opt_in_logic` é passado como `true` (por exemplo, [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). Se esse parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de aceitação dupla de SMS.
Shopify | Os usuários não serão inseridos no fluxo de trabalho de aceitação dupla de SMS quando o status da inscrição for definido por nossa integração com o Shopify.
Importação de usuários | Os usuários não serão inseridos no fluxo de trabalho de aceitação dupla de SMS quando o status da inscrição for definido pela importação de usuários.
[Central de Preferências]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center) | Os usuários entrarão automaticamente no fluxo de trabalho de aceitação dupla de SMS quando se inscreverem por meio de uma Central de Preferências.
Etapa de atualização de usuário | Os usuários podem ser inseridos no fluxo de trabalho de aceitação dupla de SMS quando seu status de inscrição é definido por meio da etapa Atualização do usuário e o parâmetro opcional `use_double_opt_in_logic` é passado como `true`. Se esse parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de aceitação dupla de SMS.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Suporte multilíngue
Para mensagens de entrada, a aceitação dupla de SMS é compatível com todos os idiomas definidos no grupo de inscrições. Isso significa que você pode definir suas respostas automáticas em diferentes idiomas e o Braze enviará a resposta automática associada a um idioma específico quando uma palavra-chave correspondente for recebida.

Os usuários que entram no fluxo de trabalho de aceitação dupla de SMS por meio de atualizações de inscrição que ocorrem fora das mensagens de entrada (por exemplo, SDK, REST API, Shopify) receberão apenas as palavras-chave em inglês.

[1]: {% image_buster /assets/img/double_opt_in_inbound.png %}
[2]: {% image_buster /assets/img/double_opt_in_outbound.png %}
[3]: {% image_buster /assets/img/double_opt_in_method.png %}
[4]: {% image_buster /assets/img/double_opt_in_fields.png %}
