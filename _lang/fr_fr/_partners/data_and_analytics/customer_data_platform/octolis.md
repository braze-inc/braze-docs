---
nav_title: Octolis
article_title: Octolis
description: "Cet article de référence décrit le partenariat entre Braze et Octolis, une plateforme d'activation de données, qui vous permet d'intégrer vos données dans Braze."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis](http://octolis.com) est une puissante plateforme d'activation de données (ou plateforme de données clients headless). En se basant sur l’une de vos bases de données, Octolis permet d'unifier, de préparer, de noter et de synchroniser les données dans vos outils professionnels.

_Cette intégration est maintenue par Octolis._

## À propos de l'intégration

L'intégration de Braze et Octolis agit comme un intergiciel entre vos sources de données brutes et Braze, vous permettant de récupérer et d'unifier des données provenant de différentes sources, en ligne et hors ligne :
1. Unifiez et combinez les données provenant de sources telles que des boutiques en ligne, le CRM, le système POS, etc.
2. Normaliser et attribuer un score
3. Synchronisation en temps réel des champs calculés et des événements avec Braze

![]({% image_buster /assets/img/Octolis/Braze_scheme.png %})

## Conditions préalables

| Condition | Descriptif |
| ----------- | ----------- |
| Compte Octolis | Un compte Octolis est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec [**users.track**]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)des autorisations. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Clé de l'application Braze | La clé de l'identifiant de votre application. Elle se trouve dans le **tableau de bord Braze > Gérer les paramètres > Clé API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Avant de commencer l'intégration, consultez les sections suivantes sur les connexions, les sources, les audiences et les synchronisations.

Pour plus d'informations, consultez la section [Mise en route](https://help.octolis.com/) d'Octolis.

### Étape 1 : Connectez Octolis à vos sources de données

Pour envoyer des données à Braze, vous devez vous assurer d'avoir créé au moins une [audience](https://help.octolis.com/audiences/create-a-no-code-audience). Une audience combine plusieurs sources de données, les applique aux étapes de préparation et ajoute des champs calculés.

Ces audiences doivent être établies à partir de plusieurs sources de données. Une source peut être l'une des suivantes :
- Un objet Salesforce (contacts, comptes, etc.)
- Un objet Zendesk (tickets)
- Un fichier à l'intérieur d'un SFTP (fichier CSV contenant certains contacts, fichier JSON contenant des événements...)
- Table/vue d'une base de données.
- L'un de vos systèmes nous envoie des enregistrements via des webhooks ou des appels d'API.

### Étape 2 : Ajouter Braze comme destination

Ensuite, pour définir Braze comme nouvelle destination, sélectionnez **\+ Ajouter plus** en haut de votre destination actuelle sur l'écran principal et sélectionnez **Braze** parmi les outils commerciaux disponibles.

![]({% image_buster /assets/img/Octolis/Braze_screen2.png %})

Une fois sélectionné, fournissez les informations suivantes :

- Votre clé API Braze : Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**.
- Fenêtre horaire : Octolis appliquera la limite tarifaire pendant la période donnée.
- Volume de la requête : Nombre de requêtes que vous pouvez faire au cours de cette période.
- Attributs personnalisés : Spécifiez ici les nouveaux champs que vous allez envoyer à Braze, leur format (chaîne de caractères, entier, float), et cochez la case **Obligatoire pour les synchronisations** si vous souhaitez que l'un d'entre eux soit obligatoire pour une synchronisation.

![]({% image_buster /assets/img/Octolis/Braze_screen3.png %})

Une fois configuré, Braze apparaîtra comme une nouvelle destination sur l'écran d'accueil.

### Étape 3 : Créer une nouvelle synchronisation

Dans le menu, cliquez sur **Synchronisation** et sélectionnez **Ajouter une synchronisation** en haut à droite. Sélectionnez l'audience que vous souhaitez sélectionner dans l'audience que vous avez créée précédemment.
Ensuite, sélectionnez **Braze** comme destination et entité à laquelle vous allez envoyer des données.

![]({% image_buster /assets/img/Octolis/Braze_screen4.png %})

### Étape 4 : Définir les paramètres de sortie

Par défaut, Braze crée tous les attributs que vous allez envoyer, mais vous devez documenter la liste des champs à synchroniser.

![]({% image_buster /assets/img/Octolis/Braze_screen5.png %}){: style="max-width:75%;"}

Voici une définition spécifique des champs de paramétrage.

| Champ d'application | Descriptif |
| --- | --- |
| Où souhaitez-vous synchroniser l'audience ? | L'entité de Braze dans laquelle vous allez créer ou mettre à jour des enregistrements. |
| Quel champ est utilisé pour identifier un enregistrement ? | Le champ utilisera Octolis pour identifier un enregistrement s'il existe déjà dans Braze. |
| À quelle fréquence souhaitez-vous envoyer chaque enregistrement ? | Par défaut, la synchronisation sera incrémentielle pour toutes les intégrations (API, base de données, FTP). Cela signifie que seules les nouvelles valeurs enregistrées depuis la dernière mise à jour seront mises à jour. Si nécessaire, vous pouvez également envoyer des tableaux entiers à intervalles réguliers. À l'initiation, Octolis enverra le tableau complet. |
| Quels champs doivent être synchronisés ? | mappage des champs d'Octolis à Braze. La liste de tous les champs disponibles apparaît dans le menu déroulant. Pour envoyer un champ calculé à Braze, vous devez d'abord vous assurer que vous avez créé la colonne correspondante dans votre entité Braze. |
| Quand souhaitez-vous synchroniser l'audience ? | Comment les données seront envoyées à Braze : manuellement, en temps réel ou par programmation.  |
| Synchroniser lorsque l'enregistrement est... | Créez : Pour les abonnements, il est important que la table Braze reste la table principale. Vous ne voulez pas qu'Octolis déclenche une synchronisation lorsque le champ est mis à jour.<br><br>Mise à jour : En revanche, pour un champ de prénom, par exemple, vous souhaitez pouvoir mettre à jour le champ de votre table Braze chaque fois qu'un client vous donne une nouvelle entrée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Déduplication à clés multiples

La déduplication constitue un défi majeur lorsqu'il s'agit de réconcilier des données provenant de sources multiples, notamment en ligne et hors ligne. Grâce au module avancé sans code d'Octolis, vous pouvez utiliser plusieurs clés pour la [déduplication](https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work). Ce module est disponible pour chaque table principale, ce qui signifie que vous pouvez adapter la logique à chaque entité.


