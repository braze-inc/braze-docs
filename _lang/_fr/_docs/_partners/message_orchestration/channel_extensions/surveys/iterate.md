---
nav_title: Iterate
article_title: Iterate
alias: /fr/partners/iterate/
description: "Cet article décrit le partenariat entre Braze et Iterate, vous permettant d'enrichir les données des clients en utilisant des sondages pour ajouter des informations supplémentaires."
page_type: partenaire
search_tag: Partenaire
---

# Iterate

> [Iterate](https://iteratehq.com) facilite l'apprentissage de vos clients, en offrant des outils de recherche intelligents et conviviaux qui ressemblent et ressemblent à votre marque.

L'intégration de Braze et Iterate vous permet d'inclure des liens de sondage Iterate dans vos messages e-mail, push, ou dans l'application. Ces liens, une fois reçus, peuvent automatiquement enregistrer et attribuer des réponses d'itération comme attributs personnalisés de Braze, vous permettant de créer de nouveaux publics et segments puissants à utiliser dans vos campagnes.

## Pré-requis

| Exigences                       | Origine                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Iterate account                 | Un [compte Iterate](https://iteratehq.com) est requis pour profiter de ce partenariat.                                                                                                                       |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance][6].                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Cas d'utilisation

Avec Iterate, vous pouvez collecter presque tous les types de données allant de l'information personnelle, les données de performance, les préférences ou les préférences de l'utilisateur. Ce que vous demandez est entièrement à vous et à quel genre d'auditoires vous cherchez à construire.

## Intégration

### Étape 1 : Connectez Braze à l'itération

Connectez-vous à votre compte Iterate et ajoutez votre point de terminaison Braze REST et votre clé API REST à la page de configuration de votre entreprise.

### Étape 2 : Créer votre enquête

Créer une enquête de lien à envoyer. Une fois que les questions ont été écrites et que vous avez personnalisé la conception, sélectionnez **Envoyer une enquête -> Intégrations -> Braze**.

Vous verrez ensuite les options de configuration pour envoyer des réponses à Braze. Activer/désactiver l'intégration pour commencer à envoyer des réponses pour cette enquête au Brésil.

Copiez le lien de l'enquête fourni. Vous devrez inclure ce lien dans votre campagne de Braze. Notez que le Liquid inclus dans le lien {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} sera automatiquement remplacé pour chaque utilisateur lors de l'envoi.

### Étape 3 : Partagez votre enquête

Votre enquête peut être partagée de deux façons : en intégrant la première question dans votre message ou en incluant un lien direct vers l'enquête sur la plateforme Iterate.

!\[Iterate link options\]\[2\]

- **Intégrer le code**
  - Copiez le code snippet sous **Email embed code** dans la section d'intégration Braze de l'onglet **Envoyer l'enquête**. Insérez le code dans le code HTML de votre courriel Braze où vous souhaitez que le début de l'enquête apparaisse.
  - Si vous avez des difficultés à rendre les questions de l'enquête ou si elles ne sont pas correctement formatées, vous devrez aller dans l'onglet **Info d'envoi** dans le compositeur de message et décocher **CSS Inline**.
- **Inclure un lien**
  - Copiez le lien sous **Lien de l'enquête** dans la section d'intégration de Braze de l'onglet **Envoyer l'enquête**.

## Step 4: Target users

Comme les utilisateurs répondent, vous verrez les données peuplées sur leurs profils en temps réel. Ces données peuvent être utilisées pour segmenter les utilisateurs et envoyer des campagnes de suivi personnalisées. Par exemple, si vous avez envoyé une question "Vous aimez nos produits? , vous pouvez créer des segments d'utilisateurs qui ont l'attribut utilisateur personnalisé `Vous aimez nos produits ?` qui ont répondu "Oui" ou "Non", et ciblé ces utilisateurs.

## Personnaliser les noms des attributs utilisateur

Par défaut, l'attribut utilisateur créé pour une question est le même que l'invite de commande. Dans certains cas, vous voudrez peut-être personnaliser cela. Pour cela, cliquez sur le menu déroulant **Personnaliser les noms d'attributs d'utilisateur** dans l'étape **Créer votre enquête** ci-dessus et entrez tous les noms personnalisés que vous souhaitez.
[2]: {% image_buster /assets/img/iterate.png %}

[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
