---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 9
description: "Esta página explica cómo configurar Inbox Vision, una característica que permite a los especialistas en marketing ver sus correos electrónicos desde la perspectiva de varios clientes de correo electrónico y dispositivos móviles."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision

> Inbox Vision te permite ver tus correos electrónicos desde la perspectiva de varios clientes de correo electrónico y dispositivos móviles. Por ejemplo, puedes utilizar Inbox Vision para comprobar si hay diferencias entre los modos oscuro y claro y confirmar que tus correos electrónicos son correctos.

{% alert important %}
En general, tu correo electrónico no funcionará con Inbox Vision si el contenido de tu correo electrónico depende de la información de la plantilla, como la información del perfil de usuario. Esto se debe a que las plantillas de Braze en un usuario vacío cuando enviamos correos electrónicos utilizando esta característica.
{% endalert %}

## Pruebe su correo electrónico en Inbox Vision

Su correo electrónico debe incluir una línea de asunto y un dominio de envío válido para poder ver estas vistas previas. Tenga en cuenta que su correo electrónico puede tener un aspecto diferente en el escritorio y en los dispositivos móviles. Al ver estas vistas previas, puede revisar su contenido y asegurarse de que su correo electrónico se muestra como es debido.

Para probar su mensaje de correo electrónico en Inbox Vision, haga lo siguiente:

1. Vaya a su editor de arrastrar y soltar o a su editor de correo electrónico HTML.
2. En tu editor, selecciona **Vista previa y Prueba**.
3. Selecciona **Visión de buzón de entrada**. 
4. Selecciona **Ejecutar Visión de Buzón de Entrada**. Esto puede llevar entre dos y diez minutos.
5. A continuación, selecciona una baldosa para ver la vista previa con más detalle. Estas vistas previas están agrupadas en estas secciones: **Clientes Web**, **Clientes de Aplicación** y **Clientes Móviles**.

![Visión general de Inbox Vision para el editor HTML.][1]

{: start="6"}
6\. Haz cambios en una plantilla, si es necesario.
7\. Selecciona **Volver a ejecutar la prueba** para ver las vistas previas actualizadas.

### Vista previa como usuario

Cuando previsualizas el correo electrónico como un usuario aleatorio, cualquier configuración o atributo específico asociado a un usuario, como su nombre o preferencias, no se guarda para las previsualizaciones actuales o futuras. Cuando seleccionas un usuario personalizado, la vista previa mostrada en la Visión de la bandeja de entrada puede diferir de la vista previa de mensajes en otros lugares, ya que esta opción utiliza datos de usuario específicos para crear la vista previa.

## Análisis del código

El análisis de código es una forma de que Braze resalte los problemas que puedan existir con su HTML, mostrando el número de ocurrencias de cada problema y proporcionando información sobre qué elementos HTML no son compatibles. 

### Visualización de la información de análisis de código

Esta información puede encontrarse en la pestaña **Visión de la Bandeja de Entrada** seleccionando <i class="fas fa-list"></i> **List view**. Esta vista de lista sólo está disponible para plantillas de correo electrónico HTML. Si utiliza plantillas de correo electrónico de arrastrar y soltar, compruebe las vistas previas para resolver cualquier posible problema.

![Ejemplo de análisis de código en la vista previa de Inbox Vision.][2]

{% alert note %}
A veces, el análisis del código se mostrará más rápido que la vista previa para un cliente de correo electrónico concreto. Esto se debe a que Braze espera hasta que el correo electrónico llega a la bandeja de entrada antes de hacer la captura de pantalla.
{% endalert %}

## Pruebas de spam

Las pruebas de spam intentan predecir si su correo electrónico llegará a las carpetas de spam o a las bandejas de entrada de sus clientes. Las pruebas de spam se ejecutan en los principales filtros de spam, como IronPort, SpamAssassin y Barracuda, así como en los filtros de los principales proveedores de servicios de Internet (ISP), como Gmail.com y Outlook.com.

### Ver los resultados de las pruebas de correo no deseado

Para comprobar los resultados de tus pruebas de correo no deseado, haz lo siguiente:

1. Selecciona la pestaña **Pruebas de correo no deseado** en la sección **Visión de la bandeja de entrada**. La tabla de **resultados de la prueba de spam** muestra el nombre, el estado y el tipo del filtro de spam.

![Tabla de resultados de la prueba de spam con tres columnas: Nombre, estado y tipo. Hay una lista de filtros de correo no deseado y filtros ISP que han superado las pruebas de correo no deseado, lo que indica que la campaña de correo electrónico no caerá en la carpeta de correo no deseado.][4]

{: start="2"}
2\. Revisa estos resultados y haz los ajustes necesarios en tu campaña de correo electrónico.
3\. Selecciona **Reejecutar prueba** para volver a cargar los resultados de tus pruebas de correo no deseado.

## Precisión de las pruebas

Todas nuestras pruebas se realizan con clientes de correo electrónico reales. Braze se esfuerza por comprobar que todos los renders sean lo más precisos posible. Si observas constantemente un problema con un cliente de correo electrónico, abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

[1]: {% image_buster /assets/img_archive/inboxvision1.png %}
[2]: {% image_buster /assets/img_archive/inboxvision2.png %}
[3]: {% image_buster /assets/img_archive/inboxvision4.png %}
[4]: {% image_buster /assets/img_archive/email_spam_testing.png %}
