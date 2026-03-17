---
nav_title: Déployer des agents
article_title: Déployer des agents personnalisés
description: "Découvrez comment utiliser les agents personnalisés dans Braze après les avoir créés."
alias: /deploying-agents/
page_order: 2
---

# Déployer des agents personnalisés

> Découvrez comment utiliser les agents personnalisés dans les étapes du canvas ou les champs du catalogue après les avoir créés. Pour une introduction, veuillez consulter [la section Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/).

## Agents dans Canvas  

Vous pouvez utiliser des agents comme étapes d'un parcours pour réaliser la personnalisation des messages ou guider la prise de décision en temps réel. Pour obtenir des instructions détaillées sur la configuration, veuillez vous référer à [l'étape Agent]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/).

### Cas d’utilisation

| Cas d’utilisation | Description |
| --- | --- |
| Évaluation et qualification des prospects | Veuillez utiliser une étape Agent pour évaluer les prospects entrants sur une échelle (par exemple, de 1 à 10). Dirigez les utilisateurs dont le score est supérieur à un seuil donné vers des parcours de fidélisation, tout en écartant les prospects peu adaptés. |
| Personnalisation dynamique des messages | Demandez à un agent de générer des lignes d'objet, des recommandations produits ou des messages en fonction des attributs des utilisateurs ou de leurs comportements récents. La réponse peut être insérée directement dans une étape Message. |
| Gestion des commentaires des clients | Transmettez les commentaires des clients à un agent afin qu'il analyse leur sentiment et rédige des messages de suivi empathiques. Pour les utilisateurs de grande valeur, l'agent peut escalader la réponse ou inclure des avantages. |
| Routage intelligent | Veuillez utiliser les résultats de l'agent (booléens ou numériques) pour répartir les utilisateurs dans différents chemins canvas. Par exemple, veuillez classer les utilisateurs comme « à risque » ou « en bonne santé » et Adjust la fréquence de l’envoi de messages en conséquence. |
| Interprétation des enquêtes ou des réponses | Permettez à un agent d'analyser les réponses ouvertes d'un sondage ou les champs de texte libre, en renvoyant des valeurs structurées (par exemple, en classant les intentions ou les besoins) qui déterminent les chemins en aval. |
| Raisonnement en plusieurs étapes | Configurez un agent pour combiner des champs contextuels et prendre des décisions complexes, telles que recommander la meilleure action à entreprendre (e-mail, SMS ou intervention humaine) en fonction de plusieurs attributs utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Agents dans les catalogues  

Vous pouvez appliquer un agent aux champs du catalogue afin qu'il génère ou calcule automatiquement des valeurs pour chaque ligne. L'agent s'exécutera également sur les nouvelles lignes qui seront ajoutées au catalogue à l'avenir. 

### Cas d’utilisation

| Cas d’utilisation | Description |
| --- | --- |
| Générer des descriptions de produits | Créez automatiquement des textes marketing courts pour les nouvelles entrées du catalogue, par exemple en générant une description accrocheuse à partir de données produit structurées telles que le nom, la catégorie et les fonctionnalités. |
| Enrichir les attributs des produits | Veuillez compléter les informations manquantes telles que la famille de couleurs, le style ou la saison en vous basant sur le nom et les détails du produit. Par exemple, si le nom d'un produit est « Lunettes de soleil polarisées Laguna », l'agent pourrait attribuer le style « sport » et la famille de couleurs « bleu ». |
| Calculer les champs dérivés | Veuillez utiliser les champs existants pour générer de nouvelles données, telles qu'un « score d'adéquation » basé sur les attributs ou une « étiquette de popularité » à partir des ventes et du nombre d'avis. |
| Catégoriser ou apposer des étiquettes sur les éléments | Attribuez des étiquettes à la logique de recommandation afin que les modèles de personnalisation puissent réaliser la segmentation des produits de manière plus efficace. Par exemple, veuillez apposer des étiquettes sur les produits comme « pour l'extérieur », « pour les festivals » ou « haut de gamme ». |
| Localiser le contenu | Traduisez le texte du catalogue dans une autre langue pour les campagnes mondiales, ou ajustez le ton et la longueur pour les canaux spécifiques à chaque région. Par exemple, traduisez « Lunettes de soleil Classic Clubmaster » en espagnol par « Gafas de sol Classic Clubmaster » ou raccourcissez les descriptions pour les campagnes SMS. |
| Veuillez résumer les avis ou les commentaires. | Résumez les sentiments ou les commentaires dans un nouveau champ, par exemple en attribuant des notes telles que « Positif », « Neutre » ou « Négatif », ou en rédigeant un bref résumé tel que « La plupart des clients mentionnent une excellente qualité, mais soulignent la lenteur de la livraison ». |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étapes

