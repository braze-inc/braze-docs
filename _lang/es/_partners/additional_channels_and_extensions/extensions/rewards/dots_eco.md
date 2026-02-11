---
nav_title: DOTS.ECO
article_title: DOTS.ECO
description: "Este artículo de referencia describe la integración de Braze y DOTS.ECO."
alias: /partners/dots.eco/
page_type: partner
search_tag: Partner
---

# DOTS.ECO

> [DOTS.ECO](https://dots.eco) te permite recompensar a los usuarios con un impacto medioambiental real mediante certificados digitales rastreables. Cada certificado puede incluir metadatos como una URL de certificado compartible y una URL de imagen, para que los usuarios puedan ver (y volver a ver) su prueba de impacto.

_Esta integración está mantenida por DOTS.ECO._

## Acerca de esta integración

Braze y DOTS.ECO conectan las interacciones con los clientes con recompensas de impacto en el mundo real. Desde un paso en Canvas o campaña de Braze, puedes activar una solicitud de creación de certificado DOTS.ECO utilizando Contenido conectado. DOTS.ECO devuelve metadatos de certificado (como `certificate_url` y `certificate_image_url`) que puedes almacenar en el perfil del usuario como atributos personalizados y reutilizar en canales como mensajes dentro de la aplicación, tarjetas de contenido y notificaciones push.

## Ejemplos

- Desencadenar un certificado de impacto cuando un usuario completa un evento clave (compra, finalización de nivel, suscripción, referidos).
- Muestra una imagen personalizada del certificado en un mensaje dentro de la aplicación después de que el paso Contenido conectado tenga éxito.
- Añade una tarjeta de contenido "Ver tu certificado" con la URL del certificado para acceder más tarde.
- Almacena los metadatos del certificado (como `certificate_url`, `certificate_image_url`, `certificate_header`, y `greeting`) como atributos personalizados para reutilizarlos en futuros mensajes.
- Asigna certificados utilizando un ID de usuario remoto para que los usuarios puedan reclamar y ver su impacto más tarde.
- Realiza pruebas A/B sobre la mensajería de impacto (diferentes textos/imágenes) manteniendo el mismo flujo de actualización de usuarios DOTS.ECO.


## Requisitos previos

Antes de empezar, necesitas lo siguiente:

| Requisito previo | Descripción |
|---|---|
| Cuenta DOTS.ECO | DOTS.ECO acceso a la cuenta. |
| DOTS.ECO credenciales | La solicitud de este artículo requiere un token de aplicación DOTS.ECO, una clave de API y un ID de asignación. Para recuperarlos, ponte en contacto con tu administrador del éxito del cliente en DOTS.ECO. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. Crea esta clave en el panel de Braze, en **Configuración** > **Claves de API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración DOTS.ECO

### Paso 1: Crea un Canvas y añade un paso de Actualización de Usuario

En el panel de Braze, crea un nuevo Canvas que se desencadene cuando un usuario complete un evento clave (como una compra, una suscripción o un hito).

Añade un paso de Actualización de Usuario justo después del paso de entrada. Este paso se utilizará para llamar a la API DOTS.ECO a través de Contenido conectado y almacenar los datos de certificado devueltos en el perfil de usuario.

Utiliza este paso para llamar a la API DOTS.ECO a través de Contenido conectado y almacenar los datos de certificado devueltos en el perfil de usuario.

### Paso 2: Componer JSON avanzado: Haz una petición POST a DOTS.ECO utilizando Contenido conectado

En el paso **Actualización del usuario**, cambia al **Editor JSON avanzado** y utiliza Contenido conectado para realizar una solicitud POST a la API de certificados DOTS.ECO.

Utiliza la etiqueta `capture` y una solicitud de Contenido conectado para llamar al punto final de certificado de DOTS.ECO. A continuación, guarda la respuesta en el perfil de usuario como atributos personalizados.

**Ejemplo de contenido conectado y actualización de usuario**  
{% raw %}
```  
{% capture post_body %} 
{  
  "remote_user_email": "{{${email_address} | default: 'braze+nadav@dots.eco'}}",  
  "app_token": "YOUR_DOTS.ECO_APP_TOKEN",  
  "impact_qty": 1,  
  "remote_user_id": "{{${user_id} | default: ${braze_id}}}",  
  "allocation_id": "YOUR_DOTS.ECO_ALLOCATION_ID"  
}  
{% endcapture %}

{% connected_content https://impact.dots.eco/api/v1/certificate/add?format=sdk  
  :method post  
  :headers { "auth-token": "YOUR_DOTS.ECO_AUTH_TOKEN" }  
  :body {{post_body}}  
  :content_type application/json  
  :save result  
%}

{  
  "attributes": [  
    {  
      "certificate_image_url": "{{result.certificate_image_url}}",  
      "certificate_url": "{{result.certificate_url}}",  
      "certificate_id": "{{result.certificate_id}}"  
    }  
  ]  
}  
```
{% endraw %}

Envía la solicitud a `https://impact.dots.eco/api/v1/certificate/add?format=sdk`.

![DOTS.ECO Paso de actualización de usuario.]({% image_buster /assets/img/dots_eco/dotseco_user_update.png %})

{% alert important %}  
Esta integración utiliza Contenido conectado dentro de un paso en Canvas **de actualización de usuario** para llamar a la API DOTS.ECO. Prueba primero las solicitudes con un cliente API (por ejemplo, Postman) para validar tu token y carga útil.  
{% endalert %}

### Paso 3: Mostrar el certificado en mensajes

Cuando los atributos del certificado se almacenan en el perfil de usuario, se puede hacer referencia a ellos en los pasos posteriores del mensaje Canvas.

![DOTS.ECO flujo.]({% image_buster /assets/img/dots_eco/dots.eco_flow.png %})

![DOTS.ECO Paso de mensajes.]({% image_buster /assets/img/dots_eco/dotseco_messages.png %})

![DOTS.ECO sección de composición de mensajes.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose.png %})

Por ejemplo:  
- Mostrar la imagen del certificado en un mensaje dentro de la aplicación utilizando {% raw %}`{{custom_attribute.${certificate_image_url}}}`{% endraw %}  
- Enlaza con el certificado alojado utilizando {% raw %}`{{custom_attribute.${certificate_url}}}`{% endraw %}

![DOTS.ECO comportamiento del mensaje al hacer clic.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


Esto te permite personalizar mensajes dentro de la aplicación, tarjetas de contenido o notificaciones push con confirmación de impacto.

## Solución de problemas

Revisa los errores de Contenido conectado en el panel de Braze, en **Configuración** > **Registro de actividad de mensajes**.

- **El Contenido conectado vuelve vacío**: Confirma que `:save result` está configurado y que estás haciendo referencia a los campos de respuesta esperados.
- **Los atributos no se muestran en el paso Mensaje**:
  - Confirma que los nombres de los atributos personalizados en Braze coinciden exactamente con los atributos que estableciste en el paso Actualización de usuario.
  - En el paso Actualizar usuario, utiliza la **vista previa y la** pestaña **de prueba** para confirmar que se rellenan los atributos. A continuación, envía una prueba a un usuario y confirma que los atributos se guardan en su perfil de usuario.
- **`422` error (entidad no procesable)**: Confirma que el token de tu aplicación y la cantidad de impactos son válidos.
- **`401` error**: Confirma que el auth token está presente y es correcto.
- **No hay vista previa de la imagen en el paso Mensaje**: Selecciona **Enviar prueba a usuario** en el paso Actualización de usuario y, a continuación, obtén una vista previa del mensaje utilizando ese mismo usuario.