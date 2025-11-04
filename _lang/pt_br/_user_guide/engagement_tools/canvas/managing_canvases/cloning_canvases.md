---
nav_title: Clonando Canvases
article_title: Clonando Canvases
page_order: 3
alias: "/cloning_canvases/"
description: "Este artigo de referência descreve como clonar um Canvas do editor original de Canvas para o fluxo de trabalho Canvas Flow."
tool: Canvas
---

# Clonando Canvases para o Canvas Flow

{% alert important %}
Você não pode mais criar ou duplicar Canvases usando a experiência original de Canvas. A Braze recomenda que os clientes que usam a experiência original de Canvas migrem para o Canvas Flow, a experiência atual de Canvas.
{% endalert %}

> Se você tiver um Canvas existente do editor original, pode clonar este Canvas para criar uma cópia no Canvas Flow. Ao mudar para o fluxo de trabalho atual de Canvas, você ganha acesso a componentes leves [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), propriedades de entrada persistentes {2]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/), e edição pós-lançamento {3]({{site.baseurl}}/post-launch_edits). Seu Canvas original não será alterado ou excluído.

Para clonar seu Canvas, faça o seguinte:

1. Vá para o painel do Canvas. 
2. Identifique o Canvas do qual você deseja criar uma cópia no fluxo de trabalho Canvas Flow. Você pode clonar Canvases com um status **Rascunho**, **Ativo** ou **Parado**. 
3. Clique em <i class="fas fa-ellipsis-vertical"></i> **Mais ações** e selecione **Clonar para Canvas Flow**.

\![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4\. Digite o nome do seu novo Canvas e clique em **Clonar para Canvas Flow**. 

\![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Agora, você tem duas versões do seu Canvas: o Canvas original e a versão Canvas Flow. Seu Canvas original ainda tem seu status original, e o Canvas clonado tem um status **Rascunho**. Você ainda pode acessar o Canvas original, mas a Braze recomenda usar o fluxo de trabalho Canvas Flow para continuar construindo seus Canvases.

Anteriormente, alguns Canvases com ramificações não podiam ser clonados. Agora, você pode clonar Canvases com ramificações. Observe que clonar Canvases com ramificações pode resultar em etapas desconectadas. Resolva essas etapas desconectadas (etapas que não têm uma etapa anterior conectada a elas) para garantir que a jornada do seu Canvas esteja mapeada corretamente.

{% alert note %}
Se você clonar um Canvas ativo, a Braze continuará enviando usuários pelo Canvas original. Recomendamos parar um Canvas antes de cloná-lo para evitar enviar mensagens duplicadas para os usuários de ambos os Canvases.
{% endalert %}

\![Painel do Canvas com dois Canvases listados: Cópia V2 do Canvas V1 e Canvas V1. A Cópia V2 do Canvas V1 tem um ícone que indica que está usando o fluxo de trabalho Canvas Flow.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

Você concluiu a clonagem do seu Canvas para o fluxo de trabalho Canvas Flow. Agora, você pode continuar construindo seus Canvases nesta experiência atualizada!

## Recomendações

Para permitir que usuários existentes continuem sua jornada após você ter clonado seu Canvas original para o Canvas Flow, você pode adicionar filtros ao seu Canvas existente que impedem novos usuários de entrar no novo Canvas.

Se a re-eligibilidade estiver desativada, adicione o filtro "Entrou na Variação do Canvas". Se a re-eligibilidade estiver ativada, estes são os métodos possíveis a considerar para garantir que os usuários não entrem no mesmo Canvas duas vezes:
- Atualize o Canvas existente para incluir uma tag única. Para o novo Canvas, adicione um filtro "Última Mensagem Recebida da Campanha ou Canvas com Tag". Isso impede que os usuários entrem no Canvas duas vezes após uma data de entrada específica (número total de dias após a última mensagem ser enviada do Canvas original mais a janela de conversão). 
- **O seguinte método registrará pontos de dados.** Atualize o Canvas original para incluir um webhook Braze-to-Braze que aciona um timestamp de data de atributo personalizado ao entrar. Esse atributo pode ser usado para impedir que os usuários entrem no novo Canvas após a data especificada (número total de dias após a última mensagem ser enviada do Canvas original mais a janela de conversão).

Para Canvases acionados por API, coordene-se com sua equipe de engenharia para garantir que esses Canvases estejam usando o novo ID do Canvas quando os novos Canvases estiverem prontos para serem lançados.

Para mais informações sobre as diferenças entre o editor do Canvas original e a experiência do Canvas Flow, confira [FAQ do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).


