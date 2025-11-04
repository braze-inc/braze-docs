---
nav_title: Listas de supressão
article_title: Listas de Supressão
page_order: 3
page_type: reference
tool: Segments
description: "Esta página cobre como usar listas de supressão para especificar quais usuários nunca devem receber suas mensagens."

---

# Listas de supressão

> Listas de supressão são grupos de usuários que automaticamente não recebem nenhuma campanha ou Canvas. Listas de supressão são definidas por filtros de segmento, e os usuários entrarão e sairão das listas de supressão à medida que atenderem aos critérios de filtro. Você também pode definir tags de exceção para que a lista de supressão não se aplique a campanhas ou Canvases com essas tags. Mensagens de campanhas ou Canvases com tags de exceção ainda alcançarão usuários da lista de supressão que estão nos segmentos-alvo.

## Por que usar listas de supressão?

Listas de supressão são dinâmicas e se aplicam automaticamente a todas as formas de mensagens, mas você pode definir exceções para tags selecionadas. Se suas tags de exceção selecionadas forem usadas em uma campanha ou Canvas, então essa lista de supressão não se aplicará a essa campanha ou Canvas. Mensagens de campanhas ou Canvases com tags de exceção ainda alcançarão qualquer usuário da lista de supressão que faça parte dos seus segmentos-alvo.

### Tipos de mensagens e canais afetados por listas de supressão

Listas de supressão se aplicarão a todos os tipos de mensagens e canais, exceto para [flags de recurso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/). Isso significa que as listas de supressão, por padrão, se aplicam a todos os canais, campanhas e Canvases, incluindo:
- [campanhas de API]({{site.baseurl}}/api/api_campaigns/)
- Campanhas e Canvases acionados por API
- [e-mails transacionais]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)

O único tipo de mensagem ao qual as listas de supressão não se aplicam são as flags de recurso. Usuários em uma lista de supressão não serão suprimidos de flags de recurso, mas serão suprimidos de todos os outros canais. 

