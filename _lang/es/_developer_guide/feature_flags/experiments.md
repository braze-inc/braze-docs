---
nav_title: Experimentos de conmutadores de características
article_title: Experimentos de conmutadores de características
page_order: 40
description: "Los experimentos con las feature flags te permiten hacer pruebas A/B de los cambios en tus aplicaciones para optimizar las tasas de conversión."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Experimentos con la bandera de características

> Los experimentos con las feature flags te permiten hacer pruebas A/B de los cambios en tus aplicaciones para optimizar las tasas de conversión. Los especialistas en marketing pueden utilizar las banderas de características para determinar si una nueva característica influye positiva o negativamente en las tasas de conversión, o qué conjunto de propiedades de la bandera de características es el más óptimo.

## Requisitos previos

Antes de que puedas hacer un seguimiento de los datos de usuario en el experimento, tu aplicación necesita registrar cuándo un usuario interactúa con una bandera de característica. Esto se denomina impresión de la feature flag. Asegúrate de registrar una impresión del indicador de característica siempre que un usuario vea o pudiera haber visto la característica que estás probando, aunque esté en el grupo de control.

Para saber más sobre el registro de impresiones de feature flags, consulta [Crear feature flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions).

{% tabs %}
{% tab JavaScript %}

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}
```

{% endtab %}
{% tab Java %}

```java
FeatureFlag featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag != null && featureFlag.getEnabled()) {
  return new NewFeature();
} else {
  return new ExistingFeature();
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("my-new-feature")
braze.logFeatureFlagImpression("my-new-feature")
if (featureFlag?.enabled == true) {
  return NewFeature()
} else {
  return ExistingFeature()
}
```

{% endtab %}
{% endtabs %}

## Crear un experimento de bandera de características

### Paso 1: Crea un experimento

1. Ve a **Mensajería** > **Campañas** y, a continuación, selecciona **\+ Crear campaña**.
2. Selecciona el **Experimento de la Bandera de Características**.
3. Da a tu campaña un nombre claro y significativo.

### Paso 2: Añadir variantes del experimento

A continuación, crea variaciones. Para cada variante, elige la bandera de característica que quieras activar o desactivar y, a continuación, revisa sus propiedades asignadas.

Para probar el impacto de tu característica, utiliza variantes para dividir el tráfico en dos o más grupos. Nombra un grupo "Mi grupo de control" y desactiva sus banderas de características.

### Paso 3: Sobrescribir propiedades (opcional)

Puedes elegir sobrescribir las propiedades predeterminadas que configuraste inicialmente para los usuarios que reciben una variante de campaña específica.

Para editar, añadir o eliminar propiedades predeterminadas adicionales, edita la propia bandera de característica desde **Mensajería** > **Banderas de característica**. Cuando una variante está desactivada, el SDK devolverá un objeto de propiedades vacío para la bandera de característica dada.

![La sección "Variantes del experimento" con la clave variable "enlace" sobrescrita con "/ventas".]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

### Paso 4: Elige los usuarios a los que dirigirte

Utiliza uno de tus segmentos o filtros para elegir a tus [usuarios objetivo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/). Por ejemplo, puedes utilizar el filtro **Variante de indicador de característica recibida** para reorientar a los usuarios que ya han recibido una prueba A/B.

![La página "Objetivo" en un experimento de bandera de característica con "Variante de bandera de característica recibida" resaltada en la barra de búsqueda del grupo de filtrado.]({% image_buster /assets/img/feature_flags/variant-filter-dropdown.png %}){: style="max-width:70%"}

{% alert note %}
La pertenencia a un segmento se calcula cuando se actualizan las banderas de características para un usuario determinado. Los cambios están disponibles cuando tu aplicación actualiza las banderas de características, o cuando se inicia una nueva sesión.
{% endalert %}

### Paso 5: Distribuir variantes

Elige la distribución porcentual para tu experimento. Como práctica recomendada, no debes cambiar la distribución una vez iniciado tu experimento.

### Paso 6: Asignar conversiones

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), después de recibir una campaña. Especifica una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

### Paso 7: Revisión y lanzamiento

Cuando hayas terminado de construir lo último de tu experimento, revisa sus detalles y, a continuación, selecciona **Iniciar experimento**.

## Revisión de los resultados

Una vez finalizado tu experimento con la bandera de características, puedes revisar los datos de impresión de tu experimento. Ve a **Mensajería** > **Campañas** y selecciona la campaña con tu experimento de la bandera de características.

### Análisis de campaña

**Los análisis de campaña** ofrecen un resumen de alto nivel del rendimiento de tu experimento, como por ejemplo:

- El número total de impresiones
- El número de impresiones únicas
- La tasa de conversión primaria
- Los ingresos totales generados por el mensaje
- La audiencia estimada

También puedes ver la configuración del experimento para la entrega, la audiencia y la conversión.

### Bandera de características rendimiento del experimento

**Banderas de características Experimentos El rendimiento** muestra el rendimiento de tu mensaje en varias dimensiones. Las métricas específicas que veas variarán en función del canal de mensajería elegido y de si estás realizando una prueba multivariante. Para ver los valores de las banderas de características asociadas a cada variante, selecciona **Vista previa**.
