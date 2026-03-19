---
nav_title: Optimiseur de contenu
article_title: "Étape de l'agent d'optimisation de contenu" 
alias: "/content_optimizer_step/"
page_order: 5
description: "L'étape Agent d'optimisation de contenu vous permet de configurer et de tester plusieurs versions de composants de contenu en une seule étape. Il vous permet de tester différentes variantes de contenu et optimise automatiquement les combinaisons les plus performantes au fil du temps."
page_type: reference

---

# Étape de l'agent d'optimisation de contenu

> L'étape Agent d'optimisation de contenu vous permet de configurer et de tester plusieurs versions de composants de contenu en une seule étape. Il vous permet de tester différentes variantes de contenu et optimise automatiquement les combinaisons les plus performantes au fil du temps. Pour une introduction, veuillez consulter [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
Content Optimizer est actuellement en version bêta. Pour obtenir de l'aide pour démarrer, veuillez contacter votre gestionnaire de la satisfaction client.
{% endalert %}

## Création d'une étape d'optimisation de contenu

Pour obtenir les meilleurs résultats, veuillez utiliser l'agent Content Optimizer dans les canevas où les utilisateurs progressent étape par étape au fil du temps. Si tous les utilisateurs passent à l'étape suivante simultanément, l'agent n'aura pas le temps de tirer des enseignements des premiers résultats. 

### Étape 1 : Ajouter une étape

Veuillez glisser-déposer le composant **Optimiseur de contenu** depuis la barre latérale ou sélectionner le bouton<i class="fas fa-plus-circle"></i> plus en bas d'une étape, puis sélectionner **Optimiseur de contenu**.

### Étape 2 : Veuillez rédiger votre message de base.

Le message de base constitue le point de départ de votre démarche. Les variantes pour chaque composant de contenu sont insérées de manière dynamique en fonction des combinaisons définies dans l'onglet **Paramètres de l'optimiseur de contenu**. 

{% alert note %}
Pendant la période bêta, l'e-mail est le seul canal pris en charge.
{% endalert %}

Dans l'onglet **Canaux de communication**, veuillez sélectionner **E-mail** et rédiger votre message électronique de base. Veuillez consulter notre section dédiée [aux e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email) pour obtenir de l'aide. 

L'agent Content Optimizer utilise les paramètres d'envoi (tels que le domaine d'e-mail et l'adresse de réponse) spécifiés dans cette variante pour envoyer tous les messages. Vous pouvez soit commencer avec un nouveau design, soit sélectionner un modèle existant pour ce message. À cette étape, veuillez déterminer les éléments du message que vous souhaitez optimiser. Vous les définirez à [l'étape 4](#step-4).

Les composants pris en charge pour l'optimisation comprennent :

- Objet
- En-tête du corps du message
- Contenu du corps du message
- CTA principal

### Étape 3 : Veuillez indiquer les paramètres de réception/distribution.

Dans l'onglet **Paramètres de réception/distribution**, vous pouvez indiquer si l'étape doit utiliser le timing intelligent ou les validations de réception/distribution. Pour plus de détails, veuillez vous référer à [la section Modifier les paramètres de réception/distribution]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) dans l'étape Message.

### Étape 4 : Ajouter des composants de contenu et des variantes {#step-4}

Les composants de contenu sont les éléments individuels de votre message que vous souhaitez tester, tels que différentes lignes d'objet, titres, corps de texte ou appels à l'action principaux. Ces composants vous permettent de générer plusieurs versions d'un message et de les optimiser automatiquement en fonction des performances au fil du temps.

Vous pouvez ajouter jusqu'à trois composants de contenu par étape et jusqu'à cinq variantes par composant, pour un total de 125 combinaisons de contenu uniques.

![Options permettant d'ajouter et de configurer des composants de contenu dans l'interface Content Optimizer. L'interface affiche les composants sélectionnables tels que l'objet, l'en-tête du corps, le contenu du corps et le CTA principal, chacun avec des champs permettant de saisir différentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Étape 4.1 : Configurer les composants de contenu

Pour configurer les composants :

1. Veuillez vous rendre dans l'onglet **Paramètres de l'optimiseur de contenu**.
2. Veuillez sélectionner les composants que vous souhaitez optimiser. Options prises en charge :
  - Objet
  - En-tête du corps du message
  - Contenu du corps du message
  - CTA principal
3. Pour chaque composant sélectionné, veuillez définir un ensemble de versions alternatives de ce contenu (variantes). Veuillez utiliser des variantes claires et distinctes qui diffèrent par le ton, la structure ou le contenu. Cela permet à Content Optimizer d'identifier plus efficacement les éléments les plus performants. Vous pouvez :
  - Veuillez rédiger vos propres variantes manuellement.
  - Utilisez les suggestions générées par l'intelligence artificielle pour explorer rapidement de nouvelles options.

![Interface des paramètres de l'optimiseur de contenu présentant les options permettant d'ajouter et de configurer des composants de contenu pour l'optimisation des e-mails. Chaque composant dispose de champs de saisie permettant d'entrer différentes variantes. Le texte visible comprend les noms des composants et les champs permettant de saisir du texte variant.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Étape 4.2 : Veuillez ajouter du liquid à votre message.

Après avoir défini au moins deux variantes pour chaque composant, veuillez copier l'étiquette Liquid associée à chacune d'elles et la coller à l'emplacement/localisation correspondant dans votre message de base.

- Par exemple, si vous optimisez la ligne d'objet, veuillez insérer {% raw %}`{% message_component "Subject" %}`{% endraw %}l'étiquette dans le champ Objet de l'éditeur d'e-mails.
- Vous pouvez également inclure des tags de composant dans un texte plus long afin de tester uniquement une partie du composant. Par exemple : {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Options permettant d'ajouter et de configurer des composants de contenu tels que l'objet, l'en-tête du corps, le contenu du corps et le CTA principal. Chaque composant comporte des champs permettant de saisir différentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si vous n'ajoutez pas d'étiquette Liquid pour un composant de contenu sélectionné, un avertissement s'affichera dans l'onglet **Paramètres de l'optimiseur** **de contenu** et une erreur apparaîtra dans l'onglet **Canaux de communication**. Le canvas ne peut être lancé tant que tous les composants sélectionnés n'ont pas été correctement ajoutés à votre message de base.

Au fur et à mesure que Canvas s'exécute, l'agent combine et associe différentes variantes entre les composants afin de générer diverses combinaisons de contenu. Au fil du temps, les combinaisons les plus performantes sont prioritaires pour la réception/distribution, ce qui vous aide à améliorer les performances sans intervention manuelle.

#### Référence liquide

| Composant | Extrait de liquid |
| --- | --- | 
| Objet | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| En-tête du corps du message | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Contenu du corps du message | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| CTA principal | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 5 : Veuillez sélectionner l'événement d'optimisation

L'événement d'optimisation détermine la manière dont l'agent Content Optimizer évalue les performances et répartit le trafic vers les combinaisons de contenu au fil du temps. 

Pour les e-mails, vous pouvez optimiser l'un des événements suivants. L'agent utilise les ouvertures et les clics enregistrés dans les 7 jours suivant l'envoi d'un message pour orienter la réception/distribution vers des combinaisons de contenus plus performantes.

| Événement | Description | Cas d’utilisation |
| --- | --- | --- |
| Ouvertures | Optimise les combinaisons qui incitent les destinataires à ouvrir l'e-mail. | Tester les lignes d'objet ou viser à accroître la visibilité |
| Clics | Optimise les combinaisons qui favorisent l'engagement avec les liens. N'inclut pas les clics effectués par des robots ni les clics de désabonnement reconnus par Braze. | Générer du trafic, de l'engagement ou des conversions à partir de liens |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

L'événement d'optimisation que vous avez sélectionné s'applique à tous les composants de contenu de cette étape. 

## Analyse

Pour examiner les performances, veuillez ouvrir le panneau d'analyse au niveau des étapes afin de consulter les indicateurs par variante de contenu et les performances globales des combinaisons. L'étape Optimiseur de contenu utilise les [mêmes analyses que l'étape Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics).

![Analyses analytiques de l'optimiseur de contenu pour trois boutons et pourcentage d'attribution des envois, qui affichent une tendance à la hausse.]({% image_buster /assets/img/content_optimizer/content_optimizer_analytics.png %})

## Résolution des problèmes

| Problème | Description | Correctif |
| --- | --- | --- |
| Étiquettes Liquid manquantes | Si vous ajoutez un composant de contenu (tel que l'objet ou le CTA) mais que vous n'insérez pas l'étiquette Liquid correspondante dans votre message de base, vous verrez s'afficher : <br>\- Un avertissement dans l'onglet **Paramètres de l'optimiseur de contenu** <br>\- Une erreur dans l'onglet **Canaux de communication** | Veuillez copier l'extrait de code Liquid affiché sous chaque composant dans l'onglet **Paramètres de l'optimiseur de contenu** et le coller à l'endroit approprié dans votre message. |
| Étiquettes Liquid orphelines | Si vous supprimez un composant de contenu mais laissez son étiquette Liquid dans le message de base, il est possible que le message ne s'affiche pas comme prévu lors de son envoi. | Veuillez supprimer toutes les étiquettes`message_component` inutilisées de votre message de base avant le lancement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

