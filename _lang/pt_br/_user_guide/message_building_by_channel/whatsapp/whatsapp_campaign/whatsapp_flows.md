---
nav_title: Fluxos do WhatsApp
article_title: Fluxos do WhatsApp
page_order: 1
description: "Este artigo de referência cobre os passos envolvidos na construção e criação de uma mensagem de Fluxos do WhatsApp."
alias: /whatsapp_flows/
page_type: reference
tool:
  - Canvas
channel:
  - WhatsApp
---

# Fluxos do WhatsApp

> Os Fluxos do WhatsApp são uma melhoria ao canal existente do WhatsApp, permitindo que você crie experiências de mensagens interativas e dinâmicas. Esta página fornece instruções passo a passo para participar do programa de Acesso Antecipado e usar os Fluxos do WhatsApp.

## Configurando os Fluxos do WhatsApp

1. Faça login na sua conta Meta.
2. Crie Fluxos a partir de um de dois locais principais:
    - **Ferramentas de conta:** Vá para a aba **Fluxos** para visualizar o ID do Fluxo e criar um novo Fluxo.
    - **Gerenciar modelos:** Este é o método recomendado para criar Fluxos. Aqui, você pode gerar modelos e selecionar uma opção de Fluxo durante o processo de criação do modelo.

\![Gerenciador do WhatsApp com uma página para criar um modelo de Fluxos.]({% image_buster /assets/img/whatsapp/flows/create_flows_template.png %})

{: start="3"}  
3\. Selecione um Fluxo existente ou crie um. Se estiver criando um Fluxo, escolha entre duas opções:
  - **Formulário Personalizado:** Para requisitos específicos
  - **Elementos Pré-projetados:** Para uma configuração mais rápida

## Configurando mensagens e respostas do Flow do WhatsApp

{% tabs local %}
{% tab Template message %}

1. Em um Canvas do Braze, crie um passo de mensagem do WhatsApp que utilize a mensagem de modelo contendo o respectivo Flow.
2. Continue criando seu modelo. Se necessário, adicione mídia, conteúdo variável ou ambos à sua mensagem. Sua seleção de Flow é escolhida quando o modelo foi criado, portanto, informações adicionais para a experiência do flow não são necessárias.

