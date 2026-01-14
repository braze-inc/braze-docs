---
nav_title: Himno del futuro
article_title: Himno del futuro
description: "Aprende a integrar Future Anthem con Braze."
alias: /partners/future_anthem/
page_type: partner
search_tag: Partner
---

# Himno del futuro

> El producto todo en uno de Future Anthem para el sector del juego con dinero real, Amplifier AI, entrega personalización de contenidos, experiencias en tiempo real y audiencias dinámicas. La IA del Amplificador funciona fácilmente en deportes, casinos y loterías, permitiendo a los clientes mejorar los perfiles de jugador Braze con atributos de jugador específicos del sector, como juego favorito, equipo favorito, puntuación de interacción, recomendación de próxima apuesta, próxima apuesta esperada y mucho más.

{% alert important %}
Esta característica está actualmente en Acceso anticipado. Ponte en contacto con el equipo de éxito del cliente de Future Anthem para empezar.
{% endalert %}

## Requisitos previos

| Requisito              | Descripción                                            |
|--------------------------|--------------------------------------------------------|
| Futura cuenta Anthem    | Una cuenta de Future Anthem. |
| Clave de API REST de Braze       | Una clave de API REST de Braze con el código [`users.track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze      | El [punto final REST de]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Braze que coincida con tu instancia, como `rest.iad-01.com`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ejemplos

Con esta integración, puedes:

- Identifica a los usuarios con altas puntuaciones de interacción y dirígete a ellos con ofertas personalizadas, como promociones exclusivas o recompensas VIP.
- Sugiere juegos similares a un usuario basándote en los juegos que ya le gustan.

## Integración

El equipo de éxito del cliente de Future Anthem te ayudará a configurar tu integración. Ponte en contacto con tu contacto de Éxito del cliente y te ayudará a identificar los atributos más relevantes para que los envíes a Braze.

|Ejemplo de atributos en Future Anthem|Ejemplo de atributos en Braze|
|-----------------------------------|---------------------------|
|![Los atributos del perfil del usuario.]({% image_buster /assets/img/future_anthem/future_anthem_example_attributes.png %})|![El atributo del objeto.]({% image_buster /assets/img/future_anthem/braze_example_attributes.png %})|

## Atributos personalizados Braze

Estos son los atributos personalizados Braze disponibles. Para obtener información más detallada, consulta [Himno Futuro: Cómo empezar](https://knowledge.futureanthem.com/getting-started).

{% tabs local %}
{% tab Recomendaciones de apuestas %}

| Subcategoría | Ejemplo (JSON) | Tipo de datos |
| ------- | ----------- |----------- |
| Preferencias del usuario | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Objeto |
| Recomendaciones de apuestas simples | `{"Sport": "Ice Hockey", "League": "NHL", "Market": "Goals", "Team": "Rangers", "Player": "Kreider"}`| Objeto |
| Recomendaciones de apuestas acumuladoras | `{"Bet_1": "Halland Goal vs. Manchester United", "Bet_2": "Liverpool vs. Everton"}`| Objeto |
| Recomendaciones de apuestas acumuladoras | `{"Bet_1": 1.5, "Bet_2": 2}` | Objeto |
| Constructor de apuestas Recomendaciones de apuestas | `{"Sport":"American Football", "Competition":"NFL", "Event":"Seahwaks@Giants", "Market":"MoneyLine", "Selection":"Seahawks"}`| Objeto |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Recomendaciones adicionales %}

| Subcategoría | Ejemplo | Tipo de datos |
| ------- | ----------- |----------- |
|NGR - Ingresos netos del juego durante la vida del usuario | 2232| Número|
| NGR14 - Ingresos netos de juego de los últimos 14 días de actividad | 42 | Número
| Puntuación de la ganancia del jugador| 130 | Número |
| Puntuación de interacción | 0.78 | Número |
| Puntuación de riesgo de pérdida | 0.02 | Número |
| Fecha estimada de la próxima apuesta | 2024-08-29 | Tiempo |
| Apuesta y Consigue - Recomendación del valor del bono | 20 | Número |
| Otras recomendaciones de valor añadido en el futuro | 0 | Número |
| Futuro CLTV  | 3126 | Número |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Recomendaciones de juegos %}

| Subcategoría | Ejemplo | Tipo de datos |
| ------- | ----------- |----------- |
| Recomendado para ti | Fluffy Favourites, Fishin' Frenzy, Big Bass Bonanza, Rainbow Gold, Wild West| Matriz |
| Juegos favoritos | Frenesí de pesca | Matriz |
| Nuevos juegos recomendados | Abejas pegajosas, Cuidado con los Megaways profundos, Fiesta del oro, Los Picapiedra| Matriz |
| Jugadores como tú están jugando (filtrado colaborativo) |Gold Blitz, Big Bass Splash, Rick y Morty, Book of Dead, Gates of Olympus, Luck O' the Irish | Matriz |
| Porque jugaste (Juego similar)|Fluffy Favourites 2, Luck Rish Express, Gold Cash, Aztec Treasure Hunt, Stars Bonanza | Matriz |
| A continuación (Secuenciación del juego) | Fishin' Frenzy La gran captura, Gran banquero, 9 máscaras de fuego, Super león, Pescando grandes ollas de oro | Matriz |
| Juegos populares | Templo de Iris, Frenesí de pesca, Recompensa de pesca, Hora loca, Favoritos esponjosos | Matriz |
| Juegos de moda | Cerdo Banquero, Hiper Oro, Rey Pirámide, Oro Efectivo | Matriz |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Grupo de jugadores %}

| Subcategoría | Ejemplo | Tipo de datos |
| ------- | ----------- |----------- |
| Muestra en qué grupo está el jugador | Juego de alto valor Diverso| Cadena |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab Sostenimiento del jugador - Riesgo potencial del jugador %}

| Subcategoría | Ejemplo | Tipo de datos |
| ------- | ----------- |----------- |
| Puntuación de riesgo | 0.5| Número |
| Jugador arriesgado | Verdadero | Booleano |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}
