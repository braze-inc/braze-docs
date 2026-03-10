---
nav_title: Crear una predicción de abandono
article_title: Crear una predicción de abandono
description: "Este artículo explica cómo crear una predicción de abandono en el dashboard de Braze."
page_order: 1.1

---

# Crear una predicción de abandono

> Aprenda a crear una predicción de abandono en el dashboard de Braze.

## Paso 1: Crear una nueva predicción

En Braze, vaya a **Análisis** > **Predictive Churn**.

Una predicción es una instancia de un modelo de aprendizaje automático entrenado y todos los parámetros y datos que utiliza. En esta página, verá una lista de las predicciones activas actuales junto con información básica sobre ellas. Aquí puede renombrar, archivar y crear nuevas predicciones. Las predicciones archivadas están inactivas y no actualizan las puntuaciones de los usuarios.

Para crear una nueva predicción, seleccione **Crear predicción** y elija una nueva **Predicción de abandono**.

{% alert note %}
Existe un límite de cinco predicciones de abandono activas de forma simultánea. Antes de adquirir Predictive Churn, el límite es una predicción de abandono en vista previa activa. Una predicción de abandono en vista previa no actualizará las puntuaciones de forma regular ni le permitirá segmentar usuarios basándose en los resultados de la predicción. Ponte en contacto con tu director de cuentas para obtener más detalles.
{% endalert %}

En la página **Básicos**, asigne un nombre único a su nueva predicción. También puede proporcionar una descripción opcional para tomar notas sobre esta predicción en particular.

Seleccione **Avanzar** para pasar al siguiente paso. Opcionalmente, puede seleccionar **Construir ahora** para usar toda la configuración predeterminada y saltar al último paso de la creación. Tendrá la oportunidad de revisar la configuración antes de iniciar el proceso de construcción. Puede volver a cualquier paso más tarde seleccionándolo en el indicador de progreso.

## Paso 2: Definir el abandono

En el panel **Definición de abandono**, utilice los filtros proporcionados para especificar cómo define el abandono de usuarios para su empresa. En otras palabras, ¿qué tiene que hacer un usuario en qué período de tiempo para que lo considere un usuario perdido?

Recuerde que no necesita explicar qué comportamientos podrían preceder al abandono, solo qué hace que un usuario sea un usuario perdido. Piense en esto en términos de algo que un usuario hace una vez (`do`) o deja de hacer (`do not`) que constituye abandono. Por ejemplo, podría considerar que los usuarios que no han abierto su aplicación en 7 días han abandonado. Podría considerar que la desinstalación, o eventos personalizados como cancelar la suscripción, desactivar una cuenta u otros, hacen que un usuario se convierta en un usuario perdido.

#### Ventana de abandono

La ventana de abandono es el período en el que la actividad de un usuario cumple los criterios de abandono. Puede configurarla hasta 60 días, dependiendo de los datos disponibles. Esta ventana se utiliza para extraer datos históricos con los que entrenar su predicción. Una vez construida la predicción, verá si hubo suficientes datos para obtener resultados precisos.

Después de que la predicción se construya y los usuarios reciban puntuaciones, la _Puntuación de riesgo de abandono_ muestra la probabilidad de que un usuario abandone dentro del período de tiempo que estableció en la ventana de abandono.

A continuación se muestra un ejemplo de una definición simple basada en sesiones inactivas en los últimos 7 días.

![Definición de abandono donde un usuario se considera perdido si no inicia una sesión en 7 días]({% image_buster /assets/img/churn/churn1.png %})

