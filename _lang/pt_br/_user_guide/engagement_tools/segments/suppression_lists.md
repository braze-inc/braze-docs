---
nav_title: Listas de supressão
article_title: Listas de supressão
page_order: 3
page_type: reference
tool: Segments
description: "Esta página aborda como usar listas de supressão para especificar quais usuários nunca devem receber suas mensagens."

---

# Listas de supressão

> As listas de supressão são grupos de usuários que não recebem automaticamente nenhuma campanha ou canvas. As listas de supressão são definidas por filtros de segmento, e os usuários entrarão e sairão das listas de supressão à medida que atenderem aos critérios de filtro. Você também pode definir tags de exceção para que a lista de supressão não se aplique a campanhas ou Canvas com essas tags. As mensagens de campanhas ou Canvas com tags de exceção ainda alcançarão os usuários da lista de supressão que estão nos segmentos de direcionamento.

## Por que usar listas de supressão?

As listas de supressão são dinâmicas e se aplicam automaticamente a todas as formas de envio de mensagens, mas você pode definir exceções para tags selecionadas. Se as tags de exceção selecionadas forem usadas em uma campanha ou Canvas, essa lista de supressão não se aplicará a essa campanha ou Canvas. As mensagens de campanhas ou Canvas com tags de exceção ainda alcançarão todos os usuários da lista de supressão que fazem parte de seus segmentos de direcionamento.

### Tipos e canais de envio de mensagens afetados pelas listas de supressão

As listas de supressão se aplicarão a todos os tipos e canais de envio de mensagens, exceto aos [sinalizadores de recursos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/). Isso significa que, por padrão, as listas de supressão se aplicam a todos os canais, campanhas e Canvas, inclusive:
- [Campanhas da API]({{site.baseurl}}/api/api_campaigns/)
- Campanhas disparadas por API e Canvas
- [E-mails de transação]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)

O único tipo de mensagem ao qual as listas de supressão não se aplicam são os sinalizadores de recursos. Os usuários em uma lista de supressão não serão suprimidos dos sinalizadores de recursos, mas serão suprimidos de todos os outros canais. 

É possível usar tags de exceção para que os usuários da lista de supressão ainda sejam direcionados por campanhas e Canvas específicos. Para obter detalhes, consulte a etapa 4 em [Configuração de listas de supressão](#setup). Se você não adicionar tags de exceção a uma lista de supressão, os usuários dessa lista de supressão não serão direcionados a nenhum envio de mensagens além dos sinalizadores de recursos. 

{% alert note %}
As listas de supressão são aplicadas às campanhas de API criadas no dashboard do Braze com um `campaign_id`. As listas de supressão não se aplicam a mensagens enviadas por meio de [endpoints de envio de mensagens do Braze]({{site.baseurl}}/api/endpoints/messaging/) sem um `campaign_id` associado.
{% endalert %}

![A seção "Configurações de exceção" com uma caixa de seleção para não aplicar a lista de supressão a campanhas e Canvas disparados pela API.]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}

## Configuração de listas de supressão {#setup}

{% alert note %}
Todos os usuários podem visualizar listas de supressão, mas somente os usuários com [permissões de administrador]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=admin#list-of-permissions) podem criar e gerenciar listas de supressão.
{% endalert %}

1. Acesse **Público** > **Listas de supressão**.<br><br>![A página "Suppression Lists" (Listas de supressão) apresenta uma lista de três listas de supressão.]({% image_buster /assets/img/suppression_lists_home.png %})<br><br>
2. Selecione **Criar lista de supressão** e adicione um nome.<br><br>![Uma janela chamada "Create a Suppression List" (Criar uma lista de supressão) com um campo para inserir um nome.]({% image_buster /assets/img/create_suppression_list.png %}){: style="max-width:80%;"}<br><br>
3. Use filtros de segmento para identificar os usuários em suas listas de supressão. Você deve selecionar pelo menos um.

{% alert important %}
Embora o processo de configuração pareça semelhante ao da [criação de segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), uma lista de supressão é um grupo de usuários para os quais **não** se deseja enviar mensagens, independentemente da associação ao segmento.
{% endalert %}

