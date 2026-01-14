---
nav_title: Análises
article_title: Análise de testes multivariados e A/B
page_order: 10
page_type: reference
description: "Este artigo explica como visualizar e interpretar os resultados de uma campanha multivariada ou A/B."
---

# Análise de testes multivariados e A/B

> Este artigo explica como visualizar os resultados de um teste multivariado ou A/B. Se você ainda não configurou seu teste, consulte [Criação de testes multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) para obter as etapas.

Depois que sua campanha for lançada, você poderá verificar o desempenho de cada variante selecionando sua campanha na seção **Campanhas** do painel. 

## Opção de análise por otimização

Sua exibição de análise varia de acordo com a seleção de uma [otimização]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) durante a configuração inicial.

### Sem otimização

Se você selecionou **No optimization (Sem otimização** ) ao configurar sua campanha, sua exibição de análise permanecerá a mesma. A página **Campaign Analytics** da sua campanha mostrará o desempenho das suas variantes em relação ao seu grupo de controle, caso tenha incluído um.

Seção Desempenho do Campaign Analytics para uma campanha de e-mail com várias variantes. A tabela lista várias métricas de desempenho para cada variante, como destinatários, rejeições, cliques e conversões.]({% image_buster /assets/img_archive/ab_analytics_no_optimization.png %})

Para obter mais detalhes, consulte o artigo do [Campaign Analytics]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) para seu canal de mensagens.

### Variante vencedora

Se você selecionou a **Variante vencedora** para sua otimização ao configurar sua campanha, terá acesso a uma guia adicional da análise de sua campanha chamada **Resultado do teste A/B**. Depois que a Variante vencedora for enviada para os usuários restantes do teste, essa guia mostrará os resultados desse envio.

O **resultado do teste A/B** é dividido em duas guias: **Teste inicial** e **variante vencedora**.

{% tabs local %}
{% tab Initial Test %}

A guia **Initial Test (Teste inicial** ) mostra as métricas de cada variante do teste A/B inicial enviado a uma parte do seu segmento-alvo. Você pode ver um resumo do desempenho de todas as variantes e se houve ou não um vencedor durante o teste.

Se uma variante superou todas as outras com mais de 95% de [confiança]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#understanding-confidence), o Braze marca essa variante com um rótulo de "Vencedor".

Se nenhuma variante superar todas as outras com 95% de confiança e você optar por enviar a variante de melhor desempenho mesmo assim, a variante de melhor desempenho ainda será enviada e indicada com o rótulo "Vencedor".

Resultados de um teste inicial enviado para determinar a Variante Vencedora em que nenhuma variante teve desempenho melhor do que as outras com confiança suficiente para atingir o limite de confiança de 95% para significância estatística.]({% image_buster /assets/img_archive/ab_analytics_wv_insufficient_confidence.png %})

#### Como a variante vencedora é selecionada

