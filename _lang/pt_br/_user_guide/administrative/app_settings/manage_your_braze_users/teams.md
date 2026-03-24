---
nav_title: Equipes
article_title: Equipes
page_order: 4
page_type: reference
alias: /teams/
description: "Este artigo de referência cobre como usar as Equipes da Braze no dashboard. Aqui, você pode aprender como criar Equipes, atribuir funções e atribuir tags e filtros."

---

# Equipes

> Como administrador da Braze, você pode agrupar os usuários da sua empresa em Equipes com diferentes funções e permissões de usuário. Isso permite que você tenha múltiplos grupos não relacionados de usuários da empresa trabalhando juntos em um espaço de trabalho, separando os tipos de conteúdo que podem ser editados.

As Equipes podem ser configuradas com base no local da base de clientes, idioma e atributos personalizados, para que os membros da Equipe e os não membros tenham acesso diferente a recursos de envio de mensagens e dados de clientes. Filtros e tags de Equipe podem ser atribuídos em várias ferramentas de engajamento. Não há limite para quantas equipes você pode criar no seu espaço de trabalho.

As Equipes não estão disponíveis em todos os contratos da Braze. Para acessar esse recurso, entre em contato com seu gerente de conta da Braze ou [fale com a gente](mailto:success@braze.com) para uma consulta.

## Como as Equipes diferem de conjuntos de permissões e funções?

{% multi_lang_include permissions.md content="Differences" %}

## Criar Equipes {#creating-teams}

Acesse **Configurações** > **Equipes internas** e selecione <i class="fas fa-plus"></i> **Adicionar equipe**.

![Janela para adicionar uma nova Equipe.]({% image_buster /assets/img_archive/adding_a_team.png %})

