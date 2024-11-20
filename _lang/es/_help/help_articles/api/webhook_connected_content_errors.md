---
nav_title: Solución de problemas de webhook y solicitudes de contenido conectado
article_title: Solución de problemas de webhook y solicitudes de contenido conectado
page_order: 3
channel:
  - webhooks
description: "Este artículo explica cómo solucionar los códigos de error de webhook y Contenido conectado, incluyendo cuáles son los errores y los pasos para resolverlos."
---

# Solución de problemas de webhook y solicitudes de contenido conectado

> Este artículo explica cómo solucionar los códigos de error más comunes de los webhooks y el Contenido conectado, y ofrece más explicaciones sobre cómo pueden producirse estos errores en tus solicitudes.

## 4XX errores

`4XX` indican que hay un problema con la solicitud enviada al punto final. Estos errores suelen deberse a solicitudes erróneas, como parámetros mal formados, omisión de cabeceras de autenticación o URL incorrectas.

Consulta la tabla siguiente para ver los detalles del código de error y los pasos para solucionarlo:

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Código de error</th>
      <th>Qué significa</th>
      <th>Pasos para resolver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Petición errónea</b></td>
      <td>Hay una sintaxis inválida en la petición.</td>
      <td>
        <ul>
          <li>Comprueba que la carga útil de la solicitud no contenga errores de sintaxis.</li>
          <li>Confirma que todos los campos obligatorios están incluidos y correctamente formateados.</li>
          <li>Si envías una carga útil JSON, valida la estructura JSON.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 No autorizado</b></td>
      <td>La solicitud requiere la autenticación del usuario.</td>
      <td>
        <ul>
          <li>Comprueba que se incluyen las credenciales de autenticación correctas (como claves de API o tokens) en los encabezados de solicitud.</li>
          <li>Confirma que tienes los permisos de usuario para acceder al punto final.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Prohibido</b></td>
      <td>El endpoint entiende la petición pero se niega a autorizarla.</td>
      <td>
        <ul>
          <li>Comprueba si la clave de API o el token tienen los permisos necesarios.</li>
          <li>Confirma que tienes los permisos de usuario para acceder al punto final.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 No encontrado</b></td>
      <td>El punto final no puede encontrar el recurso solicitado.</td>
      <td>
        <ul>
          <li>Comprueba si la URL del punto final contiene errores tipográficos o rutas incorrectas.</li>
          <li>Confirma que el recurso al que intentas acceder existe.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Método no permitido</b></td>
      <td>El método de solicitud es conocido por el punto final, pero no es compatible con el recurso de destino.</td>
      <td>
        <ul>
          <li>Comprueba el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el punto final admite el método que estás utilizando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Tiempo de espera de la solicitud</b></td>
      <td>El punto final ha agotado el tiempo de procesamiento de la solicitud.</td>
      <td>
        <ul>
          <li>Comprueba el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el punto final admite el método que estás utilizando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflicto</b></td>
      <td>La solicitud está incompleta debido a un conflicto con el estado actual del recurso.</td>
      <td>
        <ul>
          <li>Comprueba el método HTTP (DELETE, GET, POST, PUT) utilizado en la solicitud.</li>
          <li>Confirma que el punto final admite el método que estás utilizando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Demasiadas peticiones</b></td>
      <td>Se envían demasiadas solicitudes en un tiempo determinado.</td>
      <td>
        <ul>
          <li>Reduce el límite de velocidad en tu campaña o paso en Canvas.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## 5XX errores

`5XX` Los errores indican que hay un problema con el punto final. Estos errores suelen deberse a problemas del servidor.

| Código de error                    | Qué significa                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Error interno del servidor** | El punto final encontró una condición inesperada que le impidió completar la solicitud.                                                       |
| **502 Pasarela incorrecta**           | El punto final ha recibido una respuesta no válida del servidor ascendente.                                                                                   |
| **503 Servicio no disponible**   | El punto final no puede gestionar actualmente la solicitud debido a una sobrecarga temporal o a mantenimiento.                                                    |
| **504 Tiempo de espera de la puerta de enlace**       | El punto final no ha recibido una respuesta oportuna del servidor ascendente.                                                                               |
| **599 Error de conexión**      | Braze experimentó un error de tiempo de espera de conexión de red al intentar establecer una conexión con el punto final, lo que significa que el punto final puede ser inestable o estar caído. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Resolver errores 5XX

Aquí tienes consejos para la solución de problemas comunes en `5XX`:

- Revisa el mensaje de error para ver los detalles específicos disponibles en el **Registro de Actividad de Mensajes**. Para los webhooks, ve a la sección **Rendimiento en el tiempo** de la página de inicio de Braze y selecciona las estadísticas de los webhooks. Desde aquí, puedes encontrar la marca de tiempo que indica cuándo se produjeron los errores.
- Asegúrate de no enviar demasiadas peticiones que sobrecarguen el endpoint. Puedes enviar por lotes o ajustar el límite de velocidad para comprobar si así se reducen los errores.
