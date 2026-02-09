---
nav_title: Jornadas personalizadas
article_title: Jornadas personalizadas em jornadas de experimento 
page_type: reference
description: "Caminhos Personalizados permite personalizar qualquer ponto de uma jornada de canva para usuários individuais com base na probabilidade de conversão."
tool: Canvas
---

# Jornadas personalizadas em jornadas de experimento

> Caminhos Personalizados é semelhante a [Variante Personalizada]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/#personalized-variant) em campanhas e permite que você personalize qualquer ponto de uma jornada de canva para usuários individuais com base na probabilidade de conversão.

## Como funcionam os Caminhos Personalizados

Quando a Personalização de Jornadas está ativada em uma etapa da jornada experimental, o comportamento é ligeiramente diferente dependendo se o seu canva está configurado para enviar uma vez ou para se repetir:

- **Canva de envio único:** Um grupo de usuários é retido em um grupo de postergação. Os usuários restantes passam por um teste inicial para treinar um modelo de previsão por um período que você configurar - pelo menos 24 horas para obter melhores resultados. Após o teste, um modelo é criado para aprender quais comportamentos do usuário estavam associados a uma maior probabilidade de conversão em uma determinada jornada. Por fim, cada usuário do grupo de postergação é enviado para a jornada com maior probabilidade de resultar em conversão, com base nos comportamentos que exibem e no que o modelo de previsão aprendeu durante o teste inicial.
- **Canvas recorrentes, acionados por ação e acionados por API:** Um experimento inicial é realizado em todos os usuários que entram na jornada experimental durante um período especificado. Para manter a integridade do experimento, se um usuário receber várias mensagens antes do término da janela, ele será atribuído à mesma variante cada vez. Após a janela do experimento, cada usuário é enviado pela jornada mais provável de resultar em conversão para eles.

## Usando Caminhos Personalizados

### Etapa 1: Adicionar uma jornada experimental

Adicione uma [jornada experimental]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) ao seu canva, depois ative **Jornadas personalizadas**.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_path.png %})

### Etapa 2: Configurar configurações de Caminhos Personalizados

Especifique o evento de conversão que deve determinar o vencedor. Se não houver eventos de conversão disponíveis, retorne à primeira etapa da configuração do Canva e [atribua eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). 

Se você escolher aberturas ou cliques como seu evento de conversão, certifique-se de que a primeira etapa da jornada seja uma [etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step). O Braze só conta o engajamento a partir da primeira etapa da mensagem em cada jornada respectiva. Se o caminho começar com uma etapa diferente (como uma etapa de postergação ou de jornada do público) e a mensagem vier depois, essa mensagem não será incluída na avaliação do desempenho.

Em seguida, defina a **Janela de Experimento**. A **Janela de Experimento** determina quanto tempo os usuários serão enviados por todas as jornadas antes de escolher o melhor caminho para cada usuário no grupo de postergação. A janela começa quando o primeiro usuário entra na etapa.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_settings.png %})

### Etapa 3: Determine fallback

Por padrão, se os resultados do teste não forem suficientes para determinar um vencedor estatisticamente significativo, todos os futuros usuários serão enviados pela única jornada de melhor desempenho.

Alternativamente, você pode selecionar **Continue enviando os futuros usuários para essa mistura de jornadas**.

![]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

Essa opção enviará os futuros usuários para a combinação de jornadas de acordo com as porcentagens especificadas na distribuição da jornada experimental.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_percentages.png %})

### Etapa 4: Adicione suas jornadas e lance o canva

{% tabs local %}
{% tab Single-send Canvas %}

Um único componente de jornada experimental pode conter até quatro jornadas. No entanto, para canvas de envio único, você pode adicionar até três jornadas quando Jornadas personalizadas estiverem ativadas. O quarto jornada deve ser reservado para o Grupo de Postergação que a Braze adiciona automaticamente ao seu experimento.

