---
nav_title: Optimiseur de contenu
article_title: Content Optimizer agent step 
alias: "/content_optimizer_step/"
page_order: 5
description: "L'étape de l'agent Content Optimizer vous permet de configurer et de tester plusieurs versions de composants de contenu en une seule étape. Il vous aide à expérimenter des variations de contenu et optimise automatiquement les combinaisons les plus performantes au fil du temps."
page_type: reference

---

# Content Optimizer agent step

> L'étape de l'agent Content Optimizer vous permet de configurer et de tester plusieurs versions de composants de contenu en une seule étape. Il vous aide à expérimenter des variations de contenu et optimise automatiquement les combinaisons les plus performantes au fil du temps. Pour une introduction, voir [Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer/).

{% alert important %}
Content Optimizer est actuellement en version bêta. Pour obtenir de l'aide, contactez votre gestionnaire satisfaction client.
{% endalert %}

## Création d'une étape de l'Optimiseur de contenu

Pour obtenir les meilleurs résultats, utilisez l'agent Content Optimizer dans les canevas où les utilisateurs entrent progressivement dans l'étape. Si tous les utilisateurs entrent dans l'étape en même temps, l'agent n'aura pas le temps de tirer des enseignements des premiers résultats. 

### Étape 1 : Ajouter une étape

Glissez-déposez le composant **Content Optimizer** depuis la barre latérale ou cliquez sur le bouton <i class="fas fa-plus-circle"></i> plus au bas d'une étape et sélectionnez **Content Optimizer**.

### Étape 2 : Créez votre message de base

Le message de base est le point de départ de votre démarche. Des variantes pour chaque composant de contenu sont insérées dynamiquement en fonction des combinaisons définies dans l'onglet **Paramètres de l'optimiseur de contenu**. 

{% alert note %}
Pendant la période bêta, l'e-mail est le seul canal pris en charge.
{% endalert %}

Dans l'onglet **Canaux de communication**, sélectionnez **Email** et créez votre message e-mail de base. Consultez notre section dédiée à l'[e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email) pour obtenir de l'aide. 

