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

Para interromper uma campanha, abra a página **Detalhes da campanha** e selecione o botão **Interromper campanha** no canto inferior direito da página. Quando uma campanha é interrompida:
- O envio de mensagens programadas para serem enviadas será cancelado
- Os Testes A/B em que o teste inicial já foi enviado serão permanentemente cancelados
- Os eventos para mensagens que já foram enviadas (por exemplo, cliques abertos) ainda serão rastreados
- As campanhas podem ser reiniciadas clicando em **Resume**

Uma vez retomada, essa campanha continuará enviando mensagens e Testes A/B, mas as mensagens perdidas não serão reenviadas ou reagendadas.

## Campanhas disparadas

Todas as alterações nas campanhas de entrega baseada em ação e nas campanhas de entrega disparada por API entram em vigor imediatamente para envios futuros.

Se essas campanhas tiverem sido disparadas, mas ainda não tiverem sido enviadas (por exemplo, uma campanha de entrega baseada em ação com uma postergação de 1 dia é editada durante o período de 1 dia de postergação), consulte a seguinte orientação para campanhas programadas.

## Campanhas programadas

Se precisar fazer alterações em uma campanha após o lançamento, observe os seguintes itens ao editar sua campanha para verificar se as alterações têm os efeitos desejados.

### Conteúdo das mensagens

Todas as alterações no conteúdo da mensagem (incluindo títulos, corpos, imagens etc.) entram em vigor imediatamente ao serem salvas para todos os envios de mensagens futuros. Não é possível alterar o conteúdo das mensagens que já foram enviadas.

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
