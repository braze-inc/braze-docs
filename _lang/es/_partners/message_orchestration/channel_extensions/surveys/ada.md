---
nav_title: Ada
article_title: Ada
description: "Este artículo de referencia describe la alianza entre Braze y Ada, una plataforma basada en IA que automatiza y personaliza las interacciones con los clientes. Esta integración te permite aumentar los perfiles de usuario con datos recogidos de tus conversaciones automatizadas con Ada."
alias: /partners/ada/
page_type: partner
search_tag: Partner

---

# Ada

> [Ada](https://ada.cx) es una plataforma de interacción con las marcas que automatiza y personaliza la experiencia del cliente mediante IA conversacional. Utiliza Ada para adaptar tus mensajes y segmentar las campañas en función de los datos de los usuarios, mide y analiza las conversaciones para descubrir nuevas oportunidades y utiliza la información obtenida del chat con los clientes para enriquecer tus perfiles de usuario.  

La integración de Braze y Ada te permite aumentar los perfiles de usuario con datos recogidos de tus conversaciones automatizadas con Ada. Puedes establecer atributos de usuario personalizados basados en la información que recopiles durante una conversación de Ada y registrar eventos personalizados en Braze en puntos específicos de una conversación de Ada. Al conectar tu chatbot Ada a Braze, puedes conocer mejor a tus consumidores en función de las preguntas que hagan sobre tu marca o iniciando conversaciones con ellos de forma proactiva, haciéndoles preguntas que te permitan conocer mejor sus intereses y preferencias.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Ada | Para beneficiarse de esta alianza, es necesario disponer de una cuenta [Ada](https://ada.cx) con las aplicaciones Braze y Answer Utilities activadas. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST][1]. Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

Entre los casos de uso habituales para la integración de Braze y Ada se incluyen:
- Realizar un seguimiento de las diferentes interacciones que tus clientes tienen con tu bot Ada como eventos personalizados en Braze, para saber qué clientes han participado en campañas proactivas en Ada, han sido transferidos a agentes de soporte, han realizado preguntas específicas o han completado ciertas acciones.
- Preguntar a tus consumidores por sus intereses, preferencias, datos demográficos, etc. Actualiza automáticamente tu perfil en Braze con esta nueva información mediante atributos personalizados.

## Integración

Para integrar Braze y Ada, primero debes configurar la aplicación Braze en tu dashboard de Ada y trabajar con tu equipo de Ada para configurar una metavariable de ID de usuario en tu script de incrustación de Ada. A continuación, arrastra el bloque Braze al editor de respuestas donde desees enviar información a Braze, ya sea un evento o un atributo.

### Paso 1: Configurar la aplicación Braze en Ada

En el panel de Ada, ve a **Configuración > Integraciones > Traspaso de integraciones**.

Junto a Braze, haz clic en **Connect** y proporciona la siguiente información:
- **REST Endpoint**: introduce tu URL de punto final de Braze REST. 
- **API Key**: introduce tu clave REST API de Braze. 
- **App ID**: introduce el ID de aplicación con el que desees asociar los chats de Ada.

### Paso 2: Pasar un identificador de Braze a Ada

Para confirmar que estás actualizando el usuario correcto, tendrás que ponerte en contacto con tu equipo de Ada y ellos podrán ayudarte a realizar las modificaciones necesarias en el script de incrustación de Ada para recibir un identificador de Braze. Esta integración está diseñada para aceptar un ID externo, pero es posible pasar otros identificadores, como un alias de usuario. 

### Paso 3: Coloca el bloque Braze en las respuestas correspondientes

Para utilizar el bloque Braze, arrástralo desde el cajón de bloques a la Respuesta adecuada y selecciona una acción. Con el bloque Braze, puedes realizar dos acciones:
* Seguimiento de eventos
* Actualizar atributo

{% tabs local %}
{% tab seguimiento de eventos %}

#### Bloque de utilidades de respuesta

1. Arrastra el bloque Utilidades de respuesta desde el cajón de bloques hasta su posición, justo encima del bloque Braze. 
2. Selecciona la acción **Formato de fecha** e introduce `today` en el campo **Fecha**.
3. Introduce `iso` en el campo **Formato de salida**. En **Guardar respuesta como variable**, crea una variable para **Fecha con formato** llamada `iso_time`.

![El bloque Utilidades de respuesta con los campos rellenados como se describe en el texto anterior.]({% image_buster /assets/img/ada/ada-braze-2.png %})

#### Bloque Braze

**4\.** En el bloque Braze, introduce la metavariable `external_id` configurada por Ada en el paso anterior en el campo **ID externo**.<br>
**5\.** En el campo **Nombre del evento**, introduce el nombre del evento Braze que deseas rastrear.<br>
**6\.** En el campo **Hora del suceso**, introduce la variable `iso_time` que creaste en el bloque Utilidades de respuesta.<br>
**7\.** Selecciona una respuesta alternativa para que aparezca si se produce un problema al publicar el evento en Braze.

![El bloque Braze con los campos rellenados como se describe en el texto anterior.]({% image_buster /assets/img/ada/ada-braze-3.png %})

{% endtab %}
{% tab actualizar atributo %}

#### Bloque Braze

1. En el bloque Braze, introduce la metavariable `external_id` configurada por Ada en el paso anterior en el campo **ID externo**. 
2. En el campo **Nombre de atributo**, introduce el nombre del atributo Braze que deseas rastrear. 
3. En el campo **Valor del atributo**, introduce el valor que deseas establecer, que puede ser texto, una variable o una combinación de texto y variables. 
4. Selecciona una respuesta alternativa para que aparezca si se produce un problema al publicar el atributo en Braze.

![El bloque Braze con los campos rellenados como se describe en el texto anterior.]({% image_buster /assets/img/ada/ada-braze-4.png %})

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/ada/ada-braze-1.png %}
[3]: {% image_buster /assets/img/ada/ada-braze-2.png %}
[4]: {% image_buster /assets/img/ada/ada-braze-3.png %}
[5]: {% image_buster /assets/img/ada/ada-braze-4.png %}