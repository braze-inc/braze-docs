<ul>
<li><code>dispatch_id</code> ist eine ID für eine bestimmte Nachrichtenübermittlung, beispielsweise den Versand einer Kampagne. Alle Push-Ereignisse, die von der gleichen Herkunft stammen, enthalten dieselben <code>dispatch_id</code>. Verwendung <code>dispatch_id</code> Gruppieren Sie Ereignisse, die zur gleichen Sendung gehören, sodass Sie den Lebenszyklus der Push-Nachrichten für diese Sendung (z. B. Senden, Zurückweisen und Öffnung) gruppieren und miteinander in Beziehung setzen können.</li>
<li><code>state_change_source</code> gibt eine String-Zeichenfolge mit dem vollständigen Quellennamen zurück. Beispielsweise gibt der CSV-Import den String <code>CSV import</code>. Die verfügbaren Quellen sind unten aufgeführt:</li>
</ul>
<table class="reset-td-br-1 reset-td-br-2" role="presentation">
<thead>
<tr><th>Quelle</th><th>Beschreibung</th></tr>
</thead>
<tbody>
<tr><td>SDK</td><td>SDK-Endpunkte</td></tr>
<tr><td>Dashboard</td><td>Wenn der Status des Abos eines Nutzers:innen auf der Seite Benutzerprofil im Dashboard aktualisiert wird</td></tr>
<tr><td>Abo Seite</td><td>Wenn sich ein Nutzer:innen über einen E-Mail-Link abmeldet, der nicht das Einstellungscenter ist</td></tr>
<tr><td>REST API</td><td>REST API Endpunkte</td></tr>
<tr><td>CSV-Import</td><td>CSV-Nutzerimport</td></tr>
<tr><td>Präferenzzentrum</td><td>Wenn ein Nutzer:innen über das Einstellungscenter aktualisiert wird</td></tr>
<tr><td>Eingehende Nachricht</td><td>Wenn ein Nutzer:in durch eingehende Nachrichten von Endnutzern über Kanäle wie SMS aktualisiert wird</td></tr>
<tr><td>Migration</td><td>Wenn ein Nutzer:innen durch interne Migrationen oder Wartungsskripte aktualisiert wird</td></tr>
<tr><td>Nutzer:in zusammenführen</td><td>Wenn ein Nutzer:innen durch den Prozess der Zusammenführung von Nutzern aktualisiert wird</td></tr>
<tr><td>Canvas-Schritt „Nutzeraktualisierung“</td><td>Wenn ein Nutzer:innen durch den Canvas-Schritt zum Update aktualisiert wird</td></tr>
</tbody>
</table>
