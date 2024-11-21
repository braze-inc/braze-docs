---
nav_title: Configuración multilingüe
article_title: Configuración multilingüe
alias: "/multi_language_support/"
page_order: 5.5
description: "Este artículo ofrece una visión general de la configuración multilingüe en el panel de control de Braze y cómo utilizar las configuraciones regionales en la mensajería."
---

# Configuración multilingüe

> Al ajustar la configuración multilingüe, puede dirigirse a usuarios de distintos idiomas y ubicaciones con mensajes diferentes, todo dentro de un mismo mensaje de correo electrónico.

## Requisitos previos

Para editar y administrar el soporte multilingüe, debes tener el permiso de usuario "Administrar configuración multilingüe". Para añadir la configuración regional a un mensaje, necesitarás permisos para editar campañas.

## Añadir una configuración regional

1. Vaya a **Configuración** > **Soporte multilingüe** en **Configuración del espacio de trabajo**.
2. Selecciona **Añadir configuración regional**.
3. Introduce un nombre para la configuración regional.
4. Para los **atributos de usuario**, seleccione el idioma que desea añadir utilizando el menú desplegable **Idioma**.
5. (opcional) Seleccione el país que se asociará al idioma.
6. Selecciona **Añadir configuración regional**. 

![Ejemplo de francés añadido como configuración regional para usuarios cuyo país es Canadá.][2]{: style="max-width:80%;"}

Para conocer los pasos necesarios para utilizar estas configuraciones regionales en sus campañas de correo electrónico y Canvas, consulte [Utilización de configuraciones regionales]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/).

## Preguntas más frecuentes

#### ¿Cuántas configuraciones regionales puedo añadir?
Puedes añadir hasta 200 configuraciones regionales.

#### ¿Dónde se almacenan los archivos de traducción en Braze?
Los archivos de traducción se almacenan a nivel de campaña, lo que significa que cada variante de mensaje debe tener traducciones cargadas.

#### ¿El nombre de la configuración regional tiene que seguir un patrón o formato específico?
No. Puedes utilizar la convención de nomenclatura que prefieras. El nombre de la configuración regional se utiliza al seleccionar la configuración regional en el editor y aparecerá en los encabezados del archivo que descargue con los identificadores de traducción.

#### ¿Puedo utilizar atributos personalizados para definir una configuración regional?
Actualmente no. Póngase en contacto con el gestor de su cuenta o deje [un comentario sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) con más detalles sobre cómo definiría las localidades.

[2]: {% image_buster /assets/img/multi-language_support/add_locale.png %}
