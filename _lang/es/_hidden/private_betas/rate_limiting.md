---
article_title: Limitación de tasa para campañas y lonas
permalink: /rate_limiting/
page_type: reference
description: "Este artículo de referencia describe el comportamiento anterior de la tasa límite de velocidad de entrega de Braze."
---

# Limitación de velocidad

> Este artículo describe el comportamiento anterior de la tasa límite de velocidad de entrega de Braze. [Aquí]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#rate-limiting) se describe el comportamiento actualizado del límite de velocidad.

Braze te permite controlar la presión del marketing limitando la tasa de tus campañas y Canvases, regulando la cantidad de tráfico saliente de tu plataforma. Puedes implementar dos tipos diferentes de límite de velocidad para tus campañas:

1. **El límite de tasa de velocidad de entrega** tiene en cuenta el ancho de banda de tus servidores.
2. **El límite de velocidad centrado en el** usuario se centra en proporcionar la mejor experiencia al usuario. 

Para más información, consulta [Acerca del límite de velocidad]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#about-rate-limiting).

## Acerca de la limitación de la tasa de velocidad de entrega

Si prevés que las grandes campañas provoquen un aumento de la actividad de los usuarios y sobrecarguen tus servidores, puedes especificar un límite de velocidad por minuto para el envío de mensajes: esto significa que Braze no enviará más mensajes que el límite de velocidad establecido en un minuto. 

Al dirigirte a los usuarios durante la creación de la campaña, puedes navegar a **Audiencias objetivo** (para campañas) o a **Configuración de envío** (para Canvas) para seleccionar un límite de velocidad de entrega de mensajes (en varios incrementos, desde un mínimo de 10 hasta un máximo de 500.000 mensajes por minuto). Ten en cuenta que las campañas sin tasa limitada pueden superar estos límites de entrega.

Por ejemplo, si intentas enviar 75.000 mensajes con un límite de tasa de 10.000 por minuto, la entrega se repartirá en ocho minutos. Tu campaña no entregará más de 10.000 mensajes durante cada uno de los primeros siete minutos, y 5.000 mensajes durante el último minuto. 

### Consideraciones

Los mensajes enviados utilizando un límite de velocidad no tendrán la configuración del límite de velocidad (como 10.000 por minuto) enviada uniformemente a lo largo de 60 segundos. En su lugar, Braze se asegura de que no se envíen más de 10.000 mensajes por minuto (esto podría significar que un mayor porcentaje de los 10.000 mensajes se envíen en el primer medio minuto frente al último medio minuto). 

Ten cuidado con retrasar los mensajes sensibles al tiempo con esta forma de límite de tasa. Si la audiencia del mensaje contiene 30 millones de usuarios, pero fijamos el límite de velocidad en 10.000 por minuto, una gran parte de tu base de usuarios no recibirá el mensaje hasta el día siguiente. 

Ten en cuenta que los mensajes se cancelarán si se retrasan 72 horas o más debido a un límite de velocidad bajo. El usuario que creó la campaña recibirá alertas en el panel y por correo electrónico si el límite de velocidad es demasiado bajo.

## Limitación de la tasa de velocidad de entrega de las campañas

### Campañas monocanal

Al enviar una campaña monocanal con un límite de velocidad de entrega, el límite de velocidad se aplica a todos los mensajes juntos. Por ejemplo, una campaña de correo electrónico con un límite de velocidad de 10.000 mensajes por minuto enviará un máximo de 10.000 mensajes totales por minuto.


| Máximo de envíos de correo electrónico por minuto | Máximo total de mensajes enviados por minuto |
|--------------------------------|----------------------------------------|
| 10,000                         | 10,000                                 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Campañas multicanal

Al enviar una campaña multicanal con un límite de velocidad, cada canal se envía independientemente de los demás. Como consecuencia de ello, puede ocurrir lo siguiente:

- El número total de mensajes enviados por minuto podría ser superior al límite de velocidad. Por ejemplo, si tu campaña tiene un límite de velocidad de 10.000 por minuto y utiliza correo electrónico y SMS, Braze puede enviar un máximo de 20.000 mensajes en total cada minuto (10.000 por correo electrónico y 10.000 por webhooks).

