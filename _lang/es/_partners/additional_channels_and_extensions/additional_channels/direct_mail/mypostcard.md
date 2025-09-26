---
nav_title: MyPostcard
article_title: MyPostcard
page_order: 1
description: "Este artículo de referencia describe la asociación entre Braze y MyPostcard, que te permite utilizar el correo directo como un canal adicional para tu flujo de trabajo de CRM."
alias: /partners/mypostcard/
page_type: partner
search_tag: Partner

---

# MyPostcard

> [MyPostcard](https://www.mypostcard.com), una aplicación de postales líder en el mundo, te permite realizar campañas de correo directo con facilidad, proporcionándote una forma sencilla y rentable de conectar con tus clientes. 

Utiliza la integración de MyPostcard y Braze para enviar a tus clientes correos impresos sin esfuerzo.

## Requisitos previos

| Requisito                      | Descripción                                                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Cuenta MyPostcard B2B           | Es necesario registrarse en MyPostcard para beneficiarse de esta integración.                                          |
| Clave de API B2B y credenciales        | Puedes encontrar tu clave de API y las credenciales en la herramienta de administración MyPostcard B2B.                                         |
| Aprobada la campaña MyPostcard B2B | Para aprovechar esta integración, tienes que configurar una campaña de mailing impreso en la herramienta MyPostcard B2B. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Ejemplos

Para elevar tus campañas de correo directo, es crucial ir más allá de los envíos masivos tradicionales e integrar fácilmente el correo impreso en tus flujos de trabajo. Este enfoque te permite llegar a clientes específicos que se han dado de baja de tus boletines por correo electrónico o cuyos correos electrónicos están marcados como correo no deseado. Con MyPostcard, puedes enviar sin esfuerzo campañas de correo impreso directamente a través de Braze.

- Construye flujos de trabajo intuitivos en Braze, incorporando el correo impreso como un nuevo y potente canal, sin necesidad de conocimientos técnicos.
- Libera el potencial de los envíos impresos personalizados con unos sencillos pasos.
- Benefíciate de una implantación sencilla respaldada por la asistencia personalizada de un equipo especializado.

## Integración

Para integrarte con MyPostcard, [inicia sesión o regístrate](https://www.mypostcard.com/b2b/admin/) y crea tu primera campaña para utilizarla a través de [los webhooks Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks).

### Paso 1: Cree su plantilla de webhook Braze

Crea una plantilla webhook MyPostcard para utilizarla en futuras campañas o Lienzos navegando hasta **Plantillas** > **Plantillas webhook** en la plataforma Braze.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), vaya a **Compromiso** > **Plantillas y medios** > **Plantillas de Webhook**.
{% endalert %}

Si quieres crear una campaña única de webhook MyPostcard o utilizar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva campaña. Rellena los siguientes campos:

| Campo         | Descripción                                               |
|---------------|-----------------------------------------------------------|
| **URL del webhook** | La URL del webhook tal y como se muestra en la Herramienta de Administración B2B.             |
| **Cuerpo de la solicitud** | Texto sin formato (formato JSON que se encuentra en la Herramienta de administración B2B).        |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Método y encabezados de solicitud

MyPostcard requiere que se incluya en la plantilla un método HTTP junto con las siguientes cabeceras HTTP.

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>Campo</strong></th>
      <th><strong>Detalles</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Método HTTP</strong></td>
      <td><code>POST</code></td>
    </tr>
    <tr>
      <td><strong>Nombre de usuario</strong></td>
      <td><code>{{ '&lt;username&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Contraseña</strong></td>
      <td><code>{{ '&lt;password&gt;' }}</code></td>
    </tr>
    <tr>
      <td><strong>Tipo de contenido</strong></td>
      <td><code>application/json</code></td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Cuerpo de la solicitud

Copia el cuerpo de la solicitud que aparece en la Herramienta de administración B2B y, a continuación, rellena los marcadores de posición con contenido utilizando cualquier etiqueta de personalización de Liquid.

![Pestaña Componer que muestra el cuerpo JSON y la información del webhook.]({% image_buster /assets/img/mypostcard/mypostcard_compose.jpg %})

### Paso 2: Vista previa de su solicitud

A continuación, previsualiza tu solicitud en el panel **Vista previa** o ve a la pestaña **Prueba**, donde puedes elegir un usuario al azar, un usuario existente o crear un usuario personalizado para probar tu webhook. ¡No olvides guardar tu plantilla antes de salir de la página!

![Prueba la pestaña webhook con diferentes campos para validar la implementación.]({% image_buster /assets/img/mypostcard/mypostcard_test.jpg %})

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas webhook actualizadas pueden encontrarse en la lista **Plantillas webhook guardadas** al crear una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

