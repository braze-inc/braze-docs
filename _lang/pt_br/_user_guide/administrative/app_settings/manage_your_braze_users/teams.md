---
nav_title: Equipes
article_title: Equipes
page_order: 4
page_type: reference
description: "Este artigo de referência aborda como usar o Braze Teams no painel de controle. Aqui, você pode aprender a criar Teams, atribuir funções e atribuir tags e filtros."

---

# Equipes

> Como administrador do Braze, você pode agrupar os usuários do painel em Teams com funções e permissões de usuário variadas. Isso permite que você tenha vários grupos não relacionados de usuários do painel trabalhando juntos em um espaço de trabalho, separando os tipos de conteúdo que podem ser editados.

As equipes podem ser configuradas de acordo com a localização, o idioma e os atributos personalizados da base de clientes, de modo que os membros da equipe e os não membros tenham acesso diferente aos recursos de mensagens e aos dados do cliente. Filtros e tags de equipe podem ser atribuídos em várias ferramentas de engajamento.

As equipes não estão disponíveis em todos os contratos Braze. Se quiser acessar esse recurso, entre em contato com o gerente da sua conta Braze ou [entre em contato conosco](mailto:success@braze.com) para uma consulta.

## Como as equipes diferem dos conjuntos de permissões e funções?

{% multi_lang_include permissions.md content="Differences" %}

## Criando equipes

Vá para **Settings** > **Internal Teams** e selecione <i class="fas fa-plus"></i> **Add Team**.

Janela para adicionar uma nova equipe.]({% image_buster /assets/img_archive/adding_a_team.png %}){: style="max-width:70%;"}

Digite o **nome da equipe**. Se desejar, use o campo **Definir equipe** para selecionar um atributo personalizado, local ou idioma para definir melhor a quais dados do usuário a equipe tem acesso. Por exemplo, um possível caso de uso é realizar [testes com equipes](#testing-with-Teams) criando uma equipe de desenvolvimento que só tenha acesso a usuários de teste, identificados por um atributo personalizado. Outro caso de uso é restringir a comunicação com os usuários com base no produto.

Se uma equipe for definida por um atributo personalizado, idioma ou país, você poderá usar a equipe para filtrar usuários finais para recursos como campanhas, Canvases, Content Cards, segmentos e muito mais. Para saber mais, consulte [Atribuição de tags de equipe](#tags-and-filters).

## Atribuição de usuários a equipes

Os administradores do Braze e os usuários limitados com a permissão no nível da empresa "Pode gerenciar as configurações da empresa" podem atribuir permissões no nível da equipe a um usuário do painel com acesso limitado. Quando atribuídos a uma equipe, os usuários do painel são limitados a apenas ler ou gravar dados disponíveis para suas equipes específicas, como idioma do usuário, local ou atributo personalizado, conforme definido quando a equipe foi criada.

Para atribuir um usuário a uma equipe, navegue até **Settings** > **Company Users** e selecione o usuário que deseja adicionar à sua equipe.

Em seguida, execute as etapas a seguir:

1. Na seção **Permissões no nível do espaço de** trabalho, adicione o usuário ao espaço de trabalho apropriado se ele ainda não estiver incluído.

\![Uma permissão definida para o espaço de trabalho "Swifty & Droidboy".]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2\. Selecione **\+ Adicionar permissões de nível de equipe** e, em seguida, selecione a **equipe** à qual deseja adicionar esse usuário.
3\. Atribua permissões específicas na coluna Permissões **da equipe**.

\![Uma seção para selecionar permissões para a equipe de "Suporte ao cliente".]({% image_buster /assets/img/teams.png %})

### Permissões disponíveis no nível da equipe

A seguir estão todas as permissões disponíveis que podem ser atribuídas no nível da equipe. Todas as permissões não listadas aqui são concedidas somente no nível do espaço de trabalho, e essas permissões aparecerão como "--" na coluna Permissões de **equipes**.

- Acesse campanhas, telas, cartões, blocos de conteúdo, sinalizadores de recursos, segmentos, biblioteca de mídia e centros de preferência
- Enviar campanhas, telas
- Iniciar e gerenciar cartões de conteúdo
- Editar segmentos
- Exportar dados do usuário
- Exibir perfis de usuário em conformidade com PII
- Gerenciar usuários do painel
- Gerenciar ativos da biblioteca de mídia
- Campanhas de aprovação e negação
- Aprovar e recusar telas
- Criar e editar modelos de tela
- Exibir modelos de tela
- Modelos do Archive Canvas
- Criar e editar modelos de páginas de destino
- Exibir modelos de página de destino
- Modelos de página de destino de arquivo

Para ver as descrições do que cada permissão de usuário inclui e como usá-las, consulte nossa seção [Permissões de usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Atribuição de tags de equipe {#tags-and-filters}

Você pode atribuir uma equipe a Canvases, campanhas, cartões, segmentos, modelos de e-mail e ativos da biblioteca de mídia com o filtro **Add Team**.
 
\![Adicionando uma tag de equipe a uma campanha.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Com base nas *definições* aplicadas quando a equipe foi criada, quando um filtro de equipe é atribuído, o público dessa ferramenta de engajamento fica restrito aos perfis de usuário que correspondem à definição.
- Com base nas *permissões* atribuídas, os membros da equipe só poderão acessar as ferramentas de engajamento do painel que tiverem seu filtro de equipe definido. Se eles tiverem permissões limitadas ou nenhuma permissão de espaço de trabalho, deverão adicionar um filtro de equipe a determinados objetos antes de poderem salvá-los ou iniciá-los. Os membros da equipe também podem filtrar Canvases, campanhas, cartões e segmentos por equipe para identificar o conteúdo relevante para eles.

### Casos de uso

Considere os dois cenários a seguir para uma profissional de marketing no Braze chamada Michelle. Michelle é membro de uma equipe chamada "Desenvolvimento". Ela tem acesso a todas as permissões no nível da equipe para a equipe de desenvolvimento.

{% tabs %}
{% tab Scenario 1 - Only Team permissions %}

Nesse cenário, Michelle é uma usuária limitada que não tem permissões no nível do espaço de trabalho. Suas permissões são mais ou menos assim:

Permissões personalizadas sem permissões no nível do espaço de trabalho e 16 permissões baseadas em equipe.]({% image_buster /assets/img_archive/scenario1.png %})

Com base nas permissões atribuídas a Michelle, sempre que ela criar uma campanha, só poderá atribuir a equipe de "Desenvolvimento" a essa campanha. Ela não pode lançar a campanha a menos que a equipe esteja atribuída e não pode visualizar ou acessar nenhuma outra tag de equipe.

dropdown da tag Equipe de campanha que exibe apenas a tag Equipe de "Desenvolvimento".]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scenario 2 - Team permissions and workspace permissions %}

Nesse cenário, Michelle ainda é membro da equipe de desenvolvimento, mas também tem uma permissão adicional no nível do espaço de trabalho.

Permissões personalizadas com uma permissão no nível do espaço de trabalho e 15 permissões baseadas em equipe.]({% image_buster /assets/img_archive/scenario2.png %})

Como Michelle tem a permissão no nível do espaço de trabalho de "Access Campaigns, Canvases, Cards, Content Blocks, Feature Flags, Segments, Media Library e Preference Centers", ela pode visualizar e atribuir outros filtros da equipe à campanha que criar.

dropdown de tags de equipe de campanha com várias tags de equipe]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Da mesma forma que no primeiro cenário, Michelle deve adicionar a tag Equipe de desenvolvimento à campanha antes de lançá-la.

