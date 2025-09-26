---
nav_title: Stylitics
article_title: Stylitics
description: "Este artículo de referencia describe la asociación entre Braze y Stylitics, una plataforma SaaS basada en la nube que le permite mejorar sus campañas de correo electrónico existentes con contenidos agrupados atractivos y relevantes, creando una experiencia de cliente personalizada."
alias: /partners/stylitics/
page_type: partner
search_tag: Partner

---

# Stylitics

> [Stylitics](https://stylitics.com/) es una plataforma SaaS basada en la nube que permite a los minoristas automatizar y distribuir contenidos visuales a gran escala. Los paquetes de Stylitics inspiran contextualizando los productos, aumentando la confianza en la compra e incrementando la interacción, lo que en última instancia conduce a un mayor valor medio de los pedidos y tasas de conversión.

_Esta integración está mantenida por Stylitics._

## Sobre la integración

La integración de Braze y Stylitics le permite mejorar sus campañas de correo electrónico existentes con contenidos agrupados atractivos y relevantes, creando una experiencia de cliente personalizada.

![]({% image_buster /assets/img/stylitics.png %}){: style="max-width:60%;"}

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Stylitics | Es necesario disponer de una cuenta [Stylitics](https://stylitics.com/) para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

A continuación se enumeran algunos ejemplos comunes de programas de correo electrónico activados:
- Correos electrónicos de carritos abandonados 
- Navegar por correos electrónicos abandonados 
- Correos electrónicos de confirmación de envío
- Correos electrónicos posteriores a la compra 

## Integración

Stylitics proporciona los datos del paquete para esta integración. Su proveedor de servicios de correo electrónico puede crear o actualizar la plantilla de correo electrónico para incluir los paquetes de Stylitics. Stylitics no puede alterar la maquetación ni el diseño de los correos electrónicos. 

1. Integre el paquete en el correo electrónico. ESP determina la posición y la personalización.
2. ESP actualiza el código de activación del correo electrónico para incluir el contenido de Stylitics.
3. ESP probará, previsualizará y lanzará las actualizaciones desencadenadas en serie. 

Stylitics sólo proporcionará los datos de los paquetes de artículos. Entre usted y su ESP, dispondrá de los datos de los usuarios y podrá conectar los datos del paquete de Stylitics para enviarlos a los usuarios.

## Intercambio de datos

Los tres enfoques siguientes le permiten incluir paquetes de Stylitics en sus correos electrónicos activados.

### 1\. Enfoque API (recomendado)

Usted o su ESP pueden realizar una llamada a la API por artículo para rellenar los datos del paquete en su correo electrónico. Stylitics te recomienda que utilices su API para hacer llamadas a la API, ya que está lista para ser utilizada inmediatamente.

{% alert note %}
Si realizas una prueba A/B ejecutada por Stylitics, los parámetros `styliticsCID` y `styliticsoverride` deben añadirse a las URL PDP de los elementos de Stylitics en los que el usuario hace clic en el correo electrónico.
<br><br>
Por ejemplo, {% raw %}`&styliticsoverride=001?styliticsCID=email[clientname]`{% endraw %}
{% endalert %}

### 2\. Enfoque de archivo plano
Usted o su ESP pueden hacer referencia a los datos del paquete de un artículo en un archivo plano para rellenar los datos del paquete en su correo electrónico. Stylitics puede aplanar los datos de los paquetes en formato CSV, TXT o XML y enviártelos diariamente. También pueden ayudar a ajustar el formato del archivo según las necesidades de su ESP. Ten en cuenta que se tarda entre 2 y 3 semanas en crear este archivo.

#### Requisitos:
- **Ubicación**: Stylitics puede soltar el archivo en el SFTP de Stylitics para que lo recojas diariamente, o puedes enviarles tus credenciales SFTP para soltar el archivo. 
- **Hora**: Stylitics dejará el archivo diariamente por la mañana. Dígales si necesita el expediente para una fecha concreta. 
- **Clave de archivo**: Usted y Stylitics deben ponerse de acuerdo sobre la cadena de datos del artículo que se utilizará en el archivo para que su ESP pueda hacer referencia a los datos. Se suelen utilizar SKU, `item_group_id`, o `item_number`. 

### 3\. Enfoque de extracción de datos del sitio web
Los vendedores pueden rastrear el contenido de Stylitics de su sitio web e insertar los datos del paquete en los mensajes de correo electrónico. No se requiere ningún trabajo adicional por parte de Stylitics. 

## Mejores prácticas para plantillas de correo electrónico 

Usted y su ESP crearán una plantilla de correo electrónico HTML para insertar los datos y paquetes de Stylitics. Aquí tienes algunas buenas prácticas y recomendaciones. 
- Mostrar de 2 a 4 paquetes en el correo electrónico para el artículo más caro o el primer artículo de precio completo que el usuario haya comprado o con el que haya interactuado. 
- Llame a varios `item_numbers` y muestre la respuesta de los primeros paquetes 
- Disponer de una opción alternativa si no hay paquetes disponibles para el artículo. 
	- Ocultar la sección de paquetes de Stylitics 
	- Mostrar los paquetes del siguiente artículo que ha visto el usuario 
- Mostrar imágenes de paquetes y una lista de títulos de productos e imágenes en miniatura para garantizar que el usuario haga clic con claridad.

{% alert note %}
El widget JavaScript de Stylitics no puede insertarse en los correos electrónicos, ya que éstos no admiten JavaScript.
{% endalert %}

## Análisis

Stylitics proporciona los datos del paquete para este tipo de programa de correo electrónico. Por lo tanto, pedimos un intercambio de datos abierto entre tú, tu ESP y Stylitics. Si es posible, esperamos recibir de ti las siguientes métricas para comprender el ascensor y mejorar el programa:
- Correos electrónicos enviados 
- Correos electrónicos abiertos 
- Opiniones y compromisos 
- Índice de clics 
- Añadir a las bolsas 
- Compras

## Próximos pasos 

Póngase en contacto con su gestor de cuenta de Stylitics para coordinar los próximos pasos y plazos del programa de correo electrónico. Algunos de los próximos pasos son: 
- Decide qué correos electrónicos quieres utilizar
- Conecta Stylitics con tu ESP para discutir el intercambio de datos y decidir la opción API o la opción de archivo plano 
- Crea maquetas con tu ESP 
- Alinearse con los análisis 
- Alinearse en el calendario de lanzamiento 


