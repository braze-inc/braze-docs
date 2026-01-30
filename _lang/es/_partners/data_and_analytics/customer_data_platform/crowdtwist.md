---
nav_title: Oracle Crowdtwist
article_title: Crowdtwist
description: "Este artículo describe la asociación entre Braze y Oracle Crowdtwist, mediante plantillas de transformación de datos Braze especialmente creadas y objetos de push de datos de Crowdtwist."
page_type: partner
search_tag: Partner

---

# Oracle Crowdtwist

> [Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) es una solución líder de fidelización de clientes nativa en la nube que permite a las marcas ofrecer experiencias del cliente personalizadas. Su solución ofrece más de 100 vías de interacción listas para usar, lo que permite a los especialistas en marketing desarrollar rápidamente una visión más completa del cliente.

La característica Data Push de Oracle Crowdtwist permite pasar metadatos de usuarios o eventos cada vez que se produce una actualización en la plataforma Crowdtwist.

Esta guía describe cómo integrar las fuentes push en vivo de perfil de usuario, actividad de usuario y canje de usuarios de Oracle Crowdtwist en tu entorno Braze. Existen dos tipos adicionales de Data Push que no se tratan explícitamente en esta documentación, pero su configuración sigue los mismos principios que se describen a continuación. 

* [Perfil de usuario push en vivo](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/PushUserProfile-withTiersv2.html): Incluye la creación de nuevos perfiles y la actualización de los existentes.

* [Actividad de usuario push en vivo](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html): Incluye datos sobre la finalización de la actividad de los usuarios.

* [Canje de usuarios push en vivo](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserRedemption.html): Incluye datos sobre los canjes de recompensas de los usuarios. 

Utilizando una plantilla de Transformación de Datos Braze, puedes filtrar los elementos del Data Push que no son relevantes para Braze, y asignar los valores necesarios en Braze para que puedan ser aprovechados por los "destinos" disponibles.

Por ejemplo, utiliza un Push de datos para pasar eventos y atributos personalizados relevantes a Braze, como cuando un usuario cambia de nivel de fidelización o canjea una recompensa. También puedes utilizarlo para registrar atributos personalizados en Braze en cuanto se actualicen esos datos en el perfil de usuario de un miembro, como el saldo de puntos de un usuario. 

## Requisitos previos


