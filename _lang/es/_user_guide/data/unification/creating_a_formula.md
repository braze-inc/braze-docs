---
nav_title: Crear una fórmula
article_title: Crear una fórmula
page_order: 1.2
page_type: reference
description: "Este artículo de referencia trata de la creación y gestión de fórmulas, que te ayudan a comprender fácilmente las relaciones complejas que existen en tus datos."
tool: Reports

---
# Crear una fórmula

> Al ver los análisis en Braze, puedes combinar varios puntos de datos para obtener información valiosa sobre tus datos de usuario. Se denominan fórmulas. Utiliza fórmulas para normalizar tus datos de series temporales en función de tu número total de usuarios activos mensuales (MAU) y usuarios activos diarios (DAU). 

Las fórmulas te ayudan a comprender las relaciones complejas que existen en tus datos. Por ejemplo, puedes comparar cuántos eventos personalizados completaron los usuarios activos diarios que cumplen los requisitos de un segmento concreto frente a la población general (o frente a otro segmento).

## Casos de uso

Las fórmulas, especialmente cuando se combinan con eventos personalizados, pueden ayudarte a comprender los comportamientos de los usuarios dentro de tu aplicación. Las fórmulas también pueden aportar información más profunda sobre los patrones de compra de los segmentos, incluso si tu empresa utiliza medios contratados junto con Braze, como Google Ads o TV. 

Los siguientes son algunos ejemplos de los tipos de patrones de comportamiento que pueden detectarse utilizando fórmulas:

- **Aplicaciones de transporte compartido:** Si tienes un evento personalizado para cuando el usuario cancela un viaje, puedes configurar una función para Viajes cancelados / DAU para averiguar si determinados segmentos de usuarios tienden a cancelar más viajes que otros.
- **Aplicaciones de comercio electrónico:** Configurando una función para compras de un determinado ID de producto / MAU, puedes comparar la popularidad de un producto promocionado recientemente entre segmentos, aunque no se hayan podido seguir todas las promociones con Braze.
- **Aplicaciones multimedia que utilizan anuncios:** Si la experiencia de los usuarios se ve interrumpida por anuncios entre clips de vídeo o audio, registrar las salidas de mitad de anuncio como un evento personalizado y calcular la proporción de salidas de mitad de anuncio / DAU puede ayudar a encontrar los mejores segmentos a los que dirigirse con una campaña de suscripción premium sin anuncios.

## Crear fórmulas

Puedes acceder a las fórmulas en los paneles de estadísticas de las páginas [Inicio]({{site.baseurl}}/user_guide/analytics/dashboard/home_dashboard/), [Informe de ingresos]({{site.baseurl}}/user_guide/data/export_braze_data/exporting_revenue_data/) e [Informe de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) del panel de control. Para ver este panel, ve al gráfico **Rendimiento en el tiempo**, cambia el desplegable **Estadísticas para** a **Fórmulas de K**PI y, a continuación, selecciona al menos una fórmula de KPI para rellenar el gráfico.

\![Ver estadísticas de fórmulas de KPI en el panel de Braze]({% image_buster /assets/img_archive/kpi_forms.png %})

Para crear una nueva fórmula:

1. Ve al panel apropiado**(Inicio**, **Informe de ingresos** o **Informe de eventos personalizados**).
2. Selecciona **Gestionar fórmulas de KPI**.
3. Introduce un nombre para tu fórmula.
4. Selecciona los numeradores y denominadores correspondientes.
5. Selecciona **Guardar**.

## Numeradores y denominadores disponibles

<style>
  div.small_table + table {
    max-width: 50%;
  }
  div.large_table + table {
    max-width: 75%;
  }
table th:nth-child(1),
table th:nth-child(2),
table th:nth-child(3),
table td:nth-child(1),
table td:nth-child(2),
table td:nth-child(3) {
    width:25%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

### Panel de resumen

| Numeradores | Denominadores |
| --- | --- |
| DAU | MAU |
| Sesiones | DAU |
| | Tamaño del segmento |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Panel de ingresos

| Numeradores | Denominadores |
| --- | --- |
| Compras (todas) | DAU |
| Selecciona compras (como una tarjeta regalo o un ID de producto) | MAU |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Panel de eventos personalizado

| Numeradores | Denominadores |
| --- | --- |
| Recuento de eventos personalizado | MAU |
|  | DAU |
|  | Tamaño del segmento (sólo se pueden utilizar los segmentos que tengan habilitado el [seguimiento de análisis]({{site.baseurl}}/viewing_and_understanding_segment_data/) ) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

