---
nav_title: Grupo de Controle Global
article_title: Grupo de Controle Global
alias: /global_control_group/
page_order: 0

description: "Este artigo aborda como configurar e usar adequadamente o Grupo de Controle Global. Ele também aborda como visualizar relatórios e métricas resultantes do uso desses grupos."
page_type: reference
tool: Reports
search_rank: 1

---

# Grupo de Controle Global

> Use o Grupo de controle global para especificar uma porcentagem de todos os usuários que não devem receber nenhuma campanha ou Canvases, o que permite analisar o impacto geral de seus esforços de envio de mensagens ao longo do tempo. 

Ao comparar os comportamentos dos usuários que recebem mensagens com os que não recebem, é possível entender melhor como suas campanhas de marketing e Canvases resultam em um aumento de sessões e eventos personalizados.

## Como funciona o Grupo de Controle Global

Com o Grupo de controle global, é possível definir uma porcentagem de todos os usuários como um grupo de controle. Quando salvos, os usuários do grupo não receberão nenhuma campanha ou Canvases. 

{% alert important %}
Seu Grupo de controle global se aplica a todos os canais, campanhas e Canvases, exceto para [campanhas de API]({{site.baseurl}}/api/api_campaigns). Isso significa que os usuários do seu grupo de controle ainda receberão campanhas de API. No entanto, essa exceção não se aplica aos cartões de conteúdo. Se você estiver usando uma campanha de Content Card acionada por API, os usuários do seu grupo de controle não os receberão.
{% endalert %}

### Atribuir usuários aleatoriamente ao Grupo de Controle Global

O Braze seleciona aleatoriamente vários intervalos de [números de buckets aleatórios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) e inclui usuários desses buckets selecionados. Se estiver usando números de balde aleatórios para qualquer outra finalidade, consulte [Coisas a serem observadas](#things-to-watch-for). 

Quando o seu Grupo de Controle Global for gerado, todos os usuários com números aleatórios de bucket farão parte do grupo. Além disso, os novos usuários que se associarem após esse ponto (aqueles adquiridos após a geração do Grupo de Controle Global) que tiverem esses números aleatórios de bucket também serão adicionados ao Grupo de Controle Global. Da mesma forma, se muitos usuários forem excluídos, é de se esperar que o tamanho do seu Grupo de controle global diminua, pois uma porcentagem desses usuários excluídos terá sido incluída nesse grupo. Isso mantém o tamanho do seu grupo como uma porcentagem constante em relação a toda a sua base de usuários.

### Atribuir usuários aleatoriamente ao grupo de tratamento para relatórios

Para capacitá-lo a relatar o aumento, o Braze também cria um grupo de tratamento. O grupo de tratamento é um grupo de usuários selecionado aleatoriamente que não faz parte do seu Grupo de Controle Global e é gerado usando o mesmo método de números aleatórios que o Grupo de Controle Global. 

O seu grupo de tratamento será semelhante em tamanho ao seu Grupo de Controle Global, mas é improvável que seja exatamente do mesmo tamanho. Para [relatórios](#reporting), o Braze mede os comportamentos dos usuários do seu grupo de controle e dos usuários da sua amostra de tratamento. Cada espaço de trabalho tem no máximo um Grupo de Controle Global e um grupo de amostra de tratamento. O grupo de amostra de tratamento é o mesmo grupo de usuários, independentemente da configuração do relatório do Controle Global.

### Excluir usuários dos sinalizadores de recursos

Não é possível ativar [sinalizadores de recursos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) para usuários no seu Grupo de Controle Global. Isso significa que os usuários do seu Grupo de Controle Global também não podem fazer parte de experimentos com sinalizadores de recursos.

### Excluir usuários do Grupo de Controle Global

Não é possível remover usuários específicos do Grupo de controle global, mas é possível adicionar [configurações de exclusão]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings) para que campanhas e Canvases com tags especificadas **não** usem o Grupo de controle global. Também é possível desativar e reativar o Grupo de Controle Global para alterar a associação. A duração ideal para embaralhar os usuários varia de acordo com o tipo de teste que você está executando, mas recomendamos que você embaralhe no máximo uma vez por mês.

## Criar um Grupo de Controle Global

### Etapa 1: Navegue até as Configurações do grupo de controle global

No painel, vá para **Audience** > **Global Control Group**.

### Etapa 2: Atribua uma porcentagem de todos os usuários a esse grupo de controle

Insira uma porcentagem para o seu grupo de controle e selecione **Save (Salvar**). Quando inserido, o Braze mostra uma estimativa de quantos usuários se enquadrarão no seu Controle Global, tratamento e amostra de tratamento. Lembre-se de que quanto mais usuários houver no seu espaço de trabalho, mais precisa será essa estimativa. 

O número de usuários no seu Grupo de Controle Global é atualizado automaticamente após a configuração inicial para permanecer proporcional a essa porcentagem quando mais usuários são adicionados ao seu espaço de trabalho. Além disso, os usuários que se associarem depois que o Grupo de Controle Global for configurado e que tiverem números de bucket aleatórios também serão adicionados ao Grupo de Controle Global. Se muitos usuários forem adicionados, o tamanho do seu Grupo de Controle Global aumentará para manter uma porcentagem constante em relação a toda a sua base de usuários. Quando o tamanho do seu Grupo de Controle Global aumentar, os usuários que estavam anteriormente no grupo ainda permanecerão no grupo (a menos que você faça alterações no grupo desativando-o e criando um novo).

Para obter diretrizes de porcentagem, consulte [Práticas recomendadas de teste](#percentage-guidelines).

As Configurações do Grupo de Controle Global com as Configurações de Público definidas como "Atribuir cinco por cento de todos os usuários ao Grupo de Controle Global".]({% image_buster /assets/img/control_group/control_group4.png %})

### Etapa 3: Atribuir configurações de exclusão

Use tags para adicionar configurações de exclusão ao seu Grupo de Controle Global. Todas as campanhas ou Canvases que usarem as tags incluídas nas configurações de exclusão não usarão seu Grupo de Controle Global. Essas campanhas e Canvases continuam a ser enviadas para todos os usuários do público-alvo, inclusive os do seu Grupo de Controle Global.

{% alert tip %}
Talvez você queira adicionar configurações de exclusão se tiver mensagens transacionais que devam ser enviadas a todos os usuários.
{% endalert %}

A seção para adicionar ou editar configurações de exclusão para o seu Grupo de Controle Global.]({% image_buster /assets/img/control_group/control_group5.png %})

