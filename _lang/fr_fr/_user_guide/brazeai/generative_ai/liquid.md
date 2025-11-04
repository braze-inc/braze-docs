---
nav_title: Code liquide
article_title: Générer du code liquide avec BrazeAI
description: "Cet article aborde le fonctionnement de l'intelligence artificielle Liquid Assistant et la manière dont vous pouvez l'utiliser pour générer des extraits de code Liquid pour vos envois de messages."
page_type: reference
page_order: 0.0
---

# Générer du code liquide avec <sup>BrazeAITM</sup>

> L'assistant <sup>BrazeAITM</sup> Liquid est un assistant de chat alimenté par <sup>BrazeAITM</sup> qui aide à générer le Liquid dont vous avez besoin pour personnaliser le contenu des messages.

## À propos de l'assistant liquide <sup>BrazeAITM</sup> 

L'assistant liquide <sup>BrazeAITM</sup> est conçu pour vous aider à écrire un code liquide efficace et adapté à vos besoins de marketeur. Formée à la syntaxe Liquid et à la manière dont les marketeurs utilisent Liquid dans leurs messages, notre intelligence artificielle comprend les nuances de l'élaboration d'un contenu personnalisé.

En outre, en fournissant à l'assistant liquide <sup>BrazeAITM</sup> vos noms d'attributs personnalisés (tels que “favourite_color”) et vos types de données (tels que booléen et chaîne de caractères), notre assistant liquide <sup>BrazeAITM</sup> s'assure que vos messages sont précisément ciblés et alignés sur vos objectifs. En outre, si vous créez des directives de marque, l'assistant liquide de <sup>BrazeAITM</sup> peut utiliser les directives de marque pour mieux personnaliser les sorties générées et pour personnaliser le contenu en fonction de notre propre voix de marque. Les lignes directrices de la marque que vous créez ne seront utilisées que pour personnaliser le contenu pour votre propre usage.

## Canaux pris en charge

Vous pouvez utiliser l'assistant liquide de <sup>BrazeAITM</sup> lors de la création : 
- Messages SMS
- Notifications push
- Envois de messages e-mail en HTML
- Toiles

{% alert note %}
L'assistant travaille sur des messages e-mail et non sur des modèles. Il fonctionne mieux sur les messages e-mail déjà créés.
{% endalert %}

## Générer un code liquide

Pour lancer l'assistant <sup>BrazeAITM</sup> Liquid, sélectionnez l'icône de l'assistant intelligence artificielle dans le compositeur de messages.

\![Message composé avec l'assistant de l'intelligence artificielle.]({% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}){: style="max-width:50%;"}

Vous pouvez choisir l'un des messages-guides inclus ou saisir le vôtre dans la zone de texte.

{% tabs local %}
{% tab use app activity %}
L'invite **Utiliser l'activité de l'app** génère un code liquid pour vous aider à envoyer différents messages en fonction de la date de la dernière utilisation de votre app. Il se peut que l'on vous pose des questions complémentaires afin que l'assistant puisse obtenir un résultat plus précis.

