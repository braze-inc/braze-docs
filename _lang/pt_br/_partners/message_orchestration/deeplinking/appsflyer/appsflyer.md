---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "Esse artigo de referência descreve a parceria entre o Braze e a AppsFlyer, uma plataforma de análise de dados e atribuição de marketing para mobile que ajuda você a analisar e otimizar seus apps."
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> A AppsFlyer é uma plataforma de atribuição e análise de dados de marketing para mobile que ajuda a analisar e otimizar seus apps por meio de análises, atribuição para mobile e deep linking.

A integração entre o Braze e a AppsFlyer permite que você entenda melhor como otimizar e criar campanhas mais holísticas, aproveitando os dados de atribuição de instalação móvel da AppsFlyer. 

Também é possível passar seus públicos da AppsFlyer (coortes) diretamente para a Braze com a integração [AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences/), o que lhe permite criar poderosas campanhas de engajamento de clientes direcionadas aos usuários certos no momento certo. 

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta da AppsFlyer | É necessário ter uma conta da AppsFlyer para aproveitar essa parceria. |
| App para iOS ou Android | Essa integração é compatível com os apps para iOS e Android. Dependendo de sua plataforma, os trechos de código podem ser necessários em seu aplicativo. Consulte os detalhes sobre esses requisitos na etapa 1 do processo de integração. |
| SDK da AppsFlyer | Além do SDK da Braze obrigatório, você deve instalar o [SDK da AppsFlyer](https://dev.appsflyer.com/hc/docs/getting-started).
| Configuração completa do domínio de e-mail | Você deve ter concluído a [etapa de configuração de IP e domínio]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/) para configurar seu e-mail durante o envio do Braze para integração. |
| Certificado SSL | Seu [certificado SSL]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#acquiring-an-ssl-certificate) deve estar configurado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: mapeie o ID do dispositivo

{% tabs local %}
{% tab Android %}
Se você tiver um app para Android, precisará passar um ID de dispositivo Braze exclusivo para a AppsFlyer. 

Confirme se as seguintes linhas de código foram inseridas no local correto depois que o SDK do Braze for iniciado e antes do código de inicialização do SDK da AppsFlyer. Consulte o [guia de integração do SDK do Android](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) da Appsflyer para saber mais.

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```
{% endtab %}

{% tab ios %}
{% alert important %}
Antes de fevereiro de 2023, nossa integração de atribuição da AppsFlyer usava o IDFV como identificador principal para corresponder aos dados de atribuição do iOS. Não é necessário que os clientes da Braze que usam Objective-C busquem o `device_id` da Braze e o enviem para a AppsFlyer na instalação, pois não haverá interrupção do serviço.
{% endalert%}

Para quem usa o SWIFT SDK v5.7.0+, se você deseja continuar usando o IDFV como o identificador mútuo, confirme se o campo `useUUIDAsDeviceId` está definido como `false` para que não haja interrupção da integração. 

Se estiver definido como `true`, implemente o mapeamento de ID do dispositivo iOS para Swift a fim de passar o `device_id` da Braze para a AppsFlyer na instalação do app para que a Braze possa corresponder adequadamente as atribuições do iOS.

{% subtabs local %}
{% subtab Swift %}

```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```
{% endsubtab %}

{% subtab Objective-C %}
```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Unity %}
Para mapear o ID do dispositivo no Unity, use o seguinte:

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### Etapa 2: Obter a chave de importação de dados do Braze

No Braze, navegue até **Integrações com Parceiros** > **Parceiros de Tecnologia** e selecione **a AppsFlyer**. 

