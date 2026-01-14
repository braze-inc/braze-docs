---
nav_title: Antavo
article_title: Nube de fidelización Antavo
description: "Este artículo de referencia describe la asociación entre Braze y Antavo, un programa de fidelización de nueva generación que va más allá de recompensar las compras."
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Nube de fidelización Antavo

> [Antavo](https://antavo.com/) es un proveedor de tecnología de fidelización SaaS de nivel empresarial que crea programas de fidelización integrales para fomentar la fidelidad a la marca y cambiar el comportamiento del cliente.

_Esta integración está mantenida por Antavo._

## Sobre la integración

La integración de Antavo y Braze te permite utilizar los datos relacionados con el programa de fidelización para crear campañas personalizadas que mejoren la experiencia del cliente. Antavo admite la sincronización de datos de fidelización entre las dos plataformas; se trata de una sincronización de datos unidireccional únicamente, de Antavo a Braze. La integración admite el campo `external_id` Braze, que Antavo utiliza para sincronizar el ID de miembro de fidelización.

## Requisitos previos

| Requisito          | Descripción                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| Cuenta Antavo       | Se necesita una cuenta [Antavo](https://antavo.com/) con la integración Braze habilitada para aprovechar esta asociación.                                                |
| Clave de API REST de Braze   | Una clave de API REST Braze con los siguientes permisos: `users.track`, `events.list`, `events.data_series`, y `events.get`.<br><br>Puede crearse en el panel Braze desde **Configuración** > **Claves API**.  |
| Punto final REST Braze  | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia.                |
| Identificador de la aplicación Braze | La clave del identificador de tu aplicación. <br><br>Para localizar esta clave en el panel de Braze, ve a **Configuración** > **Claves de API** y busca la sección **Identificación**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Conectar Braze en Antavo

En Antavo, ve a **Módulos** > **Braze** y haz clic en **Configurar**. Al navegar por primera vez a la página de configuración de la integración Braze en Antavo, la interfaz te pedirá que conectes los dos sistemas.

Proporciona las siguientes credenciales:

- **URL de la instancia:** El punto final REST de Braze de la instancia a la que estás aprovisionado.
- **Token API (identificador):** La clave de API REST de Braze que Antavo debe utilizar al enviar solicitudes a Braze.
- **Identificador de la aplicación:** El identificador de la aplicación Braze.

Después de introducir las credenciales, haz clic en **Conectar**.

![Conecta la pantalla de Braze en Antavo con la URL de la instancia, el token de la API y el identificador de la aplicación.]({% image_buster /assets/img/antavo/connect_braze.png %})

### Paso 2: Configurar el mapeado de campos

Una vez establecida la conexión, se te redirigirá automáticamente a la página **Sincronizar campos** de Antavo para que configures la sincronización de campos entre los dos sistemas.   Puedes acceder a esta página en cualquier momento a través de **Módulos** > **Braze**.

Para configurar el mapeado de campos en Antavo:

1. Haz clic en **Añadir nuevo campo** <i class="fas fa-plus" alt=""></i>.
2. Utiliza el campo desplegable para seleccionar el **campo de fidelización** de Antavo que quieres sincronizar con Braze.
3. Introduce el **campo Remoto** que representa el atributo personalizado equivalente en Braze al que se rellenarán los datos.  

{% alert note %}
Puedes encontrar tu lista de atributos personalizados en Braze, en **Configuración de datos** > **Atributos personalizados**. Si el campo que introduces no está definido en Braze, se generará automáticamente un nuevo campo con la primera sincronización.
{% endalert %}

{:start="4"}
4\. Para añadir emparejamientos de campos adicionales, repite los pasos 1-3.
5\. Para eliminar un campo de la lista de datos sincronizados, haz clic en <i class="fa-solid fa-rectangle-xmark" title="Borrar"></i> al final de la fila.
6\. Haz clic en **Guardar**.

Cuando cualquier valor de los campos configurados cambia en Antavo, no solo se desencadena la sincronización de ese único valor, sino que todos los campos añadidos al mapeado de campos se incluyen en la solicitud.

![Página de Sincronización de Campos en Antavo.]({% image_buster /assets/img/antavo/data_field_mapping.png %})

{% alert important %}
Para minimizar el consumo de puntos de datos, recomendamos mapear solo los campos sobre los que se actuará dentro de Braze.
{% endalert %}

#### Tipos de datos admitidos

La integración admite todos los [tipos de datos de]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) atributos personalizados de Braze, a saber: número (entero, flotante), cadena, matriz, booleano, objeto, matriz de objetos y fecha.

![Perfil Braze que muestra diferentes atributos personalizados.]({% image_buster /assets/img/antavo/braze_profile.png %})

Los campos de datos se rellenan según el mapeado de campos configurado.

## Activadores

Además de configurar el mapeado de campos, la integración proporciona más funciones mediante características incorporadas a la herramienta [Flujos de trabajo](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629) de Antavo. Todos los [tipos de datos de]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) atributos personalizados Braze y [los tipos de datos de]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#expected-format) propiedades de eventos personalizados también pueden sincronizarse mediante flujos de trabajo.

### Sincronizar los datos de fidelización ocasionalmente

Utiliza esta opción si los datos no se almacenan en campos de fidelización en Antavo o si no se añaden a la lista de campos mapeados. La sincronización de los datos solicitados se desencadena cuando se cumplen los criterios de flujo de trabajo configurados.

Visita la guía paso a paso para aprender a configurar la sincronización de [los datos de fidelización relacionados con la última compra](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase).

### Sincronizar los eventos del programa de fidelización

Utiliza eventos sincronizados desde Antavo para introducir miembros de fidelización en Canvas de Braze basados en acciones. La integración puede sincronizar cualquier evento de Antavo (incluidos los eventos de compra) que aparezca en Braze como eventos personalizados.

Visita la guía paso a paso para aprender a configurar la sincronización del [evento de inscripción al programa de fidelización](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) y la sincronización del [evento de obtención de beneficios del programa de fidelización](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!).


