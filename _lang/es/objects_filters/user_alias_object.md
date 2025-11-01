---
nav_title: "Objeto alias de usuario"
article_title: Objeto de alias de usuario de API
page_order: 11
page_type: reference
description: "Este artículo de referencia explica los distintos componentes del objeto alias de usuario."

---

# Objeto alias de usuario

> Un alias sirve como identificador único alternativo del usuario. Al utilizar un objeto alias de usuario, puedes establecer un identificador coherente para los análisis que seguirá a un usuario determinado tanto antes como después de que haya iniciado sesión en una aplicación móvil o sitio web. También puedes utilizar este objeto para añadir los identificadores utilizados por un proveedor externo a tus usuarios de Braze para conciliar más fácilmente tus datos externamente.

El objeto alias de usuario consta de dos partes: un `alias_name` para el propio identificador, y un `alias_label` que indica el tipo de alias. Los usuarios pueden tener varios alias con etiquetas diferentes, pero solo un `alias_name` por `alias_label`.

Este objeto se utiliza con frecuencia en todos nuestros puntos finales, y a menudo dentro de otros objetos.

## Cuerpo del objeto

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

### Ejemplo

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "email_id"
  },
  "external_id": "user_456"
}
```