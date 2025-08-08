---
nav_title: Adobe
article_title: Adobe
description: "Esta página describe la asociación entre Braze y Adobe, una plataforma de datos de los clientes, que permite a las marcas conectar y mapear sus datos de Adobe (atributos personalizados y segmentos) con Braze en tiempo real. A continuación, las marcas pueden actuar en función de estos datos y ofrecer experiencias personalizadas y específicas a esos usuarios."
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Construida sobre la Plataforma de Experiencia de Adobe, la plataforma de datos de los clientes en tiempo real de Adobe reúne datos conocidos y anónimos de múltiples fuentes empresariales para crear perfiles de clientes. Estos perfiles pueden utilizarse para ofrecer experiencias personalizadas en todos los canales y dispositivos en tiempo real.

La integración de Braze y Adobe CDP conecta y mapea los datos de Adobe de tu marca (atributos personalizados y segmentos) con Braze en tiempo real. A continuación, puedes actuar sobre estos datos, entregando experiencias personalizadas y dirigidas a tus usuarios. Con Adobe, la integración es intuitiva. Basta con tomar cualquier [identidad](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en) de Adobe, asignarla a un ID externo Braze y enviarla a la plataforma Braze. Todos los datos enviados serán accesibles en Braze a través de un nuevo atributo `AdobeExperiencePlatformSegments`.

{% alert important %}
Actualmente, la integración de Adobe Experience Platform no admite la afiliación dinámica de audiencias. Esto significa que sólo puede añadir valores a los perfiles de usuario, no eliminarlos.
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Adobe | Se necesita una [cuenta de Adobe](https://account.adobe.com/) para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Instancia de soldadura | Puedes obtener tu instancia de Braze a través de tu administrador de incorporación a Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints). |
| Punto final REST Braze | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
El envío de atributos personalizados adicionales aumentará el uso de punto de datos. Te sugerimos que hables con tu administrador del éxito del cliente para comprender mejor este posible aumento del punto de datos.
{% endalert %}

## Integración

### Paso 1: Configurar el destino Braze

En la página **Configuración de** Adobe, selecciona **Destinos** en **Colecciones**. Desde ahí, localiza el mosaico **Braze** y selecciona **Configurar**. 

![]({% image_buster /assets/img/adobe/braze-destination-configure.png %})

{% alert note %}
Si ya existe una conexión con Braze, verás un botón **Activar** en la tarjeta de destino. Para obtener más información sobre la diferencia entre activar y configurar, consulte la sección de catálogo de la [documentación](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog) del espacio de trabajo de destino de Adobe.
{% endalert %}

### Paso 2: Proporcionar el token Braze

En el paso **Cuenta**, proporciona tu clave de API de Braze y selecciona **Conectar con destino**.

![]({% image_buster /assets/img/adobe/braze-destination-account.png %}){: style="max-width:60%"}

### Paso 3: Autenticación

A continuación, en el paso **Autenticación**, introduce los datos de tu conexión Braze:
- **Nombre**: Introduce el nombre con el que te gustaría reconocer este destino en el futuro.
- **Destino**: Introduzca una descripción que le ayude a identificar este destino.
- **Instancia del punto final**: Introduce tu instancia de Braze.
- **Caso de uso de marketing**: Los casos de uso de marketing indican la intención para la que se exportarán los datos al destino. Puede seleccionar entre los casos de uso de marketing definidos por Adobe o crear su propio caso de uso de marketing. Para obtener más información sobre los casos de uso de marketing de Adobe, visita [El gobierno de los datos en Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

![]({% image_buster /assets/img/adobe/braze-destination-authentication.png %}){: style="max-width:60%;"}

### Paso 4: Crear destino
Selecciona **Crear destino**. Se ha creado tu destino. Puedes seleccionar **Guardar y Salir** para activar los segmentos más tarde o **Siguiente** para continuar el flujo de trabajo y seleccionar los segmentos a activar. 

### Paso 5: Activar segmentos
Active los datos que tiene en el CDP en tiempo real de Adobe asignando segmentos al destino Braze.

En la siguiente lista se indican los pasos generales necesarios para activar un segmento. Para obtener información detallada sobre los segmentos de Adobe y el flujo de trabajo de activación de segmentos, visita [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Selecciona y activa el destino Braze.
2. Seleccione los segmentos aplicables.
4. Configure la programación y los nombres de archivo para cada segmento que exporte.
5. Seleccione los atributos que desea enviar a Braze.
6. Revise y verifique la activación.

### Paso 6: Mapeado del terreno

Para enviar correctamente los datos de tu audiencia desde Adobe Experience Platform a Braze, debes completar el paso de mapeado de campos. La asignación crea un vínculo entre los campos del modelo de datos de Adobe Experience y los campos correspondientes de la plataforma Braze.

1. En el paso de mapeado, selecciona **Añadir nuevo mapeado**.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping.png %}){: style="max-width:50%;"}<br><br>
2. En la sección de campo vacío, selecciona el botón de flecha situado junto al campo vacío para abrir la ventana de selección de campo vacío.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-source.png %})<br><br>
3. En la ventana, selecciona los atributos de Adobe para mapearlos con tus atributos Braze. <br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}){: style="max-width:70%;"}<br><br>A continuación, selecciona el espacio de nombres de identidad. Esta opción se utiliza para asignar un espacio de nombres de identidad de plataforma a un espacio de nombres Braze.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}){: style="max-width:80%;"}<br> Elige tus campos fuente y selecciona **Seleccionar**.<br><br>
4. En la sección del campo de destino, selecciona el icono de mapeado situado junto al campo.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}){: style="max-width:90%;"} <br><br>
5. En la ventana de selección de campos de destino, puede elegir entre tres categorías de campos de destino:<br><br>- **Selecciona el espacio de nombres de identidad**: Utilice esta opción para asignar espacios de nombres de identidad de Platform a espacios de nombres de identidad de Braze.<br>- **Selecciona atributos personalizados**: Utilice esta opción para asignar atributos Adobe XDM a atributos Braze personalizados que haya definido en su cuenta Braze. <br><br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}){: style="max-width:60%;"}<br><br>**También puede utilizar esta opción para renombrar atributos XDM existentes en Braze.** Por ejemplo, al mapear un atributo `lastname` XDM a un atributo personalizado `Last_Name` en Braze, se creará el atributo `Last_Name` en Braze si aún no existe, y se mapeará el atributo `lastname` XDM a él. <br><br> Elige los campos de destino y selecciona **Seleccionar**.<br><br>
6. Tu campo mapeado debería aparecer en la lista.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %})<br><br>
7. Para añadir más asignaciones, repita los pasos del 1 al 6, según sea necesario. 