O Braze testa todas as variantes umas contra as outras com os [testes de qui-quadrado de Pearson](https://en.wikipedia.org/wiki/Pearson%27s_chi-squared_test). Isso mede se uma variante supera ou não estatisticamente todas as outras em um nível de significância de p < 0,05, ou o que chamamos de significância de 95%. Em caso afirmativo, a variante vencedora é indicada com o rótulo "Winner" (Vencedor).

Esse é um teste separado da pontuação de confiança, que descreve apenas o desempenho de uma variante em comparação com o controle com um valor numérico entre 0 e 100%.

Uma variante pode se sair melhor do que o grupo de controle, mas o teste do qui-quadrado verifica se uma variante é melhor do que todas as outras. [Testes de acompanhamento](#recommended-follow-ups) podem fornecer mais detalhes.

{% endtab %}
{% tab Winning Variant %}

A guia **Winning Variant (Variante vencedora** ) mostra os resultados do segundo envio, em que cada usuário restante recebeu a variante de melhor desempenho do teste inicial. Sua **Audience %** será adicionada à porcentagem do segmento-alvo que você reservou para o grupo da Variante vencedora.

\![Resultados da Variante Vencedora enviados para o grupo da Variante Vencedora.]({% image_buster /assets/img_archive/ab_analytics_wv_1.png %})

{% endtab %}
{% endtabs %}

Se você quiser ver o desempenho da Variante vencedora em toda a campanha, incluindo os envios de teste A/B, verifique a página **Campaign Analytics**.

### Variante personalizada {#personalized-variant}

Se você selecionou **Personalized Variant (Variante personalizada** ) para sua otimização ao configurar sua campanha, o **Resultado do teste A/B** é dividido em duas guias: **Teste inicial** e **variante personalizada**.

{% tabs local %}
{% tab Initial Test %}

A guia **Initial Test (Teste inicial** ) mostra as métricas de cada variante do teste A/B inicial enviado a uma parte do seu segmento-alvo.

\![Resultados de um teste inicial enviado para determinar a variante de melhor desempenho para cada usuário. Uma tabela mostra o desempenho de cada variante com base em várias métricas para o canal de destino.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_1.png %})

Por padrão, o teste procura associações entre os eventos personalizados do usuário e suas preferências de variante de mensagem. Essa análise detecta se os eventos personalizados aumentam ou diminuem a probabilidade de resposta a uma determinada variante de mensagem. Essas relações são então usadas para determinar quais usuários recebem qual variante de mensagem no envio final.

As relações entre os eventos personalizados e as preferências de mensagem são exibidas na tabela da guia **Envio inicial**.

\![]({% image_buster /assets/img_archive/ab_analytics_pv_3.png %})

Se o teste não conseguir encontrar uma relação significativa entre os eventos personalizados e as preferências de variantes, o teste voltará para um método de análise baseado em sessão.

{% details Fallback analysis method %}

**Método de análise baseado em sessão**<br>
Se o método de fallback for usado para determinar as variantes personalizadas, a guia **Teste inicial** mostrará um detalhamento das variantes preferidas dos usuários com base em uma combinação de determinadas características. 

Essas características são:

- **Recência:** Quando foi a última vez que tiveram uma sessão
- **Frequência:** Com que frequência eles têm sessões
- **Posse:** Há quanto tempo é usuário

Por exemplo, o teste pode descobrir que a maioria dos usuários prefere a Variante A, mas os usuários que tiveram uma sessão há cerca de 3 a 12 dias, têm entre 1 e 12 dias de intervalo entre as sessões e foram criados nos últimos 67 a 577 dias tendem a preferir a Variante B. Portanto, os usuários dessa subpopulação receberam a Variante B no segundo envio, enquanto o restante recebeu a Variante A.

A tabela de Características do usuário, que mostra quais usuários devem preferir a Variante A e a Variante B com base nos três grupos em que se enquadram em termos de recenticidade, frequência e permanência.]({% image_buster /assets/img_archive/ab_analytics_pv_initial_test_2.png %})

**Como as variantes personalizadas são selecionadas**<br>
Com esse método, a mensagem recomendada de um usuário individual é a soma dos efeitos de sua recenticidade, frequência e permanência específicas. A recência, a frequência e a permanência são divididas em grupos, conforme ilustrado na tabela **Características do usuário**. O intervalo de tempo de cada intervalo é determinado pelos dados dos usuários em cada campanha individual e mudará de campanha para campanha. 

Cada bucket pode ter uma contribuição ou "empurrão" diferente para cada variante de mensagem. A força do impulso para cada balde é determinada a partir das respostas do usuário no envio inicial usando [regressão logística](https://en.wikipedia.org/wiki/Logistic_regression). Essa tabela apenas resume os resultados, mostrando com quais variantes os usuários de cada grupo tendem a se envolver. A variante personalizada real de qualquer usuário individual depende da soma dos efeitos dos três grupos em que ele se encontra - um para cada característica.

{% enddetails %}

{% endtab %}
{% tab Personalized Variant %}

A guia **Personalized Variant (Variante personalizada** ) mostra os resultados do segundo envio, em que cada usuário restante recebeu a variante com a qual tinha maior probabilidade de se envolver.

Os três cartões nesta página mostram sua elevação projetada, os resultados gerais e os resultados projetados se, em vez disso, você enviasse apenas a variante vencedora. Mesmo que não haja aumento, o que às vezes pode acontecer, o resultado é o mesmo que enviar apenas a Variante vencedora (um teste A/B tradicional). 

- **Elevação projetada:** A melhoria na métrica de otimização selecionada para esse envio devido ao uso de Variantes personalizadas em vez de um teste A/B padrão (se os usuários restantes receberem apenas a Variante vencedora).
- **Resultados gerais:** Os resultados do segundo envio com base na métrica de otimização escolhida*(aberturas exclusivas*, *cliques exclusivos* ou *evento de conversão principal*).
- **Resultados projetados:** Os resultados projetados do segundo envio com base na métrica de otimização escolhida, caso você tivesse enviado apenas a Variante vencedora. 

Guia Variante personalizada para uma campanha otimizada para aberturas exclusivas. Os cartões mostram a elevação projetada, as aberturas únicas gerais (com variante personalizada) e as aberturas únicas projetadas (com variante vencedora).]({% image_buster /assets/img_archive/ab_analytics_pv_1.png %})

A tabela nesta página mostra as métricas de cada variante do envio de variantes personalizadas. Seu **Audience %** corresponde à porcentagem do segmento-alvo que você reservou para o grupo Personalized Variant.

