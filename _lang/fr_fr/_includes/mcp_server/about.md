# Le serveur MCP Braze

> Découvrez le serveur MCP Braze, une connexion sécurisée en lecture seule qui permet aux outils d'intelligence artificielle tels que Claude et Cursor d'accéder aux données Braze non personnelles afin de répondre à des questions, d'analyser des tendances et de fournir des informations sans modifier les données.

{% multi_lang_include mcp_server/beta_alert.md %}

## Qu'est-ce que le protocole de contexte de modèle (MCP) ?

​Le protocole MCP (Model Context Protocol) est une norme qui permet aux agents d'intelligence artificielle de se connecter à une autre plateforme et d'utiliser ses données. Il se compose de deux parties principales :

- **Client MCP :** L'application sur laquelle l'agent d'intelligence artificielle est exécuté, telle que Cursor ou Claude.
- **Serveur MCP :** Un service fourni par une autre plateforme, telle que Braze, qui détermine les outils que l'intelligence artificielle peut utiliser et les données auxquelles elle peut accéder.

## À propos du serveur Braze MCP

Après avoir configuré le serveur Braze MCP, vous pouvez connecter des outils d'intelligence{{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %} artificielle tels {% if include.section == "user" %}{{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}que des agents, des assistants et des chatbots directement à Braze, leur permettant ainsi de lire des données agrégées telles que les analyses Canvas et Campaign, les attributs personnalisés, les segments, etc. Le serveur Braze MCP est particulièrement adapté pour :

- Création d'outils basés sur l'intelligence artificielle nécessitant le contexte Braze.
- Les ingénieurs CRM élaborent des workflows en plusieurs étapes pour les agents.
- Les marketeurs techniques explorent les requêtes en langage naturel.

Le serveur MCP Braze prend en charge 38 endpoints en lecture seule qui ne renvoient pas les données des profils utilisateurs Braze. Vous pouvez choisir d'attribuer uniquement certains de ces endpoints à votre clé API Braze afin de restreindre davantage les données auxquelles un agent peut accéder.

{% alert warning %}
Veuillez ne pas attribuer à votre clé API des autorisations qui **ne** sont **pas** en lecture seule. Les agents peuvent tenter d'écrire ou de supprimer des données dans Braze, ce qui pourrait entraîner des conséquences imprévues.
{% endalert %}

## Exemple d'utilisation

Vous pouvez interagir avec Braze en utilisant le langage naturel grâce à des outils tels que Claude ou Cursor. Pour d'autres exemples et bonnes pratiques, veuillez consulter [Utilisation du serveur Braze MCP]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}){{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}.

{% tabs %}
{% tab Claude %}
![« Quelles sont les fonctions Braze à ma disposition ? » : question posée et réponse fournie dans Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![« Quelles sont les fonctions Braze disponibles ? » : question posée et réponse fournie dans Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## Foire aux questions (FAQ) {#faq}

### Quels clients MCP sont pris en charge ?

Seuls [Claude](https://claude.ai/) et [Cursor](https://cursor.com/) sont officiellement pris en charge. Il est nécessaire de disposer d'un compte auprès de l'un de ces clients pour pouvoir utiliser le serveur Braze MCP.

### À quelles données Braze mon client MCP a-t-il accès ?

Les clients MCP peuvent uniquement accéder à des endpoints en lecture seule qui ne sont pas créés pour récupérer des informations personnelles identifiables. Ils ne peuvent pas manipuler les données dans Braze.

### Mon client MCP peut-il manipuler les données Braze ?

Non. Le serveur MCP ne fournit que des outils qui traitent des données non personnelles et en lecture seule.

### Puis-je utiliser un serveur MCP tiers pour Braze ?

Il est déconseillé d'utiliser un serveur MCP tiers pour les données Braze. Veuillez utiliser uniquement le serveur officiel Braze MCP hébergé sur [PyPi](https://pypi.org/project/braze-mcp-server/).

### Pourquoi le serveur Braze MCP n'offre-t-il pas d'accès aux informations personnelles identifiables (PII) ou en écriture ?

Afin de protéger les données tout en favorisant l'innovation, le serveur est limité aux endpoints en lecture seule qui ne renvoient généralement pas d'informations personnelles identifiables. Cela permet de réduire les risques tout en favorisant des cas d'utilisation pertinents.

### Puis-je réutiliser mes clés API ?

Non. Vous devrez créer une nouvelle clé API pour votre client MCP. Veuillez vous assurer de n'accorder à vos outils d'intelligence artificielle que l'accès aux informations que vous jugez approprié et évitez de leur accorder des autorisations étendues.

### Le serveur Braze MCP est-il hébergé localement ou à distance ?

Le serveur Braze MCP est hébergé localement.

### Pourquoi Cursor ne répertorie-t-il que des fonctions ?

Veuillez vérifier si vous êtes en mode demande ou en mode agent. Pour utiliser le serveur MCP, il est nécessaire d'être en mode agent.

### Que dois-je faire lorsque l'agent renvoie une réponse qui semble incorrecte ?

Lorsque vous utilisez des outils tels que Cursor, il peut être utile d'essayer de modifier le modèle utilisé. Par exemple, si vous l'avez réglé sur « auto », essayez de le régler sur un modèle spécifique et testez-le afin de déterminer quel modèle fonctionne le mieux pour votre cas d'utilisation. Vous pouvez également essayer de démarrer une nouvelle conversation et de réessayer l'invite. 

Si les problèmes persistent, veuillez nous contacter par e-mail à l'adresse [mcp-produit@braze.com](mailto:mcp-product@braze.com) pour nous en informer. Si possible, veuillez inclure une vidéo et développer les fonctions d'appel afin que nous puissions examiner les appels que l'agent a tenté de passer.

{% multi_lang_include mcp_server/legal_disclaimer.md %}
