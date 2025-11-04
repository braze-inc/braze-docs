---
nav_title: Taller
article_title: Taller Amazon Personalize
alias: /partners/amazon_personalize_workshop/
description: "Este artículo de referencia describe el proceso de configuración de Amazon Personalize y su integración en su entorno Braze mediante Connected Content."
page_type: partner
search_tag: Partner
---

# Taller Amazon Personalize

> Este artículo de referencia le guiará a través del proceso de configuración de Amazon Personalize y su integración en su entorno Braze mediante Connected Content. Para ello se utilizará un taller práctico que le guiará a través de todos los pasos necesarios para desplegar y entrenar las soluciones de Amazon Personalize e integrarlas en una campaña de correo electrónico Braze.

_Esta integración es mantenida por Amazon Personalize._

## Sobre la integración

Los siguientes ejemplos están desplegados en un sitio de comercio electrónico de ejemplo totalmente funcional llamado Tienda de demostración minorista. Los recursos y el código de este tutorial están publicados en la [tienda de demos de AWS Samples Retail](https://github.com/aws-samples/retail-demo-store/). Puede utilizar esta implementación de arquitectura de referencia como esquema para implementar Amazon Personalize en su propio entorno.

## Requisitos

Deberá clonar el [repositorio de Retail Demo Store](https://github.com/aws-samples/retail-demo-store/) y seguir los pasos descritos para implementar el entorno del taller en su cuenta de AWS. Se necesita una cuenta de AWS para completar el taller y ejecutar el código de integración.

## Arquitectura de integración

Antes de configurar Braze para enviar mensajes personalizados a los usuarios, revisa los componentes relevantes necesarios para un sitio web típico de comercio electrónico, utilizando como ejemplo la arquitectura de la tienda de demostración minorista.

![Una imagen en la que se desglosa la arquitectura de personalización Braze y se observa cómo interactúan entre sí los distintos componentes.]({% image_buster /assets/img/amazon_personalize/braze-personalize-arch.png %}){: style="max-width:70%" }

1. La interfaz de usuario web de Retail Demo Store utiliza la biblioteca JavaScript de AWS Amplify para enviar eventos de formación a Amazon Personalize.
2. Los registros de usuario de la campaña Braze se actualizan desde el servicio Usuario de tienda global.
3. Cuando se ejecuta una campaña Braze, se utiliza una plantilla de contenido conectado para obtener recomendaciones de Personalize y rellenar una plantilla de correo electrónico para un usuario objetivo.
4. La información del catálogo de productos también puede utilizarse para entrenar modelos de recomendación.

Braze enviará correos electrónicos a sus usuarios en función de su comportamiento o de los atributos de sus perfiles de usuario. Estos datos pueden ayudar a identificar a los usuarios y construir perfiles de usuario para ayudar a determinar cuándo enviar un mensaje o correo electrónico.

Este flujo de datos de eventos se producirá en paralelo a los datos de eventos de comportamiento que se envían a Amazon Personalize. En este taller, la tienda de demostración utiliza Amplify para enviar eventos a Personalize. Estos datos se utilizan para entrenar un modelo de recomendaciones que luego se puede utilizar en las llamadas Braze Connected Content para personalizar el contenido para los usuarios cuando se ejecuta su campaña Braze.

Braze Connected Content podrá obtener estas recomendaciones a través de un servicio de recomendaciones que se ejecuta en AWS. El taller Retail Demo Store muestra un ejemplo de implantación de un servicio de recomendación. En un escenario de despliegue en su propia infraestructura, necesitará desplegar un servicio similar para obtener elementos de su propio servicio de catálogo.

## Organización del taller sobre arquitectura de referencia

### Paso 1: Implementa la tienda de demostración de comercio minorista en tu cuenta de AWS

![Una imagen de las regiones AWS disponibles.]({% image_buster /assets/img/amazon_personalize/region.png %}){: style="float:right;max-width:40%;margin-top:15px;margin-bottom:10px;"}

En la siguiente tabla, elija una **región de AWS** y seleccione **Launch Stack**. Esta lista no representa todas las regiones posibles en las que puede desplegar el proyecto, sólo las regiones actualmente configuradas para el despliegue con la tienda de demostración minorista.

Acepta todos los valores por defecto de los parámetros de la plantilla. El despliegue de todos los recursos del proyecto debería llevar entre 25 y 30 minutos.

### Paso 2: Crear campañas de personalización de Amazon

Antes de poder ofrecer recomendaciones personalizadas de productos, primero debe entrenar los modelos de aprendizaje automático y proporcionar puntos finales de inferencia que le permitan obtener recomendaciones de Amazon Personalize. La plantilla de CloudFormation desplegada en el paso 1 incluye una instancia de bloc de notas de Amazon SageMaker que proporciona un bloc de notas de Jupyter con instrucciones detalladas paso a paso.

1. Inicie sesión en la cuenta de AWS en la que implementó la plantilla de AWS CloudFormation en el paso 1.
2. En la consola de Amazon SageMaker, seleccione **Instancias de Notebook**.
3. Si no ve la instancia del cuaderno **RetailDemoStore**, asegúrese de que se encuentra en la misma región en la que desplegó el proyecto en el paso 1.
4. Para acceder a la instancia del cuaderno, seleccione **Abrir Jupyter** o **Abrir JupyterLab**.
5. Cuando se haya cargado la interfaz Web de Jupyter para la instancia del cuaderno, elige el cuaderno `workshop/1-Personalization/1.1-Personalize.ipynb`. Puede que tenga que elegir la carpeta `workshop` para ver los subdirectorios de los cuadernos.
6. Cuando tenga abierto el cuaderno `1.1-Personalize`, recorra el taller ejecutando cada celda. Puede elegir **Ejecutar** en la barra de herramientas de Jupyter para ejecutar secuencialmente el código en las celdas. El cuaderno tarda aproximadamente dos horas en completarse.

### Paso 3: Enviar correos electrónicos personalizados desde Braze

Una vez implementadas las soluciones y campañas de Amazon Personalize, su instancia de la Tienda de demostración para minoristas estará lista para proporcionar recomendaciones a sus campañas de email. En el paso 1, desplegó la aplicación web de demostración y todos los servicios asociados, incluido el servicio de recomendación necesario para integrar sus campañas de correo electrónico con Braze a través de Connected Content, que utiliza las campañas de Amazon Personalize que desplegó en el paso 2.

Al igual que en el taller de personalización del paso 2, el siguiente taller de mensajería Braze le guiará a través de la configuración de la integración de Braze y Amazon Personalize.

1. Inicie sesión en la cuenta de AWS en la que implementó la plantilla de AWS CloudFormation en el paso 1.
2. En la consola de Amazon SageMaker, seleccione **Instancias de Notebook**.
3. Si no ves la instancia del cuaderno **RetailDemoStore**, asegúrate de que estás en la misma región de AWS en la que implementaste el proyecto.
4. Para acceder a la instancia del cuaderno, seleccione **Abrir Jupyter** o **Abrir JupyterLab**.
5. Cuando se haya cargado la interfaz Web de Jupyter para la instancia del cuaderno, elige el cuaderno `workshop/4-Messaging/4.2-Braze.ipynb`. Puede que tenga que elegir la carpeta `workshop` para ver los subdirectorios de los cuadernos.
6. Cuando tenga abierto el cuaderno `4.2-Braze`, recorra el taller ejecutando cada celda. Puede elegir **Ejecutar** en la barra de herramientas de Jupyter para ejecutar secuencialmente el código en las celdas. El cuaderno tarda aproximadamente 1 hora en completarse.

### Paso 4: Limpiar recursos

Para evitar incurrir en cargos futuros, elimina los recursos de AWS que creó el proyecto de tienda minorista de demostración eliminando la pila de AWS CloudFormation que creaste en el paso 1.