Para este caso, seleccionamos `do not` y `start a session`. Puede combinar otros filtros con `AND` y `OR` según lo considere necesario para crear la definición que necesita. ¿Le interesan algunas posibles definiciones de abandono a considerar? Puede encontrar inspiración en la siguiente sección sobre [Definiciones de abandono de ejemplo](#sample-definitions).

{% alert note %}
Para `do`, asumimos que los usuarios activos no realizaron la acción que especifica para esta fila antes de convertirse en usuarios perdidos. Realizar la acción hace que se conviertan en usuarios perdidos. <br><br>Para `do not`, consideramos que los usuarios activos son aquellos que realizaron esa acción en los días anteriores y luego dejaron de hacerlo. <br><br>**Ejemplo:** Si el abandono se define como "no ha realizado una compra en los últimos 60 días", consideramos usuarios activos a aquellos que sí realizaron una compra en los últimos 60 días. Como resultado, cualquier persona que no haya realizado una compra en los últimos 60 días no se considera un usuario activo. Esto significa que una audiencia de abandono creada a partir de esta definición de abandono solo incluiría usuarios que han comprado en los últimos 60 días. Esto puede hacer que la audiencia resultante de Predictive Churn parezca significativamente más pequeña que la población original: la mayoría de los usuarios en un espacio de trabajo podrían ya cumplir la definición de abandono y, por lo tanto, no estar activos en la predicción de abandono.
{% endalert %}

Debajo de la definición, verá estimaciones de cuántos usuarios (en el pasado que abandonaron y que no abandonaron según su definición) están disponibles. También verá los valores mínimos requeridos. Braze debe tener este recuento mínimo de usuarios disponibles en los datos históricos para que la predicción tenga suficientes datos de los que aprender.

## Paso 3: Filtrar su audiencia de predicción

Su audiencia de predicción es el grupo de usuarios para los que desea predecir el riesgo de abandono. La audiencia de predicción define el grupo de usuarios que el modelo de aprendizaje automático analiza para aprender del pasado. De forma predeterminada, está configurada como **Todos los usuarios**, lo que significa que esta predicción creará puntuaciones de riesgo de abandono para todos sus usuarios activos (consulte la nota anterior sobre quién se considera activo para un modelo de abandono).

Dependiendo de su caso de uso, es posible que desee utilizar filtros para especificar los usuarios que desea evaluar para el modelo. Para hacerlo, seleccione **Definir mi propia audiencia de predicción** y elija sus filtros de audiencia. Por ejemplo, si tiene una aplicación de transporte compartido con conductores y pasajeros en su base de usuarios, y está construyendo un modelo de abandono para pasajeros, querrá filtrar su audiencia de predicción solo a pasajeros. Tenga en cuenta que muchos casos de uso no requieren que seleccione una audiencia de predicción específica. Por ejemplo, si su caso de uso es segmentar a los usuarios de la región de la UE que tienen más probabilidades de abandonar, puede ejecutar su modelo en todos los usuarios y luego simplemente incluir un filtro para la región de la UE en el segmento de la campaña.

Braze le mostrará el tamaño estimado de su audiencia de predicción. Si especifica la audiencia deseada y no cumple con el mínimo requerido para ejecutar el modelo, intente especificar un filtro más amplio o use la opción **Todos los usuarios**. Tenga en cuenta que el tamaño de su grupo de "todos los usuarios" no es estático y varía de modelo a modelo, ya que tiene en cuenta su definición de abandono. Por ejemplo, supongamos que la definición de abandono es **no** realizar una compra en 30 días; en este caso, Braze ejecuta el modelo en usuarios que **sí** han comprado en los últimos 30 días (y predice la probabilidad de que **no** compren en los próximos 30 días), por lo que esos son los usuarios reflejados en la métrica de "todos los usuarios".

{% alert note %}
La audiencia de predicción no puede superar los 100 millones de usuarios.
{% endalert %}

Cuando la ventana de predicción es de 14 días o menos, la ventana de tiempo para los filtros que comienzan con "Último...", como "Última vez que usó la aplicación" y "Última compra realizada", **no puede superar la ventana de abandono especificada** en la definición de abandono. Por ejemplo, si su definición de abandono tiene una ventana de 14 días, la ventana de tiempo para los filtros "Último..." no puede superar los 14 días.

La ventana de abandono se evalúa mirando hacia atrás el número de días desde el día en que el modelo se ejecutó por última vez, por lo que si la ventana de abandono es de 15 días y el modelo se ejecutó por última vez el 1 de diciembre, el modelo analiza del 16 al 30 de noviembre para comprender la actividad de los usuarios en relación con la elegibilidad de la audiencia y el entrenamiento.

#### Modo de filtro completo

Para construir una nueva predicción de forma inmediata, solo se admite un subconjunto de filtros de segmentación de Braze. El modo de filtro completo le permite usar todos los filtros de Braze, pero requerirá una ventana de abandono para construir la predicción. Por ejemplo, si la ventana de abandono se establece en 15 días, tomará 15 días recopilar los datos de usuario y construir la predicción cuando se usen filtros solo compatibles con el modo de filtro completo. Además, algunas estimaciones sobre los tamaños de audiencia no estarán disponibles en el modo de filtro completo.

Para una lista de ejemplo de definiciones de audiencia de predicción, consulte nuestras definiciones de ejemplo en la siguiente sección sobre [Definiciones de abandono de ejemplo](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Al igual que en la página anterior, el panel inferior le mostrará el número estimado de usuarios históricos que resultan de su definición de abandono y definición de audiencia de predicción. Estas estimaciones deben cumplir con los requisitos mínimos mostrados para poder crear una predicción.

## Paso 4: Elegir la frecuencia de actualización para la predicción de abandono

El modelo de aprendizaje automático generará puntuaciones de probabilidad de eventos para los usuarios, y esas puntuaciones se actualizarán según la planificación que seleccione aquí. Podrá segmentar usuarios basándose en su puntuación de probabilidad de eventos.

Seleccione la **frecuencia máxima de actualizaciones** que le resulte útil. Por ejemplo, si va a enviar una promoción semanal para evitar que los usuarios abandonen, configure la frecuencia de actualización en **Semanal** en el día y la hora de su elección.

![Planificación de actualización de predicción configurada a diario a las 5 pm.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
Las predicciones de vista previa y demostración nunca actualizarán el riesgo de abandono de los usuarios. Además, las actualizaciones diarias para predicciones requieren una compra adicional más allá de las actualizaciones semanales o mensuales con Predictive Churn. Para adquirir esta funcionalidad, ponte en contacto con tu director de cuentas.
{% endalert %}

## Paso 5: Construir la predicción

Verifique que los detalles que ha proporcionado sean correctos y seleccione **Construir predicción**. También puede guardar sus cambios en forma de borrador seleccionando **Guardar como borrador** para volver a esta página y construir el modelo más tarde. Después de seleccionar **Construir predicción**, comenzará el proceso que genera el modelo. Esto puede tardar entre 30 minutos y unas pocas horas, dependiendo del volumen de datos. Para esta predicción, verá una página que explica que el entrenamiento está en progreso durante la duración del proceso de construcción del modelo. El modelo de Braze tiene en cuenta eventos personalizados, eventos de compra, eventos de interacción con campañas y datos de sesión.

Una vez finalizado, la página cambiará automáticamente a la vista de análisis, y también recibirá un correo electrónico informándole de que la predicción y los resultados están listos. En caso de error, la página volverá al modo de edición con una explicación de lo que salió mal.

La predicción se reconstruirá ("reentrenará") automáticamente cada **dos semanas** para mantenerla actualizada con los datos más recientes disponibles. Tenga en cuenta que este es un proceso separado de cuando se producen las _Puntuaciones de riesgo de abandono_ de los usuarios, que son el resultado de la predicción. Esto último está determinado por la frecuencia de actualización que eligió en el Paso 4.

## Definiciones de ejemplo de abandono y audiencia de predicción {#sample-definitions}

**Definiciones de abandono de ejemplo**<br>
- "En 7 días, realizar evento personalizado 'Cancelación de suscripción'"<br>
- "En 30 días, realizar evento personalizado 'Prueba expirada'"<br>
- "En 1 día realizar desinstalación."<br>
- "En 14 días no realizar una compra."<br>

Para las definiciones de abandono que describimos, podría haber algunas definiciones de audiencia de predicción correspondientes:<br>
- **Inició la suscripción hace más de 2 semanas O Inició la suscripción hace menos de dos semanas**<br>Es posible que desee crear 2 predicciones en este caso y luego enviar mensajes diferentes a los nuevos suscriptores que a los suscriptores de más largo plazo. También podría definir esto como "Primera compra realizada hace más de 30 días".<br>
- **Desinstaladores**<br>Podría centrarse en los clientes que han comprado algo recientemente o que han usado la aplicación muy recientemente.<br>
- **Aquellos en riesgo de no comprar como definición de abandono**<br>Es posible que desee centrarse en los clientes que han estado navegando, buscando o interactuando con su aplicación más recientemente. Quizás la intervención con el descuento adecuado evitará que este grupo más comprometido abandone.

## Predicciones archivadas

Las predicciones archivadas dejarán de actualizar las puntuaciones de los usuarios. Cualquier predicción archivada que se desarchive continuará actualizando las puntuaciones de los usuarios según su planificación predeterminada. Las predicciones archivadas nunca se eliminan y permanecen en la lista.