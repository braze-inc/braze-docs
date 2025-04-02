---
nav_title: Ihr Braze Dashboard durchsuchen
article_title: Ihr Braze Dashboard durchsuchen
page_order: 0.5
page_type: reference
description: "Erfahren Sie mehr über die globale Suche in Braze."
---

# Ihr Braze Dashboard durchsuchen

Sie können die Suchleiste verwenden, um Ihre Arbeit und andere Informationen in Ihrem Braze-Dashboard zu finden. Die Suchleiste befindet sich oben auf Ihrem Braze Dashboard. Klicken Sie auf die Suchleiste oder drücken Sie <kbd>Strg</kbd> + <kbd>K</kbd> unter Windows oder <kbd>⌘</kbd> + <kbd>K</kbd> auf dem Mac, um direkt zur Suchleiste zu gelangen.

![][3]

## Wonach können Sie suchen?

Sie können nach den folgenden Artikeln und Aktionen suchen:

- Kampagnennamen
- Canvas-Namen
- Content-Blöcke
- Segmentnamen
- Namen von E-Mail-Templates
- [Seiten innerhalb von Braze](#find-pages-that-have-been-renamed)

{% alert tip %}
Um nach genauem Text zu suchen, setzen Sie Ihren Suchbegriff in Anführungszeichen (""). Wenn Sie zum Beispiel nach ["alle Nutzer:innen"] suchen, erhalten Sie alle Artikel, die den exakten Ausdruck "alle Nutzer:innen" in ihrem Namen enthalten.
{% endalert %}

## Wichtigste Features

### Tastaturkürzel

Navigieren Sie mit Tastaturkürzeln mühelos durch die Suchergebnisse:

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

| Aktion                      | Tastaturkürzel                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| Öffnen Sie das Suchmenü        | {::nomarkdown} <ul> <li> Mac: <kbd>⌘</kbd> + <kbd>K</kbd> </li> <li>Fenster: <kbd>Strg</kbd> + <kbd>K</kbd> </li> </ul> {:/}  |
| Zwischen Suchergebnissen wechseln | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| Wählen Sie ein Suchergebnis      | <kbd>Betreten</kbd>    |
| Schließen Sie das Suchmenü       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Content-Typ und Status-Tags

Jedes Suchergebnis ist mit Tags versehen, die den Inhaltstyp (Seite, Kampagne, Canvas, Segment, E-Mail-Vorlage) und den Status (aktiv, archiviert, gestoppt usw.) des Ergebnisses angeben.

### Zugriff auf kürzlich geöffneten Content

Über das Suchmenü können Sie die zuletzt aufgerufenen Inhalte erneut aufrufen. Die Suchoberfläche zeigt Ihre zuletzt geöffneten Ergebnisse unterhalb der Suchleiste an, einschließlich der Elemente, mit denen Sie auf der gesamten Braze-Plattform interagiert haben. So können Sie zu zuvor angezeigten Seiten, Kampagnen, Canvases, Segmenten oder E-Mail-Vorlagen zurückkehren und mit weniger Klicks genau dort weitermachen, wo Sie aufgehört haben.

![][1]

### Seiten finden, die umbenannt wurden

Die Suche versteht Synonyme für Seiten, die in unserer [aktualisierten Navigation]({{site.baseurl}}/navigation) umbenannt worden sind. Zum Beispiel wird „Datenexport“ gefunden, wenn Sie nach „Currents“ suchen, da diese Seite umbenannt wurde.

<!---

### Quick create campaigns

Search for channels to see quick create options among your top 10 results. For example, searching for "email" shows "Create Email Campaign" or "Create Transactional Email Campaign".

![][2]

--->

### Filter für aktiven und Entwurfs-Content

Sie können aktiven Content und Entwürfe in Ihre Suchergebnisse einbeziehen, indem Sie **Nur aktiven Content und Entwürfe anzeigen** auswählen. Standardmäßig ist das Umschalten aktiviert, und der gesamte Content, einschließlich des archivierten, wird angezeigt.

![Das Umschaltfläche „Nur aktiven Content und Entwürfe anzeigen“.][4]

### Suche nach Emojis

Verwenden Sie Emojis, wenn Sie Ihre Arbeit in Braze benennen? Suchen Sie nach ihnen! Sie können Emojis als Suchanfragen verwenden. 😎


[1]: {% image_buster /assets/img/global_search/global_search.png %}
[2]: {% image_buster /assets/img/global_search/search_create_campaign.png %}
[3]: {% image_buster /assets/img/global_search/global_search2.png %}
[4]: {% image_buster /assets/img/global_search/show_active_draft.png %}
