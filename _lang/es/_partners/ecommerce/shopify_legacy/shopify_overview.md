---
nav_title: Resumen de Shopify (Legado)
article_title: "Resumen de Shopify (Legado)"
description: "Este artículo de referencia describe la asociación con Braze y Shopify, una empresa de comercio global que te permite conectar fácilmente su tienda Shopify con Braze para pasar determinados webhooks de Shopify a Braze. Aprovecha las estrategias Braze multicanal y Canvas para animar a los clientes a completar sus compras o reorientar a los usuarios en función de sus compras anteriores."
page_type: partner
search_tag: Partner
alias: /shopify_overview_legacy/
page_order: 0
---

# Resumen de Shopify (legado)

> [Shopify](https://www.shopify.com/) es una empresa líder en comercio global que proporciona herramientas de confianza para iniciar, hacer crecer, comercializar y administrar un negocio minorista de cualquier tamaño. Shopify hace que el comercio sea mejor para todos con una plataforma y unos servicios diseñados para ser fiables y entregar una mejor experiencia de compra a los consumidores de todo el mundo.

La integración de Shopify y Braze te permite conectar tu tienda Shopify para pasar fácilmente tus datos de Shopify a Braze. Puedes aprovechar las estrategias multicanal y Canvas en Braze para captar nuevos clientes potenciales, enviar mensajes a nuevos clientes o reorientar a tus usuarios con mensajes de pago abandonado para animarles a completar sus compras.

{% multi_lang_include alerts.md alert='Shopify deprecation' %}

## Características compatibles

- Seguimiento del comportamiento in situ y de usuarios anónimos a través del SDK Web de Braze
- Ayuda con la sincronización y conciliación de los clientes de Shopify en Braze a través del SDK Web de Braze.
- Sincronizar datos de clientes de Shopify
- Recopilar los estados de adhesión voluntaria de los suscriptores de Shopify por correo electrónico y SMS
- Rellenar datos históricos de compras en Shopify 
- Sincronización del catálogo de Shopify 
- Utilizar los mensajes dentro de la aplicación como canal 

## Casos de uso admitidos 

- Campañas Path-to-Purchase y recorridos de usuario en Canvas, incluidos: 
  - Abandono de la navegación 
  - Carrito abandonado 
  - Compra abandonada 
- Campañas posteriores a la compra y recorridos de usuario en Canvas, incluidos:
  - Confirmaciones de pedido 
  - Actualizaciones de cumplimiento 
  - Anulación de pedidos 
  - Reembolsos de pedidos
- Recomendaciones de productos
- Venta cruzada y upselling
- [En stock]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/back_in_stock/)

## Requisitos

| Requisito | Descripción |
| --- | --- |
| Tienda de Shopify | Tienes una tienda [Shopify](https://www.shopify.com/) activa.<br><br>Puedes conectar una tienda Shopify por espacio de trabajo. Si estás interesado en conectar varias tiendas a un espacio de trabajo, ponte en contacto con tu administrador del éxito del cliente para unirte al programa beta de Tiendas Múltiples de Shopify. |
| Permisos de usuario de Shopify | Tienes uno de los siguientes permisos para tu tienda Shopify:{::nomarkdown}<ul><li>Propietario de la tienda</li><li>Personal</li><li>Miembro con todas las configuraciones Generales y de Tienda Online, así como estos permisos adicionales de administrador:<ul><li>Pedidos</li><li>Ver (ubicado en <b>Productos</b>)</li><li>Clientes</li><li>Administrar configuración</li><li>Ver las aplicaciones desarrolladas por el personal y los colaboradores</li><li>Gestionar e instala aplicaciones y canales</li></ul></li></ul>{:/} |
| Implementación del SDK Web Braze | Para hacer un seguimiento del comportamiento en el sitio y de los usuarios anónimos, debes implementar el SDK de Braze Web a través de nuestra integración predeterminada en Shopify o manualmente. <br><br>Para más información sobre tus opciones de implementación, consulta [Implementar el SDK Web en tu sitio de Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify). |
| Habilitada la segmentación de propiedades del evento | Para confirmar que puedes segmentar las propiedades de tus eventos de Shopify, trabaja con tu administrador del éxito del cliente o con [el soporte de Braze]({{site.baseurl}}/braze_support/) para confirmar que la segmentación de las propiedades del evento está activada en tu panel de Braze. |
{: .reset-td-br-1 .reset-td-br-2 }

## Reglamento General de Protección de Datos (RGPD)

Con respecto a los datos personales enviados a los servicios de Braze por sus clientes o en su nombre, Braze es el procesador de datos, y nuestros clientes son los controladores de datos. En consecuencia, Braze procesa dichos datos personales únicamente por instrucción de nuestros clientes y, cuando procede, notifica a nuestros clientes las solicitudes de los interesados. Como responsables del tratamiento, nuestros clientes responden directamente a las solicitudes de los interesados. Como parte de la integración de la plataforma Braze con Shopify, Braze recibe automáticamente [los webhooks RGPD de Shopify](https://shopify.dev/tutorials/add-gdpr-webhooks-to-your-app). Sin embargo, los clientes de Braze son responsables en última instancia de responder a las solicitudes de los sujetos de datos de sus clientes de Shopify mediante el uso de [los SDK de Braze]({{site.baseurl}}/developer_guide/home/) o [las API REST]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) de acuerdo con nuestras políticas de [cumplimiento de la RGPD]({{site.baseurl}}/dp-technical-assistance/).
