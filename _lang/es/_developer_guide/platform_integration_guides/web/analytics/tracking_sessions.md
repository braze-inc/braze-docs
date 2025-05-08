---
nav_title: Seguimiento de sesiones
article_title: Seguimiento de sesiones para Web
platform: Web
page_order: 0
description: "Este artículo de referencia explica cómo hacer un seguimiento de las sesiones para la Web."

---

# Seguimiento de sesiones

> El SDK de Braze informa de los datos de sesión utilizados por el panel de Braze para calcular la participación de los usuarios y otros análisis esenciales para comprender a tus usuarios. Nuestro SDK genera puntos de datos de "inicio de sesión" y "cierre de sesión" que tienen en cuenta la duración de la sesión y los recuentos de sesiones visibles dentro del panel Braze, basándose en la siguiente semántica de sesión.

## Ciclo de vida de la sesión

Por predeterminado, las sesiones comienzan cuando se llama por primera vez a `braze.openSession()` y permanecen abiertas hasta al menos 30 minutos de inactividad. Esto significa que, si el usuario navega fuera del sitio y vuelve menos de 30 minutos después, continuará la misma sesión. Si vuelven una vez transcurridos los 30 minutos, se genera automáticamente un punto de datos de "cerrar sesión" para el tiempo en que navegaron fuera, y se abre una nueva sesión.

{% alert note %}
Si necesitas forzar una nueva sesión, puedes hacerlo cambiando de usuario.
{% endalert %}

## Personalizar el tiempo de espera de la sesión

Para personalizar el tiempo de espera de la sesión, pasa la opción `sessionTimeoutInSeconds` a tu función [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) función. El valor mínimo de `sessionTimeoutInSeconds` es 1 segundo.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` 

Si has establecido un tiempo de espera de la sesión, toda la semántica de la sesión se extiende a ese tiempo de espera personalizado.

## Probar el seguimiento de la sesión

Para detectar sesiones a través de tu usuario, busca a tu usuario en el panel y navega hasta **Uso de la aplicación** en el perfil de usuario. Puedes confirmar que el seguimiento de la sesión funciona comprobando que la métrica de la sesión aumenta cuando esperas que lo haga.

![Un componente de perfil de usuario que muestra cuántas sesiones se han producido, cuándo se utilizó la aplicación por primera vez y cuándo se utilizó por última vez.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%"}

