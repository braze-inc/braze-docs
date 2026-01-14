---
nav_title: Crear una predicción de abandono de clientes
article_title: Crear una predicción de abandono de clientes
description: "Este artículo explica cómo crear una predicción de abandono en el panel de Braze."
page_order: 1.1

---

# Crear una predicción de abandono de clientes

> Aprende a crear una predicción de abandono en el panel de Braze.

## Paso 1: Crear una nueva predicción

En Braze, ve a **Análisis** > Predictive Churn.

Una predicción es una instancia de un modelo de aprendizaje automático entrenado y todos los parámetros y datos que utiliza. En esta página, verás una lista de las predicciones activas actuales junto con información básica sobre ellas. Aquí puedes renombrar, archivar y crear nuevas predicciones. Las predicciones archivadas están inactivas y no actualizan las puntuaciones de los usuarios. 

Para crear una nueva predicción, elige **Crear predicción** y selecciona una nueva **Predicción de abandono**.

{% alert note %}
Hay un límite de cinco predicciones de abandono activas simultáneamente. Antes de comprar Predictive Churn, el límite es una predicción de abandono activa en vista previa. Una predicción de abandono vista previa no actualizará regularmente las puntuaciones ni te permitirá dirigirte a usuarios en función de los resultados de la predicción. Ponte en contacto con tu director de cuentas para obtener más información.
{% endalert %}

En la página **Conceptos básicos**, asigna a tu nueva predicción un nombre único. También puedes proporcionar una descripción opcional para tomar cualquier nota sobre esta predicción en particular.

Selecciona **Avanzar** para pasar al siguiente paso. Opcionalmente, puedes seleccionar **Construir ahora** para utilizar toda la configuración predeterminada y pasar al último paso de la creación. Tendrás la oportunidad de revisar la configuración antes de iniciar el proceso de construcción. Puedes volver a cualquier paso más tarde seleccionándolo en el rastreador de progreso.

## Paso 2: Define abandono

En el panel **Definición del abandono**, utiliza los filtros proporcionados para especificar cómo definir el abandono de usuarios para tu empresa. En otras palabras, ¿qué tiene que hacer un usuario en qué plazo de tiempo para que lo consideres abandonado?

Recuerda que no tienes que explicar qué comportamientos pueden preceder al abandono, sólo qué hace que un usuario sea un usuario abandonado. Piensa en esto en términos de algo que un usuario hace una vez (`do`) o deja de hacer (`do not`) y que constituye un abandono. Por ejemplo, puedes considerar abandonados a los usuarios que no han abierto tu aplicación en 7 días. Podrías considerar la desinstalación, o eventos personalizados como darse de baja, desactivar una cuenta u otros que provoquen que un usuario se dé de baja. 

#### Ventana de abandono

La ventana de abandono es el periodo en el que la actividad de un usuario cumple los criterios de abandono. Puedes configurarlo hasta 60 días, dependiendo de los datos disponibles. Esta ventana se utiliza para extraer datos históricos para entrenar tu predicción. Una vez construida la predicción, verás si había suficientes datos para obtener resultados precisos.

Después de que se construya la predicción y los usuarios reciban las puntuaciones, la _Puntuación de riesgo de abandono_ muestra la probabilidad de que un usuario abandone dentro del plazo que hayas establecido en la ventana de abandono. 

He aquí un ejemplo de definición simple basada en las sesiones de lapso de los últimos 7 días.

Definición de abandono: un usuario se considera abandonado si no inicia una sesión en 7 días.]({% image_buster /assets/img/churn/churn1.png %})

