{% multi_lang_include developer_guide/prerequisites/web.md %} Você também precisará [configurar notificações por push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) para o Web SDK. Note que só é possível enviar notificações por push para usuários do iOS e iPadOS que estejam usando [o Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) ou posterior.

## Configuração do Safari push para celular

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

Todos os navegadores populares (como Safari, Chrome, FireFox e Edge) suportam notificações por push da Web em suas versões mais recentes. Para solicitar permissão push no iOS ou iPadOS, seu site deve ser adicionado à tela inicial do usuário selecionando **Share To** > **Add to Home Screen**. O [Add to Homescreen](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) permite que os usuários marquem seu site como favorito, adicionando seu ícone ao valioso espaço da tela inicial.

![Um iPhone mostrando opções para marcar um site como favorito e salvá-lo na tela inicial]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Etapa 5: Mostrar o prompt push nativo {#push-prompt}
Após o app ter sido adicionado à sua tela inicial, agora é possível solicitar permissão de push quando o usuário realizar uma ação (como clicar em um botão). Isso pode ser feito usando o método [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) ou com uma [mensagem no app sem código push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

{% alert note %}
Depois de aceitar ou recusar o aviso, você precisa excluir e reinstalar o site na sua tela inicial para poder mostrar o aviso novamente.
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

Em seguida, envie a si mesmo uma [mensagem de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) para validar a integração. Depois que sua integração estiver concluída, você poderá usar nossas [mensagens push primárias sem código]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) para otimizar suas taxas de aceitação push.