\![]({% image_buster /assets/img_archive/ab_analytics_pv_2.png %})

{% endtab %}
{% endtabs %}

## Entendendo a confiança {#understanding-confidence}

A confiança é a medida estatística da certeza que temos de que uma diferença nos dados, como taxas de conversão, é real e não se deve apenas ao acaso.

{% alert note %}
Não vê confiança em seus resultados? A confiança só aparecerá se você tiver um grupo de controle.
{% endalert %}

Uma parte importante de seus resultados é a confiança em seus resultados. Por exemplo, e se o Grupo de Controle tivesse uma taxa de conversão de 20% e a Variante A tivesse uma taxa de conversão de 25%? Isso parece indicar que enviar a Variante A é mais eficaz do que não enviar nenhuma mensagem. Ter uma confiança de 95% significa que a diferença entre as duas taxas de conversão provavelmente se deve a uma diferença real nas respostas dos usuários e que há apenas 5% de probabilidade de que a diferença tenha ocorrido por acaso.

A Braze compara a taxa de conversão de cada variante com a taxa de conversão do controle por meio de um procedimento estatístico chamado [Teste Z](https://en.wikipedia.org/wiki/Z-test). Um resultado de 95% ou mais de confiança, como no exemplo anterior, indica que a diferença é estatisticamente significativa. Isso é verdadeiro em qualquer lugar em que você veja uma métrica de confiança no painel do Braze que descreva a diferença entre duas mensagens ou populações de usuários.

Em geral, é necessária uma confiança de pelo menos 95% para mostrar que seus resultados refletem as preferências reais dos usuários e não são devidos ao acaso. Em testes científicos rigorosos, 95% de confiança (ou comumente referido como o valor "p" sendo menor que 0,05) é a referência comum usada para determinar a significância estatística. Se você não conseguir atingir 95% de confiança continuamente, tente aumentar o tamanho da amostra ou diminuir o número de variantes. 

A confiança não descreve se uma variante é melhor do que as outras. É puramente uma medida da certeza que temos de que as duas (ou mais) taxas de conversão são realmente diferentes uma da outra. Isso é apenas uma função do tamanho da amostra e das diferenças entre as taxas de conversão aparentes. O fato de as taxas gerais serem altas ou baixas não afeta a força da medida de confiança. É possível que uma variante tenha uma taxa de conversão muito diferente da outra e, ainda assim, não tenha uma confiança de 95% ou mais. Também é possível que dois conjuntos de variantes tenham taxas de conversão/elevação semelhantes e, ainda assim, confiança diferente.

### Resultados estatisticamente insignificantes

Um teste que não tenha uma confiança de 95% ainda pode conter insights importantes. Aqui estão algumas coisas que você pode aprender com um teste com resultados estatisticamente insignificantes:

- É possível que todas as suas variantes tenham tido praticamente o mesmo efeito. Saber disso economiza o tempo que você gastaria para fazer essas alterações. Às vezes, você pode descobrir que as táticas convencionais de marketing, como a repetição da sua chamada para ação, não funcionam necessariamente para o seu público.
- Embora seus resultados possam ter sido devidos ao acaso, eles podem informar a hipótese para seu próximo teste. Se várias variantes parecerem ter aproximadamente os mesmos resultados, execute algumas delas novamente junto com novas variantes para ver se você consegue encontrar uma alternativa mais eficaz. Se uma variante se sair melhor, mas não por um valor significativo, você poderá realizar outro teste em que a diferença dessa variante seja mais exagerada.
- Continue testando! Um teste com resultados insignificantes deve levar a certas perguntas. Não havia realmente nenhuma diferença entre suas variantes? Você deveria ter estruturado seu teste de forma diferente? Você pode responder a essas perguntas executando testes de acompanhamento.
- Embora os testes sejam úteis para descobrir que tipo de mensagem gera a maior resposta do público-alvo, também é importante entender quais alterações nas mensagens têm apenas um efeito insignificante. Isso permite que você continue testando outra alternativa mais eficaz ou economize o tempo que poderia ter sido gasto para decidir entre duas mensagens alternativas.

Independentemente de seu teste ter ou não um vencedor claro, pode ser útil executar um [teste de acompanhamento](#recommended-follow-ups) para confirmar seus resultados ou aplicar suas descobertas a um cenário ligeiramente diferente.

## Discrepâncias entre o grupo de controle e a variante

Em campanhas de mensagens in-app, a maneira como os usuários são rastreados e como as impressões são registradas pode causar discrepâncias na divisão esperada entre o grupo de controle e a variante. Isso ocorre porque as impressões reais registradas podem não refletir essa divisão, e a Braze não tem controle sobre o comportamento individual do usuário que executará o acionamento.

Por exemplo, digamos que uma campanha tenha um público-alvo de 200 usuários no lançamento, com 100 usuários no grupo de controle e 100 usuários na variante.

Os 100 usuários da variante recebem o payload da mensagem in-app, e 50 deles executam a ação de acionamento e veem a mensagem in-app. Os 100 usuários do grupo de controle só são rastreados se realizarem a ação de disparo da campanha, e 75 deles realizam a ação de disparo e registram uma impressão, mas não veem a mensagem in-app.

Apesar da divisão inicial de 50/50, as impressões únicas registradas não são equilibradas. O grupo variante tem 50 impressões, enquanto o grupo de controle tem 75 impressões.

### Atrasos nas mensagens no aplicativo 

Para campanhas de mensagens in-app acionadas que incluem exibições atrasadas, as impressões do grupo de controle serão registradas quando o usuário final tiver recebido originalmente a mensagem in-app. Por exemplo, se uma campanha for definida para atrasar a exibição em uma hora, as impressões do grupo de controle não serão registradas até que o atraso de uma hora tenha passado. Isso ajuda no rastreamento preciso das impressões relacionadas ao momento pretendido para a entrega da mensagem.

## Acompanhamentos recomendados {#recommended-follow-ups}

Um teste multivariado e A/B pode (e deve!) inspirar ideias para testes futuros, além de orientá-lo para mudanças na sua estratégia de mensagens. As possíveis ações de acompanhamento incluem o seguinte:

#### Altere sua estratégia de mensagens com base nos resultados dos testes

Seus resultados multivariados podem levá-lo a mudar a forma como você redige ou formata suas mensagens.

#### Mude a maneira como você entende seus usuários

Cada teste esclarecerá o comportamento dos seus usuários, como eles respondem a diferentes canais de mensagens e as diferenças (e semelhanças) entre os seus segmentos.

#### Melhorar a forma como você estrutura os testes futuros

O tamanho de sua amostra era muito pequeno? As diferenças entre suas variantes eram muito sutis? Cada teste oferece uma oportunidade de aprender como melhorar os testes futuros. Se sua confiança for baixa, o tamanho da amostra é muito pequeno e deve ser ampliado para testes futuros. Se não encontrar nenhuma diferença clara entre o desempenho das variantes, é possível que as diferenças sejam sutis demais para ter um efeito perceptível nas respostas dos usuários.

#### Executar um teste de acompanhamento com um tamanho de amostra maior

Amostras maiores aumentarão as chances de detecção de pequenas diferenças entre as variantes.

#### Execute um teste de acompanhamento usando um canal de mensagens diferente

Se você descobrir que uma determinada estratégia é muito eficaz em um canal, talvez queira testar essa estratégia em outros canais. Se um tipo de mensagem for eficaz em um canal, mas não for eficaz em outro, você poderá concluir que determinados canais são mais propícios a determinados tipos de mensagens. Ou talvez haja uma diferença entre os usuários que têm maior probabilidade de ativar as notificações push e aqueles que têm maior probabilidade de prestar atenção às mensagens no aplicativo. Em última análise, a execução desse tipo de teste o ajudará a saber como seu público interage com seus diferentes canais de comunicação.

#### Execute um teste de acompanhamento em um segmento diferente de usuários

Para fazer isso, crie outro teste com o mesmo canal de mensagens e variantes, mas escolha um segmento diferente de usuários. Por exemplo, se um tipo de mensagem foi extremamente eficaz para usuários engajados, pode ser útil investigar seu efeito em usuários desistentes. É possível que os usuários inativos respondam de forma semelhante ou prefiram outra das outras variantes. Esse teste o ajudará a saber mais sobre seus diferentes segmentos e como eles respondem a diferentes tipos de mensagens. Por que fazer suposições sobre seus segmentos quando você pode basear sua estratégia em dados?

#### Executar um teste de acompanhamento com base nos insights de um teste anterior

Use os insights obtidos em testes anteriores para orientar os futuros. Um teste anterior indica que uma técnica de mensagem é mais eficaz? Você não tem certeza de qual aspecto específico de uma variante a tornou melhor? A execução de testes de acompanhamento com base nessas perguntas o ajudará a gerar descobertas criteriosas sobre seus usuários.

#### Comparar o impacto de longo prazo de diferentes variantes

Se estiver fazendo testes A/B com mensagens de reengajamento, não se esqueça de comparar o impacto de longo prazo de diferentes variantes usando [os Relatórios de retenção]({{site.baseurl}}/user_guide/analytics/reporting/retention_reports/). Você pode usar os Relatórios de retenção para analisar como cada variante afetou o comportamento de qualquer usuário de sua escolha dias, semanas, um mês após o recebimento da mensagem e verificar se há aumento.
