En el panel de Braze, ve a **Configuración de Datos** > **Transformación de Datos**.

Selecciona **Crear transformación** para darle un nombre a tu transformación y, a continuación, elige tu experiencia de edición.

![Detalles de la transformación con la opción de elegir "Usar una plantilla" o "Empezar de cero" para tu experiencia de edición.]({% image_buster /assets/img/data_transformation/data_transformation10.png %}){: style="max-width:80%;"}

Selecciona **Utilizar una plantilla** para examinar una biblioteca de plantillas, incluidos los casos de uso de Transformación de datos. O bien, selecciona **Empezar de cero** para cargar una plantilla de código predeterminada. 

Si empiezas de cero, elige un destino para tu transformación. Todavía puedes insertar una plantilla de código de la biblioteca de plantillas.

{% details Más sobre destinos %}
* **POST: Seguimiento de usuarios:** Transforma los webhooks de una plataforma de origen en actualizaciones del perfil de usuario, como atributos, eventos o compras.
* **PUT: Actualiza varios elementos del catálogo:** Transforma los webhooks de una plataforma de origen en actualizaciones de elementos del catálogo.
* **DELETE: Eliminar varios elementos del catálogo:** Transforma los webhooks de una plataforma de origen en eliminaciones de elementos del catálogo.
* **PATCH: Edita varios elementos del catálogo:** Transforma los webhooks de una plataforma de origen en ediciones de elementos del catálogo.
* **POST: Envía mensajes inmediatamente solo a través de la API:** Transforma webhooks de una plataforma de origen para enviar mensajes inmediatos a usuarios designados.
{% enddetails %}

{% alert note %}
¿Quieres solicitar plantillas o destinos adicionales? Considera la posibilidad de dejar [una opinión sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

Después de crear tu transformación, verás la vista detallada de la transformación. Aquí, puedes ver el webhook más reciente recibido para esta transformación en **Detalles del webhook** y un espacio para escribir tu código de transformación en **Código de transformación**.

{% if include.location == "typeform" %}

![Un ejemplo de detalles de webhook y código de transformación.]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

{% endif %}

Captura la **URL de tu webhook** para utilizarla en el siguiente paso.
