---
nav_title: Visto
article_title: Visto
description: "Seen habilita experiencias de video personalizadas a escala, ayudando a las marcas a impulsar una mayor interacción a lo largo del recorrido del cliente."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# Visto

> [Seen](https://seen.io) habilita a las marcas para crear y entregar experiencias de video personalizadas a escala. Con Seen, puedes diseñar un video en torno a tus datos, personalizarlo a escala en la nube y luego distribuirlo donde mejor funcione.
>
> La integración de Braze y Seen te permite enviar datos de usuario de Braze a Seen, generar dinámicamente videos personalizados y devolver activos de video -como una URL de reproductor única y una miniatura- a Braze para su uso en campañas y Canvases.


## Ejemplos

Seen admite la entrega automatizada y personalizada de video a lo largo del ciclo de vida del cliente, incluyendo:

- **Incorporación**: Da la bienvenida a nuevos usuarios con videos personalizados según su perfil o contexto de registro
- **Conversión y activación**: Refuerza las acciones clave con mensajes de video contextuales
- **Fidelización y upsell**: Destaca las ofertas personalizadas o los hitos de uso
- **Recuperación y prevención del abandono**: Reactivación de la interacción de los usuarios inactivos con contenidos de video a medida


## Requisitos previos

Antes de empezar, necesitas lo siguiente:

| Requisito previo | Descripción |
|--------------|-------------|
| Visto Acceso a la plataforma | Necesitas una suscripción a la Plataforma Seen o una campaña Seen activa. Necesitas acceder a la configuración de tu espacio de trabajo para recuperar tu ID de espacio de trabajo y generar un token de API. |
| URL Webhook de Transformación de datos Braze | La Transformación de Datos Braze reformatea los datos entrantes de Seen para que puedan ser aceptados por el punto final /users/track de Braze. |
| Braze datos de usuario | La personalización del video requiere datos a nivel de usuario. Asegúrate de que los atributos pertinentes están disponibles en Braze y de que pasas **braze_id** como identificador único. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}




## Cómo funcionan los Viajes Vistos

