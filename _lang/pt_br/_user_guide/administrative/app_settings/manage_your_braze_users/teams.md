---
nav_title: Equipes
article_title: Equipes
page_order: 4
page_type: reference
description: "Este artigo de referência aborda como usar equipes da Braze no dashboard. Aqui, você pode aprender a criar equipes, atribuir funções e atribuir tags e filtros."

---

# Equipes

> Como administrador do Braze, você pode agrupar os usuários do seu dashboard em equipes com funções e permissões de usuário variadas. Isso permite que vários grupos não relacionados de usuários do dashboard trabalhem juntos em um espaço de trabalho, separando os tipos de conteúdo que podem ser editados.

As equipes podem ser configuradas de acordo com o local, o idioma e os atributos personalizados da base de clientes, de modo que os membros e não membros da equipe tenham acesso diferente aos recursos de envio de mensagens e aos dados de clientes. Filtros e tags de equipe podem ser atribuídos em várias ferramentas de engajamento.

As equipes não estão disponíveis em todos os contratos Braze. Se quiser acessar esse recurso, entre em contato com o gerente da sua conta Braze ou [entre em contato conosco](mailto:success@braze.com) para uma consulta.

## Como as equipes diferem dos conjuntos de permissões e funções?

{% multi_lang_include permissions.md content="Differences" %}

## Criação de equipes

Acesse **Configurações** > **Equipes internas** ) e selecione <i class="fas fa-plus"></i> ** Adicionar equipe**.

![Adição de uma nova equipe][68]

