---
nav_title: Edição de sua campanha após o lançamento
article_title: Como editar sua campanha após o lançamento
page_order: 1
tool: Campaigns
page_type: reference
description: "Este artigo de referência apresenta uma visão geral do resultado da edição de determinados aspectos de uma campanha após o lançamento."

---

# Edição de sua campanha após o lançamento

> Este artigo apresenta uma visão geral do resultado da edição de determinados aspectos de uma campanha após o lançamento.

## Interromper sua campanha

Para interromper uma campanha, abra a página **Detalhes da campanha** e selecione **Interromper campanha**. Quando uma campanha é interrompida:

- As mensagens programadas para serem enviadas serão canceladas.
- Os testes A/B em que o teste inicial já foi enviado serão permanentemente cancelados.
- Os eventos de mensagens que já foram enviadas (por exemplo, cliques abertos) ainda serão rastreados.

Para reiniciar sua campanha, selecione **Resume (Continuar**). Sua campanha continuará enviando mensagens e testes A/B, mas as mensagens perdidas não serão reenviadas ou reagendadas.

## Campanhas acionadas

Todas as alterações nas campanhas de entrega baseadas em ação e nas campanhas de entrega acionadas por API entram em vigor imediatamente para envios futuros. 

Se essas campanhas tiverem sido acionadas, mas ainda não tiverem sido enviadas (por exemplo, uma campanha de entrega baseada em ação com um atraso de 1 dia é editada durante o período de atraso de 1 dia), consulte as seguintes orientações para campanhas programadas.

### Campanhas programadas

Se você precisar fazer alterações em uma campanha após o lançamento, observe os itens a seguir ao editar a campanha para verificar se as alterações têm os efeitos desejados.

### Conteúdo da mensagem

Todas as alterações no conteúdo da mensagem (incluindo títulos, corpos e imagens) entram em vigor imediatamente ao serem salvas para todos os envios de mensagens futuros. Não é possível alterar o conteúdo de mensagens que já foram enviadas.

### Programação e público

Se você editar o horário de envio programado ou o público-alvo da sua campanha, essas alterações serão refletidas na campanha real imediatamente.

### Taxa de envio

Ao usar um limite de taxa de envio, o Braze "agenda" suas mensagens em intervalos de tempo de granularidade de minutos; portanto, se você quiser alterar a taxa de envio de mensagens, siga o processo a seguir para fazer alterações imediatas.

## Fazer mudanças imediatas

Se você precisar que as alterações entrem em vigor imediatamente, faça o seguinte:

1. Interrompa a campanha afetada.
2. Duplicar a campanha.
3. Faça edições na campanha duplicada.

{% alert important %}
Isso redefine a elegibilidade para as pessoas que já receberam a campanha original, portanto, talvez você precise filtrar a campanha duplicada para as pessoas que não receberam a original.
{% endalert %}

## Salvar rascunhos de campanhas ativas {#campaign-drafts}

Os rascunhos são ótimos para fazer alterações em grande escala em campanhas ativas. Ao criar um rascunho, você pode testar as alterações planejadas antes do próximo lançamento.

{% alert note %}
Uma campanha só pode ter um rascunho por vez. Além disso, as análises não estão disponíveis, pois as alterações redigidas ainda não foram lançadas.
{% endalert %}

Para criar um rascunho, faça o seguinte:

1. Vá para sua campanha ativa.
2. Faça suas alterações.
3. Selecione **Salvar como rascunho**. Observe que, após criar um rascunho, você não poderá editar a campanha ativa até que lance ou descarte o rascunho.

\![Um rascunho de uma campanha ativa com uma opção para visualizar a campanha ativa.]({% image_buster /assets/img/campaign_draft.png %})

Ao fazer edições no rascunho, você também pode fazer referência à campanha ativa no cabeçalho do rascunho da campanha ou no rodapé da análise da campanha. 

Para retornar a uma campanha ativa, selecione **Editar rascunho** na exibição de análise ou na exibição de campanha ativa.

### Priorização de mensagens no aplicativo

A prioridade das mensagens no aplicativo será atualizada imediatamente (antes do lançamento do rascunho) quando você selecionar **Definir prioridade exata** e especificar a prioridade em relação a outras campanhas ou Canvases.
