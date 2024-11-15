---
nav_title: Asistencia técnica en protección de datos
article_title: Asistencia técnica en protección de datos
page_order: 1
description: "Esta página proporciona instrucciones técnicas para habilitarte a gestionar, a través de la Plataforma Braze, las solicitudes de las personas en relación con sus derechos sobre los datos personales."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Asistencia técnica en protección de datos

Hay una serie de leyes de protección de datos que regulan lo que las organizaciones pueden hacer con los datos personales ("Leyes de Protección de Datos"), entre ellas el Reglamento General de Protección de Datos de la UE y del Reino Unido ("RGPD"), la Ley de Privacidad del Consumidor de California ("CCPA") y la Ley de Portabilidad y Responsabilidad del Seguro Médico ("HIPAA"). Existen otras leyes y normativas de protección de datos nacionales, estatales y específicas del sector que pueden aplicarse a tu empresa.

Estas leyes de protección de datos conceden a los individuos "derechos de privacidad" sobre sus datos personales. Las organizaciones están obligadas a recibir y responder a las solicitudes de las personas que ejercen sus derechos de privacidad. La plataforma Braze puede ayudarte en el cumplimiento de estas Leyes de Protección de Datos proporcionando características para facilitar ciertas acciones requeridas por dichas leyes. Este documento proporciona instrucciones técnicas para utilizar estas características para gestionar las solicitudes de derechos de privacidad. Te corresponde a ti determinar qué Leyes de Protección de Datos se aplican a tu empresa, y actuar de conformidad con ellas.

## Aviso legal

Nada de lo que sigue pretende ser, ni se considerará, asesoramiento jurídico por parte de Braze. Te aconsejamos que busques el asesoramiento de tu propio abogado con respecto a tu situación particular y al modo en que las Leyes de Protección de Datos se aplican a ti y a tu uso de los Servicios Braze.

## Terminología

A efectos de este documento, cualquier referencia a datos personales también puede entenderse como una referencia a información personal o información identificable personalmente ("Datos personales"). Para simplificar, generalmente nos basamos en el lenguaje del RGPD cuando abordamos los derechos de los usuarios finales. El lenguaje del RGPD es a menudo intercambiable o está estrechamente alineado con un término o concepto definido de otras Leyes de Protección de Datos.

## conceptos básicos

La mayoría de las leyes sobre privacidad definen tres partes interesadas principales que intervienen en el tratamiento de Datos Personales: los interesados, los responsables del tratamiento y los encargados del tratamiento. Cada grupo tiene diferentes derechos y responsabilidades en relación con el uso de los Datos Personales:

- Un sujeto de datos es un individuo cuyos Datos Personales están siendo procesados por el procesador o controlador de datos
- Un responsable del tratamiento es una entidad que determina los fines y los medios del tratamiento de los Datos Personales
- Un procesador de datos es una entidad que procesa Datos Personales en nombre y bajo las instrucciones del controlador de datos

En relación con la plataforma Braze:

- Los sujetos de datos son, por ejemplo, los usuarios finales de tu aplicación de cliente (e.g., tus clientes) o tus empleados que son usuarios del panel en tu instancia de la plataforma Braze.
- Tú, el cliente de Braze, eres el controlador de datos que decide cómo y por qué se recopilarán y procesarán los Datos Personales de los interesados dentro de la plataforma Braze.
- Braze es un procesador de datos que procesa Datos Personales en la plataforma Braze en tu nombre y de acuerdo con las instrucciones que recibimos de ti.

Los anteriores son términos del RGPD, pero, por ejemplo, estos son los términos comparables según la Ley de Privacidad del Consumidor de California (CCPA):

- "consumidores" para los sujetos de datos.
- "empresas" para los responsables del tratamiento.
- "proveedores de servicios" para los procesadores de datos.

A continuación encontrarás información relevante sobre las solicitudes de derechos de privacidad más comunes de los interesados, incluyendo cómo puedes responder a ellas a través de las características técnicas de la plataforma Braze.

## Derecho a ser informado

