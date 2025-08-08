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

### Uso de segmentos e filtros

Você também pode adicionar segmentos e filtros nos critérios de saída. Isso significa que os usuários que corresponderem ao segmento ou ao filtro sairão do Canva e não receberão mais nenhum envio de mensagens. 

Por exemplo, se a primeira etapa de um Canva for uma etapa de Atraso com uma postergação de cinco dias, os critérios de saída serão aplicados no final dessa etapa. Portanto, se um usuário atender aos critérios de saída, ele sairá ao final dos cinco dias.

{% alert note %}
Atualmente, não há suporte para atribuições de matriz como critérios de saída em eventos de exceção.
{% endalert %}

## Exemplo

Digamos que queremos direcionar os usuários que ainda não fizeram nenhuma compra em nossa empresa de suprimentos para mochilas. Para configurar os critérios de saída, faríamos o seguinte:

1. Selecione **Make Purchase (Fazer compra)** como o evento de exceção.
2. Selecione **Add Trigger (Adicionar disparo**). 
3. Em **Segments (Segmentos**), selecione **Used in last day (Usado no último dia** ) para que, quando nosso Canva for lançado, o público exclua os usuários que fizeram compras.
4. Para **Filtros**, selecione **Comportamento de compra** > **Número de compras** > **Produto comprado**.
5. Defina o grupo de filtros como `backpack-example exactly 1`. Isso significa que os usuários que compraram nosso produto de mochila sairiam do Canva.

![Configurações de critérios de saída com "Makes Any Purchase" como o evento de exceção, portanto, se um usuário fizer qualquer compra, ele sairá dessa tela.]({% image_buster /assets/img_archive/exit_criteria_example.png %}){: style="max-width:80%;"}


