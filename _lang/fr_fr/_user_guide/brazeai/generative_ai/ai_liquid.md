---
nav_title: Assistant liquide de BrazeAI
article_title: Assistant liquide de BrazeAI
description: "Cet article aborde le fonctionnement de l'intelligence artificielle Liquid Assistant et la manière dont vous pouvez l'utiliser pour générer des extraits de code Liquid pour vos envois de messages."
page_type: reference
page_order: 5
---

# Assistant Liquid BrazeAI<sup>TM</sup>

> L'assistant <sup>BrazeAITM</sup> Liquid est un assistant de chat alimenté par <sup>BrazeAITM</sup> qui aide à générer le Liquid dont vous avez besoin pour personnaliser le contenu des messages.

L'assistant Liquid BrazeAI<sup>TM</sup> vous permet de générer des codes Liquid à partir de modèles, de recevoir des suggestions de codes Liquid personnalisés et d’optimiser les codes Liquid existants avec l'aide de BrazeAI<sup>TM</sup>. L'assistant fournit également des annotations expliquant le code Liquid utilisé, ce qui vous permet de mieux comprendre la syntaxe Liquid et d'apprendre à écrire votre propre code Liquid.

## Canaux pris en charge

Vous pouvez utiliser l'assistant liquide de <sup>BrazeAITM</sup> lors de la création : 
- messages SMS
- Notifications push
- Envois de messages e-mail en HTML
    - L'assistant travaille sur des messages e-mail et non sur des modèles et fonctionne mieux sur des messages e-mail déjà créés.
- Canvas

## Fonctionnement

L'assistant Liquid BrazeAI<sup>TM</sup> est conçu pour vous aider à écrire du code Liquid efficace et adapté à vos besoins marketing. Formée à la syntaxe Liquid et à la manière dont les marketeurs utilisent Liquid dans leurs messages, notre intelligence artificielle comprend les nuances de l'élaboration d'un contenu personnalisé. En outre, en fournissant à l'assistant liquide de <sup>BrazeAITM</sup> vos noms d'attributs personnalisés (tels que "couleur_favorite") et vos types de données (tels que booléen et chaîne de caractères), notre assistant liquide de <sup>BrazeAITM</sup> s'assure que vos messages sont précisément ciblés et alignés sur vos objectifs. En outre, si vous créez des directives de marque, l'assistant Liquid BrazeAI<sup>TM</sup> peut les utiliser pour mieux personnaliser les textes et le contenu générés en fonction de la voix de votre marque. Les lignes directrices de la marque que vous créez ne seront utilisées que pour personnaliser le contenu pour votre propre usage. 

## Générer un code Liquid

Pour lancer l'assistant Liquid BrazeAI<sup>TM</sup>, sélectionnez l'icône de l'assistant IA dans le composeur de messages.

![Compositeur de messages avec l'assistant de l'intelligence artificielle.][1]{: style="max-width:50%;"}

Vous pouvez choisir une [invite fournie](#provided-prompts) ou saisir la vôtre dans la zone de texte. Pour générer votre code Liquid, sélectionnez **Mettre à jour le composeur**.

![Fenêtre de l'assistant de l'intelligence artificielle avec les invites fournies.][2]{: style="max-width:50%;"}
 
Vous pouvez générer un autre message en utilisant la même invite en sélectionnant **Régénérer**. Pour supprimer le message et revenir au message précédent, sélectionnez **Annuler la mise à jour**.

### Messages-guides fournis

L'assistant Liquid BrazeAI<sup>TM</sup> formule une série d'invites qui vous aideront à démarrer avec Liquid. Vous trouverez ci-dessous quelques-unes des questions posées.

#### Utiliser l'activité de l'application

L'invite **Utiliser l'activité de l'app** génère un code liquid pour vous aider à envoyer différents messages en fonction de la date de la dernière utilisation de votre app. L’assistant peut également vous poser d’autres questions afin de pouvoir générer un résultat plus précis.

![Exemple de sortie de l'invite « Utiliser l’activité de l’appli ».][3]{: style="max-width:45%;"}

#### Ajouter un compte à rebours

Cette invite génère un code liquid qui envoie un message indiquant le temps restant avant qu'un événement ne se produise. Vous serez invité à fournir des détails sur la date et l'heure de l'événement.

![Exemple de sortie de l'invite "Ajouter un compte à rebours".][4]{: style="max-width:45%;"}

#### Me donner de l’inspiration

Cette invite apparaît lorsque votre boîte de message contient du contenu. Il génère une liste d'options parmi lesquelles vous pouvez choisir pour personnaliser votre message avec Liquid. 

![Exemple de sortie de l'invite "Inspirez-moi".][5]{: style="max-width:45%;"}

#### Améliorer mon Liquid

Cette invite apparaît lorsque votre compositeur de messages contient du contenu. Sélectionnez-le lorsque vous souhaitez que l'assistant rende votre code plus efficace et plus facile à lire.

![Exemple de sortie de l'invite « Améliorer mon Liquid ».][6]{: style="max-width:45%;"}

## Attributs pris en charge dans la version bêta

| Critère d'évaluation - Type de connaissance - Type d'évaluation - Type d'évaluation - Critère d'évaluation - Type d'évaluation
| - | - |
| Liquid (y compris les boucles `for`, les instructions `if`, les mathématiques et autres) | Codage |
| Attributs par défaut et attributs standard de l'utilisateur | Attributs
| Attributs personnalisés ayant l'un de ces types de données : {::nomarkdown}<ul><li>Booléens</li><li>Chiffres</li><li>Chaînes de caractères</li><li>Tableaux</li><li>Date</li></ul>{:/} | Attributs
| Contenu connecté | Codage |
{: .reset-td-br-1 .reset-td-br-2 }

## Comment mes données sont-elles utilisées et envoyées à OpenAI ?

Afin de modifier ou de créer le contenu de vos messages, Braze enverra vos invites, le contenu de vos messages et/ou vos directives de marque (si vous décidez de les créer) soumis à l'assistant d'intelligence artificielle <sup>BrazeAITM</sup> à la plateforme API d'OpenAI. Toutes les requêtes envoyées à OpenAI depuis Braze sont anonymisées, ce qui signifie qu'OpenAI ne sera pas en mesure d'identifier l’origine de la requête, à moins que vous n'incluiez des informations identifiables dans le contenu que vous fournissez. Comme détaillé dans les [engagements de la plateforme API](https://openai.com/policies/api-data-usage-policies) d'OpenAI, les données envoyées à l'API d'OpenAI via Braze ne sont pas utilisées pour former ou améliorer leurs modèles et seront supprimées après 30 jours. Veuillez vous assurer que vous respectez les politiques d'OpenAI qui vous concernent, lesquelles peuvent inclure sa [politique d'utilisation](https://openai.com/policies/usage-policies) et sa [politique en matière de partage et de publication](https://openai.com/policies/sharing-publication-policy). Braze n'offre aucune garantie de quelque nature que ce soit en ce qui concerne tout contenu généré par l'intelligence artificielle.

[1]: {% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}
[2]: {% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}
[3]: {% image_buster /assets/img/ai_liquid/use_app_activity.png %}
[4]: {% image_buster /assets/img/ai_liquid/add_countdown.png %}
[5]: {% image_buster /assets/img/ai_liquid/inspire_me.png %}
[6]: {% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}
