---
nav_title: Acionadores de atributos
article_title: Acionadores de atributos
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Este artigo de referência apresenta uma visão geral dos acionadores de atributo e como você pode usá-los para enviar mensagens baseadas em ações aos usuários."
tool:
  - Campaigns

---

# Acionadores de atributos

> Os acionadores de atributos permitem o envio de mensagens baseadas em ações quando o estado da assinatura de um usuário ou os valores de atributos personalizados são alterados. 

Os acionadores de atributos estão disponíveis para os seguintes cenários:

- Atualizações do estado da assinatura.
- Os valores de atributos personalizados booleanos, inteiros, de cadeia de caracteres ou de data são alterados para qualquer valor.
- Os valores de atributos personalizados booleanos, inteiros ou de cadeia de caracteres são alterados para um valor específico.

Para começar a usar os acionadores de atributos, crie uma campanha ou um componente do Canvas e selecione **o Action-Based Delivery** como seu método de entrega. Em seguida, selecione o acionador de atributo que você gostaria de usar.

\!["Entrega baseada em ação" com um menu suspenso para selecionar um acionador.]({% image_buster /assets/img_archive/trigger_attribute.png %})

### Atualizar o status da assinatura

Use o acionador `Update Subscription Status` para direcionar os usuários quando o status da assinatura for atualizado. 

Por exemplo, você pode direcionar os usuários quando o status da assinatura de e-mail ou push deles mudar para opt-in e agradecê-los por isso. Você também pode enviar um webhook para seus sistemas sempre que um usuário cancelar a assinatura do e-mail, para que seus sistemas internos estejam atualizados com as informações mais recentes sobre o status da assinatura.

{% alert important %}
Esse acionador não se aplica quando um novo usuário é criado com o estado global de e-mail padrão de `subscribed` e há uma solicitação subsequente para atualizar o estado para `subscribed`, uma vez que o status da assinatura não foi alterado.
{% endalert %}

### Atualizar o status do grupo de assinaturas

Use o acionador `Update Subscription Group Status` para direcionar os usuários quando o status do grupo de assinatura de e-mail, SMS ou WhatsApp for atualizado. 

Por exemplo, você pode direcionar aos usuários uma mensagem SMS de boas-vindas quando eles optarem por participar do seu programa. Você também pode especificar a origem da atualização para ter um controle mais preciso sobre quando uma mensagem é disparada. 

As fontes de atualização disponíveis variam de acordo com o canal:
- Etapa de atualização do usuário do Canvas
- Importação de CSV
- Lista de cancelamento de inscrição
- Centro de preferências
- API REST
- SDK
- Shopify (e-mail, SMS)
- Mensagem de entrada (SMS)

Por exemplo, você pode querer enviar seu SMS de boas-vindas somente quando a atualização for proveniente da API REST e não de uma mensagem recebida, uma vez que o Braze já responde automaticamente a determinados SMS recebidos.

### Alterar o valor do atributo personalizado

Para o atributo de alteração, o acionador é avaliado primeiro e, em seguida, os critérios do público. Isso difere do comportamento padrão dos critérios de público-alvo avaliados primeiro e, depois, do acionador. Para evitar uma condição de corrida, verifique se o atributo usado como acionador não é o mesmo que o atributo usado para qualificar seu público.

#### Qualquer nova opção de valor

Use o acionador `Change Custom Attribute Value` com a opção `any new value` para direcionar os usuários quando um valor booleano, inteiro, de cadeia de caracteres ou de data for alterado para qualquer novo valor.

Por exemplo, direcione os usuários quando o número de pontos de recompensa mudar para informá-los sobre quantos pontos eles têm agora. Neste exemplo, digamos que um usuário tenha 85 pontos de recompensa e você tenha configurado uma campanha para ser acionada quando o atributo de ponto de recompensa for alterado para qualquer novo valor. Se o valor do atributo de ponto de recompensa desse usuário for alterado para qualquer novo valor (como 83, 84, 86 e assim por diante), a campanha será acionada.

Considere o próximo exemplo de caso de uso com uma notificação de atualização de camada. Talvez você queira alertar os usuários se o nível de recompensas deles mudar. Para realizar esse caso de uso, configure uma campanha que seja acionada em `Change Custom Attribute Value` e defina-a para ser acionada quando o atributo personalizado rewards tier for alterado para qualquer novo valor.

{% alert important %}
Os acionadores de atributos não estão disponíveis no momento para atributos de matriz.
{% endalert %}

\![Um acionador "Change Custom Attribute Value" (Alterar valor de atributo personalizado) para o "AA_current_rewards_tier" mudar para qualquer valor.]({% image_buster /assets/img_archive/any_value.png %})

Você também pode usar o Liquid para personalizar o corpo da mensagem com o novo nível de prêmios do cliente e fornecer a ele mais informações sobre a alteração.

{% raw %}
```liquid
Your rewards tier was just changed to {{custom_attribute.${AA_current_rewards_tier}}}
```
{% endraw %}

#### Valor específico

Use o acionador `Change Custom Attribute Value` com a opção `specific value` para direcionar os usuários quando um atributo personalizado booleano, inteiro ou de cadeia de caracteres for alterado para um valor específico. 

Por exemplo, direcione os usuários quando o nível de recompensas deles mudar para o melhor nível. Para este exemplo, digamos que o melhor nível de prêmios seja o Super VIP. Você pode configurar uma campanha para ser acionada quando o atributo personalizado de nível de recompensa de um usuário for alterado para `Super VIP`, para que você possa parabenizar o usuário por se tornar um Super VIP.

\![Um acionador "Change Custom Attribute Value" (Alterar valor de atributo personalizado) para o "AA_current_rewards_tier" mudando para o valor específico de "super vip".]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Os acionadores de atributo para valores específicos de atributos personalizados não estão disponíveis para atributos personalizados de matriz e data.
- O acionador de alteração de valores de atributos personalizados não é acionado quando o valor do atributo personalizado é atualizado para nulo.  
- O acionador de alteração de valores de atributos personalizados só será acionado quando o valor de um atributo personalizado for alterado. Se o valor atual de um atributo personalizado for reenviado para o Braze (e.g o valor do atributo de cor favorita é vermelho e você reenvia o valor vermelho para o Braze), o acionador de alteração dos valores do atributo personalizado não ocorrerá.
- O acionador de alteração de valores de atributos personalizados também se aplica a novos usuários criados.
{% endalert %}

