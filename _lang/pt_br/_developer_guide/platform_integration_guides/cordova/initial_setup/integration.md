---
nav_title: Integração
article_title: Integração do SDK do Cordova Braze
page_order: 0
---

# Integração do SDK do Cordova Braze

> Saiba como integrar o Cordova Braze SDK em seu app para iOS ou Android. Depois de terminar, você pode [personalizar ainda mais o SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/).

## Integração do SDK

### Etapa 1: Adicione o SDK ao projeto

Se você estiver usando o Cordova 6 ou posterior, poderá adicionar o SDK diretamente do GitHub. Como alternativa, você pode baixar um ZIP do [repositório do GitHub](https://github.com/braze-inc/braze-cordova-sdk) e adicionar o SDK manualmente.

{% tabs localização %}
{% tab geofence desativado %}
Se não planeja usar a coleta de locais e geofences, use a ramificação `master` do GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab geofence ativada %}
Se planeja usar a coleta de locais e geofences, use `geofence-branch` do GitHub.

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
Você pode alternar entre `master` e `geofence-branch` a qualquer momento, repetindo a etapa 1.
{% endalert %}

### Etapa 2: Configure seu projeto

Em seguida, adicione as seguintes preferências ao elemento `platform` no arquivo `config.xml` de seu projeto.

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab Android %}
```xml
<preference name="com.braze.api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

Substitua o seguinte:

| Valor                 | Descrição                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_KEY`       | Sua [chave da API REST do Braze]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys).              |
| `CUSTOM_API_ENDPOINT` | Um endpoint de API personalizado. Esse endpoint é usado para rotear os dados de sua instância do Braze para o grupo de app correto em seu dashboard do Braze. |

O elemento `platform` em seu arquivo `config.xml` deve ser semelhante ao seguinte:

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab Android %}
```xml
<platform name="android">
    <preference name="com.braze.api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## Desativar o rastreamento automático de sessão (somente Android)

Por padrão, o plug-in do Android Cordova rastreia automaticamente as sessões. Para desativar o rastreamento automático de sessão, adicione a seguinte preferência ao elemento `platform` no arquivo `config.xml` do seu projeto:

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

Para começar a rastrear as sessões novamente, ligue para `BrazePlugin.startSessionTracking()`. Lembre-se de que somente as sessões iniciadas após o próximo `Activity.onStart()` serão rastreadas.
