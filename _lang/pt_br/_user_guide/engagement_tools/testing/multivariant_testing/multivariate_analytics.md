---
nav_title: Análise de dados
article_title: Análise de dados de testes multivariantes e A/B
page_order: 10
page_type: reference
description: "Este artigo explica como visualizar e interpretar os resultados de uma campanha multivariante ou A/B."
---

# Análise de dados de testes multivariantes e A/B

> Este artigo explica como visualizar os resultados de um teste multivariante ou A/B. Se ainda não tiver configurado seu teste, consulte [Criação de testes multivariantes e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) para obter as etapas.

Após o lançamento da campanha, é possível verificar a performance de cada variante da campanha selecionando-a na seção **Campanhas** do dashboard. 

## Opção de análise de dados por otimização

Sua exibição de análise de dados variará dependendo da seleção de uma [otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) durante a configuração inicial.

### Sem otimização

Se você selecionou **Sem otimização** ao configurar sua campanha, sua exibição de análise de dados permanecerá a mesma. A página **Análise de dados** da sua campanha mostrará a performance das suas variantes em relação ao grupo de controle, caso tenha incluído um.

![Seção Performance da análise de dados da campanha para uma campanha de e-mail com várias variantes. A tabela lista várias métricas de performance para cada variante, como destinatários, bounces, cliques e conversões.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Para obter mais informações, consulte o artigo sobre [análise de dados da campanha]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) para seu canal de envio de mensagens.

### Variante vencedora

Se tiver selecionado a **Variante vencedora** para sua otimização ao configurar sua campanha, você terá acesso a uma guia adicional da análise de dados da campanha chamada **Resultado de Testes A/B**. Depois que a variante vencedora for enviada para os usuários restantes no teste, essa guia mostrará os resultados desse envio.

O **resultado dos Testes A/B** é dividido em duas guias: **Teste inicial** e **variante vencedora**.

{% tabs local %}
{% tab Teste inicial %}

A guia **Teste inicial** mostra as métricas de cada variante do teste A/B inicial enviado a uma parte de seu segmento de direcionamento. Você pode ver um resumo de como foi a performance de todas as variantes e se houve ou não um vencedor durante o teste.

Se uma variante superou todas as outras com mais de 95% de [confiança]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence), o Braze marca essa variante com o rótulo "Winner" (vencedor).

Se nenhuma variante superar todas as outras com 95% de confiança e você optar por enviar a variante de melhor performance mesmo assim, a variante de melhor performance ainda será enviada e indicada com o rótulo "Winner" (Vencedor).

