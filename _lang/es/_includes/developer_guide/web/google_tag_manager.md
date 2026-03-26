## Acerca de Google Tag Manager para Web {#google-tag-manager}

Google Tag Manager (GTM) te permite añadir, eliminar y editar etiquetas de forma remota en tu sitio web sin necesidad de liberar código de producción ni recursos de ingeniería. Braze ofrece las siguientes plantillas para el SDK Web:

|Tipo de etiqueta|Casos de uso|
|--------|--------|
| Etiqueta de inicialización | Esta etiqueta te permite [integrar el SDK Web de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) sin necesidad de modificar el código de tu sitio.|
| Etiqueta de acción | Esta etiqueta te permite [crear Tarjetas de contenido]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [establecer atributos de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) y [administrar la recopilación de datos]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Registro de eventos personalizados con GTM

Puedes registrar eventos personalizados utilizando una etiqueta **Custom HTML** en GTM. Este enfoque utiliza la [capa de datos](https://developers.google.com/tag-platform/tag-manager/datalayer) de GTM para pasar datos de eventos desde tu sitio a una etiqueta GTM que llama al SDK Web de Braze.

### Paso 1: Envía el evento a la capa de datos

En el código de tu sitio, envía un evento a la capa de datos en cualquier lugar donde quieras desencadenar el evento personalizado. Por ejemplo, para registrar un evento personalizado cuando se hace clic en un botón:

```html
<button onclick="dataLayer.push({'event': 'my_custom_event'});">Track Event</button>
```

### Paso 2: Crea un activador en GTM

1. En tu contenedor de GTM, ve a **Triggers** y crea un nuevo activador.
2. Establece el **Trigger Type** en **Custom Event**.
3. Establece el **Event Name** con el mismo valor que enviaste a la capa de datos (por ejemplo, `my_custom_event`).
4. Elige cuándo debe activarse el activador (por ejemplo, **All Custom Events**).

### Paso 3: Crea una etiqueta Custom HTML

1. En GTM, ve a **Tags** y crea una nueva etiqueta.
2. Establece el **Tag Type** en **Custom HTML**.
3. En el campo HTML, añade lo siguiente:

    ```html
    <script>
    window.braze.logCustomEvent("my_custom_event");
    </script>
    ```

4. En **Triggering**, selecciona el activador que creaste en el paso 2.
5. Guarda y publica tu contenedor.

Para incluir propiedades del evento, pásalas como segundo argumento:

```html
<script>
window.braze.logCustomEvent("my_custom_event", {"property_key": "property_value"});
</script>
```

## Política de consentimiento del usuario de la UE de Google

{% alert important %}
Google está actualizando su [Política de consentimiento del usuario de la UE](https://www.google.com/about/company/user-consent-policy/) en respuesta a los cambios en la [Ley de Mercados Digitales (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que está en vigor desde el 6 de marzo de 2024. Este nuevo cambio obliga a los anunciantes a revelar determinada información a sus usuarios finales del EEE y del Reino Unido, así como a obtener de ellos los consentimientos necesarios. Consulta la siguiente documentación para obtener más información.
{% endalert %}

Como parte de la Política de consentimiento del usuario de la UE de Google, los siguientes atributos personalizados booleanos deben registrarse en los perfiles de usuario:

- `$google_ad_user_data`
- `$google_ad_personalization`

Si los configuras a través de la integración con GTM, los atributos personalizados requieren la creación de una etiqueta HTML personalizada. A continuación se muestra un ejemplo de cómo registrar estos valores como tipos de datos booleanos (no como cadenas):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Para más información, consulta [Sincronización de audiencias con Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).