Conclua a configuração do seu canva conforme necessário e, em seguida, inicie-o. Quando o primeiro usuário tiver entrado no experimento, você poderá verificar o Canva para ver a análise de dados à medida que eles entram e [rastrear o desempenho do seu experimento.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance)

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_pending.png %}){: style="max-width:75%;" }

Quando a janela do experimento passar e o experimento for concluído, o Braze enviará os usuários do grupo de postergação para suas respectivas jornadas com a maior probabilidade personalizada de conversão com base na recomendação do modelo de previsão.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_delay_group_complete.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Recurring or action-triggered or API-triggered Canvas %}

Você pode testar até quatro jornadas em uma única jornada experimental. Adicione suas jornadas e termine de configurar seu canva conforme necessário, depois lance-o.  

Quando o primeiro usuário tiver entrado no experimento, você pode verificar a canva para ver a análise de dados conforme elas chegam e [acompanhar a performance do seu experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

Quando a janela do experimento passa e o experimento é concluído, todos os usuários subsequentes que entrarem na canva serão enviados pelo jornada mais provável de resultar em conversão para eles.

![]({% image_buster /assets/img/experiment_step/experiment_personalized_recurring_analytics.png %}){: style="max-width:75%;" }

{% endtab %}
{% endtabs %}

## Análise de dados {#analytics}

Se os Caminhos Personalizados estiverem ativados, sua visão de análise de dados será separada em duas guias: **Experimento Inicial** e **Caminhos Personalizados**.

{% tabs local %}
{% tab Initial Experiment %}

A guia **Experimento Inicial** mostra as métricas para cada jornada durante a janela do experimento. Você pode ver um resumo de como todas as jornadas se saíram para os eventos de conversão especificados.

![Resultados de um experimento inicial enviado para determinar a melhor jornada para cada usuário. Uma tabela mostra a performance de cada jornada com base em várias métricas para o canal de direcionamento.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1.png %})

Por padrão, o teste procura associações entre os eventos personalizados do usuário e suas preferências de jornada, ou a variante de mensagem à qual o usuário responde melhor. Esta análise detecta se eventos personalizados aumentam ou diminuem a probabilidade de responder a uma jornada específica. Esses relacionamentos são então usados para determinar quais usuários são atribuídos a qual jornada após a janela do experimento passar.

As relações entre os eventos personalizados e as preferências de jornada são exibidas na tabela da guia **Jornada experimental inicial**.

![]({% image_buster /assets/img_archive/experiment_personalized_analytics_custom_data.png %})

Se o teste não conseguir encontrar uma relação significativa entre eventos personalizados e preferências de jornada, o teste voltará para um método de análise baseado em sessão e nenhuma tabela de dados de eventos personalizados será exibida.

{% details Fallback analysis method %}

**Método de análise baseado em sessão**<br>
Se o método fallback for usado para determinar Caminhos Personalizados, a **Experiência Inicial** guia mostra uma análise das variantes preferidas dos usuários com base em uma combinação de certas características.

Essas características são:

- **Recência:** Quando foi a última vez que tiveram uma sessão
- **Frequência:** Com que frequência eles têm sessões
- **Posse:** Há quanto tempo é usuário

![A tabela Características do usuário, que mostra quais usuários têm previsão de preferir a Jornada 1 e a Jornada 2 com base nos três grupos em que se enquadram em termos de recência, frequência e permanência.]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab1_2.png %})

Pense na {recency} como quão recente foi a última interação deles com você, {frequency} como a frequência com que eles se envolvem e {tenure} como a duração total do tempo que eles têm se envolvido com você. Agrupamos os usuários em "baldes" com base nessas três coisas (conforme explicado na tabela **Características dos Usuários**) e depois vemos qual balde gosta mais de qual jornada. É como classificar os usuários em centenas de listas diferentes com base em quando eles compraram pela última vez com você, com que frequência compram e há quanto tempo são clientes.