Para este caso, seleccionamos `do not` y `start a session`. Puedes combinar otros filtros con `AND` y `OR` según te convenga para crear la definición que necesites. ¿Te interesan algunas posibles definiciones de abandono a tener en cuenta? Puedes encontrar algo de inspiración en la siguiente sección sobre [definiciones de muestras de abandono](#sample-definitions).

{% alert note %}
Para `do`, suponemos que los usuarios activos no realizaron la acción que especifiques para esta fila antes de convertirse en abandonados. Realizar la acción provoca su abandono. <br><br>Para `do not`, consideramos usuarios activos a los que hicieron esa acción en los días anteriores y luego dejaron de hacerla. <br><br>**Ejemplo:** Si el abandono se define como "no ha comprado en los últimos 60 días", consideramos usuarios activos a los que sí compraron en los últimos 60 días. Como resultado, cualquiera que no haya realizado una compra en los últimos 60 días no se considera usuario activo. Esto significa que una audiencia de abandono creada a partir de esta definición de abandono sólo incluiría a los usuarios que han comprado en los últimos 60 días. Esto puede hacer que la audiencia predictiva de abandono resultante parezca significativamente menor que la población original: la mayoría de los usuarios de un espacio de trabajo podrían cumplir ya la definición de abandono y, por tanto, no estar activos en la predicción de abandono.
{% endalert %}

Debajo de la definición, verás estimaciones de cuántos usuarios (en el pasado que abandonaron y que no abandonaron según tu definición) están disponibles. También verás los valores mínimos requeridos. Braze debe tener este número mínimo de usuarios disponibles en los datos históricos para que la predicción tenga suficientes datos de los que aprender.

## Paso 3: Filtra tu audiencia de predicción

Tu audiencia de predicción es el grupo de usuarios para el que quieres predecir el riesgo de abandono. La audiencia de predicción define el grupo de usuarios en los que se fija el modelo de aprendizaje automático para aprender del pasado. Por defecto, está predeterminada en **Todos los usuarios**, lo que significa que esta predicción creará puntuaciones de riesgo de abandono para todos tus usuarios activos (consulta la nota anterior para saber quién se considera activo para un modelo de abandono).

Dependiendo de tu caso de uso, puede que quieras utilizar filtros para especificar los usuarios que quieres evaluar para el modelo. Para ello, selecciona **Definir mi propia audiencia de predicción** y elige tus filtros de audiencia. Por ejemplo, si eres una aplicación de transporte compartido con conductores y usuarios en tu base de usuarios, y estás creando un modelo de abandono para usuarios, querrás filtrar tu audiencia de predicción a sólo usuarios. Ten en cuenta que muchos casos de uso no requieren que selecciones una audiencia de predicción específica. Por ejemplo, si tu caso de uso es dirigirte a los usuarios de la región de la UE con más probabilidades de abandono, puedes ejecutar tu modelo en todos los usuarios y luego simplemente incluir un filtro para la región de la UE en el segmento de la campaña.

Braze te mostrará el tamaño estimado de tu audiencia de predicción. Si especificas la audiencia deseada y no alcanzas el mínimo necesario para ejecutar el modelo, prueba a especificar un filtro más amplio o utiliza la opción **Todos los usuarios**. Nota que el tamaño de tu grupo "todos los usuarios" no es estático y varía de un modelo a otro, ya que tiene en cuenta tu definición de abandono. Por ejemplo, digamos que la definición de abandono es **no** realizar una compra en 30 días; en este caso, Braze ejecuta el modelo en usuarios que **han** comprado en los últimos 30 días (y predice la probabilidad de que **no** compren en los próximos 30 días), por lo que esos son los usuarios reflejados en la métrica "todos los usuarios".

{% alert note %}
La audiencia de la predicción no puede superar los 100 millones de usuarios.
{% endalert %}

Cuando la ventana de predicción es de 14 días o menos, la ventana de tiempo para los filtros que empiezan por "Última...", como "Última aplicación utilizada" y "Última compra realizada **", no puede superar la ventana de abandono especificada** en la definición de abandono. Por ejemplo, si tu definición de abandono tiene una ventana de 14 días, la ventana de tiempo de los filtros "Último..." no puede superar los 14 días.

#### Modo de filtro completo

Para construir inmediatamente una nueva predicción, sólo se admite un subconjunto de filtros de segmentación Braze. El modo de filtro completo te permite utilizar todos los filtros Braze, pero necesitará una ventana de abandono para construir la predicción. Por ejemplo, si la ventana de abandono se establece en 15 días, se tardará 15 días en recopilar los datos de usuario y construir la predicción cuando se utilicen filtros sólo admitidos en el modo de filtro completo. Además, algunas estimaciones sobre el tamaño de la audiencia no estarán disponibles en el modo filtrar todo.

Para ver una lista de muestra de definiciones de audiencia de predicción, consulta nuestras definiciones de muestra en la siguiente sección de [Definiciones de abandono de muestra](#sample-definitions).

\![]({% image_buster /assets/img/churn/churn5.png %})

Al igual que en la página anterior, el panel inferior te mostrará el número estimado de usuarios históricos resultantes de tu definición de abandono y de audiencia de predicción. Estas estimaciones deben cumplir los requisitos mínimos indicados para crear una predicción.

## Paso 4: Elige la frecuencia de actualización de la predicción de abandono

El modelo de aprendizaje automático generará puntuaciones de probabilidad de sucesos para los usuarios, y esas puntuaciones se actualizarán en función de la programación que selecciones aquí. Podrás dirigirte a los usuarios en función de su puntuación de probabilidad de suceso. 

Selecciona la **frecuencia máxima de actualizaciones** que te resulte útil. Por ejemplo, si vas a enviar una promoción semanal para evitar el abandono de usuarios, establece la frecuencia de actualización en **Semanal** el día y la hora que elijas. 

\![Programa de actualización de predicciones establecido en diario a las 17:00 h.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
La vista previa y la predicción de demostración nunca actualizarán el riesgo de abandono de los usuarios. Además, las actualizaciones diarias de las predicciones requieren una compra adicional más allá de las actualizaciones semanales o mensuales con Predictive Churn. Para adquirir esta funcionalidad, ponte en contacto con tu director de cuentas.
{% endalert %}

## Paso 5: Construir predicción

Comprueba que los datos que has proporcionado son correctos y elige **Crear predicción**. También puedes guardar tus cambios en forma de borrador seleccionando **Guardar como borrador** para volver a esta página y construir el modelo más tarde. Después de seleccionar **Construir predicción**, comenzará el proceso que genera el modelo. Esto puede tardar entre 30 minutos y unas horas, dependiendo del volumen de datos. Para esta predicción, verás una página en la que se explica que el entrenamiento está en curso mientras dure el proceso de construcción del modelo. El modelo Braze tiene en cuenta los eventos personalizados, los eventos de compra, los eventos de interacción de campaña y los datos de sesión.

Una vez hecho esto, la página cambiará automáticamente a la vista Análisis, y también recibirás un correo electrónico informándote de que la predicción y los resultados están listos. En caso de error, la página volverá al modo Edición con una explicación de lo que ha ido mal.

La predicción se reconstruirá ("reentrenará") de nuevo cada **dos semanas automáticamente** para mantenerla actualizada con los datos disponibles más recientes. Ten en cuenta que se trata de un proceso distinto al de la obtención de _las puntuaciones de riesgo de abandono de_ los usuarios, que es el resultado de la predicción. Esto último viene determinado por la frecuencia de actualización que elegiste en el Paso 4.

## Muestra de definiciones de audiencia de abandono y predicción {#sample-definitions}

**Ejemplos de definiciones de abandono**<br>
- "En un plazo de 7 días, haz el evento personalizado 'Cancelación de suscripción'"<br>
- "En un plazo de 30 días, haz el evento personalizado 'Prueba caducada'"<br>
- "En 1 día desinstala". <br>
- "En un plazo de 14 días no Realices una Compra". <br>

Para las definiciones de abandono que hemos esbozado, puede haber algunas definiciones de audiencia de predicción correspondientes:<br>
- **Comenzó la suscripción hace más de 2 semanas O Comenzó la suscripción hace menos de dos semanas**<br>En este caso, es posible que quieras crear 2 predicciones y luego enviar mensajes a los nuevos suscriptores de forma diferente a los suscriptores a largo plazo. También podrías definirlo como "Primera compra realizada hace más de 30 días".<br>
- **Desinstaladores**<br>Podrías centrarte en clientes que hayan comprado algo en el pasado reciente o que hayan utilizado la aplicación muy recientemente.<br>
- **Los que corren el riesgo de no comprar como definición de abandono**<br>Quizá quieras centrarte en los clientes que han estado navegando, buscando o interactuando con tu aplicación más recientemente. Tal vez una intervención adecuada con descuentos evite que este grupo más comprometido abandone.

## Predicciones archivadas

Las predicciones archivadas dejarán de actualizar las puntuaciones de los usuarios. Cualquier predicción archivada que no esté archivada seguirá actualizando las puntuaciones de los usuarios en su horario predeterminado. Las predicciones archivadas nunca se borran y permanecen en la lista.


