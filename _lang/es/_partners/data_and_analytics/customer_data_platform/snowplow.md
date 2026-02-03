---
nav_title: Snowplow
article_title: Snowplow
description: "Este artículo de referencia describe la asociación entre Braze y Snowplow, una plataforma de infraestructura de datos, que te permite reenviar eventos de Snowplow a Braze en tiempo real utilizando el Reenvío de Eventos de Snowplow."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow](https://snowplowanalytics.com) es una plataforma escalable para la recopilación de datos ricos, de alta calidad y baja latencia. Snowplow está diseñado para recopilar datos de comportamiento completos y de alta calidad para empresas.

_Esta integración está mantenida por Snowplow._

## Sobre la integración

La integración de Braze y Snowplow te habilita para reenviar eventos de Snowplow a Braze en tiempo real mediante la solución de Reenvío de Eventos de Snowplow. Esta integración te permite enviar eventos a Braze al tiempo que te ofrece flexibilidad y control. Concretamente, puedes
- Filtra y transforma los eventos antes de enviarlos a Braze.
- Mapea datos de eventos de Snowplow con atributos de usuario, eventos personalizados y compras de Braze.
- Conserva todos los datos en tu nube privada hasta que decidas reenviarlos.
- Despliega tú mismo la solución en tu cuenta existente de Snowplow en la nube. 

El [reenvío de eventos](https://docs.snowplow.io/docs/destinations/forwarding-events/) de Snowplow es una característica adicional de pago disponible para los clientes de Snowplow. Para reenviar eventos a Braze sin este complemento, utiliza la [integración en](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/) servidor de Google Tag Manager de Snowplow [.](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/) 

Aprovecha los ricos datos de comportamiento de Snowplow para impulsar potentes interacciones centradas en el cliente en Braze y entregar mensajes personalizados en tiempo real.

## Requisitos previos

| Requisito             | Descripción                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tubería quitanieves       | Necesitas una tubería quitanieves en funcionamiento.                                                                                                                                                                                                                                          |
| Acceso a la consola quitanieves | Debes tener acceso a la consola de Snowplow para configurar los reenviadores de eventos.                                                                                                                                                                                                                                |
| Clave de API REST de Braze      | Una clave de API REST Braze con los siguientes permisos: `users.track`, `users.alias.new`, `users.identify`, `users.export.ids`, `users.merge`, `users.external_ids.rename`, y `users.alias.update`. <br><br> Puedes crearla en el panel de Braze desde **Configuración** > **Claves de API**. |
| Punto final REST Braze     | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final depende de la URL Braze de tu instancia.                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

### Entrega personalizada y basada en la acción
Utilice cualquiera de los numerosos eventos enriquecidos que Snowplow recopila por defecto o defina sus propios eventos personalizados para dar forma a recorridos del cliente aún más granulares que tengan sentido para su negocio. Aproveche los ricos datos de comportamiento de Snowplow para diseñar embudos de clientes y desbloquear valor para sus equipos de marketing y producto, ayudándoles a maximizar la conversión y el uso del producto a través de Braze.

### Segmentación dinámica
Cree audiencias dinámicas en Braze basadas en los datos de comportamiento de alta calidad de Snowplow: A medida que los usuarios realizan acciones en su producto, aplicación o sitio web, puede aprovechar los datos de comportamiento en tiempo real que Snowplow recopila para añadir o eliminar automáticamente usuarios de los segmentos relevantes en Braze.

## Integración

### Paso 1: Configura el destino en la Consola del Quitanieves

Para crear el reenviador de eventos:

1. En la Consola Quitanieves, navega hasta **Destinos** y selecciona **Crear nuevo destino**.
2. Al configurar la conexión, selecciona **Braze** como tipo de conexión.
3. Introduce tu clave de API Braze y el punto final de la API REST.
4. Guarda la conexión.

### Paso 2: Configurar el reenviador de eventos

Al configurar el reenviador, puedes elegir qué eventos Snowplow reenviar y mapearlos a tipos de objetos Braze:

1. **[Atributos del usuario]({{site.baseurl}}/api/objects_filters/user_attributes_object)**: Actualiza los datos de perfil de usuario y las propiedades personalizadas de usuario.
2. **[Eventos personalizados]({{site.baseurl}}/api/objects_filters/event_object)**: Envía acciones y comportamientos de los usuarios.
3. **[Compras]({{site.baseurl}}/api/objects_filters/purchase_object)**: Envía los datos de la transacción con los detalles del producto.

Para cada tipo de objeto, puedes configurar mapeados de campo para especificar cómo se mapean los datos de eventos Snowplow a los campos Braze. Consulta [la documentación Crear autocargadores](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/) de Snowplow para obtener instrucciones detalladas de instalación y configuración del mapeado de campos.

### Paso 3: Validar la integración

Confirma que los eventos están llegando a Braze comprobando las siguientes páginas en tu cuenta de Braze:

1. **Generador de consultas**: En Braze, ve a **Análisis** > **Generador de consultas**. Puedes escribir consultas en las siguientes tablas para obtener una vista previa de los datos enviados desde el Quitanieves: `USER_BEHAVIORS_CUSTOMEVENT_SHARED` y `USERS_BEHAVIORS_PURCHASE_SHARED`.
2. **Panel de uso de la API**: En Braze, ve a **Configuración** > **API e identificadores** para ver un gráfico del uso de la API a lo largo del tiempo. Puedes filtrar específicamente por la clave de API que utiliza Snowplow y ver tanto los éxitos como los fracasos.

## Envío de propiedades personalizadas

Puedes enviar propiedades personalizadas más allá de los campos estándar. La estructura depende del tipo de objeto Braze que estés utilizando:

- **Atributos del usuario**: Añadir como campos de nivel superior (por ejemplo, `subscription_tier`, `loyalty_points`)
- **Propiedades del evento**: Anidado bajo el objeto `properties` (por ejemplo, `properties.plan_type`, `properties.feature_flag`)
- **Propiedades de la compra**: Anidado bajo el objeto `properties` (por ejemplo, `properties.color`, `properties.size`)

Para los nombres de propiedades que contengan espacios, utiliza la notación de corchetes (por ejemplo, `["account type"]` o `properties["campaign source"]`).

Consulta [la documentación del Objeto de Evento]({{site.baseurl}}/api/objects_filters/event_object) para obtener información detallada sobre los tipos de datos admitidos, los requisitos de denominación de las propiedades y los límites de tamaño de la carga útil.

## Limitaciones

**Límites de velocidad:** Braze aplica un límite de velocidad de 3.000 llamadas a la API cada tres segundos para la API de seguimiento de usuarios. Como Snowplow no admite el procesamiento por lotes para los reenviadores de eventos, este límite de velocidad de la API también funciona como límite de tasa de eventos. Si tu caudal de entrada supera los 3.000 eventos cada tres segundos, puedes experimentar un aumento de la latencia.
