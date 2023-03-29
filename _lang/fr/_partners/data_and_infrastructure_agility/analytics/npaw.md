---
nav_title: NPAW
article_title: NPAW
page_order: 0
alias: /partners/npaw/
description: "Cet article de référence présente le partenariat entre Braze et NPAW, une plateforme d’analyses de données intelligente qui fournit des Insights exploitables aux leaders des médias en ligne."
page_type: partner
search_tag: Partenaire
hidden: true

---

# NPAW

> [NPAW](https://nicepeopleatwork.com/), également connu sous le nom de _Nice People at Work_, est une plateforme d’analyses de données intelligente qui fournit des Insights exploitables aux leaders des médias en ligne. Avec la suite d’outils YOUBORA de NPAW, les clients de Braze peuvent désormais tirer parti d’une IA robuste et prédictive pour mieux comprendre le comportement des clients et favoriser l’engagement sur toutes les plateformes.

# Conditions préalables

| Condition   |Origine| Description |
| --------------|------|-------------|
| Clé API YOUBORA |[Paramètres YOUBORA](https://youbora.nicepeopleatwork.com/users/login)|Une clé API générée lors de l’inscription d’un utilisateur et qui peut être trouvée dans la section **Paramètres** |
| ID |[Paramètres Braze](https://dashboard.braze.com/sign_in) | YOUBORA vous permet de relier le logiciel à Braze via un ***ID Braze***, un ***ID utilisateur externe***, ou un ***ID utilisateur*** |
| Endpoint |[Paramètres Braze](https://dashboard.braze.com/sign_in)| Un endpoint d’URL entièrement personnalisable et configurable sur votre **tableau de bord de Braze** |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

# Intégration de l’analytique

## Accès à la page Intégrations

Après vous être connecté à votre compte de la suite d’outils YOUBORA, accédez à la page Integrations (Intégrations) en sélectionnant l’option **Integration (Intégrations)** dans le menu déroulant de votre compte.

![Menu déroulant NPAW]({% image_buster /assets/img/npaw_dropdown.png %})

## Configurer votre intégration

Sur la page Integration (Intégrations), faites défiler vers le bas jusqu’à 
voir l’option d’intégration de **Braze**. Après avoir cliqué sur ce bouton, la liste s’agrandira et présentera plusieurs paramètres à remplir :

![Intégration NPAW]({% image_buster /assets/img/npaw_integration.png %})

Renseignez les informations que vous avez recueillies dans la section des conditions préalables, où :
* La valeur **Connector Name (Nom du connecteur)** est une chaîne de caractères **alphanumériques** qui sera utilisée pour se référer à cette intégration à l’avenir. Vous pouvez renseigner cette valeur comme vous le souhaitez, dans la mesure où elle contient **uniquement** des lettres et des chiffres.
* L’**ID utilisateur** est l’ID précédemment choisi pour relier votre logiciel YOUBORA à votre compte Braze. Par exemple, si vous choisissez d’effectuer la liaison via votre **ID Braze**, sélectionnez **ID Braze** dans le menu déroulant pour attribuer la valeur au champ approprié.
* La **clé API** est la clé API de votre suite d’outils YOUBORA. Cette clé se trouve dans la section **API**, sous **Settings (Paramètres)**.
* L’**endpoint** est l’endpoint d’URL personnalisable que vous avez configuré dans votre **Tableau de bord de Braze**.

Une fois tous les champs remplis, cliquez simplement sur le bouton **Connect (Connexion)** pour établir une connexion et enregistrer les modifications apportées.

## Comment utiliser votre intégration NPAW

Une fois que vous avez fini de configurer votre intégration avec Braze, accédez au produit **Users (Utilisateurs)** et sélectionnez le **Sample Manager (Gestionnaire d’échantillons)** dans le **Sections Manager (Gestionnaire de sections)**.

Après avoir créé un échantillon dans le **Sample Manager (Gestionnaire d’échantillons)**, vous pourrez maintenant cliquer sur l’icône des points de suspension sur la droite pour envoyer tous les utilisateurs de votre échantillon à Braze.

![Gestionnaire d’échantillons NPAW]({% image_buster /assets/img/npaw_sample_manager.png %})

Désormais, lorsque vous envoyez vos utilisateurs à Braze, vous pouvez effectuer certaines actions et centrer vos campagnes sur des segments utilisateur pour réengager des utilisateurs inactifs, contacter vos utilisateurs les plus fidèles ou effectuer toute action sur n’importe quel segment d’utilisateurs !
