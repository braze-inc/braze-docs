---
nav_title: Crear códigos
article_title: Crear códigos promocionales
page_order: 0.1
description: "Aprende a crear códigos promocionales en tus campañas y Lienzos."
---

# Crear códigos promocionales

> Aprende a crear códigos promocionales en tus campañas y Lienzos.

## Crear una lista de códigos promocionales {#create}

### Paso 1: Crear una nueva lista

En el panel, ve a **Configuración de datos** > **Códigos promocionales** y, a continuación, selecciona **Crear lista de códigos promocionales**.

![Botón para crear un código promocional.]({% image_buster /assets/img/promocodes/promocode1.png %})

### Paso 2: Introduce los datos

1. Asigne un nombre a su lista de códigos promocionales y añada una descripción opcional.
2. A continuación, cree un fragmento de código para el código de promoción. 

Aquí tienes algunos detalles que debes tener en cuenta al crear un fragmento de código:

- No puedes editar un fragmento de código después de guardarlo.
- Los fragmentos distinguen entre mayúsculas y minúsculas. Por ejemplo, el sistema reconoce "Birthday_promo" y "birthday_promo" como dos fragmentos de código diferentes.
- Utiliza el nombre del fragmento en Liquid para hacer referencia a este conjunto de códigos promocionales.
- Asegúrate de que el fragmento de código no se esté utilizando ya en otra lista.

![Una lista de códigos promocionales llamada "SpringSale2025" con el fragmento de código "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Paso 3: Elige opciones de código promocional

Cada lista de códigos promocionales tiene una fecha y hora de caducidad correspondientes que se establecen al crearla. La duración máxima de caducidad es de seis meses desde el día en que creas o editas tu lista.

Dentro de ese plazo, puedes cambiar y actualizar la fecha de caducidad repetidamente. Esta fecha de caducidad se aplica a todos los códigos añadidos a esta lista. Al caducar, los códigos se eliminan del sistema Braze, y no se envía ningún mensaje que llame al fragmento de código de esa lista.

![Enumera la configuración de caducidad para que todos los códigos restantes caduquen el 30 de abril de 2025 a las 12 de la mañana.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

También tienes la opción de configurar alertas de umbral opcionales y personalizadas. Si están configuradas, estas alertas envían un correo electrónico al destinatario designado cuando la lista se está quedando sin códigos promocionales disponibles en esta lista o cuando tu lista de códigos promocionales está a punto de caducar. El destinatario recibe una notificación una vez al día.

![Un ejemplo de alerta de umbral para notificar a "marketing@abc.com" cuando la lista de códigos promocionales caduque en 5 días.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Paso 4: Subir códigos promocionales

Braze no gestiona la creación ni el canje de códigos, lo que significa que debes generar tus códigos promocionales en un archivo CSV y subirlos a Braze. 

Asegúrate de que tu archivo CSV sigue estas directrices:

- Incluye una columna para códigos promocionales.
- Tiene un código promocional por fila.

Puede utilizar nuestra integración con [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) o [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) para crear y exportar códigos promocionales.

{% alert important %}
El tamaño máximo del archivo es de 100 MB y el tamaño máximo de la lista es de 20MM de códigos no utilizados. Si descubres que se ha subido un archivo incorrecto, sube uno nuevo que sustituya al anterior.
{% endalert %}

1. Una vez finalizada la carga, seleccione **Guardar lista** para guardar todos los datos y códigos que acaba de introducir.

![Archivo CSV llamado "springsale" que se ha cargado correctamente.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Tras seleccionar Guardar, aparece una nueva fila en el **Historial de Importaciones**.
3\. Para actualizar la tabla y comprobar si la importación ha finalizado, seleccione <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** en la parte superior de la tabla.

![Códigos promocionales en proceso de carga.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Los archivos más grandes tardan varios minutos en importarse. Mientras esperas, puedes salir de la página y trabajar en algo mientras se realiza la importación. Cuando finaliza la importación, el estado cambia a **Completado** en la tabla.
{% endalert %}

## Actualizar una lista de códigos promocionales

Para actualizar una lista, seleccione una de las listas existentes. Puede cambiar el nombre, la descripción, la caducidad de la lista y los umbrales de alerta. También puede añadir más códigos a la lista cargando nuevos archivos y seleccionando **Actualizar lista**. Todos los códigos de la lista tienen la misma caducidad, independientemente de la fecha de importación.

{% alert important %}
Los códigos promocionales no se pueden eliminar.
{% endalert %}

### Modificar una lista incorrecta de códigos promocionales 

Si has cargado un archivo CSV con los códigos promocionales incorrectos y has seleccionado **Guardar lista**, puedes resolverlo por cualquiera de los dos métodos:

- Desaparece toda la lista: Deja de utilizar la lista actual de códigos promocionales en cualquier campaña, Lienzo o plantilla. A continuación, sube el archivo CSV con los códigos correctos y utilízalos en tu mensajería.
- Utiliza los códigos incorrectos: Crea una campaña que envíe códigos promocionales de la lista de códigos promocionales incorrectos a un marcador de posición hasta que se utilicen todos los códigos incorrectos. A continuación, carga los códigos promocionales correctos en la misma lista.
