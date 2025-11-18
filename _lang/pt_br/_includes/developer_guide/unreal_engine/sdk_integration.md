## Sobre o SDK do Unreal Engine Braze

Com o plug-in Braze Unreal SDK, você pode:

* Meça e rastreie sessões em seu app ou jogo
* Rastreamento de compras no aplicativo e eventos personalizados
* Atualizar perfis de usuário com atributos padrão e personalizados
* Enviar notificações por push
* Integre seus apps Unreal com jornadas maiores do Canva
* Envie mensagens entre canais, como e-mail ou SMS, com base no comportamento no app

## Integração do Unreal Engine SDK

### Etapa 1: Adicionar o plug-in Braze

Em seu terminal, clone o [repositório do GitHub do Unreal Engine Braze SDK](https://github.com/braze-inc/braze-unreal-sdk).

```bash
git clone git@github.com:braze-inc/braze-unreal-sdk.git
```

Em seguida, copie o diretório `BrazeSample/Plugins/Braze` e adicione-o à pasta Plugin de seu app.

### Etapa 2: Ativar o plug-in

Ative o plug-in para seu projeto C++ ou Blueprint.

{% tabs %}
{% tab C++ %}
Para projetos C++, configure seu módulo para fazer referência ao módulo Braze. Em seu `\*.Build.cs file`, adicione `"Braze"` ao seu `PublicDependencyModuleNames`.

```cpp
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "Braze" });
```
{% endtab %}

{% tab Projeto %}
Para projetos Blueprint, acesse **Settings** > **Plugins** e, ao lado de **Braze**, marque **Ativado**.

![EnablePlugin]({% image_buster /assets/img/unreal_engine/EnablePlugin.png %})
{% endtab %}
{% endtabs %}

### Etapa 3: Defina sua chave de API e seu ponto de extremidade

Defina a chave de API e o ponto de extremidade no site `DefaultEngine.ini`. de seu projeto.

```cpp
[/Script/Braze.BrazeConfig]
bAutoInitialize=True ; true by default, initialize when the project starts
AndroidApiKey= ; your API key
IOSApiKey= ; your API key
CustomEndpoint= ; your endpoint
```

{% alert warning %}
Para projetos com direcionamento para o Android SDK 31+, a Unreal gerará compilações que falharão durante a instalação em dispositivos Android 12+ com o erro INSTALL_PARSE_FAILED_MANIFEST_MALFORMED. Para corrigir isso, localize o arquivo de patch git `UE4_Engine_AndroidSDK_31_Build_Fix.patch` na raiz deste repositório e aplique-o à compilação de código-fonte do Unreal.
{% endalert %}

### Etapa 4: Inicializar manualmente o SDK (opcional)

Por padrão, o SDK é inicializado automaticamente no lançamento. Se desejar ter mais controle sobre a inicialização (como aguardar o consentimento do usuário ou definir o nível de registro), poderá desativar o `AutoInitialize` no seu `DefaultEngine.ini` e inicializar manualmente no C++ ou no Blueprint.

{% tabs %}
{% tab C++ %}
Em C++ nativo, acesse o BrazeSubsystem e chame `InitializeBraze()` passando a ele, opcionalmente, um Config para substituir as configurações de Engine.ini.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab Projeto %}
No Blueprint, as mesmas funções podem ser acessadas como nós do Blueprint:  
Use o nó `GetBrazeSubsystem` para chamar seu nó `Initialize`.  
Um objeto BrazeConfig pode ser criado opcionalmente no Blueprint e passado para `Initialize`

![InitializeBraze]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}

## Configurações opcionais

### Registro

{% tabs local %}
{% tab Android %}
É possível definir o nível de registro em tempo de execução usando C++ ou em um nó do Blueprint.

{% subtabs %}
{% subtab C++ %}
Para definir o nível de registro em tempo de execução, chame `UBrazeSubsystem::AndroidSetLogLevel`.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
BrazeSubsystem->AndroidSetLogLevel(EBrazeLogLevel::Verbose);
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endsubtab %}

{% subtab Blueprint %}
No Blueprint, você pode usar o nó **Android Set Log Level**:

![O nó Android Set Log Level no Blueprint.]({% image_buster /assets/img/unreal_engine/AndroidSetLogLevel.png %})
{% endsubtab %}
{% endsubtabs %}

Para garantir que o registro seja definido quando o Braze SDK Initialize for chamado, é recomendável chamá-lo antes de `InitializeBraze`.
{% endtab %}

{% tab iOS %}
Para ativar o nível de registro no site `info.plist`, vá para **Settings** > **Project Settings** e selecione **iOS** em **Platforms**. Em **Extra PList Data**, localize **Additional Plist Data** e insira seu nível de registro:

```xml
<key>Appboy</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

O nível de registro padrão é 8, que é o registro mínimo. Leia mais sobre os níveis de registro: [Outras personalizações do SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)
{% endtab %}
{% endtabs %}
