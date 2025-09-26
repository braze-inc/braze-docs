---
nav_title: Conocimiento de las funciones y nueva versión de la aplicación
article_title: Conocimiento de las funciones y nueva versión de la aplicación
page_order: 9
page_type: reference
description: "En este artículo de referencia se explica cómo mantener a los usuarios informados y entusiasmados cuando se lanzan nuevas funciones o versiones."
tool: Campaigns

---

# Conocimiento de las funciones y nueva versión de la aplicación

> Este artículo de referencia aborda cómo utilizar la plataforma Braze para mantener a sus clientes al día de las nuevas funciones y versiones de su aplicación. 

Trabajas duro para actualizar y mejorar continuamente tu aplicación, y quieres que tus usuarios experimenten estas nuevas y emocionantes funciones y nuevas versiones de la aplicación. Aprenda a enseñar a sus usuarios las nuevas funciones que aún no han utilizado y anímeles a explorar la aplicación para sacar el máximo partido a sus ofertas.

Las campañas de concienciación sobre las funciones son una forma estupenda de animar a los usuarios a seguir utilizando su aplicación a medida que mejora su funcionalidad.  Mantener a los usuarios al día es una buena forma de mantenerlos activos, aumentar las valoraciones y garantizar la participación de los usuarios.

## Filtrar por las versiones más recientes de la aplicación

Los SDK de Braze rastrean automáticamente la versión más reciente de la aplicación del usuario. Estas versiones pueden utilizarse en filtros y segmentos para determinar qué usuarios deben recibir un mensaje o una campaña.

![El panel Opciones de segmentación en el paso Usuarios objetivo del flujo de trabajo de creación de campañas. La sección Filtros adicionales incluye el siguiente filtro "El número de versión de la aplicación más reciente para Android Cronómetro (Android) es inferior a 3.7.0 (134.0.0.0)".]({% image_buster /assets/img_archive/new_app_version.png %}){: style="max-width:90%;"}

### Número de versión de la aplicación

Utilice el filtro **Número de versión de la aplicación** para segmentar a los usuarios según la versión y el número de compilación de la aplicación. 

Este filtro admite comparaciones numéricas para apuntar a un rango de versiones de aplicación. Por ejemplo, puede dirigirse a usuarios cuya aplicación sea "inferior", "superior" e "igual" a la versión "1.2.3" de la aplicación, lo que podría ser beneficioso para promocionar una nueva función que requiera una actualización de la aplicación.

Este nuevo filtro puede sustituir al antiguo filtro "Nombre de versión de la aplicación", que requería enumerar explícitamente cada versión antigua o utilizar una expresión regular.

**Cómo funciona**

* Cada parte de la versión `major.minor.patch` enviada en la versión de la aplicación de su aplicación se comparan como enteros
* Si los números mayores son iguales, se comparan los números menores, etc.

**Importante**

* Las aplicaciones de Android tienen tanto una versión legible por humanos [`versionName`](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) y una interna [`versionCode`](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()). El filtro Número de versión de la aplicación utiliza `versionCode` porque está garantizado que se incrementa con cada lanzamiento de la tienda de aplicaciones.
* Esto puede causar confusión cuando `versionName` y `versionCode` de su aplicación no están sincronizados, sobre todo porque ambos campos se pueden ver desde el panel Braze. Como práctica recomendada, compruebe que las direcciones `versionName` y `versionCode` de su aplicación se incrementan juntas.
* Si necesita filtrar por el campo `versionName` legible por humanos (poco común), utilice el filtro Nombre de versión de la aplicación.

#### Requisitos del SDK

Los valores de este filtro se recopilan a partir del SDK para Android v3.6.0+ y el SDK para iOS v3.21.0+ de Braze. Aunque este filtro tiene requisitos de SDK, podrás dirigirte a usuarios de versiones inferiores (antiguas) de tu aplicación utilizando esta función.

Para Android, este número de versión se basa en el [código de versión larga del paquete](https://developer.android.com/reference/android/content/pm/PackageInfo.html#getLongVersionCode()) de la aplicación.

Para iOS, este número de versión se basa en la [cadena de versión abreviada](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) de la aplicación.

{% alert tip %}
Este filtro rellenará los valores después de que los usuarios actualicen sus aplicaciones a las versiones Braze SDK compatibles. Hasta entonces, el filtro no mostrará ninguna versión al seleccionarlo.
{% endalert %}

#### Caso de uso

En el siguiente escenario, supongamos que primero actualizaste a los SDK de Braze, que admiten este filtro en la versión `2.0.0` de tu aplicación.

Una vez que Braze reciba los datos de la versión 2.0.0 de su aplicación, podrá dirigirse a usuarios con versiones anteriores o posteriores.

| Filtro  | Versión de la aplicación del usuario  | Resultado |
:------------- | :----------- | :---------|
| Inferior a 2.0.0 | 1.0.0 | El usuario está en el segmento, aunque su SDK de Braze no admitía el filtro "Número de versión de la aplicación". |
| Superior a 2.0.0 | 2.5.1 | El usuario y todas las futuras instalaciones estarán en el segmento. |
| Superior a 2.0.0 | 1.9.9 | El usuario no está en el segmento. |
| Inferior o igual a 2.0.0 | 3.0.1 | El usuario no está en el segmento. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Nombre de la versión de la aplicación

Utilice el filtro "Nombre de la versión de la aplicación" para segmentar a los usuarios por el "nombre de compilación" de la aplicación de cara al usuario. 

Este filtro admite coincidencias con "is", "is not" y expresiones regulares. Por ejemplo, puede dirigirse a usuarios que tengan una aplicación que no sea de la versión "1.2.3-test-build".

Para Android, este nombre de versión se basa en el [Nombre de versión del paquete](https://developer.android.com/reference/android/content/pm/PackageInfo#versionName) de la aplicación. Para iOS, este nombre de versión se basa en la [cadena de versión abreviada](https://developer.apple.com/documentation/bundleresources/information_property_list/cfbundleshortversionstring) de la aplicación.

### No he utilizado la característica

Cuando se lanza una nueva versión de la aplicación y se introducen nuevas funciones, es posible que los usuarios no perciban el nuevo contenido. Llevar a cabo una campaña de concienciación sobre las funciones es una forma estupenda de enseñar a los usuarios nuevas funciones o funciones que nunca han utilizado. Para ello, debes crear un [atributo personalizado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) que se asigne a los usuarios que nunca han completado una determinada acción dentro de tu aplicación o utilizar un [evento personalizado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#custom-data) para realizar el seguimiento de una acción concreta. Puede utilizar este atributo (o evento) para segmentar los usuarios a los que desea enviar la campaña.

{% alert tip %}
¿Quieres reorientar a una parte específica de tu audiencia? Consulte [Campañas de reorientación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/) para aprender a reorientar campañas aprovechando las acciones anteriores de sus usuarios.
{% endalert %}


