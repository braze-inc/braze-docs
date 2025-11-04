---
nav_title: Caminhos de experimentos
article_title: Caminhos de experimentos 
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Este artigo aborda o Experiment Paths, um componente que permite testar vários caminhos do Canvas entre si e com um grupo de controle em qualquer ponto da jornada do usuário."
tool: Canvas
---

# Caminhos de experimentos

> Os caminhos de experiência permitem testar vários caminhos do Canvas entre si e com um grupo de controle em qualquer ponto da jornada do usuário. Usando esse componente, você pode acompanhar o desempenho do caminho para tomar decisões informadas sobre sua jornada no Canvas.

Quando você inclui uma etapa Experiment Paths na jornada do usuário, ela atribui aleatoriamente os usuários a diferentes caminhos (ou a um grupo de controle opcional) criados por você. Partes do público-alvo serão atribuídas a diferentes caminhos de acordo com as porcentagens selecionadas, permitindo que você teste diferentes mensagens ou caminhos entre si e determine qual é o mais eficaz. 

\![Uma etapa do Caminho de Experimento que se divide em Caminho 1, Caminho 2 e Controle.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Casos de uso

Os caminhos de experimento são mais adequados para testar a entrega, a cadência, o texto da mensagem e as combinações de canais.

- **Entrega:** Compare os resultados entre as mensagens enviadas com diferentes [atrasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) de tempo, com base nas ações do usuário[(caminhos de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)) e usando o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#canvas).<br><br>
- **Cadência:** Teste vários fluxos de mensagens em um período específico. Por exemplo, você pode testar duas cadências de integração diferentes:
    - Cadência 1: Enviar 2 mensagens nas primeiras 2 semanas do usuário
    - Cadência 2: Envie 3 mensagens nas primeiras 2 semanas do usuário
    
    Ao segmentar usuários inativos, você pode testar a eficácia do envio de duas mensagens de recuperação em uma semana em comparação com o envio de apenas uma.
- **Cópia da mensagem:** Semelhante a um [teste A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) padrão, você pode testar diferentes textos de mensagens para ver qual texto resulta em uma taxa de conversão mais alta.<br><br>
- **Combinações de canais:** Teste a eficácia de diferentes combinações de canais de mensagens. Por exemplo, você pode comparar o impacto do uso de apenas um e-mail versus um e-mail combinado com um push.

## Pré-requisito

Para usar os caminhos de experiência, seu Canvas deve incluir eventos de conversão. Embora não seja possível adicionar eventos de conversão após o lançamento de um Canvas, você pode clonar o Canvas lançado e adicionar eventos de conversão para adicionar Caminhos de Experimentos.

## Criação de um caminho de experimento

Para criar um componente Experiment Paths, primeiro adicione uma etapa ao seu Canvas. Arraste e solte o componente da barra lateral ou clique no botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Experiment Paths (Caminhos de experimentos**). 

Na configuração padrão desse componente, há dois caminhos padrão, **Path 1** e **Path 2**, com 50% do público sendo enviado por cada caminho. Clique no componente para expandir o painel **Experiment Settings** e você verá as opções de configuração do componente.

### Etapa 1: Escolha o número de caminhos e a distribuição do público

Você pode adicionar até quatro caminhos clicando em **Add Path (Adicionar caminho** ) e um grupo de controle opcional marcando **Add a Control Group (Adicionar grupo de controle**). Usando as caixas de porcentagem para cada caminho, você pode especificar a porcentagem do público que deve ir para cada caminho e para o grupo de controle. As porcentagens fornecidas devem somar 100% para prosseguir. Se quiser definir rapidamente todos os caminhos disponíveis (e o controle) com a mesma porcentagem, clique em **Distribute Paths Evenly (Distribuir caminhos uniformemente**).

Também é possível escolher se os usuários do grupo de controle devem continuar no Canvas ou sair após a janela de rastreamento de conversão para o **Comportamento do grupo de controle**. Opcionalmente, você pode adicionar uma descrição para explicar aos outros o que esse caminho de experimento pretende testar ou incluir informações adicionais que possam ser úteis.

\![Experiment Settings (Configurações de experimentos), onde é possível adicionar caminhos e distribuir a porcentagem de usuários em cada caminho.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Se a reelegibilidade do Canvas estiver ativada, os usuários que entrarem no Canvas e percorrerem um caminho escolhido aleatoriamente percorrerão o mesmo caminho novamente se se tornarem reelegíveis e entrarem novamente no Canvas. Isso mantém a validade do experimento e das análises associadas. Se você quiser que a etapa sempre randomize a atribuição de caminhos, selecione **Randomized Paths (Caminhos aleatórios) em Experiment Paths (Caminhos de experimentos**). Essa opção não está disponível ao usar Caminhos vencedores ou personalizados.
{% endalert %}

### Etapa 2: Ativar o Winning Path ou o Personalized Paths (opcional) {#step-2}

Você pode optar por otimizar seu experimento ativando [Winning Path (Caminho vencedor]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path) ) ou [Personalized Paths (Caminhos personalizados]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths)). Ambas as opções funcionam testando inicialmente seus caminhos com uma parte do seu público. Após o término do experimento, os usuários restantes e subsequentes são enviados para o caminho com melhor desempenho geral (Caminho vencedor) ou para o caminho com melhor desempenho para cada usuário (Caminhos personalizados).

