---
nav_title: TV e OTT
article_title: Integrações de TV e OTT para o Braze
page_order: 15

description: "Este artigo detalhará os recursos de TV e OTT da Braze, integrações, plataformas disponíveis, entre outros."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# Integrações de TV e OTT

> À medida que a tecnologia evolui para novas plataformas e dispositivos, o seu envio de mensagens também pode evoluir com a Braze! O Braze oferece diferentes canais de engajamento para vários sistemas operacionais de TV e métodos de fornecimento de conteúdo OTT (Over-the-Top).

## Plataformas e recursos

A seguir estão listados os recursos e os canais de envio de mensagens suportados hoje.

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center !important;
    vertical-align: center;
}

</style>
<table id="tv-feature-table">
    <thead>
        <tr>
            <th>Tipo de dispositivo</th>
            <th>Dados e análise de dados</th>
            <th>Mensagem no app</th>
            <th>Cartões de conteúdo</th>
            <th>Notificações por push</th>
            <th>Canva</th>
            <th>Feature Flags</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>TV LG (webOS)</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">N/D</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Samsung TV Tizen</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">N/D</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">N/D</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
             <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fa-solid fa-minus"></i></td>  
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
       <tr>
          <td>Apple Vision Pro</td>
          <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
           <td for="iam"><i class="fas fa-check text-success"></i></td>
          <td for="content-cards"><i class="fas fa-check text-success"></i></td>
          <td for="push"><i class="fa-solid fa-minus"></i></td>  
          <td for="canvas"><i class="fas fa-check text-success"></i></td>
          <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
      </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = Suportado
- <i class="fa-solid fa-minus"></i> = Suporte parcial
- <i class="fas fa-times text-warning"></i> = Não suportado pela Braze
- N/A = Não suportado pela plataforma OTT

## Guias de integração

### Amazon Fire TV {#fire-tv}

Use o SDK Braze Fire OS para integrar com dispositivos Amazon Fire TV.

Os recursos incluem:

- Coleta e análise de dados para engajamento entre canais
- Notificações por push (conhecidas como ["Heads Up Notifications"](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup))
  - A prioridade deve ser definida como "ALTA" para que estes apareçam. Todas as notificações aparecem no menu de configurações do Fire TV.
- Cartões de conteúdo
- Feature Flags
- Mensagem no app
  - Para mostrar envios de mensagens HTML em ambientes sem toque, como TVs, defina `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` como `false` (disponível no [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))

