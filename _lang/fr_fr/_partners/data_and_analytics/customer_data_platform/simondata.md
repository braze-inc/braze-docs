---
nav_title: SimonAI
article_title: SimonAI
description: "Utilisez l'intégration Braze et SimonAI pour créer et synchroniser des audiences sophistiquées vers Braze pour l'orchestration, en temps réel et sans code."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Intelligence artificielle

> La plateforme [Simon AI][1] Agentic Marketing Platform aide les équipes marketing à réaliser une véritable personnalisation one-to-one. Elle associe une CDP composable à des agents d'intelligence artificielle qui opèrent directement dans le Cloud de données d'intelligence artificielle de Snowflake pour jouer le rôle d'équipe de données et d'exécution d'un marketeur.

Utilisez l'intégration Braze et Simon Intelligence Artificielle pour créer et synchroniser des audiences avancées sur Braze pour une orchestration en temps réel et sans code. Grâce à cette intégration, vous pouvez exploiter la résolution d'identité de Simon AI, l'unification des données clients et la segmentation basée sur l'intelligence artificielle pour alimenter en aval des campagnes Braze plus personnalisées et plus percutantes.

## Conditions préalables

Pour commencer, vous devez authentifier votre compte Braze au sein de votre compte Simon Intelligence artificielle.

| Condition         | Description                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Intelligence artificielle          | Vous devez disposer d'un compte Simon Intelligence Artificielle existant pour tirer parti de l'intégration de Braze depuis Simon Intelligence Artificielle.                                                                    |
| Clé d'API REST Braze  | Une clé API REST Braze avec`users.track`, `campaigns.trigger.schedule.create` et des autorisations `campaigns.trigger.send`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| URL du tableau de bord Braze | [L'URL de votre endpoint REST.][3] Votre endpoint dépendra de l'URL de Braze pour votre instance.                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

- Déclenchez un canvas Braze ou un e-mail  
- Transmettre et gérer les propriétés du segment
- Synchroniser les traits et les propriétés des contacts

{% alert note %}  
Lors de l'utilisation de l'intégration Simon et Braze, Simon envoie uniquement des deltas à chaque synchronisation à Braze, évitant ainsi les coûts liés à des données non pertinentes. Consultez [Synchroniser les caractéristiques et les propriétés des contacts](#sync-traits-and-contact-properties) pour en savoir plus.
{% endalert %}

## Intégration

### Authentifiez votre compte Braze dans l'intelligence artificielle de Simon

Pour utiliser l'intégration Braze, authentifiez d'abord votre compte Braze dans Simon :

1. Dans la barre de navigation de gauche, cliquez sur **Intégrations**, puis accédez à Braze.
2. Entrez votre [clé API Braze REST et l'URL][2] de votre [tableau de bord][3].
3. Cliquez sur **Enregistrer les modifications**.

Une connexion réussie affiche **Connecté** dans la fenêtre.

![Écran d'intégration dans l'intelligence artificielle][8]{: style="max-width:70%"}

### Ajouter des actions Braze aux flux ou aux voyages dans Simon Intelligence Artificielle

Après avoir authentifié votre compte Braze dans Simon Intelligence artificielle, vous pouvez ajouter des actions Braze aux [flux][4] et aux [parcours][5].

Trois actions sont disponibles :

- **Synchroniser l’attribut du segment Simon** : Synchronisez les détails de votre segment avec un attribut personnalisé nouveau ou existant dans Braze.
- **Déclencher un canvas Braze :** Déclenchez un canvas Braze qui exploite les données de votre segment Simon.
- **Envoyer une campagne Braze** : Lancez l’intégralité d’une campagne Braze depuis Simon.

![Liste déroulante présentant les actions de Braze disponibles dans l'intelligence artificielle][9].{: style="max-width:60%"}

Certaines actions ne sont disponibles que pour des types de flux spécifiques ou des voyages uniquement. Pour en savoir plus, consultez [docs.simondata.com][6].

### Synchroniser les traits et les propriétés des contacts

Pour minimiser la consommation de données, vous pouvez choisir des caractéristiques spécifiques à synchroniser par défaut, plutôt que de mettre à jour tous les champs pour tous les clients d'un segment.

{% alert note %}
Pour commencer à synchroniser les caractéristiques, soumettez une requête au [centre d’assistance Simon](https://docs.simondata.com/docs/support-center). Votre gestionnaire de compte vous indiquera quand vous pourrez suivre les étapes suivantes.
{% endalert %}

Une fois que Contact Traits a été activé par votre gestionnaire de compte :

1. Dans Simon, développez le **Centre d'administration** dans la barre de navigation de gauche et sélectionnez **Synchroniser les caractéristiques des contacts**.
2. Choisissez **Braze**. Les propriétés des contacts sont affichées ici, imbriquées par jeu de données.
3. Sélectionnez les champs que vous souhaitez synchroniser lorsque vous utilisez l'intégration Simon and Braze :
   1. **Le nombre ou les traits** indiquent le nombre de traits parmi lesquels il est possible de choisir dans cet ensemble de données. Vous pouvez tout sélectionner ou développer la ligne pour sélectionner des champs individuels.
   2. Modifiez le **nom en aval** si vous souhaitez que les noms des champs apparaissent différemment lorsqu'ils arrivent dans Braze.
   3. Si c'est la première fois que vous intégrez Braze depuis Simon, cliquez sur **Remplir tous les contacts**. Le remblayage envoie tous les points de données à Braze la première fois que vous utilisez une action dans un flux ou un parcours afin de vous assurer que toutes vos données sont parfaitement synchronisées. Ensuite, lors des synchronisations suivantes, seules les caractéristiques que vous choisissez dans cet écran sont envoyées à Braze. Cela permet de s'assurer que seules les données dont vous avez besoin vous sont facturées.

![Sélection des traits de synchronisation dans l'intelligence artificielle de Simon][10].

[1]: https://www.simondata.com




[1]: https://www.simondata.com
[2]: {{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center
[8] : {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}  
[9] : {% image_buster /assets/img/simon_data/BrazeActions.png %}
[10] : {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}

