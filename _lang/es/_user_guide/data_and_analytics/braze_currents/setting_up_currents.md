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

Los siguientes requisitos son los básicos y mínimos para integrarse con la mayoría de nuestros socios. Algunos socios exigirán parámetros adicionales, que figuran en [la documentación de sus respectivos socios]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) junto con cualquier matiz asociado a estos requisitos básicos.

| Requisito | Origin | Acceso | Descripción
|---|---|---|---|
| Cuenta con socio | Acuerda una cuenta con ese socio o ponte en contacto con tu director de cuentas Braze para que te haga sugerencias. | Consulte el sitio web de ese socio o póngase en contacto con él para inscribirse. | Braze no enviará datos a un socio si no tienes acceso a esos datos a través de la cuenta de tu empresa.
| Clave de API o token del socio | Normalmente, el panel del socio. | Sólo tienes que copiarlo y pegarlo en el campo Braze designado. | Braze tiene un campo designado para ello en la página Integraciones de ese socio. Lo necesitamos para saber adónde enviamos sus datos. **Es importante que mantengas tus claves/tokens de socio actualizados; las credenciales no válidas pueden hacer que se desactive tu conector y que se pierdan eventos.**
| Código/clave de autenticación, clave secreta, archivo de certificación | Ponte en contacto con un representante de tu cuenta con ese socio. También puede existir en el panel del socio. | Copie y pegue las claves en el campo Braze designado. Genere y cargue `.json` u otros archivos de certificación en el lugar adecuado de Braze. | Braze tiene un campo designado para ello en la página Integraciones de ese socio. Esto proporciona credenciales a Braze y nos autoriza a escribir archivos en tu cuenta de socio. **Es importante que mantengas tus datos de autenticación actualizados; unas credenciales no válidas pueden hacer que se desactive tu conector y que se pierdan eventos.**
| Cubo, Ruta de carpeta | Algunos socios organizan y clasifican los datos por contenedores. Esto debería encontrarse en el panel del socio. | Si es necesario, asegúrese de copiar el nombre del cubo o la ruta del archivo exactamente en el espacio designado en Braze. No queremos que sus datos se pierdan. | Aunque esto es necesario para algunos Socios, es importante hacerlo bien cuando lo necesitas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Es importante que mantengas actualizadas tus claves/tokens de socio y los datos de autenticación; si las credenciales de tu conector caducan, el conector dejará de enviar eventos. Si esto persiste durante más de **48 horas**, los eventos del conector se eliminarán y los datos se perderán permanentemente.
{% endalert %}

## Paso 1: Elige a tu socio

Braze Currents le permite integrarse a través del almacenamiento de datos mediante archivos planos o a nuestros socios de análisis de comportamiento y datos de clientes mediante cargas útiles JSON por lotes a un punto final designado.  

Antes de empezar la integración, es mejor decidir qué integración es la mejor para sus propósitos. Por ejemplo, si ya utiliza mParticle y Segment y desea que los datos Braze se transmitan allí, lo mejor sería utilizar una carga útil JSON por lotes. Si prefieres manipular los datos por tu cuenta o tienes un sistema más complejo de análisis de datos, puede que lo mejor sea utilizar el Almacenamiento de Datos[(¡Braze utiliza este método]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/)!).

## Paso 2: Navegar a Currents

Para empezar, vaya a **Integraciones de socios** > **Exportación de datos**. Accederá a la página de gestión de la integración de Currents.

{% alert note %}
Si utiliza la [navegación antigua]({{site.baseurl}}/navigation), puede encontrar esta página en **Integraciones** > **Corrientes**.
{% endalert %}

![Página de Currents en el panel de Braze]({% image_buster /assets/img_archive/currents-main-page.png %})

## Paso 3: Añadir socio

Añade un socio, a veces llamado "conector Currents", seleccionando el desplegable de la parte superior de la pantalla.

Cada socio requiere un conjunto diferente de pasos de configuración. Para activar cada integración, consulte nuestra lista de [socios disponibles]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) y siga las instrucciones de sus respectivas páginas.

## Paso 4: Configurar eventos

Elige los eventos que deseas pasar a ese socio marcando entre las opciones disponibles. Encontrará listados de estos eventos en nuestras bibliotecas de [Eventos sobre el comportamiento de los clientes]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) y [Eventos sobre el compromiso con los mensajes]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).

![]({% image_buster /assets/img/current4.png %})

Si lo necesita, puede obtener más información sobre nuestros eventos en nuestro artículo [sobre semántica de entrega de eventos]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_delivery_semantics/).

## Paso 5: Transformaciones de campo

Las transformaciones de campo de Currents le permiten designar determinados campos de cadena en Currents para su eliminación (sustitución por una cadena vacía) o hash (aplicación de un algoritmo hash SHA-256). 

Al seleccionar un campo para una de estas transformaciones, dicha transformación se aplicará a todos los eventos en los que aparezca ese campo. Por ejemplo, si selecciona `email_address` para el hash, se aplicará hash al campo `email_address` en Envío de correo electrónico, Apertura de correo electrónico, Rebote de correo electrónico y Cambio de estado del grupo de suscripción.

![Añadir transformaciones de campo]({% image_buster /assets/img/current3.png %})

## Paso 6: Pruebe su integración

Puedes probar tu integración o echar un vistazo a los datos de muestra de Currents en nuestro [repositorio GitHub](https://github.com/Appboy/currents-examples) de ejemplos de Currents.

{% alert important %}
Ten en cuenta que Currents eliminará los eventos con cargas útiles excesivamente grandes, superiores a 900 KB.
{% endalert %}

### Conectores de prueba Currents

Los conectores Test Currents son versiones gratuitas de nuestros conectores existentes que pueden utilizarse para probar y ensayar diferentes destinos. Las corrientes de prueba tienen:
- No hay límite en el número de conectores Test Currents que puedes construir.
- Un máximo agregado de 10 000 eventos por período móvil de siete días. Este total de eventos se actualiza cada hora en el panel.

Después de que sus conectores Test Currents alcancen el límite de envío, su conector no enviará eventos hasta el siguiente periodo de siete días.

Para actualizar tu conector de prueba Currents, edita la integración en el panel y selecciona **Actualizar**.

## Actualizar corrientes

{% multi_lang_include updating_currents.md %}

## Lista de direcciones IP permitidas

Braze enviará datos Currents desde las IP incluidas en la lista, que se añaden automática y dinámicamente a cualquier clave API que se haya optado por incluir en la lista.

| Para las instancias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06` y `US-07`: |
|---|
| `127.0.0.1`
| `23.21.118.191`
| `34.206.23.173`
| `50.16.249.9`
| `52.4.160.214`
| `54.87.8.34`
| `54.156.35.251`
| `52.54.89.238`
| `18.205.178.15`

| Para las instancias `EU-01` y `EU-02`: |
|---|
| `127.0.0.1`
| `52.58.142.242`
| `52.29.193.121`
| `35.158.29.228`
| `18.157.135.97`
| `3.123.166.46`
| `3.64.27.36`
| `3.65.88.25`
| `3.68.144.188`
| `3.70.107.88` 

| Para la instancia `US-08`: |
|---|
| `52.151.246.51`
| `52.170.163.182`
| `40.76.166.157`
| `40.76.166.170`
| `40.76.166.167`
| `40.76.166.161`
| `40.76.166.156`
| `40.76.166.166`
| `40.76.166.160`
| `40.88.51.74`
| `52.154.67.17`
| `40.76.166.80`
| `40.76.166.84`
| `40.76.166.85`
| `40.76.166.81`
| `40.76.166.71`
| `40.76.166.144`
| `40.76.166.145`