Seen utiliza [Journeys](https://docs.seen.io/journey) para controlar cómo se procesan los datos entrantes y cómo se generan las salidas de video.

Un Viaje es un flujo de trabajo configurable que:
- Recibe datos de sistemas externos (como Braze)
- Aplica reglas lógicas y de personalización
- Genera un video y activos asociados
- Devuelve una carga útil de respuesta configurable

Los viajes se componen de **nodos**, cada uno con una función específica:

- **Nodo desencadenante**: Define cómo y cuándo se inicia un Viaje (para integraciones Braze, utiliza un desencadenador `On Create` )
- **Nodo condicional**: Dirige a los usuarios a través de diferentes rutas lógicas en función de los valores de los datos
- **Nodo del proyecto**: Aplica la personalización dinámica del video utilizando los datos entrantes
- **Nodo jugador**: Genera una URL única para el reproductor de video
- **Nodo webhook**: Define la carga útil de respuesta enviada de vuelta a Braze

Como las respuestas de Journey son configurables, asegúrate de que los campos de salida devueltos por Seen coinciden con los atributos esperados por tu Transformación de Datos Braze.


## Límite de velocidad
La API Vista acepta hasta 100 llamadas cada 10 segundos.


## Integración

En este ejemplo, Braze envía datos de usuario a Seen para generar un video personalizado. A continuación, Seen devuelve una URL de reproductor de video y una URL de miniatura únicas, que se almacenan como atributos personalizados en Braze para su uso en mensajería.

Si tienes varias campañas de video con Seen, repite el proceso para conectar Braze con todas las campañas de video.

### Paso 1: Crea una campaña webhook para enviar datos a Seen

Crea una nueva [campaña Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) en Braze.

Configura el webhook como se indica a continuación:

- **URL del webhook**:  
  `https://next.seen.io/v1/workspaces/{WORKSPACE_ID}/data`  
  Busca el ID de tu espacio de trabajo en la configuración de la Plataforma Seen.

- **Método HTTP**: POST
- **Cuerpo de la solicitud**: Texto sin procesar  
  Utiliza el siguiente ejemplo como punto de partida. Consulta [la documentación de creación de datos de Seen](https://docs.seen.io/create-data) para más información.

{% raw %}
```json
{
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "id": "{{${braze_id}}}"
}
```
{% endraw %}
- **Encabezados de solicitud**:
  - `Authorization`: Portador `{Seen_API_TOKEN}`
  - `Content-Type`: `application/json`

  > Genera un [token de API](https://docs.seen.io/authorization) en la Plataforma Seen, en Configuración del espacio de trabajo. Puedes ponerte en contacto con tu administrador del éxito del cliente de Seen para que te ayude.

- Para probar el webhook con un usuario, pasa a la pestaña **Prueba**.
- Tras confirmar que la prueba funciona según lo previsto, completa la configuración del webhook.


### Paso 2: Configurar un Viaje en la Plataforma Seen

Seen utiliza [Journeys](https://docs.seen.io/journey) para definir cómo se procesan, personalizan y devuelven los datos entrantes a Braze.  
Cada Viaje es un flujo de trabajo configurable compuesto por nodos que te permiten controlar tanto la lógica de generación de video como la carga útil de respuesta.

Para configurar tu Viaje:

1. Crea un nuevo Viaje en la Plataforma Seen
2. Añade un **nodo Desencadenador** y selecciona el desencadenador `On Create`   
   Esto garantiza que el Viaje se inicie cuando Braze envíe datos a Seen. Crea y añade cualquier lógica de [segmentación](https://docs.seen.io/segments) dentro de tu espacio de trabajo si es necesario.
3. Construye tu lógica utilizando los siguientes nodos según sea necesario:
   - **Nodo condicional**: Encaminar a los usuarios en función de los valores de los atributos (por ejemplo, tipo de plan o región)
   - **Nodo del proyecto**: Aplica la personalización dinámica del video utilizando los datos entrantes
   - **Nodo jugador**: Generar una URL única del reproductor de video
4. Añade un **nodo Webhook** para definir la respuesta enviada a Braze

#### Requisitos de respuesta del nodo webhook

Como la carga útil de la respuesta es configurable, asegúrate de que se devuelven los siguientes campos para admitir la Transformación de Datos Braze que se describe en el paso siguiente:

| Campo | Descripción |
|------|-------------|
| `id` | Debe coincidir con el `braze_id` enviado desde Braze |
| `player_url` | URL única para el reproductor de video personalizado |
| `email_thumbnail_url` | URL de la miniatura de video generada |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Si tu caso de uso requiere atributos adicionales, inclúyelos en la respuesta y mapealos en Braze.


### Paso 3: Crea una Transformación de Datos para recibir datos de Seen

Utiliza las Transformaciones de Datos Braze para ingerir la respuesta Seen Journey y almacenar los activos de video en el perfil de usuario.

1. Crea los siguientes [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) en Braze:
   - `player_url`
   - `email_thumbnail_url`
2. Ve a **Configuración de datos** → **Transformación de datos** y haz clic en **Crear transformación**
3. Configura la transformación:
   - **Empezar de cero**
   - **Destino** → POST: Rastrear usuarios
4. Comparte la URL del webhook generado con Seen, o añádela directamente al **nodo** Journey **Webhook**
5. Utiliza el siguiente código de transformación:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.id,
      "_update_existing_only": true,
      "player_url": payload.player_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```

{: start="6"}
6\. Envía una carga útil de prueba al punto final proporcionado. Envía datos a la Plataforma Seen para ejecutar tu Viaje, o envía la carga útil directamente a Braze con [Postman](https://www.postman.com/) u otro servicio similar.
7\. Selecciona **Validar** para asegurarte de que todo funciona según lo previsto.
8\. Selecciona **Guardar** y **Activar**.