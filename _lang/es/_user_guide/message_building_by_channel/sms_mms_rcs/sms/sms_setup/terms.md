---
page_order: 1
nav_title: Términos que debes conocer
article_title: Términos SMS que debes conocer
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Terms to Know"
glossary_top_text: "SMS–everyone has it and knows what it is. What they don't know is the nuance. Check out the following terms to learn more about SMS ecosystems, technologies, and processes."
page_type: glossary
description: "Este glosario define varios términos SMS que debes conocer."
channel: SMS 

glossaries:
  - name: SMS (Servicio de mensajes cortos)
    description: "Un canal de mensajería creado en 1980 y una de las tecnologías de envío de mensajes de texto más antiguas. También es uno de los canales de mensajes de texto más extendidos y utilizados. Este canal es una forma más directa de llegar a tus usuarios y clientes que la mayoría de los demás canales de mensajería, ya que utiliza su número de teléfono personal para llegar a ellos. Como tal, el SMS tiene más normas y regulaciones a su alrededor que otros canales de mensajería."
  - name: Código abreviado
    description: Se trata de una secuencia corta y memorable de 5-6 dígitos que permite a los remitentes enviar más mensajes a tasas más constantes que los números largos (un mensaje por segundo).<br><br>Se requiere un código abreviado o un código largo.
  - name: Código largo
    description: Es el número de teléfono estándar de 10 dígitos (en la mayoría de los países) que permite a los remitentes enviar más mensajes a la tasa de un mensaje por segundo.<br><br>Se requiere un código abreviado o un código largo.
  - name: Codificación
    description: La conversión de cualquier cosa en una forma codificada. El contenido del SMS puede codificarse en GSM-7 o UCS-2.
  - name: Codificación GSM-7 (Sistema Global de Comunicaciones Móviles)
    description: "GSM-7 es la norma de codificación más vista para la mayoría de los mensajes de mensajería SMS. Utiliza la mayoría de los alfabetos griego e inglés, así como algunos caracteres adicionales. Puedes obtener más información sobre la codificación GSM-7 y los conjuntos de caracteres que puedes utilizar en <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title=\"Alfabeto predeterminado y tabla de extensiones GSM 7 bitsWikipedia\"></a>. Las lenguas como el chino, el coreano o el japonés deben transferirse utilizando la codificación de caracteres UCS-2 de 16 bits. <br> <br> Puedes estimar que el límite de caracteres por segmento para este tipo de codificación es de 128 caracteres."
  - name: Codificación UCS-2 (Conjunto Universal de Caracteres Codificados)
    description: "La codificación UCS-2 es una norma de codificación alternativa, especialmente cuando un mensaje no puede codificarse utilizando GSM-7 o cuando un idioma necesita más de 128 caracteres para ser representado. El USC-2 se mide mejor por <a href='https://en.wikipedia.org/wiki/Code_point'>puntos de código</a>, en lugar de por \"caracteres\". En cualquier caso, podrías estimar que el límite de caracteres por segmento para este tipo de codificación es de 67 caracteres."
  - name: Grupos de suscripción para SMS
    description: Los grupos de suscripción son una herramienta de Braze que te permite dirigirte a niveles específicos de suscripción de usuarios o clientes. Los grupos de suscripción para SMS se construyen internamente en función de tu servicio de mensajería y no pueden compartirse entre espacios de trabajo.
  - name: Segmentos de mensajes
    description: "Un segmento del mensaje es una agrupación de hasta un número definido de caracteres (160 para la codificación GSM-7; 67 para la codificación UCS-2) que se enviarán en un único envío SMS. Si envías un SMS con 161 caracteres utilizando la codificación GSM-7, verás que se han enviado dos (2) segmentos del mensaje. El envío de varios segmentos del mensaje puede conllevar gastos adicionales."
  - name: Servicio de mensajería
    description: "Una colección de códigos largos, códigos abreviados e ID alfanuméricos utilizados para enviar tu mensaje SMS con Braze."
  - name: Palabra clave
    description: "Palabra corta que se envía a un código corto o largo para interactuar con un programa SMS predefinido o para solicitar la OPCIÓN DE SALIR de un programa específico o de todos los programas de un código. Por ejemplo, <code>STOP</code>. Palabras clave <br> - ser alfanumérico <br> - no tienen espacios <br> - ser inferior a 10 caracteres. <br> <br> Una combinación específica de palabra clave y código abreviado sólo puede utilizarse en un programa activo a la vez. Si se introduce una palabra clave que ya está siendo utilizada por otro programa, aparecerá un error de validación. <br> <br> Hay dos categorías de palabras clave obligatorias que todos los proveedores de SMS deben cumplir: <code>PARA</code> y <code>AYUDA</code>."
  - name: Palabra clave obligatoria AYUDA
    description: "Para cada programa que se cree en la plataforma del Administrador de Campañas SMS, debe proporcionarse el contenido para esta palabra clave y tiene que cumplir las mejores prácticas y la conformidad del operador por país o región en la que se envía y recibe el tráfico de SMS. En la mayoría de los casos, este contenido debe contener una breve explicación del programa SMS y de cómo OPTAR POR NO PARTICIPAR."
  - name: Palabras clave globales STOP
    description: "Las variaciones incluyen <code>DETENER</code>, <code>TERMINAR</code>, <code>RENUNCIAR</code>, <code>DESUSCRIBIRSE</code>, <code>CANCELAR</code>, <code>STOPALL</code>. Se denominan <code>Palabras Clave de Parada Global</code>. Si se escribe cualquiera de estas palabras clave en un código abreviado o largo, el número de móvil (el número de teléfono móvil de origen) queda excluido de todos los programas de SMS activos en ese código al que está asociado."
  - name: Código de vanidad
    description: Un código abreviado personalizado es un número de teléfono de 5-6 dígitos seleccionado específicamente por una marca. Los códigos abreviados de marca son más fáciles de recordar para los consumidores.
  - name: Código abreviado compartido
    description: "Cuando se utiliza un código abreviado compartido, todos los mensajes de texto, independientemente de la empresa u organización que los envíe, llegan al dispositivo móvil del consumidor desde el mismo número de teléfono 5-6. Aunque los códigos abreviados compartidos tienen un coste relativamente bajo y están disponibles de inmediato, esto significa que tu empresa no tendrá un código abreviado exclusivo, y estará sujeta a que otras empresas sigan el protocolo correcto con tu código abreviado compartido." 
  - name: ID alfanumérico del remitente
    description: El ID de remitente alfanumérico te permite establecer el nombre de tu empresa o marca como ID de remitente utilizando caracteres alfanuméricos al enviar mensajes unidireccionales a los países admitidos.
  - name: Número gratuito
    description: "Un número de teléfono gratuito o de llamada gratuita es un número de teléfono al que se facturan todas las llamadas entrantes en lugar de cobrarlas al suscriptor telefónico de origen. Los números gratuitos de EE.UU. y Canadá están habilitados para SMS, en los que se cobra a los suscriptores por los mensajes entrantes y salientes.<br><br>La mensajería gratuita funciona mejor cuando tu caso de uso es de persona a persona, como la atención al cliente o las ventas, y tanto el remitente como el destinatario mantienen una conversación por texto."
  - name: Mensajería unidireccional
    description: La mensajería unidireccional te permite comunicarte con tus clientes mediante el envío de mensajes de texto. La mensajería unidireccional es útil si estás implementando un ID de remitente alfanumérico en mercados donde los códigos largos y abreviados no están disponibles. 
  - name: Mensajería bidireccional
    description: La mensajería bidireccional te permite mantener una conversación enviando y recibiendo mensajes de texto. 
---
