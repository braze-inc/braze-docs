---
nav_title: Solución de problemas
article_title: Segmentos de resolución de problemas
page_order: 12
page_type: reference
tool: 
  - Segments
description: "Este artículo de referencia cubre los pasos para solucionar problemas y las consideraciones a tener en cuenta al utilizar segmentos."
---

# Segmentos de resolución de problemas

## Comportamiento de los usuarios

### El usuario ya no está en un segmento

Si un usuario no está disponible mientras se crea un segmento, sus datos de usuario que determinan su elegibilidad para el segmento podrían haber cambiado como resultado de su propia actividad o de otras campañas y Canvases con los que haya interactuado anteriormente. Si la reelección está activada, su perfil de usuario mostrará los últimos datos de la campaña recibida.

### Aparece información de los usuarios de otras aplicaciones cuando filtro una aplicación específica.

Los usuarios pueden tener varias aplicaciones, por lo que la selección de una aplicación específica en la sección **Aplicaciones utilizadas** de la página de segmentación arrojará resultados para los usuarios que al menos tengan esa aplicación. El filtro no arroja resultados para los usuarios que tienen exclusivamente esa app.

## Análisis e informes

### El *mensaje enviado* o los *destinatarios únicos* en Campaign Analytics no coinciden con el recuento de segmentos 

Si el recuento de su análisis de campaña para *Mensajes enviados* o *Destinatarios únicos* no coincide con el número de usuarios del filtro de segmento `Has received message from campaign X`, puede deberse a dos motivos:

1. **Los usuarios pueden haber sido archivados, huérfanos o eliminados desde el lanzamiento de la campaña.**<br><br>Por ejemplo, supongamos que 1000 usuarios reciben una campaña y haces una exportación CSV el mismo día. Verás 1.000 usuarios reportados. Durante el mes siguiente, 50 de esos 1.000 usuarios son eliminados (por ejemplo, por el endpoint `users/delete` ). Cuando realice otra exportación CSV, verá 950 usuarios registrados, mientras que el recuento de *destinatarios únicos* en **Campaign Analytics** sigue siendo de 1.000.<br><br>En otras palabras, la métrica de *destinatarios únicos* es un recuento incremental, mientras que el segmentador y la exportación CSV proporcionan un recuento de los usuarios existentes actualmente.<br><br>

2. **La campaña tiene configurada la reelegibilidad, por lo que los usuarios pueden volver a entrar en la campaña varias veces**<br><br>Por ejemplo, supongamos que una campaña de correo electrónico tiene la reelegibilidad establecida en cero minutos (los usuarios pueden volver a entrar en la campaña siempre que cumplan los requisitos del segmento de audiencia), y la campaña lleva en marcha más de un mes. El número de *mensajes enviados* en **Campaign Analytics** no coincidiría con el número del segmento porque este campo incluiría mensajes enviados a usuarios duplicados.<br><br>Esto se debe a que Braze cuenta los usuarios únicos como *Destinatarios Únicos Diarios*, o el número de usuarios que recibieron un mensaje concreto en un día. Esto significa que los usuarios que vuelvan a cumplir los requisitos serán contabilizados más de una vez como destinatarios únicos, ya que la ventana "única" sólo dura un día. Esto puede dar lugar a que el número de *Destinatarios Únicos Diarios* sea superior al número de perfiles de usuario en la exportación CSV. Los perfiles de usuario del archivo CSV serán realmente únicos.