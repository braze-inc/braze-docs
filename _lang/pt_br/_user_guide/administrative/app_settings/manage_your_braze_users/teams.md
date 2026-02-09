---
nav_title: Equipes
article_title: Equipes
page_order: 4
page_type: reference
description: "Este artigo de referência cobre como usar as Equipes Braze no dashboard. Aqui, você pode aprender como criar Equipes, atribuir funções e atribuir tags e filtros."

---

# Equipes

> Como um administrador Braze, você pode agrupar seus usuários do dashboard em Equipes com diferentes funções e permissões de usuário. Isso permite que vários grupos não relacionados de usuários do dashboard trabalhem juntos em um espaço de trabalho, separando os tipos de conteúdo que podem ser editados.

As Equipes podem ser configuradas com base na localização da base de clientes, idioma e atributos personalizados, para que os membros da Equipe e os não membros tenham acesso diferente aos recursos de envio de mensagens e dados de clientes. Filtros e tags de equipe podem ser atribuídos em várias ferramentas de engajamento. Não há limite para quantas equipes você pode criar em seu espaço de trabalho.

As equipes não estão disponíveis em todos os contratos Braze. Para acessar este recurso, entre em contato com seu gerente de conta Braze ou [entre em contato conosco](mailto:success@braze.com) para uma consulta.

## Como as Equipes diferem de conjuntos de permissões e funções?

{% multi_lang_include permissions.md content="Differences" %}

## Criar Equipes {#creating-teams}

Acesse **Configurações** > **Equipes internas** ) e selecione <i class="fas fa-plus"></i> ** Adicionar equipe**.

![Janela para adicionar uma nova Equipe.]({% image_buster /assets/img_archive/adding_a_team.png %}){: style="max-width:70%;"}

