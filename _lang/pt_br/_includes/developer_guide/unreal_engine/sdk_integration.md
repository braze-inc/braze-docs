## Sobre o SDK Braze do Unreal Engine

Com o plugin Braze Unreal SDK, você pode:

* Meça e rastreie sessões em seu app ou jogo
* Rastreamento de compras no aplicativo e eventos personalizados
* Atualizar perfis de usuário com atributos padrão e personalizados
* Enviar notificações por push
* Integre seus apps Unreal com jornadas maiores do Canva
* Envie mensagens entre canais, como e-mail ou SMS, com base no comportamento no app

## Integrando o SDK do Unreal Engine

### Etapa 1: Adicione o plugin Braze

No seu terminal, clone o repositório do GitHub [Unreal Engine Braze SDK](https://github.com/braze-inc/braze-unreal-sdk).

```bash
git clone git@github.com:braze-inc/braze-unreal-sdk.git
```

Em seguida, copie o diretório `BrazeSample/Plugins/Braze` e adicione-o na pasta de Plugins do seu app.

### Etapa 2: Ative o plugin

Ative o plugin para seu projeto C++ ou Blueprint.

{% tabs %}
{% tab C++ %}
Para projetos C++, configure seu módulo para referenciar o módulo Braze. No seu `\*.Build.cs file`, adicione `"Braze"` ao seu `PublicDependencyModuleNames`.

```cpp
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "Braze" });
```
{% endtab %}

{% tab Blueprint %}
Para projetos Blueprint, acesse **Configurações** > **Plugins**, então ao lado de **Braze** marque **Ativado**.

![AtivarPlugin]({% image_buster /assets/img/unreal_engine/EnablePlugin.png %})
{% endtab %}
{% endtabs %}

### Etapa 3: Defina sua chave de API e endpoint

Defina sua chave de API e endpoint no `DefaultEngine.ini` do seu projeto.

```cpp
[/Script/Braze.BrazeConfig]
bAutoInitialize=True ; true by default, initialize when the project starts
AndroidApiKey= ; your API key
IOSApiKey= ; your API key
CustomEndpoint= ; your endpoint
```

{% alert warning %}
Para projetos que visam Android SDK 31+, o Unreal gerará builds que falharão durante a instalação em dispositivos Android 12+ com o erro INSTALL_PARSE_FAILED_MANIFEST_MALFORMED. Para corrigir isso, localize o arquivo de patch git `UE4_Engine_AndroidSDK_31_Build_Fix.patch` na raiz deste repositório e aplique-o na sua build de fonte do Unreal.
{% endalert %}

## Configurações opcionais

### Registro

{% tabs local %}
{% tab Android %}
Você pode definir o nível de log em tempo de execução usando C++ ou em um nó Blueprint.

{% subtabs %}
{% subtab C++ %}
Para definir o nível de log em tempo de execução, chame `UBrazeSubsystem::AndroidSetLogLevel`.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
BrazeSubsystem->AndroidSetLogLevel(EBrazeLogLevel::Verbose);
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endsubtab %}

{% subtab Blueprint %}
No Blueprint, você pode usar o nó **Android Definir Nível de Log**:

![O nó Android Definir Nível de Log no Blueprint.]({% image_buster /assets/img/unreal_engine/AndroidSetLogLevel.png %})
{% endsubtab %}
{% endsubtabs %}

Para garantir que o registro esteja definido quando o Braze SDK Initialize for chamado, é recomendável chamar isso antes de `InitializeBraze`.
{% endtab %}

{% tab iOS %}
Para ativar o nível de log no `info.plist`, acesse **Configurações** > **Configurações do Projeto**, em seguida, selecione **iOS** em **Plataformas**. Em **Dados Extra do PList**, encontre **Dados Adicionais do Plist**, em seguida, insira seu nível de log:

```xml
<key>Appboy</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

O nível de log padrão é 8, que é o registro mínimo. Leia mais sobre níveis de log: [Outra Personalização de SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)
{% endtab %}
{% endtabs %}
