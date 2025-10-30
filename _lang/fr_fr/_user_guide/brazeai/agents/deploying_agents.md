---
nav_title: "Déploiement d'agents"
article_title: "Déploiement d'agents personnalisés"
description: "Découvrez comment utiliser les agents personnalisés dans Braze après les avoir créés."
alias: /deploying-agents/
---

# Déploiement d'agents personnalisés

> Découvrez comment utiliser les agents personnalisés dans les étapes du canvas ou les champs du catalogue après les avoir créés. Pour une introduction, voir [Agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/). 

{% alert important %}
Les Braze Currents sont actuellement en version bêta. Pour obtenir de l'aide, contactez votre gestionnaire satisfaction client.
{% endalert %}  

## Agents in Canvas  

Vous pouvez utiliser les agents comme des étapes d'un parcours pour personnaliser les messages ou guider la prise de décision en temps réel. Pour connaître les étapes détaillées de la configuration, reportez-vous à la section [Étape de l'agent.]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/agent_step/)

### Cas d'utilisation

| Cas d'utilisation | Description |
| --- | --- |
| Evaluation et qualification des prospects | Utilisez une étape Agent pour évaluer les prospects entrants sur une échelle (par exemple, de 1 à 10). Dirigez les utilisateurs dont le score est supérieur à un seuil vers des chemins de maturation, tout en disqualifiant les prospects peu adaptés. |
| Personnalisation dynamique des messages | Demandez à un agent de générer des lignes d'objet, des recommandations de produits ou des messages en fonction des attributs de l'utilisateur ou de ses comportements récents. La réponse peut être insérée directement dans une étape du message. |
| Traitement du retour d'information des clients | Transmettez les commentaires des clients à un agent pour analyser les sentiments et générer des messages de suivi empathiques. Pour les utilisateurs de grande valeur, l'agent peut accélérer la réponse ou offrir des avantages. |
| Routage intelligent | Utilisez les sorties de l'agent (booléennes ou numériques) pour répartir les utilisateurs dans différents parcours Canvas. Par exemple, classez les utilisateurs comme étant "à risque" ou "en bonne santé" et adaptez la cadence d'envoi des messages en conséquence. |
| Interprétation des enquêtes ou des réponses | Laissez un agent analyser les réponses ouvertes à une enquête ou les champs de texte libre, en renvoyant des valeurs structurées (par exemple, en catégorisant l'intention ou le besoin) qui conduisent à des chemins en aval. |
| Raisonnement en plusieurs étapes | Configurez un agent pour qu'il combine les champs de contexte et prenne des décisions complexes, comme recommander la meilleure action suivante (e-mail, SMS ou contact humain) en fonction de plusieurs attributs de l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Agents dans les catalogues  

Vous pouvez appliquer un agent aux champs du catalogue afin qu'il génère ou calcule automatiquement des valeurs pour chaque ligne. L'agent s'exécutera également sur les nouvelles lignes qui seront ajoutées au catalogue à l'avenir. 

### Cas d'utilisation

| Cas d'utilisation | Description |
| --- | --- |
| Générer des descriptions de produits | Créez automatiquement un texte marketing court pour les nouvelles entrées du catalogue, par exemple en générant une description accrocheuse à partir des données structurées du produit telles que le nom, la catégorie et les fonctionnalités. |
| Enrichir les attributs du produit | Complétez les valeurs manquantes telles que la famille de couleurs, le style ou la saison en vous basant sur le nom et les détails d'un produit. Par exemple, si le nom d'un produit est "Laguna Polarized Sunglasses", l'agent peut attribuer le style "sport" et la famille de couleurs "bleu". |
| Calculer les champs dérivés | Utilisez les champs existants pour générer de nouvelles données, telles qu'un "score d'adéquation" basé sur les attributs ou une "étiquette de popularité" à partir des ventes et du nombre d'avis. |
| Catégoriser ou taguer des éléments | Attribuez des tags pour la logique de recommandation afin que les modèles de personnalisation puissent segmenter les produits plus efficacement. Par exemple, vous pouvez taguer les produits comme "outdoor", "festival ready" ou "premium". |
| Localiser le contenu | Traduisez le texte du catalogue dans une autre langue pour les campagnes mondiales, ou ajustez le ton et la longueur pour les canaux spécifiques à une région. Par exemple, traduisez "Classic Clubmaster Sunglasses" en espagnol par "Gafas de sol Classic Clubmaster", ou raccourcissez les descriptions pour les campagnes SMS. |
| Résumez les critiques ou le retour d'information | Résumez les sentiments ou les commentaires dans un nouveau champ, par exemple en attribuant des notes de sentiment comme Positif, Neutre ou Négatif, ou en créant un court résumé textuel comme "La plupart des clients mentionnent une bonne coupe, mais notent la lenteur de la livraison." |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étapes

\![Une étape de l'agent dans un champ du catalogue.]({% image_buster /assets/img/ai_agent/agent_in_catalog.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Pour ajouter un agent à votre champ de catalogue :

1. Dans votre catalogue, ajoutez un nouveau champ.  
2. Sélectionnez **Appliquer l'agent d'intelligence artificielle**.
3. Affectez un agent à ce champ.  
4. Sélectionnez les colonnes à transmettre en entrée. Si vous n'en sélectionnez aucun, l'agent aura accès à toutes les colonnes du catalogue.  
5. Décidez si l'agent doit recalculer les champs lorsque les lignes du catalogue sont mises à jour. Si vous ne sélectionnez pas cette option, l'agent ne s'exécutera qu'une fois par ligne.
6. Sélectionnez **Ajouter des champs** pour déployer l'agent et examiner les estimations de coûts. La fenêtre modale/boîte de dialogue de l **'estimation des coûts** indique le nombre de fois que l'agent s'exécutera sur ce catalogue, à peu près égal au nombre total de lignes. Pour continuer, sélectionnez **Confirmer**.

### Comment fonctionnent les agents de catalogue  

Après le lancement, l'agent s'exécutera et évaluera chaque ligne, en prenant les colonnes sélectionnées dans son contexte pour produire un résultat. Les agents s'exécutent sur toutes les nouvelles lignes ajoutées après le déploiement de l'agent. Si vous avez sélectionné **Recalculer lorsque les lignes du catalogue sont mises à jour**, toutes les valeurs de ce champ seront mises à jour si les champs source existants sont modifiés.  

{% alert note %}
Pendant la période bêta, les agents de catalogue sont limités au traitement des valeurs d'entrée jusqu'à 10 Ko par ligne, et ne mettront à jour que les 10 000 premières lignes d'un catalogue.
{% endalert %}

### Gestion des erreurs dans les catalogues  

- Les invocations de catalogues qui échouent ne sont pas réessayées.
- Si l'appel API au fournisseur du modèle de base renvoie une erreur, telle qu'une erreur de clé API non valide ou une erreur de limite de débit, la valeur du champ ne sera pas mise à jour.   
- Vous pouvez consulter les journaux de l'agent pour obtenir des détails sur les échecs.  
