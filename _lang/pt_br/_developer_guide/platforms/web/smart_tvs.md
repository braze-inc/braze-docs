---
nav_title: Suporte a Smart TV
article_title: Suporte de Smart TV para o SDK do Braze
platform: Web
page_order: 30
description: "Este artigo aborda como usar o SDK da Braze para Web para integrar com Smart TVs (Samsung e LG)."

---

# Suporte a Smart TV

> O SDK da Braze para Web permite que você colete análises de dados e exiba mensagens Rich no app e mensagens de cartão de conteúdo para usuários de smart TV, incluindo [TVs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) e [TVs LG (webOS)](https://webostv.developer.lge.com/discover). Este artigo aborda como usar o SDK da Braze para Web para integrar com Smart TVs.

{% alert tip %}
Para uma referência técnica completa, confira nossa [Documentação JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) ou nossos [aplicativos de exemplo](https://github.com/Appboy/smart-tv-sample-apps) para ver o Web SDK rodando em uma TV.
{% endalert %}

 %} developer_guide/prerequisites/web.md

## Configuração do SDK do Braze

Existem duas mudanças necessárias ao integrar com Smart TVs:

1. Ao baixar ou importar o Web SDK, use o pacote "core" (disponível em `https://js.appboycdn.com/web-sdk/x.y/braze.core.min.js`, onde `x.y` é a versão desejada). Recomendamos usar a versão CDN do nosso SDK Web, já que a versão NPM é escrita em módulos ES nativos, enquanto a versão CDN é transpilada para ES5. Se você preferir usar a [versão NPM](https://www.npmjs.com/package/@braze/web-sdk), use um empacotador como o webpack que removerá o código não utilizado e que o código seja transpilado para ES5.
2. Ao inicializar o SDK da Web, você precisa definir as opções de inicialização `disablePushTokenMaintenance` e `manageServiceWorkerExternally` para `true`.

## Análise de dados

Todos os mesmos métodos do SDK da Web para análise de dados podem ser usados em Smart TVs. Para obter um passo a passo completo sobre o rastreamento de eventos personalizados, atributos personalizados e muito mais, consulte [Análise de dados]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web).

## Mensagens no app e Cartões de Conteúdo

O SDK da Braze para Web aceita tanto [mensagens no app]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=web) quanto [cartões de conteúdo]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web) em Smart TVs. Nota que você deve usar o ["Core" Web SDK](https://www.npmjs.com/package/@braze/web-sdk) pois a renderização de mensagens no app e Cartões de Conteúdo não é suportada usando nossa exibição padrão de UI e deve ser personalizada pelo seu app para se encaixar na experiência do seu App de TV.

Para saber mais sobre como o aplicativo da Smart TV pode receber e exibir mensagens no app, consulte [Envio de mensagens]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web).