Digite o **nome da equipe**. Se desejado, use o campo **Definir Equipe** para selecionar um atributo personalizado, localização ou idioma para definir ainda mais quais dados de usuário a Equipe tem acesso. Por exemplo, um possível caso de uso é realizar [testes com Equipes](#test-with-teams) criando uma Equipe de desenvolvimento que só tem acesso a usuários de teste, identificados por um atributo personalizado. Outro caso de uso é restringir a comunicação com usuários com base no produto.

Se uma Equipe for definida por um atributo personalizado, idioma ou país, você pode então usar a Equipe para filtrar usuários finais para recursos como campanhas, Canvases, Cartões de Conteúdo, segmentos e mais. Para mais informações, veja [Atribuindo tags de Equipe](#tags-and-filters).

## Atribuir usuários a Equipes

Administradores Braze e usuários limitados com a permissão em nível de empresa "Pode Gerenciar Configurações da Empresa" podem atribuir permissões em nível de Equipe a um usuário do dashboard com acesso limitado. Quando atribuídos a uma Equipe, os usuários do dashboard estão limitados a ler ou escrever apenas os dados disponíveis para suas respectivas Equipes, como idioma do usuário, localização ou atributo personalizado, conforme definido quando a Equipe foi criada.

Para atribuir um usuário a uma Equipe, navegue até **Configurações** > **Usuários da Empresa** e selecione um usuário que você gostaria de adicionar à sua Equipe.

Em seguida, execute as etapas a seguir:

1. Na seção **Permissões em nível de Espaço de Trabalho**, adicione o usuário ao espaço de trabalho apropriado se ele ainda não estiver incluído.

![Um conjunto de permissões para o espaço de trabalho "Swifty & Droidboy".]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2\. Selecione **\+ Adicionar permissões em nível de equipe**, em seguida, selecione a **Equipe** à qual você gostaria de adicionar este usuário.
3\. Atribua permissões específicas da coluna de permissões da **Equipe**.

![Uma seção para selecionar permissões para a equipe "Suporte ao Cliente".]({% image_buster /assets/img/teams.png %})

### Permissões disponíveis em nível de equipe

As seguintes são todas as permissões disponíveis que você pode atribuir em nível de equipe. Todas as permissões não listadas aqui são concedidas apenas no nível do espaço de trabalho, e essas permissões aparecerão como "--" na coluna Permissões de **equipes**.

- Acesse campanhas, telas, cartões, blocos de conteúdo, Feature Flags, segmentos, biblioteca de mídia e centrais de preferências
- Enviar campanhas, canvas
- Lançar e Gerenciar Cartões de Conteúdo
- Editar segmentos
- Exportar dados de usuários
- Ver perfis de usuário em conformidade com IPI
- Gerenciar usuários do dashboard
- Gerenciar ativos da biblioteca de mídia
- Aprovar e rejeitar campanhas
- Aprovar e rejeitar canvas
- Criar e editar modelos de canva
- Ver modelos de canva
- Arquivar modelos de canva
- Criar e editar modelos de landing page
- Exibir modelos de landing page
- Arquivar modelos de landing page

Para ver as descrições do que cada permissão de usuário inclui e como usá-las, consulte nossa seção [Permissões de usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Atribuir tags de equipe {#tags-and-filters}

Você pode atribuir uma equipe a Canvases, campanhas, cartões, segmentos, modelos de e-mail e ativos da biblioteca de mídia com o filtro **Adicionar Equipe**.
 
![Adicionando uma tag de equipe a uma campanha.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Com base nas *definições* aplicadas quando a equipe foi criada, quando um filtro de equipe é atribuído, o público da ferramenta de engajamento é restrito a perfis de usuário que correspondem à definição.
- Com base nas *permissões* atribuídas, os membros da equipe só poderão acessar ferramentas de engajamento do dashboard que tenham seu filtro de equipe definido. Se eles tiverem permissões limitadas ou nenhuma permissão de espaço de trabalho, devem adicionar um filtro de equipe a certos objetos antes de poderem salvá-los ou lançá-los. Os membros da equipe também podem filtrar Canvases, campanhas, cartões e segmentos por equipe para identificar conteúdo relevante para eles.

### Casos de uso

Considere os dois cenários a seguir para uma profissional de marketing no Braze chamada Michelle. Michelle é membro de uma equipe chamada "Desenvolvimento". Ela tem acesso a todas as permissões em nível de equipe para a equipe de Desenvolvimento.

{% tabs %}
{% tab Scenario 1 - Only Team permissions %}

Neste cenário, Michelle é uma usuária limitada que não tem permissões em nível de espaço de trabalho. Suas permissões são mais ou menos assim:

![Permissões personalizadas sem permissões em nível de espaço de trabalho e 16 permissões baseadas em equipe.]({% image_buster /assets/img_archive/scenario1.png %})

Com base nas permissões atribuídas a Michelle, sempre que ela cria uma campanha, ela só pode atribuir a equipe "Desenvolvimento" a essa campanha. Ela não pode lançar a campanha a menos que a equipe seja atribuída, e não pode visualizar ou acessar nenhuma outra tag de equipe.

![Menu suspenso de tag de equipe da campanha que exibe apenas a tag da equipe "Desenvolvimento".]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scenario 2 - Team permissions and workspace permissions %}

Neste cenário, Michelle ainda é membro da Equipe de Desenvolvimento, mas ela também tem uma permissão adicional em nível de espaço de trabalho.

![Permissões personalizadas com uma permissão em nível de espaço de trabalho e 15 permissões baseadas em equipe.]({% image_buster /assets/img_archive/scenario2.png %})

Como Michelle tem a permissão em nível de espaço de trabalho de "Acessar Campanhas, Canvases, Cartões, Blocos de Conteúdo, Sinais de Recursos, Segmentos, Biblioteca de Mídia e Centros de Preferência", ela pode visualizar e atribuir outros filtros de Equipe à campanha que cria.

![Menu suspenso de tags da Equipe de Campanha com várias tags de Equipe]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Semelhante ao primeiro cenário, Michelle deve adicionar a tag da Equipe de Desenvolvimento à campanha antes que ela possa lançá-la.

{% endtab %}
{% endtabs %}

## Teste com Equipes

Um possível caso de uso para Equipes é criar um sistema de aprovação baseado em Equipes para testar e lançar conteúdo em um ambiente de produção.

Para fazer isso, crie uma Equipe de "Desenvolvimento" que tenha acesso apenas a usuários de teste. Você pode limitar uma Equipe a acessar apenas usuários de teste se seus usuários de teste forem identificáveis por um atributo personalizado. Em seguida, adicione o atributo personalizado como uma definição ao criar ou editar a Equipe (veja a seção anterior [Criando Equipes](#creating-Teams)). Seus aprovadores devem ter acesso a todos os usuários.

O processo geral seria o seguinte:

1. A Equipe de Desenvolvimento cria uma campanha e adiciona a tag da Equipe "Desenvolvimento".
2. A Equipe de Desenvolvimento lança a campanha para usuários de teste.
3. A Equipe de Aprovação valida o design da campanha local, promove e lança. Para lançar, a Equipe de Aprovação muda a tag da Equipe de "Desenvolvimento" para "[Todas as Equipes]" e relança a campanha.

Para alterações em campanhas ativas:

1. A Equipe de Desenvolvimento clona a campanha em execução, adiciona a tag da Equipe "Desenvolvimento" e salva.
2. A Equipe de Desenvolvimento faz edições e compartilha com a Equipe de Aprovação.
3. A Equipe de Aprovação remove a tag da Equipe "Desenvolvimento", pausa a campanha anterior e lança a nova campanha.

## Arquivar uma Equipe existente

Você pode arquivar Equipes na página **Equipes Internas**.

Selecione uma ou várias Equipes para arquivar. Se a Equipe não estiver associada a nenhum objeto dentro do Braze, o Braze arquiva a Equipe imediatamente. Se a Equipe estiver associada a um objeto, o Braze apresenta uma opção para remover a Equipe após o processo de arquivamento ou substituir a Equipe.

![Arquivamento de uma equipe associada a um objeto no Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Os administradores do Braze podem desarquivar uma Equipe selecionando a Equipe arquivada e selecionando **Desarquivar**.

