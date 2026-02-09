---
nav_title: Critérios de saída
article_title: Critérios de saída 
page_order: 4.1
alias: /exit_criteria/
page_type: reference
description: "Este artigo de referência aborda os critérios de saída e como os usuários podem sair do seu Canva com base nos critérios selecionados."
tool: Canvas
---

# Critérios de saída

> Ao adicionar eventos de exceção diretamente às regras de entrada do Canvas, seus usuários podem sair do Canvas assim que o evento ocorrer no final da etapa do canva. Isso ajuda a obter uma abordagem mais direcionada para o envio de mensagens do Canva para seu público.

### Como os usuários saem

Depois de executar o evento de saída, os usuários saem do Canva assim que a etapa do canva em que estão atualmente for encerrada. Por exemplo, se um usuário estiver em uma etapa de postergação por 30 dias e realizar o evento de saída no primeiro dia da etapa de postergação, o usuário não sairá do Canva por mais 29 dias.

Vamos considerar outro exemplo ao usar critérios de saída baseados em tempo. Um usuário insere uma etapa de postergação definida como 24 horas em 1º de julho às 12 horas. Nesse período de postergação, eles realizam o evento de saída "Última compra feita há menos de 1 hora" às 3h. Esse usuário será avaliado quanto aos critérios de saída em 2 de julho, às 12 horas, que é a conclusão da duração da etapa de postergação. Como já se passaram 21 horas desde a compra realizada em 1º de julho às 3h da manhã, eles não sairão da etapa do canva porque não fizeram uma compra dentro de uma hora após a saída da etapa de postergação em 2 de julho. Isso afeta o "Total de saídas por critérios de saída" na análise de dados do Canvas, que só é atualizada depois que um usuário sai totalmente do Canvas.

## Definição de critérios de saída

Na etapa do **público-alvo** do construtor do Canvas, é possível configurar critérios de saída para identificar quais usuários você deseja que saiam do Canvas. 

Os critérios de saída incluem um evento de exceção, que é a ação específica que pode fazer com que os usuários saiam do Canva.

![Os critérios de saída configurados para reengajar os usuários que navegaram pelos produtos, mas ainda não os adicionaram ao carrinho ou fizeram um pedido.]({% image_buster /assets/img/exit_criteria.png %}){: style="max-width:90%;"}

### Seleção de eventos de exceção {#exception-events}

Quando um usuário executa o evento de exceção, ele sairá do Canva. Note que os eventos de exceção só dispararão saídas quando um usuário estiver na tela e avançando na jornada do usuário.

Digamos que você tenha uma tela configurada para promover um novo produto. Nesse caso, a compra do produto seria o evento de exceção. Dessa forma, depois que o usuário fizer a compra, ele não receberá mais mensagens sobre um produto que já comprou. Os eventos de exceção mantêm seu envio de mensagens relevante e personalizado.

Outros eventos de exceção incluem:

- Fazer uma compra
- Iniciar uma sessão
- Realização de um evento personalizado
- Realização de um evento de conversão
- Adição de um endereço de e-mail
- Alteração de um valor de atributo personalizado
- Atualização do status de uma inscrição
- Atualização do status de um grupo de inscrições
- Interagindo com uma campanha
- Inserção de um local
- Como disparar um geofence
- Envio de mensagens SMS de entrada
- Envio de mensagens de entrada do WhatsApp
- Envio de mensagens de entrada LINE
- Execução de um evento de atualização de carrinho
- Performance de um evento de checkout concluído
- Performance de um evento de checkout iniciado

#### Etapas programadas

Se uma etapa do Canva estiver programada, o usuário sairá imediatamente do Canvas após a ocorrência do evento de exceção. Digamos que um usuário entre em um Canva em que a primeira etapa tem uma postergação de uma semana e um evento de exceção. Se o usuário realizar o evento de exceção no dia 5, ele sairá imediatamente após realizar o evento de exceção (no dia 5). 
 
#### Etapas disparadas

Se uma etapa do Canva for acionada por um evento, o último envio programado enfileirado a partir desse disparo será cancelado, mas o usuário permanecerá dentro do Canvas durante a janela. Isso significa que o usuário ainda poderá receber a etapa se executar o evento de gatilho novamente dentro da janela. Depois que a janela passar, o usuário sairá do Canva.

### Uso de segmentos e filtros

Você também pode adicionar segmentos e filtros nos critérios de saída. Isso significa que os usuários que corresponderem ao segmento e ao filtro sairão do Canva e não receberão mais nenhum envio de mensagens. 

Por exemplo, se a primeira etapa de um Canva for uma etapa de Atraso com uma postergação de cinco dias, os critérios de saída serão aplicados no final dessa etapa. Portanto, se um usuário atender aos critérios de saída, ele sairá ao final dos cinco dias.

{% alert note %}
Atualmente, não há suporte para atribuições de matriz como critérios de saída em eventos de exceção.
{% endalert %}

### Ter o mesmo evento de saída e de conversão

Quando o evento de saída e o evento de conversão forem os mesmos, os eventos de conversão e de saída serão contabilizados. Por exemplo, se um Canvas tiver uma etapa de postergação e um usuário performar os critérios de saída enquanto estiver nessa etapa de postergação, o evento de saída será incrementado assim que o usuário sair da etapa de postergação. A conversão também será incrementada assim que o evento for registrado no perfil do usuário.

As conversões são rastreadas mesmo após o término do Canvas, mas as saídas não são rastreadas quando o usuário sai do Canvas. A janela de conversão se estende por três dias além da duração máxima do Canva. Isso significa que as conversões continuarão a ser rastreadas depois que as saídas deixarem de ser rastreadas. 

O tempo mínimo para uma janela de conversão é de cinco minutos. Defina as janelas de conversão para cinco minutos em seus eventos de conversão para chegar o mais próximo possível da paridade com os eventos de saída. Também recomendamos configurar a janela de conversão para que corresponda, pelo menos, à jornada mais longa no Canva.

Considere o seguinte exemplo sobre como as análises de dados são calculadas:

1. Dez usuários passam pelo Canva.
2. Três usuários realizam o evento de conversão em cinco minutos (o número de eventos de saída é três e o número de eventos de conversão é três).
3. Outros cinco usuários saem do Canvas após cinco minutos, mas realizam o evento de conversão após dois dias (o número de eventos de saída permanece o mesmo, mas o evento de conversão aumenta para oito).
4. Os dois últimos usuários saem do Canva após cinco minutos, mas não realizam o evento de conversão, ou o realizam após três dias e cinco minutos (eles não são contados nos eventos de saída nem nas métricas de eventos de conversão).

## Exemplo

Digamos que queremos direcionar os usuários que ainda não fizeram nenhuma compra em nossa empresa de suprimentos para mochilas. Para configurar os critérios de saída, faríamos o seguinte:

1. Selecione **Make Purchase (Fazer compra)** como o evento de exceção.
2. Selecione **Add Trigger (Adicionar disparo**). 
3. Em **Segments (Segmentos**), selecione **Used in last day (Usado no último dia** ) para que, quando nosso Canva for lançado, o público exclua os usuários que fizeram compras.
4. Para **Filtros**, selecione **Comportamento de compra** > **Número de compras** > **Produto comprado**.
5. Defina o grupo de filtros como `backpack-example exactly 1`. Isso significa que os usuários que compraram nosso produto de mochila sairiam do Canva.

![Configurações de critérios de saída com "Makes Any Purchase" como o evento de exceção, portanto, se um usuário fizer uma compra, ele sairá desse Canva.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}