Para saber mais, visite o [guia de integração do Fire OS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

### Kindle Fire {#kindle-fire}

Use o Braze Fire OS SDK para integrar com dispositivos Amazon Kindle Fire.

Os recursos incluem:

- Coleta e análise de dados para engajamento entre canais
- Notificações por push
- Cartões de conteúdo
- Feature Flags
- Mensagem no app

Para saber mais, visite o [guia de integração do Fire OS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

### Android TV {#android-tv}

Use o Braze Android SDK para integrar com dispositivos Android TV.

Os recursos incluem:

- Coleta e análise de dados para engajamento entre canais
- Cartões de conteúdo
- Feature Flags
- Mensagem no app 
  - Para mostrar envios de mensagens HTML em ambientes sem toque, como TVs, defina `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` como `false` (disponível no [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- \* notificações por push (Integração Manual Necessária)
  - Notificações por push não têm compatibilidade nativa no Android TV. Para saber por que, consulte as [Diretrizes de design](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html) do Google. Você pode, no entanto, **fazer uma integração manual da interface de usuário de notificação por push para conseguir isso**. Consulte nossa [documentação]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android%20tv) sobre como configurar isso.

Para saber mais, visite o [guia de integração do SDK do Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).

{% alert note %}
Crie um novo app Android no dashboard para sua integração Android OTT.
{% endalert %}

### LG webOS {#lg-webos}

Use o Braze Web SDK para integrar com [TVs LG webOS](https://webostv.developer.lge.com/discover).

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento multicanal
- Cartões de conteúdo (via [Headless UI](#custom-ui))
- Feature Flags
- Mensagens no app (via [Headless UI](#custom-ui))

Para saber mais, visite o [guia de integração da Web Smart TV]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/).

### Samsung Tizen {#tizen}

Use o Braze Web SDK para integrar com as [TVs Samsung Tizen](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento multicanal
- Cartões de conteúdo (via [Headless UI](#custom-ui))
- Feature Flags
- Mensagens no app (via [Headless UI](#custom-ui))

Para saber mais, visite o [guia de integração da Web Smart TV]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/).

### Roku {#roku}

Use o Braze Roku SDK para integrar com [TVs Roku](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md).

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento multicanal
- Mensagens no app (via [Headless UI](#custom-ui))
  - A plataforma Roku não é compatível com webviews, então não há suporte para mensagens HTML no app.
- Feature Flags

Para saber mais, acesse o [guia de integração do Roku]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=roku).

### Apple tvOS {#tvos}

Use o Braze Swift SDK para integrar com o tvOS. Lembre-se de que o Swift SDK não inclui nenhuma interface ou visualização padrão para tvOS, então você precisará implementar a sua própria.

Os recursos incluem:

- Coleta de dados e análise de dados para engajamento multicanal
- Cartões de conteúdo (via [Headless UI](#custom-ui))
- Feature Flags
- Mensagens no app (via [Headless UI](#custom-ui))
  - A plataforma tvOS não é compatível com webviews, então não há suporte para mensagens HTML no app.
  - Veja nosso [app de amostra](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) para saber mais sobre como usar uma interface do usuário sem cabeça para envio de mensagens personalizadas no tvOS.
- Notificações por push silenciosas e atualização de badging

Para saber mais, acesse o [guia de integração do SDK do Swift para iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert note %}
Para evitar mostrar mensagens no app móvel para seus usuários de TV, certifique-se de configurar o [direcionamento de app](#app-targeting) ou use pares de chave-valor para filtrar mensagens. Por exemplo, exibir mensagens do tvOS apenas se elas contiverem um par de chave/valor especial `tv = true`.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Use o Braze Swift SDK para integrar com o visionOS. A maioria dos recursos disponíveis no iOS também está disponível no visionOS, tais como:

- Análise de dados (sessões, eventos personalizados, compras, etc.)
- Envio de mensagens no app (modelos de dados e UI)
- Cartões de Conteúdo (modelos de dados e UI)
- Notificações por push (visíveis ao usuário com botões de ação e notificações silenciosas)
- Feature Flags
- Análise de dados de locais

Para saber mais, acesse o [guia de integração do SDK do Swift para iOS](https://github.com/braze-inc/braze-swift-sdk).

{% alert important %}
Alguns recursos do iOS são parcialmente compatíveis ou incompatíveis. Para a lista completa, consulte o [suporte ao visionOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/visionos).
{% endalert %}

## Direcionamento de apps {#app-targeting}

Para direcionar apps OTT para envio de mensagens, recomendamos criar um segmento específico para o seu app OTT.

![Um segmento criado usando o app Android OTT.]({% image_buster /assets/img/android_ott.png %})

## Headless UI {#custom-ui}

{% alert important %}
Plataformas que suportam mensagens no app ou Cartões de Conteúdo via interface de usuário sem cabeça **não** incluem qualquer interface de usuário ou visualizações padrão, então certifique-se de implementar sua própria interface de usuário personalizada.
{% endalert %}

Com a Headless UI, a Braze fornecerá um modelo de dados, como JSON, que seu app pode ler e usar dentro de uma interface de usuário que seu app controla. Esses dados conterão os campos configurados no dashboard (título, corpo, texto do botão, cores, etc.) que seu app pode ler e exibir de acordo. Para saber mais sobre o envio de mensagens personalizadas, consulte:

**Android SDK**
- [Customização de mensagem no app]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)
- [Personalização de Cartões de Conteúdo]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

**SWIFT SDK**
- [Customização de mensagem no app](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [App de amostra de Headless UI](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Personalização de Cartões de Conteúdo](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**SDK para Web**
- [Customização de mensagem no app]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web)
- [Personalização de Cartões de Conteúdo]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

