---
nav_title: Medir o tamanho do segmento
article_title: Medir o Tamanho do Segmento
page_order: 5
page_type: reference
tool: 
- Segments
description: "Esta página cobre como você pode monitorar a associação e o tamanho do seu segmento."
---

# Medir o tamanho do segmento

> Esta página cobre como você pode monitorar a associação e o tamanho do seu segmento.

## Cálculo da associação do segmento

O Braze atualiza a associação do segmento do usuário à medida que os dados são enviados de volta aos nossos servidores e processados, normalmente de forma instantânea. A associação de segmento de um usuário não será alterada até que a sessão seja processada. Por exemplo, um usuário que cair em um segmento de usuário expirado quando a sessão for iniciada será imediatamente removido do segmento de usuário expirado quando a sessão for processada.

### Cálculo do total de usuários acessíveis

Cada segmento exibe o número total de usuários que são membros desse segmento. Ao filtrar por **Usuários de todos os apps**, também exibe alguns dos canais de mensagens mais utilizados (como web push ou e-mail) e o número de usuários alcançáveis para esses canais específicos. 

É possível que o número total de usuários seja diferente do número de usuários alcançáveis por cada canal. Além disso, nem todos os canais estão listados na tabela de usuários alcançáveis. Por exemplo, Cartões de Conteúdo, webhooks e WhatsApp não são mostrados na divisão. Isso significa que o total de usuários alcançáveis pode ser maior do que a soma dos usuários para cada canal exibido.

![Uma tabela exibindo o total de usuários alcançáveis dividido por usuários alcançáveis por e-mail, push iOS, push Android, web push e push Kindle.]({% image_buster /assets/img_archive/segmenter_reachable_users.png %})

Para que um usuário seja listado como acessível por meio de um determinado canal, ele deve ter ambos:
* Um endereço de e-mail válido ou token por push associado ao seu perfil, e
* Optou por ou se inscreveu no seu app.

Um único usuário pode pertencer a diferentes grupos de usuários acessíveis. Por exemplo, um usuário pode ter um endereço de e-mail válido e um token por push válido para Android e ter aceitação em ambos, mas não ter um token por push para iOS associado. A diferença entre o total de usuários alcançáveis e a soma dos diferentes canais é o número de usuários que se qualificaram para o segmento, mas não estão alcançáveis através desses canais de comunicação.

## Estatísticas para o tamanho do segmento

Estatísticas estimadas são aproximadas por amostragem apenas uma parte do seu segmento, então você deve esperar ver tamanhos estimados que são maiores ou menores do que o valor real, com espaços de trabalho maiores vendo potencialmente margens de erro maiores. Para obter uma contagem precisa de usuários no seu segmento, selecione **Calcular Estatísticas Exatas**. A associação exata do segmento sempre será calculada antes que um segmento seja afetado por uma mensagem enviada em uma campanha ou Canvas. 

A Braze fornece as seguintes estatísticas sobre o tamanho do segmento. 

### Filtrar estatísticas

Para cada grupo de filtros, é possível visualizar os usuários alcançáveis estimados. Selecione **Expandir estatísticas extras do funil** para ver um detalhamento entre os canais.

![Um grupo de filtros com um filtro para usuários que tiveram exatamente uma contagem de sessão.]({% image_buster /assets/img_archive/segment_filter_stats.png %}){: style="max-width:80%;"}

## Estimativa de usuários alcançáveis

Você pode visualizar a estimativa de usuários alcançáveis de um segmento inteiro, incluindo contagens estimadas de usuários para cada canal, no painel lateral **Usuários Alcançáveis**. Esta **estimativa** mostra um intervalo aproximado para o tamanho do seu segmento e uma estimativa de que porcentagem da sua base de usuários geral se enquadra neste segmento. Observe que as estatísticas estimadas são armazenadas em cache por 15 minutos, a menos que você faça edições no seu segmento, caso em que as estatísticas estimadas serão atualizadas automaticamente. Você também pode ver uma contagem exata de usuários alcançáveis (tanto para o segmento geral quanto por canal) selecionando **Calcular estatísticas exatas**. 


![O painel "Usuários alcançáveis" informando que há 2,3M—2,4M de usuários estimados.]({% image_buster /assets/img_archive/reachable_users_side_panel.png %})

### Considerações para contagens estimadas

A Braze mede o número de usuários estimados consultando um subconjunto de seus usuários e, em seguida, extrapola esses resultados para todo o seu público. Como o subconjunto de usuários que a Braze consulta pode diferir a cada vez que calculamos essa estimativa, a estimativa também pode mudar em casos onde a sua adesão ao público tecnicamente deveria ter permanecido a mesma. Por exemplo, se você reordenar seus filtros ou reexaminar o mesmo segmento em um momento diferente, é possível que a contagem estimada mude (mesmo que **Calcular estatísticas exatas** revele os mesmos resultados se seu segmento não mudar).

