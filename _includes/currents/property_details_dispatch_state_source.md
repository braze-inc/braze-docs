<ul>
<li><code>dispatch_id</code> is an ID for a specific message dispatch, such as a campaign send. All push events that originate from the same dispatch include the same <code>dispatch_id</code>. Use <code>dispatch_id</code> to group events that belong to the same dispatch, allowing you to group and correlate the push message lifecycle for that dispatch (such as Send, Bounce, and Open).</li>
<li><code>state_change_source</code> returns a string of the full source name. For example, the source CSV import will return the string <code>CSV import</code>. Available sources are listed below:</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>Source</th><th>Description</th></tr>
</thead>
<tbody>
<tr><td>SDK</td><td>SDK endpoints</td></tr>
<tr><td>Dashboard</td><td>When a user's subscription state is updated from the User Profile page in Dashboard</td></tr>
<tr><td>Subscription Page</td><td>When a user unsubscribes through an email link that is not the preference center</td></tr>
<tr><td>REST API</td><td>REST API endpoints</td></tr>
<tr><td>CSV import</td><td>CSV user import</td></tr>
<tr><td>Preference Center</td><td>When a user is updated from the preference center</td></tr>
<tr><td>Inbound Message</td><td>When a user is updated by inbound messages from end-users through channels such as SMS</td></tr>
<tr><td>Migration</td><td>When a user is updated by internal migrations or maintenance scripts</td></tr>
<tr><td>User Merge</td><td>When a user is updated by the user merge process</td></tr>
<tr><td>Canvas User Update Step</td><td>When a user is updated by the Canvas user update step</td></tr>
</tbody>
</table>
