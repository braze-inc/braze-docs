---
nav_title: Critérios de saída
article_title: Critérios de saída 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Este artigo de referência aborda os critérios de saída e como os usuários podem sair do Canvas com base nos critérios selecionados."
tool: Canvas
---

# Critérios de saída

> Ao adicionar eventos de exceção diretamente às regras de entrada do Canvas, seus usuários podem sair do Canvas assim que o evento ocorrer no final da etapa. Isso ajuda a obter uma abordagem mais direcionada para as mensagens do Canvas com seu público.

### Como os usuários saem

Depois de executar o evento de saída, os usuários saem do Canvas assim que a etapa em que estão atualmente tiver sido encerrada. Por exemplo, se um usuário estiver em uma etapa de Atraso por 30 dias e realizar o evento de saída no primeiro dia da etapa de Atraso, o usuário não sairá do Canvas por mais 29 dias.

Vamos considerar outro exemplo ao usar critérios de saída baseados em tempo. Um usuário insere uma etapa de atraso definida como 24 horas em 1º de julho às 12 horas. Nesse período de atraso, eles realizam o evento de saída "Última compra feita há menos de 1 hora" às 3h. Esse usuário será avaliado quanto aos critérios de saída em 2 de julho, às 12 horas, que é a conclusão da duração da etapa de Atraso. Como já se passaram 21 horas desde a compra feita em 1º de julho às 3h da manhã, eles não sairão do Canvas porque não fizeram uma compra dentro de uma hora após a saída da etapa de atraso em 2 de julho. Isso afeta o "Total Exits by Exit Criteria" (Total de saídas por critérios de saída) em suas análises do Canvas, que só são atualizadas depois que um usuário sai totalmente do Canvas.

## Definição de critérios de saída

Na etapa **Público-alvo** do construtor do Canvas, é possível configurar critérios de saída para identificar quais usuários você deseja que saiam do Canvas. 

Os critérios de saída incluem um evento de exceção, que é a ação específica que pode fazer com que os usuários saiam do Canvas.

O critério de saída configurado para reengajar os usuários que navegaram pelos produtos, mas ainda não os adicionaram ao carrinho ou fizeram um pedido.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Seleção de eventos de exceção {#exception-events}

Quando um usuário executar o evento de exceção, ele sairá do Canvas. Observe que os eventos de exceção só acionarão saídas quando um usuário estiver no Canvas e avançando na jornada do usuário.

Digamos que você tenha um Canvas configurado para promover um novo produto. Nesse caso, a compra do produto seria o evento de exceção. Dessa forma, depois que o usuário fizer a compra, ele não receberá mais mensagens sobre um produto que já comprou. Eventos de exceção mantêm suas mensagens relevantes e personalizadas.

Outros eventos de exceção incluem:

- Fazer uma compra
- Iniciar uma sessão
- Realização de um evento personalizado
- Realização de um evento de conversão
- Adição de um endereço de e-mail
- Alteração de um valor de atributo personalizado
- Atualização do status de uma assinatura
- Atualização do status de um grupo de assinaturas
- Interagindo com uma campanha
- Inserção de um local
- Acionamento de uma geofence
- Envio de uma mensagem SMS de entrada
- Envio de uma mensagem de entrada do WhatsApp
- Envio de uma mensagem de entrada LINE
- Realização de um evento de atualização de carrinho
- Realização de um evento de checkout concluído
- Realização de um evento de checkout iniciado

#### Etapas programadas

Se uma etapa do Canvas estiver programada, o usuário sairá imediatamente do Canvas após a ocorrência do evento de exceção. Digamos que um usuário entre em um Canvas em que a primeira etapa tenha um atraso de uma semana e um evento de exceção. Se o usuário realizar o evento de exceção no dia 5, ele sairá imediatamente após realizar o evento de exceção (no dia 5). 
 
#### Etapas acionadas

Se uma etapa do Canvas for acionada por um evento, o último envio programado enfileirado a partir desse acionador será cancelado, mas o usuário permanecerá dentro do Canvas enquanto durar a janela. Isso significa que o usuário ainda poderá receber a etapa se executar o evento de acionamento novamente dentro da janela. Depois que a janela passar, o usuário sairá do Canvas.

### Uso de segmentos e filtros

Você também pode adicionar segmentos e filtros nos critérios de saída. Isso significa que os usuários que corresponderem ao segmento e ao filtro sairão do Canvas e não receberão mais mensagens. 

Por exemplo, se a primeira etapa em um Canvas for uma etapa de Atraso com um atraso de cinco dias, os critérios de saída serão aplicados no final dessa etapa. Portanto, se um usuário atender aos critérios de saída, ele sairá ao final dos cinco dias.

{% alert note %}
No momento, não há suporte para atributos de matriz como critérios de saída em eventos de exceção.
{% endalert %}

### Ter o mesmo evento de saída e de conversão

Quando o evento de saída e o evento de conversão forem os mesmos, os eventos de conversão e de saída serão contabilizados. Por exemplo, se um Canvas tiver uma etapa de Atraso e um usuário executar os critérios de saída enquanto estiver nessa etapa de Atraso, o evento de saída será incrementado assim que o usuário sair da etapa de Atraso. A conversão também será incrementada assim que o evento for registrado no perfil do usuário.

As conversões são rastreadas mesmo após o término do Canvas, mas as saídas não são rastreadas quando o usuário sai do Canvas. A janela de conversão se estende por três dias além da duração máxima do Canvas. Isso significa que as conversões continuarão a ser rastreadas depois que as saídas deixarem de ser rastreadas. 

O tempo mínimo para uma janela de conversão é de cinco minutos. Defina as janelas de conversão para cinco minutos em seus eventos de conversão para chegar o mais próximo possível da paridade com os eventos de saída. Também recomendamos configurar a janela de conversão para que corresponda, no mínimo, ao caminho mais longo do Canvas.

Considere o exemplo a seguir sobre como as análises são calculadas:

1. Dez usuários passam pelo Canvas.
2. Três usuários realizam o evento de conversão em cinco minutos (o número de eventos de saída é três e o número de eventos de conversão é três).
3. Outros cinco usuários saem do Canvas após cinco minutos, mas realizam o evento de conversão após dois dias (o número de eventos de saída permanece o mesmo, mas o evento de conversão aumenta para oito).
4. Os dois últimos usuários saem do Canvas após cinco minutos, mas não realizam o evento de conversão, ou o realizam após três dias e cinco minutos (eles não são contados nos eventos de saída nem nas métricas de eventos de conversão).

## Exemplo

Digamos que queremos segmentar usuários que ainda não fizeram nenhuma compra em nossa empresa de suprimentos para mochilas. Para configurar os critérios de saída, faríamos o seguinte:

1. Selecione **Make Purchase (Fazer compra)** como o evento de exceção.
2. Selecione **Add Trigger**. 
3. Em **Segments (Segmentos**), selecione **Used in last day (Usado no último dia** ) para que, quando nosso Canvas for lançado, o público exclua os usuários que fizeram compras.
4. Para **Filtros**, selecione **Comportamento de compra** > **Número de compras** > **Produto comprado**.
5. Defina o grupo de filtros como `backpack-example exactly 1`. Isso significa que os usuários que compraram nosso produto de mochila sairiam do Canvas.

Configurações de critérios de saída com "Makes Any Purchase" como evento de exceção, portanto, se um usuário fizer uma compra, ele sairá desse Canvas.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}


