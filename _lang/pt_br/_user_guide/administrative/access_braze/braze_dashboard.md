---
nav_title: O dashboard
article_title: Painel de controle do Braze
page_order: 2
page_type: reference
description: "O dashboard do Braze é seu espaço de trabalho central para criar, gerenciar e analisar o engajamento do cliente. Ele reúne ferramentas de envio de mensagens, insights de segmento, segmentação e dados de performance em tempo real em um só lugar."

---

# Painel de controle do Braze

> O dashboard do Braze é nossa interface da web em [dashboard.braze.com](https://dashboard.braze.com/) ou [dashboard.braze.eu](https://dashboard.braze.eu/)

Use o dashboard do Braze para planejar campanhas, lançar e gerenciar mensagens, explorar insights de público, ajustar a segmentação e analisar métricas de desempenho e engajamento em tempo real a partir de uma única interface.

## Acesse seu dashboard

Para começar, faça [login em sua conta Braze]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account). Seu acesso às páginas do dashboard e a permissão para executar determinadas ações são baseados nas [permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) atribuídas. Se precisar de ajuda com suas permissões, entre em contato com os administradores do Braze.

## Navegar no Braze

A navegação do Braze foi projetada para ajudá-lo a acessar com eficiência os recursos e o conteúdo em todos os dispositivos. Há dois níveis de navegação no dashboard do Braze: cabeçalho global e navegação lateral.

O cabeçalho global está quase sempre visível na parte superior da tela. Ele oferece acesso rápido a ferramentas e configurações essenciais, incluindo:

- Pesquisar
- Suporte e vínculos com a comunidade
- [Idioma do dashboard]({{site.baseurl}}/user_guide/administrative/access_braze/language/)
- Notificações
- Configurações da conta
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/)

### Usando a navegação lateral

O menu vertical à esquerda organiza as ferramentas Braze por função e mantém seus itens mais usados ao alcance de suas mãos. Selecione um item do menu principal para revelar suas opções em um layout vertical empilhado. 

![Alternador de espaço de trabalho no dashboard do Braze]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### Alternador de espaço de trabalho

Localizado na parte superior da navegação lateral, o alternador de espaço de trabalho permite que você se mova entre diferentes espaços de trabalho em sua instância do Braze. O espaço de trabalho ativo é destacado.

[Os espaços de trabalho]({{site.baseurl}}/user_guide/getting_started/workspaces) ajudam a organizar o conteúdo por marca, região, linha de produtos ou equipe. Cada espaço de trabalho inclui seus próprios dados, campanhas e configurações. Seu acesso pode variar entre os espaços de trabalho. Por exemplo, você pode ter acesso de edição em um espaço de trabalho e acesso somente de visualização em outro.

#### Minimizar a navegação lateral

Para reduzir a confusão visual, especialmente durante tarefas como projetar um Canva, você pode minimizar o painel de navegação lateral. Pressione **o menu Minimizar** para recolhê-lo. Mesmo quando minimizado, passe o mouse sobre qualquer ícone para exibir dicas de ferramentas com os nomes dos itens de menu. Isso o ajuda a alternar rapidamente entre as ferramentas e a manter o espaço de trabalho limpo.

![Minimizar e maximizar os ícones do menu]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### Navegação responsiva

A navegação se adapta perfeitamente a diferentes tamanhos de tela. Em telas menores, a navegação lateral é recolhida automaticamente. Pressione <i class="fa-solid fa-bars" aria-label="Abrir menu de navegação"></i> para abrir o menu quando necessário. 

![Em telas menores, a navegação lateral é recolhida automaticamente. Tocar no ícone do menu abre as opções de navegação.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## Pesquise em seu dashboard

A barra de pesquisa global, localizada no cabeçalho, é a maneira mais rápida de encontrar conteúdo em seu dashboard do Braze. Selecione para abrir a interface de pesquisa e ir diretamente para o que você precisa. 

![Pesquisa global aberta sem termos de pesquisa inseridos, mostrando as páginas abertas recentemente.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

Seu conteúdo aberto recentemente aparece abaixo da barra de pesquisa. Isso inclui qualquer campanha, Canva, modelo ou página com os quais tenha interagido recentemente, facilitando o retorno ao seu trabalho.

### O que você pode pesquisar?

Você pode pesquisar os seguintes itens e ações:

- Nomes de campanhas
- Nomes de telas
- Blocos de conteúdo
- Nomes de segmentos
- Nomes de modelos de e-mail
- Páginas dentro de Braze (incluindo sinônimos)

{% alert tip %}
Para pesquisar o texto exato, coloque o termo de pesquisa entre aspas (""). Por exemplo, a pesquisa por ["all users"] retornará todos os itens que contêm a frase exata "all users" em seu nome.
{% endalert %}

### Tipo de conteúdo e tags de status

Cada resultado é rotulado com uma tag que indica seu tipo de conteúdo - como campanha, Canva ou segmento - e seu status (ativo, arquivado, parado).

### Filtro para conteúdo ativo e de rascunho

Por padrão, a pesquisa inclui itens ativos, de rascunho e arquivados. Use a opção **Mostrar somente ativos e rascunhos** para restringir seus resultados.

![O botão de alternância "Mostrar somente ativos e rascunhos".]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### Atalhos de teclado

Você pode navegar pelos resultados da pesquisa usando o teclado.

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


## Acessibilidade no dashboard

O dashboard do Braze usa cores da marca que atendem aos padrões WCAG AA para contraste de cores. Isso favorece uma experiência inclusiva para todos os usuários e se alinha às práticas recomendadas de acessibilidade.

## Compartilhamento de feedback

Quer nos dizer o que achou? Você pode compartilhar feedback sobre navegação, acessibilidade, usabilidade, design visual e muito mais. Abra o menu **Suporte** no cabeçalho global e selecione **Compartilhar feedback**. Analisamos todos os comentários para ajudar a melhorar sua experiência no Braze.