![Resultados de um teste inicial enviado para determinar a Variante Vencedora, em que nenhuma variante teve desempenho melhor do que as outras com confiança suficiente para atingir o limite de confiança de 95% para significância estatística.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Como a variante vencedora é selecionada

O Braze testa todas as variantes umas contra as outras com os [testes de qui-quadrado de Pearson](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Isso mede se uma variante supera ou não estatisticamente todas as outras em um nível de significância de p < 0,05, ou o que chamamos de significância de 95%. Em caso afirmativo, a variante vencedora é indicada com o rótulo "Winner" (Vencedor).

Esse é um teste separado da pontuação de confiança, que descreve apenas a performance de uma variante em comparação com o controle com um valor numérico entre 0 e 100%.

Uma variante pode se sair melhor do que o grupo de controle, mas o teste do qui-quadrado verifica se uma variante é melhor do que todas as outras. [Testes de acompanhamento](#recommended-follow-ups) podem fornecer mais detalhes.

{% endtab %}
{% tab Variante vencedora %}

A guia **Winning Variant (Variante vencedora** ) mostra os resultados do segundo envio, em que cada usuário restante recebeu a variante de melhor desempenho do teste inicial. Sua **% de público** será adicionada à porcentagem do segmento de direcionamento que você reservou para o grupo da Variante vencedora.

![Resultados da variante vencedora enviados ao grupo da variante vencedora.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Se você quiser ver a performance da Variante vencedora durante toda a campanha, incluindo os envios de Testes A/B, verifique a página **Análise de dados da campanha**.

### Variante personalizada {#personalized-variant}

Se você selecionou **Variante personalizada** para sua otimização ao configurar sua campanha, o **Resultado de Testes A/B** é dividido em duas guias: **Teste inicial** e **variante personalizada**.

{% tabs local %}
{% tab Teste inicial %}

A guia **Teste inicial** mostra as métricas de cada variante do teste A/B inicial enviado a uma parte de seu segmento de direcionamento.

![Resultados de um teste inicial enviado para determinar a variante de melhor desempenho para cada usuário. Uma tabela mostra o desempenho de cada variante com base em várias métricas para o canal de direcionamento.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

Por padrão, o teste procura associações entre os eventos personalizados do usuário e suas preferências de variantes de mensagens. Essa análise detecta se os eventos personalizados aumentam ou diminuem a probabilidade de resposta a uma determinada variante de mensagem. Essas relações são então usadas para determinar quais usuários recebem qual variante de mensagem no envio final.

As relações entre os eventos personalizados e as preferências de mensagens são exibidas na tabela da guia **Envio inicial**.

![]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Se o teste não conseguir encontrar uma relação significativa entre os eventos personalizados e as preferências de variantes, o teste voltará a um método de análise baseado em sessão.

{% details Método de análise de fallback %}

**Método de análise baseado em sessão**<br>
Se o método fallback for usado para determinar as variantes personalizadas, a guia **Initial Test (Teste inicial** ) mostrará um detalhamento das variantes preferidas dos usuários com base em uma combinação de determinadas características. 

Essas características são:

- **Recência:** Quando foi a última vez que tiveram uma sessão
- **Frequência:** Com que frequência eles têm sessões
- **Posse:** Há quanto tempo é usuário

Por exemplo, o teste pode descobrir que a maioria dos usuários prefere a Variante A, mas os usuários que tiveram uma sessão há cerca de 3-12 dias, têm entre 1-12 dias entre as sessões e foram criados nos últimos 67-577 dias tendem a preferir a Variante B. Portanto, os usuários dessa subpopulação receberam a Variante B no segundo envio, enquanto o restante recebeu a Variante A.

![A tabela de Características do Usuário, que mostra quais usuários têm previsão de preferir a Variante A e a Variante B com base nos três grupos em que se enquadram em termos de recência, frequência e permanência.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Como as variantes personalizadas são selecionadas**<br>
Com esse método, a mensagem recomendada de um usuário individual é a soma dos efeitos de sua recenticidade, frequência e permanência específicas. A recência, a frequência e a permanência são divididas em grupos, conforme ilustrado na tabela **Características do usuário**. O intervalo de tempo de cada intervalo é determinado pelos dados de usuários em cada campanha individual e mudará de campanha para campanha. 

Cada bucket pode ter uma contribuição ou "push" diferente para cada variante de mensagem. A força do push para cada bucket é determinada a partir das respostas do usuário no envio inicial usando [regressão logística](https://en.wikipedia.org/wiki/Logistic_regression). Essa tabela apenas resume os resultados, mostrando com quais variantes os usuários de cada grupo tendem a se engajar. A Variante Personalizada real de qualquer usuário individual depende da soma dos efeitos dos três grupos em que ele se encontra - um para cada característica.

{% enddetails %}

{% endtab %}
{% tab Variante personalizada %}

A guia **Personalized Variant (Variante personalizada** ) mostra os resultados do segundo envio, em que cada usuário restante recebeu a variante com a qual tinha maior probabilidade de engajamento.

Os três cartões nesta página mostram sua elevação projetada, os resultados gerais e os resultados projetados se, em vez disso, você enviasse apenas a variante vencedora. Mesmo que não haja aumento, o que às vezes pode acontecer, o resultado é o mesmo que enviar apenas a variante vencedora (um teste A/B tradicional). 

- **Elevação projetada:** A melhoria na métrica de otimização selecionada para esse envio devido ao uso de Variantes personalizadas em vez de um teste A/B padrão (se os usuários restantes receberem apenas a Variante vencedora).
- **Resultados gerais:** Os resultados do segundo envio com base na métrica de otimização escolhida*(aberturas exclusivas*, *cliques exclusivos* ou *evento de conversão primária*).
- **Resultados projetados:** Os resultados projetados do segundo envio com base na métrica de otimização escolhida, caso você tivesse enviado apenas a Variante vencedora. 

![Guia Variante personalizada para uma campanha otimizada para aberturas exclusivas. Os cartões mostram a elevação projetada, as aberturas exclusivas gerais (com variante personalizada) e as aberturas exclusivas projetadas (com variante vencedora).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

A tabela nesta página mostra as métricas de cada variante do envio de variantes personalizadas. Sua **% de público** corresponde à porcentagem do segmento de direcionamento que você reservou para o grupo variante personalizada

![]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Entendendo a confiança {#understanding-confidence}

A confiança é a medida estatística da certeza que temos de que uma diferença nos dados, como taxas de conversão, é real e não se deve apenas ao acaso.

{% alert note %}
Não está confiando em seus resultados? A confiança só aparecerá se você tiver um grupo de controle.
{% endalert %}

É muito importante confiar em seus resultados. Por exemplo, e se o grupo de controle tivesse uma taxa de conversão de 20% e a variante A tivesse uma taxa de conversão de 25%? Isso parece indicar que o envio da Variante A é mais eficaz do que não enviar nenhuma mensagem. Ter uma confiança de 95% significa que a diferença entre as duas taxas de conversão provavelmente se deve a uma diferença real nas respostas dos usuários e que há apenas 5% de probabilidade de que a diferença tenha ocorrido por acaso.

O Braze compara a taxa de conversão de cada variante com a taxa de conversão do controle com um procedimento estatístico chamado [Teste Z](https://en.wikipedia.org/wiki/Z-test). Um resultado de 95% ou mais de confiança, como no exemplo anterior, indica que a diferença é estatisticamente significativa. Isso é verdadeiro em qualquer lugar em que você veja uma métrica de confiança no dashboard do Braze que descreva a diferença entre duas mensagens ou populações de usuários.

Em geral, é necessária uma confiança de pelo menos 95% para mostrar que seus resultados refletem as preferências reais dos usuários e não são devidos ao acaso. Em testes científicos rigorosos, 95% de confiança (ou comumente referido como o valor "p" sendo menor que 0,05) é a referência comum usada para determinar a significância estatística. Se você não conseguir atingir 95% de confiança de forma contínua, tente aumentar o tamanho da amostra ou diminuir o número de variantes. 

A confiança não descreve se uma variante é melhor do que as outras. É puramente uma medida da certeza que temos de que as duas (ou mais) taxas de conversão são realmente diferentes uma da outra. Isso é apenas uma função do tamanho da amostra e das diferenças entre as taxas de conversão aparentes. O fato de as taxas gerais serem altas ou baixas não afeta a força da medida de confiança. É possível que uma variante tenha uma taxa de conversão muito diferente da outra e, ainda assim, não tenha uma confiança de 95% ou mais. Também é possível que dois conjuntos de variantes tenham taxas de conversão/elevação semelhantes e, ainda assim, confiança diferente.

### Resultados estatisticamente insignificantes

Um teste que não tenha uma confiança de 95% ainda pode conter insights importantes. Aqui estão algumas coisas que você pode aprender com um teste com resultados estatisticamente insignificantes:

- É possível que todas as suas variantes tenham tido praticamente o mesmo efeito. Saber disso economiza o tempo que você gastaria para fazer essas alterações. Às vezes, você pode descobrir que as táticas convencionais de marketing, como repetir sua chamada para ação, não funcionam necessariamente para seu público.
- Embora seus resultados possam ter sido devidos ao acaso, eles podem informar a hipótese para seu próximo teste. Se várias variantes parecerem ter aproximadamente os mesmos resultados, execute algumas delas novamente junto com novas variantes para ver se você consegue encontrar uma alternativa mais eficaz. Se uma variante se sair melhor, mas não por uma quantidade significativa, você poderá realizar outro teste no qual a diferença dessa variante seja mais exagerada.
- Continue testando! Um teste com resultados insignificantes deve levar a certas perguntas. Não havia realmente nenhuma diferença entre suas variantes? Você deveria ter estruturado seu teste de forma diferente? Você pode responder a essas perguntas executando testes de acompanhamento.
- Embora os testes sejam úteis para descobrir que tipo de mensagem gera mais respostas de seu público, também é importante entender quais alterações no envio de mensagens têm apenas um efeito insignificante. Isso permite que você continue testando outra alternativa mais eficaz ou economize o tempo que poderia ter sido gasto para decidir entre duas mensagens alternativas.

Independentemente de seu teste ter ou não um vencedor claro, pode ser útil executar um [teste de acompanhamento](#recommended-follow-ups) para confirmar seus resultados ou aplicar suas descobertas a um cenário ligeiramente diferente.

## Acompanhamentos recomendados {#recommended-follow-ups}

Um teste multivariante e A/B pode (e deve!) inspirar ideias para testes futuros, além de orientá-lo em relação a mudanças na sua estratégia de envio de mensagens. As possíveis ações de acompanhamento incluem o seguinte:

#### Altere sua estratégia de envio de mensagens com base nos resultados dos testes

Seus resultados multivariantes podem levá-lo a mudar a forma como você redige ou formata seu envio de mensagens.

#### Mude a forma como você entende seus usuários

Cada teste esclarecerá o comportamento dos usuários, como eles respondem a diferentes canais de envio de mensagens e as diferenças (e semelhanças) entre seus segmentos.

#### Melhorar a forma como você estrutura os testes futuros

O tamanho de sua amostra era muito pequeno? As diferenças entre suas variantes eram muito sutis? Cada teste oferece uma oportunidade de aprender como melhorar os testes futuros. Se sua confiança for baixa, o tamanho da amostra é muito pequeno e deve ser ampliado para testes futuros. Se não encontrar nenhuma diferença clara entre a performance das suas variantes, é possível que as diferenças sejam sutis demais para ter um efeito perceptível nas respostas dos usuários.

#### Executar um teste de acompanhamento com um tamanho de amostra maior

Amostras maiores aumentarão as chances de detecção de pequenas diferenças entre as variantes.

#### Execute um teste de acompanhamento usando um canal de envio de mensagens diferente

Se descobrir que uma determinada estratégia é muito eficaz em um canal, talvez queira testar essa estratégia em outros canais. Se um tipo de mensagem for eficaz em um canal, mas não for eficaz em outro, talvez seja possível concluir que determinados canais são mais propícios a determinados tipos de mensagens. Ou talvez haja uma diferença entre os usuários que têm maior probabilidade de ativar as notificações por push e aqueles que têm maior probabilidade de prestar atenção às mensagens no app. Em última análise, a execução desse tipo de teste o ajudará a saber como seu público interage com seus diferentes canais de comunicação.

#### Execute um teste de acompanhamento em um segmento diferente de usuários

Para fazer isso, crie outro teste com o mesmo canal de envio de mensagens e variantes, mas escolha um segmento diferente de usuários. Por exemplo, se um tipo de envio de mensagens foi extremamente eficaz para os usuários engajados, pode ser útil investigar seu efeito sobre os usuários que desistiram. É possível que os usuários inativos respondam de forma semelhante ou prefiram outra das outras variantes. Esse teste o ajudará a saber mais sobre seus diferentes segmentos e como eles respondem a diferentes tipos de mensagens. Por que fazer suposições sobre seus segmentos quando você pode basear sua estratégia em dados?

#### Executar um teste de acompanhamento com base nos insights de um teste anterior

Use os insights obtidos em testes anteriores para orientar seus testes futuros. Um teste anterior indica que uma técnica de envio de mensagens é mais eficaz? Você não tem certeza de qual aspecto específico de uma variante a tornou melhor? A execução de testes de acompanhamento com base nessas perguntas ajudará você a gerar descobertas insight sobre seus usuários.

#### Comparar o impacto de longo prazo de diferentes variantes

Se estiver fazendo testes A/B com mensagens de reengajamento, não se esqueça de comparar o impacto de longo prazo de diferentes variantes usando [os Relatórios de retenção]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/). É possível usar os Relatórios de retenção para analisar como cada variante afetou o comportamento de qualquer usuário de sua escolha dias, semanas, um mês após o recebimento da mensagem, e ver se há aumento.
