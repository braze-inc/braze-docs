## Acerca de Google Tag Manager para Web {#google-tag-manager}

Google Tag Manager (GTM) te permite añadir, eliminar y editar etiquetas de forma remota en tu sitio web sin necesidad de liberar código de producción ni recursos de ingeniería. Braze ofrece las siguientes plantillas para el SDK Web:

|Tipo de etiqueta|Casos de uso|
|--------|--------|
| Etiqueta de inicialización | Esta etiqueta te permite [integrar el SDK de Web Braze]({{site.baseurl}}/developer_guide/sdk_integration/?tab=google%20tag%20manager&sdktab=web) sin necesidad de modificar el código de tu sitio.|
| Etiqueta de acción | Esta etiqueta te permite [crear tarjetas de contenido]({{site.baseurl}}/developer_guide/content_cards/?sdktab=web#web_using-google-tag-manager), [establecer atributos de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?tab=google%20tag%20manager&sdktab=web) y [administrar la recopilación de datos]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?tab=google%20tag%20manager&sdktab=web).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Política de consentimiento del usuario de la UE de Google

{% alert important %}
Google está actualizando su [Política de Consentimiento de Usuario de la UE](https://www.google.com/about/company/user-consent-policy/) en respuesta a los cambios en la [Ley de Mercados Digitales (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que entrará en vigor el 6 de marzo de 2024. Este nuevo cambio obliga a los anunciantes a revelar determinada información a sus usuarios finales del EEE y del Reino Unido, así como a obtener de ellos los consentimientos necesarios. Consulte la siguiente documentación para obtener más información.
{% endalert %}

Como parte de la Política de consentimiento del usuario de la UE de Google, los siguientes atributos personalizados booleanos deben registrarse en los perfiles de usuario:

- `$google_ad_user_data`
- `$google_ad_personalization`

Si los configuras a través de la integración GTM, los atributos personalizados requieren la creación de una etiqueta HTML personalizada. A continuación se muestra un ejemplo de cómo registrar estos valores como tipos de datos booleanos (no como cadenas):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Para más información, consulta [Sincronización de audiencias con Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).
