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

> [A AppsFlyer](https://www.appsflyer.com/) é uma plataforma de análise e atribuição de marketing para mobile que o ajuda a analisar e otimizar seus apps por meio de análise de dados de marketing, atribuição mobile e deep linking.

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
Se você tiver um app para Android, deverá passar um ID de dispositivo Braze exclusivo para a AppsFlyer. 

Certifique-se de que as seguintes linhas de código sejam inseridas no local correto - depois que o SDK do Braze for iniciado e antes do código de inicialização do SDK da AppsFlyer. Consulte o [guia de integração do SDK do Android](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk) da Appsflyer para saber mais.

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
Antes de fevereiro de 2023, nossa integração de atribuição da AppsFlyer usava o Identificador de Fornecedor (IDFV) como identificador principal para corresponder aos dados de atribuição do iOS. Não é necessário que os clientes do Braze que usam Objective C busquem o Braze `device_id` e o enviem para a AppsFlyer após a instalação, pois não há interrupção do serviço.
{% endalert%}

Para quem usa o Swift SDK v5.7.0+, se quiser continuar usando o IDFV como identificador mútuo, é preciso confirmar que o campo `useUUIDAsDeviceId` está definido como `false` para evitar a interrupção da integração. 

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

{% tab unity %}
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

Aqui, você encontra o endpoint REST e gera sua chave de importação de dados do Braze. Depois que a chave é gerada, você pode criar outra ou invalidar uma existente. A chave de importação de dados e o ponto de extremidade REST são usados na próxima etapa ao configurar um postback no dashboard da AppsFlyer.<br><br>![A caixa "Importação de dados para instalar atribuição" está disponível na página de tecnologia da AppsFlyer. Incluídos nessa caixa, estão a chave de importação de dados e o endpoint REST.]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### Etapa 3: Configurar o Braze no dashboard da AppsFlyer

1. Na AppsFlyer, navegue até a página **Parceiros integrados** na barra esquerda. Em seguida, procure o **Braze** e selecione o logotipo do Braze para abrir uma janela de configuração.
2. Na guia **Integração**, ative **Ativar parceiro**.
3. Forneça a chave de importação de dados e o ponto de extremidade REST que você encontrou no dashboard do Braze. 
4. Desative a opção **Advanced Privacy** (Privacidade avançada) e salve sua configuração.

Informações adicionais sobre essas instruções estão disponíveis na [documentação da AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration).

### Etapa 4: Confirmar a integração

Depois que o Braze recebe dados de atribuição da AppsFlyer, o indicador de status de conexão na página de parceiros de tecnologia da AppsFlyer no Braze muda de "Não conectado" para "Conectado" e inclui um registro de data e hora da última solicitação bem-sucedida.

Esse status é alterado somente depois que o Braze recebe dados sobre uma atribuição de instalação. O Braze ignora as instalações orgânicas (as exclui do postback da AppsFlyer) e não as conta ao determinar se a conexão foi bem-sucedida.

### Etapa 5: Visualização de dados de atribuição de usuários

#### Campos de dados disponíveis

Se sua integração foi bem-sucedida, o Braze mapeia todos os dados de instalações não orgânicas para filtros de segmento.

| Campo de dados da AppsFlyer | Filtro de segmento de Braze |
| -------------------- | --------------------- |
| `media_source` | Fonte atribuída |
| `campaign` | Campanha de atribuição |
| `af_adset` | Grupo de anúncios atribuídos |
| `af_ad` | Anúncio atribuído |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Você pode segmentar sua base de usuários por dados de atribuição no dashboard do Braze usando os filtros de Atribuição de Instalação.

![Quatro filtros disponíveis. A primeira é "Install Attribution Source is network_val_0". ". A segunda é "Install Attribution Source is campaign_val_0". ". A terceira é "Install Attribution Source is adgroup_val_0". ". A quarta é "Install Attribution Source is creative_val_0". ". Ao lado dos filtros listados, você pode ver como essas fontes de atribuição serão adicionadas ao perfil do usuário. Na caixa "Atribuição da instalação" na página de informações de um usuário, a fonte de instalação é listada como network_val_0,, a campanha é listada como campaign_val_0, etc.]({% image_buster /assets/img/braze_attribution.png %})

Além disso, os dados de atribuição de um determinado usuário estão disponíveis no perfil de cada usuário no dashboard do Braze.

{% alert note %}
Os dados de atribuição para campanhas do Facebook e do X (antigo Twitter) não estão disponíveis por meio de nossos parceiros. Essas fontes de mídia não permitem que seus parceiros compartilhem dados de atribuição com terceiros e, portanto, nossos parceiros não podem enviar esses dados para a Braze.
{% endalert %}

## Integrar a AppsFlyer com o Braze para deep linking

Os deep linkings - links que direcionam os usuários para uma página ou local específico dentro de um app ou site - são usados para criar uma experiência personalizada para o usuário. 

Embora amplamente utilizado, podem surgir problemas ao usar deep linkings enviados por e-mail com rastreamento de cliques#8212, outro recurso importante usado na coleta de dados de usuários. Esses problemas se devem ao fato de os provedores de serviços de e-mail (ESPs) envolverem os deep links em um domínio de gravação de cliques, quebrando o link original. Dessa forma, o suporte a deep links requer configuração adicional.

A AppsFlyer presta um [serviço](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer) que evita esses problemas, ativando a AppsFlyer para servir como intermediária entre o servidor ESP e seu nome de domínio.  Sua função como proxy ativa o fornecimento de arquivos de associação (AASA/asset links), o que facilita o deep linking. 

## Etapa 1 - Criar um domínio de rastreamento de cliques 

Seguindo os elementos iniciais da [orientação de configuração de e-mail do Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate), crie um domínio de envio de e-mail e um domínio de rastreamento de cliques. Para obter suporte, você pode criar um ticket por meio do Braze Dashboard para iniciar a configuração do novo CTD com a equipe do Braze Email.

![A interface de usuário do Braze mostra o botão "Get Help" (Obter ajuda), localizado abaixo do botão "Support" (Suporte) no canto superior direito]({% image_buster /assets/img/attribution/appsflyer/1.png %})

É obrigatório criar um novo CTD, mesmo que você já esteja usando um existente. Isso garante que não haja impacto no tráfego das campanhas ativas de e-mail atuais. 

{% alert important%}
A AppsFlyers cria o certificado SSL. Nesse estágio, os links de e-mail provavelmente não estão protegidos, o que significa que o prefixo do URL é HTTP em vez de HTTPS. Isso será resolvido em etapas posteriores.	
{%endalert%}

## Etapa 2 - Criar um modelo do OneLink na AppsFlyer
Crie um [modelo do OneLink](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures) e configure Universal Links/App Links em "When app is installed" (Quando o app é instalado). Esse modelo é usado posteriormente para criar links do OneLink para suas campanhas de e-mail.

{% alert note%} Se você já tiver um modelo existente do OneLink configurado que ativa Universal Links/App Links, poderá usá-lo.
{%endalert%}

## Etapa 3 - Configure sua integração com o Braze na Appsflyer
Agora é hora de configurar sua integração com o Braze na AppsFlyer. Essa etapa e a seguinte ("Configure your app") podem ser configuradas ao mesmo tempo.
Para definir sua integração com o Braze na Appsflyer:

### 1\. Na AppsFlyer, no menu lateral, selecione Engajamento > Integração ESP.
![UI do Appsflyer mostrando o botão "Integração ESP", encontrado no menu do lado esquerdo]({% image_buster /assets/img/attribution/appsflyer/2.png %})

 
### 2\. Selecione Braze.
![UI do Appsflyer mostrando a lista de integrações ESP, incluindo o Braze.]({% image_buster /assets/img/attribution/appsflyer/3.png %})

 
### 3\. Selecione o modelo do OneLink que deseja usar para campanhas de e-mail e clique em Next (Avançar).
![UI do Appsflyer mostrando o menu suspenso que permite aos usuários selecionar seu modelo.]({% image_buster /assets/img/attribution/appsflyer/4.png %})

 
### 4\. Digite seu domínio de rastreamento de cliques e o valor do "Braze endpoint", que foi fornecido com o novo CTD criado na etapa 1, e clique em Validar conexão.

Isso valida que o domínio de rastreamento de cliques aponta para o endpoint que você inseriu.

![A interface do usuário do Appsflyer destaca onde os clientes devem adicionar seu domínio de rastreamento de cliques e detalhes associados.]({% image_buster /assets/img/attribution/appsflyer/5.png %})

Por "Braze Endpoint", a Appsflyer está solicitando os detalhes fornecidos pelo Braze na etapa 1 deste guia, especificamente o novo CTD. 

Em seguida, clique em **Validar conexão**, que valida que o domínio de rastreamento de cliques aponta para o endpoint que você inseriu.
Quando terminar, clique em **Next**.

### 5\. Encaminhar o tráfego do link para a AppsFlyer:

#### a. Copie e envie as instruções personalizadas pré-fabricadas na AppsFlyer para seu administrador de TI ou de domínio. 

Seu administrador deve redirecionar o tráfego da campanha de e-mail dos servidores ESP para os servidores da AppsFlyer, atualizando seus registros DNS CNAME com o novo domínio fornecido pela AppsFlyer.

Como resultado, toda vez que um link é clicado, o clique é redirecionado para a AppsFlyer, que, por sua vez, o redireciona para o endpoint do ESP.

![Diagrama que ilustra como os dados de cliques são transmitidos de seu domínio para a AppsFlyer e para seu endpoint esp]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. Depois de copiar e enviar as instruções, clique em Concluído.
Sua integração com o Braze foi criada.

{%alert important%}
O status da integração do Braze está pendente e começa a funcionar somente depois que o registro CNAME é mapeado. Pode levar até 24 horas após o mapeamento para que uma nova integração comece a funcionar e se torne ativa.
{%endalert%}

## Etapa 4: Configure seu app (tarefa de desenvolvedor)
A Appsflyer [oferece orientação](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task) sobre a configuração correta do aplicativo, que deve ser seguida por suas equipes da Web ou de aplicativos para oferecer suporte à vinculação universal. 

## Etapa 5: Confirme se o rastreamento de cliques SSL está ativado com o Braze

Nessa etapa, depois de compartilhar e validar os detalhes do CTD no Appsflyer, recomendamos realizar um envio de teste para confirmar se o domínio de envio do Onelink tem um certificado SSL. Isso está de acordo com nosso guia de [configuração de e-mail](https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate).

Você pode realizar a garantia de qualidade e a solução de problemas enviando um deep linking usando o OneLink. Consulte a [documentação da AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a) para obter detalhes sobre o uso do OneLink.

Se os links CTD forem identificados como HTTP, entre em contato com a equipe de operações de e-mail do Braze para ativar o rastreamento de cliques SSL. Isso garante que todos os links HTTP sejam convertidos automaticamente para HTTPS.
Você pode usar o seguinte exemplo de texto de mensagem ao entrar em contato com seu gerente de sucesso do cliente ou ao criar um ticket no Braze Dashboard novamente, como na etapa 1: 

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS. 
```

### URLs de rastreamento de cliques da AppsFlyer no Braze (opcional)

Você pode usar [os links de atribuição do OneLink](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) da AppsFlyer em campanhas da Braze por push, e-mail e muito mais. Isso permite que você envie dados de atribuição de instalação ou reengajamento de suas campanhas do Braze para a AppsFlyer. Como resultado, você pode medir seus esforços de marketing de forma mais eficaz e tomar decisões baseadas em dados.

Você pode simplesmente criar seu URL de rastreamento do OneLink na AppsFlyer e inseri-lo diretamente em suas campanhas no Braze. Em seguida, a AppsFlyer usa suas [metodologias de atribuição probabilística](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling) para atribuir o usuário que clicou no link. Recomendamos anexar seus links de rastreamento da AppsFlyer com um identificador de dispositivo para melhorar a precisão das atribuições de suas campanhas do Braze. Isso atribui de forma determinística o usuário que clicou no link.

{% tabs local %}
{% tab Android %}
Para Android, o Braze permite que os clientes aceitem a [coleta de ID de publicidade do Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). A integração do SDK da AppsFlyer também coleta o GAID. É possível incluir o GAID em seus links de rastreamento de cliques da AppsFlyer usando a seguinte lógica Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto a Braze quanto a AppsFlyer coletam de modo automático o IDFV nativamente através das nossas integrações de SDK. Você pode usar o IDFC como identificador do dispositivo. Você pode incluir o IDFV em seus links de rastreamento de cliques da AppsFlyer usando a seguinte lógica Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}