L'agent Content Optimizer utilise les paramètres d'envoi (tels que le domaine e-mail et l'adresse de réponse) spécifiés dans cette variante pour envoyer tous les messages. Vous pouvez soit commencer par une nouvelle conception, soit sélectionner un modèle existant pour ce message. À cette étape, réfléchissez aux éléments du message que vous souhaitez optimiser. Vous les définirez à l'[étape 4.](#step-4)

Les composants pris en charge pour l'optimisation sont les suivants :

- Objet
- En-tête du corps du message
- Contenu du corps du message
- CTA principal

### Étape 3 : Spécifier les paramètres de réception/distribution

Dans l'onglet **Paramètres de réception/distribution**, vous pouvez indiquer si l'étape doit utiliser le timing intelligent ou les validations de réception/distribution. Pour plus de détails, reportez-vous à la section [Modifier les paramètres de réception/distribution]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#step-2-edit-delivery-settings) à l'étape Message.

### Étape 4 : Ajouter des composants de contenu et des variantes {#step-4}

Les composants du contenu sont les éléments individuels de votre message que vous souhaitez tester, tels que les différentes lignes d'objet, les titres, le corps du texte ou les principaux appels à l'action. Ces composants vous permettent de générer plusieurs versions d'un message et de l'optimiser automatiquement en fonction des performances au fil du temps.

Vous pouvez ajouter jusqu'à trois composants de contenu par étape et jusqu'à cinq variantes par composant, pour un total de 125 combinaisons de contenu uniques.

![Options permettant d'ajouter et de configurer des composants de contenu dans l'interface de l'Optimiseur de contenu. L'interface affiche des composants sélectionnables tels que le sujet, l'en-tête du corps, le contenu du corps et le CTA principal, chacun avec des champs permettant de saisir différentes variantes.]({% image_buster /assets/img/content_optimizer/add_content_components.png %})

#### Étape 4.1 : Configurer les composants de contenu

Pour configurer les composants :

1. Accédez à l'onglet **Paramètres de l'Optimiseur de contenu**.
2. Choisissez les composants que vous souhaitez optimiser. Options prises en charge :
  - Objet
  - En-tête du corps du message
  - Contenu du corps du message
  - CTA principal
3. Pour chaque composant sélectionné, définissez un ensemble de versions alternatives de ce contenu (variantes). Utilisez des variantes claires et distinctes qui diffèrent par le ton, la structure ou le contenu. Cela permet à Content Optimizer d'identifier plus efficacement les personnes les plus performantes. Vous pouvez le faire :
  - Rédigez manuellement vos propres variantes.
  - Utilisez les suggestions générées par l'intelligence artificielle pour explorer rapidement de nouvelles options.

![Interface des paramètres de l'optimiseur de contenu affichant des options permettant d'ajouter et de configurer des composants de contenu pour l'optimisation des e-mails. Chaque composant comporte des champs de saisie permettant d'introduire différentes variantes. Le texte visible comprend les noms des composants et les zones de saisie des textes variants.]({% image_buster /assets/img/content_optimizer/content_optimizer_settings.png %})

#### Étape 4.2 : Ajoutez du liquide à votre message

Après avoir défini au moins deux variantes pour chaque composant, copiez l'étiquette Liquid associée à chacun d'eux et collez-la à l'emplacement correspondant dans votre message de base.

- Par exemple, si vous optimisez la ligne d'objet, collez l'étiquette {% raw %}`{% message_component "Subject" %}`{% endraw %} dans le champ d'objet du compositeur d'e-mail.
- Vous pouvez également inclure des tags de composants dans un texte plus long afin de ne tester qu'une partie du composant. Par exemple : {% raw %}`Hey there, {% message_component "Subject" %}`{% endraw %}.

![Options permettant d'ajouter et de configurer des éléments de contenu tels que l'objet, l'en-tête du corps, le contenu du corps et le CTA principal. Chaque composant comporte des champs permettant de saisir différentes variantes.]({% image_buster /assets/img/content_optimizer/optimization_liquid_in_use.png %})

Si vous n'ajoutez pas d'étiquette Liquid pour un composant de contenu sélectionné, vous verrez un avertissement dans l'onglet **Paramètres de l'optimiseur de contenu** et une erreur dans l'onglet **Canaux de communication.**  Le canvas ne peut pas être lancé tant que tous les composants sélectionnés n'ont pas été correctement ajoutés à votre message de base.

Au cours de l'exécution du Canvas, l'agent mélange et associe des variantes entre les composants pour générer différentes combinaisons de contenu. Au fil du temps, les combinaisons les plus performantes sont prioritaires pour la réception/distribution, ce qui vous aide à améliorer les performances sans intervention manuelle.

#### Référence du liquide

| Composant | Extrait de code liquide |
| --- | --- | 
| Objet | {% raw %}`{% message_component "Subject" %}`{% endraw %} |
| En-tête du corps du message | {% raw %}`{% message_component "Body Header" %}`{% endraw %} |
| Contenu du corps du message | {% raw %}`{% message_component "Body Content" %}`{% endraw %} | 
| CTA principal | {% raw %}`{% message_component "Primary CTA" %}`{% endraw %} | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 5 : Sélectionnez l'événement d'optimisation

L'événement d'optimisation détermine la manière dont l'agent Content Optimizer évalue les performances et attribue le trafic aux combinaisons de contenu au fil du temps. 

Pour l'e-mail, vous pouvez optimiser pour l'un des événements suivants. L'agent utilise les ouvertures et les clics enregistrés dans les 7 jours suivant l'envoi d'un message pour réorienter la réception/distribution vers des combinaisons de contenu plus performantes.

| Événement | Description | Cas d’utilisation |
| --- | --- | --- |
| Ouvertures | Optimise les combinaisons qui incitent les destinataires à ouvrir l'e-mail. | Tester les lignes d'objet ou viser une plus grande visibilité |
| Clics | Optimise les combinaisons qui favorisent l'engagement avec les liens. Ne comprend pas les clics de robots ou les clics de désinscription reconnus par Braze. | Susciter du trafic, de l'engagement ou de la conversion à partir de liens. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

L'événement d'optimisation que vous avez sélectionné s'applique à tous les composants du contenu dans cette étape. 

## Analyse

Pour évaluer les performances, ouvrez le panneau d'analyse/analytique au niveau de l'étape pour consulter les indicateurs par variante de contenu et les performances globales de la combinaison. L'étape Content Optimizer utilise les mêmes analyses/analytiques que l'étape Message. Pour plus de détails, voir [Analyse/analytique]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/#analytics) à l'étape Message.  

## Résolution des problèmes

| Problème | Description | Correctif |
| --- | --- | --- |
| Étiquettes Liquid manquantes | Si vous ajoutez un composant de contenu (tel que Subject ou CTA) mais que vous n'insérez pas l'étiquette Liquid correspondante dans votre message de base, vous verrez : <br>\- Un avertissement sur l'onglet **Paramètres de l'Optimiseur de contenu**  <br>\- Une erreur dans l'onglet des **canaux de communication de l'envoi de messages**  | Copiez l'extrait de code liquid affiché sous chaque composant dans l'onglet **Paramètres de l'Optimiseur de contenu** et collez-le dans la partie appropriée de votre message. |
| Étiquettes Liquid orphelines | Si vous supprimez un composant de contenu mais que vous laissez son étiquette Liquid dans le message de base, le message risque de ne pas s'afficher comme prévu lors de l'envoi. | Retirez toutes les étiquettes `message_component` inutilisées de votre message de base avant de le lancer. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

