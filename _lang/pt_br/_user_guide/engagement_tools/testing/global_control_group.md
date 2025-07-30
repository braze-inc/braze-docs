---
nav_title: Grupo de controle global
article_title: Grupo de controle global
alias: /global_control_group/
page_order: 0

description: "Este artigo aborda como configurar e usar corretamente o Grupo de Controle Global. Ele também aborda como visualizar relatórios e métricas resultantes do uso desses grupos."
page_type: reference
tool: Reports
search_rank: 1

---

# Grupo de controle global

> Use o Grupo de controle global para especificar uma porcentagem de todos os usuários que não devem receber nenhuma campanha ou Canvas, o que permite analisar o impacto geral dos seus esforços de envio de mensagens ao longo do tempo. 

Ao comparar os comportamentos dos usuários que recebem envios de mensagens com os que não recebem, é possível entender melhor como suas campanhas de marketing e Canvas resultam em um aumento de sessões e eventos personalizados.

## Como funciona o Grupo de Controle Global

Com o Grupo de controle global, é possível definir uma porcentagem de todos os usuários como um grupo de controle. Quando salvos, os usuários do grupo não receberão nenhuma campanha ou Canvas. 

{% alert important %}
Seu Grupo de controle global se aplica a todos os canais, campanhas e Canvas, exceto para [campanhas de API]({{site.baseurl}}/api/api_campaigns). Isso significa que os usuários do seu grupo de controle ainda receberão campanhas de API. No entanto, essa exceção não se aplica aos cartões de conteúdo. Se estiver usando uma campanha de cartão de conteúdo disparada por API, os usuários do seu grupo de controle não os receberão.
{% endalert %}

### Atribuir usuários aleatoriamente ao Grupo de Controle Global

