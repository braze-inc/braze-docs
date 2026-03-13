---
nav_title: O dashboard
article_title: O dashboard Braze
page_order: 5
page_type: reference
description: "O dashboard Braze é seu espaço de trabalho central para construir, gerenciar e analisar o engajamento do cliente. Ele reúne ferramentas de envio de mensagens, insights de público, segmentação e dados de performance em tempo real em um só lugar."

---

# O dashboard Braze

> O dashboard Braze é seu espaço de trabalho central para construir, gerenciar e analisar o engajamento do cliente. Acesse em [dashboard.braze.com](https://dashboard.braze.com/) ou [dashboard.braze.eu](https://dashboard.braze.eu/).

Use o dashboard Braze para planejar campanhas, lançar e gerenciar mensagens, explorar insights de público, ajustar segmentação e revisar métricas de performance e engajamento em tempo real a partir de uma única interface.

## Visão geral do dashboard

Quando você faz login, o dashboard fornece uma visão centralizada de suas ferramentas e dados de engajamento:

- **Página inicial:** Mostra seu [conteúdo editado recentemente](#pick-up-where-you-left-off) e métricas de performance chave de relance
- **Navegação à esquerda:** Organiza ferramentas por função (envio de mensagens, público, análise de dados, configurações)
- **Cabeçalho global:** Fornece acesso rápido à busca, suporte, configurações de idioma, notificações e sua conta

Sua experiência no dashboard é organizada por [espaços de trabalho]({{site.baseurl}}/user_guide/getting_started/workspaces), que ajudam você a gerenciar conteúdo para diferentes marcas, regiões ou equipes. Você pode [alternar entre espaços de trabalho](#workspace-switcher) a qualquer momento na navegação lateral.

## Acesse seu dashboard

Para começar, [faça login na sua conta Braze]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account). Seu acesso às páginas dentro do dashboard e permissão para realizar certas ações são baseados nas [permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) atribuídas a você. Se você precisar de ajuda com suas permissões, entre em contato com seus administradores Braze.

## Navegar Braze

A navegação do Braze é projetada para ajudá-lo a acessar eficientemente recursos e conteúdos em diferentes dispositivos. Existem dois níveis de navegação no dashboard do Braze: cabeçalho global e navegação lateral.

O cabeçalho global está quase sempre visível na parte superior da tela. Ele fornece acesso rápido a ferramentas e configurações essenciais, incluindo:

- Pesquisar
- Links de suporte e comunidade
- [Idioma do dashboard]({{site.baseurl}}/user_guide/administrative/access_braze/language/)
- Notificações
- Configurações da conta
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/)

### Use a navegação lateral

O menu vertical à esquerda organiza as ferramentas do Braze por função e mantém seus itens mais usados ao alcance. Selecione um item do menu principal para revelar suas opções em um layout vertical empilhado. 

![Alternador de espaço de trabalho no dashboard do Braze]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### Alternador de espaço de trabalho

Localizado na parte superior da navegação lateral, o alternador de espaço de trabalho permite que você mude entre diferentes espaços de trabalho na sua instância do Braze. O espaço de trabalho ativo está destacado.

[Espaços de trabalho]({{site.baseurl}}/user_guide/getting_started/workspaces) ajudam a organizar o conteúdo por marca, região, linha de produto ou equipe. Cada espaço de trabalho inclui seus próprios dados, campanhas e configurações. Seu acesso pode variar entre os espaços de trabalho. Por exemplo, você pode ter acesso de edição em um espaço de trabalho e acesso somente de visualização em outro.

Para alternar espaços de trabalho, selecione o menu suspenso de espaço de trabalho na parte superior da navegação lateral e escolha o espaço de trabalho que deseja acessar. Você também pode [adicionar espaços de trabalho favoritos](#adding-favorite-workspaces) para acesso mais rápido aos que você usa com mais frequência.

#### Minimize a navegação lateral

Para reduzir a desordem visual, especialmente durante tarefas como projetar um canva, você pode minimizar o painel de navegação lateral. Pressione **Minimizar menu** para colapsá-lo. Mesmo quando minimizado, passe o mouse sobre qualquer ícone para ver dicas de ferramentas com os nomes dos itens do menu. Isso ajuda você a se mover rapidamente entre as ferramentas enquanto mantém seu espaço de trabalho limpo.

![Minimizar e maximizar ícones de menu]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### Navegação responsiva

A navegação se adapta perfeitamente a diferentes tamanhos de tela. Em telas menores, a navegação lateral colapsa automaticamente. Pressione <i class="fa-solid fa-bars" aria-label="Abrir menu de navegação"></i> para abrir o menu quando necessário. 

![Em telas menores, a navegação lateral colapsa automaticamente. Tocar no ícone do menu abre as opções de navegação.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## Pesquise seu dashboard

A barra de pesquisa global, localizada no cabeçalho, é a maneira mais rápida de encontrar conteúdo em seu dashboard Braze. Selecione para abrir a interface de pesquisa e ir diretamente ao que você precisa. 

![Pesquisa global aberta sem termos de pesquisa inseridos, mostrando páginas recentemente abertas.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

Seu conteúdo recentemente aberto aparece abaixo da barra de pesquisa. Isso inclui qualquer campanha, canva, modelo ou página com a qual você interagiu recentemente—facilitando o retorno ao seu trabalho.

### O que você pode pesquisar?

Você pode pesquisar os seguintes itens e ações:

- Nomes de campanhas
- Nomes de telas
- Blocos de conteúdo
- Nomes de segmentos
- Nomes de modelos de e-mail
- Páginas dentro do Braze (incluindo sinônimos)

{% alert tip %}
Para pesquisar o texto exato, coloque o termo de pesquisa entre aspas (""). Por exemplo, pesquisar por [“todos os usuários”] retornará todos os itens que contêm a frase exata “todos os usuários” em seu nome.
{% endalert %}

### Tipo de conteúdo e tags de status

Cada resultado é rotulado com uma tag indicando seu tipo de conteúdo—como campanha, canva ou segmento—e seu status (ativo, arquivado, parado).

### Filtro para conteúdo ativo e de rascunho

Por padrão, a pesquisa inclui itens ativos, rascunhos e arquivados. Use o **Mostrar apenas ativos e rascunhos** para restringir seus resultados.

![O botão de alternância "Mostrar somente ativos e rascunhos".]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### Atalhos de teclado

Você pode navegar pelos resultados da pesquisa usando seu teclado.

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2), {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| Ação                      | Atalho de teclado                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| Abra o menu de pesquisa        | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd> + <kbd>K</kbd> </li> <li>Windows: <kbd>Ctrl</kbd> + <kbd>K</kbd> </li> </ul> {:/}  |
| Mover-se entre os resultados da pesquisa | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| Selecione um resultado de pesquisa      | <kbd>Entrar</kbd>    |
| Fechar o menu de pesquisa       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Dicas

O dashboard do Braze inclui vários recursos para ajudá-lo a trabalhar de forma mais eficiente e acessar rapidamente as ferramentas e conteúdos que você mais usa.

### Continuar de onde parou

Na página **Início**, o dashboard exibe suas campanhas, canva e segmentos recentemente editados ou criados. Isso facilita voltar ao trabalho em andamento sem precisar pesquisar. Cada item inclui tags mostrando o tipo de conteúdo e status (como rascunho, ativo ou parado).

![Um rascunho do Canva, um segmento ativo e um rascunho de campanha na seção "Continue de onde parou".]({% image_buster /assets/img/pick_up_where_you_left_off.png %})

Para saber mais, veja [dashboard de Início]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off).

### Adicionar espaços de trabalho favoritos

Se você trabalha em vários espaços de trabalho, pode marcar os que usa com mais frequência como favoritos para acesso mais rápido. Para adicionar espaços de trabalho favoritos, [acesse suas configurações de perfil](#accessing-your-profile-settings), localize o campo **Espaços de trabalho favoritos** na seção **Perfil da Conta** e selecione os espaços de trabalho que deseja favoritar. Seus espaços de trabalho favoritos aparecerão no topo do seletor de espaços de trabalho para acesso rápido.

### Acesse suas configurações de perfil

Para gerenciar suas configurações de conta, preferências de notificação e informações pessoais:

1. Selecione seu ícone de perfil no cabeçalho global.
2. Selecione **Gerenciar sua conta** para acessar sua página de perfil.

Na sua página de perfil, você pode atualizar suas configurações de e-mail, configurar a autenticação de dois fatores, visualizar suas chaves de API e gerenciar outros detalhes da conta.

## Acessibilidade no dashboard

O painel do Braze usa cores de marca que atendem aos padrões WCAG AA para contraste de cores. Isso apoia uma experiência inclusiva para todos os usuários e está alinhado com as melhores práticas de acessibilidade.

## Compartilhando feedback

Quer nos contar o que você pensa? Você pode compartilhar feedback sobre navegação, acessibilidade, usabilidade, design visual e mais. Abra o menu **Suporte** no cabeçalho global e selecione **Compartilhar feedback**. Revisamos todo o feedback para ajudar a melhorar sua experiência com o Braze.

## Recursos relacionados

### Tarefas administrativas

- [Criar e gerenciar espaços de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/)
- [Gerenciar usuários do Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/)
- [Permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)
- [Equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)

### Tarefas principais e próximos passos

- **Construir campanhas**: [Criar uma campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/)
- **Criar jornadas**: [Construir um Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- **Definir públicos**: [Criar um segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)
- **Revisar desempenho**: [Visão geral da análise de dados]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/)
- **Configurar configurações**: [Configurações do app]({{site.baseurl}}/user_guide/administrative/app_settings/)


