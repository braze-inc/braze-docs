---
nav_title: Equipes
article_title: Equipes
page_order: 4
page_type: reference
description: "Este artigo de referência cobre como usar as Equipes do Braze no dashboard. Aqui, você pode aprender como criar Equipes, atribuir funções e atribuir tags e filtros."

---

# Equipes

> Como administrador do Braze, você pode agrupar os usuários do seu dashboard em Equipes com diferentes funções e permissões de usuário. Isso permite que vários grupos não relacionados de usuários do dashboard trabalhem juntos em um espaço de trabalho, separando os tipos de conteúdo que podem ser editados.

As Equipes podem ser configuradas com base na localização da base de clientes, idioma e atributos personalizados, para que os membros da Equipe e os não-membros tenham acesso diferente a recursos de envio de mensagens e dados de clientes. Filtros e tags de equipe podem ser atribuídos em várias ferramentas de engajamento.

As equipes não estão disponíveis em todos os contratos Braze. Se quiser acessar esse recurso, entre em contato com o gerente da sua conta Braze ou [entre em contato conosco](mailto:success@braze.com) para uma consulta.

## Como as Equipes diferem de conjuntos de permissões e funções?

{% multi_lang_include permissions.md content="Differences" %}

## Criando Equipes

Acesse **Configurações** > **Equipes internas** ) e selecione <i class="fas fa-plus"></i> ** Adicionar equipe**.

![Adicionando uma nova Equipe]({% image_buster /assets/img_archive/adding_a_team.png %})