![Une étape Agent dans un champ de catalogue.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Pour ajouter un agent à votre champ de catalogue :

1. Dans votre catalogue, veuillez ajouter un nouveau champ.  
2. Veuillez sélectionner **« Appliquer l'agent d'intelligence artificielle** ».
3. Veuillez désigner un agent pour ce domaine.  
4. Veuillez sélectionner les colonnes qui doivent être transmises en tant qu'entrée. Si aucune n'est sélectionnée, l'agent aura accès à toutes les colonnes du catalogue.  
5. Veuillez déterminer si l'agent doit recalculer les champs lorsque les lignes du catalogue sont mises à jour. Si vous ne sélectionnez pas cette option, l'agent ne s'exécutera qu'une seule fois par ligne.
6. Veuillez sélectionner **Ajouter des champs** pour déployer l'agent et examiner les estimations de coûts. La fenêtre modale **Estimation des** **coûts** indique le nombre d'exécutions de l'agent sur ce catalogue, ce qui correspond approximativement au nombre total de lignes. Pour continuer, veuillez sélectionner **Confirmer**.

### Fonctionnement des agents de catalogue  

Après son lancement, l'agent exécute et évalue chaque ligne, en intégrant les colonnes sélectionnées dans son contexte afin de produire un résultat. Les agents s'exécutent sur toutes les nouvelles lignes ajoutées après le déploiement de l'agent. Si vous avez sélectionné **Recalculer lors de la mise à jour des lignes du catalogue**, toutes les valeurs de ce champ sont mises à jour si les champs source existants changent.

Vous pouvez actualiser et modifier les champs de votre catalogue qui utilisent des agents. Pour supprimer un agent d'une colonne, désélectionnez **Appliquer l'agent d'intelligence artificielle**. Cela rétablit la colonne en tant que colonne non agentique, et les champs conservent les dernières valeurs que l'agent a appliquées lors de sa dernière exécution sur le catalogue.

Les références circulaires dans les catalogues ne sont pas prises en charge, ce qui signifie que le scénario suivant ne peut pas se produire :

- La colonne agentique 1 utilise la colonne agentique 2 comme entrée.
- La colonne 2 utilise la colonne 1 comme entrée.

![L'option permettant de sélectionner « Appliquer l'agent d'intelligence artificielle » pour un champ du catalogue.]({% image_buster /assets/img/ai_agent/edit_agent_column.png %}){: style="max-width:80%;"}

{% alert note %}
Les agents de catalogue sont limités au traitement de valeurs d'entrée pouvant atteindre 25 Ko par ligne.
{% endalert %}

#### Définir les champs de réponse

Si votre agent utilise [des champs]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/?tab=fields#advanced-schemas) comme format de sortie, vous pouvez sélectionner le champ correspondant dans l'agent pour **le champ Réponse** à utiliser dans le champ du catalogue. 

Supposons que vous disposiez d'un agent qui ajoute des descriptions de produits à un catalogue avec les champs suivants pour structurer le format de sortie :

| Nom du champ | Valeur |
| --- | --- |
| **Description** | Texte |
| **confidence_score_out_of_ten** | Nombre |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Vous pouvez ajouter un champ nommé**product_description**à un catalogue et sélectionner **description** comme **champ** **de réponse** pour remplir la colonne avec les descriptions de l'agent.

![Un champ"product_description"auquel l'agent « Descriptor » a été appliqué. La sortie « description » est sélectionnée comme champ de réponse.]({% image_buster /assets/img/ai_agent/response_field.png %}){: style="max-width:80%;"}

Vous pouvez également remplacer manuellement la cellule générée par l'agent en sélectionnant **Modifier l'élément** et en modifiant la description générée par l'agent avec vos modifications. Pour revenir à la description générée par l'agent, veuillez sélectionner le symbole pour actualiser la cellule.

### Gestion des erreurs dans les catalogues  

- Les invocations de catalogue qui échouent ne sont pas réessayées.
- Si l'appel API vers le fournisseur de modèle de base renvoie une erreur, telle qu'une erreur de clé API non valide ou une erreur de limite de débit, la valeur du champ n'est pas mise à jour.
- Vous pouvez consulter les journaux de l'agent pour obtenir des détails sur les exécutions ayant échoué.

## Veuillez surveiller votre agent

Dans la section **Utilisation** de votre agent, vous pouvez consulter et accéder aux endroits où l'agent est activement utilisé dans les catalogues et les canevas.

![Section Utilisation des agents qui affiche deux agents actifs et un agent inactif pour Canvases.]({% image_buster /assets/img/ai_agent/agent_usage.png %})

Dans la section **Journaux** de votre agent, vous pouvez surveiller les appels réels qui ont lieu dans vos canevas et catalogues. Vous pouvez filtrer les résultats en fonction d'informations telles que la période, le résultat (réussite ou échec) ou l'emplacement/localisation de l'appel. Vous pouvez également sélectionner **Exporter CSV** pour exporter uniquement les journaux affichés sur la page actuelle.

{% alert tip %}
Vous pouvez également surveiller les erreurs liées à la limite quotidienne d'appels dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/).
{% endalert %}

![Journaux pour un score de sentiment d'intelligence artificielle pour un agent.]({% image_buster /assets/img/ai_agent/agent_logs.png %})

Veuillez sélectionner **Afficher** pour un appel d'agent spécifique afin de consulter les données saisies, les données générées et l'ID utilisateur.

![Le panneau de détails d'une tâche aléatoire liée au sport pour un agent, qui affiche l'invite de saisie, la réponse générée et l'ID utilisateur associé.]({% image_buster /assets/img/ai_agent/agent_logs_view.png %})

### Utiliser Currents

Vous pouvez également utiliser ces événements Currents pour accéder aux schémas d'enregistrement Kafka :

- Événements exécutés par l'agent
- Événements d'invocation d'outils

Veuillez consulter le [glossaire des événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) pour plus de détails.

## Articles connexes  

- [Référence pour les agents]({{site.baseurl}}/user_guide/brazeai/agents/reference/)