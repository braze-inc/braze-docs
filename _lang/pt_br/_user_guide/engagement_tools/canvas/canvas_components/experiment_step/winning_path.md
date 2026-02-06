---
nav_title: Jornada vencedora
article_title: Jornada vencedora entre as jornadas do experimento 
page_type: reference
description: "Este artigo de referência aborda a jornada vencedora, um recurso que permite automatizar seus Testes A/B quando ativado para uma etapa da jornada experimental."
tool: Canvas
---

# Jornada vencedora entre as jornadas do experimento

> A Jornada Vencedora é semelhante à [Variante Vencedora]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) em campanhas e permite automatizar seus Testes A/B.

Quando o Winning Path é ativado em uma etapa da jornada experimental, após um período de tempo especificado, todos os usuários subsequentes são enviados para a jornada com a maior taxa de conversão.

## Usando a jornada vencedora

### Etapa 1: Adicionar uma etapa da jornada experimental

Adicione uma [jornada experimental]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) ao canva e, em seguida, ative a **Jornada vencedora**.

![Configurações na jornada experimental intituladas "Distribuir usuários subsequentes para a jornada vencedora". A seção inclui um botão de alternância para jornada vencedora e opções para configurar o evento de conversão e a janela de jornada experimental.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Etapa 2: Configurar as definições da jornada vencedora

Especifique o evento de conversão que deve determinar o vencedor. Se não houver eventos de conversão disponíveis, retorne à primeira etapa da configuração do Canva e [atribua eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). 

Se você escolher aberturas ou cliques como seu evento de conversão, certifique-se de que a primeira etapa da jornada seja uma [etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step). O Braze só conta o engajamento a partir da primeira etapa da mensagem em cada jornada respectiva. Se o caminho começar com uma etapa diferente (como uma etapa de postergação ou de jornada do público) e a mensagem vier depois, essa mensagem não será incluída na avaliação do desempenho.

Em seguida, defina a **Janela do experimento**. A **Janela do experimento** especifica por quanto tempo o experimento é executado antes que o Caminho vencedor seja determinado e todos os usuários que o seguem sejam enviados para esse caminho. A janela começa quando o primeiro usuário entra na etapa.

![Configurações da jornada vencedora com o evento de conversão "Cliques" selecionado para uma janela de jornada experimental de 12 horas.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Etapa 3: Determinar o fallback {#statistical-significance}

Por padrão, se os resultados do teste não forem suficientes para determinar um vencedor estatisticamente significativo, todos os futuros usuários serão enviados para a jornada com melhor performance. Alternativamente, você pode selecionar **Continue enviando os futuros usuários para essa mistura de jornadas**. Essa opção envia futuros usuários para a combinação de jornadas de acordo com as porcentagens especificadas na distribuição da jornada experimental.

!["Continuar enviando a todos os futuros usuários a combinação de jornadas" selecionada como o que acontece com os usuários se o resultado do teste não for estatisticamente significativo.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Um Grupo de postergação aparece na distribuição de caminhos somente se o Canvas estiver configurado para entrada única e a etapa da jornada experimental tiver três caminhos ou menos. As telas recorrentes e disparadas não têm um grupo de postergação quando a jornada vencedora está ativada.
{% endalert %}

### Etapa 4: Adicione suas jornadas e lance o canva

Um único componente de jornada experimental pode conter até quatro jornadas. No entanto, se o seu canva estiver configurado para [entrada única](#one-time-entry), uma jornada deverá ser reservada para o grupo postergado que a Braze adiciona automaticamente quando a jornada vencedora é ativada. Isso significa que, para canvas com entrada única, você pode adicionar até três jornadas experimentais.

Conclua a configuração do seu canva conforme necessário e, em seguida, inicie-o. Quando o primeiro usuário tiver entrado no experimento, você poderá verificar o Canva para ver a análise de dados à medida que eles entram e [rastrear o desempenho do seu experimento.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance)

Depois que um Caminho Vencedor é concluído, todos os usuários subsequentes que entram no Canvas seguem o Caminho Vencedor, incluindo os usuários que entraram novamente e estavam anteriormente no grupo de controle da etapa da jornada experimental.

## Análise de dados {#analytics}

Se a opção Jornada vitoriosa estiver ativada, sua visualização de análise de dados será separada em duas guias: **Experiência inicial** e **jornada vencedora**.

- **Experimento inicial:** Mostra as métricas de cada jornada durante a janela do experimento. Você pode ver um resumo da performance de todas as jornadas para os eventos de conversão especificados e qual jornada foi selecionada como vencedora.
- **Jornada vencedora:** Mostra apenas as métricas da jornada vencedora a partir do momento em que o experimento inicial foi concluído.

## Coisas para saber

### Entrada única {#one-time-entry}

Ao usar jornadas vencedoras em um canva em que os usuários podem entrar apenas uma vez, um grupo de postergação agora é incluído automaticamente. Durante a duração da experiência, uma porcentagem de usuários é mantida no Grupo de postergação enquanto os usuários restantes entram em suas jornadas experimentais.

![Etapa da jornada experimental com um grupo de postergação para a jornada vencedora]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Quando o teste termina e um Caminho Vencedor é determinado, os usuários atribuídos ao Grupo de Postergação são direcionados para a jornada escolhida e continuam no Canva.

![Etapa da jornada experimental com um grupo de postergação enviado pelo caminho vencedor]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Entrega no horário local

Não recomendamos o uso de entrega no horário local em Canvas with Winning Paths. Isso ocorre porque as janelas de experiência começam quando o primeiro usuário passa por elas. Os usuários que estão em fusos horários muito próximos podem entrar na etapa do canva e disparar o início da janela do experimento muito mais cedo do que o esperado, o que pode resultar na conclusão do experimento antes que a massa de usuários em fusos horários mais comuns tenha tido tempo suficiente para entrar no canva ou converter, ou ambos. 

Como alternativa, se desejar usar a entrega na localização, use uma janela de experiência de 24 a 48 horas ou mais. Dessa forma, os usuários nos primeiros fusos horários entram no Canva e disparam o início do experimento, mas ainda resta bastante tempo na janela do experimento. Os usuários em fusos horários posteriores ainda têm tempo suficiente para entrar no Canva e na etapa da jornada experimental com caminhos vencedores e possivelmente converter antes que a janela da experiência expire.

### Variantes baseadas em cliques

Se estiver configurando uma variante da Jornada Vencedora com base em cliques, cada interação conta como um clique, a menos que seja identificada como um clique de cancelamento de inscrição pelo Braze.
