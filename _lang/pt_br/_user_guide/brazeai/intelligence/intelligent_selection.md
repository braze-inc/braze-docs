---
nav_title: Seleção inteligente
article_title: Seleção inteligente
page_order: 1.0
description: "Este artigo aborda o Intelligent Selection, um recurso que analisa o desempenho de uma campanha recorrente ou Canvas duas vezes por dia e ajusta automaticamente a porcentagem de usuários que recebem cada variante de mensagem."
search_rank: 10
toc_headers: h2
---

# Seleção inteligente {#intelligent-selection}

> O Intelligent Selection é um recurso que analisa o desempenho de uma campanha recorrente ou Canvas duas vezes por dia e ajusta automaticamente a porcentagem de usuários que recebem cada variante de mensagem. 

## Sobre a Intelligent Selection

Uma variante que parece ter um desempenho melhor do que as outras será enviada a mais usuários, enquanto as variantes com desempenho inferior serão direcionadas a menos usuários. Cada ajuste é feito usando um [algoritmo estatístico](https://en.wikipedia.org/wiki/Multi-armed_bandit) que garante que o Braze esteja ajustando as diferenças reais de desempenho e não apenas o acaso.

Seção de teste A/B de uma campanha com a seleção inteligente ativada.]({% image_buster /assets/img/intelligent_selection1.png %})

A Seleção Inteligente o fará:
- Examine repetidamente os dados de desempenho e mude gradualmente o tráfego da campanha para as Variantes vencedoras.
- Verifique se mais usuários recebem sua variante de melhor desempenho sem sacrificar a confiança estatística.
- Exclua as variantes de baixo desempenho e identifique as variantes de alto desempenho mais rapidamente do que em um [teste A/B tradicional]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- Faça testes com mais frequência e com mais confiança de que seus usuários verão sua melhor mensagem. 

O Intelligent Selection funciona melhor para campanhas que são enviadas mais de uma vez. Ele precisa de dados de desempenho antecipados para começar a otimizar, portanto, as campanhas de envio único não serão beneficiadas. Para essas campanhas, recomendamos usar um [teste A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) tradicional.

## Pré-requisitos

{% tabs %}
{% tab Campaign %}
Antes de adicionar o Intelligent Selection à sua campanha, verifique se você configurou tudo corretamente:

- Sua campanha é enviada em uma programação recorrente. Não há suporte para campanhas de envio único.
- Você adicionou pelo menos duas variantes de mensagem.
- Você definiu um evento de conversão para medir o desempenho entre as variantes.
- A janela de reelegibilidade é definida para 24 horas ou mais. Não há suporte para janelas mais curtas, pois elas afetariam a integridade da variante de controle. Para saber mais, consulte [estas Perguntas frequentes]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endtab %}

{% tab Canvas %}
Para usar a Seleção Inteligente em um Canvas, confirme o seguinte:
- Seu Canvas inclui pelo menos duas variantes de mensagem em uma etapa de Mensagem.
- Você adicionou pelo menos um evento de conversão.
{% endtab %}
{% endtabs %}

## Adição de seleção inteligente

Você pode adicionar o Intelligent Selection às suas campanhas e Canvases.

{% tabs %}
{% tab Campaign %}
O Intelligent Selection pode ser adicionado a qualquer campanha de vários envios na etapa **Target Audiences (Públicos-alvo** ) do compositor de campanhas do Braze. As campanhas que enviam apenas uma vez não podem aproveitar esse recurso.

{% alert note %}
A Seleção Inteligente não pode ser usada em campanhas com um período de reelegibilidade inferior a 24 horas, pois isso afetaria a integridade da variante de controle. Para saber mais, consulte as [Perguntas frequentes sobre inteligência]({{site.baseurl}}/user_guide/brazeai/intelligence/faqs/#why-is-re-eligibility-in-less-than-24-hours-not-available-when-combined-with-intelligent-selection).
{% endalert %}
{% endtab %}

{% tab Canvas %}
Adicione pelo menos um evento de conversão e duas variantes ao seu Canvas. Em seguida, selecione uma das porcentagens de variantes na etapa Build. 

Um Canvas com duas variantes, cada uma definida com 50% de distribuição de variantes, permitindo que a Seleção Inteligente seja ativada.]({% image_buster /assets/img/intelligent_selection.png %})