Digite o **nome da equipe**. Se desejar, use o campo **Definir equipe** para selecionar um atributo personalizado, local ou idioma para definir melhor a quais dados de usuários a equipe tem acesso. Por exemplo, um possível caso de uso é realizar [testes com equipes](#testing-with-teams) criando uma equipe de desenvolvimento que só tenha acesso a usuários teste, identificados por um atributo personalizado. Outro caso de uso é restringir a comunicação com os usuários com base no produto.

Se uma equipe for definida por um atributo personalizado, idioma ou país, será possível usar a equipe para filtrar usuários finais para recursos como campanhas, Canvas, cartões de conteúdo, segmentos e muito mais. Para saber mais, consulte [Atribuir tags de equipe](#tags-and-filters).

## Atribuir usuários a equipes

Os administradores do Braze e os usuários limitados com a permissão no nível da empresa "Pode gerenciar as configurações da empresa" podem atribuir permissões no nível da equipe a um usuário do dashboard com acesso limitado. Quando atribuídos a uma equipe, os usuários do dashboard são limitados a apenas ler ou gravar dados disponíveis para suas equipes específicas, como idioma do usuário, local ou atributo personalizado, conforme definido quando a equipe foi criada.

Para atribuir um usuário a uma equipe, navegue até **Configurações** > **Usuários da empresa** e selecione o usuário que deseja adicionar à sua equipe.

Em seguida, execute as etapas a seguir:

1. Selecione **Edit**.
2. Defina sua função de usuário como **Limited (Limitada**).
3. Adicione-os ao espaço de trabalho apropriado. 
4. Selecione a **equipe** à qual deseja adicionar esse usuário e atribua permissões específicas na coluna Permissões **da equipe**.

![][2]

### Permissões disponíveis no nível da equipe

A seguir estão todas as permissões disponíveis que podem ser atribuídas no nível da equipe. Todas as permissões não listadas aqui são concedidas apenas no nível do espaço de trabalho, e essas permissões aparecerão como "--" na coluna Permissões de **equipes**.

- Acesse campanhas, telas, cartões, blocos de conteúdo, Feature Flags, segmentos, biblioteca de mídia e centrais de preferências
- Enviar campanhas, canvas
- Publicar cartões
- Editar segmentos
- Exportar dados de usuários
- Ver perfis de usuário em conformidade com IPI
- Gerenciar usuários do dashboard
- Gerenciar ativos da biblioteca de mídia

Para ver as descrições do que cada permissão de usuário inclui e como usá-las, consulte nossa seção [Permissões de usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Atribuindo tags de equipe {#tags-and-filters}

É possível atribuir uma equipe a Canvases, campanhas, cartões, segmentos, modelos de e-mail e ativos da biblioteca de mídia com o filtro **Add Team (Adicionar equipe** ).
 
![Adição de uma tag de equipe a uma campanha][3]{: style="max-width:70%;"}

- Com base nas *definições* aplicadas quando a equipe foi criada, quando um filtro de equipe é atribuído, o público dessa ferramenta de engajamento fica restrito aos perfis de usuário que correspondem à definição.
- Com base nas *permissões* atribuídas, os membros da equipe só poderão acessar as ferramentas de engajamento do dashboard que tiverem seu filtro de equipe definido. Se eles tiverem permissões limitadas ou nenhuma permissão de espaço de trabalho, deverão adicionar um filtro de equipe a determinados objetos antes de poderem salvá-los ou iniciá-los. Os membros da equipe também podem filtrar Canvases, campanhas, cartões e segmentos por equipe para identificar o conteúdo relevante para eles.

### Casos de uso

Considere os dois cenários a seguir para uma profissional de marketing no Braze chamada Michelle. Michelle é membro de uma equipe chamada "Desenvolvimento". Ela tem acesso a todas as permissões de nível de equipe para a equipe de desenvolvimento.

{% tabs %}
{% tab Cenário 1 - Apenas permissões da equipe %}

Nesse cenário, Michelle é uma usuária limitada que não tem permissões no nível do espaço de trabalho. Suas permissões são mais ou menos assim:

![]({% image_buster /assets/img_archive/scenario1.png %})

Com base nas permissões atribuídas a Michelle, sempre que ela criar uma campanha, só poderá atribuir a equipe de "Desenvolvimento" a essa campanha. Ela não pode lançar a campanha a menos que a equipe seja atribuída e não pode visualizar ou acessar nenhuma outra tag de equipe.

![]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Cenário 2 - Permissões da equipe e permissões do espaço de trabalho %}

Nesse cenário, Michelle ainda é um membro da equipe de desenvolvimento, mas também tem uma permissão adicional no nível do espaço de trabalho.

![]({% image_buster /assets/img_archive/scenario2.png %})

Como Michelle tem a permissão no nível do espaço de trabalho "Access Campaigns, Canvas, Cards, Content Blocks, Feature Flags, Segments, Media Library, and Preference Centers", ela pode visualizar e atribuir outros filtros de equipe à campanha que criar.

![]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Da mesma forma que no primeiro cenário, Michelle deve adicionar a tag da equipe de Desenvolvimento à campanha antes de lançá-la.

{% endtab %}
{% endtabs %}

## Testes com equipes

Um possível caso de uso para equipes é criar um sistema de aprovação baseado em equipes para testar e lançar conteúdo em um ambiente de produção.

Para isso, crie uma equipe de "Desenvolvimento" que tenha acesso apenas aos usuários teste. É possível limitar o acesso de uma equipe apenas a usuários de teste se os usuários de teste forem identificáveis por um atributo personalizado. Em seguida, adicione o atributo personalizado como uma definição ao criar ou editar a equipe (consulte a seção anterior [Criando equipes](#creating-teams)). Seus aprovadores devem ter acesso a todos os usuários.

O processo geral seria o seguinte:

1. A equipe de desenvolvimento cria uma campanha e adiciona a tag de equipe "Desenvolvimento".
2. A equipe de desenvolvimento lança a campanha para testar os usuários.
3. A equipe de aprovação valida o design da campanha local, promove e lança. Para lançar, a equipe do Aprovador altera a tag da equipe de "Desenvolvimento" para "[Todas as equipes]" e relança a campanha.

Para alterações em campanhas ativas:

1. A equipe de desenvolvimento clona a campanha em andamento, adiciona a tag da equipe de "Desenvolvimento" e salva.
2. A equipe de desenvolvimento faz as edições e compartilha com a equipe do Aprovador.
3. A equipe do aprovador remove a tag da equipe de "Desenvolvimento", pausa a campanha anterior e lança a nova campanha.

## Arquivando uma equipe existente

Você pode arquivar equipes na página **Equipes internas**.

Selecione uma ou várias equipes para arquivar. Se a equipe não estiver associada a nenhum objeto na Braze, ela será arquivada imediatamente. Se a equipe estiver associada a um objeto, será apresentada uma opção para remover a equipe após o processo de arquivamento ou substituir a equipe.

![Arquivamento de uma equipe associada a um objeto no Braze][86]{: style="max-width:70%;"}

Os administradores do Braze podem desarquivar uma equipe selecionando a equipe arquivada e selecionando **Desarquivar**.

[2]: {% image_buster /assets/img/teams.png %}
[3]: {% image_buster /assets/img/teams1.png %}
[68]: {% image_buster /assets/img_archive/adding_a_team.png %}
[86]: {% image_buster /assets/img_archive/archive_a_team.png %}