\![Exemple de sortie de l'invite "Use app activity" (utiliser l'activité de l'application).]({% image_buster /assets/img/ai_liquid/use_app_activity.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab add countdown %}
Cette invite génère un code liquid qui envoie un message indiquant le temps restant avant qu'un événement ne se produise. Il vous demandera de fournir des détails sur la date et l'heure de l'événement.

\![Exemple de sortie de l'invite "Ajouter un compte à rebours".]({% image_buster /assets/img/ai_liquid/add_countdown.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab inspire me %}
Cette invite apparaît lorsque votre boîte de message contient du contenu. Il génère une liste d'options parmi lesquelles vous pouvez choisir pour personnaliser votre message avec Liquid. 

Exemple de résultat de l'invite "Inspirez-moi".]({% image_buster /assets/img/ai_liquid/inspire_me.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab improve my liquid %}
Cette invite apparaît lorsque votre compositeur de messages contient du contenu. Sélectionnez-le lorsque vous souhaitez que l'assistant rende votre code plus efficace et plus facile à lire.

\![Exemple de sortie de l'invite "Améliorer mon liquide".]({% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}){: style="max-width:45%;"}
{% endtab %}
{% endtabs %}

Pour générer votre code Liquid, sélectionnez **Mettre à jour le compositeur**.

\![Fenêtre de l'assistant de l'intelligence artificielle avec les invites fournies.]({% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}){: style="max-width:50%;"}
 
Vous pouvez générer un autre message en utilisant la même invite en sélectionnant **Régénérer**. Pour supprimer le message et revenir au message précédent, sélectionnez **Annuler la mise à jour**.

## Attributs liquides {#supported-attributes}

Les attributs suivants sont actuellement en version bêta pour l'assistant liquide <sup>BrazeAITM</sup>:

| Critère d'évaluation - Type de connaissance - Type d'évaluation - Type d'évaluation - Critère d'évaluation - Type d'évaluation
| - | - |
| Liquid (y compris les boucles `for`, les instructions `if`, les mathématiques et autres) | Codage |
| Attributs par défaut et attributs standard de l'utilisateur | Attributs
| Attributs personnalisés ayant l'un de ces types de données : {::nomarkdown}<ul><li>Booléens</li><li>Chiffres</li><li>Chaînes de caractères</li><li>Tableaux</li><li>L'heure</li></ul>{:/} | Attributs
| Contenu connecté | Code
{: .reset-td-br-1 .reset-td-br-2 }

## Meilleures pratiques

Pour vous aider à rédiger des invites efficaces pour l'assistant liquide <sup>BrazeAITM</sup>, consultez nos meilleures pratiques :

### Utiliser le langage naturel

L'assistant liquide <sup>BrazeAITM</sup> est formé pour comprendre le langage naturel. Discutez avec lui comme vous le feriez avec un collègue de travail lorsque vous demandez de l'aide. Il est ainsi plus facile pour l'assistant de comprendre vos besoins et de vous fournir une assistance précise.

### Contexte

Fournir un contexte aide l'assistant liquide de <sup>BrazeAITM</sup> à comprendre la situation globale de votre projet. Il est utile de préciser le contexte, par exemple :

- Nom de votre entreprise et secteur d'activité
- Une campagne sur laquelle vous travaillez, comme le Black Friday ou les ventes de vacances.
- Votre objectif, tel que l'augmentation de votre taux de clics.
- Attributs personnalisés spécifiques que vous souhaitez inclure dans votre message

Le fait d'inclure le contexte dans votre invite permet à l'assistant d'adapter ses réponses à vos besoins. Vous pouvez également inclure des détails de votre campagne, de votre message ou de votre document d'envoi de messages pour mettre l'assistant au courant.

### Soyez précis

L'assistant liquide <sup>BrazeAITM</sup> peut poser des questions de suivi, mais le fait de fournir des détails dès le départ peut permettre d'obtenir des résultats plus précis plus rapidement. Pensez à inclure des détails tels que

- Toute préférence ou exigence connue concernant le message
- Instructions sur la manière de gérer les situations, telles que l'absence de réponse du destinataire du message ou les options de message de repli.
- Lorsque vous demandez un liquide qui utilise du contenu connecté, la documentation pour le point de terminaison de l'API, un exemple de réponse de l'API, ou les deux.

### Soyez créatifs

Sortez des sentiers battus avec vos invites pour voir comment l'assistant liquide <sup>BrazeAITM</sup> peut améliorer votre envoi de messages. Expérimentez avec différents messages et idées, car la créativité peut conduire à des résultats plus attrayants.

## Exemples d'invites

Voici quelques exemples pour vous aider à démarrer :

{% tabs local %}
{% tab gaining knowledge %}
- Qu'est-ce que Liquid, et comment peut-il m'aider à améliorer la personnalisation de mes campagnes marketing au sein de Braze ?
- Quels types de données puis-je utiliser dans Liquid pour personnaliser mes messages marketing, tels que des informations démographiques ou des achats antérieurs ?
{% endtab %}

{% tab personalizing dynamic content %}
- Créer un message qui affiche un contenu différent en fonction du statut de fidélité de mon client. Si nous ne connaissons pas leur statut de fidélité, envoyez un message de repli.
- Rédigez un message dynamique indiquant le produit préféré d'un utilisateur et la date de son dernier achat. S'il n'y a pas de dernier achat, le message est interrompu.
- Écrivez-moi Liquid pour encourager quelqu'un à cliquer sur mon message qui comprend un compte à rebours avec le temps restant. Si l'offre a expiré, interrompez le message.
- Aidez-moi à rédiger un message pour encourager les utilisateurs à revenir et à passer à la caisse s'il leur reste des articles dans leur panier.
- Ecrivez Liquid pour personnaliser un message en fonction du pays d'un client. Je veux remplir le message avec le nom du pays. Si nous ne disposons d'aucun d'entre eux, suggérez-leur de cliquer sur un lien pour mettre à jour leur profil.
- Comment puis-je personnaliser un message de bienvenue avec le prénom d'un utilisateur et rédiger un texte différent en fonction du sexe de l'utilisateur ?
- Ecrivez Liquid pour afficher différents messages en fonction d'un attribut personnalisé, “CUSTOM_ATTRIBUTE_NAME“ et de sa valeur. Je peux envoyer six options différentes. S'il n'y a pas de valeur pour l'attribut personnalisé, je veux envoyer un message substitutif.
{% endtab %}

{% tab handling outliers %}
- Pouvez-vous me donner des exemples d'utilisation de Liquid dans les campagnes marketing pour augmenter les taux d'engagement et de conversion ?
- Quels sont les cas d'utilisation courants des messages textuels Liquid in pour les soldes d'été, tels que les rappels de panier abandonné ou les promotions personnalisées ?
{% endtab %}
{% endtabs %}

{% alert tip %}
Faites-nous savoir si vous avez eu des idées ou des expériences intéressantes en réservant une [session de feedback](https://research.rallyuxr.com/braze/schedule/clxxhw8em0d071ak4b279553s?channel=share) avec nous.
{% endalert %}

{% multi_lang_include brazeai/generative_ai/policy.md %}
