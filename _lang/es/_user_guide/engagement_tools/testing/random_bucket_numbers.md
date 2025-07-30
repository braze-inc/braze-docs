---
nav_title: Números de contenedor aleatorio
article_title: Números de contenedor aleatorio
page_order: 2
page_type: reference
description: "Este artículo cubre el concepto de números de cubo aleatorios, y cómo puede utilizarlos para crear variantes y grupos de control."
page_type: reference
tool:
  - Campaign
  - Canvas

---

# Números de contenedor aleatorio

> Un número de cubo aleatorio es un atributo de usuario que puede utilizarse para crear segmentos de usuarios aleatorios distribuidos uniformemente. Cuando se crea un perfil de usuario en Braze, a ese usuario se le asigna automáticamente un número de cubo aleatorio entre 0 y 9999 (ambos inclusive). Puedes utilizar estos segmentos para probar la eficacia de varias campañas o Canvases en grupos de usuarios a lo largo del tiempo.

## Resumen

Los números de contenedor aleatorios se utilizan en tu grupo de control global: un grupo de usuarios que no reciben campañas ni Canvases. Braze selecciona aleatoriamente múltiples rangos de números de cubos aleatorios e incluye usuarios de esos cubos seleccionados. 

Si tienes configurado un grupo de control global y quieres utilizar números de contenedor aleatorios para otros casos de uso, consulta [Cosas que debes tener en cuenta]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#things-to-watch-for).

### Cuándo utilizar números de cubo aleatorios

Si quieres realizar pruebas a largo plazo sobre la eficacia de varias campañas o Canvases a lo largo del tiempo, puedes utilizar números de contenedor aleatorios para segmentar a tus usuarios.

### Cuándo utilizar otra cosa

Si quieres segmentar a los usuarios para realizar pruebas dentro de una sola campaña o un solo Canvas, utiliza [las pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) para campañas. En el caso de los lienzos, puede crear diferentes [variantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#adding-a-variant) para las pruebas a nivel de recorrido, o utilizar [rutas de experimentación]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) para las pruebas a nivel de paso.

## Crear segmentos utilizando números de cubo aleatorios

Al [crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/), añade el filtro "N.º de contenedor aleatorio". A continuación, especifica un número o rango de números para incluirlos en tu segmento.

![Un filtro de segmento para números de contenedor aleatorios no superiores a "3000".]({% image_buster /assets/img_archive/random_buckets_filterexample.png %})

Puede utilizar este tipo de segmentos si desea realizar una prueba de tres variantes diferentes e incluir también un grupo de control. Considere el siguiente ejemplo de plan para crear segmentos de igual tamaño para tres variantes y un grupo de control:

- Los números de cubo de 0 a 2499 corresponden al segmento de control
- Los números de cubo 2500 a 4999 corresponden al segmento que recibirá la variante 1
- Los números de cubo 5000 a 7499 corresponden al segmento que recibirá la variante 2
- Los números de cubo 7500 a 9999 corresponden al segmento que recibirá la variante 3

Dependiendo del número de segmentos que desee y de la distribución de los usuarios dentro de cada segmento, su plan puede ser diferente.

Para cada uno de tus segmentos de número de contenedor aleatorio, incluido el grupo de control, activa el [seguimiento de análisis]({{site.baseurl}}/user_guide/analytics/tracking/segment_analytics_tracking/). Al evaluar el éxito de las variantes en relación con el grupo de control, puedes ir a tu página de [eventos personalizados]({{site.baseurl}}/user_guide/data/export_braze_data/export_custom_event_data/) y ver con qué frecuencia cada segmento ha completado determinados eventos personalizados.

### Reentrada aleatoria de la audiencia mediante números de contenedor aleatorios

La reentrada aleatoria de la audiencia puede ser útil para [las pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing) o para dirigirte a grupos de usuarios específicos en tus campañas. Para realizar una reentrada aleatoria de la audiencia con números de contenedor aleatorios, haz lo siguiente:

1. [Crea tu segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment).
2. Define los contenedores aleatorios. En tu campaña o Canvas, utiliza el filtro de contenedor aleatorio para dividir a tu audiencia en diferentes grupos. Por ejemplo, puedes especificar exactamente dos contenedores aleatorios en los que dividir tu audiencia (50% de usuarios por contenedor).
3. En la sección **Audiencias** objetivo de tu campaña o Canvas, especifica la configuración del contenedor aleatorio. Esto permite a Braze asignar automáticamente usuarios a los contenedores adecuados en función de los porcentajes definidos.
4. Configura la lógica que permite a los usuarios volver a entrar en el segmento. Por ejemplo, puedes permitir que los usuarios vuelvan a entrar en el segmento si no han interactuado con una aplicación durante 15 días.
5. Lanza tu campaña y controla el rendimiento de cada contenedor. Puedes analizar métricas como las tasas de interacción y de conversión para determinar la eficacia de la reactivación de la audiencia aleatoria en tu caso de uso.


