---
nav_title: Crear una predicción de suceso
article_title: Crear una predicción de suceso
page_order: 1.1
description: "Este artículo explica cómo crear una predicción de eventos en el panel de Braze."

---

# Crear una predicción de acontecimientos

> Una predicción es una instancia de un modelo de aprendizaje automático entrenado y todos los parámetros y datos que utiliza. Para saber más sobre los Eventos de predicción, consulta el [resumen de Eventos de predicción]({{site.baseurl}}/user_guide/brazeai//predictive_events/).

En Braze, ve a **Análisis** > **Eventos de predicción**.

En esta página, verás una lista de predicciones de acontecimientos activos actuales y alguna información básica sobre ellos. Aquí puedes renombrar, archivar y crear nuevas predicciones. Las predicciones archivadas están inactivas y no actualizan las puntuaciones de los usuarios.

## Paso 1: Crear una nueva predicción

1. Elige **Crear predicción** y selecciona una nueva **Predicción de Evento**.

{% alert note %}
Hay un límite de cinco predicciones activas simultáneamente. Antes de comprar Eventos Predictivos, el límite es una predicción de vista previa activa. Una predicción con vista previa no actualizará regularmente las puntuaciones ni los usuarios objetivo basándose en los resultados de la predicción. Ponte en contacto con tu director de cuentas para obtener más información.
{% endalert %}

{: start="2"}
2\. Dale a tu predicción un nombre único. También puedes proporcionar una descripción para guardar cualquier nota relevante.

![]({% image_buster /assets/img/purchasePrediction/purchases_step1.png %})

{: start="3"}
3\. Haz clic en **Adelante** para pasar al siguiente paso. <br><br>Opcionalmente, puedes hacer clic en **Construir ahora** para utilizar toda la configuración predeterminada y pasar al último paso de la creación. Tendrás la oportunidad de revisar la configuración antes de iniciar el proceso de construcción. Además, puedes volver a cualquier paso más tarde haciendo clic en él en la barra superior.

## Paso 2: Especificar seguimiento de eventos {#event-tracking}

Especifica si los eventos de tus usuarios se almacenan en Braze como [eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) o [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/).

Aquí verás si el método seleccionado proporciona suficientes datos para que Braze cree un modelo de aprendizaje automático. Si no se cumple el requisito, intenta seleccionar el otro método de registro si también lo utiliza tu aplicación. Desgraciadamente, si no es así, Braze es incapaz de crear una predicción con la cantidad de datos disponibles. Si crees que estás viendo incorrectamente este error, ponte en contacto con tu administrador del éxito del cliente.

#### Ventana de eventos

La ventana del evento es el intervalo de tiempo en el que quieres predecir si un usuario realizará el evento. Se puede configurar hasta 60 días. Esta ventana se utiliza para consultar datos históricos para entrenar la predicción. Además, después de crear la predicción y de que los usuarios reciban puntuaciones, la puntuación de probabilidad indica la probabilidad de que un usuario realice el evento en el número de días especificado por la ventana de eventos.

### Paso 3: Filtra tu audiencia de predicción (opcional) {#audience}

Tu audiencia de predicción es el grupo de usuarios cuya puntuación de probabilidad te gustaría predecir. Si lo deseas, puedes realizar una predicción sobre toda tu población de usuarios. Para ello, deja seleccionada la opción predeterminada **Todos los usuarios**.

El modelo suele rendir mejor si filtras a los usuarios que quieres evaluar con algún criterio. Para ello, selecciona **Definir mi propia audiencia de predicción** y elige tus filtros de audiencia. Por ejemplo, es posible que quieras centrarte en los usuarios que han estado utilizando tu aplicación durante al menos 30 días seleccionando el filtro "Primera aplicación utilizada" establecido en 30 días.

La definición de la audiencia de predicción también se utiliza para consultar datos históricos que permitan al modelo de aprendizaje automático aprender del pasado. De forma similar a la página anterior, se muestra la cantidad de datos que proporcionan estos filtros junto con el requisito. Si especificas la audiencia deseada y no alcanzas el mínimo, prueba a especificar un filtro más amplio o utiliza la opción **Todos los usuarios**.

{% alert note %}
La audiencia de la predicción no puede superar los 100 millones de usuarios.
{% endalert %}

Cuando la Ventana de eventos es de 14 días o menos, la ventana de tiempo para los filtros que empiezan por "Última...", como "Última aplicación utilizada" y "Última compra realizada **", no puede superar la Ventana de eventos especificada en el [seguimiento de eventos](#event-tracking)**. Por ejemplo, si la Ventana de eventos está configurada en 14 días, la ventana de tiempo para los filtros "Último..." no puede superar los 14 días.

#### Modo de filtro completo

Para construir inmediatamente una nueva predicción, sólo se admite un subconjunto de filtros de segmentación Braze. El Modo de Filtrado Completo te permite utilizar todos los filtros Braze, pero necesitará una Ventana de Sucesos para construir la predicción. 

Por ejemplo, si la ventana de eventos se establece en 14 días, se tardará 14 días en recopilar los datos de usuario y construir la predicción cuando se utilicen filtros sólo admitidos en el modo de filtro completo. Además, algunas estimaciones sobre el tamaño de la audiencia no estarán disponibles en el modo filtrar todo.

### Paso 4: Elige el calendario de actualización

El modelo de aprendizaje automático creado cuando completes esta página se utilizará según el calendario que selecciones aquí, para generar nuevas puntuaciones de la probabilidad de que los usuarios realicen el evento (puntuación de probabilidad). Selecciona la **frecuencia máxima de actualizaciones** que te resulte útil. Por ejemplo, si estás prediciendo compras y planeas enviar una promoción semanal, establece la frecuencia de actualización en **Semanal** el día y la hora que elijas.

{% alert note %}
La vista previa y la predicción de demostración nunca actualizarán las puntuaciones de probabilidad de los usuarios.
{% endalert %}

### Paso 5: Construir predicción

Comprueba que los datos que has proporcionado son correctos y elige **Crear predicción**. También puedes guardar tus cambios en forma de borrador seleccionando **Guardar como borrador** para volver a esta página y construir el modelo más tarde. 

Después de hacer clic en **Construir predicción**, comenzará el proceso que genera el modelo. Esto puede tardar entre 30 minutos y unas horas, dependiendo del volumen de datos. Para esta predicción, verás una página en la que se explica que el entrenamiento está en curso mientras dure el proceso de construcción del modelo.

Una vez completado, la página cambiará automáticamente a la vista de análisis, y recibirás un correo electrónico informándote de que la predicción y los resultados están listos. En caso de error, la página volverá al modo de edición con una explicación de lo que ha ido mal.

La predicción se reconstruirá ("reentrenará") automáticamente cada **dos semanas** para mantenerla actualizada con los datos disponibles más recientes. Ten en cuenta que éste es un proceso distinto del que se produce cuando se obtienen las puntuaciones de probabilidad de los usuarios, el resultado de la predicción. Esto último viene determinado por la frecuencia de actualización que elegiste en el Paso 4.

## Predicciones archivadas

Las predicciones archivadas dejarán de actualizar las puntuaciones de los usuarios. Cualquier predicción archivada que no esté archivada seguirá actualizando las puntuaciones de los usuarios en su horario predeterminado. Las predicciones archivadas nunca se borran y permanecen en la lista.


