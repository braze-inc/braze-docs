---
nav_title: Zeotap
description: "Este artículo de referencia describe la asociación entre Braze y Zeotap, una plataforma de datos de los clientes de nueva generación que proporciona resolución de identidades, información y enriquecimiento."
page_type: partner
search_tag: Partner
page_order: 1
---

# Zeotap

> [Zeotap](https://zeotap.com/) es una plataforma de datos de clientes de nueva generación que le ayuda a descubrir y comprender a su audiencia móvil proporcionando resolución de identidades, perspectivas y enriquecimiento de datos.

Con la integración de Zeotap y Braze, puede ampliar la escala y el alcance de sus campañas sincronizando los segmentos de clientes de Zeotap para asignar los datos de usuario a las cuentas de usuario de Braze. A continuación, puede actuar en función de estos datos y ofrecer experiencias personalizadas a sus usuarios.

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
|Cuenta Zeotap | Se necesita una [cuenta Zeotap](https://zeotap.com/) para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze  | La URL de su punto final REST. Tu punto final dependerá de la [URL de Braze para tu instancia]({% image_buster /assets/img/zeotap/zeotap1.png %}). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integración

### Paso 1: Crear un destino Zeotap

1. Desde la plataforma Zeotap Unity, navega hasta la aplicación **DESTINATIONS**.
2. En **Todos los canales**, seleccione **Braze**.
3. En el mensaje que aparece, nombra tu destino e indica tu nombre de cliente y la clave de API REST Braze asociada a tu cuenta Braze.
4. Por último, seleccione su instancia de punto final Braze REST en el menú desplegable y guarde el destino. <br><br>![]({% image_buster /assets/img/zeotap/zeotap1.png %})

### Paso 2: Cree y vincule un segmento Zeotap a su destino 
 
1. Desde la plataforma Zeotap Unity, navega hasta la aplicación **CONNECT**.
2. Cree un segmento y seleccione el destino Braze creado en el paso 1.
3. Seleccione un identificador de salida compatible: MAID, dirección de correo electrónico con hash SHA256 o cualquier identificador de cliente 1P reconocido por Braze (si desea utilizar un identificador personalizado para su cuenta Braze, póngase en contacto con Zeotap para que se habilite para su cuenta). Sólo se puede utilizar un identificador de salida para la integración Braze. Estos identificadores deben ser los mismos que el ID externo establecido al recopilar los datos de Braze SDK.
4. Guarda el segmento.

![]({% image_buster /assets/img/zeotap/zeotap2.png %})

{% alert note %}
Los identificadores que aparecen están disponibles en el segmento y son compatibles con Braze.
{% endalert %}

### Paso 3: Crear segmento Braze

Tras crear, enviar y procesar correctamente un segmento en Zeotap, los usuarios de Zeotap aparecerán en el panel de control de Braze. Puede buscar usuarios por ID de usuario en el panel de control de Braze. 

![Un perfil de usuario de Braze que muestra los segmentos del uno al cuatro como "verdadero" en "Atributos personalizados".]({% image_buster /assets/img/zeotap/zeotap4.png %})

Si un usuario forma parte del segmento Zeotap, el nombre del segmento aparece como atributo personalizado en su perfil de usuario con el valor booleano `true`. Anote el nombre del atributo personalizado, ya que lo necesitará al crear un segmento Braze. 

A continuación, debe crear y definir este segmento en Braze:
1. En el panel de control de Braze, seleccione **Segmentos** y, a continuación, **Crear segmento**.
2. A continuación, asigne un nombre a su segmento y seleccione el segmento de atributos personalizados creado en Zeotap.
3. Guarda los cambios. 

![En el constructor de segmentos Braze, puedes encontrar los segmentos importados configurados como atributos personalizados.]({% image_buster /assets/img/zeotap/zeotap3.png %})

Ahora puede añadir este segmento recién creado a futuras campañas y lienzos Braze para dirigirse a estos usuarios finales. 

