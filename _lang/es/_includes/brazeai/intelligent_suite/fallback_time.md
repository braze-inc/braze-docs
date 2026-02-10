Puedes elegir una de las siguientes opciones:

- **Los más populares:** Este es el tiempo de uso más popular de tu aplicación entre todos los usuarios.
- **Personalizado:** Se trata de una alternativa personalizada de tu elección. El mensaje se entregará en función de la zona horaria local de cada usuario.

{% subtabs local %}
{% subtab most popular %}
La hora más popular de la aplicación viene determinada por la hora media de inicio de sesión de tu espacio de trabajo (en hora local). Este tiempo se muestra en rojo en el gráfico de vista previa.

En el improbable caso de que tu aplicación no tenga suficientes datos de sesión para calcular cuándo se utiliza más la aplicación (una aplicación completamente nueva sin datos), el mensaje se enviará a las 5 de la tarde en la zona horaria local del usuario. Si se desconoce la hora local del usuario, se enviará a las 17:00 en la zona horaria de tu empresa.

Es importante ser consciente de las limitaciones de utilizar el Intelligent Timing al principio del ciclo de vida de un usuario, cuando se dispone de datos limitados. Puede seguir siendo valioso, ya que incluso los usuarios con pocas sesiones grabadas pueden ofrecer información sobre su comportamiento. Sin embargo, Braze puede calcular más eficazmente la hora óptima de envío más adelante en el ciclo de vida del usuario.

{% if include.type == "campaigns" %}
{% alert note %}
Para las campañas, si especificaste una [ventana de entrega](#sending-within-specific-hours) y el momento más popular para utilizar tu aplicación cae fuera de esa ventana, el mensaje se enviará más cerca del borde de la ventana de entrega. Por ejemplo, si tu ventana de entrega es de 13:00 a 20:00 y la hora más popular de la aplicación es las 22:00, el mensaje se enviará a las 20:00.
{% endalert %}
{% endif %}
{% endsubtab %}

{% subtab custom %}
Utiliza la hora alternativa personalizada para elegir una hora diferente para enviar el mensaje. De forma similar a la hora de la aplicación más popular, el mensaje se enviará a la hora alternativa de la zona horaria local del usuario. Si se desconoce la zona horaria local del usuario, se enviará en la zona horaria de tu empresa.

Para las campañas con una hora alternativa personalizada especificada, si lanzas la campaña dentro de las 24 horas siguientes a la fecha de envío, los usuarios cuyas horas óptimas ya hayan pasado recibirán la campaña a la hora alternativa personalizada. Si la hora alternativa personalizada ya ha pasado en su zona horaria, el mensaje se enviará inmediatamente.
{% endsubtab %}
{% endsubtabs %}