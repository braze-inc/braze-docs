---
nav_title: Iterate
article_title: Iterate
alias: /fr/partners/iterate/
description: "Cet article décrit le partenariat entre Braze et Iterate vous permettant d'enrichir les données des clients en utilisant des sondages pour ajouter des informations supplémentaires."
page_type: partenaire
search_tag: Partenaire
---

# Iterate

> [Iterate](https://iteratehq.com) facilite l'apprentissage de vos clients, en offrant des outils de recherche intelligents et conviviaux qui ressemblent et ressemblent à votre marque.

Iterate s’intègre à Braze en enregistrant les réponses d’enquête sous forme d’attributs utilisateur personnalisés dans Braze vous permettant de créer de nouveaux publics et segments puissants.

## Exigences

Pour connecter Braze avec Iterate, vous aurez besoin des trois éléments suivants :

| Exigences                            | Origine | Libellé                                                                                                                                                                                                      |
| ------------------------------------ | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Clé API Braze                        | Brasero | Vous devrez créer une nouvelle clé d'API.<br><br>Ceci peut être créé dans la __Console Développeur -> Paramètres API -> Créer une nouvelle clé API__ avec __utilisateurs. permissions__ de rack. |
| [Point de terminaison REST Braze][6] | Brasero | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL de Braze pour votre instance.                                                                                                    |
| Itérer le compte                     | Iterate | Vous devrez avoir un compte Iterate. Visitez leur [site web](https://iteratehq.com/) pour commencer.                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Détails de l'intégration

Remplissez les vides et enrichissez les données de vos clients en envoyant un lien vers votre enquête Iterate via n'importe quel canal au Brésil : e-mail, email, push, ou message dans l'application. Le lien inclura l'identifiant Braze de l'utilisateur, qui sera utilisé pour identifier cet utilisateur. Quand ils remplissent l'enquête, les réponses à chaque question seront définies comme un attribut utilisateur personnalisé.

### Étape 1 : Connectez Braze à l'itération

Connectez-vous à votre compte Iterate et ajoutez votre clé **Braze REST Endpoint** et **API avec les utilisateurs `. droit d'accès`** à la page des paramètres de votre entreprise.

### Étape 2 : Créer votre enquête

Créez l'enquête de lien que vous allez envoyer. Une fois que les questions ont été écrites et que vous avez personnalisé le design, allez à *Envoyer l'enquête* et sélectionnez *Intégrations*, puis *Braze*. Vous verrez ensuite les options de configuration pour envoyer des réponses à Braze.

Activer/désactiver l'intégration pour commencer à envoyer des réponses pour cette enquête au Brésil. Copiez le lien de l'enquête répertorié, c'est ce que vous allez inclure dans votre campagne. Notez le {% raw %}`? ser_braze_id={{${braze_id}}}`{% endraw %} que Braze remplacera automatiquement par le bon identifiant Braze de l'utilisateur que vous envoyez dans la campagne.

### Étape 3 : Partagez votre enquête

Ensuite, lancez simplement votre campagne en incluant ce lien et lorsque les utilisateurs répondront vous verrez les données peuplées sur leurs profils en temps réel.

## Personnaliser les noms des attributs utilisateur

Par défaut, l'attribut utilisateur créé pour une question est le même que l'invite de commande. Par exemple, une question avec l'invite : "Dans l'ensemble, à quel point êtes-vous satisfait de l'itérate? sera ajouté en tant qu'attribut utilisateur `dans l'ensemble, à quel point êtes-vous satisfait d'itérate?` en Brésil. Dans certains cas, vous voudrez peut-être personnaliser cela, pour faire cela, cliquez sur le menu déroulant *Personnaliser les noms d'attributs d'utilisateur* dans l'étape **Créer votre enquête** ci-dessus et entrez tous les noms personnalisés que vous souhaitez.

## Cas d'utilisation

Avec Iterate, vous pouvez collecter presque tous les types de données. Éloignement des informations personnelles (nom, âge, e-mail), données de performance (NPS, satisfaction du client, évaluation des étoiles), préférences (dispositif préféré, fréquence préférée de communication), ou personnalité (livre favori, chien ou chat). Ce que vous demandez est entièrement à vous et à quel genre d'auditoires vous cherchez à construire.

[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
