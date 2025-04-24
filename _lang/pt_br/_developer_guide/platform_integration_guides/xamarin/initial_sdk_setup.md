---
nav_title: Configuração inicial do SDK
article_title: Configuração inicial do SDK para Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 0
toc_headers: h2
description: "Este artigo aborda a configuração inicial do SDK do iOS, Android e FireOS para a plataforma Xamarin."
search_rank: 1
---

# Configuração inicial do SDK

> Saiba como instalar o Braze SDK para Xamarin. A instalação do SDK da Braze fornecerá a funcionalidade básica de análise de dados, bem como mensagens no app com as quais você poderá engajar seus usuários. 

{% alert important %}
A partir de `version 3.0.0`, esse SDK requer o uso do .NET 6+ e remove o suporte para projetos que usam a estrutura Xamarin.
A partir de `version 4.0.0`, esse SDK deixou de oferecer suporte ao Xamarin e ao Xamarin.Forms e adicionou suporte ao .NET MAUI.
Consulte [a política da Microsoft](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin) com relação ao fim do suporte para o Xamarin.
{% endalert %}

## Etapa 1: Obter a vinculação do Xamarin

{% tabs %}
{% tab Android %}
Uma ligação Xamarin é uma maneira de usar bibliotecas nativas em apps Xamarin. A implementação de uma associação consiste em criar uma interface C# para a biblioteca e, em seguida, usar essa interface em seu aplicativo.  Consulte a [documentação da Xamarin](http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/). Há duas maneiras de incluir a associação do SDK da Braze: usando o NuGet ou compilando a partir da fonte.

