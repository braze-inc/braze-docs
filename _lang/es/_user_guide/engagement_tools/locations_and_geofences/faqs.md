---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre ubicación y geovallas
page_order: 4
page_type: FAQ
description: "Este artículo de referencia aborda algunas preguntas frecuentes en torno al uso del seguimiento de la ubicación y las geocercas."
tool: Location

---

# Preguntas más frecuentes

> Esta página ofrece respuestas a las preguntas más frecuentes sobre ubicaciones y geocercas.

## Seguimiento de la ubicación

### ¿Cuándo recopila Braze datos de localización?

Braze sólo recoge la ubicación cuando la aplicación está abierta en primer plano. Como resultado, nuestro filtro `Most Recent Location` se dirige a los usuarios en función de dónde abrieron la aplicación por última vez (también denominado inicio de sesión).

También debe tener en cuenta los siguientes matices:

- Si la localización está desactivada, el filtro `Most Recent Location` mostrará la última localización registrada.
- Si alguna vez se ha almacenado la ubicación de un usuario en su perfil, se le aplicará el filtro `Location Available`, aunque desde entonces haya optado por que no se rastree su ubicación.

### ¿Cuál es la diferencia entre los filtros Localización más reciente del dispositivo y Localización más reciente?

La dirección `Most Recent Device Locale` procede de la configuración del dispositivo del usuario. Por ejemplo, para los usuarios de iPhone aparece en su dispositivo en **Ajustes** > **General** > **Idioma y región**. Este filtro se utiliza para capturar el idioma y el formato regional, como fechas y direcciones, y es independiente del filtro `Most Recent Location`.

La dirección `Most Recent Location` es la última ubicación GPS conocida del dispositivo. Se actualiza al iniciar la sesión y se almacena en el perfil del usuario.

### Si un usuario renuncia al seguimiento de su ubicación, ¿se eliminarán de Braze sus antiguos datos de localización?

No. Si alguna vez se ha almacenado la ubicación de un usuario en su perfil, esos datos no se eliminarán automáticamente si posteriormente el usuario opta por no participar en el seguimiento de la ubicación.

## Geovallas

### ¿Cuál es la diferencia entre geovallas y seguimiento de ubicación?

En Braze, una geovalla es un concepto diferente del seguimiento de ubicación. Las geovallas se utilizan como desencadenantes de determinadas acciones. Una geovalla es un límite virtual establecido alrededor de una ubicación geográfica. Cuando un usuario entra o sale de este límite, puede desencadenar una acción específica, como el envío de un mensaje.

El seguimiento de la ubicación se utiliza para recopilar y almacenar los datos de ubicación más recientes de un usuario. Estos datos pueden utilizarse para segmentar a los usuarios en función del filtro `Most Recent Location`. Por ejemplo, puede utilizar el filtro `Most Recent Location` para dirigirse a una región específica de su audiencia, como enviar un mensaje a usuarios situados en Nueva York.

### ¿Qué grado de precisión tienen las geovallas Braze?

Las geocercas Braze utilizan una combinación de todos los proveedores de localización disponibles en un dispositivo para triangular la ubicación del usuario. Entre ellos se encuentran las torres Wi-Fi, GPS y de telefonía móvil.

La precisión típica se sitúa en el intervalo de 20-50 m y la precisión en el mejor de los casos estará en el intervalo de 5-10 m. En las zonas rurales, la precisión puede degradarse significativamente, pudiendo llegar a varios kilómetros. Braze recomienda crear geocercas con radios mayores en las zonas rurales.

Para más información sobre la precisión de las geocercas, consulte la documentación de [Android](https://developer.android.com/develop/sensors-and-location/location/geofencing) e [iOS](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html#//apple_ref/doc/uid/TP40009497-CH9-SW1).

### ¿Cómo afectan las geocercas a la duración de la batería?

Nuestra solución de geovallas utiliza el servicio nativo del sistema de geovallas en iOS y Android y está ajustada para equilibrar de forma inteligente la precisión y la potencia, garantizando la mejor duración de la batería y mejoras en el rendimiento a medida que mejora el servicio subyacente.

### ¿Cuándo están activas las geovallas?

Las geocercas Braze funcionan a cualquier hora del día, incluso cuando la aplicación está cerrada. Se activan en cuanto se definen y se cargan en el panel Braze. Sin embargo, las geovallas no pueden funcionar si el usuario ha desactivado el seguimiento de la ubicación.

Para que las geocercas funcionen, los usuarios deben tener activados los servicios de localización en su dispositivo y deben haber concedido permiso a tu aplicación para acceder a su ubicación. Si un usuario ha desactivado el seguimiento de su ubicación, tu aplicación no podrá detectar cuándo entra o sale de una geo-valla.

### ¿Se almacenan los datos de la geovalla en los perfiles de usuario?

No, Braze no almacena datos de geovallas en los perfiles de usuario. Las geovallas son controladas por los servicios de ubicación de Apple y Google, y Braze solo recibe una notificación cuando un usuario desencadena una geovalla. En ese momento, procesamos cualquier campaña desencadenante asociada.

### ¿Puedo configurar una geovalla dentro de una geovalla?

Como práctica recomendada, evite configurar geocercas una dentro de otra, ya que esto puede causar problemas con la activación de las notificaciones.

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://developer.apple.com/library/content/documentation/UserExperience/Conceptual/LocationAwarenessPG/RegionMonitoring/RegionMonitoring.html
