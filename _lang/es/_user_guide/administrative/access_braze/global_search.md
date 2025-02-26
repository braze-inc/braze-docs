---
nav_title: Búsqueda en el panel de control de Braze
article_title: Búsqueda en el panel de control de Braze
page_order: 0.5
page_type: reference
description: "Más información sobre la búsqueda global en Braze."
---

# Buscar en el panel de control de Braze

Puedes utilizar la barra de búsqueda para encontrar tu trabajo y otra información dentro de tu panel Braze. La barra de búsqueda se encuentra en la parte superior del panel de control de Braze. Haz clic en la barra de búsqueda o pulsa <kbd>Ctrl</kbd> + <kbd>K</kbd> en Windows o <kbd>⌘</kbd> + <kbd>K</kbd> en Mac para saltar directamente a la barra de búsqueda.

![][3]

## ¿Qué puede buscar?

Puede buscar los siguientes elementos y acciones:

- Nombres de las campañas
- Nombres en lienzo
- Bloques de contenido
- Nombres de los segmentos
- Nombres de plantillas de correo electrónico
- [Páginas dentro de Braze](#find-pages-that-have-been-renamed)

{% alert tip %}
Para buscar un texto exacto, ponga el término de búsqueda entre comillas (""). Por ejemplo, la búsqueda ["todos los usuarios"] devolverá todos los elementos que contengan la frase exacta "todos los usuarios" en su nombre.
{% endalert %}

## Características principales

### Atajos de teclado

Navega por los resultados de búsqueda sin esfuerzo con los atajos de teclado:

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2), {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| Acción                      | Atajo de teclado                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| Abrir el menú de búsqueda        | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd> + <kbd>K</kbd> </li> <li>Windows: <kbd>Ctrl</kbd> + <kbd>K</kbd> </li> </ul> {:/}  |
| Desplazarse entre los resultados de búsqueda | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| Seleccionar un resultado de búsqueda      | <kbd>Entrar</kbd>    |
| Cerrar el menú de búsqueda       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Tipo de contenido y etiquetas de estado

Cada resultado de búsqueda se asocia con etiquetas que indican el tipo de contenido del resultado (página, campaña, lienzo, segmento, plantilla de correo electrónico) y el estado (activo, archivado, detenido, etc.).

### Acceder a contenidos abiertos recientemente

En el menú de búsqueda puede volver a consultar los contenidos a los que ha accedido recientemente. La interfaz de búsqueda muestra los resultados abiertos recientemente debajo de la barra de búsqueda, incluidos los elementos con los que se ha interactuado en toda la plataforma Braze. Esto le permite volver a páginas, campañas, lienzos, segmentos o plantillas de correo electrónico que haya visto anteriormente, de modo que puede continuar justo donde lo dejó con menos clics.

![][1]

### Encontrar páginas que han cambiado de nombre

La búsqueda comprende los sinónimos de las páginas que han cambiado de nombre en nuestra [navegación actualizada]({{site.baseurl}}/navigation). Por ejemplo, encontrará "Exportación de datos" cuando busque "Corrientes", ya que esa página ha cambiado de nombre.

<!---

### Quick create campaigns

Search for channels to see quick create options among your top 10 results. For example, searching for "email" shows "Create Email Campaign" or "Create Transactional Email Campaign".

![][2]

--->

### Filtrar contenido activo y borrador

Puede incluir contenidos activos y borradores en los resultados de búsqueda seleccionando **Mostrar sólo activos y borradores**. Por defecto, la opción está activada y se muestran todos los contenidos, incluidos los archivados.

![La opción "Mostrar sólo activos y borradores".][4]

### Buscar emojis

¿Utilizas emojis para nombrar tus obras en Braze? ¡Búscalos! Puedes utilizar emojis como consultas de búsqueda. 😎


[1]: {% image_buster /assets/img/global_search/global_search.png %}
[2]: {% image_buster /assets/img/global_search/search_create_campaign.png %}
[3]: {% image_buster /assets/img/global_search/global_search2.png %}
[4]: {% image_buster /assets/img/global_search/show_active_draft.png %}
