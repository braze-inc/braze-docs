---
nav_title: Modèles de lien
article_title: Modèles de lien
page_order: 4
description: "Les modèles de liens permettent aux utilisateurs d'ajouter des paramètres ou de préfixer des URL à tous les liens dans un courriel. Cet article couvre la façon de créer différents types de modèles de liens."
tool:
  - Modèles
channel:
  - Email
---

# Modèles de lien

> Cet article traite de la façon de créer des modèles de liens à utiliser pour la messagerie électronique.

Les modèles de liens vous permettent d'ajouter des paramètres ou de préfixer des URL à tous les liens dans un courriel. Ceci est le plus souvent utilisé pour les cas d'utilisation suivants :

1. Ajout des paramètres de requête Google Analytics à tous les liens dans un e-mail donné
2. Prévisualisation d'une URL vers tous les liens dans un e-mail donné

{% alert note %}
Lors de l'utilisation de modèles de lien et de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), le code Liquid ne doit être ajouté qu'à l'intérieur de la balise body pour assurer un rendu cohérent.
{% endalert %}

## Création d'un modèle de lien

!\[Create Link Template\]\[11\]{: style="float:right;max-width:30%;"}

Pour créer un modèle de lien, accédez à la page **Modèles & Média** et sélectionnez l'onglet **Modèles de liens**. Vous pouvez créer un nombre illimité de modèles de liens pour répondre à vos différents besoins. Cliquez sur **Créer un modèle de lien** pour commencer.

{% alert note %}
Les modèles de liens sont une fonctionnalité optionnelle. Si l'onglet **Modèles de lien** est manquant dans votre page **Modèles & Média** , contactez votre gestionnaire de service client ou votre gestionnaire de compte pour activer la fonction de flipper pour les modèles de liens.
{% endalert %}

Il y a deux types de modèles de liens que vous pouvez créer :

- [Modèle de lien qui insère avant une URL](#prepend-link-template)
- [Modèle de lien qui insère après une URL](#append-link-template)

### Précédent : Créer un modèle de lien qui s'insère avant une URL {#prepend-link-template}

Si vous voulez ajouter une chaîne ou une URL avant les liens dans votre message e-mail, créer un nouveau modèle de lien et définir la **Position du modèle** à **Avant l'URL**.  Cela vous permettra de saisir une chaîne de caractères qui sera toujours préfixé à votre URL.

Une section d'aperçu est fournie pour vous donner un exemple du processus d'insertion.

![Pre Append]({% image_buster /assets/img_archive/link_template_preappend.png %})

### Ajouter : Créer un modèle de lien qui insère après une URL {#append-link-template}

Si vous voulez ajouter des paramètres de requête après une URL dans votre message e-mail, créer un nouveau modèle de lien et définir la **Position du modèle** à **Après l'URL**.  Cela vous permettra de saisir les paramètres de la requête (`value=something`) à la fin de chaque URL.

Vous pouvez avoir plusieurs paramètres ajoutés à la fin d'une URL.

![Ajouter une publication]({% image_buster /assets/img_archive/link_template_postappend.png %})

## Utiliser vos modèles dans les campagnes de messagerie

Une fois vos modèles configurés, vous pouvez sélectionner le modèle que vous souhaitez utiliser dans votre e-mail à partir de l'éditeur de courriel.

À partir de l'éditeur de courriel, cliquez sur **Bibliothèque de contenu** et sélectionnez l'onglet **Lier le modèle**. Vous verrez tous les liens présents dans votre e-mail et pourrez y ajouter le modèle.

!\[Composeur de message\]\[1\]

## Gestion des modèles de liens

Vous pouvez aussi [dupliquer]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) modèles de liens ! En savoir plus sur la création et la gestion de modèles et de contenus créatifs dans [Modèles & Médias]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert important %}
L'archivage des modèles n'est actuellement pas disponible pour les [Modèles de lien]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates).
{% endalert %}

## Foire aux questions

Pour obtenir des réponses aux questions les plus fréquemment posées sur les modèles de liens, consultez notre page [FAQ][10] sur les modèles d'e-mails et de liens.
[1]:{% image_buster /assets/img_archive/link_template_messagecomposer2.png %} [2]:{% image_buster /assets/img_archive/link_template_postappend.png %} [3]:{% image_buster /assets/img_archive/link_template_preappend.png %} [11]: {% image_buster /assets/img_archive/create_link_template.png %}

[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
