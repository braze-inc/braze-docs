---
nav_title: Caminho da vitória
article_title: Caminho vencedor em caminhos de experimentos 
page_type: reference
description: "Este artigo de referência aborda o Winning Path, um recurso que permite que você automatize seus testes A/B quando ativado para uma etapa do Experiment Path."
tool: Canvas
---

# Caminho vencedor em caminhos de experimentos

> O Winning Path é semelhante ao [Winning Variant]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) em campanhas e permite que você automatize seus testes A/B.

Quando o Caminho Vencedor é ativado em uma etapa do Caminho de Experimento, após um período de tempo especificado, todos os usuários subsequentes serão enviados para o caminho com a maior taxa de conversão.

## Usando o Winning Path

### Etapa 1: Adicionar uma etapa do Caminho do Experimento

Adicione um [Caminho de Experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) ao seu Canvas e ative o **Caminho Vencedor**.

Configurações no caminho do experimento intituladas "Distribuir usuários subsequentes no caminho vencedor". A seção inclui um botão de alternância para Winning Path e opções para configurar o evento de conversão e a janela do experimento.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Etapa 2: Configurar as definições do Winning Path

Especifique o evento de conversão que deve determinar o vencedor. Se não houver eventos de conversão disponíveis, retorne à primeira etapa da configuração do Canvas e [atribua eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). 

Se você escolher aberturas ou cliques como seu evento de conversão, certifique-se de que a primeira etapa do caminho seja uma [etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step). O Braze só conta o engajamento a partir da primeira etapa da Mensagem em cada caminho respectivo. Se o caminho começar com uma etapa diferente (como uma etapa de Atraso ou Caminho do público) e a mensagem vier depois, essa mensagem não será incluída na avaliação do desempenho.

Em seguida, defina a **Janela do experimento**. A **Janela do** experimento especifica por quanto tempo o experimento será executado antes que o Caminho vencedor seja determinado e todos os usuários que o seguem sejam enviados para esse caminho. A janela começa quando o primeiro usuário entra na etapa.

Configurações de caminho vencedor com o evento de conversão "Clicks" selecionado para uma janela de experimento de 12 horas.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Etapa 3: Determinar o fallback {#statistical-significance}

Por padrão, se os resultados do teste não forem suficientes para determinar um vencedor estatisticamente significativo, todos os futuros usuários serão enviados para o caminho de melhor desempenho.

Como alternativa, você pode selecionar **Continuar enviando a todos os futuros usuários a combinação de caminhos**. Essa opção enviará os futuros usuários para a combinação de caminhos de acordo com as porcentagens especificadas na distribuição de caminhos do experimento.

\!["Continue enviando a todos os futuros usuários a combinação de caminhos" selecionada como o que acontecerá com os usuários se o resultado do teste não for estatisticamente significativo.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Um Grupo de Atraso só aparecerá na distribuição de caminhos se o Canvas estiver configurado para entrada única e a etapa do Experimento tiver três caminhos ou menos. Os Canvases recorrentes e acionados não terão um Grupo de atraso quando o Caminho vencedor estiver ativado.
{% endalert %}

### Etapa 4: Adicione seus caminhos e inicie o Canvas

Um único componente de Caminho de Experimento pode conter até quatro caminhos. No entanto, se o Canvas estiver configurado para [entrada única](#one-time-entry), um caminho deverá ser reservado para o Delay Group que o Braze adiciona automaticamente quando o Winning Path é ativado. Isso significa que, para Canvases com entrada única, você pode adicionar até três caminhos à sua experiência.

Conclua a configuração do Canvas conforme necessário e, em seguida, inicie-o. Quando o primeiro usuário tiver entrado no experimento, você poderá verificar o Canvas para ver as análises à medida que eles entram e [acompanhar o desempenho do experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance).

Após a conclusão de um Caminho Vencedor, todos os usuários subsequentes que entrarem no Canvas seguirão o Caminho Vencedor, inclusive os usuários que entraram novamente e estavam anteriormente no grupo de controle da etapa do Caminho do Experimento.

## Análises {#analytics}

Se o Winning Path estiver ativado, sua visualização de análise será separada em duas guias: **Experiência inicial** e **caminho de vitória**.

- **Experimento inicial:** Mostra as métricas de cada caminho durante a janela do experimento. Você pode ver um resumo do desempenho de todos os caminhos para os eventos de conversão especificados e qual caminho foi selecionado como vencedor.
- **Caminho da vitória:** Mostra apenas as métricas do Caminho Vencedor a partir do momento em que o Experimento Inicial foi concluído.

## Coisas para saber

### Entrada única {#one-time-entry}

Ao usar Caminhos Vencedores em um Canvas em que os usuários têm permissão para entrar apenas uma vez, um Grupo de Atraso é incluído automaticamente. Durante a duração do experimento, uma porcentagem de usuários será mantida no Grupo de Atraso enquanto os usuários restantes entram em seus Caminhos de Experimento.

Etapa do experimento com um grupo de atrasos para o caminho vencedor]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Quando o teste for concluído e um Caminho Vencedor for determinado, os usuários atribuídos ao Grupo de Atraso serão direcionados para o caminho escolhido e continuarão no Canvas.

\![Etapa de experimento com um grupo de atraso enviado pelo caminho vencedor]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Entrega em horário local

Não recomendamos o uso de entrega em horário local em Canvases with Winning Paths. Isso ocorre porque as janelas de experiência começam quando o primeiro usuário passa por elas. Os usuários que estão em fusos horários muito próximos podem entrar na etapa e acionar o início da janela do experimento muito antes do esperado, o que pode resultar na conclusão do experimento antes que a maioria dos usuários em fusos horários mais comuns tenha tido tempo suficiente para entrar no Canvas ou converter, ou ambos. 

Como alternativa, se desejar usar a entrega local, use uma janela de experiência de 24 a 48 horas ou mais. Dessa forma, os usuários nos primeiros fusos horários entram no Canvas e acionam o início do experimento, mas ainda resta bastante tempo na janela do experimento. Os usuários em fusos horários posteriores ainda terão tempo suficiente para entrar no Canvas e na Etapa do Experimento com Caminhos Vencedores e possivelmente converter antes que a janela do experimento expire.

