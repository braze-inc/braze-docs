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

{% alert important %}
El soporte multilingüe está actualmente en acceso temprano. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Añadir una configuración regional

1. Vaya a **Configuración** > **Soporte multilingüe** en **Configuración del espacio de trabajo**.
2. Selecciona **Añadir configuración regional** y, a continuación, selecciona **Configuración regional predeterminada** o **Atributos personalizados**.<br><br>![El desplegable "Añadir localización" con opciones para seleccionar la localización predeterminada o atributos personalizados.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}
3. Introduce un nombre para la configuración regional.
4. Selecciona los atributos de usuario correspondientes a la opción de localización que hayas elegido.

{% tabs %}
{% tab Localización predeterminada %}

En **Configuración regional predeterminada**, utiliza los desplegables para seleccionar el idioma que se va a añadir y, opcionalmente, el país que se va a asociar al idioma.<br><br>![Una ventana llamada "Añadir localización - Idioma y país predeterminados" para especificar el idioma y el país.]({% image_buster /assets/img/multi-language_support/default_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Atributos personalizados %}

Para los **atributos personalizados**, utiliza el desplegable para seleccionar el atributo personalizado asociado y, en el campo de texto, introduce el valor.<br><br>![Una ventana llamada "Añadir localización - Atributos personalizados" para especificar el atributo personalizado y el valor.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{: start="5"}
5\. Selecciona **Añadir configuración regional**. 

Para conocer los pasos necesarios para utilizar estas configuraciones regionales en sus campañas de correo electrónico y Canvas, consulte [Utilización de configuraciones regionales]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/).

## Consideraciones

- Al configurar una localización, puedes seleccionar los idiomas a partir de los atributos predeterminados del usuario o de atributos personalizados. No puedes elegir entre ambos.
- Puedes seleccionar hasta dos atributos personalizados en una única localización, o hasta dos idiomas predeterminados para atributos de usuario. En ambos casos, el segundo atributo es opcional.
- Cuando edites los valores traducidos del archivo CSV, evita modificar los valores predeterminados del archivo.
- La clave de configuración regional de tu archivo cargado debe coincidir con la de tu configuración multilingüe.

### Apoyo y priorización

- Los usuarios que coinciden con la localización de un atributo personalizado tienen prioridad sobre los usuarios que coinciden con un atributo predeterminado de usuario.
- La compatibilidad con atributos personalizados se limita a los tipos de cadena y a la clave de comparación `equals`.
- Si se elimina un atributo personalizado o se cambia su tipo, el usuario ya no podrá pertenecer a esa localización y bajará en la lista de prioridad de localizaciones a las que pertenece o recibirá traducciones de marketing predeterminadas.
- Si una localización no es válida (el atributo personalizado ha cambiado o se ha eliminado), el error aparecerá en la página de **Soporte multilingüe**.

## Preguntas más frecuentes

#### ¿Cuántas configuraciones regionales puedo añadir?

Puedes añadir hasta 200 configuraciones regionales.

#### ¿Dónde se almacenan los archivos de traducción en Braze?

Los archivos de traducción se almacenan a nivel de campaña, lo que significa que cada variante de mensaje debe tener traducciones cargadas.

#### ¿El nombre de la configuración regional tiene que seguir un patrón o formato específico?

No. Puedes utilizar la convención de nomenclatura que prefieras. El nombre de la configuración regional se utiliza al seleccionar la configuración regional en el editor y aparecerá en los encabezados del archivo que descargue con los identificadores de traducción.

