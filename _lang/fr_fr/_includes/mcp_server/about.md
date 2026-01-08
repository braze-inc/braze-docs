# Le serveur MCP de Braze

> Découvrez le serveur MCP de Braze, une connexion sécurisée en lecture seule qui permet aux outils d'intelligence artificielle comme Claude et Cursor d'accéder aux données non PII de Braze pour répondre aux questions, analyser les tendances et fournir des informations sans modifier les données.

{% multi_lang_include mcp_server/beta_alert.md %}

## Qu'est-ce que le protocole de contexte de modèle (MCP) ?

​Model Context Protocol, ou MCP, est une norme qui permet aux agents d'intelligence artificielle de se connecter à des données provenant d'une autre plateforme et de travailler avec elles. Il se compose de deux parties principales :

- **Client MCP :** L'application dans laquelle l'agent d'intelligence artificielle s'exécute, par exemple Cursor ou Claude.
- **Serveur MCP :** Un service fourni par une autre plateforme, comme Braze, qui définit les outils que l'intelligence artificielle peut utiliser et les données auxquelles elle peut accéder.

## À propos du serveur MCP de Braze

Après [avoir configuré le serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, vous pouvez connecter des outils d'intelligence artificielle tels que des agents, des assistants et des chatbots directement à Braze, ce qui leur permet de lire des données agrégées telles que les analyses Canvas et Campaign, les attributs personnalisés, les segments et bien plus encore. Le serveur MCP de Braze est idéal pour :

- Créer des outils alimentés par l'intelligence artificielle qui ont besoin du contexte de Braze.
- Ingénieurs CRM créant des flux de travail en plusieurs étapes pour les agents.
- Les marketeurs techniques expérimentent les requêtes en langage naturel.

Le serveur MCP de Braze prend en charge 38 endpoints en lecture seule qui ne renvoient pas les données des profils utilisateurs de Braze. Vous pouvez choisir d'attribuer seulement certains de ces endpoints à votre clé API Braze pour restreindre davantage les données auxquelles un agent peut accéder.

{% alert warning %}
N'attribuez pas à votre clé API des autorisations qui **ne soient pas** en lecture seule. Les agents peuvent essayer d'écrire ou de supprimer des données dans Braze, ce qui pourrait avoir des conséquences inattendues.
{% endalert %}

## Exemple d'utilisation

Vous pouvez interagir avec Braze en langage naturel à l'aide d'outils tels que Claude ou Cursor. Pour d'autres exemples et bonnes pratiques, consultez [Using the Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![La question "Quelles sont les fonctions de Braze disponibles ?" est posée à Claude, qui y répond.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Curseur %}
![La question "Quelles sont les fonctions de Braze disponibles ?" est posée et trouve une réponse dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Foire aux questions (FAQ) {#faq}

### Quels sont les clients MCP pris en charge ?

Actuellement, seuls [Claude](https://claude.ai/) et [Cursor](https://cursor.com/) sont officiellement pris en charge. Vous devez disposer d'un compte pour l'un de ces clients afin d'utiliser le serveur MCP de Braze.

### A quelles données de Braze mon client MCP peut-il accéder ?

Les clients MCP ne peuvent accéder qu'à des endpoints en lecture seule qui ne sont pas créés pour récupérer des IIP. Ils ne peuvent pas manipuler de données dans Braze.

### Mon client MCP peut-il manipuler les données de Braze ?

Non. Le serveur MCP n'expose que des outils qui traitent des données non PII, en lecture seule.

### Puis-je utiliser un serveur MCP tiers pour Braze ?

L'utilisation d'un serveur MCP tiers pour les données Braze n'est pas recommandée. N'utilisez que le serveur MCP officiel de Braze hébergé sur [PyPi](https://pypi.org/project/braze-mcp-server/).

### Pourquoi le serveur MCP de Braze n'offre-t-il pas d'accès PII ou d'accès en écriture ?

Pour protéger les données tout en permettant l'innovation, nous avons créé le serveur pour qu'il soit limité aux endpoints qui sont en lecture seule et qui ne renvoient généralement pas d'IIP. Cela permet de réduire les risques tout en soutenant des cas d'utilisation intéressants.

### Puis-je réutiliser mes clés API ?

Non. Vous devrez créer une nouvelle clé API pour votre client MCP. N'oubliez pas de ne donner à vos outils d'intelligence artificielle accès qu'à ce avec quoi vous êtes à l'aise, et évitez les autorisations élevées.

### Le serveur MCP de Braze est-il hébergé localement ou à distance ?

Actuellement, le serveur Braze Currents est hébergé localement.

### Pourquoi le curseur n'énumère-t-il que des fonctions ?

Vérifiez si vous êtes en mode demande ou en mode agent. Pour utiliser le serveur MCP, vous devez être en mode agent.

### Que dois-je faire lorsque l'agent renvoie une réponse qui semble incorrecte ?

Lorsque vous travaillez avec des outils tels que le curseur, vous pouvez essayer de modifier le modèle utilisé. Par exemple, si vous l'avez réglé sur automatique, essayez de le changer pour un modèle spécifique et expérimentez pour trouver le modèle le plus performant pour votre cas d'utilisation. Vous pouvez également essayer de démarrer un nouveau chat et de réessayer l'invite. 

Si les problèmes persistent, vous pouvez nous envoyer un e-mail à [mcp-product@braze.com](mailto:mcp-product@braze.com) pour nous en informer. Si possible, incluez une vidéo et développez les fonctions d'appel afin que nous puissions voir quels appels l'agent a tenté.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
