---
nav_title: Jornadas do experimento 
article_title: Jornadas do experimento 
alias: /experiment_step/
page_order: 4
page_type: reference
description: "Este artigo aborda os Caminhos de Experimento, um componente que permite testar vários caminhos de canva entre si e um grupo de controle em qualquer ponto da jornada do usuário."
tool: Canvas
---

# Jornadas do experimento

> Os Caminhos de Experimento permitem testar vários caminhos de canva entre si e um grupo de controle em qualquer ponto da jornada do usuário. Usando este componente, você pode acompanhar a performance da jornada para tomar decisões informadas sobre seu canva.

Quando você inclui uma etapa da jornada experimental na sua jornada do usuário, ela atribuirá aleatoriamente os usuários a diferentes caminhos (ou a um grupo de controle opcional) que você criar. Porções do público serão atribuídas a diferentes caminhos de acordo com as porcentagens que você selecionar, permitindo que você teste diferentes mensagens ou caminhos entre si e determine qual é o mais efetivo. 

![Uma etapa da jornada experimental que se divide em Caminho 1, Caminho 2 e Controle.]({% image_buster /assets/img/experiment_step/experiment_step.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

## Casos de uso

As jornadas experimentais são mais adequadas para testar a entrega, cadência, cópia de mensagem e combinações de canal.

- **Entrega:** Compare os resultados entre mensagens enviadas com diferentes [atrasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/), com base nas ações do usuário ([jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)), e usando [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#canvas).<br><br>
- **Cadência:** Teste vários fluxos de envio de mensagens durante um período específico. Por exemplo, você poderia testar duas cadências diferentes de integração:
    - Cadência 1: Envie 2 mensagens nas primeiras 2 semanas do usuário
    - Cadência 2: Envie 3 mensagens nas primeiras 2 semanas do usuário
    
    Ao {direcionamento} de usuários em lapsos, você pode testar a eficácia de enviar duas mensagens de {recuperar} em uma semana em comparação com enviar apenas uma.
- **Mensagem copiada:** Semelhante a um [teste A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/), você pode testar diferentes cópias de mensagens para ver qual redação resulta em uma taxa de conversão mais alta.<br><br>
- **Combinações de canal:** Teste a eficácia de diferentes combinações de canal de mensagem. Por exemplo, você pode comparar o impacto de usar apenas um e-mail versus um e-mail combinado com um push.

## Pré-requisito

Para usar os Caminhos de Experimento, seu canva deve incluir eventos de conversão. Embora você não possa adicionar eventos de conversão após um Canvas ter sido lançado, você pode clonar o Canvas lançado e adicionar eventos de conversão para adicionar Caminhos de Experimento.

## Criação de uma jornada experimental

Para criar um componente de jornada experimental, primeiro adicione uma etapa ao seu canva. Arraste e solte o componente da barra lateral ou clique no <i class="fas fa-plus-circle"></i> botão de mais na parte inferior de uma etapa e selecione **Experiment Paths**. 

Na configuração padrão desse componente, existem duas jornadas padrão, **Jornada 1** e **Jornada 2**, com 50% do público sendo enviado por cada jornada. Clique no componente para expandir o painel **Configurações do Experimento**, e você verá as opções de configuração para o componente.

### Etapa 1: Escolha o número de caminhos e a distribuição do público

Você pode adicionar até quatro jornadas clicando em **Add Path** e um grupo de controle opcional marcando **Add a Control Group**. Usando as caixas de porcentagem para cada jornada, você pode especificar a porcentagem do público que deve acessar cada jornada e o grupo de controle. As porcentagens fornecidas devem somar 100% para prosseguir. Se você deseja definir rapidamente todos os caminhos disponíveis (e controle) para a mesma porcentagem, clique em **Distribuir Caminhos Uniformemente**.

Você também pode escolher se os usuários no grupo de controle devem continuar no canva ou sair após a janela de rastreamento de conversão para o **Comportamento do Grupo de Controle**. Opcionalmente, você pode adicionar uma descrição para explicar aos outros o que esta jornada experimental pretende testar ou incluir informações adicionais que possam ser úteis para nota.

![Configurações de jornada experimental onde é possível adicionar jornadas e distribuir a porcentagem de usuários em cada jornada.]({% image_buster /assets/img/experiment_step/exp_settings.png %})

{% alert note %}
Se a re-eligibilidade do canva estiver ativada, os usuários que entrarem no canva e seguirem uma jornada escolhida aleatoriamente seguirão a mesma jornada novamente se se tornarem elegíveis novamente e reentrarem no canva. Isso mantém a validade do experimento e da análise de dados associada. Se você deseja que a etapa sempre randomize a atribuição de jornada, selecione **Jornadas aleatórias em jornadas de experimento**. Esta opção não está disponível ao usar Caminhos Vencedores ou Personalizados.
{% endalert %}

### Etapa 2: Ative a Jornada de Sucesso ou Jornadas Personalizadas (opcional) {#step-2}

Você pode optar por otimizar seu experimento ativando [Jornada Vencedora]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path) ou [Jornadas Personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths). Ambas as opções funcionam testando inicialmente suas jornadas com uma parte do seu público. Após o experimento terminar, os usuários restantes e subsequentes são enviados pelo melhor caminho geral (Caminho Vencedor) ou pelo melhor caminho para cada usuário (Caminhos Personalizados).

### Etapa 3: Criar caminhos

Por fim, você deve montar suas jornadas dependentes. Selecione **Concluído** e retorne ao construtor de canva. Clique no <i class="fas fa-plus-circle"></i> botão de mais sob cada jornada para começar a criar jornadas usando as ferramentas usuais do canva como achar melhor, e lance o canva quando estiver pronto.

![Adição de etapas a cada caminho que se divide de um componente de Jornada Experimental.]({% image_buster /assets/img/experiment_step/experiment_downstream_paths.gif %}){: style="max-width:75%"}

Lembre-se de que os caminhos e seus passos subsequentes não podem ser removidos de uma canva depois de serem criados. No entanto, quando lançado, você pode modificar a distribuição do público entre as jornadas conforme achar adequado. Por exemplo, se um dia após lançar um canva, você concluir que uma jornada é superior às demais com base na análise de dados, você pode definir essa jornada para 100% e as outras para 0%. Ou, dependendo das suas necessidades, continue enviando os usuários por várias jornadas.

{% alert important %}
Para evitar a contaminação do experimento, se o seu Canvas tiver um experimento ativo ou em andamento e você atualizar o Canvas ativo (mesmo que não seja na etapa da jornada experimental), o experimento em andamento será encerrado. Para reiniciar o experimento, é possível desconectar a jornada experimental existente e iniciar uma nova, ou duplicar o Canvas e iniciar um novo Canvas. Você também não pode ativar Jornadas Personalizadas ou Jornadas Vencedoras para um canva já ativo com uma etapa de jornada experimental.<br><br>Para saber mais, consulte [Editar canvas após o lançamento]({{site.baseurl}}/post-launch_edits/).
{% endalert %}

## Rastreamento de performance

Na página de **análise de dados da canva**, clique na jornada experimental para abrir uma [tabela detalhada]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/measuring_and_testing_with_canvas_analytics/#performance-breakdown-by-variant) idêntica à guia **Analisar Variantes** para comparar estatísticas detalhadas de performance e conversão entre jornadas. Você também pode exportar a tabela via CSV e comparar as mudanças percentuais para métricas de interesse em relação à jornada ou controle que você selecionar.

Cada etapa em cada jornada exibirá estatísticas na visualização [análise de dados do canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), assim como qualquer etapa do canva. No entanto, tenha em mente que a análise de dados dos passos individuais **não** leva em conta a estrutura do experimento. A análise de dados na Etapa do Experimento deve ser usada para comparar entre jornadas.

### Desempenho da Jornada Vencedora e Jornadas Personalizadas

Aproveite as Jornadas Vencedoras para acompanhar a performance ao longo de um período de tempo e, em seguida, enviar automaticamente os usuários subsequentes pela jornada com a melhor performance. Para saber mais sobre análise de dados quando **Jornada Vencedora** ou **Jornadas Personalizadas** estão ativadas para o seu experimento, consulte:

- [Jornada vencedora]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/winning_path/#analytics)
- [Jornadas personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths/#analytics)

### Configurações adicionais

Os Caminhos de Experimento registrarão os usuários que entrarem em cada etapa e se converterem enquanto estiverem no caminho atribuído. Isso rastreará todos os eventos de conversão especificados na configuração da canva. Na guia **Configurações adicionais**, insira quantos dias (entre 1 e 30) você gostaria que este experimento rastreasse conversões. A janela de tempo que você especificar aqui determinará por quanto tempo os eventos de conversão (escolhidos na configuração do canva) serão rastreados para o experimento. As janelas de conversão por evento especificadas na configuração do canva não se aplicarão ao rastreamento desta etapa e serão substituídas por esta janela de conversão.