\![Compositor de mensagem do WhatsApp usando um modelo de Flow do WhatsApp.]({% image_buster /assets/img/whatsapp/flows/composer_flow_template.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Response message %}

1. Em um Canvas do Braze, crie um passo de mensagem do WhatsApp que utilize uma mensagem de resposta e mensagem de flow.

\![Um passo de mensagem para um tipo de mensagem de resposta do WhatsApp e layout de mensagem de Flow.]({% image_buster /assets/img/whatsapp/flows/message_step_flow_message.png %}){: style="max-width:80%;"}

{: start="2"}
2\. Selecione o respectivo Flow, e então continue criando sua mensagem. 

\![Um compositor de resposta de mensagem de Flow com um dropdown estendido para selecionar um Flow.]({% image_buster /assets/img/whatsapp/flows/flow_message_composer.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Visualizar Flow

Antes de lançar um Canvas com um Flow, você pode selecionar **Visualizar Flow** para visualizar o Flow diretamente no Braze para confirmar que ele se comporta como esperado. Você também pode interagir com o Flow na visualização para experimentar como um usuário navegaria pelo Flow, e então fazer ajustes em tempo real. Se um Flow contiver várias páginas, você pode interagir com cada página.

\![Janela de visualização exibindo um formulário para um usuário finalizar o cadastro.]({% image_buster /assets/img/whatsapp/flows/flow_preview.png %}){: style="max-width:50%;"}

## Salvando a resposta completa do Flow {#full-flow}

### Passo 1: Criar um Caminho de Ação

Crie um passo de Canvas de [Caminho de Ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) ou uma campanha baseada em ações. Selecione um gatilho de **Enviar uma mensagem de WhatsApp recebida** e a condição **Respondeu ao Fluxo**, e então selecione o Fluxo relevante ou **Qualquer Fluxo**.

\![Um gatilho para usuários que enviaram uma mensagem de WhatsApp recebida e responderam a qualquer Fluxo.]({% image_buster /assets/img/whatsapp/flows/trigger_responded_flow.png %})

### Passo 2: Componha sua mensagem de WhatsApp

Ao compor sua mensagem de WhatsApp, selecione o ícone de mais para abrir a janela de **Adicionar Personalização**, depois selecione **Propriedades do WhatsApp** para o tipo de personalização e **inbound_flow_response** para o atributo personalizado. Isso salvará informações nos perfis dos usuários ou as encaminhará para outros serviços, como webhooks.

\![Compositor de mensagem do WhatsApp com um componente "Adicionar Personalização" para inserir uma personalização de propriedades do WhatsApp com o atributo personalizado `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/inbound_flow_response.png %}){: style="max-width:60%;"}

### Passo 3: Salve a resposta completa do Fluxo

Você pode usar o editor JSON avançado para salvar atributos da resposta do Fluxo em atributos personalizados, ou usar um Canvas de múltiplos passos para salvar a resposta em um atributo personalizado aninhado. 

{% tabs %}
{% tab Advanced JSON editor %}

No editor JSON avançado, insira {% raw %}`{"attributes": [{"flow_1": {{whats_app.${inbound_flow_response}}}}]}`{% endraw %}, onde “flow_1” é o atributo personalizado que você gostaria que o fluxo fosse salvo.

\![Passo de Atualização do Usuário com um editor JSON avançado.]({% image_buster /assets/img/whatsapp/flows/user_update_advanced_json_editor.png %})

{% endtab %}
{% tab UI editor %}

1. Confirme que você já criou um atributo personalizado com o tipo de dado objeto ("flow_1" neste exemplo) dentro das configurações de dados do seu espaço de trabalho.
2. No editor de UI, use o Liquid {% raw %}```{{whats_app.${inbound_flow_response}}}``` para preencher o atributo personalizado e salvar toda a resposta do Fluxo do usuário nele. Você precisa preencher o valor da chave como ```{{whats_app.${inbound_flow_response}}}```{% endraw %} antes de selecionar o atributo personalizado que você criou.

\![Passo de Atualização do Usuário que usa o editor de UI.]({% image_buster /assets/img/whatsapp/flows/user_update_ui_editor.png %})

Depois que a Braze receber uma resposta do Fluxo, salvaremos o atributo personalizado aninhado com a nomenclatura prescrita no perfil do usuário. Esse atributo personalizado pode ser utilizado ao construir Canvases. 

\![Uma janela exibindo o conteúdo de um "flow_1" atributo personalizado.]({% image_buster /assets/img/whatsapp/flows/user_attribute_flow.png %})

{% endtab %}
{% endtabs %}

Quando estiver pronto, envie uma mensagem de teste para testar o Fluxo. Em seguida, inicie o Canvas!

## Salvando campos específicos das respostas do Fluxo em um atributo personalizado específico 

Você pode usar atributos personalizados aninhados ou a tag `json_parse` Liquid para extrair campos específicos das respostas do Fluxo.

{% tabs %}
{% tab Nested custom attributes %}

Para salvar partes específicas da resposta do Fluxo do usuário, complete todas as etapas em [Salvando a resposta completa do Fluxo](#full-flow), **incluindo iniciar o Canvas**. O Canvas deve ser iniciado para criar o atributo personalizado aninhado que você irá referenciar. Após iniciar o Canvas e completar um Fluxo, siga as etapas a seguir:

1. Crie uma etapa de Atualização de Usuário subsequente que use o editor de UI.
2. Selecione **Adicionar Personalização**, em seguida, selecione **Atributo Personalizado Aninhado** e o atributo de nível superior correspondente onde o Fluxo está armazenado.  

\![Etapa de Atualização de Usuário com uma personalização de Atributos Personalizados Aninhados.]({% image_buster /assets/img/whatsapp/flows/nested_custom_attributes.png %})

{: start="3" }
3\. Selecione o atributo chave que você gostaria de salvar e insira o Liquid no campo **Valor Chave**.

\![Janela para "flow_1" com atributos para selecionar.]({% image_buster /assets/img/whatsapp/flows/attribute_key.png %})

{: start="4" }
4\. Escolha o atributo onde você deseja armazená-lo.
5\. Envie uma mensagem de teste para testar o Fluxo.

{% endtab %}
{% tab Parse function %}

Use a tag `json_parse` Liquid para extrair respostas específicas do fluxo. Por exemplo, você pode extrair o token do Fluxo e as opções selecionadas para personalizar uma mensagem de acompanhamento.

### Passo 1: Criar um Caminho de Ação

Crie um [Caminho de Ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) com **Enviar uma mensagem de WhatsApp recebida** como gatilho para processar as informações do Fluxo.

{% alert note %}
Você poderá especificar o Fluxo quando recursos adicionais forem lançados durante o acesso antecipado.
{% endalert %}

### Passo 2: Componha sua mensagem de WhatsApp

Ao compor sua mensagem de WhatsApp, selecione o ícone de mais para abrir a janela de **Adicionar Personalização**, depois selecione **Propriedades do WhatsApp** para o tipo de personalização e **inbound_flow_response** para o atributo personalizado. Isso salvará informações nos perfis dos usuários ou as encaminhará para outros serviços, como webhooks.

### Passo 3: Salve campos específicos da resposta do Fluxo

No editor de UI, selecione o seguinte: 

- **Nome do Atributo:** YOUR_CUSTOM_ATTRIBUTE (neste exemplo: “First_name”)
- **Ação:** Atualizar
- **Valor da Chave:** {% raw %} ```{% assign parsed_json = {{whats_app.${inbound_flow_response}}} | json_parse %}{{ parsed_json.FIELDS_THAT_APPLY }}```{% endraw %}

\![Compositor de mensagem do WhatsApp com um componente "Adicionar Personalização" para inserir uma personalização de propriedades do WhatsApp com o atributo personalizado `inbound_flow_response`.]({% image_buster /assets/img/whatsapp/flows/parsed_json.png %})

{% alert note %}
Uma nova mensagem do WhatsApp "limpa" a capacidade do Canvas de usar (e reutilizar) a resposta do Fluxo Líquido, então certifique-se de que as mensagens de acompanhamento estejam após todas as etapas de Atualização do Usuário, webhooks ou outras etapas que utilizem a resposta do Fluxo Líquido.
{% endalert %}

Quando estiver pronto, envie uma mensagem de teste para testar o Fluxo. Em seguida, inicie o Canvas!

{% endtab %}
{% endtabs %}

{% alert note %}
Funcionalidades adicionais do Fluxo serão introduzidas, incluindo filtros de etapas de ação avançados e mensagens de resposta que incorporam elementos do Fluxo.
{% endalert %}

Para quaisquer perguntas ou assistência adicional, entre em contato com [Suporte]({{site.baseurl}}/braze_support/).