Aqui você encontra o endpoint REST e gera sua chave de importação de dados da Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente. A chave de importação de dados e o ponto de extremidade REST são usados na próxima etapa ao configurar um postback no dashboard da AppsFlyer.<br><br>![A caixa "Importação de dados para instalar atribuição" está disponível na página de tecnologia da AppsFlyer. Incluídos nessa caixa estão a chave de importação de dados e o ponto de extremidade REST.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### Etapa 3: Configurar o Braze no dashboard da AppsFlyer

1. Na AppsFlyer, navegue até a página **Parceiros integrados** na barra esquerda. Em seguida, procure o **Braze** e selecione o logotipo do Braze para abrir uma janela de configuração.
2. Na guia **Integração**, ative **Ativar parceiro**.
3. Forneça a chave de importação de dados e o ponto de extremidade REST que você encontrou no dashboard do Braze. 
4. Desative a opção **Advanced Privacy** (Privacidade avançada) e salve sua configuração.

Informações adicionais sobre essas instruções estão disponíveis na [documentação da AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration).

### Etapa 4: Confirmar a integração

Quando o Braze receber dados de atribuição da AppsFlyer, o indicador de status de conexão na página de parceiros de tecnologia da AppsFlyer no Braze mudará de "Não conectado" para "Conectado". Um registro de data e hora da última solicitação bem-sucedida também será incluído. 

Observe que isso não acontecerá até recebermos dados sobre uma instalação atribuída. Instalações orgânicas, que devem ser excluídas do postback da AppsFlyer, são ignoradas pela nossa API e não são contadas ao determinar se uma conexão bem-sucedida foi estabelecida.

### Etapa 5: Visualização de dados de atribuição de usuários

#### Campos de dados disponíveis

Supondo que você configure sua integração conforme sugerido, o Braze mapeará todos os dados de instalações não orgânicas para filtros de segmento.

| Campo de dados da AppsFlyer | Filtro de segmento de Braze |
| -------------------- | --------------------- |
| `media_source` | Fonte atribuída |
| `campaign` | Campanha de atribuição |
| `af_adset` | Grupo de anúncios atribuídos |
| `af_ad` | Anúncio atribuído |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Sua base de usuários pode ser segmentada por dados de atribuição no dashboard do Braze usando os filtros de Atribuição de Instalação.

![Quatro filtros disponíveis. A primeira é "Instalação por origem é network_val_0". A segunda é "Install Attribution Source is campaign_val_0" (A fonte de atribuição da instalação é campaign_val_0). A terceira é "Install Attribution Source is adgroup_val_0" (A fonte de atribuição da instalação é adgroup_val_0). A quarta é "Instalação por origem é creative_val_0". Ao lado dos filtros listados, você pode ver como essas fontes de atribuição serão adicionadas ao perfil do usuário. Na caixa "Atribuição da instalação" na página de informações de um usuário, a Fonte de instalação é listada como network_val_0, a campanha é listada como campaign_val_0, etc.]({% image_buster /assets/img/braze_attribution.png %})

Além disso, os dados de atribuição de um determinado usuário estão disponíveis no perfil de cada usuário no dashboard do Braze.

{% alert note %}
Os dados de atribuição para campanhas do Facebook e do X (antigo Twitter) não estão disponíveis por meio de nossos parceiros. Essas fontes de mídia não permitem que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.
{% endalert %}

## Integrar a AppsFlyer com um provedor de serviço de e-mail para deep linking

A AppsFlyer se integra ao SendGrid e ao SparkPost como prestadores de serviço de e-mail para oferecer suporte a deep linking e rastreamento de cliques. Siga as instruções abaixo para fazer a integração com o ESP de sua preferência.

{% alert tip %}
Os deep linkings - links que direcionam os usuários para uma página ou local específico dentro de um app ou site - são usados para criar uma experiência personalizada para o usuário. Embora amplamente utilizado, podem surgir problemas ao usar deep links enviados por e-mail com rastreamento de cliques, outro recurso importante usado na coleta de dados de usuários. Esses problemas se devem ao fato de os provedores de serviços de e-mail envolverem os deep links em um domínio de registro de cliques, quebrando o link original. Dessa forma, o suporte a deep links requer configuração adicional. Ao integrar a AppsFlyer com o SendGrid ou o SparkPost, você evita esses problemas. Saiba mais sobre esse tópico em [Links universais e links de apps]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).
{% endalert %}

### Etapa 1: Configurar o OneLink na AppsFlyer