Quando se trata de escolher uma mensagem para um usuário, a Braze examina os grupos nos quais eles se enquadram. Cada bucket exerce uma influência distinta na seleção da jornada dos usuários. Quantificamos essa influência usando um método estatístico chamado [regressão logística](https://en.wikipedia.org/wiki/Logistic_regression), que é uma forma de prever comportamentos futuros com base em ações passadas. Este método leva em conta as interações do usuário durante o envio inicial da mensagem. Esta tabela apenas resume os resultados exibindo com qual jornada os usuários em cada grupo tendiam a se envolver.

Em última análise, a Braze combina todos esses dados para selecionar uma jornada de mensagens personalizada para cada usuário, para garantir que seja o mais envolvente e relevante possível para eles.

{% alert note %}
Os intervalos de tempo para cada bucket são determinados com base em dados de usuários específicos da canva, que podem variar entre canvas.
{% endalert %}

**Como os Caminhos Personalizados são selecionados**<br>
Com este método, a mensagem recomendada para um usuário individual é a soma dos efeitos de sua recência, frequência e tempo específicos. Recência, frequência e tempo de serviço são divididos em categorias, conforme ilustrado na tabela de **Características do Usuário**. O intervalo de tempo de cada bucket é determinado pelos dados dos usuários em cada canva individual e mudará de canva para canva.

Cada bucket pode ter uma contribuição diferente ou "push" para cada jornada. A força do push para cada balde é determinada a partir das respostas dos usuários no experimento inicial usando [regressão logística](https://en.wikipedia.org/wiki/Logistic_regression). Esta tabela apenas resume os resultados exibindo com qual jornada os usuários em cada grupo tendiam a se envolver. O caminho personalizado real de qualquer usuário individual depende da soma dos efeitos dos três baldes em que eles estão - um para cada característica.

{% enddetails %}

{% endtab %}
{% tab Personalized Paths %}

A guia **Jornadas Personalizadas** mostra os resultados do experimento final, onde os usuários do Grupo de Postergação foram direcionados para a jornada de melhor desempenho para eles.

As três cartas nesta página mostram sua elevação projetada, resultados gerais e os resultados projetados se você enviasse apenas a jornada vencedora. Mesmo que não haja elevação, o que às vezes pode acontecer, o resultado é o mesmo que enviar apenas a Jornada Vencedora (um teste A/B tradicional).

- **Elevação projetada:** A melhoria no seu evento de conversão selecionado devido ao uso de Jornadas Personalizadas em vez de enviar todos os usuários pelo caminho de melhor desempenho geral.
- **Resultados gerais:** Os resultados do segundo envio com base no seu evento de conversão.
- **Resultados projetados:** Os resultados projetados do segundo envio com base na métrica de otimização escolhida se você tivesse enviado apenas a Variante Vencedora.

![Guia de Caminhos Personalizados para um Canva. Os cartões mostram o aumento projetado, as conversões gerais (com jornadas personalizadas) e as aberturas exclusivas projetadas (com a jornada vencedora).]({% image_buster /assets/img/experiment_step/experiment_personalized_analytics_tab2.png %})

{% endtab %}
{% endtabs %}

## Usando Caminhos Personalizados com entrega no horário local

Não recomendamos usar entrega no horário local em canvas com Caminhos Personalizados. Isso ocorre porque as janelas de experimentos começam quando o primeiro usuário passa. Os usuários que estão em fusos horários muito adiantados podem entrar na etapa e disparar o início da janela do experimento muito antes do que você espera, o que pode resultar na conclusão do experimento antes que a maior parte dos seus usuários em fusos horários mais típicos tenham tido tempo suficiente para entrar no canva e converter.

Alternativamente, se você deseja usar a entrega local, use uma janela de experimento de 24-48 ou mais horas. Dessa forma, os usuários em fusos horários iniciais entram na canva e disparam o experimento para começar, mas ainda resta bastante tempo na janela do experimento. Os usuários em fusos horários posteriores ainda terão tempo suficiente para entrar na canva e na etapa do experimento com caminhos personalizados e possivelmente converter antes que a janela do experimento expire.

