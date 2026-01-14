---
nav_title: Acerca de Audience Sync
article_title: Acerca de Audience Sync
alias: /partners/about_audience_sync/
description: "En este artículo de referencia se explica cómo utilizar Braze Audience Sync con Facebook para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 0
Tool:
  - Canvas

---

# Acerca de Audience Sync

> La característica Braze Audience Sync te ayuda a ampliar el alcance de tus campañas a muchas de las principales tecnologías sociales y publicitarias. A través de [Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas), las marcas pueden sincronizar de forma dinámica y segura datos de usuarios de primera mano en el ecosistema publicitario para impulsar el marketing y la eficiencia operativa.

## Disponibilidad de características

Todos los clientes de Braze tendrán acceso inmediato a la Sincronización de Audiencias con Google y Facebook. Para desbloquear destinos adicionales de Audience Sync, como TikTok, Pinterest, Snapchat o Criteo, tendrás que comprar Audience Sync Pro. Póngase en contacto con su gestor de cuentas Braze para obtener más información.

## Ejemplos

- Dirigirse a usuarios de alto valor utilizando canales propios y de pago para aumentar las compras o la interacción.
- Creación de audiencias similares de sus usuarios de alto valor para optimizar los costes de adquisición de nuevos usuarios y las conversiones.
- Reorientar a los usuarios con anuncios que son menos receptivos a otros canales de marketing.
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de su marca.

## Resumen

<style>
table td {
    word-break: break-word;
}
</style>

| Destino | Tiempo para que el destino coincida con los miembros de la audiencia | Límite de velocidad | Similitud o semejanza | Consejos |
| --- | --- | --- | --- | --- |
| [Criteo]({{site.baseurl}}/partners/canvas_audience_sync/criteo_audience_sync/) | Hasta 24 horas | 250.000 solicitudes por minuto. Por lotes cada 5 segundos con un reintento automático basado en la respuesta de Google. | Sí | {::nomarkdown}<ul><li>Criteo admite hasta 1.000 audiencias de anuncios.</li><li>La audiencia mínima es de 500 personas, y la recomendada es de más de 20.000.</li></ul>{:/} |
| [Facebook o Instagram]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) | Hasta 24 horas | 190.000 cuentas de anuncios por hora | Sí | {::nomarkdown}<ul><li>Facebook admite hasta 500 audiencias de anuncios.</li><li>Facebook requiere audiencias de al menos 1.000 usuarios.</li></ul>{:/} |
| [Google Ads o YouTube]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) | Entre 6 y 12 horas | Por lotes cada 5 segundos con un auto-reintento basado en la respuesta de Google | No | {::nomarkdown}<ul><li><b>A juego con el cliente:</b> Utiliza el anuncio del móvil, la dirección de correo electrónico o el número de teléfono.</li><li>Google Audience requiere al menos 5.000 usuarios para empezar a publicar anuncios.</li><li>El tamaño de la audiencia se mostrará como cero hasta que haya al menos 1.000 usuarios.</li></ul>{:/} |
| [LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/) | 48 horas | LinkedIn procesa 10 consultas por segundo y 100.000 usuarios por solicitud. Braze agrupa a los usuarios cada 5 segundos. | Audiencias predictivas con IA | {::nomarkdown}<ul><li>El tamaño mínimo de la audiencia es de 300 miembros, teniendo en cuenta la ubicación.</li><li>LinkedIn muestra la tasa en el panel de Braze.</li></ul>{:/} |
| [Pinterest]({{site.baseurl}}/partners/canvas_audience_sync/pinterest_audience_sync/) | Entre 24 y 48 horas | Pinterest procesa 7 consultas por segundo y 100.000 usuarios por solicitud. Braze agrupa a los usuarios cada 5 segundos. | Sí | Las audiencias de Pinterest requieren al menos 100 usuarios. |
| [Snapchat]({{site.baseurl}}/partners/canvas_audience_sync/snapchat_audience_sync/) | N/A | Snapchat procesa 10 consultas por segundo y 100.000 usuarios por solicitud. Braze agrupa a los usuarios cada 5 segundos. | Sí | Snapchat admite hasta 1.000 audiencias de anuncios. |
| [TikTok]({{site.baseurl}}/partners/canvas_audience_sync/tiktok_audience_sync/) | Entre 24 y 48 horas | TikTok procesa 50 consultas por segundo y 10.000 usuarios por solicitud. Braze agrupa a los usuarios cada 5 segundos. | Sí | {::nomarkdown}<ul><li>TikTok admite hasta 400 audiencias de anuncios.</li><li>Las audiencias de TikTok requieren al menos 1.000 usuarios para empezar a mostrar anuncios.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
<sup>Cuando se alcance el límite de velocidad, Braze reintentará las sincronizaciones durante 13 horas.</sup>

## Cómo funciona

Para utilizar Audience Sync con Google o Facebook, conecta tu cuenta de anuncios buscando al socio en la página de **socios tecnológicos**.

![Socio tecnológico de Facebook.]({% image_buster /assets/img/audience_sync/facebook_partner.png %}){: style="max-width:35%;"} ![Socio tecnológico de Google Ads.]({% image_buster /assets/img/audience_sync/google_ads_partner.png %}){: style="max-width:35%;"}

Después de conectar tu cuenta de publicidad, puedes crear un Canvas con un paso en Canvas de Sincronización de audiencia.

![Menú del componente Canvas para añadir el paso Sincronización de la audiencia al recorrido del usuario.]({% image_buster /assets/img/audience_sync/audience_sync7.png %}){: style="max-width:75%;"}

