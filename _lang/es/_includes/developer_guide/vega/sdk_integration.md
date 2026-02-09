## Acerca del SDK Braze Vega

El SDK Braze Vega te permite recopilar análisis y mostrar mensajes enriquecidos dentro de la aplicación a tus usuarios. La mayoría de los métodos del SDK de Braze Vega son asíncronos y devuelven promesas que deben esperarse o resolverse.

## Integración del SDK Braze Vega

### Paso 1: Instala la biblioteca Braze

Instala el SDK de Braze Vega con tu administrador de paquetes preferido.

{% tabs local %}
{% tab npm %}
Si tu proyecto utiliza NPM, puedes añadir el SDK de Braze Vega como dependencia.

```bash
npm install @braze/vega-sdk --save
```

Tras la instalación, puedes importar los métodos que necesites:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
Si tu proyecto utiliza Yarn, puedes añadir el SDK de Braze Vega como dependencia.

```bash
yarn add @braze/vega-sdk
```

Tras la instalación, puedes importar los métodos que necesites:

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### Paso 2: Inicializar el SDK

Una vez añadido el SDK Braze Vega a tu proyecto, inicializa la biblioteca con la clave de API y la [URL del punto final SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) que encontrarás en **Configuración** > **Configuración de la aplicación** dentro de tu panel Braze.

{% alert important %}
Debes esperar o resolver la promesa `changeUser` antes de llamar a otros métodos Braze, o los eventos y atributos pueden establecerse en el usuario incorrecto.
{% endalert %}

```javascript
import { useEffect } from "react-native";
import {
  initialize,
  changeUser,
  logCustomEvent,
  openSession,
  setCustomUserAttribute,
  setUserCountry
} from "@braze/vega-sdk";

const App = () => {
  useEffect(() => {
    const initBraze = async () => {
      // Initialize the SDK
      await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
        sessionTimeoutInSeconds: 60,
        appVersionNumber: "1.2.3.4",
        enableLogging: true, // set to `true` for debugging
      });

      // Change user
      await changeUser("user-id-123");
      
      // Start a session
      await openSession();
      
      // Log custom events and set user attributes
      logCustomEvent("visited-page", { pageName: "home" });
      setCustomUserAttribute("my-attribute", "my-attribute-value");
      setUserCountry("USA");
    };
    
    initBraze();
  }, []);
  
  return (
    // Your app components
  );
};
```

{% alert important %}
Los usuarios anónimos pueden contabilizarse en tu [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users). Como resultado, puede que quieras cargar o inicializar condicionalmente el SDK para excluir a estos usuarios de tu recuento de MAU.
{% endalert %}

## Configuraciones opcionales

### Registro

Puedes habilitar el registro del SDK para ayudar con la depuración y la solución de problemas. Hay varias formas de habilitar el registro.

#### Habilitar el registro durante la inicialización

Pasa `enableLogging: true` a `initialize()` para registrar mensajes de depuración en la consola:

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
Los registros básicos son visibles para todos los usuarios, así que considera desactivar el registro antes de poner tu código en producción.
{% endalert %}

#### Habilitar el registro tras la inicialización

Utiliza `toggleLogging()` para habilitar o deshabilitar el registro del SDK tras la inicialización:

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### Registro personalizado

Utiliza `setLogger()` para proporcionar una función de registro personalizada para tener más control sobre cómo se gestionan los registros del SDK:

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### Opciones de configuración

Puedes pasar opciones de configuración adicionales a `initialize()` para personalizar el comportamiento del SDK:

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 30 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## Actualizar el SDK

Cuando hagas referencia al SDK de Braze Vega desde NPM o Yarn, puedes actualizarte a la última versión actualizando la dependencia de tu paquete:

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## Prueba tu integración

Para verificar que tu integración de SDK funciona correctamente:

1. Inicializa el SDK con `enableLogging: true` para ver los mensajes de depuración en la consola.
2. Asegúrate de que `await changeUser()` antes de llamar a otros métodos del SDK
3. Llama a `await openSession()` para iniciar una sesión
4. Comprueba tu panel Braze en **Visión general** para verificar que se están registrando los datos de la sesión
5. Prueba a registrar un evento personalizado y comprueba que aparece en tu panel