![Um criador de listas de supressão com um filtro para usuários que abriram um e-mail pela última vez há mais de 90 dias.]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4\. Determine se deseja ter exceções com base na tag marcando a caixa abaixo do nome do segmento (consulte [Por que usar listas de supressão?](#why-use-suppression-lists) para obter mais informações) e, em seguida, adicione as tags de campanhas ou Canvas que os usuários dessa lista de supressão ainda devem receber. <br><br>Em outras palavras, se você adicionar a tag de exceção "Shipping confirmation" (Confirmação de envio), os usuários da sua lista de supressão serão excluídos de todos os envios de mensagens, exceto aqueles que usam a tag "Shipping confirmation" (Confirmação de envio).<br><br>![A seção "Shipping List Details" com uma tag de exceção aplicada chamada "Shipping confirmation".]({% image_buster /assets/img/exception_tags.png %})<br><br>
5\. Salve ou ative sua lista de supressão.
- Quando você salvar, sua lista de supressão será salva, mas não será ativada, o que significa que não entrará em vigor. Sua lista de supressão permanecerá inativa até que você a ative, e as listas de supressão inativas não afetarão o envio de mensagens (os usuários não serão excluídos das mensagens).
- Ao ser ativada, sua lista de supressão será salva e entrará em vigor imediatamente, o que significa que os usuários em sua lista de supressão serão imediatamente excluídos de campanhas ou Canvas (exceto os que contêm uma tag de exceção).

{% alert note %}
Somente os administradores podem salvar ou ativar listas de supressão. Você pode ter até cinco listas de supressão ativas por vez na versão beta.
{% endalert %}

Você pode desativar ou arquivar listas de supressão quando não precisar mais delas. 
- Para desativar, selecione uma lista de supressão ativa e selecione **Desativar**. As listas de supressão desativadas podem ser reativadas posteriormente.
- Para arquivar, faça isso na página **Listas de supressão**.

## Uso da lista de supressão

Para verificar se a lista de supressão impediu que um usuário recebesse uma mensagem, use a **Pesquisa de usuários** na etapa do **público-alvo** em sua campanha ou no Canva. Aqui, você poderá ver de qual lista de supressão eles fazem parte.

![Janela "User Lookup" mostrando que um usuário está em uma lista de supressão.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

{% alert tip %}
Você também pode encontrar listas de supressão aplicadas na etapa **Resumo**.
{% endalert %}

Ao criar uma campanha ou um Canva, use a **pesquisa de usuário** na etapa do **público-alvo** para procurar um usuário e, se ele não estiver no público-alvo, você poderá ver a lista de supressão da qual ele faz parte. 

![Janela "User Lookup" mostrando que um usuário está em uma lista de supressão.]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}

### Campanha interrompida 

Se um usuário estiver em uma lista de supressão, ele não receberá uma campanha à qual essa lista de supressão se aplica. Consulte [Tipos de mensagens e canais afetados por listas de supressão](#message-types-and-channels-affected-by-suppression-lists) para saber os casos em que uma lista de supressão não se aplica.

![A seção "Listas de supressão" com uma lista de supressão ativa, chamada "Pontuações baixas de integridade de marketing".]({% image_buster /assets/img/active_suppression_list.png %})

### Canva 

A partir do momento em que um usuário é adicionado a uma lista de supressão, ele não entrará no Canvas. Se eles já tiverem entrado em um Canva, não receberão as etapas do Mensagens. Isso significa que, se um usuário já estiver dentro de um Canvas quando for adicionado a uma lista de supressão, ele avançará pelo Canvas até a próxima etapa de mensagens, momento em que sairá sem receber a etapa de mensagens. 

Por exemplo, digamos que um Canva tenha uma etapa de Atualização do usuário seguida de uma etapa de Mensagem. Se um usuário entrar no Canva e, em seguida, for adicionado a uma lista de supressão, ele ainda passará pela etapa de Atualização do usuário (onde poderá ser atualizado) e, em seguida, sairá na etapa de Mensagens, momento em que será incluído nas métricas de saída.
