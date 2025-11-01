---
nav_title: "A2P 10DLC"
article_title: A2P 10DLC
page_order: 2.9
description: "Este artículo trata sobre la 10DLC A2P, por qué es necesario el registro 10DLC para los clientes de código largo de EE.UU., información útil sobre costes y rendimiento, y cómo empezar con el registro."
page_type: reference
channel:
  - SMS
  
---

# Aplicación-a-Persona Códigos largos de 10 dígitos

> A2P 10DLC hace referencia a un sistema de Estados Unidos que permite a las empresas enviar mensajería del tipo Aplicación a Persona (A2P) a través de un número de teléfono estándar de código largo de 10 dígitos (10DLC). A estos códigos largos registrados se les concede un mayor rendimiento, una mejor capacidad de entrega y un mejor cumplimiento que al código largo estándar.

{% alert important %}
Todos los clientes que actualmente tienen y/o utilizan códigos largos de EE.UU. para enviar a clientes de EE.UU. deben registrar sus códigos largos para 10DLC; los que no lo hagan experimentarán un fuerte filtrado de todos los mensajes. Este proceso de solicitud tarda entre 4 y 6 semanas.
{% endalert %}

## Por qué es necesario

El servicio 10DLC se creó para facilitar específicamente la mensajería A2P utilizando códigos largos. Históricamente, los códigos largos estaban pensados para la mensajería de Persona a Persona (P2P), pero cuando se utilizaban por motivos de marketing, hacían que las empresas se vieran constreñidas por un rendimiento limitado y un mayor filtrado. 

10DLC ayuda a aliviar esos problemas ofreciendo: 
- **Mayor rendimiento**: Los números 10DLC admiten un mayor volumen de mensajes que los códigos largos normales.
- **Mejor capacidad de entrega**: Los números 10DLC están designados para el tráfico A2P, por lo que los mensajes enviados con estos números tienen más probabilidades de llegar al destinatario y es menos probable que el operador los filtre o rechace que los mensajes enviados a través de códigos largos locales normales. 
- **Mejora del cumplimiento**: Utilizar un código largo local para la mensajería de texto comercial es contrario a las directrices [de la CTIA](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf). Los números 10DLC se designaron para la mensajería masiva y permiten a las marcas cumplir la normativa del sector sin depender de códigos abreviados.
- **Presupuesto asequible**: 10DLC es una gran opción para las empresas que quieren empezar a enviar SMS o enviar SMS en pequeños volúmenes. Para las marcas que envían grandes volúmenes de mensajería, de más de 100.000 mensajes al día, recomendamos utilizar un código abreviado. 

Desde 2019, los operadores han empezado a adoptar 10DLC para la mensajería comercial: Verizon y AT&T son actualmente compatibles con 10DLC, y esperamos que pronto lo hagan todos los operadores importantes. Aunque puede causar inconvenientes a corto plazo, a largo plazo los clientes disfrutarán de mejores tasas de capacidad de entrega, al tiempo que protegen a sus consumidores de mensajes no deseados. 

## Lo que debes saber

### Accede a

El registro de códigos largos con A2P 10DLC tardará entre 4 y 6 semanas.

### Costes 

El registro en A2P 10DLC puede incluir varios tipos de tasas:

| Tipo de tasa | Descripción |
| -------- | ---------- |
| Tasas de inscripción | Se aplican tasas nominales al registrar tu marca y tu caso de uso en las principales redes de EE.UU. |
| Tasas de examen secundario | Las marcas pueden apelar su [puntuación de confianza en la marca](#trust-score) y solicitar un proceso de investigación secundario para mejorar su rendimiento general; este proceso conlleva una tasa. |
| Tasas del operador | Tarifas cobradas por los operadores por los mensajes SMS y MMS salientes enviados a los usuarios tras el registro en 10DLC. A partir del 1 de octubre de 2021, las tasas de los operadores serán más elevadas para el tráfico no registrado (códigos largos estándar) que para el tráfico registrado (10DLC). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Visita el artículo sobre Twilio 10DLC para consultar las [estimaciones](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-) actualizadas [de las tarifas](https://support.twilio.com/hc/en-us/articles/1260803965530-What-pricing-and-fees-are-associated-with-the-A2P-10DLC-service-).

### Rendimiento

El rendimiento de los mensajes de tu 10DLC depende de varios factores, como la puntuación de confianza de la marca, los límites diarios de mensajes y tus casos de uso de la mensajería.

#### Puntuación de confianza en la marca {#trust-score}

El Registro de Campañas (TCR) es una agencia externa que utiliza un algoritmo de reputación para revisar criterios específicos relacionados con tu empresa y asignar una puntuación de confianza que determina el rendimiento de la mensajería de cada marca. Esta puntuación de confianza se asignará cuando un cliente se registre para recibir mensajería US 10DLC. Cuanto mayor sea la puntuación de confianza, mejor será la experiencia de mensajes por segundo (MPS). 

|     | Puntuación de confianza | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| Alta | 75-100 | 75 MPS | 75 MPS | 75 MPS |
| Medio | 50-74 | 40 MPS | 40 MPS | 40 MPS |
| Baja | 1-49 | 4 MPS | 4 MPS | 4 MPS | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert tip %}
Las empresas incluidas en el Índice Russel 3000 obtendrán un alto rendimiento y una puntuación de confianza en la marca tras el registro y la revisión de 10DLC.
{% endalert %} 

#### Límites de mensajes diarios

Los límites diarios van de 2.000 a 200.000 mensajes, en función de la puntuación de confianza de tu marca, y se aplican a todos los códigos largos. Aunque las puntuaciones de confianza de marca elevadas conllevan un rendimiento de 60 mensajes por segundo, se seguirán aplicando los límites de mensajes diarios establecidos por el operador. Esto significa que los códigos abreviados serían una mejor opción si el pico diario de mensajes de una marca es superior al límite diario impuesto. 

#### Casos de uso de la mensajería

El rendimiento también se ve afectado por el tipo de caso de uso de mensajería que elijas. La mayoría de los clientes entrarán en el caso de uso de marketing estándar o mixto. Otros casos de uso menos comunes serán susceptibles de valores de rendimiento diferentes.

Dependiendo de tu caso de uso, la puntuación de confianza necesaria para conseguir el máximo rendimiento variará. Las tablas siguientes enumeran casos de uso estándar y rangos de puntuación de confianza de casos de uso común. Para casos de uso especiales, como servicios de emergencia o caridad, consulta [la documentación de Twilio](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US).

| Casos de uso estándar | Descripción |
| ------------------ | ----------- |
| Marketing | Contenido promocional, como rebajas y ofertas por tiempo limitado. |
| Mixto | Campaña que cubre múltiples casos de uso, como la Atención al Cliente. | 
| Educación Superior | Campañas para instituciones de enseñanza superior. |
| Colegio electoral & Votar | Encuestas y votaciones no políticas, como cuestionarios a clientes. |
| PSA | Anuncios de servicio público para sensibilizar sobre un tema determinado. |
| Atención al cliente | Asistencia, administración de cuentas y otras interacciones con los clientes. |
| Notificaciones de entrega | Estado de los mensajes de entrega. |
| Notificaciones de la cuenta | Notificaciones sobre el estado de una cuenta. |
| 2FA | Cualquier autenticación de verificación de cuenta, como OTP. | 
| Alertas de seguridad | Notificación de un sistema comprometido. |
| Alertas de fraude | Mensajería sobre actividades potencialmente fraudulentas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% tabs %}
{% tab Declared Use Case %}
Un caso de uso declarado significa que has elegido un caso de uso específico no relacionado con el marketing (por ejemplo, 2FA o Notificaciones de cuenta).

| Puntuación de confianza | Rendimiento total hacia las principales redes de EE.UU. | AT&T | T-Mobile | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74	 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% tab Mixed Marketing Use Case %}

Se pueden registrar casos de uso de marketing mixto para clientes que quieran enviar mensajes para varios casos de uso desde el mismo conjunto de números o para marketing.

| Puntuación de confianza | Rendimiento total hacia las principales redes de EE.UU. | AT&T | T-Mobile  | Verizon |
| --- | ----------- | ---- | -------- | ------- |
| 75-100 | 225 MPS | 75 MPS | 75 MPS | 75 MPS |
| 50-74 | 120 MPS | 40 MPS | 40 MPS | 40 MPS |
| 1-49 | 12 MPS | 4 MPS | 4 MPS | 4 MPS| 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% endtab %}
{% endtabs %}

Visita el artículo sobre Twilio 10DLC para consultar las [estimaciones de rendimiento](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) actualizadas.

## Próximos pasos

Los clientes que aún no se hayan registrado en 10DLC deben trabajar con su administrador del éxito del cliente para registrar sus códigos largos. **Si los clientes no registran sus códigos largos, a partir del 1 de octubre de 2021, cualquier remitente A2P que utilice códigos largos experimentará un fuerte filtrado de todos los mensajes.** Ponte en contacto con tu administrador del éxito del cliente para empezar a registrarte en 10DLC. 