A continuación, selecciona el socio para sincronizar audiencias.

![Opción para seleccionar tu socio de sincronización de audiencia en el paso Sincronización de audiencia.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:85%;"}

Para cada socio, tendrás que configurar lo siguiente como parte del paso de sincronización de audiencias: 

- Cuenta publicitaria
- Audiencia 
- Acción de añadir o eliminar usuarios 
- Campos que deben coincidir 

Tenga en cuenta que Braze sincronizará a los usuarios en cuanto entren en el paso Sincronización de público dentro de su Canvas. 

Para cada destino de la Sincronización de Audiencias, el socio puede tener diferentes requisitos sobre los campos que podemos enviar. Consulta la documentación específica del socio para más detalles. 

### Audience Sync Pro

Para utilizar un socio de Audience Sync Pro, como TikTok, Pinterest, Snapchat o Criteo, podrás seleccionar tus socios en función de tus asignaciones de compra de Audience Sync Pro en la sección **Audience Sync Pro** de la página de **socios tecnológicos**.

![Audience Sync Pro sin socios seleccionados todavía.]({% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}){: style="max-width:75%;"}

Primero, selecciona los socios que pretendes utilizar seleccionando Seleccionar socios. Cada compra de Audience Sync Pro te proporcionará 3 destinos asignados de Audience Sync Pro, que estarán disponibles en cada uno de tus espacios de trabajo dentro de tu panel.

![Opción de seleccionar hasta tres socios para conectarse a Braze.]({% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}){: style="max-width:65%;"}

Después de seleccionar tus destinos de Audience Sync Pro, conecta la cuenta de publicidad de tu socio seleccionado haciendo clic en el mosaico de socios.

![Un ejemplo de Snapchat y TikTok seleccionados como socios para Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}){: style="max-width:70%;"}

![Audiencia de Snapchat Sincroniza la configuración con el mensaje: "Has conectado con éxito 1 cuenta de Snapchat".]({% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}){: style="max-width:70%;"}

Por último, crea tu paso en Canvas para la Sincronización de Audiencias utilizando este destino de Audience Sync Pro.

### Correos electrónicos de error de Sincronización de Audiencias

Si el error está relacionado con la integración del socio en general (como un problema de autorización), se envía un correo electrónico al usuario que conectó la integración. Si ese usuario ya no existe, los administradores recibirán los correos electrónicos. 

Si el error está relacionado con problemas con el componente Sincronización de audiencia (como "La audiencia no existe") en Canvas, se envía un correo electrónico al usuario que configuró el Canvas. Si ese usuario ya no existe, entonces recae en el administrador de la empresa.

Para configurar quién recibirá estos correos electrónicos, ponte en contacto con tu administrador del éxito del cliente para añadir destinatarios en **Preferencias de notificación**. Dado que esta característica cambiará el comportamiento actual, tendrás que añadir inmediatamente destinatarios a esta nueva preferencia de notificación, ya que Braze no da la adhesión voluntaria a nadie de forma predeterminada, y para asegurarte de que no se pierda ningún correo electrónico de error.

## Consideraciones sobre la privacidad de los datos

{% alert important %}
Esta documentación no pretende ofrecer asesoramiento jurídico ni puede considerarse como tal. El uso de Audience Sync está sujeto a requisitos legales específicos. Para asegurarse de que lo utiliza de conformidad con la legislación vigente, consulte a su asesor jurídico.
{% endalert %}

Al crear audiencias para el seguimiento de anuncios, es posible que desee incluir o excluir a determinados usuarios en función de sus preferencias y para cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la [CCPA](https://oag.ca.gov/privacy/ccpa). Los vendedores deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada en Canvas. A continuación enumeramos algunas opciones.

Si has recogido el [IDFA de iOS a través del SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), podrás utilizar el filtro "Seguimiento de anuncios habilitado". Selecciona el valor como `true` para enviar sólo a los usuarios a los destinos de Audience Sync en los que hayan optado por la adhesión voluntaria.

![Un Canvas con una audiencia de entrada de "El seguimiento de anuncios habilitado es verdadero".]({% image_buster /assets/img/audience_sync/audience_sync2.png %})

Si estás recopilando `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, o cualquier otro atributo personalizado relevante, debes incluirlos dentro de tus criterios de entrada en Canvas como filtro:

![Un Canvas con una audiencia de entrada de "opted_in_marketing igual a true".]({% image_buster /assets/img/audience_sync/audience_sync.png %})

Para saber más sobre cómo cumplir estas leyes de Protección de Datos dentro de la plataforma Braze, consulta la [Asistencia Técnica sobre Protección de Datos]({{site.baseurl}}/dp-technical-assistance/).

## Gestión del consentimiento para la orientación publicitaria

Como anunciante, es tu responsabilidad gestionar el consentimiento para el seguimiento de anuncios o la segmentación de tus usuarios.

Para enviar anuncios a tus usuarios, debes cumplir todas las leyes y normativas aplicables, así como las políticas y requisitos de la plataforma publicitaria. Utiliza Braze sólo para segmentar y sincronizar usuarios cuando hayas obtenido su consentimiento. 

Para mantener actualizadas tus listas de audiencia en estas plataformas publicitarias y eliminar a los usuarios que hayan revocado su consentimiento, configura un Canvas para eliminar a los usuarios de estas listas de audiencia existentes mediante un paso en Canvas de Sincronización de audiencias.


