---
nav_title: Push para web em dispositivos móveis no Safari
article_title: Push para web em dispositivos móveis no Safari
platform: Web
channel: push
page_order: 5
page_type: reference
description: "Este artigo de referência aborda como integrar o web push em seus navegadores Safari para iOS e iPad."
search_rank: 3
---

# Push para web em dispositivos móveis no Safari (iOS e iPadOS)

> [O Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) é compatível com web push para dispositivos móveis, o que significa que agora é possível reengajar usuários móveis com notificações por push no iOS e iPadOS.<br><br>Este artigo detalhará as etapas necessárias para configurar o push em dispositivos móveis para o Safari.

## Etapas de integração

Primeiro, leia e siga nosso [guia padrão de integração de push para web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/). As etapas a seguir são necessárias apenas para oferecer suporte a web push no Safari para iOS e iPadOS.

### Etapa 1: Criar um arquivo de manifesto {#manifest}

Um [Manifesto de Aplicativo Web](https://developer.mozilla.org/en-US/docs/Web/Manifest) é um arquivo JSON que controla como o seu site é apresentado quando instalado na tela inicial de um usuário.

Por exemplo, é possível definir a cor do tema de fundo e o ícone que o [App Switcher](https://support.apple.com/en-us/HT202070) usa, se ele é renderizado em tela inteira para se assemelhar a um aplicativo nativo ou se o aplicativo deve ser aberto no modo paisagem ou retrato.

Crie um novo arquivo `manifest.json` no diretório raiz do seu site, com os seguintes campos obrigatórios. 

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

A lista completa de campos suportados pode ser encontrada [aqui](https://developer.mozilla.org/en-US/docs/Web/Manifest).

### Etapa 2: Vincular o arquivo de manifesto {#manifest-link}

Adicione a seguinte tag `<link>` ao elemento `<head>` de seu site, apontando para o local onde o arquivo de manifesto está hospedado.

```html
<link rel="manifest" href="/manifest.json" />
```

### Etapa 3: Adicionar um service worker{#service-worker}

Seu site precisa ter um arquivo de service worker que importe a biblioteca de service worker da Braze, conforme descrito em nosso [guia de integração de push para web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-1-configure-your-sites-service-worker).

### Etapa 4: Adicionar à tela inicial {#add-to-homescreen}

Ao contrário dos principais navegadores, como Chrome e Firefox, não é possível solicitar permissão push no Safari iOS/iPadOS, a menos que seu site tenha sido adicionado à tela inicial do usuário. 

O recurso [Add to Homescreen](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) permite que os usuários marquem seu site como favorito, adicionando seu ícone ao valioso espaço da tela inicial deles.

![Um iPhone mostrando opções para marcar um site como favorito e salvá-lo na tela inicial]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Etapa 5: Mostrar o prompt push nativo {#push-prompt}
Depois que o app tiver sido adicionado à sua tela inicial, agora é possível solicitar permissão de push quando o usuário realizar uma ação (como clicar em um botão). Isso pode ser feito usando o método [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) ou com uma [mensagem no app sem código push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).

{% alert note %}
Depois de aceitar ou recusar a solicitação, você precisará excluir e reinstalar o site na tela inicial para poder exibir a solicitação novamente.
{% endalert %}

![Um prompt push pedindo para "permitir" ou "não permitir" notificações]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

Por exemplo:

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```


## Próximas etapas

Em seguida, envie a si mesmo uma [mensagem de teste]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) para validar a integração. Depois que sua integração estiver concluída, você poderá usar nossas [mensagens push primárias sem código]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/) para otimizar suas taxas de aceitação push.

