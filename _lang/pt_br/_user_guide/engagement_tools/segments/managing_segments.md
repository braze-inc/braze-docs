---
nav_title: Gerenciamento de segmentos
article_title: Gerenciamento de segmentos
page_order: 1
page_type: tutorial
tool: Segments
description: "Este artigo aborda as ações que você pode executar para gerenciar seus segmentos, como filtrar uma lista de segmentos, criar segmentos e editar segmentos."

---

# Gerenciamento de segmentos

> A seção Segments (Segmentos) permite visualizar uma lista abrangente dos segmentos existentes, criar novos segmentos e editar segmentos existentes. Você pode refinar a lista de segmentos selecionando uma variedade de filtros e colunas para que apenas as informações mais relevantes para você sejam exibidas.

\![A seção Segmentos exibe uma lista de segmentos ativos.]({% image_buster /assets/img/segment/segments_page.png %})

## Personalizando sua visualização

Adapte sua visualização da lista de segmentos usando filtros e alterando as colunas que você deseja que apareçam. Quando você sair da seção **Segmentos** e retornar, a lista será revertida para a visualização padrão, limpando todos os filtros selecionados anteriormente.

### Filtro de status

Você pode restringir a lista para exibir apenas segmentos ativos ou arquivados. Qualquer segmento não arquivado é considerado ativo.

### Filtros

Classifique os segmentos na lista ajustando os seguintes filtros:
- **Última edição por:** O usuário que editou os segmentos pela última vez
- **Última edição:** Intervalo de tempo no qual os segmentos foram editados pela última vez
- **Tamanho estimado:** Faixa aproximada de quantos usuários estão nos segmentos
- **Tags:** Tags associadas aos segmentos
- **Equipes:** Equipes associadas aos segmentos
- **Somente segmentos de rastreamento avançado:** Visualize apenas os segmentos que têm [o Analytics Tracking]({{site.baseurl}}/user_guide/data_and_analytics/tracking/segment_analytics_tracking#segment-analytics-tracking) ativado.

### Colunas

Essas são as colunas de informações que você pode selecionar para exibir na lista de segmentos:
- **Filtros:** Número de filtros no segmento
- **Última edição:** Data em que o segmento foi editado pela última vez
- **Última edição por:** O usuário que editou o segmento pela última vez
- **Tags:** Tags associadas ao segmento
- **Equipes:** Equipes associadas ao segmento
- **Tamanho estimado:** Número estimado de usuários no segmento
- **Telas:** Número de telas que usam o segmento
- **Campanhas:** Número de campanhas que usam o segmento

### Mostrar somente com estrela

A seleção de **Show Starred Only** restringe sua visualização aos segmentos que foram marcados com estrela por você.

## Visualização do uso de mensagens de um segmento

Vá para a seção **Messaging Use (Uso de mensagens)** de um segmento para obter uma visão geral de onde o segmento está sendo usado, como em outros segmentos, campanhas e Canvases.

{% alert note %}
Para evitar loops de segmentos que fazem referência uns aos outros, os segmentos que usam o filtro **Segment Membership** não podem ser referenciados por outros segmentos. Para obter mais detalhes, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/).
{% endalert %}

## Gerenciamento de segmentos específicos

O menu de edição de um segmento mostra as opções "Editar", "Duplicar", "Arquivar" e "Adicionar aos favoritos".]({% image_buster /assets/img/segment/segments_page_edit_menu.png %}){: style="float:right;max-width:25%;"}

Para gerenciar um segmento específico, passe o mouse sobre ele e selecione o ícone de menu no final da linha para revelar as seguintes opções:
- **Editar:** Edite os filtros em seu segmento.
- **Duplicado:** Faça uma cópia de seu segmento.
- **Arquivo:** Arquivar o segmento. Observe que isso também arquivará todas as campanhas ou Canvases que usam esse segmento.
- **Adicionar aos favoritos:** Marque o segmento com estrela, o que lhe permite acessá-lo rapidamente marcando a caixa Show starred only (Mostrar somente com estrela) na seção de segmentos.
 
Você também pode executar ações em massa - especificamente, arquivamento em massa e marcação em massa - marcando as caixas ao lado de vários nomes de segmentos.

Vários segmentos selecionados com "CRM" selecionado no campo suspenso "Tag As".]({% image_buster /assets/img/segment/segments_bulk_action.png %}){: style="max-width:45%;"}

### Alterações desde a última visualização

O número de atualizações dos segmentos feitas por outros membros da sua equipe é rastreado pela métrica *Changes Since Last Viewed (Alterações desde a última visualização)* na página de visão geral do segmento. Selecione **Changes Since Last Viewed (Alterações desde a última visualização** ) para ver um registro de alterações das atualizações do nome, da descrição e do público-alvo do segmento. Para cada atualização, você pode ver quem realizou a atualização e quando. Você pode usar esse registro de alterações para auditar as alterações em seu segmento.

## Busca de segmentos
Pesquise nomes de segmentos inserindo termos no campo de pesquisa. 

Todos os termos e cadeias de caracteres inseridos nesse campo serão pesquisados. Por exemplo, a busca por "test segment 1" retornará segmentos com "test", "segment" ou "1" em qualquer parte do nome. Para pesquisar uma cadeia de caracteres exata, coloque aspas ao redor do termo de pesquisa. A pesquisa por ["test segment 1"] retornará todos os segmentos que contêm a frase exata "test segment 1" em seu nome.

Os resultados da pesquisa ao inserir "todos os usuários" no campo de pesquisa incluem "Todos os usuários (teste)", "Todos os usuários", "Todos os usuários 15".]({% image_buster /assets/img/segment/segments_search.png %})

