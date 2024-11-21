---
nav_title: Tarjetas de contenido
article_title: Integración de tarjetas de contenido
page_order: 2
---

# Integración de tarjetas de contenido

> Aprende a integrar tarjetas de contenido para el SDK Braze de Cordova.

{% multi_lang_include cordova/prerequisites.md %}

## Fuentes de tarjetas

El SDK de Braze incluye una fuente de tarjetas predeterminada. Para mostrar la fuente de tarjetas predeterminada, puedes utilizar el método `launchContentCards()`. Este método gestiona todo el seguimiento de análisis, los descartes y la representación de las tarjetas de contenido de un usuario.

## Tarjetas de contenido

Puedes utilizar estos métodos adicionales para crear una fuente personalizada de tarjetas de contenido dentro de tu aplicación:

|Método | Descripción |
|---|---|
|`requestContentCardsRefresh()`|Envía una petición en segundo plano para solicitar las últimas tarjetas de contenido al servidor del SDK de Braze.|
|`getContentCardsFromServer(successCallback, errorCallback)`|Recupera tarjetas de contenido del SDK Braze. Esto solicitará las últimas tarjetas de contenido al servidor y devolverá la lista de tarjetas al finalizar.|
|`getContentCardsFromCache(successCallback, errorCallback)`|Recupera tarjetas de contenido del SDK Braze. Esto devolverá la última lista de tarjetas de la caché local, que se actualizó en la última actualización.|
|`logContentCardClicked(cardId)`|Registra un clic para el ID de tarjeta de contenido dado.|
|`logContentCardImpression(cardId)`|Registra una impresión para el ID de tarjeta de contenido dado.|
|`logContentCardDismissed(cardId)`|Registra un descarte para el ID de tarjeta de contenido dado.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Soporte de GIF

{% multi_lang_include wrappers/gif_support/content_cards.md %}
