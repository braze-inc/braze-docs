---
nav_title: Suporte AMP
article_title: Suporte AMP para a Web
platform: Web
page_order: 5
page_type: reference
description: "Este artigo de referência descreve o suporte da AMP para a Web e como integrar a Braze em uma página AMP."

---

# Suporte a AMP

{% alert note %}
Não é necessário integrar essa seção, a menos que esteja tentando integrar a Braze em uma página AMP.
{% endalert %}

> Este artigo de referência descreve o suporte da AMP para a Web e como integrar a Braze em uma página AMP. O Accelerated Mobile Pages (AMP) é um projeto apoiado pelo Google, criado para melhorar o tempo de carregamento de páginas em dispositivos móveis, aplicando determinados padrões, incluindo a restrição do uso de JavaScript.

Como resultado, o SDK da Braze não pode ser carregado em uma página AMP. No entanto, o projeto AMP fornece um componente compatível com push para web. As [instruções a seguir](https://www.ampproject.org/docs/reference/components/amp-web-push) detalham como configurar esse componente e fazem referência à documentação a seguir sobre o componente `amp-web-push`.

## Etapa 1: Incluir script de push para web de AMP

Adicione a seguinte tag de script assíncrono em seu cabeçalho:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

## Etapa 2: Adicionar um widget de inscrição e cancelamento de inscrição

Será necessário adicionar um widget que permita que os usuários assinem e cancelem a inscrição no push. Ele deve ficar dentro do corpo do seu HTML e pode ser estilizado da maneira que você achar melhor.

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

## Etapa 3: Baixe o iFrame auxiliar e a caixa de diálogo de permissão

O componente AMP Web Push funciona criando um pop-up que lida com a inscrição push. Como resultado, você precisará incluir alguns arquivos auxiliares em seu projeto. Baixe o arquivo [helper-iframe.html](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html) e o arquivo [permission-dialog.html](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html) e armazene-os em seu site.

## Etapa 4: Criar um arquivo de service worker

Crie um arquivo `service-worker.js` com o seguinte conteúdo e coloque-o no diretório raiz do seu site:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Etapa 5: Configurar o elemento HTML do AMP web push

Agora você precisará adicionar o elemento HTML `amp-web-push` à sua página. Insira o seguinte código HTML no corpo de seu documento:

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```

Em particular, o `service-worker-URL` exige que você anexe os endereços `apiKey` e `baseUrl` (https://dev.appboy.com/api/v3) como parâmetros de consulta.

Agora você deve estar configurado para inscrição e cancelamento de inscrição push em sua página AMP.
