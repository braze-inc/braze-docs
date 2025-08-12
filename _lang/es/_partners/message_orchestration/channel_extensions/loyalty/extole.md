---
nav_title: Extole
article_title: Extole
description: "Este artículo describe la asociación entre Braze y Extole, una empresa de marketing de recomendación, que permite extraer eventos y atributos de los clientes de los programas de recomendación a un amigo y de crecimiento en Braze."
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> [Extole](https://www.extole.com/), una empresa de SaaS, es líder en el sector del marketing de recomendación a amigos y ayuda a crear y optimizar programas eficaces de marketing de recomendación para aumentar la captación de clientes.

_Esta integración está mantenida por Extole._

## Sobre la integración

Con la integración de Braze y Extole, puede extraer eventos y atributos de clientes de los programas de crecimiento y de recomendación de amigos de Extole a Braze, lo que le permite crear campañas de marketing más personalizadas que impulsan la captación, el compromiso y la fidelidad de los clientes. También puedes incorporar dinámicamente atributos de contenido de Extole, como códigos de compartición y enlaces personalizados, a las comunicaciones Braze.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Extole | Se necesita una cuenta de Extole para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST de Braze con el permiso `users.track`. Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| URL de la API Braze | La URL de la API de Braze es específica de su [instancia de Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

Los siguientes casos de uso muestran algunas formas de aprovechar la integración de Extole con Braze. Trabaje con sus responsables de implantación y de éxito de clientes de Extole para desarrollar una opción que se adapte a las necesidades específicas de su empresa.

- Aproveche los eventos personalizados de sus programas de recomendación y compromiso para activar una campaña Braze o Canvas
- Cree segmentos personalizados, cuadros de mando e informes utilizando los datos de sus programas impulsados por Extole.
- Dar de baja o suscribir usuarios automáticamente a su lista de marketing en Braze

## Integración

Complete los siguientes pasos para poner en marcha rápidamente su integración. Tus administradores del éxito del cliente y de implementación de Extole te ayudarán en este proceso y responderán a cualquier pregunta que puedas tener.

### Conéctate a tu cuenta Braze

1. Seleccione la integración Braze en la página [Socios](https://my.extole.com/partners) de su cuenta Mi Extole.
2. En la integración Braze, seleccione **Instalar** para iniciar la conexión entre Extole y Braze.
3. Rellena los campos obligatorios, empezando por tu clave de API REST Braze. 
4. Introduce la URL de tu API Braze. Esta URL depende de la instancia en la que esté aprovisionada su cuenta Braze.
5. Añade los eventos de Extole que quieras enviar a Braze. Los eventos por defecto, las propiedades de los eventos y los atributos de usuario se describen en [la tabla Eventos de Extole](https://dev.extole.com/docs/braze#extole-program-events).
6. Añade los estados de recompensa que quieras enviar a Braze, aparte del estado `FULFILLED`. Consulta [la tabla de recompensas de Extole](https://dev.extole.com/docs/braze#extole-rewards) para ver las descripciones de los estados de recompensa disponibles.
7. Seleccione su asignación de clave de identificación externa Braze. Así es como Extole actualiza los perfiles de los usuarios en Braze. Puede asignar la clave de identificación externa Braze a `email_address` o `partner_user_id` de Extole para el usuario. Recomendamos utilizar `external_id` en lugar de `email_address`, ya que es más seguro.
8. Guarde la configuración para completar la conexión. Ahora, los eventos de Extole pueden fluir a tu cuenta Braze.

### Eventos del programa Extole

A continuación se muestran los eventos predeterminados, las propiedades de los eventos y los atributos de usuario que Extole enviará a Braze. Póngase en contacto con sus responsables de implementación de Extole o de éxito del cliente para identificar y añadir eventos adicionales de Extole a su integración.

| Evento | Descripción | Propiedades del evento | Atributos del usuario |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | Un participante crea su enlace para compartir introduciendo su correo electrónico en Extole Share Experience. | Nombre de evento  <br>Hora del evento  <br>Socio (Extole)  <br>Embudo (defensor o amigo)  <br>Programa | <br>ID externo <br>Correo electrónico  <br>Compartir enlace |
| `extole_shared` | Un participante comparte su enlace de recomendación con un amigo. | Nombre de evento  <br>Hora del evento  <br>Socio (Extole)  <br>ID externo  <br>Embudo (defensor o amigo)  <br>Programa  <br>Compartir canal | Correo electrónico <br>Nombre <br>Apellido |
| `outcome` - El resultado es dinámico en función de la configuración de su programa (como `extole_shipped`, `extole_converted`)| Un participante ha convertido o completado el evento de resultado deseado configurado para el programa. | Dinámica por programa | Correo electrónico <br>Nombre <br>Apellido |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Estados de suscripción a Extole

| Estado de suscripción | Descripción | Propiedades del evento | Atributos del usuario |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | Un participante ha optado por recibir mensajes de marketing. | N/A | Correo electrónico  <br>Tipo de lista  <br>ID externo  <br>Suscripción por correo electrónico (adhesión voluntaria) |
| `unsubscribed` | Un participante ha optado por no recibir comunicaciones por correo electrónico de Extole.| Correo electrónico  <br>ID externo  <br>Estado de la suscripción (desuscrito)  <br>ID del grupo de suscripción  | Tipo de lista |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Recompensas de Extole

Por defecto, Extole enviará los eventos de recompensa en el estado `FULFILLED` a Braze para que puedas desencadenar notificaciones de recompensa a través de una campaña Braze o Canvas. Consulta la tabla siguiente para conocer otros estados de recompensa.

| Estado de la recompensa | Descripción | Propiedades del evento | Atributos del usuario |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | El estado por defecto. Un proveedor de recompensas de Extole ha asignado un valor a la recompensa (como un cupón o una tarjeta regalo). | Correo electrónico <br>Valor nominal  <br>Código del cupón  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `EARNED` | Se ha creado una recompensa y se ha asociado a una persona. | Correo electrónico <br>Valor nominal  <br>Código del cupón  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `SENT` | La recompensa se ha cumplido y se ha enviado por correo electrónico o a través de un dispositivo al destinatario. | Correo electrónico <br>Valor nominal  <br>Código del cupón  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `REDEEMED` | La recompensa ha sido utilizada por el destinatario, como lo demuestra un evento de conversión o canje enviado a Extole.| Correo electrónico <br>Valor nominal  <br>Código del cupón  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `FAILED` | Un problema ha impedido que se emita o envíe la recompensa, lo que requiere atención. | Correo electrónico <br>Valor nominal  <br>Código del cupón  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `CANCELED` | La recompensa se ha desactivado y volverá al inventario. | Correo electrónico <br>Valor nominal  <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
| `REVOKED` | La recompensa cumplida ha sido invalidada. Por ejemplo, Extole solicitó una tarjeta regalo de un proveedor y luego determinó que la tarjeta se había enviado por error. Si el proveedor apoya la revocación de la recompensa, Extole solicitará la devolución de los fondos y la recompensa dejará de ser válida. | Correo electrónico <br>Valor nominal   <br>Tipo de valor nominal  | Correo electrónico <br>Nombre  <br>Apellido |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Personalización

### Buscar y crear usuarios en Braze

Para determinados casos de uso, como una nueva suscripción por correo electrónico o SMS en la que Extole no dispone de un identificador externo (identificador de usuario), Extole puede comprobar el identificador del usuario mediante el [punto final Export user profile by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) de Braze. Extole añadirá y actualizará los atributos del perfil si el usuario existe en Braze. Si la solicitud no devuelve un perfil de usuario, Extole utilizará el endpoint `/users/track` para crear un alias de usuario con la dirección de correo electrónico del usuario como nombre del alias.

## Mediante esta integración

Tras conectar sus cuentas, los eventos comenzarán a fluir automáticamente de Extole a Braze sin ninguna acción por su parte. Puedes ver en vivo los eventos que se envían a Braze en el Centro de Webhooks Salientes de Extole para la solución de problemas. 

