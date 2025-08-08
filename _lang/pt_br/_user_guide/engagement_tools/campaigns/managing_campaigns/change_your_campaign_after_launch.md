---
nav_title: Como editar sua campanha após o lançamento
article_title: Como editar sua campanha após o lançamento
page_order: 1
tool: Campaigns
page_type: reference
description: "Este artigo de referência apresenta uma visão geral do resultado da edição de determinados aspectos de uma campanha após o lançamento."

---

# Edição de sua campanha após o lançamento

> Este artigo apresenta uma visão geral do resultado da edição de determinados aspectos de uma campanha após o lançamento.

## Interromper sua campanha

Para parar uma campanha, abra sua página de **Detalhes da Campanha** e selecione **Parar Campanha**. Quando uma campanha é interrompida:

- Mensagens agendadas para serem enviadas serão canceladas.
- Testes A/B onde o teste inicial já foi enviado serão cancelados permanentemente.
- Eventos para mensagens que já foram enviadas (por exemplo, cliques abertos) ainda serão rastreados.

Para reiniciar sua campanha, selecione **Retomar**. Sua campanha continuará enviando mensagens e testes A/B, mas quaisquer mensagens perdidas não serão reenviadas ou reprogramadas.

## Campanhas disparadas

Todas as alterações em campanhas de entrega baseada em ação e campanhas de entrega acionadas por API entram em vigor imediatamente para envios futuros. 

Se essas campanhas foram acionadas, mas ainda não enviadas (por exemplo, uma campanha de entrega baseada em ação com um atraso de 1 dia é editada durante o período de atraso de 1 dia), consulte as seguintes orientações para campanhas agendadas.

### Campanhas programadas

Se precisar fazer alterações em uma campanha após o lançamento, observe os seguintes itens ao editar sua campanha para verificar se as alterações têm os efeitos desejados.

### Conteúdo das mensagens

Quaisquer alterações no conteúdo da mensagem (incluindo títulos, corpos e imagens) entram em vigor imediatamente ao salvar para todos os envios de mensagens futuros. Não é possível alterar o conteúdo de mensagens que já foram despachadas.

### Programação e público

Se você editar o horário de envio programado ou o público da sua campanha, essas alterações serão refletidas na campanha real imediatamente.

### Taxa de envio

Ao usar um limite de frequência de envio, o Braze "agenda" suas mensagens em intervalos de tempo de granularidade de minutos; portanto, se você quiser alterar a frequência de envio de mensagens, siga o processo a seguir para fazer alterações imediatas.

## Fazer mudanças imediatas

Se você precisar que as alterações entrem em vigor imediatamente, faça o seguinte:

1. Interrompa a campanha afetada.
2. Duplicar a campanha.
3. Faça edições na campanha duplicada.

{% alert important %}
Isso redefine a elegibilidade para as pessoas que já receberam a campanha original, portanto, talvez seja necessário filtrar a campanha duplicada para as pessoas que não receberam a original.
{% endalert %}

## Salvando rascunhos de campanhas ativas {#campaign-drafts}

Rascunhos são ótimos para fazer alterações em larga escala em campanhas ativas. Ao criar um rascunho, você pode testar alterações planejadas antes do seu próximo lançamento.

{% alert note %}
Uma campanha só pode ter um rascunho por vez. Além disso, análises não estão disponíveis, pois as alterações rascunhadas ainda não foram lançadas.
{% endalert %}

Para criar um rascunho, faça o seguinte:

1. Acesse sua campanha ativa.
2. Faça suas alterações.
3. Selecione **Salvar como Rascunho**. Observe que, após criar um rascunho, você não pode editar a campanha ativa até que você lance ou descarte seu rascunho.

![Um rascunho de uma campanha ativa com uma opção para visualizar a campanha ativa.]({% image_buster /assets/img/campaign_draft.png %})

Enquanto você faz edições no rascunho, você também pode consultar a campanha ativa no cabeçalho do rascunho da campanha ou no rodapé da análise da campanha. 

Para retornar a uma campanha ativa, selecione **Editar rascunho** na exibição de análise de dados ou na exibição de campanha ativa.

### Priorização de mensagens no app

A prioridade das mensagens no app será atualizada imediatamente (antes do lançamento do rascunho) quando você selecionar **Definir prioridade exata** e especificar a prioridade em relação a outras campanhas ou Canvas.
