## Integrando o SDK .NET MAUI

Integrar o SDK Braze .NET MAUI (anteriormente Xamarin) fornecerá a você funcionalidades básicas de análise de dados, além de mensagens in-app com as quais você pode engajar seus usuários. 

### Pré-requisitos

Antes de integrar o SDK Braze .NET MAUI, certifique-se de atender aos seguintes requisitos:

- A partir de `version 3.0.0`, esse SDK requer o uso do .NET 6+ e remove o suporte para projetos que usam a estrutura Xamarin.
- A partir de `version 4.0.0`, este SDK deixou de dar suporte ao Xamarin & Xamarin.Forms e adicionou suporte ao .NET MAUI. Consulte [a política da Microsoft](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin) com relação ao fim do suporte para o Xamarin.

### Etapa 1: Obtenha o binding .NET MAUI

{% tabs %}
{% tab android %}
Um binding .NET MAUI é uma forma de usar bibliotecas nativas em apps .NET MAUI. A implementação de uma associação consiste em criar uma interface C# para a biblioteca e, em seguida, usar essa interface em seu aplicativo.  Veja a [.documentação .NET MAUI](http://developer.xamarin.com/guides/android/advanced_topics/java_integration_overview/binding_a_java_library_%28.jar%29/). Há duas maneiras de incluir a associação do SDK da Braze: usando o NuGet ou compilando a partir da fonte.