1. Na AppsFlyer, selecione um modelo do OneLink para suas campanhas de e-mail. Certifique-se de que o modelo seja compatível com links universais (iOS) ou App Links (Android). 
2. Configure seu app para suportar o deep linking com o OneLink. Consulte a [documentação da AppsFlyer](https://dev.appsflyer.com/hc/docs/dl_work_flow#initial-setup) para obter detalhes sobre como configurar seu app para suportar o OneLink.

### Etapa 2: Configure seu aplicativo para suportar links universais e App Links

Os links universais (iOS) ou links de aplicativos (Android) são permitidos pelo sistema operacional do dispositivo para abrir um app específico quando clicados.

Execute as etapas a seguir para oferecer suporte a links universais e links de apps.

{% tabs local %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
Configure a hospedagem de arquivos da Apple App Site Association (AASA) para ativar links universais em seus e-mails.

1. Obtenha um arquivo AASA em um dos seguintes métodos:
    * Se você configurou o OneLink com links universais, é possível que já tenha um arquivo AASA associado ao OneLink. Para obter o arquivo AASA, faça o seguinte:
        * Copie o subdomínio do OneLink de seu modelo do OneLink. Certifique-se de que o modelo seja compatível com links universais.
        * Cole-o no lugar do espaço reservado no URL a seguir: `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * Para baixar o arquivo AASA, cole o URL do OneLink na barra de endereços do navegador e pressione **Enter**. O arquivo será baixado em seu computador, e você poderá abrir e visualizar seu conteúdo usando qualquer editor de texto.
    * [O guia da Apple sobre links universais](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) explica como criar o arquivo AASA.
2. Hospede o arquivo AASA em seu servidor de domínio de gravação de cliques. O arquivo deve ser hospedado no caminho: `click.example.com/.well-known/apple-app-site-association`. 

Consulte a [documentação da SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links) para saber como configurar o arquivo AASA para a SendGrid e definir os serviços de CDN para hospedar o arquivo AASA.

{% alert important %}
Depois que o arquivo AASA for hospedado, qualquer alteração na configuração do OneLink (modificação ou substituição) exigirá a geração de um novo arquivo AASA.
{% endalert %}
{% endsubtab %}
{% subtab Android %}
Configure a hospedagem do arquivo Digital Asset Links para ativar os links de apps em seus e-mails.

1. Obtenha um arquivo Digital Asset Links com um destes métodos:
    * Se você configurou o OneLink com links de apps, talvez já tenha um arquivo Digital Asset Links associado ao OneLink. Para obter o arquivo, faça o seguinte:
        * Copie o subdomínio do OneLink de seu modelo do OneLink. Certifique-se de que o modelo seja compatível com App Links.
        * Adicione `/.well-known/assetlinks.json` ao final do URL do OneLink.
        * Para baixar o arquivo Digital Asset Links, cole o URL do OneLink na barra de endereços do navegador e pressione **Enter**. Por exemplo, `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. O arquivo será baixado em seu computador, e você poderá abrir e visualizar seu conteúdo usando qualquer editor de texto.
    * [O guia do Android para links de apps](https://developer.android.com/studio/write/app-link-indexing) explica como criar o arquivo Digital Asset Links.
2. Hospede o arquivo Digital Asset Links no seu servidor de domínio de gravação de cliques. O arquivo deve ser hospedado no caminho: `click.example.com/.well-known/apple-app-site-association`.

Consulte a [documentação do SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links) para saber como configurar o arquivo Digital Asset Links para o SendGrid e definir os serviços de CDN para hospedar o arquivo Digital Asset Links.

{% alert important %}
Depois que o arquivo Digital Asset Links for hospedado, qualquer alteração na configuração do OneLink (modificação ou substituição) exigirá a geração de um novo arquivo.
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### Etapa 2a: Configurar a hospedagem de arquivos da AASA
Configure a hospedagem de arquivos da Apple App Site Association (AASA) para ativar links universais em seus e-mails.

1. Obtenha um arquivo AASA em um dos seguintes métodos:
    * Se você configurou o OneLink com links universais, é possível que já tenha um arquivo AASA associado ao OneLink. Para obter o arquivo AASA, faça o seguinte:
        * Copie o subdomínio do OneLink de seu modelo do OneLink. Certifique-se de que o modelo seja compatível com links universais.
        * Cole-o no lugar do espaço reservado no URL a seguir: `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * Para baixar o arquivo AASA, cole o URL do OneLink na barra de endereços do navegador e pressione **Enter**. O arquivo será baixado em seu computador, e você poderá abrir e visualizar seu conteúdo usando qualquer editor de texto.
    * [O guia da Apple sobre links universais](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content) explica como criar o arquivo AASA.
2. Hospede o arquivo AASA em seu servidor de domínio de gravação de cliques. O arquivo deve ser hospedado no caminho: `click.example.com/.well-known/apple-app-site-association`. 

Consulte a [documentação do SparkPost](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve) para saber como configurar o arquivo AASA para o SparkPost e definir subcaminhos de links personalizados.

{% alert important %}
Depois que o arquivo AASA for hospedado, qualquer alteração na configuração do OneLink (modificação ou substituição) exigirá a geração de um novo arquivo AASA.
{% endalert %}

#### Etapa 2b: Redirecione seu domínio de rastreamento de cliques para seu host de arquivos da AASA
Durante a [configuração do e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/), você criou um registro CNAME no servidor DNS. Execute as etapas a seguir depois de verificar seu domínio de rastreamento de cliques no Braze. 

1. Exclua o registro CNAME que redireciona seu subdomínio para o domínio SparkPost.
2. Crie um registro CNAME que redirecione o domínio de rastreamento de cliques para a CDN que hospeda o arquivo AASA do app, em vez do registro excluído acima.
{% endsubtab %}
{% subtab Android %}
#### Etapa 2a: Configurar a hospedagem de arquivos do Digital Asset Links
Configure a hospedagem do arquivo Digital Asset Links para ativar os links de apps em seus e-mails.

1. Obtenha um arquivo Digital Asset Links com um destes métodos:
    * Se você configurou o OneLink com links de apps, talvez já tenha um arquivo Digital Asset Links associado ao OneLink. Para obter o arquivo, faça o seguinte:
        * Copie o subdomínio do OneLink de seu modelo do OneLink. Certifique-se de que o modelo seja compatível com App Links.
        * Adicione `/.well-known/assetlinks.json` ao final do URL do OneLink.
        * Para baixar o arquivo Digital Asset Links, cole o URL do OneLink na barra de endereços do navegador e pressione **Enter**. Por exemplo, `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`. O arquivo será baixado em seu computador, e você poderá abrir e visualizar seu conteúdo usando qualquer editor de texto.
    * [O guia do Android para links de apps](https://developer.android.com/studio/write/app-link-indexing) explica como criar o arquivo Digital Asset Links.
2. Hospede o arquivo Digital Asset Links no seu servidor de domínio de gravação de cliques. O arquivo deve ser hospedado no caminho: `click.example.com/.well-known/apple-app-site-association`.

Consulte a [documentação do SparkPost](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve) para saber como configurar o arquivo de links de ativos digitais para o SparkPost e definir subcaminhos de links personalizados.

{% alert important %}
Depois que o arquivo Digital Asset Links for hospedado, qualquer alteração na configuração do OneLink (modificação ou substituição) exigirá a geração de um novo arquivo.
{% endalert %}

#### Etapa 2b: Redirecione seu domínio de rastreamento de cliques para o host do arquivo de links de ativos digitais
Durante a [configuração do e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/), você criou um registro CNAME no servidor DNS. Execute as etapas a seguir depois de verificar seu domínio de rastreamento de cliques no Braze. 

1. Exclua o registro CNAME que redireciona seu subdomínio para o domínio SparkPost.
2. Crie um registro CNAME que redirecione seu domínio de rastreamento de cliques para a CDN que hospeda o arquivo Digital Asset Links do seu app, em vez do registro que você excluiu acima.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Etapa 3: configure o SDK da AppsFlyer para suportar o deep linking

{% tabs local %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
#### Etapa 3a: Configure seu SDK para suportar o arquivo AASA
Depois de hospedar o arquivo AASA no seu domínio de gravação de cliques, configure o SDK da AppsFlyer para suportar o arquivo AASA.

1. No Xcode, selecione seu projeto.
2. Selecione **Capacidades.**
3. Ative a opção **Associated Domains (Domínios associados).**
4. Clique em **+** e digite seu domínio de clique. Por exemplo, `applinks:click.example.com`.
Quando ocorre um clique no link universal, seu app é aberto, e o SDK é iniciado. Para permitir que o app extraia o OneLink por trás do domínio de cliques e resolva o deep linking, faça o seguinte:

#### Etapa 3b: lidar com os dados do deep linking
1. Forneça o domínio de registro de cliques à API do SDK [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls). Essa API precisa ser chamada antes da inicialização do SDK. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
2. Use a [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API para obter os parâmetros do deep linking e manipular os dados do deep linking.

{% endsubtab %}
{% subtab Android %}
#### Etapa 3a: configure seu SDK para suportar o arquivo Digital Asset Links

Depois de hospedar o arquivo Digital Asset Links no seu domínio de gravação de cliques na etapa anterior, configure seu SDK para suportar o arquivo.

Em seu manifesto do Android, adicione o host do domínio de clique e qualquer prefixo na tag de atividade da atividade para a qual deseja fazer o deep linking.

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### Etapa 3b: lidar com os dados do deep linking
Quando ocorre um clique em um link de app, seu app é aberto, e o SDK é iniciado.  Para permitir que o app extraia o OneLink por trás do domínio de cliques e resolva o deep linking, liste os domínios de clique no método do SDK [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls). Essa propriedade precisa ser definida antes da inicialização do SDK. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "anotherclickdomain.com");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### Etapa 3a: Configure seu SDK para suportar o arquivo AASA
Depois de hospedar o arquivo AASA no seu domínio de gravação de cliques, configure o SDK para suportar o arquivo AASA.

1. No Xcode, selecione seu projeto.
2. Selecione **Capacidades.**
3. Ative a opção **Associated Domains (Domínios associados).**
4. Clique em **+** e digite seu domínio de clique. Por exemplo, `applinks:click.example.com`.

#### Etapa 3b: lidar com os dados do deep linking
Quando ocorre um clique no link universal, seu app é aberto, e o SDK é iniciado. Para permitir que o SDK extraia o OneLink por trás do domínio de cliques, faça o seguinte:
1. Liste os domínios de clique na propriedade do SDK [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls). Defina essa propriedade antes da inicialização do SDK.
2. Confirme se a lista <em>spgo.io</em> é um dos domínios listados. O SparkPost é proprietário desse domínio, e ele faz parte do fluxo de redirecionamento. `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
3. Use a [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API para obter os parâmetros do deep linking e manipular os dados do deep linking.
{% endsubtab %}
{% subtab Android %}
#### Etapa 3a: configure seu SDK para suportar o arquivo Digital Asset Links

Depois de hospedar o arquivo Digital Asset Links no seu domínio de gravação de cliques na etapa anterior, configure seu SDK para suportar o arquivo.

Em seu manifesto do Android, adicione o host do domínio de clique e qualquer prefixo na tag de atividade da atividade para a qual deseja fazer o deep linking.

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### Etapa 3b: Manipular os dados do App Link
Quando ocorre um clique em um link de app, seu app é aberto, e o SDK é iniciado. Para permitir que o app extraia o OneLink por trás do domínio de cliques e resolva o deep linking, faça o seguinte:

1. Liste os domínios de clique no método do SDK [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls). Essa propriedade precisa ser definida antes da inicialização do SDK.
2. Confirme se a lista *spgo.io* é um dos domínios listados. O SparkPost é proprietário desse domínio, e ele faz parte do fluxo de redirecionamento. `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "spgo.io");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

Depois de concluir as etapas de integração, você pode realizar a garantia de qualidade e a solução de problemas enviando um deep linking usando o OneLink. Consulte a [documentação da AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a) para obter detalhes sobre o uso do OneLink.

### URLs de rastreamento de cliques da AppsFlyer no Braze (opcional)

Você pode usar [os links de atribuição do OneLink](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) da AppsFlyer em campanhas da Braze por push, e-mail e muito mais. Isso permite enviar dados de atribuição de instalação ou reengajamento de suas campanhas do Braze para a AppsFlyer. Como resultado, você poderá medir seus esforços de marketing de forma mais eficaz e tomar decisões baseadas em dados.

Você pode simplesmente criar seu URL de rastreamento do OneLink na AppsFlyer e inseri-lo diretamente em suas campanhas no Braze. A AppsFlyer usará suas [metodologias de atribuição probabilística](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento da AppsFlyer com um identificador de dispositivo para melhorar a precisão das atribuições de suas campanhas do Braze. Isso atribuirá de forma determinística o usuário que clicou no link.

{% tabs local %}
{% tab Android %}
Para Android, a Braze permite que os clientes façam a aceitação da [coleta do ID de publicidade do Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). O GAID também é coletado nativamente pela integração SDK da AppsFlyer. É possível incluir o GAID em seus links de rastreamento de cliques da AppsFlyer utilizando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto a Braze quanto a AppsFlyer coletam de modo automático o IDFV nativamente através das nossas integrações de SDK. Isso pode ser usado como identificador do dispositivo. É possível incluir o IDFV em seus links de rastreamento de cliques da AppsFlyer utilizando a seguinte lógica Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}



