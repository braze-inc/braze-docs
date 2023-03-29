---
nav_title: Octolis
article_title: Octolis
description: "Cet article de référence décrit le partenariat entre Braze et Octolis, une plateforme d’activation des données qui vous permet d’intégrer vos données dans Braze."
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis][0] est une plateforme d’activation des données puissante (ou CDP headless). Placé au-dessus d’une base de données qui vous appartient, Octolis fournit un moyen facile d’unifier, préparer, établir un score et synchroniser les données dans vos outils d’entreprise.

L’intégration Braze-Octolis fait office de middleware entre vos sources de données brutes et Braze, ce qui vous permet d’extraire et d’unifier les données provenant de diverses sources en ligne et hors-ligne :
1. Unifier et combiner des données provenant de sources telles qu’une boutique en ligne (E-shop), votre CRM, un système de point de vente (POS) etc.
2. Normaliser et établir un score
3. Synchronisation en temps réel des champs calculés et des événements avec Braze

![][7]

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Octolis | Un compte Octolis est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé API REST Braze avec autorisations [**users.track (suivi des utilisateurs)**][1]. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][2]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
| Clé de l’application Braze | Votre clé d’identification de l’application. Vous pouvez y trouver ce que vous pouvez trouver dans le **Tableau de bord de Braze > Manage Settings (Gérer les paramètres) > API Key (Clé API)**. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Avant de commencer l’intégration, veuillez lire les sections suivantes sur les connexions, les audiences, les sources et les synchronisations.

Pour plus d’informations, consultez la section [Pour démarrer][4] d’Octolis.

### Étape 1 : Connectez Octolis à vos sources de données

Pour envoyer des données à Braze, vous devez avoir créé au moins une [audience][5]. Une audience combine plusieurs sources de données, les applique dans les étapes de préparation et ajoute les champs calculés.

Ces audiences doivent être construites à partir de plusieurs sources de données. Une source peut être :
- Un objet Salesforce (contacts, comptes, etc.)
- Un objet Zendesk (tickets)
- Un fichier dans un SFTP (fichier CSV avec des contacts, fichier JSON avec des événements…)
- Table/view d’une base de données.
- Un de vos systèmes nous envoie des enregistrements via des webhooks ou appels API.

### Étape 2 : Ajouter Braze en tant que destination

Ensuite, pour définir Braze en tant que nouvelle destination, sélectionnez **+ Add more (+ Ajouter)** en haut de votre destination actuelle sur l’écran principal et sélectionnez **Braze** dans la liste des outils d’entreprise disponibles.

![][9]

Une fois sélectionné, indiquez les éléments suivants :

- Votre clé API REST Braze : Cela peut être créé dans le **Tableau de bord de Braze > Developer Console (Console du développeur) > REST API Key (Clé API REST) > Create New Api Key (Créer une nouvelle clé API)**
- Période : Octolis appliquera la limitation du débit dans la période donnée.
- Volume de requêtes : Nombre de requêtes que vous pouvez faire durant la période.
- Attributs personnalisés : Spécifiez ici les nouveaux champs que vous allez envoyer à Braze, leur format (string, integer, float) et cochez la case **Required for syncs (Requis pour les synchronisations)** si vous souhaitez que ces champs soient obligatoires pour une synchronisation.

![][10]

Une fois configuré, Braze apparaitra en tant que nouvelle destination sur la page d’accueil.

### Étape 3 : Créer une nouvelle synchronisation

Dans le menu, cliquez sur **Syncs** et sélectionnez **Add sync (Ajouter une synchronisation)** dans le coin supérieur droit. Sélectionnez votre audience souhaitée à partir de l’audience que vous avez créée précédemment.
Ensuite, sélectionnez **Braze** en tant que destination et indiquez à quelle entité vous allez envoyer les données.

![][11]

### Étape 4 : Définir les paramètres de sortie

Par défaut, Braze crée tous les attributs que vous enverriez, mais vous devez préciser la liste des champs qui doivent être synchronisés.

![][12]{: style="max-width:75%;"}

Voici les définitions spécifiques des champs de paramétrage.

| Champ | Description |
| --- | --- |
| Où voulez-vous synchroniser l’audience ? | L’entité Braze où vous allez créer ou mettre à jour des enregistrements. |
| Quel champ est utilisé pour identifier un enregistrement ? | Le champ utilisera Octolis pour identifier un enregistrement s’il existe déjà dans Braze. |
| À quelle fréquence souhaitez-vous envoyer chaque enregistrement ? | Par défaut, la synchronisation sera incrémentale pour toutes les intégrations (API, base de données, FTP). Cela signifie que seules les nouvelles valeurs (depuis la dernière mise à jour) seront mises à jour. Le cas échéant, vous pouvez aussi envoyer des tables entières à intervalles réguliers. Octolis enverra la table entière au moment de l’initiation. |
| Quels champs doivent être synchronisés ? | Mappage des champs de Octolis vers Braze. La liste des champs disponibles apparait dans le menu déroulant. Pour envoyer un champ calculé à Braze, assurez-vous de créer d’abord la colonne correspondante dans votre entité Braze. |
| Quand souhaitez-vous synchroniser l’audience ? | Comment les données seront-elles envoyées à Braze  : manuellement, en temps réel ou de façon programmée.  |
| Synchroniser quand l’enregistrement est… | Créer : Pour les abonnements (opt-ins), il est important que la table Braze reste la table principale (master table). Il ne faut pas qu’Octolis déclenche une synchronisation pendant qu’un champ est mis à jour.<br><br>Mise à jour : D’un autre côté, pour un champ Prénom par exemple, vous voulez être capable de mettre à jour le champ dans votre table Braze chaque fois qu’un client vous donne une nouvelle entrée. |
{: .reset-td-br-1 .reset-td-br-2}

## Déduplication avec clés multiples

La déduplication est un vrai défi lorsqu’il s’agit de réconcilier les données provenant de sources multiples, surtout lorsque certaines sont en ligne et d’autres hors-ligne. Avec le module sans code avancé d’Octolis, vous pouvez utiliser des clés multiples pour la [déduplication][3]. Ce module est disponible pour chaque table principale, ce qui signifie que vous pouvez adapter la logique à chaque entité.

[0]: http://octolis.com
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work
[4]: https://help.octolis.com/
[5]: https://help.octolis.com/audiences/create-a-no-code-audience
[6]: {{site.baseurl}}/api/api_limits/
[7]: {% image_buster /assets/img/Octolis/Braze_scheme.png %}
[8]: {% image_buster /assets/img/Octolis/Braze_screen1.png %}
[9]: {% image_buster /assets/img/Octolis/Braze_screen2.png %}
[10]: {% image_buster /assets/img/Octolis/Braze_screen3.png %}
[11]: {% image_buster /assets/img/Octolis/Braze_screen4.png %}
[12]: {% image_buster /assets/img/Octolis/Braze_screen5.png %}
