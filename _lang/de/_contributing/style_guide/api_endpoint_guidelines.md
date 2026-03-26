---
nav_title: Richtlinien zur API-Endpunkt-Dokumentation
article_title: Richtlinien zur API-Endpunkt-Dokumentation
description: "Richtlinien für die Dokumentation von Braze API-Endpunkten."
page_order: 3
noindex: true
---

# Richtlinien zur API-Endpunkt-Dokumentation

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

> Im Allgemeinen sollte die Dokumentation für API-Endpunkte den in den [Allgemeinen Richtlinien]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#general-guidelines) beschriebenen Vorgaben folgen. Es gibt jedoch spezielle Themen, die andere Inhaltsrichtlinien erfordern können, die in diesem Dokument aufgeführt sind.

Braze unterstützt die folgenden REST API-Methoden:

* GET  
* DELETE  
* PATCH  
* POST  
* PUT

## Einen neuen Endpunkt-Artikel erstellen

Wenn Sie einen neuen Endpunkt-Artikel erstellen, stellen Sie sicher, dass Sie diesen Endpunkt auch in den [Braze API-Leitfaden]({{site.baseurl}}/api/home) aufnehmen, damit der Endpunkt durchsuchbar ist. Navigieren Sie zum Ordner **`_docs`** **`> _api`** und zur Datei **`> home.md`**, um den Endpunkt mit seinem Pfad und einer einzeiligen Beschreibung hinzuzufügen.

## Endpunkte referenzieren

Im Allgemeinen gibt es keine einheitliche Konvention für die Bezugnahme auf Endpunkte in der Dokumentation. Wenn Sie auf Braze-Endpunkte verweisen, nutzen Sie Ihr bestes Urteilsvermögen, um zu entscheiden, wie Sie je nach Anwendungsfall auf einen Endpunkt verweisen.

Sie können auf einen Endpunkt über seinen Pfad verweisen (zum Beispiel `/users/track`) oder über den Namen des Endpunkts, gefolgt vom Wort „Endpunkt" (zum Beispiel der Track-User-Endpunkt). Wenn Ihr Pfad besonders lang ist, verwenden Sie stattdessen den Endpunktnamen.

Verwenden Sie Satzschreibweise, wenn Sie den Endpunkt über seinen Namen referenzieren. Verwenden Sie Code-Text, wenn Sie den Endpunkt über seinen Pfad referenzieren.

Schreiben Sie das Wort „Endpunkt" nicht groß, es sei denn, Sie beziehen sich direkt auf einen Abschnittsnamen. Verwenden Sie nicht das Wort „API", wenn Sie direkt auf einen Endpunkt verweisen.

Es gibt Fälle, in denen ein Endpunkt als API bezeichnet wird. Zum Beispiel ist dies eine korrekte Aussage: „Braze verwendet eine REST API mit vielen Endpunkten", wenn allgemein über Braze-Endpunkte gesprochen wird.

Setzen Sie keine Anführungszeichen um den Endpunktnamen. Verwenden Sie keinen einfachen Text, wenn Sie auf den Pfad verweisen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Verwenden Sie den Endpunkt „Generate preference center URL", um die nächsten Schritte abzuschließen.</td><td style="width: 50%;">Verwenden Sie <code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code>, um die nächsten Schritte abzuschließen.</td></tr>
<tr><td style="width: 50%;">Verwenden Sie den Endpunkt <code>/users/track</code>.</td><td style="width: 50%;">Verwenden Sie den „Users Track" API-Endpunkt.</td></tr>
</tbody>
</table>
{:/}

### Verlinkung zu Endpunkt-Artikeln

Wenn Sie auf Endpunkt-Artikel verweisen, verwenden Sie [aussagekräftigen Linktext]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#writing-links), der auch ohne Kontext verständlich ist. Wenn Sie den Pfad des Endpunkts als Link verwenden, stellen Sie sicher, dass der umgebende Text Details enthält, da der Pfad die Funktion des Endpunkts möglicherweise nicht klar vermittelt.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Löschen Sie Nutzerprofile mit dem Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete-User-Endpunkt</a>.</td><td style="width: 50%;">Löschen Sie Nutzerprofile mit dem Braze <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a>-Endpunkt.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code>-Endpunkt</a></td><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a>-Endpunkt</td></tr>
</tbody>
</table>
{:/}

