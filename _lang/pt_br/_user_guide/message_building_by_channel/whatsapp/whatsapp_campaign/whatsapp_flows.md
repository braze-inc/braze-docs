---
nav_title: Fluxos do WhatsApp
article_title: Fluxos do WhatsApp
page_order: 1
description: "Este artigo de referência aborda as etapas envolvidas na criação e elaboração de uma mensagem do WhatsApp Flows."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# Fluxos do WhatsApp

> O WhatsApp Flows é um aprimoramento do canal WhatsApp existente, permitindo que você crie experiências de mensagens interativas e dinâmicas. Esta página fornece instruções de etapa a etapa para usar o WhatsApp Flows.

## Configurando o WhatsApp Flows

1. Faça o registro na sua conta Meta.
2. Crie fluxos a partir de um dos dois locais principais:
    - **Ferramentas da conta:** Acesse a guia **Fluxos** para visualizar o ID do fluxo e criar um novo fluxo.
    - **Gerenciar modelos:** Este é o método recomendado para criar fluxos. Aqui, você pode gerar modelos e selecionar uma opção de fluxo durante o processo de criação do modelo.

![WhatsApp Manager com uma página para criar um modelo de fluxos.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\. Selecione um fluxo existente ou crie um novo. Ao criar um fluxo, escolha entre duas opções:
  - **Formulário personalizado:** Para requisitos específicos
  - **Elementos pré-concebidos:** Para uma configuração mais rápida

## Configurando mensagens e respostas do WhatsApp Flow

{% tabs local %}
{% tab Template message %}

1. Em um Braze Canvas, crie uma etapa de mensagem do WhatsApp que utilize o modelo de mensagem contendo o respectivo fluxo.
2. Continue criando seu modelo. Se necessário, adicione mídia, conteúdo variável ou ambos à sua mensagem. Sua seleção de fluxo é escolhida quando o modelo é criado, portanto, não são necessárias informações adicionais para a experiência de fluxo.

![Criador de mensagem do WhatsApp usando um modelo do WhatsApp Flow.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Em um Braze Canvas, crie uma etapa de mensagem do WhatsApp que utilize uma mensagem de resposta e uma mensagem de fluxo.

![Uma etapa de mensagem para um tipo de mensagem de resposta do WhatsApp e layout de mensagem do Flow.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Selecione o fluxo correspondente e continue criando sua mensagem. 

![Um criador de mensagem do Flow com um menu suspenso ampliado para selecionar um Flow.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Prévia do Flow

Antes de lançar um Canvas com um fluxo, você pode selecionar **Prévia do fluxo** para visualizar o fluxo diretamente no Braze e confirmar se ele funciona conforme o esperado. Você também pode interagir com o fluxo na prévia para experimentar como um usuário navegaria pelo fluxo e, em seguida, fazer ajustes em tempo real. Se um fluxo contiver várias páginas, você poderá interagir com cada uma delas.

![Janela de prévia exibindo um formulário para o usuário concluir a inscrição.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Salvar a resposta completa do Flow {#full-flow}

Ao incorporar uma mensagem do WhatsApp Flow em um Braze Canvas ou campanha, você pode querer capturar e utilizar informações específicas que os usuários enviam através do Flow. A Braze precisa receber informações adicionais sobre a estrutura da resposta do usuário, especificamente o formato esperado da resposta JSON, para gerar o esquema de atributos personalizados aninhados (NCA) necessário.

### Etapa 1: Gerar o atributo personalizado Fluxo

{% tabs local %}
{% tab Recommended method %}

A maneira mais simples de fornecer ao Braze as informações sobre a estrutura da resposta é salvar a resposta do fluxo como um atributo personalizado e concluir um envio de teste.

#### Usando um fluxo que não foi utilizado no Braze

Se você estiver usando um fluxo que não foi usado anteriormente no Braze, ao visualizar a seção **Atributo personalizado do fluxo** em **Compor mensagens**, talvez não veja nenhuma informação. Isso significa que o esquema ainda não foi gerado.

![Seção Meta Flow com uma opção para visualizar o atributo personalizado Flow.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute.png %}){: style="max-width:70%;"}

Para resolver isso, faça o seguinte:

1. Conclua a etapa de configuração da sua mensagem do WhatsApp.
2. Confirme se você marcou a opção **“Salvar respostas do fluxo como um atributo personalizado**”.

![Seção Meta Flow com uma caixa de seleção para salvar as respostas do Flow como um atributo personalizado.]({% image_buster /assets/img/whatsapp/flows/save_flow_responses_checkbox.png %}){: style="max-width:80%;"}

{: start="3"}
3\. Envie uma mensagem de teste para si mesmo e conclua o fluxo como usuário.

Agora, o Braze tem o formato da resposta JSON do Flow e pode gerar o atributo personalizado.

{% endtab %}
{% tab Alternative methods %}

Use o editor JSON avançado para salvar atributos da resposta do Flow em atributos personalizados ou use um Canvas de várias etapas para salvar a resposta em um atributo personalizado aninhado. 

{% subtabs %}
{% subtab Advanced JSON editor %}

No editor JSON avançado, insira {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, onde“flow_1”  é o atributo personalizado no qual você deseja que o fluxo seja salvo.

![Etapa de atualização do usuário com um editor JSON avançado.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endsubtab %}
{% subtab UI editor %}

1. Confirme se você já criou um atributo personalizado com o tipo de dados do("flow_1" objeto (neste exemplo) nas configurações de dados do seu espaço de trabalho.
2. No editor da interface do usuário, use o Liquid{% raw %}```{{whats_app.${inbound_flow_response}}}```para preencher o atributo personalizado e salvar toda a resposta do Flow do usuário nele. Você precisa preencher o valor da chave como```{{whats_app.${inbound_flow_response}}}```{% endraw %}antes de selecionar o atributo personalizado que você criou.

![Etapa de atualização do usuário que utiliza o editor da interface do usuário.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Depois que a Braze receber uma resposta do Flow, salvaremos o atributo personalizado aninhado com a nomenclatura prescrita no perfil do usuário. Esse atributo personalizado pode ser extraído ao criar canvas. 

![Uma janela que exibe o conteúdo de um "flow_1"atributo personalizado.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Etapa 2: Visualizar a resposta do fluxo salva

Quando o fluxo é concluído, o Braze cria automaticamente um atributo personalizado do fluxo com um nome baseado no ID do fluxo. Em seguida, você pode acessar o perfil do usuário para visualizar a resposta do Flow salva como um objeto aninhado na seção **de atributos personalizados**.

Após a geração do esquema, a seção **Atributo personalizado** do fluxo exibirá a estrutura esperada, incluindo os tipos de dados previstos para cada resposta (por exemplo, “String” ou “Matriz de strings”).

![Janela de detalhes dos atributos personalizados do fluxo com menu suspenso do esquema.]({% image_buster /assets/img/whatsapp/flows/flow_custom_attribute_details.png %}){: style="max-width:80%;"}

### Considerações

- **Atributos existentes:** Se um atributo personalizado para um fluxo específico já tiver sido gerado, o fluxo será carregado com as informações do atributo disponíveis. Nesses casos, você não precisa enviar uma mensagem de teste para gerar o esquema, pois o Braze já reconhece as mensagens de resposta esperadas.
- **Alterações no fluxo:** Se você fizer alguma alteração no fluxo após a geração do esquema, será necessário enviar uma mensagem de teste adicional para que a Braze possa entender que a forma da resposta do fluxo foi alterada e ajustar a estrutura do atributo de acordo. Esta ação está limitada a uma vez a cada 24 horas. 
- **Consistência:** O atributo personalizado do fluxo gerado é consistente e será o mesmo atributo para este fluxo específico, independentemente do Canvas em que for utilizado.
- **Opção manual:** Você não precisa marcar a caixa de seleção **Salvar respostas do fluxo como um atributo personalizado**. Você pode gerar manualmente o atributo personalizado [salvando campos específicos das respostas do Flow em um atributo personalizado específico](#saving-specific-fields-from-flow-responses-to-a-specific-custom-attribute), o que evita a duplicação de etapas do usuário.

## Salvar campos específicos das respostas do Flow em um atributo personalizado específico 

### Etapa 1: Criar uma jornada de ação

Crie uma etapa do canva [da jornada de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) ou uma campanha baseada em ações. Selecione um gatilho **para disparar a mensagem recebida no WhatsApp** e uma condição **Respondido ao fluxo** e, em seguida, selecione o fluxo relevante ou **Qualquer fluxo**.

![Para disparar um gatilho para usuários que enviaram uma mensagem de entrada pelo WhatsApp e responderam a qualquer fluxo.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Etapa 2: Extrair campos das respostas do Flow

Você pode usar atributos personalizados aninhados ou a`json_parse`Liquid tag para extrair campos específicos das respostas do Flow.

{% tabs %}
{% tab Nested custom attributes %}

Para salvar partes específicas da resposta do Flow do usuário, conclua todas as etapas em [Salvando a resposta completa do Flow](#full-flow), **incluindo o lançamento do Canvas**. O Canvas deve ser iniciado para criar o atributo personalizado aninhado que você irá referenciar. Após iniciar o Canvas e concluir um fluxo, execute as seguintes etapas:

1. Crie uma etapa subsequente de atualização do usuário que utilize o editor da interface do usuário.
2. Selecione **Adicionar personalização**, depois selecione **Atributo personalizado aninhado** e o atributo de nível superior correspondente onde o fluxo está armazenado.  

![Etapa de atualização do usuário com personalização de atributos personalizados aninhados.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. Selecione o atributo-chave que deseja salvar e insira o Liquid no campo **Valor-chave**.

![Janela para"flow_1"  com atributos para selecionar.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. Escolha o atributo onde deseja armazená-lo.
5\. Envie uma mensagem de teste para testar o fluxo.

{% endtab %}
{% tab Parse function %}

Use a`json_parse`Liquid tag to extract specific responses from the flow. Por exemplo, você pode retirar o token Flow e as opções selecionadas para personalizar uma mensagem de acompanhamento.

No editor da interface do usuário, selecione o seguinte: 

- **Nome do atributo:**YOUR_CUSTOM_ATTRIBUTE(neste exemplo: “First_name”)
- **Ação:** Atualizar
- **Valor-chave:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

![Criador de mensagens do WhatsApp com um componente "Adicionar personalização" para inserir uma personalização das propriedades do WhatsApp com o atributo `inbound_flow_response`.]({%image_buster/assets/img/whatsapp/flows/parsed_json.pngpersonalizado    %})

Quando estiver pronto, envie uma mensagem de teste para testar o fluxo. Em seguida, inicie o Canva!

{% endtab %}
{% endtabs %}

{% alert note %}
Uma nova mensagem do WhatsApp “limpa” a capacidade do Canvas de usar (e reutilizar) a resposta do Fluxo Líquido, portanto, certifique-se de que as mensagens de acompanhamento sejam enviadas após todas as etapas de Atualização do Usuário, webhooks ou outras etapas que usam a resposta do Fluxo Líquido.
{% endalert %}

## Adicionando uma tag de personalização do Flow

Para usar a resposta do Flow através do Liquid com [tags de personalização compatíveis]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/), siga estas etapas:

1. Ao redigir sua mensagem no WhatsApp, selecione o ícone de mais para abrir a janela **Adicionar personalização.**
2. Selecione **Propriedades do WhatsApp** para o tipo de personalização e**inbound_flow_response**  para o atributo personalizado. Isso pode ser usado para salvar informações em perfis de usuário, incluí-las no envio de mensagens ou encaminhá-las para outros serviços, como webhooks.

![Criador de mensagens do WhatsApp com um componente "Adicionar personalização" para inserir uma personalização das propriedades do WhatsApp com o atributo inbound_flow_response.]({%image_buster/assets/img/whatsapp/flows/inbound_flow_response.pngpersonalizado    %}){: style="max-width:80%;"}

Para quaisquer dúvidas ou assistência adicional, entre em contato com [o Suporte]({{site.baseurl}}/braze_support/).