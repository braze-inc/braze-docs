{% if include.alert == "Liquid email display name and reply-to address" %}

{% alert tip %}
Puedes utilizar [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) en los campos **De nombre para mostrar + dirección** y **Responder a dirección** para crear plantillas dinámicas basadas en atributos personalizados. Esto te permite realizar envíos desde diferentes marcas, regiones o departamentos utilizando una única campaña de correo electrónico o paso en Canvas.
{% endalert %}

{% endif %}

{% if include.alert == "Reference properties from triggering event" %}

{% alert tip %}
No necesitas un paso de Contexto para hacer referencia a propiedades del evento desencadenante en pasos para [rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) o [división de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split). Puedes hacer referencia a las propiedades directamente en los grupos de filtros con el filtro **Variable contextual**. Asegúrate de seleccionar el tipo de datos correcto.
{% endalert %}

{% endif %}

{% if include.alert == 'catalog data images' %}

{% alert tip %}
Para extraer imágenes de los elementos desencadenantes del catálogo, éste debe incluir un campo llamado `image_url`. Luego puedes hacer referencia a él utilizando {%raw%}``{{ items[0].image_url }}``{%endraw%}.
{% endalert %}

{% endif %}