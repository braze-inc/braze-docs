---
nav_title: Medição do tamanho do segmento
article_title: Medição do tamanho do segmento
page_order: 5
page_type: reference
tool: 
- Segments
description: "Esta página aborda como você pode monitorar a associação e o tamanho do seu segmento."
---

# Medição do tamanho do segmento

> Esta página aborda como você pode monitorar a associação e o tamanho do seu segmento.

## Cálculo de associação de segmentos

O Braze atualiza a associação do segmento do usuário à medida que os dados são enviados de volta aos nossos servidores e processados, normalmente de forma instantânea. A associação de segmento de um usuário não será alterada até que a sessão seja processada. Por exemplo, um usuário que cair em um segmento de usuário expirado quando a sessão for iniciada será imediatamente removido do segmento de usuário expirado quando a sessão for processada.

### Cálculo do total de usuários acessíveis

Cada segmento exibe o número total de usuários que são membros desse segmento. Ao filtrar **Usuários de todos os apps**, ele também exibe alguns dos canais de envio de mensagens usados com mais frequência (como web push ou e-mail) e o número de usuários acessíveis para esses canais específicos. 

É possível que o número total de usuários seja diferente do número de usuários alcançáveis por cada canal. Além disso, nem todos os canais estão listados na tabela de usuários acessíveis. Por exemplo, os cartões de conteúdo, webhooks e WhatsApp não são mostrados no detalhamento. Isso significa que a contagem total de usuários acessíveis pode ser maior do que a soma dos usuários de cada canal exibido.

