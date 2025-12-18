# Utilisation du serveur MCP de Braze

> Apprenez à interagir avec vos données Braze en langage naturel à l'aide d'outils tels que Claude et Cursor. Pour des informations plus générales, voir [Serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## Conditions préalables

Avant de pouvoir utiliser cette fonctionnalité, vous devez [configurer le serveur MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## Bonnes pratiques

Lorsque vous utilisez le serveur MCP de Braze à l'aide d'outils de langage naturel tels que Claude et Cursor, gardez ces conseils à l'esprit pour obtenir les meilleurs résultats :

- Les LLM peuvent faire des erreurs, veillez donc à toujours vérifier leurs réponses.
- Pour l'analyse des données, définissez clairement la période dont vous avez besoin. Des distances plus courtes donnent souvent des résultats plus précis.
- Utilisez la [terminologie](https://www.braze.com/resources/articles/glossary) exacte [de Braze](https://www.braze.com/resources/articles/glossary) pour que votre LLM appelle la bonne fonction.
- Si les résultats semblent incomplets, demandez à votre MLD de continuer ou d'approfondir.
- Essayez d'être créatif ! En fonction de votre client MCP, vous pourrez peut-être exporter un fichier CSV ou d'autres fichiers utiles.

## Exemples d’utilisation

Après [avoir configuré le serveur MCP de Braze]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, vous pouvez interagir avec Braze en langage naturel à l'aide d'outils tels que Claude ou Cursor. Voici quelques exemples pour vous aider à démarrer :

### Quelles sont les fonctions de Braze dont je dispose ?

{% tabs %}
{% tab Claude %}
![La question "Quelles sont les fonctions de Braze disponibles ?" est posée à Claude, qui y répond.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Curseur %}
![La question "Quelles sont les fonctions de Braze disponibles ?" est posée et trouve une réponse dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### Obtenir des informations sur l'ID d'une toile

{% tabs %}
{% tab Claude %}
![La question "Obtenir des informations sur un ID canvas" est posée et traitée dans Claude.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Curseur %}
![La question "Obtenir des informations sur un ID de toile" est posée et traitée dans le curseur.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### Montrez-moi mes toiles récentes

{% tabs %}
{% tab Claude %}
![La question "Montrez mes toiles récentes" est posée et trouve une réponse dans Claude.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Curseur %}
![La question "Montrer mes toiles récentes" est posée et la réponse est donnée dans Curseur.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
