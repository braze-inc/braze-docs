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

# Crear un experimento de bandera de características

> Los experimentos con las feature flags te permiten hacer pruebas A/B de los cambios en tus aplicaciones para optimizar las tasas de conversión. Los especialistas en marketing pueden utilizar las banderas de características para determinar si una nueva característica influye positiva o negativamente en las tasas de conversión, o qué conjunto de propiedades de la bandera de características es el más óptimo.

## Requisitos previos

Antes de que puedas hacer un seguimiento de los datos de usuario en el experimento, tu aplicación necesita registrar cuándo un usuario interactúa con una bandera de característica. Esto se denomina impresión de la feature flag. Asegúrate de registrar una impresión del indicador de característica siempre que un usuario vea o pudiera haber visto la característica que estás probando, aunque esté en el grupo de control.

Para saber más sobre el registro de impresiones de feature flags, consulta [Crear feature flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create/#impressions).

```javascript
const featureFlag = braze.getFeatureFlag("my-new-feature");
braze.logFeatureFlagImpression("my-new-feature");
if (featureFlag?.enabled) {
   return <NewFeature />
} else {
   return <ExistingFeature />
}

```

## Paso 1: Crea un experimento

1. Ve a **Mensajería** > **Campañas** y haz clic en **\+ Crear campaña**.
2. Selecciona el **Experimento de la Bandera de Características**.
3. Pon a tu campaña un nombre claro y significativo.

## Paso 2: Añadir variantes del experimento

A continuación, crea variaciones. Para cada variante, elige la bandera de característica que quieras activar o desactivar y revisa las propiedades asignadas.

Para probar el impacto de tu característica, utiliza variantes para dividir el tráfico en dos o más grupos. Nombra un grupo "Mi grupo de control" y desactiva sus banderas de características.

### Sobrescribir propiedades

Aunque hayas especificado propiedades predeterminadas al configurar originalmente tu bandera de características, puedes elegir sobrescribir esos valores para los usuarios que reciban una variante de campaña específica.

![]({% image_buster /assets/img/feature_flags/feature_flag_experiment_override.png %}){: style="max-width:80%"}

Para editar, añadir o eliminar propiedades predeterminadas adicionales, edita la propia bandera de característica desde **Mensajería** > **Banderas de característica**.

Cuando una variante está desactivada, el SDK devolverá un objeto de propiedades vacío para la bandera de característica dada. 

## Paso 3: Elige los usuarios a los que dirigirte

A continuación, tienes que [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. La pertenencia a un segmento se calcula cuando se actualizan las banderas de características para un usuario determinado.

{% alert note %}
Los cambios están disponibles cuando tu aplicación actualiza las banderas de características, o cuando se inicia una nueva sesión.
{% endalert %}

## Paso 4: Distribuir variantes

Elige la distribución porcentual para tu experimento. Como práctica recomendada, no debes cambiar la distribución una vez iniciado tu experimento.

## Paso 5: Asignar conversiones

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), después de recibir una campaña. Especifica una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

## Paso 6: Revisión y lanzamiento

Cuando hayas terminado de construir lo último de tu experimento, revisa sus detalles y haz clic en **Iniciar experimento**.



