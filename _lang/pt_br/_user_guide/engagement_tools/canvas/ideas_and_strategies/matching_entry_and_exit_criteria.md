---
nav_title: Correspondência de critérios de saída com eventos de entrada
article_title: Correspondência de critérios de saída com eventos de entrada
page_order: 5
page_type: tutorial
description: "Saiba como configurar critérios de saída e jornadas de ação que comparam propriedades de eventos com propriedades de entrada do canva, para que os usuários só saiam ou sigam uma ramificação quando concluírem a ação específica com a qual entraram."
tool: Canvas
---

# Correspondência de critérios de saída com eventos de entrada

> Este artigo aborda como configurar critérios de saída e jornadas de ação que se correlacionam diretamente com o evento de entrada do canva, para que os usuários só saiam ou sigam uma ramificação quando realizarem uma ação específica relacionada ao motivo pelo qual entraram no canva.

Ao comparar propriedades de eventos com [propriedades de entrada do canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/), você pode criar fluxos altamente direcionados. Por exemplo, em um canva de checkout abandonado, você pode configurar um usuário para sair somente quando ele comprar o item exato que abandonou, enquanto continua recebendo mensagens de lembrete se comprar um item diferente.

Essa abordagem usa [variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/) para comparar propriedades entre eventos. O padrão se aplica a muitos cenários além do eCommerce, incluindo renovações de apólices, lembretes de reservas e gerenciamento de inscrições.

## Critérios de saída: saindo do canva quando uma ação correspondente ocorre

Use [critérios de saída]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/) quando quiser que um usuário saia completamente do canva após realizar uma ação que corresponda ao evento de entrada.

### Exemplo: compra de ingresso abandonada

Neste cenário, um usuário entra no canva quando realiza o evento personalizado `Selected Ticket`, que contém uma propriedade chamada `event_id`. Os critérios de saída são configurados para que, quando um usuário dispara o evento personalizado `Purchased Ticket` — que também inclui uma propriedade chamada `event_id` — a propriedade do evento de saída seja comparada com a propriedade do evento de entrada. Se as duas corresponderem, o usuário sai do canva.

Isso significa:

- Se o usuário comprar o mesmo ingresso que selecionou originalmente, ele sai do canva e para de receber lembretes.
- Se o usuário comprar um ingresso diferente, ele permanece no canva e continua recebendo mensagens de acompanhamento sobre o ingresso original.

Para configurar isso:

1. Configure uma entrada de canva baseada em ação com o evento personalizado de gatilho (como `Selected Ticket`) e sua propriedade relevante (como `event_id`).
2. Na etapa **Público-alvo**, configure o evento de exceção dos critérios de saída com o evento personalizado de conclusão (como `Purchased Ticket`).
3. Selecione **Adicionar filtros de propriedade** e adicione um filtro onde a comparação da propriedade básica `event_id` esteja definida como `equals`.
4. Ative o toggle **Personalizar valor**, defina o **Tipo de personalização** como `Context Variables` e defina o **Atributo** como `event_id`.

Isso compara o `event_id` do evento `Purchased Ticket` com o `event_id` armazenado do evento de entrada original do canva. Para mais detalhes sobre como configurar esses filtros, consulte [Exemplos de critérios de saída]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#exit-criteria-examples).

## Jornadas de ação: ramificação baseada em uma ação correspondente

Use [jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) quando quiser que um usuário permaneça no canva, mas siga uma jornada diferente dependendo de se a ação subsequente corresponde ao evento de entrada.

### Exemplo: checkout abandonado com jornadas ramificadas

Neste cenário, um usuário que selecionou um item mas não concluiu a compra primeiro recebe uma mensagem de checkout abandonado. O usuário é então mantido em uma etapa de jornada de ação por uma semana antes de ser direcionado para três jornadas com base no que fez durante esse período:

- **Concluiu a compra original:** O ID da propriedade do evento personalizado é igual ao ID da propriedade de entrada. Esses usuários podem receber uma mensagem de agradecimento ou recomendação de venda cruzada.
- **Fez uma compra diferente:** O ID da propriedade do evento personalizado não é igual ao ID da propriedade de entrada. Esses usuários podem receber um lembrete sobre o item original.
- **Não fez uma compra:** Cai no grupo **Restante do público**. Esses usuários podem receber um incentivo mais forte ou lembrete final.

Para configurar isso:

1. Adicione uma etapa de [jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) e defina o período de avaliação (como uma semana).
2. Para o primeiro grupo de ação (compra original), adicione um gatilho para o evento personalizado de conclusão (como `Purchased_Ticket`). Selecione **Adicionar filtros de propriedade** e adicione um filtro onde a comparação da propriedade básica `event_id` esteja definida como `equals`. Ative **Personalizar valor**, defina o **Tipo de personalização** como `Context Variables` e defina o **Atributo** como `event_id`.
3. Para o segundo grupo de ação (compra diferente), adicione o mesmo evento de gatilho, mas defina a comparação como `does not equal` com a mesma configuração de variável de contexto.
4. Use o grupo **Restante do público** para usuários que não realizaram o evento de conclusão.

Para mais detalhes sobre como configurar esses filtros, consulte [Exemplos de jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#action-path-examples).

## Outras aplicações

Embora este artigo use um exemplo de compra abandonada, você pode aplicar o mesmo padrão a qualquer cenário em que uma ação de conclusão precise se correlacionar com a ação de entrada, incluindo:

- **Renovações de apólices:** Remova usuários que renovarem a apólice específica que disparou o canva.
- **Lembretes de reservas:** Ramifique usuários com base em se confirmaram ou modificaram a reserva original.
- **Gerenciamento de inscrições:** Direcione usuários de forma diferente dependendo de se fizeram upgrade do plano específico sobre o qual foram notificados.
- **Registros em eventos:** Remova usuários que concluírem o registro para o evento específico no qual demonstraram interesse.

## Informações importantes

- As configurações neste artigo são exemplos ilustrativos. Teste todos os componentes no seu ambiente de desenvolvimento antes de lançar.
- Verifique se os nomes das propriedades e os tipos de dados nos seus eventos de entrada correspondem aos usados nos seus critérios de saída ou jornadas de ação.
- Consulte [variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/) para detalhes sobre como as comparações de propriedades funcionam entre eventos.