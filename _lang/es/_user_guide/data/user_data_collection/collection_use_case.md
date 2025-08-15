---
nav_title: Caso de uso de la recopilación
article_title: Caso de uso de la recopilación
page_order: 3
page_type: reference
description: "Este artículo de referencia trata un caso de uso de recopilación de datos de usuario sobre cómo una aplicación de transporte compartido puede decidir qué datos de usuario recopilar."

---

# Caso de uso de la recopilación

> Este artículo trata un caso de uso de recopilación de datos de usuario sobre cómo una aplicación de transporte compartido podría decidir qué datos de usuario recopilar.

Supongamos que una aplicación de transporte compartido, llamada StyleRyde, quiere decidir qué datos de usuario recopilar. Las siguientes preguntas y el proceso de lluvia de ideas son un gran modelo a seguir por sus equipos de marketing y desarrollo. Al final de este ejercicio, ambos equipos deberían tener una sólida comprensión de qué eventos y atributos personalizados tiene sentido recopilar para ayudar a cumplir su objetivo.

## Pregunta del caso 1: ¿Cuál es el objetivo?

El objetivo de StyleRyde es sencillo: quieren que los usuarios llamen a taxis a través de su aplicación.

## Pregunta del caso 2: ¿Cuáles son los pasos para alcanzar ese objetivo tras la instalación de la aplicación?

1. StyleRyde necesita que los usuarios inicien el proceso de registro y rellenen sus datos personales.
2. StyleRyde necesita que los usuarios completen y verifiquen el proceso de registro introduciendo un código en la aplicación que reciben a través de SMS.
3. StyleRyde necesita que los usuarios intenten llamar a un taxi.
4. StyleRyde tiene que estar disponible cuando los usuarios llamen a un taxi.

Estas acciones podrían entonces etiquetarse como los siguientes eventos personalizados:

- Inicio de la inscripción
- Registro completo
- Llamadas de taxi con éxito
- Llamadas de taxi fallidas

Una vez implementados los eventos, StyleRyde puede realizar campañas como las siguientes:

1. Envía mensajes a los usuarios que iniciaron el registro pero no lo han completado en un plazo determinado.
2. Enviar mensajes de felicitación a los usuarios que hayan completado el registro.
3. Enviar disculpas y crédito promocional a los usuarios que hayan tenido llamadas de taxi fallidas, que no hayan sido seguidas por una llamada de taxi exitosa dentro de un cierto período de tiempo.
4. Envíe promociones a los usuarios con más llamadas de taxi realizadas con éxito para agradecerles su fidelidad.

## Pregunta del caso 3: ¿Qué otra información sobre el usuario podríamos recopilar y utilizar para informar nuestra mensajería?

- ¿Si los usuarios tienen algún crédito promocional?
- ¿Cuál es la tasa media que los usuarios dan a sus conductores?
- ¿Códigos promocionales únicos para usuarios?

Estas características podrían etiquetarse como los siguientes atributos personalizados:

- Saldo de crédito promocional (tipo decimal)
- Clasificación promedio de los conductores (tipo de número entero)
- Código promocional único (tipo cadena)

Estos atributos te permiten enviar campañas a usuarios como:

1. Recordar a los usuarios que no han utilizado la aplicación en siete días y tienen crédito promocional en su cuenta que vuelvan a la aplicación y utilicen el crédito.
2. Utilizar nuestras plantillas de mensajes y [funciones de personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/#personalized-messaging) para arrastrar el atributo de código promocional único a los mensajes dirigidos a los usuarios.

{% alert important %}
Braze prohibirá o bloqueará a los usuarios ("usuarios ficticios") con más de 5.000.000 de sesiones y dejará de ingerir sus eventos SDK porque suelen ser el resultado de una mala integración. Si descubre que esto le ha ocurrido a un usuario legítimo, póngase en contacto con su gestor de cuenta Braze.
{% endalert %}

