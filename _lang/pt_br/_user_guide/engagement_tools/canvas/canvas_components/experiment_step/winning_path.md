---
nav_title: Jornada vencedora 
article_title: Jornada vencedora entre as jornadas do experimento 
page_type: reference
description: "Este artigo de referência aborda a jornada vencedora, um recurso que permite automatizar seus Testes A/B quando ativado para uma etapa da jornada experimental."
tool: Canvas
---

# Jornada vencedora entre as jornadas do experimento

> A Jornada Vencedora é semelhante à [Variante Vencedora]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/optimizations/) em campanhas e permite automatizar seus Testes A/B.

Quando o Winning Path é ativado em uma etapa da jornada experimental, após um período de tempo especificado, todos os usuários subsequentes serão enviados para a jornada com a maior taxa de conversão.

## Usando a jornada vencedora

### Etapa 1: Adicionar uma etapa da jornada experimental

Adicione uma [jornada experimental]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) ao canva e, em seguida, ative a **Jornada vencedora**.

![Configurações na jornada experimental intituladas "Distribuir usuários subsequentes para a jornada vencedora". A seção inclui um botão de alternância para Winning Path e opções para configurar o evento de conversão e a janela de jornada experimental.]({% image_buster /assets/img/experiment_step/experiment_winning_path_recurring.png %})

### Etapa 2: Configurar as definições da jornada vencedora

Especifique o evento de conversão que deve determinar o vencedor. Se não houver eventos de conversão disponíveis, retorne à primeira etapa da configuração do Canva e [atribua eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#choose-conversion-events). Observe que, se você determinar o vencedor com aberturas e cliques, somente a primeira mensagem na jornada que gerar aberturas ou cliques contribuirá para determinar o vencedor.

Em seguida, defina a **Janela do experimento**. A **Janela do** experimento especifica por quanto tempo o experimento será executado antes que a Jornada vencedora seja determinada e todos os usuários que a seguem sejam enviados para essa jornada. A janela começa quando o primeiro usuário entra na etapa.

![Configurações da jornada vencedora com o evento de conversão "Cliques" selecionado para uma janela de jornada experimental de 12 horas.]({% image_buster /assets/img/experiment_step/experiment_winning_settings.png %})

### Etapa 3: Determinar o fallback {#statistical-significance}

Por padrão, se os resultados do teste não forem suficientes para determinar um vencedor estatisticamente significativo, todos os futuros usuários serão enviados para a jornada com melhor performance.

Alternativamente, você pode selecionar **Continue enviando os futuros usuários para essa mistura de jornadas**. Essa opção enviará os futuros usuários para a combinação de jornadas de acordo com as porcentagens especificadas na distribuição da jornada experimental.

!["Continue enviando a todos os futuros usuários a combinação de jornadas" selecionada como o que acontecerá com os usuários se o resultado do teste não for estatisticamente significativo.]({% image_buster /assets/img/experiment_step/experiment_winning_statistical.png %})

{% alert note %}
Um Grupo de postergação só aparecerá em sua distribuição de caminhos se o Canvas estiver configurado para entrada única e a etapa do canva tiver três caminhos ou menos. As telas recorrentes e disparadas não terão um grupo de postergação quando a Jornada vitoriosa estiver ativada.
{% endalert %}

### Etapa 4: Adicione suas jornadas e lance o canva

Um único componente de jornada experimental pode conter até quatro jornadas. No entanto, se o seu canva estiver configurado para [entrada única](#one-time-entry), uma jornada deverá ser reservada para o grupo postergado que a Braze adiciona automaticamente quando a jornada vencedora é ativada. Isso significa que, para canvas com entrada única, você pode adicionar até três jornadas experimentais.

Conclua a configuração do seu canva conforme necessário e, em seguida, inicie-o. Quando o primeiro usuário tiver entrado no experimento, você poderá verificar o Canva para ver a análise de dados à medida que eles entram e [rastrear o desempenho do seu experimento.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#tracking-performance)

Após a conclusão de um Caminho Vencedor, todos os usuários subsequentes que entrarem no Canvas seguirão o Caminho Vencedor, incluindo os usuários que entraram novamente e estavam anteriormente no grupo de controle da etapa da jornada experimental.

## Análise de dados {#analytics}

Se a Jornada vitoriosa estiver ativada, sua visualização de análise de dados será separada em duas guias: **Experiência inicial** e **jornada vencedora**.

- **Experimento inicial:** Mostra as métricas de cada jornada durante a janela do experimento. Você pode ver um resumo da performance de todas as jornadas para os eventos de conversão especificados e qual jornada foi selecionada como vencedora.
- **Jornada vencedora:** Mostra apenas as métricas da jornada vencedora a partir do momento em que o experimento inicial foi concluído.

## Coisas para saber

### Entrada única {#one-time-entry}

Ao usar jornadas vencedoras em um canva em que os usuários podem entrar apenas uma vez, um grupo de postergação agora é incluído automaticamente. Durante a duração da experiência, uma porcentagem de usuários será mantida no Grupo de postergação enquanto os usuários restantes entram em suas jornadas experimentais.

![Etapa da jornada experimental com um grupo de postergação para o caminho vencedor]({% image_buster /assets/img/experiment_step/experiment_one_time.png %}){: style="max-width:75%"}

Quando o teste for concluído e um Caminho Vencedor for determinado, os usuários atribuídos ao Grupo de postergação serão direcionados para a jornada escolhida e continuarão no Canva.

![Etapa da jornada experimental com um grupo de postergação enviado pelo caminho vencedor]({% image_buster /assets/img/experiment_step/experiment_one_time_results.png %}){: style="max-width:75%"}

### Entrega no horário local

Não recomendamos o uso de entrega no horário local em Canvas with Winning Paths. Isso ocorre porque as janelas de experiência começam quando o primeiro usuário passa por elas. Os usuários que estão em fusos horários muito próximos podem entrar na etapa do canva e disparar o início da janela do experimento muito mais cedo do que o esperado, o que pode resultar na conclusão do experimento antes que a massa de usuários em fusos horários mais comuns tenha tido tempo suficiente para entrar no canva ou converter, ou ambos. 

Como alternativa, se desejar usar a entrega na localização, use uma janela de experiência de 24 a 48 horas ou mais. Dessa forma, os usuários nos primeiros fusos horários entram no Canva e disparam o início do experimento, mas ainda resta bastante tempo na janela do experimento. Os usuários que estiverem em fusos horários posteriores ainda terão tempo suficiente para entrar no Canva e na etapa do experimento com as jornadas experimentais e possivelmente converter antes que a janela do experimento expire.

