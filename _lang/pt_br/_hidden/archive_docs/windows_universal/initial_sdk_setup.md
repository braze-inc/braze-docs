---
nav_title: Configuração inicial do SDK
article_title: Configuração inicial do SDK para Windows Universal
platform: Windows Universal
page_order: 0
description: "Este artigo de referência aborda as etapas iniciais para integrar o SDK da Braze em sua plataforma Windows Universal."
search_rank: 1
hidden: true
---

# Integração inicial de SDK
{% multi_lang_include archive/windows_deprecation.md %}

O Braze SDK fornecerá uma API para relatar informações a serem usadas em análise de dados, segmentação e engajamento, bem como a capacidade de registrar usuários para notificações por push e receber notificações.

>  O Windows Universal SDK também é compatível com os apps .NET MAUI Windows.

## Etapa 1: Instale o SDK por meio do gerenciador de pacotes NuGet

O Windows Universal SDK é instalado por meio do [NuGet Package Manager][14]. Para instalar o Braze Windows SDK via NuGet:

1. Clique com o botão direito do mouse no arquivo de projeto
2. Clique em "Manage NuGet Packages" (Gerenciar pacotes NuGet)
3. Clique em "Online" no menu suspenso à esquerda
4. Pesquise "Appboy" em "NuGet.org"
5. Clique no pacote NuGet "AppboyPlatform.Universal.Release" e clique em Instalar

>  A Biblioteca Universal do Windows deve ser usada para todos os apps Windows 8.1, Windows Phone 8.1 e UWP.

## Etapa 2: Criação e configuração de AppboyConfiguration.xml

Crie um arquivo chamado `AppboyConfiguration.xml` no diretório raiz do seu projeto e adicione o seguinte trecho de código a esse arquivo:

```xml
    <?xml version="1.0" encoding="utf-8"?>
    <AppboyConfig>
        <ApiKey>YOUR_API_KEY_HERE</ApiKey>
    </AppboyConfig>
```

>  Não se esqueça de atualizar `YOUR_API_KEY_HERE` com sua chave de API, que pode ser encontrada na página [Chaves de API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/).

Depois de adicionar esse snippet, não se esqueça de modificar as seguintes propriedades de arquivo para `AppboyConfiguration.xml`

1. Defina `Build Action` como `Content`
2. Defina `Copy to Output Directory` como `Copy Always`

## Etapa 3: Configuração do package.appxmanifest

Na guia "Capabilities" (Recursos), verifique se a opção `Internet (Client)` está marcada.
![][18]

## Etapa 4: Edição da classe do app

- Adicione o seguinte a `usings` de seu arquivo `App.xaml.cs`:

```csharp
using AppboyPlatform.PCL.Managers;
using AppboyPlatform.Universal;
using AppboyPlatform.Universal.Managers.PushArgs;
```

- Chame o seguinte em seu método de ciclo de vida `OnLaunched`:

```csharp
Appboy.SharedInstance.OpenSession();
```

- Chame o seguinte em seu método de ciclo de vida `OnSuspending`:

```csharp
Appboy.SharedInstance.CloseSession();
```

## Integração básica de SDK concluída

Agora, o Braze deve estar coletando dados do seu aplicativo. Consulte os artigos a seguir sobre como registrar [atribuições]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/setting_custom_attributes/), [eventos]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_custom_events) e [compras]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/analytics/logging_purchases) em nosso SDK e como instrumentar o envio de mensagens push.

>  Se estiver usando o projeto Braze Unity no mesmo app, talvez seja necessário qualificar totalmente as chamadas na Braze como "AppboyPlatform.Universal.Appboy"

[14]: http://www.nuget.org/
[18]: {% image_buster /assets/img_archive/internet_client.png %}