{% endtab %}
{% endtabs %}

## Testes com equipes

Um possível caso de uso do Teams é a criação de um sistema de aprovação baseado no Teams para testar e lançar conteúdo em um ambiente de produção.

Para isso, crie uma equipe de "desenvolvimento" que só tenha acesso a usuários de teste. Você pode limitar uma equipe a acessar apenas usuários de teste se os usuários de teste forem identificáveis por um atributo personalizado. Em seguida, adicione o atributo personalizado como uma definição ao criar ou editar a equipe (consulte a seção anterior [Criando equipes](#creating-Teams)). Seus aprovadores devem ter acesso a todos os usuários.

O processo geral seria o seguinte:

1. A equipe de desenvolvimento cria uma campanha e adiciona a tag de equipe "Desenvolvimento".
2. A equipe de desenvolvimento lança a campanha para testar os usuários.
3. A Equipe de Aprovação valida o design, a promoção e o lançamento da campanha local. Para lançar, a equipe de aprovadores altera a tag da equipe de "Desenvolvimento" para "[Todas as equipes]" e relança a campanha.

Para alterações em campanhas ativas:

1. A Equipe de Desenvolvimento clona a campanha em andamento, adiciona a tag da Equipe de "Desenvolvimento" e salva.
2. A equipe de desenvolvimento faz edições e compartilha com a equipe de aprovação.
3. A Equipe de Aprovadores remove a tag da Equipe de "Desenvolvimento", pausa a campanha anterior e lança a nova campanha.

## Arquivamento de uma equipe existente

Você pode arquivar equipes na página **Equipes internas**.

Selecione um ou vários Teams para arquivar. Se a equipe não estiver associada a nenhum objeto no Braze, ela será arquivada imediatamente. Se a equipe estiver associada a um objeto, será apresentada uma opção para remover a equipe após o processo de arquivamento ou substituir a equipe.

Arquivar uma equipe associada a um objeto no Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Os administradores do Braze podem desarquivar uma equipe selecionando a equipe arquivada e selecionando **Desarquivar**.

