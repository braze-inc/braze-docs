<ul>
<li><code>dispatch_id</code> est un ID pour un envoi de messages spécifique, tel qu'un envoi de campagne. Tous les événements "push" qui proviennent du même envoi comprennent le même <code>dispatch_id</code>. Utilisation <code>dispatch_id</code> pour regrouper les événements qui appartiennent au même envoi, ce qui vous permet de regrouper et de corréler le cycle de vie du message push pour cet envoi (comme l'envoi, le rebond et l'ouverture).</li>
<li><code>state_change_source</code> renvoie une chaîne de caractères contenant le nom complet de la source. Par exemple, l'importation de la source CSV renverra la chaîne de caractères suivante <code>CSV import</code>. Les sources disponibles sont énumérées ci-dessous :</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>Source</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>SDK</td><td>Endpoints SDK</td></tr>
<tr><td>Tableau de bord</td><td>Lorsque l'état de l'abonnement d'un utilisateur est mis à jour à partir de la page Profil de l'utilisateur dans le tableau de bord</td></tr>
<tr><td>Page d'abonnement</td><td>Lorsqu'un utilisateur se désinscrit par le biais d'un lien d'e-mail qui n'est pas le centre de préférences</td></tr>
<tr><td>API REST</td><td>Points d'extrémité de l'API REST</td></tr>
<tr><td>Importation CSV</td><td>Importation d'utilisateurs CSV</td></tr>
<tr><td>Centre de préférences</td><td>Lorsqu'un utilisateur est mis à jour à partir du centre de préférences</td></tr>
<tr><td>Message entrant</td><td>Lorsqu'un utilisateur est mis à jour par des messages entrants provenant d'utilisateurs finaux par le biais de canaux tels que les SMS</td></tr>
<tr><td>Migration</td><td>Lorsqu'un utilisateur est mis à jour par des migrations internes ou des scripts de maintenance.</td></tr>
<tr><td>Fusion d'utilisateurs</td><td>Lorsqu'un utilisateur est mis à jour par le processus de fusion des utilisateurs</td></tr>
<tr><td>Étape de mise à jour de l’utilisateur du canvas</td><td>Lorsqu'un utilisateur est mis à jour par l'étape du canvas de mise à jour de l'utilisateur</td></tr>
</tbody>
</table>
