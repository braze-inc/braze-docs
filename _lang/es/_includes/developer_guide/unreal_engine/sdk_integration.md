## Acerca del SDK Braze de Unreal Engine

Con el plugin Braze Unreal SDK, puedes:

* Mide y sigue las sesiones dentro de tu aplicación o juego
* Seguimiento de compras dentro de la aplicación y eventos personalizados
* Actualiza los perfiles de usuario con atributos estándar y personalizados
* Enviar notificaciones push
* Integra tus aplicaciones de Unreal con recorridos más extensos de Canvas
* Envía mensajería de canales cruzados, como correo electrónico o SMS, basándote en el comportamiento dentro de la aplicación.

## Integración del SDK de Unreal Engine

### Paso 1: Añade el plugin Braze

En tu terminal, clona el [repositorio GitHub del SDK Braze de Unreal Engine](https://github.com/braze-inc/braze-unreal-sdk).

```bash
git clone git@github.com:braze-inc/braze-unreal-sdk.git
```

A continuación, copia el directorio `BrazeSample/Plugins/Braze` y añádelo a la carpeta Plugin de tu aplicación.

### Paso 2: Habilitar el plugin

Habilita el plugin para tu proyecto C++ o Blueprint.

{% tabs %}
{% tab C++ %}
Para proyectos C++, configura tu módulo para que haga referencia al módulo Braze. En tu `\*.Build.cs file`, añade `"Braze"` a tu `PublicDependencyModuleNames`.

```cpp
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "Braze" });
```
{% endtab %}

{% tab Plano %}
Para los proyectos Blueprint, ve a **Configuración** > **Plugins**, y junto a **Braze** marca **Habilitado**.

![ActivarPlugin]({% image_buster /assets/img/unreal_engine/EnablePlugin.png %})
{% endtab %}
{% endtabs %}

### Paso 3: Configura tu clave de API y tu punto final

Configura tu clave de API y tu punto final en la página `DefaultEngine.ini` de tu proyecto.

```cpp
[/Script/Braze.BrazeConfig]
bAutoInitialize=True ; true by default, initialize when the project starts
AndroidApiKey= ; your API key
IOSApiKey= ; your API key
CustomEndpoint= ; your endpoint
```

{% alert warning %}
Para los proyectos dirigidos a Android SDK 31+, Unreal generará compilaciones que fallarán durante la instalación en dispositivos Android 12+ con el error INSTALL_PARSE_FAILED_MANIFEST_MALFORMED. Para solucionarlo, localiza el archivo de parche git `UE4_Engine_AndroidSDK_31_Build_Fix.patch` en la raíz de este repositorio y aplícalo a tu compilación fuente de Unreal.
{% endalert %}

### Paso 4: Inicializa manualmente el SDK (opcional)

Por defecto, el SDK se inicializa automáticamente al iniciarse. Si quieres tener más control sobre la inicialización (como esperar el consentimiento del usuario o establecer el nivel de registro), puedes desactivar `AutoInitialize` en tu `DefaultEngine.ini` e inicializar manualmente en C++ o Blueprint.

{% tabs %}
{% tab C++ %}
En C++ nativo, accede al BrazeSubsystem y llama a `InitializeBraze()` pasándole opcionalmente un Config para anular la configuración de Engine.ini.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab Plano %}
En Blueprint, las mismas funciones son accesibles como nodos Blueprint:  
Utiliza el nodo `GetBrazeSubsystem` para llamar a su nodo `Initialize`.  
Opcionalmente, se puede crear un objeto BrazeConfig en Blueprint y pasarlo a `Initialize`

![InicializarBraze]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}

## Configuraciones opcionales

### Registro

{% tabs local %}
{% tab Android %}
Puedes establecer el nivel de registro en tiempo de ejecución utilizando C++ o en un nodo Blueprint.

{% subtabs %}
{% subtab C++ %}
Para configurar el nivel de registro en tiempo de ejecución, llama a `UBrazeSubsystem::AndroidSetLogLevel`.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
BrazeSubsystem->AndroidSetLogLevel(EBrazeLogLevel::Verbose);
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endsubtab %}

{% subtab Blueprint %}
En Blueprint, puedes utilizar el nodo **Establecer nivel de registro de Android**:

![El nodo Android Establecer Nivel de Registro en Blueprint.]({% image_buster /assets/img/unreal_engine/AndroidSetLogLevel.png %})
{% endsubtab %}
{% endsubtabs %}

Para garantizar que el registro está configurado cuando se llama a Inicializar el SDK de Braze, se recomienda llamarlo antes de `InitializeBraze`.
{% endtab %}

{% tab iOS %}
Para habilitar el nivel de registro en `info.plist`, ve a **Configuración** > **Configuración del proyecto** y, a continuación, selecciona **iOS** en **Plataformas**. En **Datos PList Extra**, busca **Datos PList Adicionales**, e introduce tu nivel de registro:

```xml
<key>Appboy</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

El nivel de registro predeterminado es 8, que es el registro mínimo. Más información sobre los niveles de registro: [Otros SDK Personalizados]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)
{% endtab %}
{% endtabs %}
