---
nav_title: Páginas de destino
article_title: Páginas de inicio
page_order: 31
guide_top_header: "Páginas de inicio"
description: "Este artículo contiene recursos para crear y personalizar páginas de destino Braze."
alias: /landing_pages/
---

# Acerca de las páginas de destino

> Las páginas de destino de Braze son páginas web independientes que pueden impulsar tu estrategia de captación e interacción de usuarios.

Utiliza las páginas de destino para aumentar tu audiencia, captar datos de usuario, promocionar ofertas especiales y apoyar campañas multicanal.

{% alert note %}
La disponibilidad de la página de destino y del dominio personalizado depende de tu paquete Braze. Ponte en contacto con tu director de cuentas o administrador del éxito del cliente para empezar.
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## Requisitos previos

Para poder acceder a las páginas de destino, crearlas y publicarlas, necesitas [permisos de]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) administrador o todos los permisos siguientes:

- Acceder a páginas de inicio
- Crear borradores de página de inicio
- Publicar páginas de inicio

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## Niveles del plan

El número de páginas de destino publicadas y dominios personalizados que puedes utilizar depende de tu tipo de plan: gratuito o de pago (incremental).

| Característica                                                                                                   | Grada libre     | Nivel de pago (incremental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Páginas de destino publicadas                                                                 | Cinco por empresa | 20 adicionales |
| Dominios personalizados          | Uno por empresa | Cinco adicionales |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Añadir Google Tag Manager a una página de destino

Para añadir Google Tag Manager a tus páginas de destino, añade un bloque de **código personalizado** a tu página de destino en el editor de arrastrar y soltar, y luego inserta el código de Google Tag Manager en el bloque. Asegúrate de añadir una capa de datos antes del código del administrador de etiquetas, como en este ejemplo:

```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

Para más detalles sobre la implementación de Google Tag Manager, consulta [la documentación de Google.](https://developers.google.com/tag-platform/tag-manager/datalayer#installation)

## Preguntas más frecuentes

### ¿Cuál es el tamaño máximo de las páginas de destino?

El tamaño del cuerpo de la página de destino puede ser de hasta 500 KB.

### ¿Existen requisitos técnicos para publicar una página de aterrizaje?

No, no hay requisitos técnicos.

### ¿Existe un editor HTML para las páginas de destino?

Sí. Utiliza el bloque de **código personalizado** en el editor de arrastrar y soltar para añadir o editar HTML.

### ¿Puedo crear un webhook dentro de una página de destino?

No, actualmente no es compatible.