## Casos de uso

Digamos que su esquema de perfil XDM y su instancia Braze contienen los siguientes atributos e identidades:

|     | Esquema del perfil XDM | Instancia de soldadura |
| --- | ------------------ | -------------- |
| Atributos | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| Identidades | - `Email`<br>\- ID de anuncio de Google (`GAID`)<br>\- ID de Apple para anunciantes (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

La asignación correcta sería la siguiente:

![Asignaciones de destino: IdentityMap:IDFA mapeado a IdentityMap:external_id, IdentityMap:GAID mapeado a IdentityMap:external_id, IdentityMap:Email mapeado a IdentityMap:external_id, xdm:mobilePhone.number mapeado a CustomAttribute:PhoneNumber, xdm:person.name.lastName mapeado a CustomAttribute:LastName, xdm:person.name.firstName mapeado a CustomAttribute:FirstName]({% image_buster /assets/img/adobe/braze-destination-mapping-example.png %})

## Datos exportados
Para verificar si los datos se han exportado correctamente a Braze, comprueba tu cuenta Braze. Los segmentos de Adobe Experience Platform se exportan a Braze con el atributo `AdobeExperiencePlatformSegments`.

## Uso y gobernanza de los datos
Todos los destinos de Adobe Experience Platform cumplen las políticas de uso de datos cuando manejan tus datos. Consulta [Gobernanza de datos en tiempo real CDP](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) para obtener información detallada sobre cómo Adobe Experience Platform aplica la gobernanza de datos. 