Digite o **Nome da equipe**. Se desejado, use o campo **Definir Equipe (Opcional)** para selecionar um atributo personalizado, local ou idioma para definir melhor quais dados de usuários a Equipe tem acesso. Por exemplo, um possível caso de uso é realizar [testes com Equipes](#test-with-teams) criando uma Equipe de desenvolvimento que só tem acesso a usuários teste, identificados por um atributo personalizado. Outro caso de uso é restringir a comunicação com usuários com base no produto.

Se uma Equipe é definida por um atributo personalizado, idioma ou país, você pode usar a Equipe para filtrar usuários finais para recursos como campanhas, canvas, Cartões de conteúdo, segmentos e mais. Para mais informações, veja [Atribuindo tags de Equipe](#tags-and-filters).

## Atribuir usuários a Equipes

Administradores da Braze e usuários limitados com a permissão de nível de empresa "Pode Gerenciar Configurações da Empresa" podem atribuir permissões de nível de Equipe a um usuário da empresa com acesso limitado. Quando atribuído a uma Equipe, os usuários da empresa ficam limitados a ler ou escrever apenas os dados disponíveis para suas respectivas Equipes, como idioma do usuário, local ou atributo personalizado, conforme definido quando a Equipe foi criada.

Para atribuir um usuário a uma Equipe, navegue até **Configurações** > **Usuários da Empresa** e selecione o usuário que você gostaria de adicionar à sua Equipe.

Em seguida, execute as etapas a seguir:

1. Na seção **Permissões de nível de espaço de trabalho**, adicione o usuário ao espaço de trabalho apropriado se ele ainda não estiver incluído.

![Permissões de nível de espaço de trabalho com o conjunto de permissões do modelo de banner.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. Selecione **+ Adicionar permissões de nível de equipe** e depois selecione a **Equipe** à qual você gostaria de adicionar este usuário.
3. Atribua permissões específicas na seção de permissões da **Equipe**.

![Permissões de modelo de landing page de nível de equipe.]({% image_buster /assets/img/teams.png %})

### Permissões de nível de Equipe disponíveis

A seguir estão todas as permissões disponíveis que você pode atribuir no nível da Equipe. Todas as permissões não listadas aqui são concedidas apenas no nível do espaço de trabalho e aparecerão como "--" na coluna de permissões de **Equipes**.

{% tabs %}
{% tab Granular permissions %}

{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

- Ver Campanhas
- Editar Campanhas
- Arquivar Campanhas
- Ver Canvas
- Editar Canvas
- Arquivar Canvas
- Ver Blocos de Conteúdo
- Editar Blocos de Conteúdo
- Arquivar Blocos de Conteúdo
- Lançar Blocos de Conteúdo
- Visualizar Feature Flags
- Editar Feature Flags
- Arquivar Feature Flags
- Ver Segmentos
- Editar Segmentos
- Ver Modelos de E-mail
- Editar Modelos de E-mail
- Arquivar Modelos de E-mail
- Ver Modelos de Webhook
- Editar Modelos de Webhook
- Arquivar Modelos de Webhook
- Ver Modelos de Links de E-mail
- Editar Modelos de Links de E-mail
- Ver Ativos da Biblioteca de Mídia
- Editar Ativos da Biblioteca de Mídia
- Excluir Ativos da Biblioteca de Mídia
- Lançar Campanhas
- Lançar Canvas
- Exportar Dados de Usuários
- Ver Perfis de Usuário em Conformidade com IPI
- Editar Usuários do Dashboard
- Aprovar Campanhas
- Aprovar Canvas
- Editar Modelos de Canvas
- Ver Modelos de Canvas
- Arquivar Modelos de Canvas
- Ver Relatórios do Dashboard
- Editar Relatórios do Dashboard
- Excluir Relatórios do Dashboard
- Ver IPI

{% endtab %}
{% tab Legacy permissions %}

- Acessar Campanhas, Canvas, Cartões, Blocos de Conteúdo, Feature Flags, Segmentos, Biblioteca de Mídia e Central de Preferências
- Enviar Campanhas, Canvas
- Lançar e Gerenciar Cartões de Conteúdo
- Editar Segmentos
- Exportar Dados de Usuários
- Ver Perfis de Usuário em Conformidade com IPI
- Gerenciar Usuários do Dashboard
- Gerenciar Ativos da Biblioteca de Mídia
- Aprovar e Rejeitar Campanhas
- Aprovar e Rejeitar Canvas
- Criar e Editar Modelos de Canvas
- Ver Modelos de Canvas
- Arquivar Modelos de Canvas
- Editar Modelos de Landing Page
- Ver Modelos de Landing Page
- Arquivar Modelos de Landing Page

{% endtab %}
{% endtabs %}

Para ver as descrições do que cada permissão de usuário inclui e como usá-las, consulte nossa seção [Permissões de usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Atribuir tags de Equipe {#tags-and-filters}

Você pode atribuir uma Equipe a canvas, campanhas, Cartões de conteúdo, segmentos, modelos de e-mail, modelos de webhook, blocos de conteúdo e ativos da biblioteca de mídia com o filtro **Adicionar Equipe**.
 
![Adicionando uma tag de Equipe a uma campanha.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Com base nas *definições* aplicadas quando a Equipe foi criada, quando um filtro de Equipe é atribuído, o público da ferramenta de engajamento é restrito a perfis de usuário que correspondem à definição.
- Com base nas *permissões* atribuídas, os membros da Equipe só poderão acessar ferramentas de engajamento do dashboard que tenham seu filtro de Equipe definido. Se eles tiverem permissões limitadas ou nenhuma permissão de espaço de trabalho, devem adicionar um filtro de Equipe a certos objetos antes de poderem salvá-los ou lançá-los. Os membros da Equipe também podem filtrar canvas, campanhas, Cartões de conteúdo e segmentos por Equipe para identificar conteúdo relevante para eles.

### Casos de uso

Considere os dois cenários a seguir para uma profissional de marketing na Braze chamada Michelle. Michelle é membro de uma Equipe chamada "Desenvolvimento". Ela tem acesso a todas as permissões em nível de Equipe para a Equipe de Desenvolvimento.

{% tabs %}
{% tab Scenario 1 - Only Team permissions %}

Neste cenário, Michelle é uma usuária limitada que não possui permissões em nível de espaço de trabalho. Suas permissões são mais ou menos assim:

![Permissões personalizadas sem permissões em nível de espaço de trabalho e 16 permissões baseadas em equipe.]({% image_buster /assets/img_archive/scenario1.png %})

Com base nas permissões atribuídas a Michelle, sempre que ela cria uma campanha, ela só pode atribuir a Equipe "Desenvolvimento" a essa campanha. Ela não pode lançar a campanha a menos que a Equipe esteja atribuída, e não pode visualizar ou acessar nenhuma outra tag de Equipe.

![Menu suspenso de tag de Equipe da campanha que exibe apenas a tag da Equipe "Desenvolvimento".]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scenario 2 - Team permissions and workspace permissions %}

Neste cenário, Michelle ainda é membro da Equipe de Desenvolvimento, mas ela também possui uma permissão adicional em nível de espaço de trabalho.

![Permissões personalizadas com uma permissão em nível de espaço de trabalho e 15 permissões baseadas em equipe.]({% image_buster /assets/img_archive/scenario2.png %})

Como Michelle tem a permissão em nível de espaço de trabalho de "Acessar Campanhas, Canvas, Cartões, Blocos de Conteúdo, Feature Flags, Segmentos, Biblioteca de Mídia e Central de Preferências", ela pode visualizar e atribuir outros filtros de Equipe à campanha que cria.

![Menu suspenso de tag de Equipe da campanha com várias tags de Equipe]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Semelhante ao primeiro cenário, Michelle deve adicionar a tag da Equipe de Desenvolvimento à campanha antes de poder lançá-la.

{% endtab %}
{% endtabs %}

## Teste com Equipes

Um possível caso de uso para Equipes é criar um sistema de aprovação baseado em Equipes para testar e lançar conteúdo em um ambiente de produção.

Para fazer isso, crie uma Equipe "Desenvolvimento" que tenha acesso apenas a usuários teste. Você pode limitar uma Equipe a acessar apenas usuários teste se seus usuários teste forem identificáveis por um atributo personalizado. Em seguida, adicione o atributo personalizado como uma definição ao criar ou editar a Equipe (veja a seção anterior [Criando Equipes](#creating-Teams)). Seus aprovadores devem ter acesso a todos os usuários.

O processo geral seria o seguinte:

1. A Equipe de Desenvolvimento cria uma campanha e adiciona a tag da Equipe "Desenvolvimento".
2. A Equipe de Desenvolvimento lança a campanha para usuários teste.
3. A Equipe de Aprovação valida o design da campanha local, promove e lança. Para lançar, a Equipe de Aprovação muda a tag da Equipe de "Desenvolvimento" para "[Todas as Equipes]" e relança a campanha.

Para alterações em campanhas ativas:

1. A Equipe de Desenvolvimento clona a campanha em execução, adiciona a tag da Equipe "Desenvolvimento" e salva.
2. A Equipe de Desenvolvimento faz edições e compartilha com a Equipe de Aprovação.
3. A Equipe de Aprovação remove a tag da Equipe "Desenvolvimento", pausa a campanha anterior e lança a nova campanha.

## Arquivar uma Equipe existente

Você pode arquivar Equipes na página **Equipes Internas**.

Selecione uma ou várias Equipes para arquivar. Se a Equipe não estiver associada a nenhum objeto dentro da Braze, ela será arquivada imediatamente. Se a Equipe estiver associada a um objeto, você verá uma opção para remover a Equipe após o processo de arquivamento ou substituir a Equipe.

![Arquivamento de uma Equipe associada a um objeto na Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Os administradores da Braze podem desarquivar uma Equipe selecionando a Equipe arquivada e escolhendo **Desarquivar**.