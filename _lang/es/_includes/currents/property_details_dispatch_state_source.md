<ul>
<li><code>dispatch_id</code> es un ID para el envío de un mensaje específico, como el envío de una campaña. Todos los eventos push que se originan en el mismo envío incluyen lo mismo. <code>dispatch_id</code>. Uso <code>dispatch_id</code> agrupar eventos que pertenecen al mismo envío, lo que te permite agrupar y correlacionar el ciclo de vida de los mensajes push para ese envío (como Enviar, Rebotar y Abrir).</li>
<li><code>state_change_source</code> devuelve una cadena con el nombre completo de la fuente. Por ejemplo, la importación del CSV de origen devolverá la cadena <code>CSV import</code>. A continuación se enumeran las fuentes disponibles:</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>Fuente</th><th>Descripción</th></tr>
</thead>
<tbody>
<tr><td>SDK</td><td>Puntos finales del SDK</td></tr>
<tr><td>Dashboard</td><td>Cuando se actualiza el estado de suscripción de un usuario desde la página Perfil de usuario del Panel de control</td></tr>
<tr><td>Página de suscripción</td><td>Cuando un usuario se da de baja a través de un enlace de correo electrónico que no es el centro de preferencias</td></tr>
<tr><td>API REST</td><td>Puntos finales de la API REST</td></tr>
<tr><td>Importación CSV</td><td>Importación de usuarios CSV</td></tr>
<tr><td>Centro de preferencias</td><td>Cuando se actualiza un usuario desde el centro de preferencias</td></tr>
<tr><td>Mensaje entrante</td><td>Cuando un usuario se actualiza mediante mensajes entrantes de usuarios finales a través de canales como SMS</td></tr>
<tr><td>Migración</td><td>Cuando un usuario se actualiza mediante migraciones internas o scripts de mantenimiento</td></tr>
<tr><td>Fusión de usuarios</td><td>Cuando un usuario es actualizado por el proceso de fusión de usuarios</td></tr>
<tr><td>Paso de actualización de usuario del Canvas</td><td>Cuando un usuario es actualizado por el paso de actualización de usuarios de Canvas</td></tr>
</tbody>
</table>
