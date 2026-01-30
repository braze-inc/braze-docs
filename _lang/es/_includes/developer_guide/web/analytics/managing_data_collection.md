## Desactivar el seguimiento de datos

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab standard implementation %}
Para desactivar la actividad de seguimiento de datos en el SDK Web, utiliza el método [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk). Esto sincronizará cualquier dato registrado antes de llamar a `disableSDK()`, y hará que se ignoren todas las llamadas posteriores al SDK de la Web de Braze para esta página y para futuras cargas de páginas.
{% endtab %}

{% tab google tag manager %}
Utiliza el tipo de etiqueta **Deshabilitar seguimiento** o **Reanudar seguimiento** para deshabilitar o volver a habilitar el seguimiento Web, respectivamente. Estas dos opciones llaman [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) y [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).
{% endtab %}
{% endtabs %}

### Buenas prácticas

Para ofrecer a los usuarios la opción de detener el seguimiento, recomendamos crear una página sencilla con dos enlaces o botones: uno que llame a `disableSDK()` al hacer clic, y otro que llame a `enableSDK()` para permitir a los usuarios volver a optar por la adhesión voluntaria. También puedes utilizar estos controles para iniciar o detener el seguimiento a través de otros subprocesadores de datos.

{% alert note %}
No es necesario inicializar el SDK de Braze para llamar a `disableSDK()`, lo que te permite desactivar el seguimiento de usuarios totalmente anónimos. Por el contrario,`enableSDK()` no inicializa el SDK de Braze, por lo que también debes llamar después a `initialize()` para habilitar el seguimiento.
{% endalert %}

## Reanudar el seguimiento de los datos

Para reanudar la recopilación de datos, puedes utilizar el método [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) método.
