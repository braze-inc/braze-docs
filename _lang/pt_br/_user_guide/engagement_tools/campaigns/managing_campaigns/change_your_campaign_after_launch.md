---
nav_title: Edite sua campanha após o lançamento
article_title: Edite Sua Campanha Após o Lançamento
page_order: 1
tool: Campaigns
page_type: reference
description: "Este artigo de referência apresenta uma visão geral do resultado da edição de determinados aspectos de uma campanha após o lançamento."

---

# Edite sua campanha após o lançamento

> Este artigo apresenta uma visão geral do resultado da edição de determinados aspectos de uma campanha após o lançamento.

## Interromper sua campanha

Para parar uma campanha, abra sua página de **Detalhes da Campanha** e selecione **Parar Campanha**. Quando uma campanha é interrompida:

- As mensagens programadas para serem enviadas serão canceladas.
- Os testes A/B em que o teste inicial já foi enviado serão cancelados permanentemente.
- Eventos para mensagens que já foram enviadas (por exemplo, cliques abertos) ainda serão rastreados.

Para reiniciar sua campanha, selecione **Retomar**. Sua campanha continuará enviando mensagens e testes A/B, mas quaisquer mensagens perdidas não serão reenviadas ou reprogramadas.

## Campanhas disparadas

Todas as alterações nas campanhas de entrega baseada em ação e nas campanhas de entrega acionadas por API entram em vigor imediatamente para envios futuros. 

Se essas campanhas foram acionadas, mas ainda não enviadas (por exemplo, uma campanha de entrega baseada em ação com um atraso de 1 dia é editada durante o período de atraso de 1 dia), consulte as orientações a seguir para campanhas programadas.

### Campanhas programadas

Se precisar fazer alterações em uma campanha após o lançamento, observe os seguintes itens ao editar sua campanha para verificar se as alterações têm os efeitos desejados.

### Conteúdo das mensagens

Quaisquer alterações no conteúdo das mensagens (incluindo títulos, corpos e imagens) entram em vigor imediatamente ao salvar para todos os envios de mensagens a partir de agora. Não é possível alterar o conteúdo das mensagens que já foram despachadas.

### Programação e público

Se você editar o horário de envio programado ou o público da sua campanha, essas alterações serão refletidas na campanha real imediatamente.

#### Considerações

Se sua campanha usa Inteligent Timing ou entrega em fuso horário local, edições no horário de envio programado não serão refletidas se a edição for feita dentro de 24 horas do horário de envio original. Isto é porque:

- **Intelligent Timing:** A Braze começa a calcular o horário de envio ideal à meia-noite, horário de Samoa. Se esse horário já passou, a mensagem começará a ser processada. Para saber mais, consulte [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_timing/).
- **Entrega em fuso horário local:** Editar uma campanha de fuso local que está programada para menos de 24 horas de antecedência não alterará o cronograma da mensagem. Para saber mais, consulte [Como agendar uma campanha em fuso horário local?]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign).

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

Rascunhos são ótimos para fazer alterações em larga escala em campanhas ativas. Ao criar um rascunho, você pode testar as alterações planejadas antes do seu próximo lançamento.

{% alert note %}
Uma campanha só pode ter um rascunho por vez. Além disso, a análise de dados não está disponível, pois as alterações rascunhadas ainda não foram lançadas.
{% endalert %}

Para criar um rascunho, faça o seguinte:

1. Acesse sua campanha ativa.
2. Faça suas alterações.
3. Selecione **Salvar como Rascunho**. Note que, após criar um rascunho, você não pode editar a campanha ativa até que você lance ou descarte seu rascunho.

![Um rascunho de uma campanha ativa com uma opção para visualizar a campanha ativa.]({% image_buster /assets/img/campaign_draft.png %})

Enquanto você faz edições no rascunho, também pode consultar a campanha ativa no cabeçalho do rascunho da campanha ou no rodapé da análise de dados da campanha. 

Para retornar a uma campanha ativa, selecione **Editar rascunho** na exibição de análise de dados ou na exibição de campanha ativa.

### Priorização de mensagens no app

A prioridade das mensagens no app será atualizada imediatamente (antes do lançamento do rascunho) quando você selecionar **Definir prioridade exata** e especificar a prioridade em relação a outras campanhas ou Canvas.
