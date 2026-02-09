---
nav_title: Edite sua campanha após o lançamento
article_title: Edite sua campanha após o lançamento
page_order: 1
tool: Campaigns
page_type: reference
description: "Este artigo de referência apresenta uma visão geral do resultado da edição de determinados aspectos de uma campanha após o lançamento."

---

# Edite sua campanha após o lançamento

> Este artigo apresenta uma visão geral do resultado da edição de determinados aspectos de uma campanha após o lançamento.

## Interromper sua campanha

Para interromper uma campanha, abra a página **Detalhes da campanha** e selecione **Interromper campanha**. Quando uma campanha é interrompida:

- Os envios de mensagens programados para serem enviados serão cancelados.
- Os Testes A/B em que o teste inicial já foi enviado serão permanentemente cancelados.
- Os eventos de mensagens que já foram enviadas (por exemplo, cliques abertos) ainda serão rastreados.

Para reiniciar sua campanha, selecione **Resume (Continuar**). Sua campanha continuará enviando mensagens e Testes A/B, mas as mensagens perdidas não serão reenviadas ou reagendadas.

## Campanhas disparadas

Todas as alterações nas campanhas de entrega baseadas em ação e nas campanhas de entrega disparadas por API entram em vigor imediatamente para envios futuros. 

Se essas campanhas tiverem sido disparadas, mas ainda não tiverem sido enviadas (por exemplo, uma campanha de entrega baseada em ação com uma postergação de 1 dia é editada durante o período de 1 dia de postergação), consulte a seguinte orientação para campanhas programadas.

### Campanhas programadas

Se precisar fazer alterações em uma campanha após o lançamento, observe os seguintes itens ao editar sua campanha para verificar se as alterações têm os efeitos desejados.

### Conteúdo das mensagens

Todas as alterações no conteúdo da mensagem (incluindo títulos, corpos e imagens) entram em vigor imediatamente ao serem salvas para todos os envios de mensagens futuros. Não é possível alterar o conteúdo de mensagens que já foram enviadas.

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

## Salvar rascunhos de campanhas ativas {#campaign-drafts}

Os rascunhos são ótimos para fazer alterações em grande escala em campanhas ativas. Ao criar um rascunho, você pode testar as alterações planejadas antes do próximo lançamento.

{% alert note %}
Uma campanha só pode ter um rascunho por vez. Além disso, a análise de dados não está disponível, pois as alterações esboçadas ainda não foram lançadas.
{% endalert %}

Para criar um rascunho, faça o seguinte:

1. Acesse sua campanha ativa.
2. Faça suas alterações.
3. Selecione **Salvar como rascunho**. Observe que, depois de criar um rascunho, você não poderá editar a campanha ativa até lançar ou descartar o rascunho.

![Um rascunho de uma campanha ativa com uma opção para visualizar a campanha ativa.]({% image_buster /assets/img/campaign_draft.png %})

Ao fazer edições no rascunho, você também pode fazer referência à campanha ativa no cabeçalho do rascunho da campanha ou no rodapé da análise de dados da campanha. 

Para retornar a uma campanha ativa, selecione **Editar rascunho** na exibição de análise de dados ou na exibição de campanha ativa.

### Priorização de mensagens no app

A prioridade das mensagens no app será atualizada imediatamente (antes do lançamento do rascunho) quando você selecionar **Definir prioridade exata** e especificar a prioridade em relação a outras campanhas ou Canvas.