El derecho a ser informado engloba tu obligación de proporcionar "información sobre el tratamiento justo", normalmente a través de un aviso de privacidad. Enfatiza la necesidad de transparencia sobre cómo utilizas los Datos Personales.

### Recomendación Braze

La mayoría de las Leyes de Protección de Datos hacen hincapié en la necesidad de transparencia en relación con la forma en que utilizas los Datos Personales. Esto es responsabilidad de los responsables del tratamiento de datos, que normalmente mantendrán un aviso de privacidad que sea fácilmente accesible para los usuarios de sus productos y servicios y que cubra el tratamiento realizado por Braze.

## Derecho de acceso

En virtud de las leyes de protección de datos, los sujetos de datos pueden tener derecho a obtener:

- Confirmación de que sus Datos Personales están siendo procesados,
- Acceso a sus Datos Personales, y
- Otra información complementaria que determine la Ley de Protección de Datos aplicable.

### Recomendación Braze

Para proporcionar Datos personales de Braze en un formato legible por máquina en respuesta a la solicitud de acceso de un sujeto de datos, puedes exportar su Perfil de usuario final haciendo una llamada API a [las API REST](https://www.braze.com/docs/api/endpoints/export/#user-export) de Braze con su identificador de usuario (definido por ti como el `external_id` proporcionado a Braze) y/o su identificador de dispositivo.

## Derecho de rectificación

Las personas tienen derecho a que se corrijan sus Datos Personales si son inexactos o incompletos. Si has comunicado los Datos Personales en cuestión a terceros, puedes considerar la necesidad de informarles de la rectificación cuando sea posible.

### Recomendación Braze

En caso de que un Sujeto de los Datos solicite que rectifiques inexactitudes en los Datos Personales que estás procesando o que Braze está procesando en tu nombre, puedes utilizar los SDK de Braze o [las API REST de](https://www.braze.com/docs/api/endpoints/user_data/#user-track-endpoint) Braze para corregir dichos Datos Personales.

## El derecho a la eliminación

El derecho a la eliminación también se conoce como "derecho al olvido" o "derecho a ser eliminado".

### Recomendación Braze

#### Eliminación estándar 

Una vez que hayas detenido la recopilación de datos, puedes utilizar [el punto final de la API REST de eliminación de usuarios de Braze](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/) para eliminar a un usuario final, lo que eliminará todos los registros de dicho usuario final de los Servicios de Braze:

- Para los usuarios finales que tengan un ID externo dentro de los Servicios, puedes utilizar ese ID para eliminar los datos de ese usuario final.
- Para los usuarios finales anónimos que no tengan un identificador externo dentro de los Servicios, puedes recuperar el identificador de dispositivo de ese usuario final utilizando el SDK de Braze y puedes utilizar el identificador de dispositivo para encontrar el perfil de usuario final asociado a ese dispositivo. A continuación, puedes utilizar la API de eliminación de usuarios para eliminar el perfil asociado a ese usuario final.

La eliminación de un usuario final de los Servicios Braze eliminará de forma permanente el perfil de usuario centralizado de Braze para ese usuario final, tal y como se define en el sitio `external_id` proporcionado. Esto incluye información de perfil estructurada que Braze recopiló de forma predeterminada o que configuraste para que los Servicios Braze recopilaran, como información del dispositivo, país, idioma y dirección de correo electrónico.

Ten en cuenta que Braze podría seguir almacenando la dirección de correo electrónico o el número de teléfono asociados al perfil del usuario final, ya que podrían estar asociados al perfil de otro usuario final. Las direcciones de correo electrónico y los números de teléfono no son únicos en los Servicios Braze. Esto significa que tu equipo podría haber configurado Braze para almacenar la misma dirección de correo electrónico o número de teléfono en varios perfiles de usuario. Si tu equipo ha configurado Braze de este modo, ten en cuenta que es posible que tengas que eliminar todos los perfiles de usuario que representen a un determinado sujeto de datos para cumplir con la solicitud de eliminación de un sujeto de datos, y tu equipo tendría que realizar varias llamadas a la API para eliminar todos los perfiles de usuario que hagan referencia a un sujeto de datos concreto.

#### Consideraciones adicionales sobre la eliminación

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
<tbody>
  <tr>
    <td>
        <p>Los clientes pueden crear campos personalizados para propiedades del evento y extras de mensajería. Estos campos no están destinados a datos personales, por lo que no están incluidos en el proceso de eliminación predeterminado descrito anteriormente. Sin embargo, si utilizas Braze para introducir o recopilar datos personales a través de propiedades del evento y extras de mensajes, puedes configurar el proceso de eliminación desencadenado por el punto final de la API REST de eliminación de usuarios para que también incluya estos campos, de modo que los datos contenidos en estos campos también se eliminen.</p>
        <p>La configuración predeterminada se aplica a nivel de empresa, pero puedes elegir eliminar los siguientes campos cuando se ejecute el proceso de eliminación, a nivel de grupo de aplicaciones/espacio de trabajo:</p>
    <ul>
        <li>PROPIEDADES para USERS_BEHAVIORS_CUSTOMEVENT</li>
        <li>PROPIEDADES para USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS para:</li>
            <ul>
            <li>USERS_MESSAGES_CONTENTCARD</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>USERS_MESSAGES_WEBHOOK_SEND</li>
            <li>USERS_MESSAGES_SMS_SEND</li>
            <li>Futuros eventos de envío de mensajes</li>
            </ul>
    </ul>
    <p>Puedes acceder a esta configuración a través de <b>Configuración de la empresa</b> > <b>Configuración de administración</b> > <b>Configuración de seguridad</b>. Las preferencias de eliminación de datos se establecen por tipo o categoría de evento. Sólo un usuario con preferencias de Administrador puede realizar cambios en esta configuración. Alternativamente, un Administrador puede delegar estos permisos en otro usuario.</p>
    <p>Si se configura un tipo de evento o mensaje extra para que se incluya en el proceso de eliminación, los datos de este campo se eliminarán en adelante para los usuarios para los que estés ejecutando un punto final de la API REST de eliminación de usuarios. Además, cuando selecciones esta preferencia de eliminación, en el siguiente trabajo de eliminación programado, los datos de estos campos se eliminarán de cualquier conjunto de datos anonimizados existente que contenga estos campos. No será posible restaurar los campos de datos eliminados.</p>
    </td>
  </tr>
</tbody>
</table>

#### Análisis

Para mantener la integridad de los análisis de uso de campañas y aplicaciones, los datos agregados anónimos no se modificarán cuando se elimine a un usuario final. Por ejemplo, Braze no disminuirá el número total de sesiones de una aplicación cuando se elimine un usuario final. La sesión o sesiones en las que dicho usuario final visitó la aplicación seguirán estando incluidas en el número total de visitas a esa aplicación, pero esos datos no estarán conectados de ninguna manera al perfil del usuario final olvidado, lo que garantiza que estos datos anonimizados y agregados no puedan vincularse a un usuario final individual.

Los análisis dentro de los Servicios Braze están vinculados al identificador de usuario final Braze. Una vez eliminado el perfil del usuario final, el identificador de usuario Braze se convierte en un identificador completamente anónimo, ya que Braze no puede vincularlo a ningún usuario final individual.

#### Una vez que se ha producido la eliminación

Por lo general, se espera que hagas esfuerzos razonables para notificar a los interesados cuando hayas atendido su solicitud de borrar sus Datos Personales. Un usuario final eliminado puede volver a registrarse o reactivarse con tu aplicación o servicio más adelante, y Braze no podrá identificarlo como el usuario eliminado u olvidado. Los Servicios Braze no pueden crear listas de identificadores de usuario o direcciones de correo electrónico eliminadas en tu nombre.

## Derecho a la restricción del tratamiento

Los interesados pueden tener derecho a "bloquear" o suprimir el tratamiento de sus Datos Personales en determinadas circunstancias. Restringir el tratamiento significa no llevar a cabo ningún tratamiento al que se haya opuesto el interesado.

### Recomendación Braze

Los Servicios de Braze no admiten la restricción del procesamiento de categorías individuales de Datos Personales. Si un interesado te ha pedido que restrinjas el tratamiento de determinados subconjuntos de sus Datos personales, debes utilizar [las API de Braze](https://www.braze.com/docs/api/home/) para exportar el perfil o perfiles completos de ese usuario final y, a continuación, [eliminarlos](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) de Braze. Las API de Braze pueden utilizarse para reimportar estos datos en caso de que el usuario final te permita posteriormente procesar esos subconjuntos concretos de sus Datos Personales. Además, debes recomendar a tu usuario final que desinstale o cierre la sesión de todas y cada una de tus Aplicaciones que utilicen el SDK de Braze para dejar de recopilar datos adicionales sobre el interesado.

## Derecho a la portabilidad de datos

El derecho a la portabilidad de los datos permite a los interesados obtener y reutilizar sus Datos Personales para sus propios fines en diferentes servicios. Los Datos Personales deben facilitarse en un formato estructurado, legible por máquina y de uso común.

### Recomendación Braze

De forma similar al Derecho de Acceso, puedes utilizar la [API REST](https://www.braze.com/docs/api/endpoints/export/#user-export) de Braze para exportar los Datos Personales de un usuario final y proporcionárselos al Sujeto de los Datos conforme a su solicitud.

## Derecho de oposición

Las personas pueden tener derecho a oponerse:

- tratamiento basado en intereses legítimos o en el rendimiento de una tarea en interés público/ejercicio de la autoridad oficial (incluida la elaboración de perfiles);
- marketing directo (incluida la elaboración de perfiles); y
- tratamiento con fines de investigación científica/histórica y estadística.

### Recomendación Braze

Braze ofrece la posibilidad de marcar un perfil de usuario como dado de baja de SMS, correos electrónicos o notificaciones push tanto a través de nuestras [API REST](https://www.braze.com/docs/api/home/) como a través de los SDK de [iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/), [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) y [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/). Si recibes objeciones de los Sujetos de los Datos a recibir dichos mensajes, puedes utilizar las API de Braze para cancelar la suscripción de esos usuarios finales.

Si esto no fuera suficiente, para evitar el tratamiento de los Datos Personales del usuario final por parte de Braze, el perfil de usuario final deberá eliminarse de la misma forma que se especifica en el "Derecho de supresión".

## Derechos relacionados con la toma de decisiones automatizada y la elaboración de perfiles

Algunas Leyes de Protección de Datos impiden, o permiten a los interesados renunciar, a la automatización de la toma de decisiones o la elaboración de perfiles en determinadas circunstancias, en particular en el caso de decisiones que "produzcan un efecto jurídico o un efecto significativo similar sobre la persona".

### Recomendación Braze

Braze no realiza ninguna acción automatizada de elaboración de perfiles ni de toma de decisiones con ramificaciones legales o equivalentes para los interesados. Si crees que tu propio uso de la Plataforma Braze tendrá repercusiones legales o equivalentes y has recibido una objeción al respecto, puedes optar por eliminar el perfil de usuario de la misma forma que en el "Derecho de eliminación".

## Publicidad dirigida

En virtud de algunas leyes de privacidad del estado de EE.UU., los interesados pueden oponerse al uso de sus Datos Personales con fines de publicidad dirigida.

### Recomendación Braze

Al crear audiencias con el fin de dirigir anuncios a tus interesados, debes asegurarte de que has excluido a cualquier interesado que se haya opuesto a la publicidad dirigida, por ejemplo, los consumidores de California que hayan ejercido su derecho a "No vender ni compartir" en virtud de la CCPA.

Para obtener más información sobre cómo crear audiencias para sincronizarlas con plataformas de terceros, consulta [Sincronización de audiencias](https://www.braze.com/docs/partners/canvas_steps).

## Derecho a la no discriminación 

Los sujetos de datos tienen derecho a ejercer su derecho a la intimidad sin discriminación.

### Recomendación Braze

En su uso de los Servicios Braze, los clientes deben asegurarse de no discriminar a los interesados que hayan ejercido sus derechos de privacidad. Por ejemplo, recomendamos que los sujetos de datos que hayan ejercido su derecho a la intimidad no sean segmentados en audiencias o de otro modo que dé lugar a ser discriminados.