{% subtabs local %}
{% subtab NuGet %}
O método mais simples de integração envolve a obtenção do SDK da Braze no [NuGet.org](https://www.nuget.org/) repositório central. Na barra lateral do Visual Studio, clique com o botão direito do mouse na pasta `Packages` e clique em `Add Packages...`.  Procure por "Braze" e instale o pacote [`BrazePlatform.BrazeAndroidBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/) em seu projeto.
{% endsubtab %}

{% subtab Source %}
O segundo método de integração é incluir a [fonte de ligação](https://github.com/braze-inc/braze-xamarin-sdk). Em [`appboy-component/src/androidnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding) você encontrará nosso código-fonte de vinculação; adicionar uma referência de projeto a ```BrazeAndroidBinding.csproj``` em seu aplicativo Xamarin fará com que a vinculação seja criada com seu projeto e fornecerá acesso ao SDK  para Android.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ios %}
{% alert important %}
As ligações do iOS para o Xamarin SDK versão 4.0.0 e posteriores usam o [SDK para Swift](https://github.com/braze-inc/braze-swift-sdk/), enquanto as versões anteriores usam o [AppboyKit SDK legado](https://github.com/Appboy/Appboy-ios-sdk).
{% endalert %}

Uma ligação Xamarin é uma maneira de usar bibliotecas nativas em apps Xamarin.  A implementação de uma associação consiste em criar uma interface C# para a biblioteca e, em seguida, usar essa interface em seu aplicativo. Há duas maneiras de incluir a associação do SDK da Braze: usando o NuGet ou compilando a partir da fonte.

{% subtabs local %}
{% subtab NuGet %}
O método mais simples de integração envolve a obtenção do SDK da Braze no [NuGet.org](https://www.nuget.org/) repositório central. Na barra lateral do Visual Studio, clique com o botão direito do mouse na pasta `Packages` e clique em `Add Packages...`.  Procure por "Braze" e instale os pacotes NuGet mais recentes do Xamarin iOS: [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit), [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI), e [Braze.iOS.BrazeLocation]https://www.nuget.org/packages/Braze.iOS.BrazeLocation em seu projeto.

Também fornecemos os pacotes de bibliotecas de compatibilidade: [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat) e [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat)para ajudar a facilitar sua migração para o .NET MAUI.
{% endsubtab %}

{% subtab Source %}
O segundo método de integração é incluir a [fonte de ligação](https://github.com/braze-inc/braze-xamarin-sdk). Em [`appboy-component/src/iosnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding) você encontrará nosso código-fonte de associação; adicionar uma referência de projeto a ```BrazeiOSBinding.csproj``` em seu aplicativo Xamarin fará com que a associação seja criada com seu projeto e fornecerá acesso ao SDK da Braze para iOS. Verifique se o site `BrazeiOSBinding.csproj` está sendo exibido na pasta "Reference" do seu projeto.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Etapa 2: Configure sua instância do Braze

{% tabs %}
{% tab Android %}
### Etapa 2.1: Configure o SDK da Braze em Braze.xml

Agora que as bibliotecas foram integradas, você precisa criar um arquivo `Braze.xml` na pasta `Resources/values` do seu projeto. O conteúdo desse arquivo deve se parecer com o seguinte trecho de código:

{% alert note %}
Certifique-se de substituir `YOUR_API_KEY` pela chave de API localizada em **Configurações** > **Chaves de API** no dashboard do Braze.
<br><br>
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar as chaves de API em **Console do desenvolvedor** > **Configurações de API**.
{% endalert %}

```xml
  <?xml version="1.0" encoding="utf-8"?>
  <resources>
    <string translatable="false" name="com_braze_api_key">YOUR_API_KEY</string>
    <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
    <string-array name="com_braze_internal_sdk_metadata">
      <item>XAMARIN</item>
      <item>NUGET</item>
    </string-array>
  </resources>
```
Se estiver incluindo a fonte de vinculação manualmente, remova `<item>NUGET</item>` do seu código.

{% alert tip %}
Para ver um exemplo em `Braze.xml`, confira nosso [app de amostra Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/Resources/values/Braze.xml).
{% endalert %}

### Etapa 2.2: Adicionar permissões necessárias ao manifesto do Android

Agora que adicionou sua chave de API, você precisa adicionar as seguintes permissões ao arquivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
Para obter um exemplo de seu `AndroidManifest.xml`, consulte o aplicativo de amostra do [Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml).

### Etapa 2.3: Rastreie as sessões de usuários e o registro de mensagens no app

Para ativar o rastreamento da sessão do usuário e registrar seu aplicativo para mensagens no app, adicione a seguinte chamada ao método de ciclo de vida `OnCreate()` da classe `Application` do seu aplicativo:

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```
{% endtab %}

{% tab ios %}
Ao configurar sua instância da Braze, adicione o seguinte snippet para configurar sua instância:

{% alert note %}
Certifique-se de substituir `YOUR_API_KEY` pela chave de API localizada em **Configurações** > **Chaves de API** no dashboard do Braze.

Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar as chaves de API em **Console do desenvolvedor** > **Configurações de API**.
{% endalert %}

```csharp
var configuration = new BRZConfiguration("YOUR_API_KEY", "YOUR_ENDPOINT");
configuration.Api.AddSDKMetadata(new[] { BRZSDKMetadata.Xamarin });
braze = new Braze(configuration);
```

Consulte o arquivo `App.xaml.cs` no aplicativo de amostra [MAUI do iOS](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/App.xaml.cs).
{% endtab %}
{% endtabs %}

## Etapa 3: Teste a integração

{% tabs %}
{% tab Android %}
Agora você pode iniciar seu aplicativo e ver as sessões sendo registradas no dashboard do Braze (juntamente com informações do dispositivo e outras análises de dados). Para uma discussão mais aprofundada sobre as práticas recomendadas para a integração básica do SDK, consulte as [instruções de integração do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).
{% endtab %}

{% tab ios %}
Agora você pode iniciar seu aplicativo e ver as sessões sendo registradas no dashboard do Braze. Para uma discussão mais aprofundada sobre as práticas recomendadas para a integração básica do SDK, consulte as [instruções de integração do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overview/).

{% alert important %}
Nossa atual vinculação pública do Xamarin para o SDK do iOS não se conecta ao SDK do Facebook do iOS (vinculando dados sociais) e não inclui o envio do IDFA para a Braze.
{% endalert %}
{% endtab %}
{% endtabs %}
