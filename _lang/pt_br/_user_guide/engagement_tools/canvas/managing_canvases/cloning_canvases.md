---
nav_title: Clonagem de telas
article_title: Clonagem de telas
page_order: 3
alias: "/cloning_canvases/"
description: "Este artigo de referência descreve como clonar um Canvas do editor de Canvas original para o fluxo de trabalho do Canvas Flow."
tool: Canvas
---

# Clonagem de canvas para o Canvas Flow

{% alert important %}
A partir de 28 de fevereiro de 2023, não será mais possível criar ou duplicar Canvas usando a experiência original do Canvas. A Braze recomenda que os clientes que usam a experiência original do Canvas migrem para o Canvas Flow.
{% endalert %}

> Se você tiver uma tela existente do editor original, poderá clonar essa tela para criar uma cópia no Canvas Flow. Ao mudar para o fluxo de trabalho do Canvas Flow, você obtém acesso a [componentes leves do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/), [propriedades de entrada persistentes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) e [edição pós-lançamento]({{site.baseurl}}/post-launch_edits). Sua tela original não será alterada ou excluída.

Para clonar seu Canva, faça o seguinte:

1. Acesse o dashboard do canvas. 
2. Identifique o canvas do qual você deseja criar uma cópia no fluxo de trabalho do Canvas Flow. Você pode clonar Canvas com status de **Rascunho**, **Ativo** ou **Parado**. 
3. Clique em <i class="fas fa-ellipsis-vertical"></i> **More actions** e selecione **Clone to Canvas Flow**.

![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4\. Digite o nome de seu novo canvas e clique em **Clonar para o Canvas Flow**. 

![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Agora, você tem duas versões de seu canvas: o canvas original e a versão do Canvas Flow. Seu Canvas original ainda tem o status original, e o Canvas clonado tem o status de **Rascunho**. Você ainda pode acessar o Canvas original, mas o Braze recomenda o uso do fluxo de trabalho Canvas Flow para continuar a criar seus Canvases.

Anteriormente, algumas telas com ramificações não podiam ser clonadas. Agora, você pode clonar Canvas com ramificação. Note que a clonagem de Canvas com ramificação pode resultar em etapas desconectadas. Resolva essas etapas desconectadas (etapas que não têm uma etapa anterior conectada a elas) para garantir que sua jornada do Canvas seja mapeada corretamente.

{% alert note %}
Se você clonar um canvas ativo, a Braze continuará enviando usuários por meio do canvas original. Recomendamos interromper um Canvas antes da clonagem para evitar o envio de mensagens duplicadas aos usuários de ambos os Canvas.
{% endalert %}

![Painel dashboard com dois canvas listados: V2 Cópia do canvas V1 e do canvas V1. A cópia V2 do Canvas V1 tem um ícone que indica que está usando o fluxo de trabalho do Canvas Flow.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

Você concluiu a clonagem de seu Canvas no fluxo de trabalho do Canvas Flow. Agora, você pode continuar construindo suas Canvas nesta experiência atualizada!

## Recomendações

Para permitir que os usuários existentes continuem a jornada do usuário depois de clonar o Canvas original para o Canvas Flow, é possível adicionar filtros ao Canvas existente que impedem que novos usuários entrem no novo Canvas.

Se a reelegibilidade estiver desativada, adicione o filtro "Variação de canvas inserida". Se a reelegibilidade estiver ativada, estes são os possíveis métodos a serem considerados para garantir que os usuários não entrem na mesma tela duas vezes:
- Atualize o Canva existente para incluir uma tag exclusiva. Para o novo Canvas, adicione um filtro "Last Received Message from Campaign or Canvas with Tag" (Última mensagem recebida da campanha ou do Canvas com tag). Isso impede que os usuários entrem no Canvas duas vezes após uma data de entrada específica (número total de dias após o envio da última mensagem do Canvas original mais a janela de conversão). 
- **O método a seguir consumirá pontos de dados.** Atualize o Canva original para incluir um webhook Braze-to-Braze que dispara um atributo personalizado de data e hora na entrada. Essa atribuição pode ser usada para impedir que os usuários entrem no novo Canvas após a data especificada (número total de dias após o envio da última mensagem do Canvas original mais a janela de conversão).

Para Canvases disparados pela API, coordene com sua equipe de engenharia para garantir que esses Canvases estejam usando o novo ID do Canvas quando os novos Canvases estiverem prontos para serem lançados.

Para saber mais sobre as diferenças entre o editor original do Canvas e a experiência do Canvas Flow, consulte [as Perguntas frequentes sobre o Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).


