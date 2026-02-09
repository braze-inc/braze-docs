---
nav_title: Lemnisk
article_title: Integrar Lemnisk con Braze
description: "Este artículo de referencia detalla la asociación entre Braze y Lemnisk, una plataforma de datos de clientes basada en IA y dirigida a la Automatización del Marketing, que te permite transmitir datos de usuario recopilados en Lemnisk desde varias fuentes, a Braze para activarlos en varios canales y destinos utilizando las herramientas de Braze."
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/) es una solución de automatización del marketing y una plataforma de datos de clientes (CDP) impulsada por IA que habilita la captura, unificación y activación en tiempo real de datos de clientes procedentes de fuentes diversas y aisladas. Entrega sin problemas estos datos unificados a través de varias plataformas MarTech y empresariales, al tiempo que ofrece un sólido análisis en tiempo real para hacer un seguimiento de cada etapa del ciclo de vida de los datos de los clientes. 

_Esta integración está mantenida por Lemnisk._

## Sobre la integración

La integración de Lemnisk y Braze permite a las marcas y empresas liberar todo el potencial de Braze actuando como una capa de inteligencia dirigida por CDP que unifica los datos de usuario en todas las plataformas en tiempo real, y enviando la información y los comportamientos del usuario recopilados a Braze en tiempo real. Lemnisk entrega perfiles de cliente enriquecidos directamente en Braze, combinando señales de comportamiento y atributos personales que te permiten personalizar tu mensajería con un contexto más profundo.

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuentas Lemnisk | Se necesita una cuenta [Lemnisk](https://www.lemnisk.co/) para beneficiarse de esta asociación. |
| API externa en Lemnisk | Ponte en contacto con tu CSM de Lemnisk para habilitar **la API externa** para tu cuenta. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permiso de `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu cuenta]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints#api-and-sdk-endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Integración de Lemnisk

### Paso 1: Crear una API externa Braze {#create-a-braze-external-api}

En Lemnisk, ve al canal API Externa. Selecciona **Añadir nueva API externa**. Ahora configuraremos el punto final [Seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track) como una API externa.

![Iniciar el proceso de creación de la API Externa en Lemnisk]({% image_buster /assets/img/lemnisk/open_external_api.png %})

En **Detalles básicos**, introduce un nombre, una descripción, un canal y un identificador de canal.

![Introducir detalles básicos de configuración para una nueva API Externa en Lemnisk]({% image_buster /assets/img/lemnisk/ext_api_basic_details.png %})

En **Detalles de la API externa**, introduce los detalles relevantes de tu punto final `users.track`. Puedes definir varios campos a nivel de interacción utilizando {% raw %}`{{}}`{% endraw %}, lo que te permite establecer valores distintos para campañas diferentes.

![Rellenar el punto final de la API externa y los detalles de la carga útil]({% image_buster /assets/img/lemnisk/ext_api_ext_api_details.png %})

Para finalizar la configuración del Seguimiento de usuarios, selecciona **Guardar**. Se te redirigirá automáticamente a la página de **la API de prueba**.

### Paso 2: Prueba la configuración

En la página **Probar API**, introduce algunos valores de prueba para los parámetros de la API en tu vista de árbol JSON y, a continuación, selecciona **Probar configuración**.

Si tus credenciales y las definiciones de la API son correctas, Braze te devolverá una respuesta satisfactoria.

![Probar la configuración de una API externa con una carga útil de muestra y una respuesta satisfactoria]({% image_buster /assets/img/lemnisk/test_ext_api.png %})

A continuación, comprobarás que tus eventos se envían a Braze correctamente. En el panel de Braze, ve a **Audiencia** > **Buscar usuarios** y, a continuación, introduce uno de los identificadores de tu configuración de API externa (como una dirección de correo electrónico de usuario). Si todo funciona correctamente, aparecerá en la lista el perfil que recibió tu desencadenador de API de prueba.

![Ver el perfil de un usuario y un resumen de su actividad en Braze]({% image_buster /assets/img/lemnisk/braze_cov.png %})

### Paso 3: Desencadenar eventos de usuario en Braze

1. En Lemnisk, crea un nuevo segmento. Por ejemplo, puedes crear un segmento que envíe información a Braze en cuanto los usuarios envíen un formulario de captación de clientes potenciales.
2. En tu nuevo segmento, ve a **API externa** > **Añadir interacción**.
3. En **Creación de interacciones**, introduce los datos básicos y selecciona la configuración [que creaste anteriormente](#create-a-braze-external-api).
4. En **Configurar parámetros**, encontrarás las entradas de los parámetros Braze que hayas decidido exponer a nivel de interacción. En el siguiente ejemplo, muestra _el Nombre del usuario_, el _ID del producto_ y la _Hora del evento_.
    ![Crear una interacción para enviar datos de usuario a Braze]({% image_buster /assets/img/lemnisk/create_an_engagement.png %})
5. Introduce las variables de personalización pertinentes para los parámetros que hayamos elegido y, a continuación, selecciona **Guardar**.
6. Cuando hayas terminado, activa la interacción.
