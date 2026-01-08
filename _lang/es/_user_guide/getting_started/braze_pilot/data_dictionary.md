---
nav_title: Diccionario de datos
article_title: Diccionario de datos para Piloto Braze
page_order: 3
page_type: reference
description: "Este artículo de referencia cubre brevemente los pasos de integración que deben dar tus ingenieros o desarrolladores."
---

# Diccionario de datos

> Cada simulación de aplicación en Braze Pilot está instrumentada para recopilar una serie de eventos y atributos basados en la actividad del usuario en la aplicación. 

## El enfoque de los datos

La aplicación registra atributos personalizados y eventos típicos del sector representado por la marca ficticia. Puedes utilizar estos atributos para impulsar demostraciones para una variedad de casos de uso comunes.
Generalmente, todos los eventos y atributos llevan como prefijo un código abreviado que corresponde a la simulación de la aplicación responsable de los datos. Por ejemplo:

- Todos los datos registrados por la simulación de la aplicación Steppington llevan el prefijo `st_`
- Todos los datos registrados por la simulación de la aplicación PantsLabyrinth llevan el prefijo `pl_`
- Todos los datos registrados por la simulación de la aplicación MovieCanon llevan el prefijo `mc_`

## Lista de eventos registrados y atributos

La siguiente tabla enumera los eventos y atributos registrados por Braze Pilot.

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 32%;
}
th:nth-child(2), td:nth-child(2) {
    width: 15%;
}
th:nth-child(3), td:nth-child(3) {
    width: 10%;
}
th:nth-child(4), td:nth-child(4) {
    width: 20%;
}
th:nth-child(5), td:nth-child(5) {
    width: 28%;
}
</style>

<table>
    <thead>
        <tr>
            <th>Nombre</th>
            <th>Aplicación</th>
            <th>Tipo</th>
            <th>Propiedades</th>
            <th>Cuando se registra</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>mc_entered_app</code></td>
            <td>MovieCanon</td>
            <td>Evento</td>
            <td></td>
            <td>Cuando el usuario entra en la aplicación MovieCanon</td>
        </tr>
        <tr>
            <td><code>mc_watched_movie</code></td>
            <td>MovieCanon</td>
            <td>Evento</td>
            <td><code>título: cadena</code></td>
            <td>Cuando el usuario termina de ver un video</td>
        </tr>
        <tr>
            <td><code>mc_viewed_movie_page</code></td>
            <td>MovieCanon</td>
            <td>Evento</td>
            <td><code>título: cadena</code></td>
            <td>Cuando el usuario ve una página de películas</td>
        </tr>
        <tr>
            <td><code>pl_viewed_item</code></td>
            <td>PantalonesLaberinto</td>
            <td>Evento</td>
            <td><code>item_name: cadena</code></td>
            <td>Cuando el usuario ve una página de producto</td>
        </tr>
        <tr>
            <td><code>pl_entered_app</code></td>
            <td>PantalonesLaberinto</td>
            <td>Evento</td>
            <td></td>
            <td>Cuando el usuario entra en la aplicación PantsLabyrinth</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_wishlist</code></td>
            <td>PantalonesLaberinto</td>
            <td>Evento</td>
            <td><code>item_name: cadena</code></td>
            <td>Cuando el usuario añade un artículo a su lista de deseos</td>
        </tr>
        <tr>
            <td><code>pl_added_item_to_cart</code></td>
            <td>PantalonesLaberinto</td>
            <td>Evento</td>
            <td><code>item_name: cadena</code></td>
            <td>Cuando el usuario añade un artículo a su cesta</td>
        </tr>
        <tr>
            <td><code>&lt;purchase_event></code></td>
            <td>PantalonesLaberinto</td>
            <td>Evento</td>
            <td><code>nombre: cadena</code><br><code>precio: número</code></td>
            <td>Cuando el usuario completa una compra</td>
        </tr>
        <tr>
            <td><code>st_entered_app</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td></td>
            <td>Cuando el usuario entra en la aplicación Steppington</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>class_type: cadena</code><br><code>calories_burned: número</code><br><code>workout_length: número</code></td>
            <td>Cuando el usuario completa un entrenamiento</td>
        </tr>
        <tr>
            <td><code>st_viewed_premium_benefit</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>benefit_type: cadena</code></td>
            <td>Cuando el usuario visita la pestaña Steppington+ (si está habilitada con la bandera de característica)</td>
        </tr>
        <tr>
            <td><code>st_viewed_class</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>class_type: cadena</code></td>
            <td>Cuando el usuario visita una página de entrenamiento</td>
        </tr>
        <tr>
            <td><code>st_completed_class</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>class_type: cadena</code><br><code>calories_burned: número</code><br><code>workout_length: número</code></td>
            <td>Cuando el usuario completa un entrenamiento</td>
        </tr>
        <tr>
            <td><code>st_most_recent_completed_class</code></td>
            <td>Steppington</td>
            <td>Atributo</td>
            <td><code>cadena</code></td>
            <td>Cuando el usuario completa un entrenamiento</td>
        </tr>
        <tr>
            <td><code>st_favorited_class</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>class_type: cadena</code></td>
            <td>Cuando el usuario favorece una clase</td>
        </tr>
        <tr>
            <td><code>st_unfavorited_class</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>class_type: cadena</code></td>
            <td>Cuando al usuario no le gusta una clase</td>
        </tr>
        <tr>
            <td><code>st_started_free_trial</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td></td>
            <td>Cuando el usuario selecciona el botón <strong>Iniciar Prueba Gratuita</strong> </td>
        </tr>
        <tr>
            <td><code>st_set_goal</code></td>
            <td>Steppington</td>
            <td>Evento</td>
            <td><code>goal_name: cadena</code><br><code>objetivo: número</code><br><code>unidades: cadena</code></td>
            <td>Cuando el usuario selecciona el botón <strong>Iniciar prueba gratuita</strong>.</td>
        </tr>
    </tbody>
</table>
