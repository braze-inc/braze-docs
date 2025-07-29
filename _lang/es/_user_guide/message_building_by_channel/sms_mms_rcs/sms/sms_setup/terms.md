---
page_order: 1
nav_title: Términos que debe conocer
article_title: Términos SMS que debes conocer
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Terms to Know"
glossary_top_text: "SMS–everyone has it and knows what it is. What they don't know is the nuance. Check out the following terms to learn more about SMS ecosystems, technologies, and processes."
page_type: glossary
description: "En este glosario se definen varios términos de SMS que debes conocer."
channel: SMS 

glossaries:
  - name: SMS (Servicio de mensajes cortos)
    description: "Canal de mensajería creado en 1980 y una de las tecnologías de envío de mensajes de texto más antiguas. También es uno de los canales de mensajes de texto más extendidos y utilizados. Este canal es una forma más directa de llegar a sus usuarios y clientes que la mayoría de los demás canales de mensajería, ya que utiliza su número de teléfono personal para ponerse en contacto con ellos. Como tal, el SMS tiene más normas y reglamentos a su alrededor que otros canales de mensajería."
  - name: Código abreviado
    description: Se trata de una secuencia corta y memorable de 5-6 dígitos que permite a los remitentes enviar más mensajes a un ritmo más constante que los números largos (un mensaje por segundo).<br><br>Se requiere un código corto o largo.
  - name: Código largo
    description: Es el número de teléfono estándar de 10 dígitos (en la mayoría de los países) que permite a los remitentes enviar más mensajes a razón de un mensaje por segundo.<br><br>Se requiere un código corto o largo.
  - name: Codificación
    description: La conversión de cualquier cosa en una forma codificada. El contenido de los SMS puede codificarse en GSM-7 o UCS-2.
  - name: Codificación GSM-7 (Sistema Global de Comunicaciones Móviles)
    description: "GSM-7 es la norma de codificación más vista para la mayoría de los mensajes SMS. Utiliza la mayoría de los alfabetos griego e inglés, así como algunos caracteres adicionales. Puede obtener más información sobre la codificación GSM-7 y los conjuntos de caracteres que puede utilizar en <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title=\"Alfabeto predeterminado y tabla de extensiones GSM 7 bitsWikipedia\"></a>. Los idiomas como el chino, el coreano o el japonés deben transferirse utilizando la codificación de caracteres UCS-2 de 16 bits. <br> <br> Puede estimar que el límite de caracteres por segmento para este tipo de codificación es de 128 caracteres."
  - name: Codificación UCS-2 (juego de caracteres codificado universal)
    description: "La codificación UCS-2 es una norma de codificación alternativa, sobre todo cuando un mensaje no puede codificarse con GSM-7 o cuando un idioma necesita más de 128 caracteres para ser representado. El USC-2 se mide mejor por <a href='https://en.wikipedia.org/wiki/Code_point'>puntos de código</a> que por \"caracteres\". En cualquier caso, se podría estimar que el límite de caracteres por segmento para este tipo de codificación es de 67 caracteres."
  - name: Grupos de suscripción para SMS
    description: Los grupos de suscripción son una herramienta de Braze que le permite dirigirse a niveles de suscripción específicos de usuarios o clientes. Los grupos de suscripción para SMS se construyen internamente en función de su servicio de mensajes y no pueden compartirse entre espacios de trabajo.
  - name: Segmentos de mensajes
    description: "Un segmento de mensaje es una agrupación de hasta un número definido de caracteres (160 para la codificación GSM-7; 67 para la codificación UCS-2) que se enviarán en un único envío SMS. Si envía un SMS con 161 caracteres utilizando la codificación GSM-7, verá que se han enviado dos (2) segmentos de mensaje. El envío de varios segmentos de mensajes puede dar lugar a cargos adicionales."
  - name: Servicio de mensajes
    description: "Una colección de códigos largos, códigos cortos e identificadores alfanuméricos utilizados para enviar mensajes SMS con Braze."
  - name: Palabra clave
    description: "Palabra corta que se envía a un código corto o largo para interactuar con un programa SMS predefinido o para solicitar la OPCIÓN DE SALIR de un programa específico o de todos los programas de un código. Por ejemplo, <code>STOP</code>. Las palabras clave deben reunir estos requisitos: <br> - ser alfanuméricas <br> - no contener espacios <br> - contener menos de 10 caracteres <br> <br> Una combinación específica de palabra clave y código corto sólo puede utilizarse en un programa activo a la vez. Si se introduce una palabra clave que ya está siendo utilizada por otro programa, aparecerá un error de validación. <br> <br> Hay dos categorías de palabras clave obligatorias que todos los proveedores de contenidos SMS deben cumplir: <code>STOP</code> y <code>HELP</code>."
  - name: Palabra clave obligatoria AYUDA
    description: "Para cada programa que se crea en la plataforma SMS Campaign Manager, se debe proporcionar el contenido para esta palabra clave y tiene que cumplir con las mejores prácticas y el cumplimiento del operador por país o región en la que se envía y recibe el tráfico de SMS. En la mayoría de los casos, este contenido debe incluir una breve explicación del programa SMS y de cómo OPTAR POR EL MISMO."
  - name: Palabras clave globales STOP
    description: "Las variaciones incluyen <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>. Se denominan <code>Global-Stop-Keywords</code>. Si se escribe cualquiera de estas palabras clave en un código corto o largo, el número de móvil (el número de teléfono móvil de origen) queda excluido de todos los programas de SMS activos en ese código al que está asociado."
  - name: Código Vanity
    description: Un código corto personalizado es un número de teléfono de 5-6 dígitos seleccionado específicamente por una marca. Los códigos cortos de vanidad son de marca y más fáciles de recordar para los consumidores.
  - name: Código corto compartido
    description: "Cuando se utiliza un código corto compartido, todos los mensajes de texto, independientemente de la empresa u organización que los envíe, llegan al dispositivo móvil del consumidor desde el mismo número de teléfono 5-6. Aunque los códigos cortos compartidos tienen un coste relativamente bajo y están disponibles de inmediato, esto significa que su empresa no tendrá un código corto exclusivo y estará sujeta a que otras empresas sigan el protocolo correcto con su código corto compartido." 
  - name: ID alfanumérico del remitente
    description: El ID de remitente alfanumérico le permite establecer el nombre de su empresa o marca como ID de remitente utilizando caracteres alfanuméricos al enviar mensajes unidireccionales a los países admitidos.
  - name: Número gratuito
    description: "Un número de teléfono gratuito o de llamada gratuita es un número de teléfono al que se facturan todas las llamadas entrantes en lugar de cobrarlas al suscriptor telefónico de origen. Los números gratuitos de EE.UU. y Canadá están habilitados para SMS, por lo que se cobra a los abonados por los mensajes entrantes y salientes.<br><br>La mensajería gratuita funciona mejor cuando su caso de uso es de persona a persona, como la atención al cliente o las ventas, y tanto el remitente como el destinatario mantienen una conversación a través de texto."
  - name: Mensajería unidireccional
    description: La mensajería unidireccional le permite comunicarse con sus clientes mediante el envío de mensajes de texto. La mensajería unidireccional es útil si está implementando un ID de remitente alfanumérico en mercados donde los códigos largos y cortos no están disponibles. 
  - name: Mensajería bidireccional
    description: La mensajería bidireccional te permite mantener una conversación enviando y recibiendo mensajes de texto. 
---
