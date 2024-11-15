---
nav_title: Preguntas frecuentes sobre el fraude del bombeo de tráfico SMS
permalink: "/sms_traffic_pumping_fraud/"
description: "Este artículo de referencia cubre las preguntas más frecuentes sobre el fraude en el bombeo de tráfico SMS."
hidden: true
---

# Preguntas frecuentes sobre el fraude por bombeo de tráfico SMS 

### ¿Qué es el fraude por bombeo de tráfico SMS? 

El bombeo de tráfico SMS es una amenaza creciente en el espacio SMS. Se produce cuando los estafadores encuentran la forma de desencadenar el envío de mensajes SMS a números de teléfono que no están asociados a clientes reales, con el fin de recaudar ingresos vinculados al envío fraudulento de mensajes. La mayoría de las veces, desencadenan envíos de SMS de gran volumen utilizando formularios en línea, como formularios de adhesión voluntaria por SMS o contraseñas de un solo uso para restablecer contraseñas o iniciar sesión en cuentas.  

Por ejemplo, si una marca tiene un formulario de adhesión voluntaria por SMS en su sitio web para que los clientes opten por recibir mensajes de texto, un estafador introducirá números de teléfono fraudulentos en el formulario para desencadenar mensajes SMS. El estafador utiliza números de teléfono de tarificación adicional para estos mensajes y reclama una parte de los ingresos al operador de telefonía móvil local, que es responsable de la entrega de los mensajes a los usuarios finales. Este esquema genera cargos fraudulentos a la marca. 

### ¿Qué hace Braze para mitigar el fraude en el bombeo de SMS?

Braze mantiene actualmente una lista de bloqueo de SMS tanto para los países sometidos a embargo por EE.UU., como para los países conocidos por su alto riesgo de bombeo de tráfico, que puede consultarse en [nuestra documentación]({{site.baseurl}}/sms_country_blocklist). Se bloquean todos los intentos de envío a números de teléfono con estos códigos de país.

Además, Braze está introduciendo una Lista de Permisos Geográficos para SMS, que te protegerá aún más contra comportamientos fraudulentos al imponer controles sobre los países a los que puedes enviar.

### ¿Cómo puedo proteger mi marca contra el fraude por bombeo de SMS? 

Hay varias formas de protegerte, entre ellas 
- **Controla tus volúmenes diarios de envío de SMS para detectar picos y anomalías:**
    - Recomendamos establecer [límites de campaña y alertas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) para limitar y notificar si se envía un número inusualmente alto de mensajes.
    - Los picos inusuales en el envío de mensajes podrían indicar un bombeo de tráfico.
    - Un número inusualmente alto de adhesiones voluntarias en poco tiempo (al margen de estrategias intencionadas para conseguir adhesiones voluntarias) podría indicar un bombeo de tráfico.
- **Mejora la seguridad de los formularios de captura de números de teléfono online:**
    - [Las plantillas de formularios de registro de]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) Braze SMS proporcionan medidas de seguridad listas para usar, como la validación de la longitud y el formato del número de teléfono. También puedes configurar el formulario para que sólo recoja números de teléfono con códigos de país que se ajusten a tus clientes objetivo:
        - Por ejemplo, si sólo haces negocios en EE.UU. y Reino Unido, configura el formulario para que sólo recoja números con código de país +1 y +44 (puedes encontrar detalles técnicos en [nuestra documentación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/#step-2-customize-your-phone-number-input-component)).
    - Si estás creando una captura de números de teléfono personalizada en tu sitio web, te recomendamos que establezcas reglas para validar la longitud y el formato del número de teléfono y que te asegures de que los formularios están totalmente completos antes de recopilar los números de teléfono. Asegúrate de trabajar con tu equipo de ingeniería o técnico para validar las entradas del formulario tanto en el lado del cliente como en el lado del servidor para una máxima protección.
        - Además, considera la posibilidad de utilizar herramientas como CAPTCHA para garantizar que el formulario lo envía un humano y no un proceso automatizado. Un requisito CAPTCHA en los formularios de registro por SMS puede ayudar a reducir el número de registros fraudulentos.

### Mi marca hace negocios en EE. UU. y ese país está en mi Lista de permisos geográficos permitidos por SMS. ¿Mis clientes seguirán recibiendo mis mensajes SMS cuando viajen fuera de EE.UU.? 

Sí, siempre que tus clientes tengan un número de teléfono con un código de área de EE.UU., seguirán recibiendo tus mensajes mientras viajan. 

{% alert important %}
Si tienes más preguntas sobre el bombeo de tráfico SMS y sobre cómo estos cambios en el producto pueden afectar a tus envíos de SMS, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}