Isso permite que você edite a distribuição de variantes e ative a Seleção Inteligente. 

\![Opção Intelligent Selection ativada para um Canvas]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

A Seleção inteligente não estará disponível se você ainda não tiver adicionado eventos de conversão ao seu Canvas ou se sua campanha for composta por uma variante individual.
{% endtab %}
{% endtabs %}

## Tempo de execução

Para campanhas e Canvases, o Intelligent Selection será executado até reunir evidências suficientes sobre as taxas de conversão "verdadeiras" das variantes. O "suficiente" é determinado por uma métrica especial chamada "arrependimento". Você pode pensar nisso como algo semelhante à confiança, pois o Intelligent Selection será desativado quando houver dados suficientes para saber qual é a melhor variante. 

Na maioria dos casos, o Intelligent Selection escolherá uma das variantes como a Variante Vencedora. Essa variante receberá 100% da audiência para envios futuros.

{% alert note %}
É possível que a Intelligent Selection pare de otimizar sem escolher um único vencedor claro. A Intelligent Selection interrompe a otimização quando tem 95% de confiança de que a continuação do experimento não melhorará a taxa de conversão em mais de 1% da taxa atual.
{% endalert %}

## Distribuição de variantes do Intelligent Selection

O Intelligent Selection baseia sua distribuição de variantes no status atual das conversões da campanha. Ele determina apenas as distribuições finais após o período de treinamento. 

Isso significa que, durante os estágios iniciais da campanha, tanto o Intelligent Selections de 99% quanto o de 1% podem receber envios aproximadamente iguais, mas as porcentagens finais para alocação de variantes podem ser definidas como 99%-1%.

Se você não quiser que o Intelligent Selection envie 50/50 durante os estágios iniciais da campanha, recomendamos o uso de um teste A/B tradicional com variantes fixas.

## Perguntas frequentes {#faq}

### Por que a reelegibilidade em menos de 24 horas não está disponível quando combinada com o Intelligent Selection?

Não permitimos que as campanhas do Intelligent Selection tenham reelegibilidade em um período muito curto, pois isso afetaria a integridade da variante de controle. Ao criar um intervalo de 24 horas, ajudamos a garantir que o algoritmo tenha um conjunto de dados estatisticamente válido para trabalhar.

Normalmente, as campanhas com reelegibilidade farão com que os usuários insiram novamente a mesma variante que receberam anteriormente. Com a Seleção Inteligente, o Braze não pode garantir que um usuário receberá a mesma variante de campanha porque a distribuição de variantes teria mudado devido ao aspecto de alocação ideal para esse recurso. Se fosse permitido que o usuário entrasse novamente antes de a Intelligent Selection reexaminar o desempenho da variante, os dados poderiam ser distorcidos devido aos usuários que entraram novamente.

Por exemplo, se uma campanha estiver usando essas variantes:

- Variante A: 20%
- Variante B: 20%
- Controle: 60%

Então, a distribuição de variantes poderia ser a seguinte para a segunda rodada:

- Variante A: 15%
- Variante B: 25%
- Controle: 60%

### Por que minhas variantes do Intelligent Selection estão mostrando envios iguais durante os estágios iniciais da minha campanha?

O Intelligent Selection aloca variantes para envio com base no status atual da conversão da campanha. Ele só determina as alocações de variantes finais após um período de treinamento, em que os envios são feitos de forma homogênea entre as variantes. Se não quiser que a Intelligent Selection envie uniformemente durante os estágios iniciais de sua campanha, use variantes fixas para um teste A/B tradicional.

### A Intelligent Selection deixará de otimizar sem escolher um vencedor claro?

A Intelligent Selection interromperá a otimização quando tiver 95% de confiança de que a continuação do experimento não melhorará a taxa de conversão em mais de 1% da taxa atual.

### Por que não consigo ativar a Seleção Inteligente em meu Canvas ou campanha (acinzentado)?

O Intelligent Selection não estará disponível se:

- Você não adicionou eventos de conversão à sua campanha ou ao Canvas
- Você está criando uma campanha de envio único
- Você tem a reelegibilidade ativada com uma janela de menos de 24 horas
- Seu Canvas é composto de uma única variante, sem variantes adicionais ou grupos de controle adicionados
- Seu Canvas é composto de um único grupo de controle, sem variantes adicionadas
