---
nav_title: Vínculos profundos de navegación
article_title: Vínculos profundos de navegación en Braze Pilot
page_order: 4
page_type: reference
description: "Este artículo de referencia cubre brevemente los pasos de integración que deben seguir sus ingenieros o desarrolladores."
---

# Vínculos profundos de navegación en Braze Pilot

> Braze Pilot admite vinculación en profundidad desde la mensajería de Braze a partes concretas de la aplicación Pilot. Esto te permite crear casos de uso de interacción, dirigiendo a los usuarios a diversas partes de la aplicación Pilot. También puedes utilizar parámetros de vínculos profundos opcionales para personalizar el contenido de páginas concretas de la aplicación para el usuario. Para obtener más información sobre la vinculación en profundidad, consulta [Vínculos profundos a contenido dentro de la aplicación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking).

## General

Estos son los vínculos profundos para las páginas de navegación principales de la aplicación Pilot. 

| Pantalla | Vínculo profundo |
| --- | --- |
| Proyectos | `braze-pilot://navigation/projects` |
| Datos de registro | `braze-pilot://navigation/logdata` |
| Configuración | `braze-pilot://navigation/setup` |
| Cambiar idioma | `braze-pilot://navigation/selectlanguage` |
| Cámara | `braze-pilot://navigation/camera` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Steppington

Estos son los vínculos profundos para la aplicación de la marca ficticia Steppington en Pilot.

### Ejemplo de vínculo profundo

`braze-pilot://navigation/steppington/workout?title=Running&icon=HEART_DETAILS&image=https://picsum.photos/400&info=This%20workout%20is%20awesome%21&workout=5k%20Run&calories=600&length=25&workout_info_left_text=Road%20Run&workout_info_left_icon=RUNNING_HOME&workout_info_center_text=120%20BPM&workout_info_center_icon=HEART_DETAILS&workout_info_right_text=25%3A00&workout_info_right_icon=TIMER_DETAILS`

### Vínculos profundos sin parámetros

| Pantalla | Vínculo profundo |
| --- | --- |
| Pantalla de inicio | `braze-pilot://navigation/steppington/splash` |
| Inicio | `braze-pilot://navigation/steppington/home` |
| Página de Steppington+ | `braze-pilot://navigation/steppington/plus` |
| Pantalla de objetivos | `braze-pilot://navigation/steppington/goals` |
| Cambiar pantalla de objetivos | `braze-pilot://navigation/steppington/changegoals` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Vínculos profundos con parámetros

