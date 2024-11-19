---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "Este artículo de referencia describe la asociación entre Braze y Kochava, una plataforma de atribución móvil que ofrece perspectivas de atribución y análisis para ayudarle a aprovechar sus datos para el crecimiento."
page_type: partner
search_tag: Partner

---

# Kochava

> Kochava ofrece soluciones de análisis y atribución móvil para ayudarte a potenciar tus datos para crecer. La plataforma de audiencia de Kochava te permite planificar, direccionar, activar, medir y optimizar tus campañas de aplicaciones.

La integración de Braze y Kochava ayuda a impulsar una comprensión más holística de sus campañas mediante el envío de datos de atribución a Braze para comprender mejor qué campañas están impulsando las instalaciones, la actividad dentro de la aplicación y mucho más.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Kochava | Para beneficiarse de esta asociación es necesario disponer de una cuenta Kochava. |
| Aplicación para iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de su plataforma, es posible que se requieran fragmentos de código en su aplicación. Encontrará más detalles sobre estos requisitos en el paso 1 del proceso de integración. |
| SDK de Kochava | Además del SDK de Braze necesario, debes instalar el [SDK de Kochava](https://support.kochava.com/sdk-integration/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Asignar ID de usuario

#### Android

El SDK de [Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3) genera un GUID como ID de Braze al iniciar la sesión. Este es el identificador que recomendamos pasar al método Kochava `IdentityLink`, ya que permite a Braze reconciliar los datos con el perfil de usuario correcto. El ID de Braze se puede recuperar mediante el siguiente método:

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
Antes de febrero de 2023, nuestra integración de atribución de Kochava utilizaba el IDFV como identificador principal para cotejar los datos de atribución de iOS. No es necesario que los clientes de Braze que utilicen Objective-C obtengan el Braze `device_id` y lo envíen a Kochava al instalarlo, ya que no habrá interrupción del servicio.
{% endalert%}

Para los que utilicen Swift SDK v5.7.0+, si deseas seguir utilizando IDFV como identificador mutuo, debes asegurarte de que el campo `useUUIDAsDeviceId` está configurado en `false` para que no haya interrupciones en la integración. Si se establece en `true`, debe implementar la asignación de ID de dispositivo iOS para Swift con el fin de pasar el `device_id` de Braze a Kochava al instalar la aplicación para que Braze coincida correctamente con las atribuciones de iOS.

Braze tiene dos APIs que producirán el mismo valor, una con un manejador de finalización y otra usando el nuevo soporte de concurrencia de Swift. Tenga en cuenta que tendrá que modificar los siguientes fragmentos de código para ajustarlos a las instrucciones [del SDK para iOS](https://support.kochava.com/sdk-integration/ios-sdk-integration/) de Kochava. Si necesitas más ayuda, ponte en contacto con el servicio de asistencia de Kochava.

##### Gestor de finalización
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### Concurrencia Swift
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### Paso 2: Obtener la clave de importación de datos Braze

En Braze, vaya a **Integraciones de socios** > **Socios tecnológicos** y seleccione **Kochava**. 

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), encontrará a **los socios tecnológicos** en **Integraciones**.
{% endalert %}

Aquí encontrarás el punto final REST y generarás tu clave de importación de datos Braze. Una vez generada la clave, puede crear una nueva o invalidar una existente. La clave de importación de datos y el punto final REST se utilizan en el siguiente paso al configurar un postback en el panel de control de Kochava.<br><br>![Esta imagen muestra la casilla "Importación de datos para la atribución de instalación" que se encuentra en la página de tecnología de Kochava. En este cuadro, se te muestra la clave de importación de datos y el punto final REST.][4]{: style="max-width:90%;"}

### Paso 3: Configurar un postback desde Kochava

[Añade un postback][18] en tu panel Kochava. Se le pedirá la clave de importación de datos y el punto final REST que encontró en el panel de Braze.

### Paso 4: Confirmar la integración

Una vez que Braze reciba los datos de atribución de Kochava, el indicador de estado de la conexión en la página de socios tecnológicos de Kochava en Braze cambiará de "No conectado" a "Conectado". También se incluirá una marca de tiempo de la última solicitud realizada con éxito. 

Ten en cuenta que esto no ocurrirá hasta que recibamos datos sobre una instalación atribuida. Las instalaciones orgánicas, que deben excluirse del postback de Kochava, son ignoradas por nuestra API y no se tienen en cuenta a la hora de determinar si se ha establecido una conexión satisfactoria.

## Datos de atribución de Facebook y X (antes Twitter)

Los datos de atribución de las campañas de Facebook y X (antes Twitter) no están disponibles a través de nuestros socios. Estas fuentes de medios no permiten a sus socios compartir datos de atribución con terceros y, por lo tanto, nuestros socios no pueden enviar esos datos a Braze.

## URL de seguimiento de clics de Kochava en Braze (opcional)

El uso de enlaces de seguimiento de clics en tus campañas Braze te permitirá ver fácilmente qué campañas están impulsando la instalación de aplicaciones y la reactivación de la interacción. Como resultado, podrá medir sus esfuerzos de marketing con mayor eficacia y tomar decisiones basadas en datos sobre dónde invertir más recursos para obtener el máximo rendimiento de la inversión.

Para empezar a utilizar los enlaces de seguimiento de clics de Kochava, visite su [documentación](https://support.kochava.com/reference-information/attribution-overview/). Puede insertar directamente los enlaces de seguimiento de clics de Kochava en sus campañas Braze. Kochava utilizará entonces sus [metodologías de atribución probabilística](https://www.kochava.com/getting-prepared-for-ios-14/) para atribuir al usuario que ha hecho clic en el enlace. Le recomendamos que añada un identificador de dispositivo a sus enlaces de seguimiento de Kochava para mejorar la precisión de las atribuciones de sus campañas Braze. Esto atribuirá de forma determinista al usuario que ha hecho clic en el enlace.

{% tabs local %}
{% tab Android %}
Para Android, Braze permite a los clientes la adhesión voluntaria a la [recopilación de ID de publicidad de Google (GAID)]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id). El GAID también se recoge de forma nativa a través de la integración del SDK de Kochava. Puede incluir el GAID en sus enlaces de seguimiento de clics de Kochava utilizando la siguiente lógica de Liquid:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Para iOS, tanto Braze como Kochava recopilan automáticamente el IDFV de forma nativa a través de nuestras integraciones SDK. Puede utilizarse como identificador del dispositivo. Puede incluir el IDFV en sus enlaces de seguimiento de clics de Kochava utilizando la siguiente lógica de Liquid:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Esta recomendación es meramente facultativa**<br>
Si actualmente no utiliza ningún identificador de dispositivo -como el IDFV o el GAID- en sus enlaces de seguimiento de clics, o no tiene previsto hacerlo en el futuro, Kochava podrá seguir atribuyendo estos clics a través de su modelado probabilístico.
{% endalert %}


[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Postbacks Kochava"
[29]: https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3
[30]: https://support.kochava.com/sdk-integration/windows-and-xbox-one-sdk-integration?scrollto=marker_8
[4]: {% image_buster /assets/img/attribution/kochava.png %}
