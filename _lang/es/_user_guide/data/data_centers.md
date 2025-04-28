---
nav_title: Centros de datos
article_title: Centros de datos
page_order: 0.1
page_type: reference
description: "Este artículo de referencia contiene información sobre los centros de datos, incluida su ubicación y cómo registrarse en centros de datos específicos de una región."
---

# Centros de datos

> Los centros de datos Braze están construidos para ofrecerte opciones sobre dónde se procesan y almacenan los datos de tus usuarios. Esto te permite gestionar eficazmente los riesgos relacionados con la soberanía, flexibilidad y gestión de los datos. Cuando eliges un centro de datos Braze, puedes estar seguro de que nuestra plataforma cumple o supera todos los requisitos locales en materia de gestión de datos.

## Cómo funciona

Braze gestiona varios centros de datos ubicados en distintas regiones del mundo. Estos centros de datos permiten que nuestros servicios sean fiables y escalables. Esta distribución geográfica ayuda a minimizar la latencia, que es el tiempo que tardan los datos en viajar entre el servidor y el usuario. 

Esto también significa que cuando un usuario interactúa con tu aplicación o sitio web, sus peticiones se dirigen al centro de datos más cercano, optimizando el rendimiento y reduciendo los tiempos de carga. Al conectarte al centro de datos más cercano, tus usuarios pueden disfrutar de tiempos de carga rápidos, lo que es especialmente importante para la mensajería en tiempo real y la interacción con los usuarios.

Supongamos que tienes una aplicación móvil que envía notificaciones push a los usuarios. Si un usuario de Melbourne recibe una notificación, la solicitud de envío de dicha notificación se dirige al centro de datos más cercano de Australia. En caso de que la aplicación móvil experimente un aumento de usuarios durante un evento promocional, Braze tiene una infraestructura escalable con múltiples centros de datos que pueden gestionar el aumento de la demanda.

## Lista de centros de datos

Consulta la tabla siguiente para ver la lista de centros de datos disponibles.

<style>
table th:nth-child(1) {
    width: 10%;
}
table th:nth-child(2) {
    width: 33%;
}
table th:nth-child(3) {
    width: 33%;
}
table th:nth-child(4) {
    width: 24%;
}
table td {
    word-break: break-word;
}
</style>
<table>
  <thead>
    <tr>
      <th>Región del centro de datos</th>
      <th>URL del panel de control</th>
      <th>Punto final REST</th>
      <th>punto final SDK</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Australia</b></td>
      <td><code>https://dashboard.au-01.braze.com</code></td>
      <td><code>https://rest.au-01.braze.com</code></td>
      <td><code>sdk.au-01.braze.com</code></td>
    </tr>
    <tr>
      <td><b>Europa</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.eu</code></li>
          <li><code>https://dashboard-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.fra-01.braze.eu</code></li>
          <li><code>https://rest.fra-02.braze.eu</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.fra-01.braze.eu</code></li>
          <li><code>sdk.fra-02.braze.eu</code></li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>US</b></td>
      <td>
        <ul>
          <li><code>https://dashboard-01.braze.com</code></li>
          <li><code>https://dashboard-02.braze.com</code></li>
          <li><code>https://dashboard-03.braze.com</code></li>
          <li><code>https://dashboard-04.braze.com</code></li>
          <li><code>https://dashboard-05.braze.com</code></li>
          <li><code>https://dashboard-06.braze.com</code></li>
          <li><code>https://dashboard-07.braze.com</code></li>
          <li><code>https://dashboard-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>https://rest.iad-01.braze.com</code></li>
          <li><code>https://rest.iad-02.braze.com</code></li>
          <li><code>https://rest.iad-03.braze.com</code></li>
          <li><code>https://rest.iad-04.braze.com</code></li>
          <li><code>https://rest.iad-05.braze.com</code></li>
          <li><code>https://rest.iad-06.braze.com</code></li>
          <li><code>https://rest.iad-07.braze.com</code></li>
          <li><code>https://rest.iad-08.braze.com</code></li>
        </ul>
      </td>
      <td>
        <ul>
          <li><code>sdk.iad-01.braze.com</code></li>
          <li><code>sdk.iad-02.braze.com</code></li>
          <li><code>sdk.iad-03.braze.com</code></li>
          <li><code>sdk.iad-04.braze.com</code></li>
          <li><code>sdk.iad-05.braze.com</code></li>
          <li><code>sdk.iad-06.braze.com</code></li>
          <li><code>sdk.iad-07.braze.com</code></li>
          <li><code>sdk.iad-08.braze.com</code></li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Registrarse en centros de datos específicos de una región

Cuando configures tu cuenta Braze, puedes registrarte en centros de datos específicos de una región. Ponte en contacto con tu director de cuentas para obtener información y recomendaciones sobre qué centros de datos funcionan mejor para ti en función de las regiones geográficas de tus usuarios.