Se você tiver uma grande população de usuários em seu espaço de trabalho, pode ver mais variação entre suas contagens estimadas em comparação com suas contagens de cálculo exatas, especialmente em casos onde seu segmento é uma porcentagem muito pequena da população total do seu espaço de trabalho. Isso ocorre porque a Braze mede a estimativa consultando um subconjunto de seus usuários e extrapolando os resultados para toda a sua base de usuários. Para bases de usuários maiores, diferenças maiores entre contagens estimadas e exatas são esperadas.

Segmentos muito pequenos terão uma faixa estimada que inclui 0, significando que a porcentagem de usuários totais pode arredondar para 0. Nesses casos, **Calcular estatísticas exatas** ajudará você a ver uma contagem precisa do tamanho do seu segmento, que pode não ser realmente 0.

![O painel lateral "Usuários alcançáveis".]({% image_buster /assets/img_archive/reachable_users_panel.png %})

### Usuários alcançáveis por canal

Para ver o número de usuários que são alcançáveis para cada canal de mensagem, selecione **Mostrar detalhamento** no painel **Usuários alcançáveis**. Isso exibe alguns dos canais de mensagem mais utilizados (como web push ou e-mail) e o número de usuários alcançáveis para esses canais específicos. 

A métrica _Total_ representa usuários únicos. Por exemplo, se um usuário tem tanto push Android quanto push iOS, ele será contado para ambas as linhas, mas contará como 1 usuário na linha _Total_.

No entanto, é possível que o número total de usuários seja diferente da soma de usuários alcançáveis por cada canal, já que um único usuário pode pertencer a diferentes grupos de usuários alcançáveis. Por exemplo, um usuário pode ter um endereço de e-mail válido e um token por push válido para Android e ter aceitação em ambos, mas não ter um token por push para iOS associado. 

Lembre-se, nem todos os canais estão listados na tabela **Usuários alcançáveis** (como Cartões de Conteúdo, webhooks e WhatsApp). Por exemplo, se você tiver usuários apenas alcançáveis através do Whatsapp, eles serão refletidos no _Total_ mas não em nenhuma das linhas específicas do canal. Isso significa que o total de usuários alcançáveis pode ser diferente da soma dos usuários para cada canal exibido.

Nos casos em que o _Total_ é maior do que a soma dos canais, a diferença representa o número de usuários que se qualificaram para o segmento, mas não estão acessíveis através desses canais de comunicação.

Para que um usuário seja listado como alcançável através de um determinado canal, o usuário deve ter:
- Um endereço de e-mail válido ou token por push associado ao seu perfil, e
- Optou por ou se inscreveu no seu app.

#### Filtros aplicados para usuários alcançáveis específicos do canal

Os seguintes filtros são aplicados para cada canal ao determinar usuários alcançáveis.

| Canal | Filtrar |
| --- | --- |
| E-mail | **Email Disponível** é verdadeiro. |
| Push | **Push em Primeiro Plano Habilitado** é verdadeiro. |
| SMS | **Grupo de Inscrição** é qualquer grupo de inscrição por SMS. **Número de Telefone Inválido** é falso. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Calculando estatísticas exatas 

Para visualizar uma contagem precisa do número de usuários em seu segmento, selecione **Calcular estatísticas exatas** no painel **Usuários alcançáveis**.

Para atualizar as estatísticas de um cálculo que você executou anteriormente, selecione **Atualizar estatísticas exatas**. A data em que este cálculo foi executado pela última vez será atualizada automaticamente.

Observe que a precisão de um cálculo é de apenas 99,999% ou mais. Portanto, para segmentos grandes, você pode notar pequenas variações—mesmo ao calcular estatísticas exatas—o que é um comportamento normal. Além disso, os resultados das estatísticas exatas são armazenados em cache por 24 horas, a menos que você faça edições em seu segmento, caso em que você pode recalcular as estatísticas exatas.

{% alert note %}
Segmentos divididos igualmente por [números de balde aleatórios]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) não terão o mesmo tamanho. Por exemplo, se você criar um segmento com o filtro **Baldes Aleatórios # menor que 5000** e um segmento com o filtro **Baldes Aleatórios # pelo menos 5000**, é possível e esperado que os tamanhos dos segmentos variem em até alguns pontos percentuais. Isso se deve a situações como usuários inativos sendo excluídos e usuários sendo inacessíveis.
{% endalert %}

![O painel "Usuários alcançáveis" com uma opção para mostrar a divisão.]({% image_buster /assets/img_archive/reachable_users_breakdown.png %})

