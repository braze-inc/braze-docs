---
nav_title: Seleção Inteligente
article_title: Seleção Inteligente
page_order: 1
description: "Este artigo aborda a Seleção Inteligente, um recurso que analisa a performance de uma campanha recorrente ou do Canvas duas vezes por dia e ajusta automaticamente a porcentagem de usuários que recebem cada variante de mensagem."
search_rank: 10
---

# Seleção inteligente {#intelligent-selection}

> O Intelligent Selection é um recurso que analisa a performance de uma campanha recorrente ou do Canvas duas vezes por dia e ajusta automaticamente a porcentagem de usuários que recebem cada variante de mensagem. 

Uma variante que pareça ter um desempenho melhor do que outras será enviada a mais usuários, enquanto as variantes com desempenho inferior serão direcionadas a menos usuários. Cada ajuste é feito usando um [algoritmo estatístico][227] que garante que estamos ajustando as diferenças reais de performance e não apenas o acaso.

![Seção Testes A/B de uma campanha com a Seleção Inteligente ativada.][3]

A Seleção Inteligente:
- Examine repetidamente os dados de performance e mude gradualmente o tráfego da campanha para as variantes vencedoras.
- Verifique se mais usuários recebem sua variante de melhor performance sem sacrificar a confiança estatística.
- Exclua as variantes de baixo desempenho e identifique as variantes de alto desempenho mais rapidamente do que em um [teste A/B tradicional][1].
- Faça testes com mais frequência e com mais confiança de que seus usuários verão sua melhor mensagem. 

O Intelligent Selection é ideal para campanhas que estão programadas para serem enviadas várias vezes. Os resultados iniciais são necessários para começar a ajustar sua campanha; portanto, uma campanha que seja enviada apenas uma vez não trará benefícios. Para essas campanhas, um [teste A/B][1] seria mais eficaz.

## Como faço para adicionar o Intelligent Selection às minhas campanhas?

### Seleção inteligente de campanhas
O Intelligent Selection pode ser adicionado a qualquer campanha de múltiplos envios na etapa de direcionamento do **público** do criador de campanhas da Braze. As campanhas que enviam apenas uma vez não podem aproveitar esse recurso.

### Seleção inteligente do Canva
Ao adicionar variantes em seu Canva, clique em uma das porcentagens de variantes. Isso permite que você edite a distribuição de variantes e ative a Seleção Inteligente.

![Um canva com duas variantes, cada uma definida com 50% de distribuição de variantes, permitindo que a Seleção Inteligente seja ativada.][2]

A Intelligent Selection não estará disponível se você ainda não tiver adicionado eventos de conversão ao seu Canva ou se sua campanha for composta de uma variante solo.

{% alert note %}
Não permitimos o uso da Seleção Inteligente em campanhas com reelegibilidade ativada em menos de 24 horas, pois isso afetaria a integridade da variante de controle. Consulte as [Perguntas frequentes sobre inteligência]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection) para saber mais.
{% endalert %}

## Por quanto tempo ele funcionará?

Para campanhas e canvas, o Intelligent Selection será executado até reunir evidências suficientes sobre as taxas de conversão "verdadeiras" das variantes. O "suficiente" é determinado por uma métrica especial chamada "arrependimento". Você pode pensar nisso como algo semelhante à confiança, pois o Intelligent Selection será desativado quando houver dados suficientes para saber qual é a melhor variante. 

Na maioria dos casos, a Seleção Inteligente escolherá uma das variantes como a Variante Vencedora. Essa variante receberá 100% do público para envios futuros.

{% alert note %}
É possível que a Intelligent Selection pare de otimizar sem escolher um único vencedor claro. A Seleção Inteligente interrompe a otimização quando tem 95% de confiança de que a continuação do experimento não melhorará a taxa de conversão em mais de 1% da taxa atual.
{% endalert %}

[1]: {{site.baseurl}}/user_guide/intelligence/multivariate_testing/
[2]: {% image_buster /assets/img/intelligent_selection.png %}
[3]: {% image_buster /assets/img/intelligent_selection1.png %}
[227]: https://en.wikipedia.org/wiki/Multi-armed_bandit

