---
nav_title: Registros de sincronización y observabilidad
article_title: Registros de sincronización y observabilidad
page_order: 10
page_type: reference
description: "Esta página ofrece un resumen de las características de observabilidad disponibles en CDI."
---

# Registros de sincronización y observabilidad

> El panel de **Registro de Sincronización** de la Ingesta de Datos en la Nube (CDI) te permite supervisar todos los datos procesados por CDI, verificar si los datos se sincronizaron correctamente y diagnosticar cualquier problema con datos "incorrectos" o ausentes.

Para acceder a los registros de sincronización, ve a **Configuración de datos** > **Ingesta de datos en la nube** y selecciona la pestaña **Registro de sincronización**.

## Comprender el panel del Registro de Sincronización

La página principal **del Registro de sincronización** proporciona un resumen de alto nivel de todas tus sincronizaciones, incluido un resumen de las sincronizaciones recientes según su estado actual o final.

* **Corriendo:** Sincroniza los trabajos que están en curso.  
* **Éxito:** Trabajos de sincronización que se completaron y todas las filas se procesaron correctamente.  
* **Éxito parcial:** Trabajos de sincronización que se completaron, pero una o más filas encontraron un error.  
* **Error:** Tareas de sincronización que no se completaron.  
* **Límite superado:** Trabajos de sincronización que dejaron de procesarse porque se superó un límite de datos.

![Un ejemplo de registros de sincronización con 6.576 aciertos totales.]({% image_buster /assets/img/cloud_ingestion/sync_logs1.png %}){: style="max-width:80%"}

Los registros de sincronización también proporcionan los siguientes detalles para cada sincronización:

* **Nombre de sincronización:** El nombre de la configuración de sincronización.  
* **ID de ejecución:** Un identificador único para una ejecución concreta de la sincronización. Selecciona este ID para ver más detalles. También se puede utilizar en los [puntos finales de la API CDI]({{site.baseurl}}/api/endpoints/cdi), o para hacer referencia a una sincronización ejecutada con el soporte de Braze.   
* **Estado:** El estado de la ejecución (éxito, éxito parcial, error, en ejecución).  
* **Nuevas filas leídas de la fuente:** El número de filas nuevas extraídas de tu almacén de datos para esta ejecución.  
* **Resultados:** Un desglose de cuántas filas tuvieron éxito o fallaron en la ejecución.  
* **Última "UPDATED_AT":** La marca de tiempo del registro más reciente procesado en esta ejecución de sincronización.  
* **Hora de inicio de la carrera:** Cuando comenzó el trabajo de sincronización.  
* **Duración de la carrera:** El tiempo total que tardó en completarse la tarea de sincronización.

![Detalles de un registro de sincronización.]({% image_buster /assets/img/cloud_ingestion/sync_logs3.png %}){: style="max-width:80%"}

### Retención de datos

Los datos del registro de sincronización, incluidas todas las cargas útiles a nivel de fila y los detalles de los errores, se conservan hasta **30 días**. Los registros de más de 30 días se purgarán automáticamente.

Los metadatos de ejecución de la sincronización, como el número de filas procesadas, se conservan durante al menos 12 meses.

### Filtrar registros de sincronización

Puedes filtrar la tabla de registros de sincronización para encontrar ejecuciones concretas. Los filtros disponibles son:

* **Fecha de inicio del trabajo:** Selecciona un intervalo predefinido (como "Últimos 30 días") o un intervalo de fechas personalizado.  
* **Estado:** Filtrar por uno o más estados de sincronización (como mostrar sólo los estados **Error** y **Éxito parcial** ).  
* **Nombre de sincronización:** Busca una sincronización concreta por su nombre.

Para investigar una sincronización concreta, selecciona el **ID de ejecución** correspondiente en la tabla Registros de sincronización. En la página **Detalles de la ejecución**, encontrarás un registro granular, fila por fila, de la sincronización.

### Resumen de la ejecución

Esta sección resume la ejecución seleccionada, incluyendo su hora de inicio, hora de finalización, duración y el número total de filas leídas de la fuente. También proporciona un recuento de cuántas filas tuvieron éxito y cuántas dieron lugar a un error.

### Filas procesadas en esta ejecución

Esta tabla proporciona visibilidad a nivel de fila de los datos procesados durante la sincronización, permitiéndote validar registros individuales.

* **Busca:** Puedes buscar un usuario concreto dentro de los resultados de la ejecución utilizando la barra **Buscar por ID de usuario**.  
* **Detalles disponibles:**   
  * **UPDATED_AT:** La fecha y hora de la columna `UPDATED_AT` para esa fila concreta.  
  * **ID:** Los identificadores de usuario (como `external_id`, `email`, o `alias_name`) utilizados para hacer coincidir el registro con un perfil de usuario Braze.  
  * **Estado:** El estado de procesamiento individual de esa fila**(Correcto** o **Error**).  
  * **Carga útil de origen:** Un enlace para ver la carga útil de datos.  
  * **Motivo del error:** Si el estado es **Error**, esta columna proporciona un mensaje que explica por qué la fila no se sincronizó.

#### Visualización de las cargas útiles

Para ver los datos exactos enviados a Braze para una fila concreta, selecciona **Ver carga útil** en la columna Carga útil de **origen**. Muestra la carga útil JSON sin procesar que se procesó para ese usuario.

![Ejemplo de carga útil para una fila concreta de un registro de sincronización.]({% image_buster /assets/img/cloud_ingestion/sync_logs2.png %}){: style="max-width:80%"}

#### Exportar registros de sincronización

Selecciona **Exportar filas** para exportar los registros a nivel de fila de una ejecución de sincronización. A continuación, elige exportar por:

* **Filas con errores:** Descarga un archivo que contiene sólo las filas que tenían un estado de **Error**.
* **Todas las filas:** Descarga un archivo que contiene todas las filas procesadas en la ejecución.

{% alert important %}
La exportación de los registros de sincronización de todas las filas está actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.
{% endalert %}

Los registros no se pueden exportar directamente desde el panel. Una vez generada la exportación, recibirás un correo electrónico con un enlace para descargar el archivo de exportación del registro. 

## Notificaciones

Puedes configurar notificaciones por correo electrónico para mantenerte informado sobre el estado de tus sincronizaciones CDI. Estos ajustes se configuran cuando creas una sincronización y se pueden actualizar en cualquier momento.

### Notificaciones de error

Se requiere al menos una dirección de correo electrónico de contacto para recibir notificaciones de errores de sincronización. Estas alertas se envían cuando un trabajo de sincronización completo no se ejecuta o no se completa, o si la sincronización se encuentra con un error que requiere la intervención del usuario para cambiarlo, como credenciales caducadas o una tabla de origen que falta.

Las notificaciones adicionales incluyen:

- **Error de fila:** Recibe alertas cuando un determinado porcentaje de filas no se actualice en una sincronización.
- **Umbral de fallo (%):** Especifica el porcentaje de fallos de fila que deben desencadenar una alerta. Por ejemplo, si se establece en **1**, se enviaría una notificación si el 1% o más de las filas de una ejecución de sincronización dan lugar a un error.
- **Sincronización correcta:** Recibe una notificación al finalizar correctamente una sincronización.
- **Alerta aunque no cambie ninguna fila:** Recibe una notificación incluso cuando una ejecución de sincronización correcta procese cero filas nuevas o actualizadas.