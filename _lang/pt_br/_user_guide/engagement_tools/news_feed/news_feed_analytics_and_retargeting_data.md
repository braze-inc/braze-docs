---
nav_title: Análise de dados do feed de notícias
article_title: Análise de dados e análises do feed de notícias e dados de redirecionamento
page_order: 10
page_type: reference
description: "Este artigo de referência aborda a análise de dados do Feed de notícias e vários filtros relacionados."
tool: 
- Reports
channel: news feed
hidden: true

---

# Análise de dados do feed de notícias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Semelhante às campanhas programadas, a ferramenta Feed de notícias vem com um dashboard de análise de dados para monitorar impressões, cliques e taxas de cliques. Ao clicar em uma mensagem específica do Feed de notícias em seu dashboard, uma série de análises de dados visuais são exibidas. 

Na parte superior da página, você pode selecionar o intervalo de datas dos dados e ver uma visualização rápida das métricas mais importantes. Além disso, você pode ver detalhes específicos sobre essa mensagem do Feed de notícias, como quando ela foi enviada e para quem foi enviada.

![Detalhes e análises de dados do Feed de notícias.][19]

Ao rolar a página para baixo, você pode ver um detalhamento maior de seus cliques e impressões dia a dia. O total de cliques/impressões é facilmente comparado com cliques e impressões exclusivos por meio de gráficos de linha, enquanto a taxa de cliques é apresentada como um gráfico de barras interativo.

![Gráfico de decomposição da performance.][20]

## Dados de redirecionamento

É possível aproveitar os dados do Braze sobre quais usuários estão interagindo com seu Feed de notícias por meio de filtros de segmento que permitem redirecionar comportamentos específicos.

### Filtro de impressão de feed

O Braze rastreia automaticamente quando os usuários visualizam o feed e quantas vezes eles o visualizaram. Há dois filtros disponíveis:

- Última visualização do feed de notícias
- Contagem de visualizações do feed de notícias

**O Feed de notícias visualizado pela última vez** é uma maneira eficaz de usar outros canais para atrair os usuários de volta ao feed. Isso pode ser feito facilmente com notificações por push e no app. A Braze registrou aumentos de mais de 100% nas impressões do feed de notícias com um direcionamento eficaz. À medida que a conscientização sobre o feed aumenta, esses benefícios são mantidos.

**A contagem de visualizações do feed de notícias** pode ser usada para direcionamento a usuários que nunca visualizaram o feed ou que raramente visualizam o feed para incentivar mais impressões de seus cartões.

Considere a possibilidade de usar esses filtros em conjunto ou com outros filtros para criar uma chamada à ação ainda mais direcionada.

### Filtro de cartão clicado

É possível criar segmentos com base em como os usuários interagiram com cartões específicos no feed. O filtro está na seção Redirecionamento da lista de filtros e se chama cartão clicado.

### Clicou no filtro do cartão

- Funciona bem para redirecionar usuários que clicaram em um cartão, mas não seguiram sua chamada para ação.
- Também é útil redirecionar os usuários com conteúdo relacionado que possa ser do interesse deles.
- Também é possível usar esse filtro para direcionamento de usuários que não clicaram em um cartão. Esse filtro pode ser aplicado a cartões específicos para que eles desapareçam do feed do usuário depois que ele clicar neles.
  - Para configurar isso, depois de criar um cartão, volte e edite o segmento de direcionamento para incluir **Não clicou**.
  - Depois que um usuário clicar no cartão, ele sairá automaticamente do feed quando a próxima sessão do usuário for iniciada.
  - Evite o uso excessivo desse direcionamento, pois os usuários podem acabar com feeds vazios. A prática recomendada é usar uma combinação de conteúdo estático e removido automaticamente.
- Ele também funciona bem para redirecionar os usuários que não clicam em um cartão para fazer o acompanhamento com outra chamada para ação.

![Exemplo de filtro de segmento que mostra os usuários-alvo que não clicaram no cartão "Cheers! O que fazer e o que não fazer ao fazer um brinde".][14]


[19]: {% image_buster /assets/img_archive/braze_newsfeedanalytics.png %}
[20]: {% image_buster /assets/img_archive/braze_newsfeedanalytics2.png %}
[14]: {% image_buster /assets/img_archive/braze_newsfeedsegment.png %}
