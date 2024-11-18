---
nav_title: Desactivar el seguimiento del SDK Web
article_title: Desactivar el seguimiento del SDK Web
platform: Web
page_order: 6
page_type: reference
description: "Este artículo trata sobre la desactivación del seguimiento del SDK Web, incluyendo por qué, cómo y las implicaciones de hacerlo para la Web."

---

# Desactivar el seguimiento del SDK Web

{% multi_lang_include archive/web-v4-rename.md %}

> Para cumplir la normativa sobre privacidad de datos, la actividad de seguimiento de datos en el SDK Web puede detenerse por completo utilizando el método [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). 

Este método sincronizará todos los datos registrados antes de llamar a `disableSDK()`, y hará que se ignoren todas las llamadas posteriores al SDK de la Web de Braze para esta página y para futuras cargas de páginas. Si deseas reanudar la recopilación de datos en un momento posterior, puedes utilizar el método [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) para reanudar la recopilación de datos.

Si deseas ofrecer a los usuarios la opción de detener el seguimiento, te recomendamos que crees una página sencilla con dos enlaces o botones, uno que llame a `disableSDK()` cuando se haga clic en él, y otro que llame a `enableSDK()` para permitir a los usuarios volver a optar por la adhesión voluntaria. También puedes utilizar estos controles para iniciar o detener el seguimiento a través de otros subprocesadores de datos.

Ten en cuenta que no es necesario inicializar el SDK de Braze para llamar a `disableSDK()`, lo que te permite desactivar el seguimiento de usuarios totalmente anónimos. Por el contrario,`enableSDK()` no inicializa el SDK de Braze, por lo que también debes llamar después a `initialize()` para habilitar el seguimiento.
