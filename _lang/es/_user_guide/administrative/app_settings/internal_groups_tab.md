---
nav_title: Grupos internos
article_title: Grupo interno
page_order: 10
page_type: reference
description: ""

---

# Grupos internos

>   

{% alert tip %}

{% endalert %}

## 



## 

 

1. Vaya a **Configuración** > **Grupos internos**.
2. 
3. 
4. 

|          | Descripción                                                                                 |
|--------------------|---------------------------------------------------------------------------------------------|
|    | Se utiliza para verificar eventos o registros de su dispositivo de prueba.                                    |
|  | Puede utilizarse en mensajes push, de correo electrónico e in-app para enviar una copia renderizada del mensaje. |
|          | Envía automáticamente una copia del correo electrónico a todas las personas del Grupo Semilla al enviarlo.               |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



### Añadir usuarios de prueba

 

1. 
2. 

|                   | Descripción                                                                                                                                                                                                                                          |
|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  |                                                                                                                                                            |
|   | Busca por dirección IP. A continuación, proporcione un nombre para cada usuario de prueba que se añada. Este es el nombre con el que se asociarán todos los registros de eventos en la página [Registro de usuario de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/). |
|       |  Sólo puede añadir usuarios ya conocidos en el panel de control.           |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



### Grupos de pruebas de contenido

Similar al envío de una prueba de vista previa de un mensaje, el Grupo de prueba de contenido le ahorra tiempo y le permite lanzar pruebas a una lista predefinida de usuarios de Braze simultáneamente.  Sólo los grupos etiquetados como Grupos de prueba de contenido estarán disponibles en la sección de vista previa de un mensaje.

{% alert note %}
Los mensajes [SMS de]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) prueba sólo pueden enviarse a números de teléfono válidos de la base de datos.
{% endalert %}

 Si su mensaje incluye algún líquido u otra personalización dinámica, Braze utilizará los atributos disponibles para cada usuario para personalizar el contenido del mensaje. Para los usuarios que no tengan atributos, Braze utilizará el valor predeterminado establecido.

Además, si previsualiza el mensaje como usuario aleatorio, usuario personalizado o usuario existente, puede enviar esa versión previsualizada en su lugar. Si desactiva la casilla de verificación, podrá enviar en función de los atributos de cada usuario frente a la versión previsualizada.





### Grupos semilla

 

  

 

 

- 
-  
- 
- 

{% alert tip %}

{% endalert %}

#### Para las campañas



Los Grupos Semilla se envían una vez a cada variante de correo electrónico y se entregan la primera vez que el usuario recibe esa variante concreta. En el caso de los mensajes programados, suele ser la primera vez que se lanza la campaña. Para las campañas basadas en acciones o desencadenadas por la API, será el momento en que se envía un mensaje al primer usuario.

 

{% alert note %}

{% endalert %}



#### Para lienzo

Los grupos de semillas en Canvas funcionan de forma similar a la de cualquier campaña activada. Braze detecta automáticamente todos los pasos que contienen un mensaje de correo electrónico y los enviará cuando el usuario llegue por primera vez a ese paso concreto.

Si se actualizó un paso de correo electrónico después de enviar el grupo semilla, se presentará la opción de enviar solo a los pasos actualizados, a todos los pasos o de desactivar las semillas.