Digite o **nome da equipe**. Se desejado, use o campo **Definir Equipe** para selecionar um atributo personalizado, localização ou idioma para definir melhor quais dados de usuário a Equipe tem acesso. Por exemplo, um possível caso de uso é realizar [testes com Equipes](#testing-with-Teams) criando uma Equipe de desenvolvimento que só tem acesso a usuários de teste, identificados por um atributo personalizado. Outro caso de uso é restringir a comunicação com os usuários com base no produto.

Se uma Equipe é definida por um atributo personalizado, idioma ou país, você pode então usar a Equipe para filtrar usuários finais para recursos como campanhas, Canvases, Cartões de Conteúdo, segmentos e mais. Para mais informações, veja [Atribuindo tags de Equipe](#tags-and-filters).

## Atribuindo usuários a Equipes

Administradores do Braze e usuários limitados com a permissão de nível de empresa "Pode Gerenciar Configurações da Empresa" podem atribuir permissões de nível de Equipe a um usuário do dashboard com acesso limitado. Quando atribuídos a uma Equipe, os usuários do dashboard estão limitados a ler ou escrever apenas os dados disponíveis para suas respectivas Equipes, como idioma do usuário, localização ou atributo personalizado, conforme definido quando a Equipe foi criada.

Para atribuir um usuário a uma Equipe, navegue até **Configurações** > **Usuários da Empresa** e selecione um usuário que você gostaria de adicionar à sua Equipe.

Em seguida, execute as etapas a seguir:

1. Selecione **Edit**.
2. Defina sua função de usuário como **Limited (Limitada**).
3. Adicione-os ao espaço de trabalho apropriado. 
4. Selecione a **equipe** à qual deseja adicionar esse usuário e atribua permissões específicas na coluna Permissões **da equipe**.

![]({% image_buster /assets/img/teams.png %})

### Permissões de nível de Equipe disponíveis

As seguintes são todas as permissões disponíveis que você pode atribuir no nível da Equipe. Todas as permissões não listadas aqui são concedidas apenas no nível do espaço de trabalho, e essas permissões aparecerão como "--" na coluna Permissões de **equipes**.

- Acesse campanhas, telas, cartões, blocos de conteúdo, Feature Flags, segmentos, biblioteca de mídia e centrais de preferências
- Enviar campanhas, canvas
- Publicar cartões
- Editar segmentos
- Exportar dados de usuários
- Ver perfis de usuário em conformidade com IPI
- Gerenciar usuários do dashboard
- Gerenciar ativos da biblioteca de mídia

Para ver as descrições do que cada permissão de usuário inclui e como usá-las, consulte nossa seção [Permissões de usuário]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Atribuindo tags de Equipe {#tags-and-filters}

Você pode atribuir uma Equipe a Canvases, campanhas, cartões, segmentos, modelos de e-mail e ativos da biblioteca de mídia com o filtro **Adicionar Equipe**.
 
![Adicionando uma tag de Equipe a uma campanha]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- Com base nas *definições* aplicadas quando a Equipe foi criada, quando um filtro de Equipe é atribuído, o público da ferramenta de engajamento é restrito a perfis de usuário que correspondem à definição.
- Com base nas *permissões* atribuídas, os membros da Equipe só poderão acessar as ferramentas de engajamento do dashboard que têm seu filtro de Equipe definido. Se eles tiverem permissões limitadas ou nenhuma permissão de espaço de trabalho, devem adicionar um filtro de Equipe a certos objetos antes de poderem salvá-los ou lançá-los. Os membros da Equipe também podem filtrar Canvases, campanhas, cartões e segmentos por Equipe para identificar conteúdo relevante para eles.

### Casos de uso

Considere os dois cenários a seguir para uma profissional de marketing no Braze chamada Michelle. Michelle é membro de uma Equipe chamada "Desenvolvimento". Ela tem acesso a todas as permissões de nível de Equipe para a Equipe de Desenvolvimento.

{% tabs %}
{% tab Cenário 1 - Apenas permissões de Equipe %}

Nesse cenário, Michelle é uma usuária limitada que não tem permissões no nível do espaço de trabalho. Suas permissões são mais ou menos assim:

![]({% image_buster /assets/img_archive/scenario1.png %})

Com base nas permissões atribuídas a Michelle, sempre que ela cria uma campanha, ela só pode atribuir a Equipe "Desenvolvimento" a essa campanha. Ela não pode lançar a campanha a menos que a Equipe esteja atribuída, e não pode visualizar ou acessar nenhuma outra tag de Equipe.

![]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Cenário 2 - Permissões da equipe e permissões do espaço de trabalho %}

Neste cenário, Michelle ainda é membro da Equipe de Desenvolvimento, mas ela também tem uma permissão adicional de nível de espaço de trabalho.

![]({% image_buster /assets/img_archive/scenario2.png %})

Porque Michelle tem a permissão de nível de espaço de trabalho de "Acessar Campanhas, Canvases, Cartões, Blocos de Conteúdo, Sinais de Recursos, Segmentos, Biblioteca de Mídia e Centros de Preferência", ela pode visualizar e atribuir outros filtros de Equipe à campanha que cria.

![]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Semelhante ao primeiro cenário, Michelle deve adicionar a tag da Equipe de Desenvolvimento à campanha antes que ela possa lançá-la.

{% endtab %}
{% endtabs %}

## Testando com Equipes

Um possível caso de uso para Equipes é criar um sistema de aprovação baseado em Equipes para testar e lançar conteúdo em um ambiente de produção.

Para fazer isso, crie uma Equipe "Desenvolvimento" que tenha acesso apenas a usuários de teste. Você pode limitar uma Equipe a acessar apenas usuários de teste se seus usuários de teste forem identificáveis por um atributo personalizado. Em seguida, adicione o atributo personalizado como uma definição ao criar ou editar a Equipe (veja a seção anterior [Criando Equipes](#creating-Teams)). Seus aprovadores devem ter acesso a todos os usuários.

O processo geral seria o seguinte:

1. A Equipe de Desenvolvimento cria uma campanha e adiciona a tag da Equipe "Desenvolvimento".
2. A Equipe de Desenvolvimento lança a campanha para usuários de teste.
3. A Equipe de Aprovação valida o design da campanha local, promove e lança. Para lançar, a Equipe de Aprovação muda a tag da Equipe de "Desenvolvimento" para "[Todas as Equipes]" e relança a campanha.

Para alterações em campanhas ativas:

1. A Equipe de Desenvolvimento clona a campanha em execução, adiciona a tag da Equipe "Desenvolvimento" e salva.
2. A Equipe de Desenvolvimento faz edições e compartilha com a Equipe de Aprovação.
3. A Equipe de Aprovação remove a tag da Equipe "Desenvolvimento", pausa a campanha anterior e lança a nova campanha.

## Arquivamento de uma equipe existente

Você pode arquivar Equipes na página **Equipes Internas**.

Selecione uma ou várias Equipes para arquivar. Se a Equipe não estiver associada a nenhum objeto dentro do Braze, a Equipe será arquivada imediatamente. Se a Equipe estiver associada a um objeto, você será apresentado a uma opção para remover a Equipe após o processo de arquivamento ou substituir a Equipe.

![Arquivando uma Equipe que está associada a um objeto no Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Os administradores do Braze podem desarquivar uma Equipe selecionando a Equipe arquivada e selecionando **Desarquivar**.