| Requisito | Descripción |
| --- | --- |
| Cuenta Oracle Crowdtwist | Se necesita una [cuenta Oracle Crowdtwist](https://www.oracle.com/uk/cx/marketing/customer-loyalty/) para aprovechar esta asociación. |
| Punto final de transformación de datos Braze| Esta integración se basa en la [Herramienta de Transformación de Datos]({{site.baseurl}}/user_guide/data/data_transformation/overview) de Braze. Cuando creas una Transformación de Datos, Braze genera un punto final único que puedes añadir como destino para el Push de Datos de Crowdtwist.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Braze y Oracle Crowdtwist han creado [plantillas de Transformación]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation?redirected=1#step-2-create-a-transformation) de Datos para ayudar a nuestros clientes a desarrollar sus propias Transformaciones de Datos que aprovechen los eventos Perfil de Usuario, Canje de Usuario y Actividad de Usuario. 

## Paso 1: Crear transformación de datos a partir de la plantilla Oracle Crowdtwist

Ve a **Configuración de datos > Transformación de datos > Crear transformaciones > Utilizar una plantilla** > y selecciona la plantilla "BRAZE <> CROWDTWIST" que prefieras. 

Encontrarás cuatro plantillas: una para transformar los eventos Perfil de usuario, Actividad de usuario y Canje de usuario, y una plantilla maestra que utiliza la lógica condicional para aplicarla a varios eventos Push de datos.

Como se muestra en [la documentación de Oracle Crowdtwist sobre Data Push](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/DataPush.html), los objetos Data Push contienen metadatos diferentes, por lo que cada uno requiere su propio código de transformación para crear los objetos Braze adecuados. La plantilla maestra ilustra cómo configurar una única Transformación de datos para que acepte cada uno de los tres tipos de objetos y crea una salida adecuada con valores de cada objeto.

## Paso 2: Actualizar y probar la plantilla

A continuación, verás las plantillas anotadas. El cuerpo de estas plantillas está diseñado para aplicarse al destino `/users/track`. Las anotaciones están marcadas con el inicio de línea `//` y texto verde, y puedes borrarlas sin que ello afecte al funcionamiento del código de transformación. 

La transformación utiliza JavaScript, que construye un objeto llamado "brazecall". En este objeto se crea el cuerpo de la solicitud que se envía a un punto final de la API REST de Braze. Para orientarte sobre las estructuras requeridas de las solicitudes a estos destinos, consulta los enlaces de la sección "destinos".    

{% alert note %}
Observa que los "valores" de cada "clave" empiezan por `payload.`. La carga útil representa el objeto de datos recibido de Oracle Crowdtwist. Utiliza la notación de puntos de JavaScript para elegir qué datos quieres que rellenen los elementos de tu objeto Braze. Por ejemplo, cuando veas `external_id: payload.thirdPartyId`, significa que el ID externo de Braze está establecido por el valor `third_party_id` almacenado en Oracle Crowdtwist. Para más información sobre el esquema o la composición de los objetos procedentes de Oracle Crowdtwist, consulta [la documentación de Oracle.](https://docs.oracle.com/en/cloud/saas/marketing/crowdtwist-develop/Developers/LivePushUserActivity.html)
{% endalert %}

{% alert important %}
 Utiliza los objetos enviados desde Oracle Crowdtwist para crear usuarios en Braze. Al incluir la clave `update_existing_only` con el valor `false`, si un objeto de atributo o evento incluye un identificador que no existe en Braze, Braze crea un perfil de usuario con los atributos incluidos en el objeto de evento o atributo. Si prefieres que Oracle Crowdtwist actualice sólo los perfiles que ya existen en Braze, establece este atributo en `true` en cada atributo u objeto de evento.
{% endalert %}

### Plantillas de transformación de datos
{% tabs %}
{% tab User Profile Event Template%}
```javascript
let brazecall = {
 "attributes": [
   {
     //You must include an appropriate identifier for your attribute or event object from data available in Oracle Crowdtwist. This could be an external ID, Braze ID, user alias, phone, or email address for attribute or event objects.
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
   // **Important** To allow Oracle Crowdtwist events to create users in Braze, set the value of "_update_existing_only" to false. Otherwise, set this value to true in your event and attribute objects.
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
 //In this example, the "tierInfo" object from Crowdtwist is transformed into a Braze Nested Custom Attribute. Use the "_merge_objects" value to avoid duplications in a data point efficient manner.
 //The "tierinfo_current_level" attribute is a flat Braze custom attribute, while "tierInfo" below is a nested object mirroring the Crowdtwist payload; the difference in capitalization is intentional.
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{ 
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
//Below we show how to create both custom attributes and events from a single Crowdtwist User Profile object.
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
//Below we can see how to write a timestamp in your object, which is a required value for some objects, like the Event Object. 
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
// After the /users/track request is assigned to brazecall, return brazecall to create an output.
return brazecall;

```

{% endtab %}
{% tab User Activity Event Template %}
```javascript
let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
```
{% endtab %}
{% tab Redemption Event Template %}
```javascript
let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   //A user redemption event may not have a third party id, in which case you can instead provide the opportunity to include a user alias.
   "user_alias": { "alias_name" : "crowdtwist_redemption_username", "alias_label" : payload.userName},
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;

```
{%endtab%}
{% tab Master Template %}
```javascript
//The master template uses JavaScript's conditional operators to determine the output of the Data Transformation. This example shows how to apply JavaScript to your transformation to allow for a dynamic range of sources or inputs. 

 // We open the transformation with a simple "if" function. We're checking if the value "payload.tierInfo" is present. "tierInfo" is a value that is always populated in the User Profile Live Push object, but is not present in the others.

if (payload.tierInfo) {
let brazecall = {
 "attributes": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "_update_existing_only": false,
     "crowdtwist_loyalty_points": payload.redeemablePoints,
     "tierinfo_current_level": payload.tierInfo.currentLevel,
     "_merge_objects" : true,
     "tierInfo" : {
       "resetDate": payload.tierInfo.resetDate,
       "dateReached":payload.tierInfo.dateReached,
        "scoreNeededToReach": payload.tierInfo.scoreNeededToReach,
        "nextLevel":{ 
        "minValue":payload.tierInfo.nextLevel.minValue,
        "maxValue":payload.tierInfo.nextLevel.maxValue,
        "title":payload.tierInfo.nextLevel.title
     }
     }
   }
 ]
,
 "events": [
   {
     "external_id": payload.thirdPartyId,
     "email": payload.emailAddress,
     "name": "assignedByEvent",
     "time": new Date().toISOString(),
     "properties": {
       "assigned_by_event": payload.tierInfo.assignedByEvent,
       "date_assigned": payload.tierInfo.dateAssigned
     },
           "_update_existing_only": false
   }
 ]
};
return brazecall;
//Now we use an "else if" operator to change the "brazecall" body if the object is a User Activity event by checking if the unique key "activityId" has been populated.
} else if (payload.activityId) {
 let brazecall = {
"events": [
   {
     "external_id": payload.thirdPartyId,
     "_update_existing_only": false,
     "activityId": payload.activityId,
     "name": payload.activityName,
     "time": new Date().toISOString(),
     "properties": {
       "description": payload.description,
       "date_assigned": payload.dateAwarded
     }
   }
 ]
};
return brazecall;
//Finally, this conditional statement triggers if the Data Push object is a User Redemption event, based on whether a value populates in the key "rewardId".
} else if (payload.rewardId) {
 let brazecall = {
 "attributes": [
   {
   "external_id": payload.thirdPartyId,
   "_update_existing_only": false,
   "redeemed_coupon": payload.couponCode,
   "total_points_redeemed": payload.totalPointsRedeemed
      }
]
}
return brazecall;
} else {
 //Include this error message to help with troubleshooting in the log if a call fails. Replace the text in the parentheses with anything that might be clearer to your team based on your Data Transformation.
 throw new Error("No appropriate Identifiers found");
}

```
{% endtab %}
{% endtabs %}

### Destinos

Las plantillas de esta guía se han creado para entregar al destino "Seguimiento de usuarios", pero puedes diseñar tu plantilla para enviar a cualquiera de los puntos finales enumerados en [la guía de Transformación de datos de Braze]({{site.baseurl}}/user_guide/data/data_transformation/creating_a_transformation/#step-2-create-a-transformation), con el apoyo de la [documentación de la API REST]({{site.baseurl}}/api/home) asociada.

### Pruebas

Después de modificar la plantilla a tu gusto, debes validar que funciona correctamente. Haz clic en "Validar" para obtener una vista previa de la salida de tu código y comprobar si es una solicitud aceptable para el destino elegido. 

![Captura de pantalla de la IU de transformación de datos Braze]({% image_buster /assets/img/crowdtwist_tools/screenshot.png %}){: style="max-width:70%;margin-bottom:15px;border:none;"}

Cuando estés satisfecho con el objeto que ves en el campo "salida", haz clic en **Activar** para que el punto final de Transformación de Datos esté listo para aceptar datos. 

Encontrarás la URL del webhook de tu Transformación de Datos en el panel lateral izquierdo. Cópialo y utilízalo para la configuración dentro del Hub de integración de Oracle Crowdtwist.

{% alert important %}
Los puntos finales de Transformación de Datos Braze tienen un límite de velocidad de 1000 peticiones por minuto. Considera la velocidad a la que quieres que estos datos estén disponibles en Braze, y habla con tu administrador de cuentas Braze si necesitas un límite de velocidad de Transformación de Datos más alto.
{% endalert %}

Las Transformaciones de Datos son una herramienta muy dinámica y puedes diseñarlas para fines que vayan más allá de lo expuesto en este documento con conocimientos de JavaScript y con la orientación de nuestra documentación de la API REST. Para obtener ayuda o solución de problemas sobre cambios complejos en tus plantillas de Transformación de datos, habla con tu administrador del éxito del cliente para conocer la orientación que tienes a tu disposición.