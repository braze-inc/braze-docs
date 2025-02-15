---
nav_title: Creación y gestión de espacios de trabajo
article_title: Creación y gestión de espacios de trabajo
page_order: 0
page_type: reference
description: "Este artículo explica cómo crear, configurar y gestionar tus espacios de trabajo."

---

# Creación y gestión de espacios de trabajo

> Este artículo explica cómo crear, configurar y gestionar tus espacios de trabajo. 

## ¿Qué es un espacio de trabajo?

Todo lo que haces en Braze ocurre dentro de un espacio de trabajo. Los espacios de trabajo son un entorno compartido para que rastrees y gestiones la participación en aplicaciones móviles o sitios web relacionados. Los espacios de trabajo agrupan aplicaciones iguales o muy similares: por ejemplo, las versiones para Android e iOS de tu aplicación móvil. 

## Crear un espacio de trabajo

### Paso 1: Ten un plan

Antes de empezar, asegúrese de haber trabajado con su equipo y su gestor de incorporación a Braze para determinar la mejor configuración del espacio de trabajo para su caso de uso. Para obtener más información sobre cómo planificar tus espacios de trabajo en Braze, consulta nuestra [Introducción: Guía de espacios de trabajo][enlace].

### Paso 2: Añade tu espacio de trabajo

Puede crear nuevos espacios de trabajo o cambiar entre espacios de trabajo existentes desde el desplegable de espacios de trabajo de la cabecera global.

1. Seleccione el menú desplegable del espacio de trabajo y haga clic en <i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> **Crear espacio de trabajo**.

![][1]

{:start="2"}
2\. Dale un nombre a tu espacio de trabajo.

{% alert tip %}
Es posible que desee adoptar una convención de nombres para que otras personas de su empresa puedan encontrar fácilmente su espacio de trabajo. Por ejemplo: "Upon Voyage US - Producción" y "Upon Voyage US - Puesta en escena".
{% endalert %}

{:start="3"}
3\. Seleccione **Crear**. Braze puede tardar unos segundos en crear tu espacio de trabajo.

![][2]

Accederá a la página **Configuración de la aplicación** para empezar a añadir instancias de su aplicación. Puedes acceder a esta página en cualquier momento desde **Ajustes** > **Ajustes de la aplicación**.

![][3]

### Paso 3: Añada las instancias de su aplicación

Denominamos "instancias de aplicación" a los distintos sitios y aplicaciones que se reúnen en un espacio de trabajo.

1. En la página **Configuración de aplicaciones**, haz clic en **\+ Añadir aplicación**.
2. Dé un nombre a su instancia de aplicación y seleccione en qué plataforma o plataformas se encuentra esta instancia de aplicación. Si selecciona varias plataformas, Braze creará una instancia de aplicación para cada plataforma.

![][4]{: style="max-width:60%" }

{:start="3"}
3\. Haz clic en **Añadir aplicación** para confirmar.

#### Claves API de la aplicación

Después de añadir la instancia de tu aplicación, tendrás acceso a su clave de API. La clave API se utiliza al realizar solicitudes entre la instancia de su aplicación y la API Braze. La clave de API también es importante para integrar el SDK de Braze con tu aplicación o sitio web.

![][5]

{% alert note %}
Debe crear instancias de aplicación distintas para cada versión de su aplicación en cada plataforma. Por ejemplo, si tiene versiones Free y Pro de su aplicación tanto en iOS como en Android, cree cuatro instancias de aplicación dentro de su espacio de trabajo (aplicación Free para iOS, aplicación Free para Android, aplicación Pro para iOS y aplicación Pro para Android). Esto te dará cuatro claves de API para utilizar, una para cada instancia de la aplicación.
{% endalert %}

#### Versión del SDK en vivo

La versión del SDK activa que se muestra en la página Configuración de la aplicación para una aplicación específica es la versión más alta de la aplicación con al menos el 5% del total de sus sesiones diarias y tiene al menos 500 sesiones en el último día.

Este campo aparece después de haber integrado el SDK de Braze con tu aplicación o sitio web. Si hay disponible una versión más reciente del SDK de Braze para tu plataforma, se anotará aquí con la etiqueta "Versión más reciente disponible."

![][6]

### Paso 4: Repetir según sea necesario

Repita los pasos 2 y 3 para configurar tantos espacios de trabajo como requiera su plan. Como práctica recomendada, le recomendamos que cree un espacio de trabajo de pruebas para las pruebas de integración y de campaña.

{% alert tip %}
**Añadir un espacio de trabajo de pruebas**<br>Puede realizar pruebas de aplicaciones aislando completamente a determinados usuarios de su instancia de producción. Cree un nuevo espacio de trabajo y, cuando publique la aplicación, asegúrese de cambiar la clave de API que utiliza Braze para que coincida con la de su espacio de trabajo de producción y no con la de su espacio de trabajo de pruebas.
{% endalert %}

## Gestión de los espacios de trabajo

### Añadir favoritos

Puedes añadir espacios de trabajo favoritos para acceder aún más rápido a los que más utilizas.

![][7]

Para añadir espacios de trabajo favoritos:

1. Seleccione el menú desplegable de su perfil y, a continuación, seleccione **Gestionar su cuenta**.
2. En la sección **Perfil de la cuenta**, localice el campo **Espacios de trabajo favoritos**.
3. Seleccione sus espacios de trabajo en la lista.
4. Seleccione **Guardar cambios**.

No hay límite en el número de espacios de trabajo que puedes marcar como favoritos, pero te recomendamos que mantengas esta lista corta por comodidad.

### Renombrar espacios de trabajo

Para cambiar el nombre de su espacio de trabajo:

1. Ve a **Ajustes** > **Ajustes de la aplicación**.
2. Pase el ratón por encima del nombre de su espacio de trabajo y seleccione <i class="image: /assets/img/braze_icons/pencil-01.svg" style="color: #0b8294;"></i>.
3. Asigne un nuevo nombre a su espacio de trabajo y seleccione <i class="fa-solid fa-square-check" style="color: #0b8294;"></i> **Guardar**.

![][8]

### Eliminar espacios de trabajo


Para eliminar tu espacio de trabajo:

1. Ve a **Ajustes** > **Ajustes de la aplicación**.
2. Seleccione **Eliminar espacio de trabajo**.

{% alert warning %}
Ten cuidado al eliminar espacios de trabajo. Una vez eliminado un espacio de trabajo, no se puede restaurar.
{% endalert %}

![][9]

## Preguntas más frecuentes

### ¿Debo crear un nuevo espacio de trabajo cuando publique una aplicación actualizada?

Si los usuarios sólo necesitan actualizar su aplicación y no vas a lanzar una aplicación completamente nueva a la tienda de aplicaciones, no deberías crear un nuevo espacio de trabajo a menos que no planees volver a enviar mensajes a los usuarios en la versión anterior.

Al crear un nuevo espacio de trabajo, todos los datos históricos y perfiles de usuario de la versión anterior de la aplicación no existirán en este nuevo espacio de trabajo. Así, cuando los usuarios actuales se actualicen a la nueva versión de la aplicación, se les creará un nuevo perfil sin ninguno de los datos de comportamiento de la antigua aplicación.

Además, sus usuarios existirían en dos lugares: el espacio de trabajo antiguo y el nuevo. También pueden tener potencialmente el mismo "push token". Esto puede dar lugar a que los usuarios reciban un mensaje de marketing destinado únicamente a los usuarios de espacios de trabajo antiguos, aunque ya se hayan actualizado.

#### ¿Qué debo hacer en su lugar?

Para separar las aplicaciones antiguas de las nuevas, cree una nueva instancia de aplicación dentro del mismo espacio de trabajo. De este modo, podrá dirigirse eficazmente a los usuarios de la nueva versión cuando seleccione esa aplicación durante la segmentación. Si desea enviar mensajes a usuarios que utilizan la versión anterior, puede utilizar filtros para [seleccionar la versión anterior de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

### Tengo varias instancias de aplicaciones en un espacio de trabajo, ¿cómo puedo asegurarme de que mi mensaje sólo se dirige a una única aplicación? {#singular-app}

Para asegurarse de que su mensaje sólo se dirige a una aplicación específica, añada un segmento que sólo se dirija a los usuarios de las instancias de la aplicación elegida. Esto es especialmente importante si un usuario puede tener dos tokens push para diferentes instancias de aplicaciones en el mismo espacio de trabajo. En este caso, los usuarios podrían recibir una notificación de una aplicación distinta de la que están utilizando. No es una experiencia ideal.

Por defecto, un segmento se dirige a todas las aplicaciones y sitios web del área de trabajo. Para establecer un segmento que sólo se dirija a una aplicación o sitio web:

1. Cree un segmento con un nombre significativo. En Braze, utilizamos el formato "Todos los usuarios ({Nombre} {Plataforma})". Por ejemplo, "Todos los usuarios (Upon Voyage iOS)".
2. Para **aplicaciones y sitios web específicos**, seleccione **Usuarios de aplicaciones específicas**.
3. En el menú desplegable **Aplicaciones específicas**, seleccione su aplicación o sitio.

![][10]{: style="max-width:75%" }

A continuación, puede añadir este segmento a su mensaje y empezar a refinar aún más su audiencia con segmentos y filtros adicionales si es necesario.

#### Campañas

Para las campañas, añada su segmento al paso **Usuarios objetivo** del compositor.

#### Canvas Flow

En Canvas Flow, añade tu segmento a tus pasos de Mensaje, en la sección **Validaciones de Entrega**. Las validaciones de entrega comprueban que tu audiencia cumple los criterios de entrega al enviar los mensajes. Recuerde especificar validaciones de entrega para cada paso de Mensaje para asegurarse de que se entregará a la aplicación correcta. No hay necesidad de segmentar en el nivel de entrada.

{% details Ampliar los pasos del flujo de trabajo original de Canvas %}

{% alert important %}
A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando el editor original. Este contenido está disponible como referencia para comprender los segmentos y la segmentación en el editor original.<br><br>Braze recomienda a los clientes que utilicen la experiencia Canvas original que se pasen a Canvas Flow. Es una experiencia de edición mejorada para construir y gestionar mejor los Lienzos. Más información sobre la [clonación de tus lienzos en el flujo de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

En el flujo de trabajo original del lienzo, añada su segmento al nivel de componentes del lienzo en la sección **Audiencia**. No hay necesidad de segmentar en el nivel de entrada.
{% enddetails %}


[1]: {% image_buster /assets/img/workspaces/workspace_create.png %}
[2]: {% image_buster /assets/img/workspaces/workspace_name.png %}
[3]: {% image_buster /assets/img/workspaces/workspace_empty_state.png %}
[4]: {% image_buster /assets/img/workspaces/workspace_add_app.png %}
[5]: {% image_buster /assets/img/workspaces/app_api_key.png %}
[6]: {% image_buster /assets/img/workspaces/app_live_sdk_version.png %}
[7]: {% image_buster /assets/img/workspaces/workspace_favorites.png %}
[8]: {% image_buster /assets/img/workspaces/workspace_rename.gif %}
[9]: {% image_buster /assets/img/workspaces/workspace_delete.png %}
[10]: {% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %}
[link]: {{site.baseurl}}/user_guide/getting_started/workspaces/
