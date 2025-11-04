---
nav_title: Caminhos personalizados
article_title: Caminhos personalizados em Caminhos de experimentos 
page_type: reference
description: "O Personalized Paths permite personalizar qualquer ponto de uma jornada do Canvas para usuários individuais com base na probabilidade de conversão."
tool: Canvas
---

# Caminhos personalizados em Caminhos de experimentos

> O Personalized Paths é semelhante ao [Personalized Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/#personalized-variant) nas campanhas e permite personalizar qualquer ponto de uma jornada do Canvas para usuários individuais com base na probabilidade de conversão.

## Como funciona o Personalized Paths

Quando os Caminhos personalizados são ativados em uma etapa do Caminho de experimento, o comportamento é ligeiramente diferente, dependendo se o Canvas está configurado para enviar uma vez ou para se repetir:

- **Canvas de envio único:** Um grupo de usuários é retido em um grupo de atraso. Os usuários restantes passam por um teste inicial para treinar um modelo preditivo por um período que você configurar - pelo menos 24 horas para obter melhores resultados. Após o teste, é criado um modelo para saber quais comportamentos do usuário foram associados a uma maior probabilidade de conversão em um determinado caminho. Por fim, cada usuário do grupo de atraso é enviado ao caminho com maior probabilidade de resultar em conversão com base nos comportamentos que exibem e no que o modelo preditivo aprendeu durante o teste inicial.
- **Canvases recorrentes, acionados por ação e acionados por API:** Um experimento inicial é realizado em todos os usuários que entram no Caminho do Experimento durante uma janela especificada. Para manter a integridade do experimento, se um usuário receber várias mensagens antes do término da janela, ele será atribuído à mesma variante todas as vezes. Após a janela de experiência, cada usuário é enviado para o caminho com maior probabilidade de resultar em conversão para ele.

## Usando caminhos personalizados

### Etapa 1: Adicionar um caminho de experimento

Adicione um [caminho de experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) ao seu Canvas e, em seguida, ative **os caminhos personalizados**.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### Etapa 2: Configurar as definições de Caminhos personalizados

Especifique o evento de conversão que deve determinar o vencedor. Se não houver eventos de conversão disponíveis, retorne à primeira etapa da configuração do Canvas e [atribua eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). 

Se você escolher aberturas ou cliques como seu evento de conversão, certifique-se de que a primeira etapa do caminho seja uma [etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step). O Braze só conta o engajamento a partir da primeira etapa da Mensagem em cada caminho respectivo. Se o caminho começar com uma etapa diferente (como uma etapa de Atraso ou Caminho do público) e a mensagem vier depois, essa mensagem não será incluída na avaliação do desempenho.

Em seguida, defina a **Janela do experimento**. A **janela de experiência** determina por quanto tempo os usuários serão enviados por todos os caminhos antes de escolher o melhor caminho para cada usuário no grupo de atraso. A janela começa quando o primeiro usuário entra na etapa.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### Etapa 3: Determinar o fallback

Por padrão, se os resultados do teste não forem suficientes para determinar um vencedor estatisticamente significativo, todos os futuros usuários serão enviados para o caminho único de melhor desempenho.

Como alternativa, você pode selecionar **Continuar enviando a todos os futuros usuários a combinação de caminhos**.

\![]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

Essa opção enviará os futuros usuários para a combinação de caminhos de acordo com as porcentagens especificadas na distribuição de caminhos do experimento.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

### Etapa 4: Adicione seus caminhos e inicie o Canvas

{% tabs local %}
{% tab Single-send Canvas %}

Um único componente de Caminho de Experimento pode conter até quatro caminhos. No entanto, para Canvases de envio único, você pode adicionar até três caminhos quando Personalized Paths (Caminhos personalizados) estiver ativado. O quarto caminho deve ser reservado para o Delay Group que o Braze adiciona automaticamente ao seu experimento.

Conclua a configuração do Canvas conforme necessário e, em seguida, inicie-o. Quando o primeiro usuário tiver entrado no experimento, você poderá verificar o Canvas para ver as análises à medida que eles entram e [acompanhar o desempenho do experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

Quando a janela do experimento passar e ele for concluído, o Braze enviará os usuários do grupo de atraso para seus respectivos caminhos com a maior probabilidade personalizada de conversão com base na recomendação do modelo preditivo.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Recurring or action-triggered or API-triggered Canvas %}

É possível testar até quatro caminhos em um único caminho de experimento. Adicione seus caminhos e termine de configurar o Canvas conforme necessário e, em seguida, inicie-o.  

Quando o primeiro usuário tiver entrado no experimento, você poderá verificar o Canvas para ver as análises à medida que eles entram e [acompanhar o desempenho do experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

Quando a janela do experimento passar e o experimento for concluído, todos os usuários subsequentes que entrarem no Canvas serão enviados para o caminho com maior probabilidade de resultar em conversão para eles.

\![]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Análises {#analytics}

Se Personalized Paths estiver ativado, sua visualização de análise será separada em duas guias: **Experiência inicial** e **caminhos personalizados**.

{% tabs local %}
{% tab Initial Experiment %}

A guia **Initial Experiment (Experimento inicial** ) mostra as métricas de cada caminho durante a janela do experimento. Você pode ver um resumo do desempenho de todos os caminhos para os eventos de conversão especificados.

\![Resultados de um experimento inicial enviado para determinar o caminho de melhor desempenho para cada usuário. Uma tabela mostra o desempenho de cada caminho com base em várias métricas para o canal de destino.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

Por padrão, o teste procura associações entre os eventos personalizados do usuário e suas preferências de caminho, ou a variante de mensagem à qual o usuário responde melhor. Essa análise detecta se os eventos personalizados aumentam ou diminuem a probabilidade de resposta a um determinado caminho. Essas relações são usadas para determinar quais usuários recebem qual caminho depois que a janela do experimento passa.

As relações entre os eventos personalizados e as preferências de caminho são exibidas na tabela da guia **Experiência inicial**.

\![]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

Se o teste não conseguir encontrar uma relação significativa entre os eventos personalizados e as preferências de caminho, o teste voltará para um método de análise baseado em sessão.

{% details Fallback analysis method %}

**Método de análise baseado em sessão**<br>
Se o método de fallback for usado para determinar os Caminhos personalizados, a guia **Experiência inicial** mostrará um detalhamento das variantes preferidas dos usuários com base em uma combinação de determinadas características.

Essas características são:

- **Recência:** Quando foi a última vez que tiveram uma sessão
- **Frequência:** Com que frequência eles têm sessões
- **Posse:** Há quanto tempo é usuário

A tabela Características do usuário, que mostra quais usuários devem preferir o Caminho 1 e o Caminho 2 com base nos três grupos em que se enquadram em termos de recência, frequência e permanência.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

Pense em recência como a última interação que tiveram com você, frequência como a frequência com que se envolvem e permanência como o período geral de tempo em que se envolveram com você. Agrupamos os usuários em "grupos" com base nesses três aspectos (conforme explicado na tabela **Características do usuário** ) e, em seguida, verificamos qual grupo gosta mais de qual caminho. É como classificar os usuários em centenas de listas diferentes com base em quando eles compraram pela última vez com você, com que frequência compram e há quanto tempo são clientes.

Quando se trata de escolher uma mensagem para um usuário, o Braze examina os grupos em que ele se enquadra. Cada balde exerce uma influência distinta na seleção de caminhos para os usuários. Quantificamos essa influência usando um método estatístico chamado [regressão logística](https://en.wikipedia.org/wiki/Logistic_regression), que é uma forma de prever o comportamento futuro com base em ações passadas. Esse método leva em conta as interações do usuário durante o envio da mensagem inicial. Essa tabela apenas resume os resultados, mostrando com qual caminho os usuários de cada grupo tendem a se envolver.

Por fim, o Braze combina todos esses dados para selecionar um caminho de mensagem personalizado para cada usuário, para garantir que seja o mais envolvente e relevante possível para ele.

{% alert note %}
Os intervalos de tempo para cada intervalo são determinados com base nos dados do usuário específicos do Canvas, que podem variar entre os Canvases.
{% endalert %}

**Como os caminhos personalizados são selecionados**<br>
Com esse método, a mensagem recomendada de um usuário individual é a soma dos efeitos de sua recenticidade, frequência e permanência específicas. A recência, a frequência e a permanência são divididas em grupos, conforme ilustrado na tabela **Características do usuário**. O intervalo de tempo de cada intervalo é determinado pelos dados dos usuários em cada Canvas individual e mudará de Canvas para Canvas.

Cada balde pode ter uma contribuição ou "empurrão" diferente para cada caminho. A força do impulso para cada balde é determinada a partir das respostas dos usuários no experimento inicial usando [regressão logística](https://en.wikipedia.org/wiki/Logistic_regression). Essa tabela apenas resume os resultados, mostrando com qual caminho os usuários de cada grupo tendem a se envolver. O Caminho Personalizado real de qualquer usuário individual depende da soma dos efeitos dos três grupos em que ele se encontra - um para cada característica.

{% enddetails %}

{% endtab %}
{% tab Personalized Paths %}

A guia **Personalized Paths (Caminhos personalizados** ) mostra os resultados do experimento final, em que os usuários do Delay Group (Grupo de atraso) foram enviados para o caminho de melhor desempenho para eles.

Os três cartões nesta página mostram sua elevação projetada, os resultados gerais e os resultados projetados se, em vez disso, você enviasse apenas o Caminho Vencedor. Mesmo que não haja aumento, o que às vezes pode acontecer, o resultado é o mesmo que enviar apenas o Caminho vencedor (um teste A/B tradicional).

- **Elevação projetada:** A melhoria no evento de conversão selecionado devido ao uso de caminhos personalizados em vez de enviar cada usuário pelo caminho geral de melhor desempenho.
- **Resultados gerais:** Os resultados do segundo envio com base em seu evento de conversão.
- **Resultados projetados:** Os resultados projetados do segundo envio com base na métrica de otimização escolhida, caso você tivesse enviado apenas a Variante vencedora.

\![Guia Caminhos personalizados para um Canvas. Os cartões mostram o aumento projetado, as conversões gerais (com caminhos personalizados) e as aberturas exclusivas projetadas (com caminho vencedor).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Uso de caminhos personalizados com entrega em horário local

Não recomendamos o uso de entrega em horário local em Telas com Caminhos Personalizados. Isso ocorre porque as janelas de experiência começam quando o primeiro usuário passa por elas. Os usuários que estão em fusos horários muito próximos podem entrar na etapa e acionar o início da janela do experimento muito antes do esperado, o que pode resultar na conclusão do experimento antes que a maioria dos usuários em fusos horários mais comuns tenha tido tempo suficiente para entrar no Canvas e converter.

Como alternativa, se desejar usar a entrega local, use uma janela de experiência de 24 a 48 horas ou mais. Dessa forma, os usuários nos primeiros fusos horários entram no Canvas e acionam o início do experimento, mas ainda resta bastante tempo na janela do experimento. Os usuários em fusos horários posteriores ainda terão tempo suficiente para entrar no Canvas e na Etapa do Experimento com Caminhos Personalizados e possivelmente converter antes que a janela do experimento expire.

