---
nav_title: Disparos de atribuição
article_title: Disparos de atribuição
page_order: 1
alias: /attribute_triggers/
page_type: reference
description: "Este artigo de referência oferece uma visão geral dos disparadores de atribuição e como usá-los para enviar mensagens baseadas em ações aos usuários."
tool:
  - Campaigns

---

# Disparos de atribuições

> Os disparadores de atributos permitem o envio de mensagens baseadas em ações quando o estado da inscrição de um usuário ou os valores de atributos personalizados mudam. 

Os disparadores de atribuição estão disponíveis para os seguintes cenários:

- Atualizações do estado da inscrição.
- Os valores dos atributos personalizados booleano, inteiro, string ou data são alterados para qualquer valor.
- Os valores dos atributos personalizados booleanos, inteiros ou de string são alterados para um valor específico.

Para começar a usar os disparos de atribuição, crie uma campanha ou um componente do Canvas e selecione **Entrega baseada em ação** como seu método de entrega. Em seguida, selecione o disparador de atribuição que você gostaria de usar.

![]({% image_buster /assets/img_archive/trigger_attribute.png %})

### Atualizar o status da inscrição

Use o disparador `Update Subscription Status` para direcionar os usuários quando o status da inscrição deles for atualizado. 

Por exemplo, é possível direcionar os usuários quando o status da inscrição por e-mail ou push deles mudar para aceitação e agradecê-los por isso. Também é possível enviar um webhook para seus sistemas sempre que um usuário cancelar inscrição de e-mail, para que seus sistemas internos estejam atualizados com as informações mais recentes sobre o status da inscrição.

{% alert important %}
Esse disparo não se aplica quando um novo usuário é criado com o estado global de e-mail padrão de `subscribed` e há uma solicitação subsequente para atualizar o estado para `subscribed`, uma vez que o status da inscrição não foi alterado.
{% endalert %}

### Atualizar o status do grupo de inscrições

Use o disparador `Update Subscription Group Status` para direcionar os usuários quando o status do grupo de inscrições para e-mail, SMS ou WhatsApp for atualizado. 

Por exemplo, é possível direcionar aos usuários uma mensagem SMS de boas-vindas quando eles aceitarem participar do seu programa. Também é possível especificar a origem da atualização para ter um controle mais preciso sobre quando uma mensagem é disparada. 

As fontes de atualização disponíveis variam de acordo com o canal:
- Importação de CSV
- Central de Preferências
- API REST
- SDK
- Shopify (e-mail, SMS)
- Envio de mensagens (SMS)

Por exemplo, talvez você queira enviar seu SMS de boas-vindas somente quando a atualização vier da API REST e não de uma mensagem recebida, já que o Braze já responde automaticamente a determinados SMS recebidos.

### Alterar o valor do atributo personalizado

Para atribuição de alteração, o disparador é avaliado primeiro e, em seguida, os critérios do público. Isso difere do comportamento padrão dos critérios de público avaliados primeiro e depois disparados. Para evitar uma condição de corrida, certifique-se de que o atributo usado como disparador não seja o mesmo que o atributo usado para qualificar seu público.

#### Qualquer nova opção de valor

Use o disparador `Change Custom Attribute Value` com a opção `any new value` para direcionar os usuários quando um valor booleano, inteiro, string ou data for alterado para qualquer novo valor.

Por exemplo, direcione os usuários quando o número de pontos de fidelidade mudar para que eles saibam quantos pontos têm agora. Neste exemplo, digamos que um usuário tenha 85 pontos de fidelidade e você tenha configurado uma campanha para disparar quando a atribuição do ponto de fidelidade for alterada para qualquer novo valor. Se o valor da atribuição do ponto de fidelidade desse usuário mudar para qualquer novo valor (e.g 83, 84, 86, etc.), a campanha será disparada.

Considere o próximo exemplo de caso de uso com uma notificação de atualização de camada. Talvez queira alertar os usuários se o nível de fidelidade deles mudar. Para realizar esse caso de uso, configure uma campanha que seja disparada pelo site `Change Custom Attribute Value` e defina-a para ser disparada quando o atributo personalizado fidelidade mudar para qualquer novo valor.

{% alert important %}
Os disparadores de atributos não estão disponíveis atualmente para atributos de matriz.
{% endalert %}

![Qualquer novo valor]({% image_buster /assets/img_archive/any_value.png %})

Você também pode usar o Liquid para personalizar o corpo da mensagem com o novo nível de fidelidade do cliente e fornecer a ele mais informações sobre a mudança.

{% raw %}
```liquid
Your loyalty tier was just changed to {{custom_attribute.${loyalty_tier}}}
```
{% endraw %}

#### Valor específico

Use o disparador `Change Custom Attribute Value` com a opção `specific value` para direcionar os usuários quando um atributo personalizado booleano, inteiro ou string for alterado para um valor específico. 

Por exemplo, direcione os usuários quando o nível de fidelidade deles mudar para o melhor nível. Para este exemplo, digamos que o melhor nível de fidelidade seja o Super VIP. É possível configurar uma campanha para disparar quando o atributo personalizado de nível de fidelidade de um usuário mudar para `Super VIP`, para que você possa parabenizar o usuário por se tornar um Super VIP.

![]({% image_buster /assets/img_archive/super_vip.png %})

{% alert important %}
- Os disparadores de atributos para valores específicos de atributos personalizados não estão disponíveis para atributos personalizados de matriz e data.
- O acionador de alteração de valores de atributos personalizados não é disparado quando o valor do atributo personalizado é atualizado para nulo.  
- O acionador de alteração de valores de atributos personalizados somente será disparado quando o valor de um atributo personalizado for alterado. Se o valor atual de um atributo personalizado for reenviado ao Braze (e.g o valor do atributo de cor favorita é vermelho e você reenvia o valor vermelho ao Braze), o disparo de alteração dos valores do atributo personalizado não ocorrerá.
- O disparo de alteração de valores de atributos personalizados também se aplica a novos usuários criados.
{% endalert %}

