---
nav_title: Grupos de suscripción
article_title: Grupos de suscripción
page_order: 1
description: "Este artículo trata de los grupos de suscripción a mensajes de LINE."
page_type: reference
channel:
 - LINE
alias: /line/subscription_groups/
---

# Grupos de suscripción LINE

> Existen dos estados de suscripción para los usuarios de LINE: suscrito y no suscrito. LINE puede tener hasta 100 grupos de suscripción por espacio de trabajo, con cada grupo de suscripción conectado a su propio canal LINE.

| Estado | Definición |
| --- | --- |
| Suscrito | El usuario siguió el canal de LINE desde su aplicación de LINE. Los usuarios se suscriben automáticamente cuando te siguen después de que hayas completado los pasos de integración. |
| No suscrito | El usuario no siguió el canal de LINE desde su aplicación de LINE, o el usuario dejó de seguir explícitamente el canal de LINE. <br><br> Los usuarios que se den de baja de un grupo de suscripción de LINE dejarán de recibir mensajes de LINE de los canales de envío que pertenezcan al grupo de suscripción. |
{: .reset-td-br-1 .reset-td-br-2 }

## Establecer el grupo de suscripción LINE de un usuario

LINE alberga el estado de suscripción de los usuarios. Braze procesa los eventos follow y unfollow que actualizan el estado de la suscripción.