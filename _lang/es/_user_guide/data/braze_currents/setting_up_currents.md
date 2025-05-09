---
nav_title: Configurar las corrientes
article_title: Configurar las corrientes
page_order: 0
page_type: tutorial
description: "Este artículo explica el proceso de integración y configuración de Braze Currents."
tool: Currents
search_rank: 8
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/currents-the-basics-2/){: style="float:right;width:120px;border:0;" class="noimgborder"}Configuración de Currents

> Esta página resume y describe el proceso genérico de integración y configuración de Braze Currents.

{% alert important %}
Las corrientes están incluidas en algunos paquetes Braze. Póngase en contacto con su representante de Braze si tiene alguna pregunta o desea obtener acceso.
{% endalert %}

## Requisitos

El uso de Currents con cualquiera de nuestros socios requiere los mismos parámetros básicos y metodología de conexión.

Cada socio requiere que Braze tenga permiso para escribirle y enviarle archivos de datos, y Braze le pide la ubicación en la que debe escribir esos archivos, concretamente nombres de bucket o claves.

Los siguientes requisitos son los básicos y mínimos para integrarse con la mayoría de nuestros socios. Algunos socios exigirán parámetros adicionales, que figuran en [la documentación de sus respectivos socios]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) junto con cualquier matiz asociado a estos requisitos básicos.

| Requisito | Origin | Acceso | Descripción
|---|---|---|---|
| Cuenta con socio | Acuerda una cuenta con ese socio o ponte en contacto con tu director de cuentas Braze para que te haga sugerencias. | Consulta el sitio web de ese socio o ponte en contacto con él para registrarte. | Braze no enviará datos a un socio si no tienes acceso a esos datos a través de la cuenta de tu empresa.
| Clave de API o token del socio | Normalmente el panel del socio. | Sólo tienes que copiarlo y pegarlo en el campo Braze designado. | Braze tiene un campo designado para ello en la página de integraciones de ese socio. Lo necesitamos para saber adónde enviamos sus datos. **Es importante que mantengas tus claves o tokens de socio actualizados; unas credenciales no válidas pueden hacer que se desactive tu conector y que se pierdan eventos.**
| Código/clave de autenticación, clave secreta, archivo de certificación | Ponte en contacto con un representante de tu cuenta con ese socio. También puede existir en el panel del socio. | Copie y pegue las claves en el campo Braze designado. Genere y cargue `.json` u otros archivos de certificación en el lugar adecuado de Braze. | Braze tiene un campo designado para ello en la página de integraciones de ese socio. Esto proporciona credenciales a Braze y nos autoriza a escribir archivos en tu cuenta de socio. **Es importante que mantengas tus datos de autenticación actualizados; unas credenciales no válidas pueden hacer que se desactive tu conector y que se pierdan eventos.**
| Cubo, Ruta de carpeta | Algunos socios organizan y clasifican los datos por contenedores. Debe encontrarse en el panel del socio. | Si es necesario, asegúrate de copiar el nombre de contenedor o la ruta del archivo exactamente en el espacio designado en Braze. No queremos que sus datos se pierdan. | Aunque esto es necesario para algunos socios, es importante acertar cuando lo necesites. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Es importante que mantengas actualizadas tus claves de socio, tokens de socio y detalles de autenticación; si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

## Configuración de Currents

### Paso 1: Elige a tu socio

Braze Currents te permite integrarte a través del Almacenamiento de Datos utilizando archivos planos o a nuestros socios de análisis del comportamiento y datos de clientes utilizando una carga útil JSON por lotes a un punto final designado.  

Antes de empezar la integración, es mejor decidir qué integración es la mejor para sus propósitos. Por ejemplo, si ya utilizas mParticle y Segment y quieres que los datos de Braze fluyan allí, lo mejor sería utilizar una carga útil JSON por lotes. Si prefieres manipular los datos por tu cuenta o tienes un sistema más complejo de análisis de datos, puede que lo mejor sea utilizar el Almacenamiento de Datos[(¡Braze utiliza este método]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/)!).

### Paso 2: Corrientes Abiertas

Para empezar, vaya a **Integraciones de socios** > **Exportación de datos**. Accederá a la página de gestión de la integración de Currents.

![Página de Currents en el panel de Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

### Paso 3: Añade tu socio

Añade un socio, a veces llamado "conector Currents", seleccionando el desplegable de la parte superior de la pantalla.

Cada socio requiere un conjunto diferente de pasos de configuración. Para habilitar cada integración, consulta nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) y sigue las instrucciones de sus respectivas páginas.

### Paso 4: Configura tus eventos

Elige los eventos que deseas pasar a ese socio marcando entre las opciones disponibles. Encontrará listados de estos eventos en nuestras bibliotecas de [Eventos sobre el comportamiento de los clientes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) y [Eventos sobre el compromiso con los mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

![]({% image_buster /assets/img/current4.png %})

Si lo necesita, puede obtener más información sobre nuestros eventos en nuestro artículo [sobre semántica de entrega de eventos]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/).

### Paso 5: Configura las transformaciones de campo

Puedes utilizar las transformaciones de campo de Currents para eliminar o convertir en hash un campo de cadena.

- **Elimina:** Sustituye el campo cadena por `[REDACTED]`. Esto es útil si tu socio rechaza eventos en los que faltan campos o están vacíos.
- **Hash:** Aplica un algoritmo hash SHA-256 al campo cadena.

Al seleccionar un campo para una de estas transformaciones, dicha transformación se aplicará a todos los eventos en los que aparezca ese campo. Por ejemplo, si seleccionas `email_address` para el hash, el campo `email_address` se convertirá en hash en los eventos Envío por correo electrónico, Apertura de correo electrónico, Rebote de correo electrónico y Cambio de estado del grupo de suscripción.

![Añadir transformaciones de campo]({% image_buster /assets/img/current3.png %})

### Paso 6: Pruebe su integración

Puedes probar tu integración o echar un vistazo a los datos de muestra de Currents en nuestro [repositorio GitHub](https://github.com/Appboy/currents-examples) de ejemplos de Currents.

{% alert important %}
Currents eliminará los eventos con cargas útiles excesivamente grandes, superiores a 900 KB.
{% endalert %}

#### Comprobación de los conectores Currents

Los conectores Test Currents son versiones gratuitas de nuestros conectores existentes que pueden utilizarse para probar y ensayar diferentes destinos. Las corrientes de prueba tienen:

- No hay límite en el número de conectores Test Currents que puedes construir.
- Un máximo agregado de 10 000 eventos por período móvil de siete días. Este total de eventos se actualiza cada hora en el panel.

Después de que sus conectores Test Currents alcancen el límite de envío, su conector no enviará eventos hasta el siguiente periodo de siete días.

Para actualizar tu conector de prueba Currents, edita la integración en el panel y selecciona **Actualizar**.

## Actualizar corrientes

{% multi_lang_include updating_currents.md %}

## Lista de direcciones IP permitidas

Braze enviará datos de Currents desde las IP de la lista:

{% multi_lang_include data_centers.md datacenters='ips' %}