| Pantalla | Vínculo profundo |
| --- | --- |
| Entrenamiento | `braze-pilot://navigation/steppington/workout` |
| Entrenamiento activo | `braze-pilot://navigation/steppington/activeworkout` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Parámetros aceptados

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 22%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table>
    <thead>
        <tr>
            <th>Parámetro</th>
            <th>Descripción</th>
            <th>Obligatoria</th>
            <th>Predeterminado (si no se especifica)</th>
            <th>Tipo</th>
            <th>Ejemplo</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>title</code></td>
            <td>El título que se utilizará en la parte superior de la pantalla.</td>
            <td>Sí</td>
            <td></td>
            <td>Cadena</td>
            <td>En ejecución</td>
        </tr>
        <tr>
            <td><code>icon</code></td>
            <td>Una cadena que representa el icono que se va a utilizar.</td>
            <td>No</td>
            <td><code>RUNNING_HOME</code></td>
            <td>Cadena</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>La URL de la imagen del artículo.</td>
            <td>Sí</td>
            <td></td>
            <td>Cadena</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>info</code></td>
            <td>Información sobre el entrenamiento que se colocará sobre el botón de inicio del entrenamiento.</td>
            <td>Sí</td>
            <td></td>
            <td>Cadena</td>
            <td>¡Este entrenamiento es increíble!</td>
        </tr>
        <tr>
            <td><code>workout</code></td>
            <td>El nombre del entrenamiento. Enviado en el <code>st_completed_class</code> evento.</td>
            <td>Sí</td>
            <td></td>
            <td>Número</td>
            <td>Carrera de 5 km</td>
        </tr>
        <tr>
            <td><code>calories</code></td>
            <td>El número de calorías que se mostrarán en la pantalla de entrenamiento activo. Enviado en el <code>st_completed_class</code> evento.</td>
            <td>No</td>
            <td>Número aleatorio entre 500 y 1250.</td>
            <td>Número</td>
            <td>600</td>
        </tr>
        <tr>
            <td><code>length</code></td>
            <td>La duración del entrenamiento. Enviado en el <code>st_completed_class</code> evento.</td>
            <td>No</td>
            <td></td>
            <td>Número</td>
            <td>25</td>
        </tr>
        <tr>
            <td><code>workout_info_left_text</code></td>
            <td>El texto que se utilizará en la tarjeta izquierda de la pantalla de entrenamiento activo.</td>
            <td>No</td>
            <td></td>
            <td>Cadena</td>
            <td>Carretera%20Correr</td>
        </tr>
        <tr>
            <td><code>workout_info_left_icon</code></td>
            <td>El icono que se utilizará en la tarjeta izquierda de la pantalla de entrenamiento activo.</td>
            <td>No</td>
            <td></td>
            <td>Cadena</td>
            <td>RUNNING_HOME</td>
        </tr>
        <tr>
            <td><code>workout_info_center_text</code></td>
            <td>El texto que se utilizará en la tarjeta central de la pantalla de entrenamiento activo.</td>
            <td>No</td>
            <td></td>
            <td>Cadena</td>
            <td>120 % 20 BPM</td>
        </tr>
        <tr>
            <td><code>workout_info_center_icon</code></td>
            <td>El icono que se utilizará en la tarjeta central de la pantalla de entrenamiento activo.</td>
            <td>No</td>
            <td></td>
            <td>Cadena</td>
            <td>HEART_DETAILS</td>
        </tr>
        <tr>
            <td><code>workout_info_right_text</code></td>
            <td>El texto que se utilizará en la tarjeta derecha de la pantalla de entrenamiento activo.</td>
            <td>No</td>
            <td></td>
            <td>Cadena</td>
            <td>25 %: 00</td>
        </tr>
        <tr>
            <td><code>workout_info_right_icon</code></td>
            <td>El icono que se utilizará en la tarjeta derecha de la pantalla de entrenamiento activo.</td>
            <td>No</td>
            <td></td>
            <td>Cadena</td>
            <td>TIMER_DETAILS</td>
        </tr>
    </tbody>
</table>

##### Opciones de iconos