![Uma tabela que exibe o total de usuários acessíveis divididos por usuários acessíveis por e-mail, iOS push, Android push, web push e Kindle push.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Para que um usuário seja listado como acessível por meio de um determinado canal, ele deve ter ambos:
* Um endereço de e-mail válido ou um token por push associado ao seu perfil; e
* Aceitação ou assinatura do seu app.

Um único usuário pode pertencer a diferentes grupos de usuários acessíveis. Por exemplo, um usuário pode ter um endereço de e-mail válido e um token por push válido para Android e ter aceitação em ambos, mas não ter um token por push para iOS associado. A diferença entre o total de usuários alcançáveis e a soma dos diferentes canais é o número de usuários que se qualificaram para o segmento, mas não são alcançáveis por meio desses canais de comunicação.

## Estatísticas para o tamanho do segmento

As estatísticas estimadas são aproximadas pela amostragem de apenas uma parte do seu segmento, portanto, você deve esperar ver tamanhos estimados maiores ou menores do que o valor real, com espaços de trabalho maiores apresentando margens de erro potencialmente maiores. Para obter uma contagem precisa de usuários em seu segmento, selecione **Calculate Exact Statistics (Calcular estatísticas exatas**). A associação exata do segmento sempre será calculada antes que um segmento seja afetado por uma mensagem enviada em uma campanha ou Canva. 

A Braze fornece as seguintes estatísticas sobre o tamanho do segmento. 

### Filtrar estatísticas

Para cada grupo de filtros, é possível visualizar os usuários alcançáveis estimados. Selecione **Expandir estatísticas extras do funil** para ver um detalhamento entre os canais.

![Um grupo de filtros com um filtro para usuários que tiveram exatamente uma contagem de sessões.]({% image_buster /assets/img_archive/segment_filter_stats.png %}){: style="max-width:80%;"}

## Estimativa de usuários alcançáveis

É possível visualizar os usuários alcançáveis estimados de um segmento inteiro, incluindo as contagens de usuários estimadas para cada canal, no painel lateral **Reachable users (Usuários alcançáveis** ). Essa **estimativa** mostra um intervalo aproximado para o tamanho do seu segmento e uma estimativa da porcentagem da sua base geral de usuários que se enquadra nesse segmento. Note que as estatísticas estimadas são armazenadas em cache por 15 minutos, a menos que você faça edições em seu segmento, caso em que as estatísticas estimadas serão atualizadas automaticamente. Também é possível visualizar uma contagem exata de usuários acessíveis (para o segmento geral e por canal) selecionando **Calculate exact statistics (Calcular estatísticas exatas**). 


![O painel "Reachable users" (Usuários acessíveis) informa que há uma estimativa de 2,3 milhões a 2,4 milhões de usuários.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Considerações sobre a contagem de estimativas

O Braze mede o número de usuários estimados por meio de consultas a um subconjunto de seus usuários e, em seguida, extrapola esses resultados para todo o seu público. Como o subconjunto de usuários que o Braze consulta pode ser diferente a cada vez que calculamos essa estimativa, a estimativa também pode mudar nos casos em que a associação do seu público tecnicamente deveria ter permanecido a mesma. Por exemplo, se você reordenar seus filtros ou verificar novamente o mesmo segmento em um momento diferente, é possível que a contagem estimada mude (mesmo que **o Calculate exact stats** revele os mesmos resultados se o segmento não tiver mudado).

Se houver uma grande população de usuários em seu espaço de trabalho, poderá haver mais variação entre as contagens estimadas em comparação com as contagens exatas do cálculo, especialmente nos casos em que o segmento é uma porcentagem muito pequena da população geral do espaço de trabalho. Isso ocorre porque o Braze mede a estimativa consultando um subconjunto de seus usuários e extrapolando os resultados para toda a sua base de usuários. Para bases de usuários maiores, é de se esperar diferenças maiores entre as contagens estimadas e exatas.

Segmentos muito pequenos terão um intervalo estimado que inclui 0, o que significa que a porcentagem do total de usuários pode ser arredondada para 0. Nesses casos, o **recurso Calcular estatísticas exatas** o ajudará a ver uma contagem precisa do tamanho do seu segmento, que pode não ser realmente 0.

![O painel lateral "Reachable users" (Usuários acessíveis).]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Usuários alcançáveis por canal

Para visualizar o número de usuários que estão acessíveis para cada canal de envio de mensagens, selecione **Mostrar detalhamento** no painel **Usuários acessíveis**. Isso exibe alguns dos canais de envio de mensagens usados com mais frequência (como web push ou e-mail) e o número de usuários acessíveis para esses canais específicos. 

A métrica _Total_ representa usuários únicos. Por exemplo, se um usuário tiver tanto o Android push quanto o iOS push, ele será contado para ambas as linhas, mas contará apenas como 1 usuário na linha _Total_.

No entanto, é possível que o número total de usuários seja diferente da soma dos usuários acessíveis por cada canal, pois um único usuário pode pertencer a diferentes grupos de usuários acessíveis. Por exemplo, um usuário pode ter um endereço de e-mail válido e um token por push válido para Android e ter aceitação em ambos, mas não ter um token por push para iOS associado. 

Lembre-se de que nem todos os canais estão listados na tabela de **usuários acessíveis** (como cartões de conteúdo, webhooks e WhatsApp). Por exemplo, se você tiver usuários acessíveis apenas pelo Whatsapp, eles serão refletidos no _Total_, mas não em nenhuma das linhas específicas do canal. Isso significa que a contagem total de usuários acessíveis pode ser diferente da soma dos usuários de cada canal exibido.

Nos casos em que o _Total_ é maior do que a soma dos canais, a lacuna representa o número de usuários que se qualificaram para o segmento, mas que não podem ser alcançados por meio desses canais de comunicação.

Para que um usuário seja listado como acessível por meio de um determinado canal, ele deve ter:
- Um endereço de e-mail válido ou um token por push associado ao seu perfil, e
- Aceitação ou assinatura do seu app.

## Cálculo de estatísticas exatas 

Para visualizar uma contagem precisa do número de usuários em seu segmento, selecione **Calculate exact stats (Calcular estatísticas exatas** ) no painel **Reachable users (Usuários alcançáveis** ).

Para atualizar as estatísticas de um cálculo que você executou anteriormente, selecione **Refresh exact statistics (Atualizar estatísticas exatas**). A data em que esse cálculo foi executado pela última vez será atualizada automaticamente.

Note que a precisão de um cálculo é de apenas 99,999% ou mais. Portanto, para segmentos grandes, você pode notar pequenas variações, mesmo ao calcular estatísticas exatas, o que é um comportamento normal. Além disso, os resultados das estatísticas exatas são armazenados em cache por 24 horas, a menos que você faça edições em seu segmento, caso em que poderá recalcular as estatísticas exatas.

![O painel "Reachable users" (Usuários acessíveis) com uma opção para mostrar o detalhamento.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

As estatísticas em um nível por filtro sempre serão estimadas, mesmo que você calcule estatísticas exatas. **Calcular estatísticas** exatas calcula apenas as estatísticas exatas no nível do segmento, não no nível do filtro ou do grupo de filtros. Esse cálculo pode levar alguns minutos para ser executado. Os espaços de trabalho maiores, em particular, podem exigir períodos mais longos para concluir os cálculos. Você pode rastrear seu progresso na barra de progresso no painel de **usuários Reachable**. Quando se espera que um cálculo dure mais de cinco minutos, o Braze enviará os resultados por e-mail. 

O Braze prioriza um cálculo de cada vez por espaço de trabalho, portanto, a execução de vários cálculos ao mesmo tempo causará postergação. Você pode selecionar **View calculation queue (Exibir fila de cálculo** ) para ver quais segmentos estão à frente do seu, o progresso deles e o iniciador, e ter uma ideia de quando seu cálculo pode ser priorizado.

![Uma fila de cálculo com um cálculo.]({% image_buster /assets/img_archive/calculation_queue.png %})

Você pode cancelar um cálculo de estatística exata selecionando **Cancel (Cancelar**). Isso pode ser útil se houver vários cálculos na fila e você quiser priorizar outro cálculo primeiro. 

![Um cálculo ativo com a opção de cancelar]({% image_buster /assets/img_archive/cancel_calculation.png %}){: style="max-width:25%"}

## Visualização do histórico do tamanho da associação do segmento

Para todos os segmentos, você pode visualizar um gráfico histórico de associação que mostra a associação estimada do segmento para cada dia. Este gráfico mostra como o tamanho de seu segmento mudou ao longo do tempo. Use o menu suspenso para filtrar a associação ao segmento por intervalo de datas.

![Use o menu suspenso Associação histórica para filtrar a associação do segmento por intervalo de datas.]({% image_buster /assets/img_archive/historical_membership2.png %})

Como o objetivo desse gráfico é dar a você uma noção das tendências gerais de associação ao segmento, a contagem diária é uma estimativa, da mesma forma que o tamanho do segmento é uma estimativa antes de você selecionar **Calculate Exact Statistics (Calcular estatísticas exatas**). E como esse gráfico mostra estimativas, é possível que o tamanho do seu segmento apareça como "0" nesse gráfico, embora seu tamanho real (que pode ser determinado após a seleção de **Calculate Exact Stats**) não seja "0". É especialmente provável que o gráfico mostre uma estimativa de "0" se seu segmento for muito pequeno em relação ao tamanho da população de seu espaço de trabalho.

O Braze estima a contagem de membros do segmento consultando um subconjunto de seus usuários e, em seguida, extrapolando esses resultados para todo o seu público. Isso significa que os resultados do gráfico fornecem apenas uma estimativa do número de membros do segmento naquele dia, e espera-se que também flutue diariamente porque uma amostra diferente de usuários pode ser consultada para essa estimativa a cada dia.

{% alert note %}
Todas as estimativas podem ser maiores ou menores do que o valor mostrado em aproximadamente 1% do tamanho total da população de seu espaço de trabalho. Espaços de trabalho maiores com mais usuários têm mais probabilidade de ter estimativas que podem diferir dos cálculos exatos por um valor numérico maior, mesmo que a diferença ainda seja de 1% da população de usuários do espaço de trabalho. Isso significa que é de se esperar que haja diferenças maiores entre as estimativas e as contagens exatas entre os grandes espaços de trabalho.
{% endalert %}

### Razões para mudanças significativas

O número de associados pode mudar significativamente por vários motivos, como os apresentados nesta tabela.

| Motivo | Exemplo |
| --- | --- |
| Comportamento normal do usuário | Os usuários se inscrevem após uma campanha particularmente bem-sucedida. |
| A importação de usuários é feita por CSV | Foi importado um arquivo CSV de usuários que aumentou significativamente o número de membros do segmento. |
| Os critérios de público do segmento são modificados | As regras de público de um segmento existente (como filtros) foram alteradas, causando mudanças significativas na associação do segmento. |
| Os usuários são excluídos | Um número significativo de usuários foi excluído. |
| Uma integração com parceiros sincronizada com o Braze | Um terceiro enviou dados para a Braze que influenciaram significativamente a associação ao segmento. |
| Os usuários inativos são arquivados | Um número significativo de perfis inativos foi arquivado. Por exemplo, um grande número de usuários importados de CSV nunca registra atividades e é arquivado ao mesmo tempo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