### Etapa 4: Salve seu grupo de controle

Nesse momento, o Braze gera um grupo de usuários selecionados aleatoriamente para compor a porcentagem selecionada da sua base total de usuários. Quando salvos, todas as campanhas e Canvases ativos e futuros não serão mais enviados aos usuários desse grupo, exceto para campanhas ou Canvases que contenham qualquer uma das tags em suas configurações de exclusão.

## Como fazer alterações no Grupo de Controle Global

Só é possível fazer alterações no Grupo de Controle Global desativando-o e criando um novo. Por exemplo, se você configurar um Grupo de Controle Global que represente 10% do seu público e quiser diminuir esse tamanho para 5%, deverá desativar o Grupo de Controle Global atual e reativar um novo Grupo de Controle Global. 

Você pode desativar seu Grupo de Controle Global a qualquer momento na guia **Configurações do Grupo de Controle Global**, mas lembre-se de que isso fará com que os usuários desse grupo se tornem imediatamente qualificados para campanhas e Canvases.

Antes de desativar o grupo de controle, recomendamos [exportar](#export-group-members) um CSV dos usuários desse grupo, caso seja necessário fazer referência a ele posteriormente. Quando você desativa um grupo de controle, não há como o Braze restaurar o grupo ou identificar quais usuários estavam nesse grupo.

Depois de desativar o Grupo de Controle, você pode salvar um novo. Quando você insere uma porcentagem e a salva, o Braze gera um novo grupo de usuários selecionados aleatoriamente. Se você inserir a mesma porcentagem de antes, o Braze ainda gerará um novo grupo de usuários para os grupos de controle e tratamento.

\![Uma caixa de diálogo intitulada "Você está fazendo alterações nas Configurações de Mensagens Globais" com um texto avisando que, quando o Grupo de Controle Global for desativado, ele não será mais excluído de nenhuma campanha ou Canvases nova ou ativa.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Exportar os membros do grupo de controle {#export-group-members}

Se quiser ver quais usuários estão no seu Grupo de Controle Global, você pode exportar os membros do seu grupo por CSV ou API. 

Para executar uma exportação CSV, navegue até a guia **Configurações do Grupo de Controle Global** e clique em <i class="fas fa-download"></i> **Export**. Para exportar por API, use o [ponto de extremidade`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

{% alert important %}
Os grupos de controle históricos não são preservados, portanto, só é possível exportar os membros do grupo atual. Certifique-se de exportar todas as informações necessárias antes de desativar um grupo de controle.
{% endalert %}

## Ver se um usuário está em um Grupo de Controle Global

É possível visualizar a associação ao Grupo de Controle Global acessando a seção **Diversos** na guia **Envolvimento** do perfil de um usuário individual.

\![Uma seção "Diversos" informando que o usuário tem um número de bucket aleatório de 6356 e não está no Grupo de Controle Global.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Relatórios

Consulte [Relatórios do Grupo de Controle Global]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/) para obter informações sobre métricas de relatórios.

## Solução de problemas

Ao configurar os grupos de controle global e visualizar os relatórios, veja os erros que podem ocorrer:

| Problema | Solução de problemas |
| --- | --- |
| Não é possível salvar a porcentagem inserida ao designar um Grupo de Controle Global. | Esse problema ocorre se você inserir um número não inteiro ou um número inteiro que não esteja entre 1 e 15 (inclusive). |
| Erro "Braze is not able to update your Global Control Group" na página de configurações do Global Control. | Isso geralmente indica que algum componente dessa página foi alterado, provavelmente devido a ações tomadas por outro usuário em sua conta Braze. Nesse caso, atualize a página e tente novamente. |
| O relatório do Global Control Group não possui dados. | Se você acessar o Relatório do Grupo de Controle Global sem ter salvo um Grupo de Controle Global, não verá nenhum dado no relatório. Crie e salve um Grupo de Controle Global e tente novamente. |
| Minha taxa de conversão é 0% ou não estou vendo a exibição do gráfico, mesmo que haja mais de zero eventos ocorrendo. | Se o número de conversões for muito pequeno e seus grupos de controle ou de tratamento forem muito grandes, a taxa de conversão poderá ser arredondada para 0% e, portanto, não aparecerá no gráfico. Você pode verificar isso conferindo a métrica Número total de eventos. Você pode comparar a eficácia de seus dois grupos usando a métrica de porcentagem de aumento incremental.  |
| Minha taxa de conversão (ou outras métricas) está mudando drasticamente, dependendo do período de tempo para o qual estou visualizando os dados. | Se estiver visualizando dados em períodos curtos, é possível que suas métricas flutuem dia a dia ou semana a semana. Recomendamos que você visualize as métricas ao longo de pelo menos um mês. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Coisas a serem observadas {#things-to-watch-for}

#### Números de baldes aleatórios sobrepostos

Seu Global Control Group é formado usando Random Bucket Numbers e, portanto, se você estiver executando outros testes usando filtros de segmento Random Bucket Numbers, lembre-se de que pode haver uma sobreposição entre os segmentos criados e os usuários do Global Control Group.

#### Endereços de e-mail duplicados

Se dois usuários com IDs de usuário externo diferentes tiverem o mesmo endereço de e-mail, e um deles estiver no grupo de controle e o outro não, um e-mail ainda será enviado a esse endereço de e-mail sempre que o usuário do grupo sem controle estiver qualificado para receber um e-mail. Quando isso ocorrer, marcaremos ambos os perfis de usuário como tendo recebido a campanha ou o Canvas contendo esse e-mail.

#### Grupo de controle global e grupos de controle específicos de mensagens

É possível ter um Grupo de controle global e também usar um grupo de controle específico da campanha ou do Canvas. Ter um grupo de controle específico para a campanha ou para o Canvas permite medir o impacto de uma determinada mensagem.

Os usuários do seu Grupo de Controle Global são impedidos de receber quaisquer mensagens que não sejam aquelas com exceções de tag e, se você adicionar um controle a uma campanha ou tela, o Braze impedirá que uma parte do seu grupo de tratamento global receba essa campanha ou tela específica. Isso significa que, se um membro do Grupo de Controle Global não estiver qualificado para receber uma determinada campanha ou Canvas, ele também não estará presente no grupo de controle dessa campanha ou Canvas específico.

> Em resumo, os usuários do Grupo de Controle Global são filtrados para fora da campanha ou do público-alvo do Canvas antes da entrada. Dos usuários que entram na campanha ou no Canvas, uma porcentagem deles é atribuída à variante de controle.

#### Segmentos do Grupo de Controle Global no Console do Desenvolvedor

Você pode ver vários segmentos **de controle global** na seção **Additional API Identifiers (Identificadores adicionais de API** ) da página [API Keys (Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/) ). Isso ocorre porque toda vez que o Grupo de Controle Global é ativado ou desativado, um novo Grupo de Controle Global é formado. Isso leva a vários segmentos rotulados como "Grupo de controle global".

Apenas um desses segmentos está ativo e pode ser consultado usando o [ponto de extremidade`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) ou exportado do painel. A exportação do painel indica especificamente quais subsegmentos compõem esse Grupo de Controle Global.

## Práticas recomendadas de teste

### Tamanho ideal do grupo de controle {#percentage-guidelines}

Duas regras principais que devem ser levadas em conta são\*\*:
1. Seu grupo de controle não deve ser menor do que 1.000 usuários.
2. Seu grupo de controle não deve ser mais do que 10% de todo o seu público.

Se você tiver um público total menor que 10.000, deverá aumentar a porcentagem para criar um grupo de mais de 1.000 usuários; nesse caso, não deverá aumentar a porcentagem para mais de 15%. Lembre-se de que quanto menor for o tamanho total do seu espaço de trabalho, mais difícil será realizar um teste estatisticamente rigoroso.

- Algumas compensações a serem consideradas ao pensar no tamanho do grupo de controle são que é necessário um número significativamente grande de clientes no grupo de controle para que qualquer análise de comportamento criada seja confiável. No entanto, quanto maior for o seu grupo de controle, menos clientes receberão suas campanhas, o que é uma desvantagem se você estiver usando suas campanhas para impulsionar o engajamento e as conversões.
- A porcentagem ideal do seu público total dependerá do tamanho do seu público total. Quanto maior for o seu público total, menor poderá ser a sua porcentagem. No entanto, se o seu público for pequeno, você precisará de uma porcentagem maior para o grupo de controle.

### Duração do experimento 

#### Escolha uma duração ideal {#reshuffle}

O tempo de execução do experimento antes de reorganizar os membros do grupo de controle depende do que está sendo testado e dos comportamentos de base dos usuários. Se você não tiver certeza, um bom ponto de partida é um trimestre (três meses), mas não deve ser inferior a um mês.

Para determinar o período de tempo adequado para o seu experimento, considere as perguntas que espera responder. Por exemplo, você está procurando ver se há uma diferença nas sessões? Se for o caso, pense na frequência com que seus usuários fazem sessões organicamente. As marcas cujos usuários têm sessões todos os dias podem executar experimentos mais curtos do que as marcas cujos usuários têm sessões apenas algumas vezes por mês. 

Ou você pode estar interessado em um evento personalizado, portanto, seu experimento pode precisar ser executado por mais tempo do que um experimento em que você está examinando sessões, se for provável que seus usuários acionem esse evento personalizado com menos frequência.

{% alert tip %}
Quanto mais tempo você mantiver o mesmo grupo de controle, mais ele divergirá do grupo de tratamento, o que pode criar um viés. A redefinição do Grupo de Controle Global reequilibra a população.
{% endalert %}

#### Tente limitar o término prematuro dos experimentos

Você deve decidir por quanto tempo executar o experimento antes de iniciá-lo e, em seguida, só deve encerrar o experimento e coletar os resultados finais depois de atingir esse ponto predeterminado. Terminar o experimento antes do tempo, ou sempre que vir dados promissores, introduzirá uma tendência.

#### Pense em métricas valiosas

Considere quaisquer comportamentos de linha de base para as métricas nas quais você está mais interessado. Você tem interesse em taxas de compra para planos de assinatura que são renovados apenas anualmente? Ou os clientes têm um hábito semanal para o evento que você gostaria de medir? Pense em quanto tempo os usuários levam para alterar potencialmente seus comportamentos devido às suas mensagens. Depois de decidir quanto tempo o experimento deve durar, certifique-se de não encerrar o experimento nem registrar os resultados finais antes do tempo, ou suas descobertas poderão ser tendenciosas.

