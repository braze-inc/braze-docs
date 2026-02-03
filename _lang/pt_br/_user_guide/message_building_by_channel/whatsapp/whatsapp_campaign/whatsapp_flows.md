---
nav_title: WhatsApp Flows
article_title: WhatsApp Flows
page_order: 1
description: "Este artigo de referência aborda as etapas envolvidas na construção e criação de uma mensagem do WhatsApp Flows."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# WhatsApp Flows

> O WhatsApp Flows é um aprimoramento do canal existente do WhatsApp, que permite criar experiências de envio de mensagens interativas e dinâmicas. Esta página fornece instruções passo a passo para usar o WhatsApp Flows.

## Configuração dos fluxos do WhatsApp

1. Faça o registro em sua conta Meta.
2. Crie fluxos em um dos dois locais principais:
    - **Ferramentas de conta:** Acesse a guia **Flows (Fluxos** ) para visualizar o ID do fluxo e criar um novo fluxo.
    - **Gerenciar modelos:** Esse é o método recomendado para a criação de fluxos. Aqui, você pode gerar modelos e selecionar uma opção de fluxo durante o processo de criação de modelos.

![WhatsApp Manager com uma página para criar um modelo de Flows.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\. Selecione um fluxo existente ou crie um. Se estiver criando um fluxo, escolha entre duas opções:
  - **Formulário personalizado:** Para requisitos específicos
  - **Elementos pré-projetados:** Para uma configuração mais rápida

## Configuração das mensagens e respostas do WhatsApp Flow

{% tabs local %}
{% tab Template message %}

1. Em um Braze Canvas, crie uma etapa de mensagem do WhatsApp que use o modelo de mensagem que contém o respectivo Flow.
2. Continue criando seu modelo. Se necessário, adicione mídia, conteúdo variável ou ambos à sua mensagem. Sua seleção de fluxo foi escolhida quando o modelo foi criado, portanto, não são necessárias informações adicionais para a experiência de fluxo.

![Criador de mensagens do WhatsApp usando um modelo do WhatsApp Flow.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Em um Braze Canvas, crie uma etapa de mensagem do WhatsApp que use uma mensagem de resposta e uma mensagem de fluxo.

![Uma etapa de mensagem para um tipo de mensagem de resposta do WhatsApp e layout de mensagem de fluxo.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Selecione o respectivo fluxo e continue criando sua mensagem. 

![Um criador de resposta de mensagem de fluxo com um menu suspenso estendido para selecionar um fluxo.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Prévia do Flow

Antes de iniciar um Canvas Flow com um fluxo, você pode selecionar **Preview Flow** para fazer uma prévia do fluxo diretamente no Braze e confirmar que ele se comporta como esperado. Também é possível interagir com o fluxo na prévia para experimentar como um usuário navegaria no fluxo e, em seguida, fazer ajustes em tempo real. Se um fluxo contiver várias páginas, você poderá interagir com cada página.

![Janela prévia exibindo um formulário para que o usuário termine de inscrever-se.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Salvando a resposta completa do Flow {#full-flow}

Ao incorporar uma mensagem do WhatsApp Flow a um Braze Canvas ou a uma campanha, talvez você queira capturar e utilizar informações específicas que os usuários enviam por meio do Flow. O Braze precisa receber informações adicionais sobre a estrutura da resposta do usuário, especificamente a forma esperada da resposta JSON, para gerar o esquema de atributo personalizado aninhado (NCA) necessário.

### Etapa 1: Gerar o atributo personalizado Flow

{% tabs local %}
{% tab Recommended method %}

A maneira mais simples de fornecer ao Braze as informações sobre a estrutura da resposta é salvar a resposta do fluxo como um atributo personalizado e concluir um teste de envio.

#### Usar um fluxo que não tenha sido usado no Braze

Se você estiver usando um fluxo que não tenha sido usado anteriormente no Braze, ao visualizar a seção **Atributo personalizado do fluxo** no **criador de mensagens**, talvez não veja nenhuma informação. Isso significa que o esquema ainda não foi gerado.

![Seção Meta Flow com uma opção para visualizar o atributo personalizado Flow.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Para resolver isso, faça o seguinte:

1. Conclua a etapa de configuração de suas mensagens do WhatsApp.
2. Confirme que você marcou **Salvar respostas de fluxo como um atributo personalizado**.

![Seção Meta Flow com uma caixa de seleção para salvar as respostas do Flow como um atributo personalizado.]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3\. Envie a si mesmo uma mensagem de teste e conclua o Flow como usuário.

Agora, o Braze tem a forma do JSON da resposta do Flow e pode gerar o atributo personalizado.

{% endtab %}
{% tab Alternative methods %}

Use o editor JSON avançado para salvar atribuições da resposta do Flow em atributos personalizados ou use um Canvas de várias etapas para salvar a resposta em um atributo personalizado aninhado. 

{% subtabs %}
{% subtab Advanced JSON editor %}

No editor JSON avançado, digite {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, em que “flow_1” é o atributo personalizado no qual você gostaria que o fluxo fosse salvo.

![Etapa de atualização do usuário com um editor JSON avançado.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. Confirme que você já criou um atributo personalizado com o tipo de dados do objeto ("flow_1" (neste exemplo) dentro das configurações de dados do espaço de trabalho.
2. No editor de interface do usuário, use o Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}``` para preencher o atributo personalizado e salvar toda a resposta de fluxo do usuário nele. É necessário preencher o valor da chave como ```{{whats_app.${inbound_flow_response}}}```{% endraw %} antes de selecionar o atributo personalizado que você criou.

![Etapa de atualização do usuário que usa o editor da interface do usuário.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Depois que o Braze receber uma resposta do Flow, salvaremos o atributo personalizado aninhado com a nomenclatura prescrita no perfil do usuário. Esse atributo personalizado pode ser obtido ao criar Canvas. 

![Uma janela que exibe o conteúdo de um atributo personalizado do site "flow_1".]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Etapa 2: Exibir a resposta de fluxo salva

Quando o fluxo é concluído, o Braze cria automaticamente um atributo personalizado do fluxo com um nome baseado no ID do fluxo. Em seguida, acesse o perfil do usuário para visualizar a resposta de fluxo salva como um objeto aninhado na seção **Atributos personalizados**.

Após a geração do esquema, a seção **Atributo personalizado** de fluxo exibirá a estrutura esperada, incluindo os tipos de dados previstos para cada resposta (por exemplo, "String" ou "String Array").

![Janela de detalhes de atributos personalizados de fluxo com menu suspenso de esquema.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Considerações

- **Atribuições existentes:** Se um atributo personalizado para um determinado fluxo já tiver sido gerado, o fluxo será carregado com as informações de atributo disponíveis. Nesses casos, não é necessário enviar uma mensagem de teste para gerar o esquema, pois o Braze já reconhece as mensagens de resposta esperadas.
- **Mudanças de fluxo:** Se você fizer alguma alteração no fluxo após a geração do esquema, deverá enviar uma mensagem de teste adicional para que o Braze possa entender que a forma da resposta do fluxo foi alterada e ajustar a estrutura de atribuições de acordo. Essa ação é limitada a uma vez a cada 24 horas. 
- **Consistência:** O atributo personalizado do fluxo gerado é consistente e será o mesmo atributo para esse fluxo específico, independentemente da tela em que for usado.
- **Opção manual:** Não é necessário marcar a caixa de seleção **Salvar respostas de fluxo como um atributo personalizado**. É possível gerar manualmente o atributo personalizado [salvando campos específicos das respostas do fluxo em um atributo personalizado específico](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), o que evita a duplicação das etapas do usuário.

## Salvar campos específicos das respostas do Flow em um atributo personalizado específico 

### Etapa 1: Criar uma jornada de ação

Crie uma etapa do canva do [Action Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) ou uma campanha baseada em ações. Selecione um disparador **Enviar uma mensagem de entrada do WhatsApp** e a condição **Fluxo respondido** e, em seguida, selecione o fluxo relevante ou **Qualquer fluxo**.

![Um disparo para usuários que enviaram uma mensagem de entrada do WhatsApp e responderam a qualquer Flow.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Etapa 2: Extrair campos das respostas do Flow

Você pode usar atributos personalizados aninhados ou a tag `json_parse` Liquid para extrair campos específicos das respostas do Flow.

{% tabs %}
{% tab Nested custom attributes %}

Para salvar partes específicas da resposta do usuário ao Flow, conclua todas as etapas de [Como salvar a resposta completa ao Flow](#full-flow), **incluindo o lançamento do Canvas**. O Canva deve ser iniciado para criar o atributo personalizado aninhado ao qual você fará referência. Depois de iniciar o Canvas e concluir um fluxo, execute as etapas a seguir:

1. Crie uma etapa subsequente de atualização do usuário que use o editor da interface do usuário.
2. Selecione **Add Personalization (Adicionar personalização**) e, em seguida, selecione **Nested Custom Attribute (Atributo personalizado aninhado** ) e o atributo de nível superior correspondente onde o fluxo está armazenado.  

![Etapa de atualização do usuário com uma personalização de atributos personalizados aninhados.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. Selecione a atribuição da chave que deseja salvar e insira o Liquid no campo **Key Value (Valor da chave** ).

![Janela para "flow_1" com atribuições a serem selecionadas.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. Escolha a atribuição onde você deseja armazená-la.
5\. Envie uma mensagem de teste para testar o Flow.

{% endtab %}
{% tab Parse function %}

Use a tag `json_parse` Liquid para extrair respostas específicas do fluxo. Por exemplo, você pode retirar o token de fluxo e as opções selecionadas para personalizar uma mensagem de acompanhamento.

No editor da interface do usuário, selecione o seguinte: 

- **Nome da atribuição:** YOUR_CUSTOM_ATTRIBUTE (neste exemplo: “First_name”)
- **Ação:** Atualizar
- **Valor-chave:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![Criador de mensagens do WhatsApp com um componente "Adicionar personalização" para inserir uma personalização de propriedades do WhatsApp com o atributo personalizado `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

Quando estiver pronto, envie uma mensagem de teste para testar o Flow. Em seguida, inicie o Canva!

{% endtab %}
{% endtabs %}

{% alert note %}
Uma nova mensagem do WhatsApp "limpa" a capacidade do Canvas de usar (e reutilizar) a resposta do Liquid Flow, portanto, certifique-se de que as mensagens de acompanhamento estejam após todas as etapas de atualização do usuário, webhooks ou outras etapas que usem a resposta do Liquid Flow.
{% endalert %}

## Adição de uma tag de personalização do Flow

Para usar a resposta do Flow por meio do Liquid com [tags de personalização compatíveis]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), conclua as etapas a seguir:

1. Ao ser o criador de sua mensagem do WhatsApp, selecione o ícone de mais para abrir a janela **Adicionar personalização** 
2. Selecione **WhatsApp Properties** para o tipo de personalização e **inbound_flow_response** para o atributo personalizado. Isso pode ser usado para salvar informações em perfis de usuário, incluí-las em mensagens ou encaminhá-las a outros serviços, como webhooks.

![Criador de mensagens do WhatsApp com um componente "Adicionar personalização" para inserir uma personalização de propriedades do WhatsApp com o atributo personalizado inbound_flow_response.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:80%;"}

Em caso de dúvidas ou assistência adicional, entre em contato com [o Suporte]({{site.baseurl}}/braze_support/).