| Máximo de envíos de correo electrónico por minuto | Máximo de mensajes SMS enviados por minuto | Máximo total de mensajes enviados por minuto |
|--------------------------------|--------------------------------------|----------------------------------------|
| 10,000                         | 10,000                               | 20,000                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

- Los usuarios podrían recibir los distintos canales en momentos diferentes, y no es necesariamente predecible qué canal recibirán primero. 

Por ejemplo, si envías una campaña que contiene correo electrónico y SMS, puede que tengas 10.000 usuarios con números de teléfono válidos, pero 50.000 usuarios con direcciones de correo electrónico válidas. Si configuras la campaña para enviar 100 mensajes por minuto (un límite de tasa lento para el tamaño de la campaña), un usuario podría recibir el SMS en el primer lote de envíos y el correo electrónico en el último lote de envíos, casi nueve horas después.

### Campañas push multiplataforma

Para las campañas push que se entregan en varias plataformas, el límite de velocidad seleccionado se distribuirá equitativamente entre las plataformas. Una campaña de mensajería push que aproveche Android e iOS con un límite de tasa de 10.000 por minuto distribuirá equitativamente los 10.000 mensajes entre las dos plataformas.

| Máximo de notificaciones de Android enviadas por minuto | Máximo de notificaciones push de iOS enviadas por minuto | Máximo total de notificaciones push enviadas por minuto |
|--------------------------------|--------------------------------------|----------------------------------------|
| 10,000                         | 10,000                               | 10,000                                 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Limitación de la tasa de velocidad de entrega de Canvas

Al enviar un Canvas con un límite de velocidad, cada canal se envía independientemente de los demás. Como consecuencia de ello, puede ocurrir lo siguiente:

- El número total de mensajes enviados por minuto podría ser superior al límite de velocidad. 
    - Por ejemplo, si tu Canvas tiene un límite de velocidad de 10.000 por minuto y utiliza correo electrónico y mensajes dentro de la aplicación, Braze puede enviar hasta 20.000 mensajes en total cada minuto (10.000 por correo electrónico y 10.000 dentro de la aplicación).

- Los límites de velocidad pueden afectar al orden en que los usuarios reciben los mensajes en un Canvas. 
    - Por ejemplo, si envías un Canvas que contiene correos electrónicos y notificaciones push a 50.000 usuarios, puede ocurrir que los 50.000 tengan direcciones de correo electrónico válidas, pero sólo 10.000 usuarios tengan tokens de notificaciones push válidos. En este caso, si configuras el Canvas para que envíe 1.000 mensajes por minuto y hay un paso en Canvas multicanal que contiene tanto correo electrónico como push, es posible que un usuario pueda avanzar al siguiente paso en Canvas (y ser elegible para recibir este siguiente paso) tras haber recibido sólo la notificación push, pero aún no el correo electrónico. 

## Resumen del comportamiento anterior y nuevo del límite de velocidad

Tu cuenta Braze está utilizando actualmente el comportamiento anterior de limitación de tasa de velocidad de entrega. La información que aparece a continuación detalla la diferencia general entre el comportamiento anterior y el nuevo del límite de velocidad de entrega:

- **Campañas monocanal y lonas:** Los límites de velocidad se aplicarán siempre a todos los mensajes juntos.
- **Campañas multicanal y Canvases (incluyendo push multiplataforma):**


<style>
table td {
    word-break: normal;
}
</style>

<table>
  <tr>
    <th></th>
    <th><b>Campañas</b></th>
    <th><b>Canvas</b></th>
  </tr>
  <tr>
    <td><b>Anterior</b></td>
    <td>Se aplica a cada canal por separado, y las plataformas push* comparten el límite colectivamente</td>
    <td>Se aplica a cada canal por separado, y las plataformas push* comparten el límite colectivamente</td>
  </tr>
  <tr>
    <td><b>Nuevo</b></td>
    <td>Se aplica por separado por canal y plataforma push</td>
    <td>Compartido colectivamente</td>
  </tr>
</table>

_\*Las plataformas push incluyen: Android, iOS, Web push y Kindle._