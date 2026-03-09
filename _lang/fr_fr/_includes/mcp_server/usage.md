# Utilisation du serveur Braze MCP

> Découvrez comment interagir avec vos données Braze à l'aide du langage naturel grâce à des outils tels que Claude et Cursor. Pour obtenir des informations générales, veuillez consulter [le serveur Braze MCP]{% if include.section == "user" %}.{{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/mcp_server/){% endif %}

{% multi_lang_include mcp_server/beta_alert.md %}

## Conditions préalables

Avant de pouvoir utiliser cette fonctionnalité, il est nécessaire de configurer le serveur Braze MCP.{% if include.section == "user" %}{{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}

## Bonnes pratiques

Lorsque vous utilisez le serveur Braze MCP via des outils de langage naturel tels que Claude et Cursor, veuillez garder à l'esprit ces conseils afin d'obtenir les meilleurs résultats :

- Les LLM peuvent commettre des erreurs, il est donc important de toujours vérifier leurs réponses.
- Pour l'analyse des données, veuillez préciser la période qui vous intéresse. Les distances plus courtes fournissent souvent des résultats plus précis.
- Veuillez utiliser [la terminologie](https://www.braze.com/resources/articles/glossary) exacte [de Braze](https://www.braze.com/resources/articles/glossary) afin que votre LLM appelle la fonction appropriée.
- Si les résultats semblent incomplets, veuillez demander à votre assistant de recherche de poursuivre ou d'approfondir ses recherches.
- Veuillez essayer des suggestions créatives. Selon votre client MCP, il est possible que vous puissiez exporter un fichier CSV ou d'autres fichiers utiles.

## Exemples d’utilisation

Après avoir configuré le serveur Braze MCP,{{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %} vous pouvez interagir avec Braze en {% if include.section == "user" %}utilisant le langage naturel grâce à des outils tels que{{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %} Claude ou Cursor. Voici quelques exemples pour vous aider à démarrer :

### Quelles sont les fonctionnalités Braze à ma disposition ?

{% tabs %}
{% tab Claude %}
![« Quelles sont les fonctions Braze à ma disposition ? » : question posée et réponse fournie dans Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![« Quelles sont les fonctions Braze disponibles ? » : question posée et réponse fournie dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### Obtenir des informations sur un ID Canvas

{% tabs %}
{% tab Claude %}
![« Obtenir des informations sur un ID de canvas » : question posée et réponse donnée dans Claude.]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![« Obtenir des informations sur un ID de canvas » : question posée et réponse fournie dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### Veuillez me montrer mes toiles récentes.

{% tabs %}
{% tab Claude %}
![« Montrez mes toiles récentes » : question posée et réponse donnée dans Claude.]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![« Montrez mes toiles récentes » : question posée et réponse donnée dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
