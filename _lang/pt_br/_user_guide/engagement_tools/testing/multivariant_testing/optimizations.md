---
nav_title: Otimizações
article_title: Otimização de Testes A/B com Variante Vencedora ou Variantes Personalizadas
page_order: 1
page_type: reference
description: "Aprenda a usar Variante Vencedora ou Variante Personalizada ao criar testes multivariantes e A/B."
---

# Otimização de testes A/B com Variante Vencedora ou Variantes Personalizadas

Ao [criar um teste A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) para campanhas de e-mail, push, webhook, SMS e WhatsApp programadas para enviar uma vez, você pode selecionar uma otimização. Existem duas opções de otimização: **Variante Vencedora** e **Variante Personalizada**.

![Opções de otimização listadas na seção de Testes A/B ao escolher seu público-alvo. Três opções estão listadas: Sem otimização, Variante vencedora e Variante personalizada. A variante personalizada está selecionada.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Ambas as opções funcionam enviando um teste inicial para uma porcentagem do seu segmento alvo. Após o teste terminar, os usuários restantes em seu público são enviados ou para a variante de melhor desempenho (Variante Vencedora) ou para a variante com a qual eles têm mais probabilidade de se engajar (Variante Personalizada).

{% alert tip %}
As otimizações estão localizadas na **Etapa de Públicos-alvo** da criação da campanha, em **Testes A/B**.
{% endalert %}

## Variante vencedora

Enviar a Variante Vencedora é semelhante a um teste A/B padrão. Os usuários deste grupo receberão a Variante Vencedora quando o teste inicial estiver completo.

1. Selecione **Variante Vencedora**, depois especifique qual porcentagem do seu público da campanha deve ser atribuída ao grupo Variante Vencedora.
2. Configure as seguintes configurações adicionais.

| Campo | Descrição |
| --- | --- | 
| Determinar variante vencedora | A métrica a ser otimizada. Escolha entre *Aberturas Únicas* ou *Cliques* para e-mail, *Aberturas* para push, ou *Taxa de Conversão Primária* para todos os canais. Selecionar *Abre* ou *Clica* para determinar o vencedor não afeta o que você escolhe para os [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) da campanha. <br><br>Lembre-se de que, se você estiver usando um grupo de controle, os usuários no grupo de controle não podem realizar *Aberturas* ou *Cliques*, então a performance do grupo de controle é garantida como `0`. Como resultado, o grupo de controle não pode vencer o teste A/B. No entanto, você ainda pode querer usar um grupo de controle para rastrear outras métricas para usuários que não recebem uma mensagem. |
| Horário de envio da variante vencedora | A data e a hora em que a variante vencedora é enviada. |
| Se nenhuma variante vencedora puder ser determinada | O que acontece se nenhuma variante vencer por uma margem estatisticamente significativa. Escolha entre enviar a variante de melhor desempenho de qualquer maneira ou encerrar o teste e não enviar mais mensagens. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Variante personalizada

Use variantes personalizadas para enviar a cada usuário em seu segmento alvo a variante com a qual eles têm mais probabilidade de se envolver.

Para determinar a melhor variante para cada usuário, a Braze enviará um teste inicial para uma parte do seu público-alvo para procurar associações entre características do usuário e preferências de mensagem. Com base em como os usuários respondem a cada variante no teste inicial, essas características são usadas para determinar quais usuários restantes receberão cada variante. Se nenhuma associação for encontrada e nenhuma personalização puder ser feita, a Variante Vencedora é automaticamente enviada aos usuários restantes. Para saber mais sobre como as Variantes Personalizadas são determinadas, consulte [análise de dados de teste multivariante e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant).

1. Selecione **Variante Personalizada**, depois especifique qual porcentagem do seu público da campanha deve ser atribuída ao grupo Variante Personalizada.
2. Configure as seguintes configurações adicionais.

| Campo | Descrição |
| --- | --- | 
| Determinar variante personalizada | A métrica a ser otimizada. Escolha entre *Aberturas Únicas* ou *Cliques* para e-mail, *Aberturas* para push, ou *Taxa de Conversão Primária* para todos os canais. Selecionar *Abre* ou *Clica* para determinar o vencedor não afeta o que você escolhe para os [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) da campanha. <br><br>Lembre-se de que, se você estiver usando um grupo de controle, os usuários no grupo de controle não podem realizar *Aberturas* ou *Cliques*, então a performance do grupo de controle é garantida como `0`. Como resultado, o grupo de controle não pode vencer o teste A/B. No entanto, você ainda pode querer usar um grupo de controle para rastrear outras métricas para usuários que não recebem uma mensagem. |
| Horário de envio da variante personalizada | A data e a hora em que a variante personalizada é enviada. |
| Se nenhuma variante personalizada puder ser determinada | O que acontece se nenhuma Variante Personalizada for encontrada. Escolha entre enviar a Variante Vencedora ou encerrar o teste e não enviar mais mensagens. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Análise de dados

Para saber mais sobre os resultados do seu teste A/B com uma otimização, consulte [análise de dados de teste multivariante e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