As estatísticas em nível de filtro sempre serão estimadas, mesmo que você calcule estatísticas exatas. **Calcular estatísticas exatas** apenas calcula as estatísticas exatas no nível do segmento, não no nível do filtro ou grupo de filtros. Esse cálculo pode levar alguns minutos para ser executado. Espaços de trabalho maiores, em particular, podem exigir períodos mais longos para concluir os cálculos. Você pode acompanhar seu progresso na barra de progresso no painel **Usuários alcançáveis**. Quando um cálculo deve levar mais de cinco minutos, a Braze enviará um e-mail com os resultados. 

A Braze prioriza um cálculo por vez por espaço de trabalho, portanto, executar vários cálculos ao mesmo tempo causará atrasos. Você pode selecionar **Ver fila de cálculos** para ver quais segmentos estão à sua frente, seu progresso e seu iniciador, e ter uma ideia de quando seu cálculo pode ser priorizado.

![Uma fila de cálculos com um cálculo.]({% image_buster /assets/img_archive/calculation_queue.png %})

Você pode cancelar um cálculo de estatísticas exatas selecionando **Cancelar**. Isso pode ser benéfico se houver vários cálculos na fila e você quiser priorizar outro cálculo primeiro. 

![Um cálculo ativo com a opção de cancelar]({% image_buster /assets/img_archive/cancel_calculation.png %}){: style="max-width:25%"}

## Visualizando o tamanho histórico da associação do segmento

Para todos os segmentos, você pode visualizar um gráfico de associação histórica que mostra a associação estimada do segmento para cada dia. Este gráfico mostra como o tamanho do seu segmento mudou ao longo do tempo. Use o menu suspenso para filtrar a associação ao segmento por intervalo de datas.

![Use o menu suspenso Associação histórica para filtrar a associação do segmento por intervalo de datas.]({% image_buster /assets/img_archive/historical_membership2.png %})

Como o objetivo deste gráfico é dar uma noção das tendências gerais de associação do segmento, a contagem diária é uma estimativa, semelhante a como o tamanho do segmento é uma estimativa antes de você selecionar **Calcular Estatísticas Exatas**. E como este gráfico mostra estimativas, é possível que o tamanho do seu segmento apareça como "0" neste gráfico, mesmo que seu tamanho real (que pode ser determinado após selecionar **Calcular Estatísticas Exatas**) não seja "0". É especialmente provável que o gráfico mostre uma estimativa de "0" se seu segmento for muito pequeno em relação ao tamanho da população do seu espaço de trabalho.

Por exemplo, digamos que seu espaço de trabalho contenha 100 milhões de usuários e seu segmento tenha cerca de 700 usuários. É possível que em alguns dias, nenhum usuário esteja no segmento, e nenhum usuário caia na faixa de balde aleatório usada para a estimativa de associação histórica, resultando em uma contagem de associação de 0 em um dia.

A Braze estima a contagem de membros do segmento consultando um subconjunto de seus usuários e, em seguida, extrapolando esses resultados para todo o seu público. Isso significa que os resultados do gráfico fornecem apenas uma estimativa de qual pode ser a contagem de membros do segmento naquele dia, e espera-se que também flutue de dia para dia, pois um conjunto diferente de usuários pode ser consultado para essa estimativa a cada dia.

{% alert note %}
Todas as estimativas podem ser maiores ou menores do que o valor mostrado em aproximadamente 1% do tamanho total da população do seu espaço de trabalho. Espaços de trabalho maiores com mais usuários têm maior probabilidade de ter estimativas que podem diferir de cálculos exatos por um valor numérico maior, mesmo que a diferença ainda seja 1% da população de usuários do espaço de trabalho. Isso significa que diferenças maiores entre estimativas e contagens exatas entre grandes espaços de trabalho são esperadas.
{% endalert %}

### Razões para mudanças significativas

A contagem de membros pode mudar significativamente por uma série de razões, como as que estão nesta tabela.

| Motivo | Exemplo |
| --- | --- |
| Comportamento normal do usuário | Os usuários se inscrevem após uma campanha particularmente bem-sucedida. |
| Os usuários são importados por CSV | Um arquivo CSV de usuários foi importado que aumentou significativamente a contagem de membros do segmento. |
| Os critérios de audiência do segmento são modificados | As regras de audiência de um segmento existente (como filtros) foram alteradas, causando mudanças significativas na contagem de membros do segmento. |
| Os usuários são excluídos | Um número significativo de usuários foi excluído. |
| Uma integração com parceiros foi sincronizada com a Braze | Um terceiro enviou dados para a Braze que influenciaram significativamente a contagem de membros do segmento. |
| Usuários inativos são arquivados | Um número significativo de perfis inativos foi arquivado. Por exemplo, um grande número de usuários importados por CSV nunca registra atividade e é arquivado ao mesmo tempo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
