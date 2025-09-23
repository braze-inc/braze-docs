---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "Cet article de référence décrit le partenariat entre Braze et NPAW, une plateforme d'analyse de données intelligente qui fournit des informations exploitables aux principaux professionnels des médias en ligne."
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> [La société NPAW](https://nicepeopleatwork.com/), également connue sous le nom de _Nice People at Work_, est une plateforme d'analyse de données intelligente qui fournit des informations exploitables aux principaux professionnels des médias en ligne. Grâce à la suite d'outils YOUBORA de NPAW, les clients de Braze peuvent désormais tirer parti d'une intelligence artificielle prédictive et robuste pour mieux comprendre le comportement des clients et stimuler l'engagement sur toutes les plateformes.

# Prérequis

| Exigence   |Origine| Descriptif |
| --------------|------|-------------|
| Clé API YOUBORA |[Paramètres YOUBORA](https://youbora.nicepeopleatwork.com/users/login)|Une clé API générée lors de l'inscription de l'utilisateur et qui se trouve dans l’onglet **Paramètres** |
| ID |[Paramètres Braze](https://dashboard.braze.com/sign_in) | YOUBORA vous permet de lier le logiciel à Braze via un ***ID Braze***, un ***ID d’utilisateur externe*** ou un ***ID d’utilisateur*** |
| Endpoint |[Paramètres Braze](https://dashboard.braze.com/sign_in)| Un endpoint URL entièrement personnalisable et configurable via votre tableau de bord de Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

# intégration des outils d'analyse

## Accès à la page des intégrations

Après vous être connecté à votre compte YOUBORA tool suite, accédez à la page Intégrations en sélectionnant l'option **Intégrations** dans le menu déroulant du compte.

![NPAW dropdown]({% image_buster /assets/img/npaw_dropdown.png %})

## Configuration de votre intégration

Une fois que vous avez accédé à la page d'intégration, faites défiler la page vers le bas jusqu'à
voir l'option d'**intégration de Braze**. Après avoir cliqué dessus, il s'agrandira et proposera un certain nombre de paramètres requis à remplir :

![Intégration NPAW ] ({% image_buster /assets/img/npaw_integration.png %})

Remplissez les champs appropriés avec les informations recueillies dans la section des prérequis, où :
* Le **nom du connecteur** est une chaîne de caractères **alphanumérique** qui sera utilisée pour faire référence à cette intégration à l'avenir. Cette valeur peut être réglée comme vous le souhaitez tant qu'elle **ne** contient que des lettres et des chiffres.
* **L'ID utilisateur** est l'identifiant précédemment choisi pour associer votre logiciel YOUBORA à votre compte Braze. Par exemple, si vous choisissez d'effectuer le lien via votre **Braze ID**, sélectionnez Braze **ID** dans la liste déroulante pour attribuer la valeur au champ approprié.
* La **clé API** est la clé API de votre suite d'outils YOUBORA qui se trouve précédemment dans la section **API** sous **Paramètres.**
* **Endpoint** est l’endpoint URL personnalisable précédemment configuré dans votre tableau de bord de Braze.

Une fois tous les champs remplis, il suffit de cliquer sur le bouton **Connecter** pour établir une connexion et enregistrer les modifications apportées.

## Utilisation de votre intégration NPAW

Une fois que vous avez terminé de configurer votre intégration avec Braze, accédez au produit **Utilisateurs** et sélectionnez le **gestionnaire d'échantillons** dans le **gestionnaire de sections**.

Après avoir créé un échantillon dans le **gestionnaire d'échantillons**, vous pouvez maintenant cliquer sur l'icône à trois points sur le côté droit pour envoyer tous les utilisateurs de votre échantillon vers Braze.

![Gestionnaire d'échantillons NPAW ] ({% image_buster /assets/img/npaw_sample_manager.png %})

Désormais, une fois que vous avez envoyé vos utilisateurs vers Braze, vous pouvez passer à l'action et concentrer les campagnes sur les segments d'utilisateurs pour réengager les utilisateurs inactifs, contacter vos utilisateurs les plus fidèles ou toute action sur n'importe quel segment d'utilisateurs !