Você pode usar tags de exceção para que os usuários da lista de supressão ainda sejam alvo de campanhas e Canvases específicos. Para detalhes, consulte a etapa 4 em [Configuração de listas de supressão](#setup). Se você não adicionar tags de exceção a uma lista de supressão, os usuários nessa lista de supressão não serão alvo de nenhuma mensagem além de flags de recurso. 

{% alert note %}
Listas de supressão são aplicadas a campanhas de API que são criadas no painel do Braze com um `campaign_id`. Listas de supressão não se aplicam a mensagens enviadas através de [Pontos de extremidade de mensagens do Braze]({{site.baseurl}}/api/endpoints/messaging/) sem um `campaign_id` associado.
{% endalert %}

\![A seção "Configurações de Exceção" com uma caixa de seleção para não aplicar a lista de supressão a campanhas e Canvases acionadas por API.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## Configurando listas de supressão {#setup}

{% alert note %}
Todos os usuários podem visualizar listas de supressão, mas apenas usuários com [permissões de administrador]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=admin#list-of-permissions) podem criar e gerenciar listas de supressão.
{% endalert %}

1. Vá para **Público** > **Listas de Supressão**.<br><br>\![A página "Listas de Supressão" com uma lista de três listas de supressão.]({% image_buster /assets/img/suppression_lists_home.png %})<br><br>
2. Selecione **Criar Lista de Supressão** e adicione um nome.<br><br>\![Uma janela chamada "Criar uma Lista de Supressão" com um campo para inserir um nome.]({% image_buster /assets/img/create_suppression_list.png %}){: style="max-width:80%;"}<br><br>
3. Use filtros de segmento para identificar os usuários em suas listas de supressão. Você deve selecionar pelo menos um.

{% alert important %}
Embora o processo de configuração pareça semelhante à [criação de segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), uma lista de supressão é um grupo de usuários que você **não** deseja enviar mensagens, independentemente da associação ao segmento.
{% endalert %}

\![Um construtor de lista de supressão com um filtro para usuários que abriram um e-mail pela última vez há mais de 90 dias.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4\. Determine se deve haver exceções com base na tag marcando a caixa abaixo do nome do seu segmento (consulte [Por que usar listas de supressão?](#why-use-suppression-lists) para mais informações), em seguida, adicione as tags de campanhas ou Canvases que os usuários nesta lista de supressão ainda devem receber. <br><br>Em outras palavras, se você adicionar a tag de exceção "Confirmação de envio", os usuários na sua lista de supressão serão excluídos de todas as mensagens, exceto aquelas que usam a tag "Confirmação de envio".<br><br>\![A seção "Detalhes da Lista de Envio" com uma tag de exceção aplicada chamada "Confirmação de envio".]({% image_buster /assets/img/exception_tags.png %})<br><br>
5\. Salve ou ative sua lista de supressão.
- Quando você salva, sua lista de supressão será salva, mas não será ativada, o que significa que não entrará em vigor. Sua lista de supressão permanecerá inativa até que você a ative, e listas de supressão inativas não impactarão as mensagens (os usuários não serão excluídos das mensagens).
- Quando você ativa, sua lista de supressão será salva e entrará em vigor imediatamente, o que significa que os usuários na sua lista de supressão serão imediatamente excluídos de campanhas ou Canvases (exceto aqueles que contêm uma tag de exceção).

{% alert note %}
Apenas administradores podem salvar ou ativar listas de supressão. Você pode ter até cinco listas de supressão ativas ao mesmo tempo na versão beta.
{% endalert %}

Você pode desativar ou arquivar listas de supressão quando não precisar mais delas. 
- Para desativar, selecione uma lista de supressão ativa e selecione **Desativar**. Listas de supressão desativadas podem ser reativadas posteriormente.
- Para arquivar, faça isso na página **Listas de Supressão**.

## Uso da lista de supressão

Para verificar se sua lista de supressão impediu um usuário de receber uma mensagem, use **Consulta de Usuário** na etapa **Público-Alvo** dentro da sua campanha ou Canvas. Aqui, você poderá ver de qual lista de supressão eles fazem parte.

\![Janela "Consulta de Usuário" mostrando que um usuário está em uma lista de supressão.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
Você também pode encontrar listas de supressão aplicadas na etapa **Resumo**.
{% endalert %}

Ao criar uma campanha ou Canvas, use **User Lookup** na etapa **Target Audience** para procurar um usuário, e se ele não estiver no público-alvo, você pode ver a lista de supressão da qual ele faz parte. 

\![Janela "Consulta de Usuário" mostrando que um usuário está em uma lista de supressão.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

### Campanha 

Se um usuário estiver em uma lista de supressão, ele não receberá uma campanha para a qual essa lista de supressão se aplica. Consulte [Tipos de mensagens e canais afetados por listas de supressão](#message-types-and-channels-affected-by-suppression-lists) para casos em que uma lista de supressão não se aplicará.

\![A seção "Listas de Supressão" com uma lista de supressão ativa, chamada "Baixos índices de saúde de marketing".]({% image_buster /assets/img/active_suppression_list.png %})

### Canvas 

A partir do momento em que um usuário é adicionado a uma lista de supressão, ele não entrará em Canvases. Se ele já entrou em um Canvas, não receberá etapas de Mensagem. Isso significa que se um usuário já estiver dentro de um Canvas quando for adicionado a uma lista de supressão, ele avançará pelo Canvas até a próxima etapa de Mensagem, momento em que sairá sem receber a etapa de Mensagem. 

Por exemplo, digamos que um Canvas tenha uma etapa de Atualização de Usuário seguida por uma etapa de Mensagem. Se um usuário entrar no Canvas e depois for adicionado a uma lista de supressão, esse usuário ainda avançará pela etapa de Atualização de Usuário (onde pode ser atualizado) e, em seguida, sairá na etapa de Mensagem, momento em que será incluído nas métricas de saída.