O Braze seleciona aleatoriamente vários intervalos de [números de buckets aleatórios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/ab_testing_with_random_buckets/#step-1-segment-your-users-by-the-random-bucket-attribute) e inclui usuários desses buckets selecionados. Se estiver usando números de balde aleatórios para qualquer outra finalidade, consulte [Coisas a serem observadas](#things-to-watch-for). 

Quando o seu grupo de controle global for gerado, todos os usuários com números aleatórios farão parte do grupo. Além disso, os novos usuários que ingressarem após esse ponto (aqueles adquiridos depois que o Grupo de Controle Global foi gerado) que tiverem esses números aleatórios de bucket também serão adicionados ao Grupo de Controle Global. Da mesma forma, se muitos usuários forem excluídos, é de se esperar que o tamanho do seu Grupo de Controle Global diminua, pois uma porcentagem desses usuários excluídos terá sido incluída nesse grupo. Isso mantém o tamanho do seu grupo como uma porcentagem constante em relação a toda a sua base de usuários.

### Atribuir usuários aleatoriamente ao grupo de tratamento para relatórios

Para capacitá-lo a relatar a elevação, o Braze também cria um grupo de tratamento. O grupo de tratamento é um grupo de usuários selecionado aleatoriamente que não faz parte do seu grupo de controle global e é gerado usando o mesmo método de números aleatórios que o grupo de controle global. 

O seu grupo de tratamento terá tamanho semelhante ao do seu grupo de controle global, mas é improvável que tenha exatamente o mesmo tamanho. Para [relatórios](#reporting), o Braze mede os comportamentos dos usuários do seu grupo de controle e dos usuários da amostra do grupo de tratamento. Cada espaço de trabalho tem no máximo um grupo de controle global e um grupo de amostra do grupo de tratamento. O grupo de amostra do grupo de tratamento é o mesmo grupo de usuários, independentemente da configuração do relatório do Controle Global.

### Excluir usuários de feature flags

Não é possível ativar [sinalizadores de recursos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/) para usuários do seu grupo de controle global. Isso significa que os usuários do seu Grupo de Controle Global também não podem fazer parte de experimentos de sinalização de recursos.

## Criar um grupo de controle global

### Etapa 1: Navegue até as Configurações do grupo de controle global

No dashboard, acesse **Público** > **Grupo de controle global**.

### Etapa 2: Atribuir uma porcentagem de todos os usuários a esse grupo de controle

Insira uma porcentagem para o seu grupo de controle e selecione **Save (Salvar**). Quando inserido, o Braze mostra uma estimativa de quantos usuários se enquadrarão no seu Controle Global, tratamento e amostra de tratamento. Lembre-se de que quanto mais usuários houver em seu espaço de trabalho, mais precisa será essa estimativa. 

O número de usuários no seu Grupo de Controle Global é atualizado automaticamente após a configuração inicial para permanecer proporcional a essa porcentagem quando mais usuários são adicionados ao seu espaço de trabalho. Além disso, os usuários que se associarem depois que o Grupo de Controle Global for configurado e que tiverem números de bucket aleatórios também serão adicionados ao Grupo de Controle Global. Se muitos usuários forem adicionados, o tamanho do seu Grupo de Controle Global crescerá para manter uma porcentagem constante em relação a toda a sua base de usuários. Quando o tamanho do seu Grupo de Controle Global aumentar, os usuários que estavam anteriormente no grupo ainda permanecerão no grupo (a menos que você faça alterações no grupo desativando-o e criando um novo).

Para obter diretrizes de porcentagem, consulte [Práticas recomendadas de teste](#percentage-guidelines).

![As Configurações do Grupo de Controle Global com as Configurações de Público definidas como "Atribuir cinco por cento de todos os usuários ao Grupo de Controle Global".]({% image_buster /assets/img/control_group/control_group4.png %})

### Etapa 3: Atribuir configurações de exclusão

Use tags para adicionar configurações de exclusão ao seu Grupo de Controle Global. Todas as campanhas ou Canvas que usarem as tags incluídas nas configurações de exclusão não usarão seu Grupo de controle global. Essas campanhas e Canvas continuam a ser enviadas a todos os usuários do público-alvo, incluindo os do seu Grupo de Controle Global.

{% alert tip %}
Você pode querer adicionar configurações de exclusão se tiver mensagens transacionais que devem ser enviadas a todos os usuários.
{% endalert %}

![A seção para adicionar ou editar configurações de exclusão para o seu Grupo de Controle Global.]({% image_buster /assets/img/control_group/control_group5.png %})

### Etapa 4: Salve seu grupo de controle

Nesse ponto, o Braze gera um grupo de usuários selecionados aleatoriamente para compor a porcentagem selecionada da sua base total de usuários. Quando salvas, todas as campanhas e Canvas ativas e futuras não serão mais enviadas aos usuários desse grupo, exceto para campanhas ou Canvas que contenham qualquer uma das tags em suas configurações de exclusão.

## Como fazer alterações no seu Grupo de Controle Global

Só é possível fazer alterações no seu Grupo de Controle Global desativando-o e criando um novo. Por exemplo, se você configurar um Grupo de controle global com 10% do seu público e quiser diminuir o tamanho para 5%, deverá desativar o Grupo de controle global atual e ativar novamente um novo Grupo de controle global. 

É possível desativar o grupo de controle global a qualquer momento na guia **Configurações do grupo de controle global**, mas lembre-se de que isso fará com que os usuários desse grupo se tornem imediatamente elegíveis para campanhas e telas.

Antes de desativar o grupo de controle, recomendamos [exportar](#export-group-members) um CSV dos usuários desse grupo, caso seja necessário fazer referência a ele posteriormente. Ao desativar um grupo de controle, não há como o Braze restaurar o grupo ou identificar quais usuários estavam nesse grupo.

Depois de desativar o grupo de controle, é possível salvar um novo. Quando você insere uma porcentagem e a salva, a Braze gera um novo grupo de usuários selecionados aleatoriamente. Se você inserir a mesma porcentagem de antes, o Braze ainda gerará um novo grupo de usuários para os grupos de controle e de tratamento.

![Uma caixa de diálogo intitulada "Você está fazendo alterações nas configurações de mensagens globais" com um texto avisando que, depois que o seu grupo de controle global for desativado, ele não será mais excluído de nenhuma campanha ou tela nova ou ativa.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Exportar os membros do grupo de controle {#export-group-members}

Se quiser ver quais usuários estão no seu grupo de controle global, é possível exportar os membros do grupo por CSV ou API. 

Para executar uma exportação CSV, navegue até a guia **Configurações do grupo de controle global** e clique em <i class="fas fa-download"></i> **Export**. Para exportar por API, use o [ponto de extremidade`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).

{% alert important %}
Os grupos de controle históricos não são preservados, portanto, só é possível exportar os membros do grupo atual. Certifique-se de exportar todas as informações necessárias antes de desativar um grupo de controle.
{% endalert %}

## Ver se um usuário está em um Grupo de Controle Global

É possível visualizar a associação ao Grupo de Controle Global acessando a seção **Diversos** na guia **Engajamento** do perfil de um usuário individual.

![Uma seção "Miscelânea" informando que o usuário tem um número de balde aleatório de 6356 e não está no Grupo de Controle Global.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Relatórios

Consulte [Relatórios do grupo de controle global]({{site.baseurl}}/user_guide/analytics/reporting/global_control_group_reporting/) para obter informações sobre métricas de relatórios.

## Solução de problemas

Ao configurar os grupos de controle globais e visualizar os relatórios, veja os erros que podem ocorrer:

| Problema | Solução de problemas |
| --- | --- |
| Não é possível salvar a porcentagem inserida ao designar um Grupo de Controle Global. | Esse problema ocorre se você inserir um número não inteiro ou um número inteiro que não esteja entre 1 e 15 (inclusive). |
| Erro "Braze não consegue atualizar seu Grupo de Controle Global" na página de configurações do Controle Global. | Isso geralmente indica que algum componente dessa página foi alterado, provavelmente devido a ações tomadas por outro usuário em sua conta Braze. Nesse caso, atualize a página e tente novamente. |
| O relatório do Grupo de Controle Global não tem dados. | Se acessar o Relatório do grupo de controle global sem ter salvo um grupo de controle global, você não verá nenhum dado no relatório. Crie e salve um Grupo de Controle Global e tente novamente. |
| Minha taxa de conversão é 0% ou não estou vendo a exibição do gráfico, mesmo que haja mais de zero eventos ocorrendo. | Se o número de conversões for muito pequeno e os grupos de controle ou de tratamento forem muito grandes, a taxa de conversão poderá ser arredondada para 0% e, portanto, não aparecerá no gráfico. Você pode verificar isso conferindo a métrica Número total de eventos. Você pode comparar a eficácia de seus dois grupos usando a métrica de porcentagem de aumento incremental.  |
| Minha taxa de conversão (ou outras métricas) está mudando drasticamente, dependendo do período para o qual estou visualizando os dados. | Se estiver visualizando dados em períodos curtos, é possível que suas métricas flutuem dia a dia ou semana a semana. Recomendamos que você visualize as métricas ao longo de pelo menos um mês. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Coisas a serem observadas {#things-to-watch-for}

#### Números de baldes aleatórios sobrepostos

Seu grupo de controle global é formado usando números aleatórios de bucket e, portanto, se estiver executando outros testes usando filtros de segmento de números aleatórios de bucket, lembre-se de que pode haver uma sobreposição entre os segmentos criados e os usuários do grupo de controle global.

#### Endereços de e-mail duplicados

Se dois usuários com IDs de usuário externo diferentes tiverem o mesmo endereço de e-mail, e um deles estiver no grupo de controle e o outro não, um e-mail ainda será enviado a esse endereço de e-mail sempre que o usuário do grupo sem controle for elegível para receber um e-mail. Quando isso ocorrer, marcaremos ambos os perfis de usuário como tendo recebido a campanha ou o Canva contendo esse e-mail.

#### Grupo de controle global e grupos de controle específicos de mensagens

É possível ter um grupo de controle global e também usar um grupo de controle específico da campanha ou específico do Canva. Ter um grupo de controle específico para a campanha ou para o Canva permite medir o impacto de uma determinada mensagem.

Os usuários do seu Grupo de Controle Global são impedidos de receber quaisquer mensagens que não sejam aquelas com exceções de tag e, se você adicionar um controle a uma campanha ou Canvas, o Braze impedirá que uma parte do seu grupo de tratamento global receba essa campanha ou Canvas específico. Isso significa que, se um membro do Grupo de Controle Global não for elegível para receber uma determinada campanha ou canva, ele também não estará presente no grupo de controle dessa campanha ou canva específico.

> Em resumo, os usuários do grupo de controle global são filtrados para fora da campanha ou do público do Canva antes da entrada. Dos usuários que entram na campanha ou no Canva, uma porcentagem deles é atribuída à variante de controle.

#### Segmentos do grupo de controle global no console do desenvolvedor

É possível ver vários segmentos **de Controle global** na seção **Identificadores adicionais de API** da página [Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Isso ocorre porque cada vez que o Grupo de Controle Global é ativado ou desativado, um novo Grupo de Controle Global é formado. Isso leva a vários segmentos rotulados como "Grupo de controle global".

Apenas um desses segmentos está ativo e pode ser consultado usando o [ponto de extremidade`/users/export/global_control_group` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) ou exportado do dashboard. A exportação do dashboard indica especificamente quais subsegmentos compõem esse Grupo de Controle Global.

## Práticas recomendadas de teste

### Tamanho ideal do grupo de controle {#percentage-guidelines}

Duas regras principais que devem ser levadas em conta são\*\*:
1. Seu grupo de controle não deve ser menor do que 1.000 usuários.
2. Seu grupo de controle não deve ser mais do que 10% de todo o seu público.

Se o seu público total for menor que 10.000, aumente a porcentagem para criar um grupo de mais de 1.000 usuários; nesse caso, não aumente a porcentagem para mais de 15%. Lembre-se de que quanto menor for o tamanho geral do espaço de trabalho, mais desafiador será realizar um teste estatisticamente rigoroso.

- Algumas compensações a serem consideradas ao pensar no tamanho do grupo de controle são que é necessário um número significativamente grande de clientes no grupo de controle para que qualquer análise de comportamento criada seja confiável. No entanto, quanto maior for o grupo de controle, menos clientes receberão suas campanhas, o que é uma desvantagem se você estiver usando suas campanhas para impulsionar o engajamento e as conversões.
- A porcentagem ideal de seu público total dependerá do tamanho de seu público total. Quanto maior for o seu público total, menor poderá ser a sua porcentagem. No entanto, se o seu público for pequeno, precisará de uma porcentagem maior para o grupo de controle.

### Duração do experimento 

#### Escolha uma duração ideal {#reshuffle}

O tempo de execução do experimento antes de reorganizar os membros do grupo de controle depende do que está sendo testado e dos comportamentos de base dos usuários. Se não tiver certeza, um bom ponto de partida é um trimestre (três meses), mas não deve ser inferior a um mês.

Para determinar o intervalo de tempo adequado para o seu experimento, considere as perguntas que espera responder. Por exemplo, você está tentando descobrir se há uma diferença nas sessões? Se for o caso, pense na frequência com que seus usuários fazem sessões organicamente. As marcas cujos usuários têm sessões todos os dias podem executar experimentos mais curtos do que as marcas cujos usuários têm sessões apenas algumas vezes por mês. 

Ou, talvez esteja interessado em um evento personalizado, portanto, seu experimento pode precisar ser executado por mais tempo do que um experimento em que você está examinando sessões, se for provável que seus usuários disparem esse evento personalizado com menos frequência.

{% alert tip %}
Quanto mais tempo você mantiver o mesmo grupo de controle, mais ele divergirá do grupo de tratamento, o que pode criar um viés. A redefinição do Grupo de Controle Global reequilibra a população.
{% endalert %}

#### Tente limitar o término prematuro dos experimentos

Você deve decidir por quanto tempo executar seu experimento antes de iniciá-lo e, em seguida, só deve encerrar o experimento e coletar os resultados finais depois de atingir esse ponto predeterminado. Terminar seu experimento antes do tempo, ou sempre que vir dados promissores, introduzirá uma tendência.

#### Pense em métricas valiosas

Considere quaisquer comportamentos de linha de base para as métricas nas quais você está mais interessado. Você quer apenas as taxas de compra para planos de inscrição que são renovados apenas anualmente? Ou os clientes têm um hábito semanal para o evento que você gostaria de medir? Pense em quanto tempo os usuários levam para alterar potencialmente seus comportamentos devido ao envio de mensagens. Depois de decidir quanto tempo o experimento deve durar, certifique-se de não encerrar o experimento nem registrar os resultados finais antes do tempo, ou suas descobertas poderão ser tendenciosas.

