---
nav_title: Centros de datos
article_title: Centros de datos
page_order: 1
page_type: reference
description: "Este artículo de referencia contiene información sobre los centros de datos, incluida su ubicación y cómo registrarse en centros de datos específicos de una región."
---

# Centros de datos

> Los centros de datos Braze están construidos para ofrecerte opciones sobre dónde se procesan y almacenan los datos de tus usuarios. Esto te permite gestionar eficazmente los riesgos relacionados con la soberanía, flexibilidad y gestión de los datos.

## Cómo funciona

Braze gestiona varios centros de datos ubicados en distintas regiones del mundo. Estos centros de datos permiten que nuestros servicios sean fiables y escalables. Esta distribución geográfica ayuda a minimizar la latencia, que es el tiempo que tardan los datos en viajar entre el servidor y el usuario. 

Esto también significa que cuando un usuario interactúa con tu aplicación o sitio web, sus peticiones se dirigen al centro de datos más cercano, optimizando el rendimiento y reduciendo los tiempos de carga. Al conectarte al centro de datos más cercano, tus usuarios pueden disfrutar de tiempos de carga rápidos, lo que es especialmente importante para la mensajería en tiempo real y la interacción con los usuarios.

Supongamos que tienes una aplicación móvil que envía notificaciones push a los usuarios. Si un usuario de Melbourne recibe una notificación, la solicitud de envío de dicha notificación se dirige al centro de datos más cercano de Australia. En caso de que la aplicación móvil experimente un aumento de usuarios durante un evento promocional, Braze tiene una infraestructura escalable con múltiples centros de datos que pueden gestionar el aumento de la demanda.

## Lista de centros de datos

### Australia

{% multi_lang_include data_centers.md datacenters='AU' %}

### Unión Europea

{% multi_lang_include data_centers.md datacenters='EU' %}

### Indonesia

{% multi_lang_include data_centers.md datacenters='ID' %}

### Estados Unidos

{% multi_lang_include data_centers.md datacenters='US' %}

## Registrarse en centros de datos específicos de una región

Cuando configures tu cuenta Braze, puedes registrarte en centros de datos específicos de una región. Ponte en contacto con tu director de cuentas para obtener información y recomendaciones sobre qué centros de datos funcionan mejor para ti en función de las regiones geográficas de tus usuarios.