{% subtabs local %}
{% subtab NuGet %}
O método mais simples de integração envolve a obtenção do SDK da Braze no [NuGet.org](https://www.nuget.org/) repositório central. Na barra lateral do Visual Studio, clique com o botão direito do mouse na pasta `Packages` e clique em `Add Packages...`.  Procure por "Braze" e instale o pacote [`BrazePlatform.BrazeAndroidBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidBinding/) em seu projeto.

Para usar os serviços de localização e geofences do Braze, instale também o pacote [`BrazePlatform.BrazeAndroidLocationBinding`](https://www.nuget.org/packages/BrazePlatform.BrazeAndroidLocationBinding/).
{% endsubtab %}

{% subtab Source %}
O segundo método de integração é incluir a [fonte de ligação](https://github.com/braze-inc/braze-xamarin-sdk). Sob [`appboy-component/src/androidnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidNet6Binding) você encontrará nosso código-fonte do binding; adicionar uma referência de projeto ao ```BrazeAndroidBinding.csproj``` em sua aplicação .NET MAUI fará com que o binding seja construído com seu projeto e fornecerá acesso ao SDK Braze Android.

Para usar os serviços de localização e geofences do Braze, adicione também uma referência de projeto ao ```BrazeAndroidLocationBinding.csproj``` encontrado sob [`appboy-component/src/androidnet6/BrazeAndroidLocationBinding`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/androidnet6/BrazeAndroidLocationBinding).
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab ios %}
{% alert important %}
Os bindings iOS para a versão 4.0.0 do SDK .NET MAUI e posteriores usam o [SDK Braze Swift](https://github.com/braze-inc/braze-swift-sdk/), enquanto versões anteriores usam o [SDK AppboyKit legado](https://github.com/Appboy/Appboy-ios-sdk).
{% endalert %}

Um binding .NET MAUI é uma forma de usar bibliotecas nativas em apps .NET MAUI. A implementação de uma associação consiste em criar uma interface C# para a biblioteca e, em seguida, usar essa interface em seu aplicativo. Há duas maneiras de incluir a associação do SDK da Braze: usando o NuGet ou compilando a partir da fonte.

{% subtabs local %}
{% subtab NuGet %}
O método mais simples de integração envolve a obtenção do SDK da Braze no [NuGet.org](https://www.nuget.org/) repositório central. Na barra lateral do Visual Studio, clique com o botão direito do mouse na pasta `Packages` e clique em `Add Packages...`.  Pesquise por 'Braze' e instale os pacotes NuGet iOS .NET MAUI mais recentes: [Braze.iOS.BrazeKit](https://www.nuget.org/packages/Braze.iOS.BrazeKit), [Braze.iOS.BrazeUI](https://www.nuget.org/packages/Braze.iOS.BrazeUI), e [Braze.iOS.BrazeLocation](https://www.nuget.org/packages/Braze.iOS.BrazeLocation) em seu projeto.

Também fornecemos os pacotes de bibliotecas de compatibilidade: [Braze.iOS.BrazeKitCompat](https://www.nuget.org/packages/Braze.iOS.BrazeKitCompat) e [Braze.iOS.BrazeUICompat](https://www.nuget.org/packages/Braze.iOS.BrazeUICompat)para ajudar a facilitar sua migração para o .NET MAUI.
{% endsubtab %}

{% subtab Source %}
O segundo método de integração é incluir a [fonte de ligação](https://github.com/braze-inc/braze-xamarin-sdk). Sob [`appboy-component/src/iosnet6`](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/src/iosnet6/BrazeiOSNet6Binding) você encontrará nosso código-fonte do binding; adicionar uma referência de projeto ao ```BrazeiOSBinding.csproj``` em sua aplicação .NET MAUI fará com que o binding seja construído com seu projeto e fornecerá acesso ao SDK Braze iOS. Verifique se o site `BrazeiOSBinding.csproj` está sendo exibido na pasta "Reference" do seu projeto.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Etapa 2: Configure sua instância do Braze

{% tabs %}
{% tab android %}
#### Etapa 2.1: Configure o SDK da Braze em Braze.xml

Agora que as bibliotecas foram integradas, você precisa criar um arquivo `Braze.xml` na pasta `Resources/values` do seu projeto. O conteúdo desse arquivo deve se parecer com o seguinte trecho de código:

{% alert note %}
Certifique-se de substituir `YOUR_API_KEY` pela chave de API localizada em **Configurações** > **Chaves de API** no dashboard do Braze.
<br><br>
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), poderá encontrar as chaves de API em **Console do desenvolvedor** > **Configurações de API**.
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

#### Etapa 2.2: Adicionar permissões necessárias ao manifesto do Android

Agora que adicionou sua chave de API, você precisa adicionar as seguintes permissões ao arquivo `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
Para obter um exemplo de seu `AndroidManifest.xml`, consulte o aplicativo de amostra do [Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/AndroidManifest.xml).

#### Etapa 2.3: Rastreie as sessões de usuários e o registro de mensagens no app

Para ativar o rastreamento da sessão do usuário e registrar seu aplicativo para mensagens no app, adicione a seguinte chamada ao método de ciclo de vida `OnCreate()` da classe `Application` do seu aplicativo:

```kotlin
RegisterActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
```
{% endtab %}

{% tab ios %}
Ao configurar sua instância da Braze, adicione o seguinte snippet para configurar sua instância:

{% alert note %}
Certifique-se de substituir `YOUR_API_KEY` pela chave de API localizada em **Configurações** > **Chaves de API** no dashboard do Braze.

Se estiver usando a [navegação mais antiga]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), poderá encontrar as chaves de API em **Console do desenvolvedor** > **Configurações de API**.
{% endalert %}

```csharp
var configuration = new BRZConfiguration("YOUR_API_KEY", "YOUR_ENDPOINT");
configuration.Api.AddSDKMetadata(new[] { BRZSDKMetadata.Xamarin });
braze = new Braze(configuration);
```

Consulte o arquivo `App.xaml.cs` no aplicativo de amostra [MAUI do iOS](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/App.xaml.cs).
{% endtab %}
{% endtabs %}

### Etapa 3: Teste a integração

{% tabs %}
{% tab android %}
Agora você pode iniciar seu aplicativo e ver as sessões sendo registradas no dashboard do Braze (juntamente com informações do dispositivo e outras análises de dados). Para uma discussão mais aprofundada sobre as práticas recomendadas para a integração básica do SDK, consulte as [instruções de integração do Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android).
{% endtab %}

{% tab ios %}
Agora você pode iniciar seu aplicativo e ver as sessões sendo registradas no dashboard do Braze. Para uma discussão mais aprofundada sobre as práticas recomendadas para a integração básica do SDK, consulte as [instruções de integração do iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift).

{% alert important %}
Nosso binding público atual .NET MAUI para o SDK iOS não se conecta ao SDK Facebook iOS (vinculando dados sociais) e não inclui o envio do IDFA para o Braze.
{% endalert %}
{% endtab %}
{% endtabs %}
