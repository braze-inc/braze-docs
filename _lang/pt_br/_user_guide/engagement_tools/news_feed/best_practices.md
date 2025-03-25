---
nav_title: Práticas recomendadas
article_title: Práticas recomendadas do feed de notícias
page_order: 20
page_type: reference
description: "Este artigo apresenta as práticas recomendadas para projetar e personalizar cartões de feed de notícias."
channel: news feed
hidden: true

---

# Práticas recomendadas do feed de notícias

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> O feed de notícias do Braze é um fluxo dinâmico e direcionado de conteúdo rico. Ele oferece uma maneira eficiente de alcançar os usuários com conteúdo continuamente atualizado que não exige trabalho de desenvolvimento adicional. Esse conteúdo pode ser direcionado a vários segmentos e programado da mesma forma que outras mensagens do Braze. Cada cartão consiste em um título, um resumo, uma imagem e, opcionalmente, um URL. O feed também inclui a capacidade de fazer deep linking dentro do app, fazer link diretamente para a App Store, Google Play, etc. ou direcionar os usuários para uma visualização na Web. Esse elemento exclusivo da interface do usuário do Braze deve ser ativado durante a [integração][1]. Não deixe de discutir isso com seus desenvolvedores.

Para saber mais sobre os diferentes tipos de cartões do Feed de notícias, como criá-los, casos de uso, bem como especificações de cartões e imagens, leia nossa página sobre [criação de itens do Feed de notícias][4].

> A Braze melhora o tempo de carregamento usando um CDN global para hospedar todas as imagens do feed de notícias.

## Práticas recomendadas {#news-feed-best-practices}

Na Braze, valorizamos a personalização que o Feed de notícias oferece. Aqui estão algumas de nossas práticas recomendadas e dicas para ajudá-lo a tirar o máximo proveito do Braze.

### Torne-o atraente

Quanto mais notável, relevante e interessante for seu Feed de notícias, maior será a probabilidade de ele ser visto por outras pessoas.  

- Use o Feed de notícias para ajudar a fazer com que seu app pareça dinâmico e atualizado regularmente, exibindo novos conteúdos.
- Diversifique o tipo de anúncios de cartões modelados para manter o feed de notícias interessante
- Aproveite o espaço visual incorporando imagens e gráficos que se destaquem.

### Torne-o pessoal

As empresas e seus usuários adoram e valorizam a personalização.

- Personalize o Feed de notícias para refletir a identidade de sua marca e criar uma experiência perfeita no app.
- Lembre-se de que os módulos direcionados podem inspirar imediatamente a ação dentro do app, e os URLs de protocolo podem direcionar a atenção para diferentes seções do app, incentivando comportamentos específicos, como avaliações, compras e muito mais.
- Segmente os usuários e adapte determinados anúncios para inspirar ações específicas.

### Torne-o útil

O conteúdo que você escolhe mostrar no Feed de notícias pode variar muito e trabalhar em conjunto com as campanhas.  

- Forneça anúncios que incentivem a interação, destaquem as novidades e promovam as vendas.
- Desenvolva um cronograma para campanhas, como integração etc., e determine a cadência e a frequência adequadas do envio de mensagens.
- Fortaleça e reforce as campanhas de mensagens integrando outras mensagens em vários canais no feed de notícias

## Exemplo de integração

O 1-800-Flowers.com usa o Feed de notícias para fornecer informações relevantes aos seus usuários. A integração do SDK permanece totalmente transparente: não há nenhuma menção ao Braze no próprio aplicativo e o módulo Feed de notícias tem uma estética de design consistente com o restante do app.

![shapefeed][2]{: style="max-width:50%;"}

Você pode ver mais exemplos de feeds de notícias em nossos [Estudos de caso][3].

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/news_feed/
[2]: {% image_buster /assets/img_archive/18F_newsfeed.png %}
Daqui a [3]: https://www.braze.com/customers
[4]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/
