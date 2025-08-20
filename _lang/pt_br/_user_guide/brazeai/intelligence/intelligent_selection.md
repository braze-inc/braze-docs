---
nav_title: Seleção Inteligente
article_title: Seleção Inteligente
page_order: 1.0
description: "Este artigo aborda a Seleção Inteligente, um recurso que analisa a performance de uma campanha recorrente ou do Canvas duas vezes por dia e ajusta automaticamente a porcentagem de usuários que recebem cada variante de mensagem."
search_rank: 10
toc_headers: h2
---

# Seleção inteligente {#intelligent-selection}

> O Intelligent Selection é um recurso que analisa a performance de uma campanha recorrente ou do Canvas duas vezes por dia e ajusta automaticamente a porcentagem de usuários que recebem cada variante de mensagem. 

## Sobre a Seleção Inteligente

Uma variante que pareça ter um desempenho melhor do que outras será enviada a mais usuários, enquanto as variantes com desempenho inferior serão direcionadas a menos usuários. Cada ajuste é feito usando um [algoritmo estatístico](https://en.wikipedia.org/wiki/Multi-armed_bandit) que garante que o Braze está ajustando para diferenças reais de desempenho e não apenas por acaso.

![Seção de Testes A/B de uma campanha com Seleção Inteligente ativada.]({% image_buster /assets/img/intelligent_selection1.png %})

A Seleção Inteligente:
- Examine repetidamente os dados de performance e mude gradualmente o tráfego da campanha para as variantes vencedoras.
- Verifique se mais usuários recebem sua variante de melhor performance sem sacrificar a confiança estatística.
- Exclua as variantes de baixo desempenho e identifique as variantes de alto desempenho mais rapidamente do que em um [teste A/B tradicional]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- Faça testes com mais frequência e com mais confiança de que seus usuários verão sua melhor mensagem. 

A Seleção Inteligente funciona melhor para campanhas que enviam mais de uma vez. Ela precisa de dados de desempenho iniciais para começar a otimizar, então campanhas de envio único não se beneficiarão. Para essas campanhas, recomendamos usar um [teste A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) tradicional em vez disso.

## Pré-requisitos

{% tabs %}
{% tab Campanha %}
Antes de adicionar a Seleção Inteligente à sua campanha, certifique-se de que você configurou tudo corretamente:

- Sua campanha é enviada em um cronograma recorrente. Campanhas de envio único não são suportadas.
- Você adicionou pelo menos duas variantes de mensagem.
- Você definiu um evento de conversão para medir o desempenho entre as variantes.
- A janela de re-eligibilidade está definida para 24 horas ou mais. Janelas mais curtas não são suportadas, pois afetariam a integridade da variante de controle. Para saber mais, consulte [FAQ de Inteligência]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endtab %}

{% tab Canva %}
Para usar a Seleção Inteligente em um Canva, confirme o seguinte:
- Seu Canva inclui pelo menos duas variantes de mensagem em uma etapa de Mensagem.
- Você adicionou pelo menos um evento de conversão.
{% endtab %}
{% endtabs %}

## Adicionando Seleção Inteligente

Você pode adicionar Seleção Inteligente às suas campanhas e Canvases.

{% tabs %}
{% tab Campanha %}
O Intelligent Selection pode ser adicionado a qualquer campanha de múltiplos envios na etapa de direcionamento do **público** do criador de campanhas da Braze. As campanhas que enviam apenas uma vez não podem aproveitar esse recurso.

{% alert note %}
A Seleção Inteligente não pode ser usada em campanhas com um período de re-eligibilidade de menos de 24 horas, pois isso afetaria a integridade da variante de controle. Para saber mais, consulte [FAQ de Inteligência]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}

{% tab Canva %}
Adicione pelo menos um evento de conversão e duas variantes ao seu canva. Em seguida, selecione uma das porcentagens de variante na etapa de Construção. 

![Um canva com duas variantes, cada uma configurada para 50% de distribuição de variante, permitindo que a Seleção Inteligente seja ativada.]({% image_buster /assets/img/intelligent_selection.png %})

Isso permite que você edite a distribuição de variantes e ative a Seleção Inteligente. 

![Opção de Seleção Inteligente ativada para um canva]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

A Intelligent Selection não estará disponível se você ainda não tiver adicionado eventos de conversão ao seu Canva ou se sua campanha for composta de uma variante solo.
{% endtab %}
{% endtabs %}

## Tempo de execução

Para campanhas e canvas, o Intelligent Selection será executado até reunir evidências suficientes sobre as taxas de conversão "verdadeiras" das variantes. O "suficiente" é determinado por uma métrica especial chamada "arrependimento". Você pode pensar nisso como algo semelhante à confiança, pois o Intelligent Selection será desativado quando houver dados suficientes para saber qual é a melhor variante. 

Na maioria dos casos, a Seleção Inteligente escolherá uma das variantes como a Variante Vencedora. Essa variante receberá 100% do público para envios futuros.

{% alert note %}
É possível que a Intelligent Selection pare de otimizar sem escolher um único vencedor claro. A Seleção Inteligente interrompe a otimização quando tem 95% de confiança de que a continuação do experimento não melhorará a taxa de conversão em mais de 1% da taxa atual.
{% endalert %}

## Perguntas Frequentes (FAQ) {#faq}

### Por que a reelegibilidade em menos de 24 horas não está disponível quando combinada com o Intelligent Selection?

Não permitimos que as campanhas da Seleção Inteligente sejam reelegíveis em um período muito curto, pois isso afetaria a integridade da variante de controle. Ao criar um intervalo de 24 horas, ajudamos a garantir que o algoritmo tenha um conjunto de dados estatisticamente válido para trabalhar.

Normalmente, as campanhas com reelegibilidade farão com que os usuários insiram novamente a mesma variante que receberam antes. Com a Seleção Inteligente, a Braze não pode garantir que um usuário receberá a mesma variante de campanha porque a distribuição de variantes teria mudado devido ao aspecto de alocação ideal para esse recurso. Se for permitido que o usuário entre novamente antes de a Intelligent Selection reexaminar a performance da variante, os dados de usuários que entraram novamente poderão ser distorcidos.

Por exemplo, se uma campanha estiver usando estas variantes:

- Variante A: 20%
- Variante B: 20%
- Controle: 60%

Então, a distribuição de variantes poderia ser a seguinte para a segunda rodada:

- Variante A: 15%
- Variante B: 25%
- Controle: 60%

### Por que minhas variantes do Intelligent Selection estão mostrando envios iguais durante os estágios iniciais da minha campanha?

O Intelligent Selection aloca variantes para envio com base no status atual da conversão da campanha. Ele só determina as alocações finais de variantes após um período de treinamento, em que os envios são feitos de forma homogênea entre as variantes. Se não quiser que a Seleção Inteligente envie uniformemente durante os estágios iniciais de sua campanha, use variantes fixas para um teste A/B tradicional.

### A Intelligent Selection deixará de otimizar sem escolher um vencedor claro?

A Seleção Inteligente interromperá a otimização quando tiver 95% de confiança de que a continuação do experimento não melhorará a taxa de conversão em mais de 1% da taxa atual.

### Por que não consigo ativar a Seleção Inteligente em minha canva ou campanha (acinzentado)?

O Intelligent Selection não estará disponível se:

- Você não adicionou eventos de conversão à sua campanha ou ao Canva
- Você está criando uma campanha de envio único
- Sua capacitação foi ativada com uma janela de menos de 24 horas
- Seu Canva é criado com uma única variante, sem variantes adicionais ou grupos de controle adicionados
- Seu Canva é composto por um único grupo de controle, sem variantes adicionadas