## Überschriften

Die Einleitung eines Endpunkt-Artikels muss die folgenden Informationen enthalten:

* Anfragetyp und Endpunkt-Pfad-URL  
* Eine kurze Beschreibung des Endpunkts, beginnend mit „Verwenden Sie diesen Endpunkt, um …"  
* Link „In Postman ansehen"  
* Ein Hinweis-Alert mit der erforderlichen REST-API-Schlüssel-Berechtigung

Verwenden Sie diese Checkliste, um sicherzustellen, dass die richtigen Überschriften (und Inhalte) in jedem Endpunkt-Artikel enthalten sind und in der aufgeführten Reihenfolge stehen. Beachten Sie, dass es Unterüberschriften geben kann, die für einen Endpunkt spezifisch sind, wie z. B. verschiedene Arten von Beispielanfragen.

* Rate-Limit  
* Pfadparameter  
* Anfragekörper  
* Anfrageparameter  
* Beispielanfrage  
* Antwortparameter  
* Beispielantwort  
* Fehlerbehebung (falls zutreffend)

Weitere Formatierungsrichtlinien finden Sie unter [Überschriften und Titel]({{site.baseurl}}/contributing/style_guide/writing_style_guide/#headings-and-titles).

### Pfadparameter

Wenn es Pfadparameter für den Endpunkt gibt, fügen Sie eine Überschrift und Tabelle für Pfadparameter ein (ähnlich der Tabelle für Anfrageparameter).

Wenn es keine Pfadparameter für den Endpunkt gibt, fügen Sie eine Überschrift für Pfadparameter und den folgenden Hinweis ein: „Es gibt keine Pfadparameter für diesen Endpunkt."

Wenn es weder Pfad- noch Anfrageparameter für den Endpunkt gibt, fassen Sie den Hinweis in einem Abschnitt zusammen, wie unten gezeigt.

{% raw %}
{::nomarkdown}
<div style="margin-left: 2em;">
<code>
## Pfad- und Anfrageparameter <br>
Es gibt keine Pfad- oder Anfrageparameter für diesen Endpunkt.
</code>
</div>
{:/}
{% endraw %}

## Namenskonventionen

Beginnen Sie jeden Endpunktnamen mit einem aktiven Verb nach seiner Methode. So erkennen Nutzer:innen sofort die Funktion des Endpunkts.

Verwenden Sie die API-Methode nicht als führendes Verb für den Endpunktnamen.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">POST: Create new user alias</td><td style="width: 50%;">POST: New user alias</td></tr>
<tr><td style="width: 50%;">GET: Look up an existing dashboard user account</td><td style="width: 50%;">GET: Existing dashboard user account</td></tr>
</tbody>
</table>
{:/}

Ausnahmen von dieser Namenskonvention sind die Endpunkte im [Abschnitt „Export"]({{site.baseurl}}/api/endpoints/export), da der Abschnittsname ein Verb ist, das anzeigt, dass die aufgeführten Informationen exportiert werden können.

## API-Schlüssel-Berechtigungen

API-Schlüssel-Berechtigungen sind Berechtigungen, die Sie einer Nutzerin oder einem Nutzer oder einer Gruppe zuweisen können, um deren Zugriff auf bestimmte API-Aufrufe einzuschränken. Fügen Sie für jede Endpunkt-Dokumentation den folgenden Hinweis nach dem Postman-Dokumentationslink ein:

> Um diesen Endpunkt zu verwenden, müssen Sie einen API-Schlüssel mit der Berechtigung `permission_name_here` generieren.

Die vollständige Liste der API-Schlüssel-Berechtigungen finden Sie unter **Einstellungen > API-Schlüssel** im Bereich **Setup und Tests** im Braze-Dashboard. Wählen Sie einen API-Schlüssel mit Vollzugriff aus (der Schlüsselname enthält in der Regel den Ausdruck „full access"). Jeder Berechtigungsname sollte im Allgemeinen dem Endpunktnamen entsprechen.

Beachten Sie, dass SCIM-Endpunkte keine aufgeführten API-Schlüssel-Berechtigungen haben, da sie spezifisch für die SCIM-Integration sind, die außerhalb der Entwicklungskonsole stattfindet.

## Rate-Limits

Im Allgemeinen sollte Ihr Rate-Limit die Anzahl der Anfragen und den zugewiesenen Zeitraum angeben.

Achten Sie auf Endpunkte, die sich ein gemeinsames Rate-Limit teilen. Zum Beispiel teilen sich alle asynchronen Katalog-Artikel-Endpunkte ein gemeinsames Rate-Limit, daher ist es wichtig, dies in den jeweiligen Artikeln anzugeben.

### So aktualisieren Sie die Rate-Limit-Datei

Wenn Ihre Endpunkt-Dokumentation die Aktualisierung oder Auflistung eines neuen Rate-Limits erfordert, navigieren Sie zu **_docs > _api > api_limits.md**, um die Änderungen am Rate-Limit vorzunehmen.

## Parameter

Definieren Sie sowohl die Anfrage- als auch die Antwortparameter in zwei separaten Tabellen. Diese Tabellen sollten die folgenden Spalten enthalten:

* **Parameter**  
* **Erforderlich**  
* **Datentyp**  
* **Beschreibung**

Wenn Sie direkt auf die Parameter eines Endpunkts verweisen und die Werte in der Spalte **Parameter** auflisten, verwenden Sie Code-Text. Wenn Sie die Werte in den Spalten **Erforderlich**, **Datentyp** und **Beschreibung** auflisten, verwenden Sie Großschreibung am Anfang.

### Platzhaltertext

Verwenden Sie für Platzhaltertext geschweifte Klammern mit einer kurzen Beschreibung dessen, was die Nutzerin oder der Nutzer einfügen soll.

Verwenden Sie für API-Schlüssel-Platzhalter `YOUR_REST_API_KEY`, nicht `YOUR-REST-API-KEY`.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">Richtig</th><th style="width: 50%;">Falsch</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</code></td><td style="width: 50%;"><code>/preference_center/v1/[preferenceCenterExternalId]</code></td></tr>
<tr><td style="width: 50%;"><code>/scim/v2/Users/{userId}</code></td><td style="width: 50%;"><code>/url/[userId]/scim/v2/Users/userID</code></td></tr>
</tbody>
</table>
{:/}

Verwenden Sie für API-Schlüssel-Platzhalter `YOUR_REST_API_KEY` (mit Unterstrichen), nicht `YOUR-REST-API-KEY` (mit Bindestrichen).

## Anfragen und Antworten

Eine API-Anfrage enthält den Header und die Anfrageparameter. Die Anfrageparameter sollten wie folgt formatiert sein:

```bash
parameter": (required/optional, data type) A brief description
```

Hier ist ein Beispiel für einen Anfragekörper für den [Endpunkt „Create new user alias"]({{site.baseurl}}/api/endpoints/user_data/post_user_alias/):

```bash
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "user_aliases": (required, array of new user alias object)
}
```

Verwenden Sie doppelte gerade Anführungszeichen (" "), um Parameter zu kennzeichnen, die Strings oder Arrays in einer Beispielanfrage sind. Stellen Sie sicher, dass alle geöffneten Klammern geschlossen werden.

Eine API-Antwort enthält den Antwortkörper, Header und den HTTP-Statuscode. Fügen Sie immer eine Beispielantwort ein. Dieses Beispiel muss ein einfaches Textbeispiel enthalten, das den Parameter beschreibt. Hier ist eine Beispielantwort für den [Endpunkt „Update user alias"]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/#example-request).

```bash
curl --location --request POST 'https://rest.iad-01.braze.com/users/alias/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "alias_updates" :[
    {
      "alias_label": "example_alias_label",
      "old_alias_name" : "example_old_alias_name",
      "new_alias_name" : "example_new_alias_name"
    }
  ]
}'
```

### Status- und Fehlercodes

Statuscodes zeigen an, ob eine bestimmte Anfrage einer Nutzerin oder eines Nutzers erfolgreich abgeschlossen wurde. Es kann hilfreich sein, die Statuscodes aufzuführen, damit Nutzer:innen wissen, was als Erfolg gilt. Zum Beispiel können 400 und 404 Indikatoren für eine Fehlerantwort des Endpunkts sein.

Wenn Ihre Endpunkt-Dokumentation die Auflistung von Fehlercodes erfordert, verlinken Sie stattdessen auf den Artikel [API-Fehler und -Antworten]({{site.baseurl}}/api/errors/) unter dem Ordner **_docs** **> _api** und der Datei **> errors.md**.

## Beispielcode

Beispielcode, wie Beispielanfragen und -antworten, sollte mit minimalem Aufwand kopiert und verwendet werden können. Mit Ausnahme von Platzhaltertext (zum Beispiel der API-Schlüssel im Header) sollten Beispielanfragen sofort funktionieren. Verwenden Sie Postman, um sicherzustellen, dass Ihre Anfrage korrekt formatiert ist.

### Formatierter versus minimierter Code

Wenn die Anfrage des Endpunkts einen Body enthält, formatieren Sie das Beispiel in Postman im lesbaren Format (Beautify). Dies erleichtert es Entwickler:innen, die Braze-Konventionen lernen, jeden Teil der Anfrage zu verstehen.

Wenn der Anfragekörper des Endpunkts sehr kurz ist oder keinen Body enthält, minimieren Sie die Anfrage, sodass unnötige Leerzeichen entfernt werden. Verwenden Sie dafür ein Tool wie [JSON Minifier](https://codebeautify.org/jsonminifier).

### Inline-Kommentare

Verwenden Sie zwei Schrägstriche (//), um einzeilige Kommentare im Beispielcode zu kennzeichnen.

Inline-Kommentare sind wertvolle Werkzeuge, um die Aufmerksamkeit der Nutzerin oder des Nutzers auf einen bestimmten Codeabschnitt zu lenken, die Funktion eines Codeblocks zu erklären oder zusätzlichen Kontext bereitzustellen.

Verwenden Sie Inline-Kommentare, um schnell zu zeigen, wo die Logikschicht der Nutzerin oder des Nutzers platziert werden würde und wie sie auf den SDK-Code verweisen würde. Verwenden Sie einfache, aber realistische Beispiele. Zum Beispiel ist ein Beispielattribut wie „favorite_movie" aussagekräftiger als „example_attribute". Selbst wenn das Unternehmen der Nutzerin oder des Nutzers den Lieblingsfilm eines Endnutzers nicht trackt oder sich nicht dafür interessiert, zeigt dieses Beispiel die *Art* von Anwendungsfällen, die über dieses Attribut verfolgt werden könnten. Generische Beispiele erzeugen nicht dasselbe intuitive Verständnis.

Vermeiden Sie Inline-Kommentare, die einfach lesbaren Code oder Methodennamen wiederholen. Verwenden Sie stattdessen verschiedene Synonyme für die Braze-spezifischen Methoden und Parameter, um nicht-englischen Muttersprachler:innen eine Orientierungshilfe zu bieten.

Halten Sie sich im Allgemeinen an die standardmäßigen englischen Konventionen, wenn Sie Inline-Kommentare verfassen. Beginnen Sie beispielsweise Sätze mit einem Großbuchstaben, schreiben Sie Wörter vollständig aus usw.

## Zusätzliche Ressourcen

- [Google Developer Documentation Style Guide](https://developers.google.com/style)  
  - [API reference code and comments](https://developers.google.com/style/api-reference-comments)