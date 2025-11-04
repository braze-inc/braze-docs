---
nav_title: "Configuración RCS"
article_title: Configuración RCS
page_order: 1
alias: /rcs_setup/
description: "Este artículo de referencia cubre los requisitos necesarios para poner en marcha RCS."
page_type: reference
channel:
  - RCS
---

# Configuración de RCS

> Este artículo cubre los requisitos necesarios para poner en marcha tu canal RCS.

Configurar RCS es tan sencillo como configurar SMS. Sigue leyendo para saber cómo puedes empezar a enviar mensajes ricos e interactivos.

## Paso 1: Cumplir los criterios de elegibilidad

Para ser elegible para enviar RCS con Braze, tu empresa debe cumplir tres criterios por adelantado:

1. Tu contrato Braze actual debe incluir Créditos de mensajes. 
2. Debes enviar tus mensajes RCS a uno de los siguientes países compatibles con Braze:
- Estados Unidos
- Reino Unido
- Alemania
- México
- Suecia
- España
- Singapur
- Brasil
- Francia
- Italia
- Colombia
3. Debes adquirir un SKU(s) de 0 RCS en tu contrato.

## Paso 2: Registrar un remitente verificado por RCS

Antes de poder enviar mensajes RCS, debes registrar un remitente verificado por RCS. Es la representación de tu marca que los usuarios verán en sus dispositivos móviles, que incluye el nombre de tu marca, el logotipo, una señal de verificación y un eslogan opcional. El remitente verificado por RCS refuerza la confianza del cliente y confirma que tus mensajes proceden de una fuente autenticada. 

\![Un ejemplo de remitente verificado por RCS en un mensaje RCS llamado "Cat Failz Cafe".]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Cuando hayas añadido las SKU de RCS a tu formulario de pedido, Braze recibirá una notificación y se pondrá en contacto contigo para facilitarte la información de registro del remitente de RCS. Su formato dependerá de los países a los que desees enviar mensajes RCS. 

Cuando hayas enviado tus formularios cumplimentados a Braze, completaremos el proceso de inscripción en tu nombre. 

### Paso 2.1: Configurar alternativas de SMS para grupos de suscripción RCS

Como la cobertura actual de los operadores varía según el país, y la compatibilidad del hardware y el software con el usuario varía según el individuo, la alternativa SMS es un componente clave para tener un programa RCS de éxito hoy en día. Recomendamos configurar la alternativa SMS. Si un operador no admite RCS o el dispositivo de un usuario no puede recibir mensajes RCS, SMS fallback enviará tu mensaje a pesar de todo, para que nunca te pierdas un momento importante con tus usuarios.

Te recomendamos encarecidamente que revises tu experiencia actual de adhesión voluntaria por SMS, los grupos de suscripción y la segmentación de la audiencia antes de desplegar tu primera campaña de RCS. Si lo necesitas, tu administrador del éxito del cliente está siempre disponible para orientarte y ayudarte en el proceso de configuración.

### Calendario para la aprobación del operador

El plazo para la aprobación del operador varía según el país y también puede variar dentro de un mismo país. Ten en cuenta que el mercado de RCS aún está en pañales, por lo que los procesos de operadores y agregadores están evolucionando rápidamente. En Estados Unidos, Braze calcula que el plazo de aprobación de un operador para un remitente verificado por RCS suele oscilar entre 4 y 6 semanas, y que un remitente de prueba suele ser aprobado en una semana.

Cuando se apruebe tu remitente verificado por RCS, nuestro equipo de operaciones actualizará tus grupos de suscripción según sea necesario para confirmar que tienen incluido al remitente RCS. 

## Paso 3: Configurar grupos de suscripción

El RCS se suele utilizar de dos formas: 
- Para mejorar el tráfico SMS existente 
- Habilitar nuevos casos de uso que sólo son posibles con la funcionalidad más rica que proporciona RCS.

Dependiendo de tu integración, Braze puede añadir remitentes verificados por RCS a tus grupos de suscripción SMS existentes o configurar nuevos grupos de suscripción para ti. En cualquier caso, tu equipo Braze te guiará a través de una actualización del tráfico SMS sin problemas y conforme a las normas. Para más información, consulta [Grupos de suscripción SMS y RCS]({{site.baseurl}}/sms_rcs_subscription_groups/).

Para nuevos casos de uso que no son posibles con SMS, considera la posibilidad de establecer grupos de suscripción RCS dedicados para alinearlos con los objetivos de tu programa.