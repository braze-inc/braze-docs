---
nav_title: Pesquisando em seu dashboard do Braze
article_title: Pesquisando em seu dashboard do Braze
page_order: 0.5
page_type: reference
description: "Saiba mais sobre a pesquisa global no Braze."
---

# Pesquisando em seu dashboard do Braze

Você pode usar a barra de pesquisa para encontrar seu trabalho e outras informações em seu dashboard do Braze. A barra de pesquisa está na parte superior de seu dashboard da Braze. Clique na barra de pesquisa ou pressione <kbd>Ctrl</kbd> + <kbd>K</kbd> no Windows ou <kbd>⌘</kbd> + <kbd>K</kbd> no Mac para ir diretamente para a barra de pesquisa.

![][3]

## O que você pode pesquisar?

Você pode pesquisar os seguintes itens e ações:

- Nomes de campanhas
- Nomes de telas
- Blocos de conteúdo
- Nomes de segmentos
- Nomes de modelos de e-mail
- [Páginas da Braze](#find-pages-that-have-been-renamed)

{% alert tip %}
Para pesquisar o texto exato, coloque o termo de pesquisa entre aspas (""). Por exemplo, a pesquisa por ["todos os usuários"] retornará todos os itens que contêm a frase exata "todos os usuários" em seu nome.
{% endalert %}

## Principais recursos

### Atalhos de teclado

Navegue pelos resultados da pesquisa sem esforço com atalhos de teclado:

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

### Tipo de conteúdo e tags de status

Cada resultado de pesquisa é associado a tags que indicam o tipo de conteúdo do resultado (página, campanha, Canva, segmento, modelo de e-mail) e o status (ativo, arquivado, parado etc.).

### Acessar conteúdo aberto recentemente

Você pode revisitar o conteúdo acessado recentemente no menu de pesquisa. A interface de pesquisa exibe seus resultados abertos recentemente abaixo da barra de pesquisa, incluindo itens com os quais interagiu em toda a plataforma Braze. Isso permite que você retorne a páginas, campanhas, Canvas, segmentos ou modelos de e-mail visualizados anteriormente, para que possa continuar de onde parou com menos cliques.

![][1]

### Localizar páginas que foram renomeadas

A pesquisa compreende sinônimos para páginas que foram renomeadas em nossa [navegação atualizada]({{site.baseurl}}/navigation). Por exemplo, ele encontrará "Exportação de Dados" quando você pesquisar "Currents", pois essa página foi renomeada.

<!---

### Quick create campaigns

Search for channels to see quick create options among your top 10 results. For example, searching for "email" shows "Create Email Campaign" or "Create Transactional Email Campaign".

![][2]

--->

### Filtro para conteúdo ativo e de rascunho

Você pode incluir conteúdo ativo e de rascunho nos resultados da pesquisa selecionando **Mostrar somente ativo e de rascunho**. Por padrão, a alternância está ativada e todo o conteúdo, inclusive o arquivado, é mostrado.

![O botão de alternância "Mostrar somente ativos e rascunhos".][4]

### Pesquisar emojis

Você usa emojis ao nomear seu trabalho no Braze? Procure por eles! Você pode usar emojis como consultas de pesquisa. 😎


[1]: {% image_buster /assets/img/global_search/global_search.png %}
[2]: {% image_buster /assets/img/global_search/search_create_campaign.png %}
[3]: {% image_buster /assets/img/global_search/global_search2.png %}
[4]: {% image_buster /assets/img/global_search/show_active_draft.png %}
