---
nav_title: Transformación de datos
hidden: true
---

# Transformación de datos Braze

> Braze [Data Transformation]({{site.baseurl}}/data_transformation/) puede recibir un webhook de una plataforma asociada y permitir que un cliente defina una asignación para convertir la carga útil de ese webhook en los datos de usuario deseados, como atributos, eventos o compras en perfiles de usuario Braze.

## Cómo sería una integración basada en la transformación de datos

Una integración de socios basada en la función de transformación de datos podría ser una plantilla de código de transformación compartida con los clientes a través de documentación pública.

Para los clientes mutuos, sería algo así:

1. Se conectan a su plataforma y configuran webhooks.
2. Trabajan con su equipo Braze para obtener acceso a Braze Data Transformation y crear una nueva transformación dentro de su panel Braze.
3. Se copia la URL generada por la transformación.
4. De vuelta en Braze, envían un webhook de prueba a la URL de transformación copiada.
5. En Braze, copian y pegan la plantilla de código de transformación.
6. Permiten la transformación.
7. Cuando se activa, pueden verificar a través de la herramienta de búsqueda de usuarios Braze que el perfil del usuario se actualiza en función del webhook y editar el código de transformación como se desee.

{% alert tip %}
Se recomienda crear una transformación por tipo de webhook enviado a Braze cuando se construyan ejemplos de código de transformación.
{% endalert %}
