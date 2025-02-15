---
nav_title: Categorias do feed de notícias
page_order: 9

page_type: reference
description: "Este artigo de referência descreve as categorias do feed de notícias, que possibilitam a integração de várias instâncias do feed de notícias em seu aplicativo."
tool: Dashboard
channel: news feed
hidden: true

---

# Categorias do feed de notícias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> As categorias do Feed de notícias possibilitam a integração de várias instâncias do Feed de notícias em seu aplicativo. É possível integrar feeds em diferentes janelas que exibem apenas cartões do Feed de notícias de uma determinada categoria.

![O painel do Feed de notícias com uma prévia do cartão de imagem legendada para um item do Feed de notícias intitulado "Sweet Teeth - Buy candy in bulk!" (Dentes doces - Compre doces em massa!) com a mensagem "Satisfaça sua vontade de comer doces e passe em nossa loja! Mencione este anúncio e ganhe 50% de desconto em seu primeiro saco de doces." Há quatro caixas de seleção de categorias do Feed de notícias: Notícias, anúncios, publicidade e social. Nenhuma das categorias é selecionada.][1]

A marcação de um Feed de notícias como sendo de uma categoria específica não é visível para o usuário final. Por padrão, o feed de notícias do Braze exibirá cartões de todas as categorias, a menos que um feed seja especificamente configurado no código do app para exibir categorias específicas. Para saber mais sobre a configuração do código do app, consulte [Definição de uma categoria de feed de notícias][2].

[1]: {% image_buster /assets/img_archive/Newsfeed_category.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/defining_a_news_feed_category/