| Ícono | Imagen |
| --- | --- |
| `RUNNING_HOME` | ![Un icono del calzado deportivo.]({% image_buster /assets/img/braze_pilot/running_home_icon.png %}){:style="max-width:30%"} |
| `HEART_DETAILS` | ![Un icono con forma de corazón.]({% image_buster /assets/img/braze_pilot/heart_details_icon.png %}){:style="max-width:30%"} |
| `TIMER_DETAILS` | ![Un icono de cronómetro.]({% image_buster /assets/img/braze_pilot/timer_details_icon.png %}){:style="max-width:30%"} |
| `YOGA_HOME` | ![Icono de una persona en una postura de yoga.]({% image_buster /assets/img/braze_pilot/yoga_home_icon.png %}){:style="max-width:30%"} |
| `BICYCLE_HOME` | ![Un icono del ciclismo.]({% image_buster /assets/img/braze_pilot/bicycle_home_icon.png %}){:style="max-width:30%"} |
| `DUMBBELL_HOME` | ![Un icono de mancuerna.]({% image_buster /assets/img/braze_pilot/dumbbell_home_icon.png %}){:style="max-width:30%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## PantsLabyrinth

Estos son los vínculos profundos para la aplicación de la marca ficticia PantsLabyrinth en Pilot.

### Ejemplo de vínculo profundo

`braze-pilot://navigation/pantslabyrinth/itemdetails?name=Jeans&price=85&image=https://picsum.photos/400&description=This%20item%20is%20awesome%21&quantity=2&size=Large&colors=%230000FF,%23FF0000&color_strings=White,Blue&selected_color=1`

### Vínculos profundos sin parámetros

| Pantalla | Vínculo profundo |
| --- | --- |
| Pantalla de inicio | `braze-pilot://navigation/pantslabyrinth/splash` |
| Pantalla de bienvenida | `braze-pilot://navigation/pantslabyrinth/welcome` |
| Pantalla de listado | `braze-pilot://navigation/pantslabyrinth/listing` |
| Página del carrito | `braze-pilot://navigation/pantslabyrinth/cart` |
| Página de la lista de deseos | `braze-pilot://navigation/pantslabyrinth/wishlist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Vínculos profundos con parámetros

| Pantalla | Vínculo profundo |
| --- | --- |
| Página de detalles del artículo | `braze-pilot://navigation/pantslabyrinth/itemdetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Parámetros aceptados

<style>
table td {
    word-break: break-word;
}
th:nth-child(1), td:nth-child(1) {
    width: 20%;
}
th:nth-child(2), td:nth-child(2) {
    width: 30%;
}
th:nth-child(3), td:nth-child(3) {
    width: 8%;
}
th:nth-child(4), td:nth-child(4) {
    width: 13%;
}
th:nth-child(5), td:nth-child(5) {
    width: 10%;
}
th:nth-child(6), td:nth-child(6) {
    width: 30%;
}
</style>

<table>
    <thead>
        <tr>
            <th>Parámetro</th>
            <th>Descripción</th>
            <th>Obligatoria</th>
            <th>Predeterminado (si no se especifica)</th>
            <th>Tipo</th>
            <th>Ejemplo</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><code>name</code></td>
            <td>El nombre del artículo.</td>
            <td>Sí</td>
            <td></td>
            <td>Cadena</td>
            <td>Vaqueros</td>
        </tr>
        <tr>
            <td><code>price</code></td>
            <td>El precio del artículo.</td>
            <td>Sí</td>
            <td></td>
            <td>Cadena</td>
            <td>85</td>
        </tr>
        <tr>
            <td><code>image</code></td>
            <td>La URL de la imagen del artículo.</td>
            <td>Sí</td>
            <td></td>
            <td>Cadena</td>
            <td><code>https://picsum.photos/400</code></td>
        </tr>
        <tr>
            <td><code>description</code></td>
            <td>La descripción del artículo.</td>
            <td>Sí</td>
            <td></td>
            <td>Cadena</td>
            <td>¡Este artículo es increíble!</td>
        </tr>
        <tr>
            <td><code>quantity</code></td>
            <td>La cantidad del artículo.</td>
            <td>No</td>
            <td>1</td>
            <td>Número</td>
            <td>2</td>
        </tr>
        <tr>
            <td><code>size</code></td>
            <td>Una cadena que representa el tamaño del elemento.</td>
            <td>No</td>
            <td>M</td>
            <td>Cadena</td>
            <td>Grande</td>
        </tr>
        <tr>
            <td><code>colors</code></td>
            <td>Una lista de colores hexadecimales separados por comas. Estos son los colores disponibles para el artículo.</td>
            <td>No</td>
            <td>%23000000</td>
            <td>Cadena</td>
            <td>%230000FF,%23FF0000</td>
        </tr>
        <tr>
            <td><code>color_strings</code></td>
            <td>Una lista de cadenas de colores separadas por comas. Representa los colores en el texto.</td>
            <td>No</td>
            <td>Negro</td>
            <td>Cadena</td>
            <td>Azul, Rojo</td>
        </tr>
        <tr>
            <td><code>selected_color</code></td>
            <td>El índice seleccionado del color que se elegirá en el SELECTOR de color cuando llegues a la pantalla. Si no se utiliza ningún valor, se selecciona el primer color.</td>
            <td>No</td>
            <td>0</td>
            <td>Número</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

## MovieCanon

Estos son los vínculos profundos para la aplicación de la marca ficticia Steppington en Pilot.

### Ejemplo de vínculo profundo

`braze-pilot://navigation/moviecannon/moviedetails?id=1&title=Jaws&thumbnail=https://picsum.photos/400&video=0&description=This%20video%20is%20awesome%21`

### Vínculos profundos sin parámetros

| Pantalla | Vínculo profundo |
| --- | --- |
| Pantalla de inicio | `braze-pilot://navigation/moviecannon/splash` |
| Pantalla de bienvenida | `braze-pilot://navigation/moviecannon/welcome` |
| Página de listado de películas | `braze-pilot://navigation/moviecannon/moviecannon` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Vínculos profundos con parámetros

| Pantalla | Vínculo profundo |
| --- | --- |
| Página de detalles de la película | `braze-pilot://navigation/moviecannon/moviedetails` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Parámetros aceptados

| Parámetro | Descripción | Obligatoria | Tipo | Ejemplo |
| --- | --- | --- | --- | --- |
| `id` | El ID de la película. | Sí | Número | 1 |
| `title` | El título de la película. | Sí | Cadena | Tiburón |
| `thumbnail` | La URL Web de la miniatura que se mostrará antes de la película. | Sí | Cadena | `https://picsum.photos/400` |
| `video` | El índice en la lista de videos que se mostrarán. | No | Número | 0 |
| `description` | La descripción del video. | Sí | Cadena | `This%20video%20is%20awesome%21` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation" }
