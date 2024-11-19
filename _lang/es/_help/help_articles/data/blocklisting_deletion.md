---
nav_title: Diferencia entre bloquear y eliminar
article_title: Diferencia entre bloquear y eliminar
page_order: 2

page_type: solution
description: "Este artículo de ayuda te explica la diferencia entre el bloqueo y la eliminación de atributos."
---

# Diferencia entre agregar a la lista de bloqueo y eliminar

Para entender la diferencia entre agregar a la lista de bloqueo y eliminar atributos en Braze, revisemos los resultados de cada acción:

- **Lista de bloqueo:** Si se agregan a la lista de bloqueo atributos personalizados, eventos o compras, permanecerán en el perfil de usuario, pero no se procesarán nuevas solicitudes del atributo.
- **Eliminación:** Si se eliminan atributos personalizados, eventos o compras, se eliminarán los datos. Sin embargo, Braze seguirá aceptando nuevas solicitudes entrantes para ese atributo si se sigue haciendo un seguimiento a través del SDK o se carga a través de la API o CSV.

## ¿Qué debo hacer?

Para llevar a cabo el bloqueo, Braze tendrá que enviar la información de la lista de bloqueo al dispositivo de cada usuario, y será una operación que consumirá muchos datos, lo que, idealmente, intentamos evitar. Además, si la lista es demasiado grande (> 100 atributos, eventos o compras), tu aplicación puede empezar a ralentizarse. 

Si ya no piensas enviar atributos a Braze, la ruta de eliminación sería la solución recomendada.

Independientemente de tu ruta, los atributos personalizados, eventos y compras que desees eliminar ya no aparecerán en la página **Gestionar espacio de trabajo**, que los elimina como filtros de segmento. Los datos a nivel de usuario permanecerán en los perfiles. 