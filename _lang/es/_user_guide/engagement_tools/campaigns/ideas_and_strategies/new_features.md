---
nav_title: Conocimiento de las características y nueva versión de la aplicación
article_title: Conocimiento de las características y nueva versión de la aplicación
page_order: 9
page_type: reference
description: "Este artículo de referencia trata sobre cómo mantener a tus usuarios informados y entusiasmados cuando lanzas nuevas características o versiones."
tool: Campaigns

---

# Conocimiento de las características y nueva versión de la aplicación

> Este artículo de referencia trata de cómo utilizar la plataforma Braze para mantener a tus clientes al día de las nuevas características y versiones de tu aplicación. 

Trabajas duro para actualizar y mejorar continuamente tu aplicación, y quieres que tus usuarios experimenten estas emocionantes nuevas características y nuevas versiones de la aplicación. Aprende a enseñar a tus usuarios las nuevas características que aún no han utilizado, y anímales a explorar la aplicación para sacar el máximo partido de lo que puedes ofrecerles.

Las campañas de concienciación sobre características son una forma estupenda de animar a los usuarios a seguir interactuando con tu aplicación mientras sigues mejorando la funcionalidad de tu aplicación.  Mantener a los usuarios al día es una forma estupenda de mantenerlos activos, aumentar las valoraciones y garantizar la interacción de los usuarios.

## Filtrar por las versiones más recientes de la aplicación

Los SDK de Braze hacen un seguimiento automático de la versión más reciente de la aplicación del usuario. Estas versiones pueden utilizarse en filtros y segmentos para determinar qué usuarios deben recibir un mensaje o una campaña.

El panel Opciones de segmentación en el paso Usuarios objetivo del flujo de trabajo de creación de campañas. La sección Filtros adicionales incluye el siguiente filtro "El número de versión más reciente de la aplicación Cronómetro Android (Android) es inferior a 3.7.0 (134.0.0.0)".]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

{% alert note %}
Las versiones actuales de la aplicación pueden tardar un poco en aparecer. La versión de la aplicación en el perfil de usuario se actualiza cuando la información es capturada por el SDK, que se basa en el momento en que los usuarios abren sus aplicaciones. Si el usuario no abre la aplicación, la versión actual no se actualizará. <br><br> Estos filtros tampoco se aplicarán con carácter retroactivo. Es bueno utilizar "mayor que" o "igual" a las versiones actuales y futuras, pero utilizar filtros de versiones anteriores puede provocar comportamientos inesperados.
{% endalert %}

### Número de versión de la aplicación

Utiliza el filtro **Número de versión de la aplicación** para segmentar a los usuarios según la versión y el número de compilación de la aplicación. 

Este filtro admite comparaciones numéricas para apuntar a un rango de versiones de aplicación. Por ejemplo, puedes dirigirte a usuarios cuya aplicación esté "por debajo", "por encima" e "igual" de la versión de la aplicación "1.2.3", lo que podría ser beneficioso para promocionar una nueva característica que requiera una actualización de la aplicación.

Este nuevo filtro puede sustituir al antiguo filtro "Nombre de la versión de la aplicación", que requería enumerar explícitamente cada versión antigua o utilizar una expresión regular.

**Cómo funciona**

* Cada parte de la versión `major.minor.patch` enviada en la versión de la aplicación de tu aplicación se comparan como enteros
* Si los números mayores son iguales, se comparan los números menores, etc.

**Importante**

* Las aplicaciones de Android tienen tanto una versión legible por humanos [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) y una interna [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()). El filtro Número de versión de la aplicación utiliza `versionCode` porque está garantizado que se incrementa con cada lanzamiento de la tienda de aplicaciones.
* Esto puede causar confusión cuando `versionName` y `versionCode` de tu aplicación no estén sincronizados, sobre todo porque ambos campos pueden verse desde el panel de Braze. Como buena práctica, comprueba que `versionName` y `versionCode` de tu aplicación se incrementan juntos.
* Si necesitas filtrar por el campo `versionName` legible por humanos (poco común), utiliza el filtro Nombre de la versión de la aplicación.

#### Requisitos del SDK

Los valores de este filtro se recopilan a partir de Braze Android SDK v3.6.0+ y iOS SDK v3.21.0+. Aunque este filtro tiene requisitos de SDK, ¡podrás dirigirte a usuarios que estén en versiones inferiores (antiguas) de tu aplicación utilizando esta característica!

Para Android, este número de versión se basa en el [código de versión larga del paquete](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) de la aplicación.

Para iOS, este número de versión se basa en la [cadena de versión abreviada](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) de la aplicación.

{% alert tip %}
Este filtro rellenará los valores después de que los usuarios actualicen sus aplicaciones a las versiones compatibles del SDK de Braze. Hasta entonces, el filtro no mostrará ninguna versión al seleccionarlo.
{% endalert %}

#### Casos de uso

En el siguiente escenario, supongamos que primero actualizaste a los SDK de Braze, que admiten este filtro en la versión `2.0.0` de tu aplicación.

Una vez que Braze reciba datos de la versión 2.0.0 de tu aplicación, podrás dirigirte a usuarios con versiones anteriores o posteriores.

| Filtrar  | Versión de la aplicación para el usuario  | Resultado |
:------------- | :----------- | :---------|
| Menos de 2.0.0 | 1.0.0 | El usuario está en el segmento, aunque su SDK de Braze no admitía el filtro "Número de versión de la aplicación". |
| Superior a 2.0.0 | 2.5.1 | El usuario y todas las futuras instalaciones estarán en el segmento. |
| Superior a 2.0.0 | 1.9.9 | El usuario no está en el segmento. |
| Inferior o igual a 2.0.0 | 3.0.1 | El usuario no está en el segmento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Nombre de la versión de la aplicación

Utiliza el filtro "Nombre de versión de la aplicación" para segmentar a los usuarios según el "nombre de compilación" de la aplicación de cara al usuario. 

Este filtro admite coincidencias con "es", "no es" y expresiones regulares. Por ejemplo, puedes dirigirte a usuarios que tengan una aplicación que no sea de la versión "1.2.3-test-build".

Para Android, este nombre de versión se basa en el [Nombre de versión del paquete](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) de la aplicación. Para iOS, este nombre de versión se basa en la [cadena de versión abreviada](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) de la aplicación.

### No he utilizado la característica

Cuando lanzas una nueva versión de la aplicación e introduces nuevas características, es posible que los usuarios no perciban el nuevo contenido. Llevar a cabo una campaña de concienciación sobre las características es una forma estupenda de enseñar a los usuarios nuevas características o características que nunca han utilizado. Para ello, debes crear un [atributo personalizado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) que se asigne a los usuarios que nunca han completado una determinada acción dentro de tu aplicación o utilizar un [evento personalizado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) para realizar el seguimiento de una acción concreta. Puedes utilizar este atributo (o evento) para segmentar a los usuarios a los que quieres enviar la campaña.

{% alert tip %}
¿Quieres reorientar a una parte específica de tu audiencia? Consulta [Campañas de reorientación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/) para aprender a reorientar campañas aprovechando las acciones anteriores de tu usuario.
{% endalert %}


