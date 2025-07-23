## Integración del SDK de Roku

### Paso 1: Añadir archivos

Los archivos del SDK de Braze se encuentran en el directorio `sdk_files` del [repositorio del SDK de Roku de Braze](https://github.com/braze-inc/braze-roku-sdk).

1. Añade `BrazeSDK.brs` a tu aplicación en el directorio `source`.
2. Añade `BrazeTask.brs` y `BrazeTask.xml` a tu aplicación en el directorio `components`.

### Paso 2: Añadir referencias

Añade una referencia a `BrazeSDK.brs` en tu escena principal utilizando el siguiente elemento `script`:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Paso 3: Configura

En `main.brs`, establece la configuración de Braze en el nodo global:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Puedes encontrar tu [punto final SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) y tu clave de API en el panel de Braze.

### Paso 4: Inicializar Braze

Inicializa la instancia de Braze:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Configuraciones opcionales

### Registro

Para depurar tu integración Braze, puedes ver los registros de la consola de depuración de Roku para Braze. Consulta el [código de depuración](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) de los desarrolladores de Roku para obtener más información.
