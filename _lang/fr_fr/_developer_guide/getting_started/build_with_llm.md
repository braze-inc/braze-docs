---
nav_title: Créer avec un LLM
article_title: Créer avec un LLM
page_order: 4
description: "Découvrez comment utiliser les assistants de codage basés sur l'intelligence artificielle avec la documentation Braze pour accélérer votre processus d'intégration SDK."
platform:
  - Web
  - React Native
---

# Créer avec un LLM

> Utilisez des assistants de codage basés sur l'intelligence artificielle pour accélérer votre flux de travail d'intégration Braze. Veuillez connecter votre IDE au serveur MCP Braze Documentation via Context7 et obtenez des conseils précis et actualisés sur le SDK directement dans votre environnement de développement.

Les assistants de codage basés sur l'intelligence artificielle peuvent vous aider à écrire du code d'intégration, à résoudre des problèmes et à explorer les fonctionnalités du SDK Braze, mais uniquement s'ils disposent du contexte approprié. Le serveur Braze Docs MCP permet à votre assistant à intelligence artificielle d'accéder directement à la documentation Braze, afin qu'il puisse générer des extraits de code précis et répondre à des questions techniques en se basant sur les dernières références SDK.

## Connexion à la documentation Braze MCP

[Context7](https://context7.com/braze-inc/braze-docs) sert de passerelle entre votre assistant d'intelligence artificielle et la bibliothèque de documentation Braze. En ajoutant Context7 à la configuration MCP de votre IDE, votre assistant d'intelligence artificielle peut interroger l'ensemble de la documentation Braze et récupérer à la demande les références SDK, les exemples de code et les guides d'intégration pertinents.

### Configuration de Context7

Pour connecter votre assistant d'intelligence artificielle au MCP Braze Docs via Context7, veuillez ajouter la configuration suivante au fichier `mcp.json`de votre IDE.

{% tabs %}
{% tab Cursor %}
Dans [Cursor](https://cursor.com/), veuillez vous rendre dans **Paramètres** > **Outils et intégrations** > **Outils MCP** > **Ajouter un MCP personnalisé**, puis ajoutez l'extrait de code suivant :

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Veuillez enregistrer la configuration et redémarrer Cursor. Votre assistant d'intelligence artificielle peut désormais accéder à la documentation Braze via Context7 lorsque vous incluez`use context7`  dans vos invites.
{% endtab %}

{% tab Claude %}
Dans Claude Desktop, veuillez vous rendre dans **Paramètres** > **Développeur** > **Modifier la configuration**, puis ajoutez ce qui suit à votre`claude_desktop_config.json`fichier :

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Veuillez enregistrer la configuration et redémarrer Claude Desktop.
{% endtab %}

{% tab VS Code %}
Veuillez ajouter les éléments suivants à votre fichier VS Code`settings.json``.vscode/mcp.json`ou :

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp@latest"]
    }
  }
}
```

Veuillez enregistrer la configuration et redémarrer VS Code.
{% endtab %}
{% endtabs %}

{% alert note %}
Context7 diffère du [serveur]({{site.baseurl}}/developer_guide/mcp_server/) [Braze MCP]({{site.baseurl}}/developer_guide/mcp_server/). Context7 permet à votre assistant en intelligence artificielle d'accéder à **la documentation Braze**, tandis que le serveur Braze MCP offre un accès en lecture seule aux **données de votre espace de travail Braze** (telles que les campagnes, les segments et les analyses). Vous pouvez utiliser les deux ensemble pour bénéficier d'une expérience de développement assistée par l'intelligence artificielle plus complète.
{% endalert %}

## Consignes de rédaction pour le développement du SDK Braze

Une fois Context7 configuré, veuillez inclure`use context7`  dans vos invites afin d'indiquer à votre assistant à intelligence artificielle d'utiliser la documentation Braze comme contexte. Les exemples suivants illustrent comment rédiger des invites efficaces pour les tâches courantes du SDK.

### React Native SDK

Ces invites illustrent les tâches d'intégration courantes pour le [SDK Braze React native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/react_sdk_setup/).

#### Initialisation du SDK

```text
Using the Braze React Native SDK, show me how to initialize the SDK 
in my App.tsx with an API key and custom endpoint. Include the 
configuration for automatic session tracking. Use context7.
```

#### Enregistrement d'événements personnalisés avec des propriétés

```text
I need to track user activity in my React Native app using the Braze 
React Native SDK. Show me how to log a custom event called 
"ProductViewed" with properties for product_id, category, and price. 
Use context7.
```

#### Configuration des notifications push

```text
Using the Braze React Native SDK, walk me through requesting push 
notification permissions on both iOS and Android 13+. Include the 
code for registering the push token with Braze. Use context7.
```

#### Gestion des messages in-app

```text
Show me how to subscribe to in-app messages using the Braze React 
Native SDK, including how to log impressions and button clicks 
programmatically. Use context7.
```

### Web SDK

Ces invites illustrent les tâches d'intégration courantes pour le [SDK Web Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/).

#### Initialisation du SDK

```text
Using the Braze Web SDK, show me how to initialize the SDK with 
braze.initialize(), including the API key, base URL, and options 
for enabling logging and automatic in-app message display. 
Use context7.
```

#### Suivi des événements personnalisés et des achats

```text
Using the Braze Web SDK, create a JavaScript module that logs a 
custom event called "VideoPlayed" with properties for video_id, 
duration_seconds, and completion_percentage. Also show how to log 
a purchase with product ID, price, currency code, and quantity. 
Use context7.
```

#### Inscription aux notifications push Web

```text
Using the Braze Web SDK, provide the HTML and JavaScript needed to 
register a user for web push notifications after they click a 
"Subscribe to updates" button. Include the service worker setup. 
Use context7.
```

#### Gestion des attributs utilisateur

```text
Using the Braze Web SDK, show me how to set standard user attributes 
(first name, email, country) and custom user attributes (favorite_genre, 
subscription_tier) for the current user. Use context7.
```

## Documentation en texte brut

Vous pouvez accéder à la documentation du Guide du développeur Braze sous forme de fichiers texte brut optimisés pour les outils d'intelligence artificielle et les modèles linguistiques à grande échelle (LLM). Ces fichiers fournissent la documentation Braze dans un format que les assistants basés sur l'intelligence artificielle peuvent analyser et comprendre sans les contraintes du rendu HTML.

| Fichier | Description |
|------|-------------|
| [llms.txt](https://www.braze.com/docs/developer_guide/llms.txt) | Index des pages de documentation pour les développeurs Braze, avec titres et descriptions. Veuillez utiliser ceci comme point de départ pour découvrir la documentation disponible. |
| [llms-full.txt](https://www.braze.com/docs/developer_guide/llms-full.txt) | La documentation complète pour les développeurs Braze dans un seul fichier texte brut, formaté pour être utilisé par les modèles d'apprentissage automatique (LLM). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Ces fichiers respectent la[llms.txt](https://llmstxt.org/)[norme](https://llmstxt.org/), une convention émergente visant à rendre la documentation accessible aux outils d'intelligence artificielle. Vous pouvez référencer ces fichiers directement dans vos invites ou coller leur contenu dans un LLM pour le contexte.
