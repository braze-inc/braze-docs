---
nav_title: Otimizações
article_title: Otimização de testes A/B com variante vencedora ou variantes personalizadas
page_order: 1
page_type: reference
description: "Saiba como usar a Variante vencedora ou a Variante personalizada ao criar testes multivariados e A/B."
---

# Otimização de testes A/B com variante vencedora ou variantes personalizadas

Ao [criar um teste A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) para campanhas de e-mail, push, webhook, SMS e WhatsApp programadas para serem enviadas uma vez, você pode selecionar uma otimização. Há duas opções de otimização: **Variante vencedora** e **variante personalizada**.

Opções de otimização listadas na seção Teste A/B ao escolher seu público-alvo. São listadas três opções: Sem otimização, Variante vencedora e Variante personalizada. A variante personalizada é selecionada.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Ambas as opções funcionam enviando um teste inicial para uma porcentagem do seu segmento-alvo. Após o término do teste, os usuários restantes do seu público-alvo recebem a variante com melhor desempenho (Variante vencedora) ou a variante com a qual eles têm maior probabilidade de interagir (Variante personalizada).

{% alert tip %}
As otimizações estão localizadas na etapa **Target Audiences (Públicos-alvo** ) da criação da campanha, em **A/B Testing (Teste A/B**).
{% endalert %}

## Variante vencedora

O envio da variante vencedora é semelhante a um teste A/B padrão. Os usuários desse grupo receberão a variante vencedora quando o teste inicial for concluído.

1. Selecione **Variante vencedora** e, em seguida, especifique a porcentagem do público-alvo da campanha que deve ser atribuída ao grupo Variante vencedora.
2. Defina as seguintes configurações adicionais.

| Campo | Descrição |
| --- | --- | 
| Determinar a variante vencedora | A métrica a ser otimizada. Escolha entre aberturas *exclusivas* ou *cliques* para e-mail, *aberturas* para push ou *taxa de conversão primária* para todos os canais. A seleção de *aberturas* ou *cliques* para determinar o vencedor não afeta o que você escolhe para os [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/) da campanha. <br><br>Lembre-se de que, se você estiver usando um grupo de controle, os usuários do grupo de controle não poderão realizar *aberturas* ou *cliques*, portanto, o desempenho do grupo de controle é garantido como `0`. Como resultado, o grupo de controle não pode vencer o teste A/B. No entanto, talvez você ainda queira usar um grupo de controle para rastrear outras métricas para usuários que não recebem uma mensagem. |
| Tempo de envio da variante vencedora | A data e a hora em que a variante vencedora é enviada. |
| Se não for possível determinar a variante vencedora | O que acontece se nenhuma variante vencer por uma margem estatisticamente significativa. Escolha entre enviar a variante de melhor desempenho de qualquer maneira ou encerrar o teste e não enviar mais nenhuma mensagem. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Variante personalizada

Use Personalized Variants (Variantes personalizadas) para enviar a cada usuário do seu segmento-alvo a variante com a qual ele tem maior probabilidade de se envolver.

Para determinar a melhor variante para cada usuário, o Braze enviará um teste inicial a uma parte do seu público-alvo para procurar associações entre as características do usuário e as preferências de mensagem. Com base em como os usuários respondem a cada variante no teste inicial, essas características são usadas para determinar quais usuários restantes receberão cada variante. Se nenhuma associação for encontrada e nenhuma personalização puder ser feita, a Variante vencedora será automaticamente enviada aos usuários restantes. Para saber mais sobre como as variantes personalizadas são determinadas, consulte [Análise de testes multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant).

1. Selecione **Personalized Variant (Variante personalizada**) e especifique qual porcentagem do público-alvo da campanha deve ser atribuída ao grupo Personalized Variant (Variante personalizada).
2. Defina as seguintes configurações adicionais.

| Campo | Descrição |
| --- | --- | 
| Determinar a variante personalizada | A métrica a ser otimizada. Escolha entre aberturas *exclusivas* ou *cliques* para e-mail, *aberturas* para push ou *taxa de conversão primária* para todos os canais. A seleção de *aberturas* ou *cliques* para determinar o vencedor não afeta o que você escolhe para os [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) da campanha. <br><br>Lembre-se de que, se você estiver usando um grupo de controle, os usuários do grupo de controle não poderão realizar *aberturas* ou *cliques*, portanto, o desempenho do grupo de controle é garantido como `0`. Como resultado, o grupo de controle não pode vencer o teste A/B. No entanto, talvez você ainda queira usar um grupo de controle para rastrear outras métricas para usuários que não recebem uma mensagem. |
| Tempo de envio da variante personalizada | A data e a hora em que a variante personalizada é enviada. |
| Se nenhuma variante personalizada puder ser determinada | O que acontece se nenhuma variante personalizada for encontrada. Escolha entre enviar a variante vencedora ou encerrar o teste e não enviar mais nenhuma mensagem. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Análises

Para saber mais sobre os resultados de seu teste A/B com uma otimização, consulte [Análise de testes multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