### Etapa 3: Criar caminhos

Por fim, você deve criar seus caminhos downstream. Selecione **Concluído** e retorne ao construtor do Canvas. Clique no botão de adição <i class="fas fa-plus-circle"></i> abaixo de cada caminho para começar a criar jornadas usando as ferramentas usuais do Canvas, conforme sua preferência, e inicie o Canvas quando estiver pronto.

\![Adição de etapas a cada caminho que se divide de um componente de Caminho de Experimento.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Lembre-se de que os caminhos e suas etapas posteriores não podem ser removidos de um Canvas depois de criados. No entanto, quando iniciada, você pode modificar a distribuição do público-alvo entre os caminhos conforme achar adequado. Por exemplo, se um dia depois de lançar um Canvas, você concluir que um caminho é superior aos demais com base na análise, poderá definir esse caminho como 100% e os outros como 0%. Ou, dependendo das suas necessidades, você pode continuar enviando os usuários por vários caminhos.

{% alert important %}
Para evitar a contaminação do experimento, se o seu Canvas tiver um experimento de Caminho vencedor ou Caminho personalizado ativo ou em andamento e você atualizar o Canvas ativo, independentemente de atualizar a própria etapa do Caminho do experimento, o experimento em andamento será encerrado e a etapa do experimento não determinará um caminho vencedor ou caminhos personalizados. Para reiniciar o experimento, você pode desconectar o Caminho do Experimento existente e iniciar um novo, ou duplicar o Canvas e iniciar um novo Canvas. Caso contrário, os usuários percorrerão o caminho do experimento como se nenhum método de otimização tivesse sido selecionado. Também não é possível ativar Caminhos personalizados ou Caminhos vencedores para um Canvas já ativo com uma etapa de Caminho de experimento.<br><br>Para obter mais informações, consulte [Edição de telas após o lançamento]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

## Rastreamento de desempenho

Na página **do Canvas Analytics**, selecione o Caminho do experimento para abrir uma [tabela detalhada]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) idêntica à guia **Analisar variantes** para comparar o desempenho detalhado e as estatísticas de conversão entre os caminhos. Também é possível exportar a tabela via CSV e comparar as alterações percentuais das métricas de interesse em relação ao caminho ou controle selecionado.

Cada etapa em cada caminho exibirá estatísticas na visualização [do Canvas Analytics]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), assim como qualquer etapa do Canvas. No entanto, lembre-se de que as análises de etapas individuais **não** levam em conta a estrutura do experimento. A análise na etapa de experimento deve ser usada para comparar os caminhos.

### Desempenho do Winning Path e do Personalized Paths

Aproveite os Caminhos Vencedores para acompanhar o desempenho durante um período de tempo e, em seguida, envie automaticamente os usuários subsequentes para o caminho com o melhor desempenho. Para obter mais informações sobre análises quando **o Winning Path** ou **os Personalized Paths** estão ativados para seu experimento, consulte:

- [Caminho da vitória]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path/#analytics)
- [Caminhos personalizados]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths/#analytics)

### Configurações adicionais

Os caminhos de experiência registrarão os usuários que entrarem em cada etapa e converterem enquanto estiverem no caminho atribuído. Isso rastreará todos os eventos de conversão especificados na configuração do Canvas. Na guia **Additional Settings (Configurações adicionais** ), insira quantos dias (entre 1 e 30) você gostaria que esse experimento rastreasse as conversões. A janela de tempo que você especificar aqui determinará por quanto tempo os eventos de conversão (escolhidos na configuração do Canvas) serão rastreados para o experimento. As janelas de conversão por evento especificadas na configuração do Canvas não se aplicarão ao rastreamento dessa etapa e serão substituídas por essa janela de conversão.

