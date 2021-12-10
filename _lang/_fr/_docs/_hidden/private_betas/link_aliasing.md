---
nav_title: Alimentation du lien
permalink: /fr/link_aliasing/
description: "Cet article décrit comment fonctionne Link Aliasing et certaines des nuances avec la fonctionnalité."
hidden: vrai
---

# Alimentation du lien

> Utiliser l'alias de lien pour créer des noms identifiables générés par les utilisateurs pour identifier les liens envoyés dans les messages électroniques en provenance de Braze. L'alias de lien vous donne la possibilité de re-cibler les utilisateurs qui ont cliqué sur des liens spécifiques, vous permettant de créer des déclencheurs basés sur l'action lorsque les utilisateurs cliquent sur un lien alias spécifique.

## Aperçu

L'alias de lien fonctionne en décorant un paramètre de requête généré par le Brésil sur les liens dans le canal de messagerie. Pour chaque lien connu qui est présent dans le corps de l'e-mail, Braze ajoutera {% raw %}`couvercle={{placeholder}}` à la fin{% endraw %}, où {% raw %}`{{placeholder}}`{% endraw %} est une valeur alphanumérique unique générée par Liquide.

Ces paramètres de requête sont également ajoutés aux blocs de contenu, permettant le suivi des liens à des fins de segmentation.

!\[link_aliasing_composer\]\[2\]

Pour créer un alias de lien, cliquez sur l'onglet __Gestion des liens__ dans une campagne Braze ou l'assistant de Canvas pour décorer tous les liens connus dans le corps de l'e-mail. Les utilisateurs peuvent également définir un alias qui sera utilisé pour référencer ce lien lorsqu'ils traitent de rapport ou de segmentation. Les alias doivent être nommés de manière unique par variante de campagne de courriel ou pas de Canvan. Vous pouvez également ajouter des modèles de liens à partir de la section de gestion des liens.

### Activation de la fonctionnalité

L'activation de l'alias de lien est simple et ne nécessite aucun temps d'interruption. Cette activation n'est pas compatible avec le passé, signifie que tous les messages ou blocs de contenu précédemment créés ne seront pas reconnus par cette fonctionnalité (à moins qu'ils ne soient modifiés et relancés à nouveau).

## Conditions préalables et limitations

__Messages modifiés par l'Analyseur HTML__<br> Vos messages seront modifiés par un analyseur HTML ; cela peut conduire à ce que l'analyseur corrige potentiellement du HTML. (C'est déjà le cas si vous utilisez des fonctionnalités telles que le champ de saisie pré-en-tête, les instructions Liquid, ou modèles de lien)<br><br> __État partiellement migré__<br> Vous pouvez vous trouver dans un état partiellement migré où certains messages et blocs de contenu auront un aliasing. La modification de messages ou de blocs de contenu avant d'avoir la fonctionnalité activée entraînera l'édition de liens Braze.<br><br> __Link Aliasing Support__<br> L'alias de lien n'est supporté que dans les attributs `href` des balises d'ancrage HTML où il est sûr d'ajouter un paramètre de requête. Il est préférable d'inclure un point d'interrogation ? à la fin de votre lien afin que Braze puisse ajouter facilement la valeur du `couvercle` .<br><br> __Mettre à jour les limites du bloc de contenu__<br> Ajouter des valeurs `couvercle` à un bloc de contenu existant ne prendra en charge que la propagation des documents de liens vers les 50 premiers "includeurs". Un includer est une variante de message où le bloc de contenu est utilisé, ou un autre bloc de contenu est imbriqué.

## Activer la publication

{% tabs %}
{% tab Message Variants %}
__Variantes de message__

Les nouvelles variantes de messages électroniques (campagne ou Canvas) auront leurs liens modifiés où Braze ajoutera un couvercle {% raw %}`={{placeholder}}`{% endraw %} à chaque lien, le cas échéant.

Toute variante de message électronique qui a été créée avant Braze activant cette fonctionnalité ne verra ses liens modifiés que lorsque le HTML de ces variantes sera modifié.

{% endtab %}
{% tab HTML Content Blocks%}
__Blocs de contenu HTML__

Les nouveaux blocs de contenu auront leurs liens modifiés où Braze ajoutera un couvercle {% raw %}`={{placeholder}}`{% endraw %} à chaque lien, le cas échéant. La valeur placeholder est résolue quand elle est insérée dans une variante de message email.

Tous les blocs de contenu existants qui ont été créés avant que Braze n'active cette fonctionnalité auront leurs liens modifiés uniquement lorsque le HTML de ce bloc de contenu sera modifié, et le bloc de contenu est relancé.

Quand un bloc de contenu qui n'est pas décoré avec la valeur `couvercle` est inséré dans...<br> &#45; un nouveau message, les liens de ce bloc de contenu ne sont pas suivis avec un alias.<br> &#45; un ancien message, et ce message n'a pas été édité ; les liens ne sont pas suivis avec aucun alias.

Lorsqu'un nouveau bloc de contenu est inséré dans une variante de message 'vieux', les liens de cette variante de message seront reconnus par cette fonctionnalité (depuis que la variante a été modifiée). Les liens du bloc de contenu sont également reconnus.

Les blocs de contenu "Ancien" (pas marqués) ne peuvent pas imiter les blocs de contenu "nouveau".

{% alert tip%}
Pour les blocs de contenu, il est recommandé de créer des copies des blocs de contenu existants à utiliser dans de nouveaux messages. Cela peut être fait en utilisant la fonctionnalité [dupliquage en vrac]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/#duplicate-multiple-templates). Cela empêche certains cas où vous pourriez référencer un bloc de contenu qui n'a pas été activé pour l'alias de lien dans un nouveau message.
{% endalert %}

{% endtab %}
{% endtabs %}

## Modèles de lien
Pour les nouvelles variantes de message, tout modèle de lien existant peut être utilisé dans l'onglet __Gestion des liens__.

Pour toute variation de message d'e-mail configurée avant que cette fonctionnalité soit activée, les modèles de liens existants seront toujours présents. Cependant, si la variation du message est modifiée, les modèles de liens devront être réappliqués.


## Segmentation de lien

La redistribution des alias est maintenant disponible en tant que filtre de segmentation. Les deux nouveaux filtres vous permettent de créer des filtres de segmentation en fonction de vos clients en cliquant sur un alias suivi spécifique, à partir d'une campagne de courriel ou d'une étape de Canvan. Le filtre n'affiche que les campagnes ou les Canvases qui ont suivi les alias présents.

### Suivi d'un lien

Lors de la rédaction de votre message e-mail, une nouvelle colonne sera présente dans l'onglet __Gestion des liens__. Ici, vous pouvez indiquer à Braze quel alias vous souhaitez être "suivi" à des fins de segmentation. Seuls les alias que vous avez indiqué pour être suivi seront présents dans les filtres de segmentation. Veuillez noter que les alias suivis sont uniquement à des fins de segmentation et n'auront aucune incidence sur le suivi de votre lien à des fins de déclaration.

#### Annuler le suivi d'un lien
Untracking a link will not deallocate existing segments with the filter to the untracked alias. Les anciennes données resteront sur les profils de l'utilisateur jusqu'à ce qu'elles soient expulsées par de nouvelles données. Les filtres de segmentation suivants continueront d'exister mais de nouveaux segments ne peuvent pas être créés avec ce filtre.

### Filtres de segment

!\[link_aliasing_segmentation_filters\]\[5\]

#### Alias cliqué dans la campagne
Retarget les utilisateurs basés sur l'alias spécifique qui a été cliqué dans une campagne. Seules les campagnes qui ont des alias qui ont été suivis seront reflétées ici.

#### Alias cliqués à l'étape de Canvas
Retarget les utilisateurs en fonction de l'alias spécifique qui a été cliqué dans une étape de Canvas . Une option de filtre délimité de tubes affiche l'étape Canvas et Canvas suivie de l'alias à l'intérieur du pas de Canvan. Seules les étapes de Canvas avec des alias suivis seront affichées ici.

{% alert tip%}
Les alias sont uniques par variante de message de campagne ou pas de Canvan. Par conséquent, vous devez d'abord sélectionner l'étape de la campagne, Canvas, ou Canavas avant de sélectionner vos alias.
{% endalert %}

### Filtres basés sur l'action

!\[link_aliasing_action_based_filters\]\[6\]

En plus de créer des filtres de segments, vous pouvez également créer des messages par action ciblant tout lien (suivi ou non suivi) à travers une campagne de courriel ou une étape de Canvan.

## Suivi et Rapports

### Suivi des liens

À des fins de segmentation, seuls 100 liens peuvent être suivis par groupe d'applications par défaut. Les liens dans les messages archivés seront automatiquement désuivis. Si les messages archivés sont désarchivés, les liens devront être suivis à nouveau.

### Cliquez sur le lien Reporting
Les rapports de liens seront maintenant indexés par l'alias `` plutôt que par des domaines de premier niveau et/ou des URL complètes.

!\[link_aliasing_click_table\]\[1\]

### Changements d'événement en cours
{% api %}
Evénements des clics par e-mail

{% apitags %}
E-mail, clics
{% endapitags %}

Cet événement se produit lorsqu'un utilisateur clique sur un email. Plusieurs événements peuvent être générés pour la même campagne si un utilisateur clique plusieurs fois ou clique sur différents liens dans l'email.

```json
// Email Click: users.messages.email. lick
{
  "id": (string) unique id de cet événement,
  "user_id": (string) Braze identifiant utilisateur de l'utilisateur,
  "external_user_id": (string) ID externe de l'utilisateur,
  "temps": (int) 10 chiffres heure UTC de l'événement en secondes depuis l'époque,
  "fuseau horaire": (chaîne) IANA fuseau horaire de l'utilisateur au moment de l'événement,
  "campaign_id": (string) id de la campagne si à partir d'une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) id de la variation de message si une campagne,
  "canvas_id": (chaîne) id de la toile si une toile
  "canvas_name": (string) nom des Canvas,
  "canvas_variation_id": (string) id de la variation de Canvas dans laquelle l'utilisateur est à partir d'un Canvas,
  "canvas_variation_name": (chaîne) nom de la variation de Canvas dans laquelle l'utilisateur est si à partir d'un Canvas,
  "canvas_step_id": (string) id de l'étape pour ce message si à partir d'un Canvas,
  "canvas_step_name": (string) nom de l'étape pour ce message si à partir d'un Canvas,
  "send_id": (string) id du message si spécifié pour la campagne (Voir Send Identifier under API Identifier Types),
  "dispatch_id": (string) id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plate-forme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur.
  "email_address": (chaîne) adresse email pour cet événement,
  "url": (chaîne) l'url qui a été cliqué (Email Click events seulement),
  "user_agent": (string) description du système de l'utilisateur et du navigateur pour l'événement (Email Click, Ouvrir, et les événements MarkAsSpam seulement),
  "ip_pool": (string) pool IP utilisé pour l'envoi de messages,
  "link_id": (chaîne) valeur unique générée par Braze pour l'URL,
  "link_alias": (chaîne) nom d'alias défini lors de l'envoi du message
}
```

{% alert update %}
Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Mise à jour notée en août 2019._
{% endalert %}

{% endapi %}

## Choses à noter

__Utiliser des blocs de contenu HTML dans d'autres canaux__<br> Si le bloc de contenu HTML est utilisé dans d'autres canaux (par exemple, dans le message de l'application), une valeur `lid=` sera toujours ajoutée à chaque lien. La valeur ne sera pas remplie, donc vos liens ressembleront à ceci : `http://www.braze.com?lid="`

__Heatmap__<br> La fonctionnalité de la carte de chaleur n'est pas prise en charge avec cette version du produit d'alias de lien. Les prochaines itérations peuvent soutenir la présentation de la carte de chaleur.

__API-Triggered__<br> Cette fonctionnalité ne prend en charge aucune variante de message où le client transmet des données relatives aux liens.

__Extracting Data__<br> The following endpoints are available to extract the `alias` set in each message variant in a campaign or an email Canvas step:

- [Point de terminaison du lien de campagne][3]
- [Point de terminaison de l'alias de lien de canvas][4]
[1]: {% image_buster /assets/img/link_aliasing_click_table.png %} [2]: {% image_buster /assets/img/link_aliasing_composer. ng %} [5]: {% image_buster /assets/img/link_aliasing_segmentation_filters.png %} [6]: {% image_buster /assets/img/link_aliasing_action_based_filters.png %}

[3]: {{site.baseurl}}/get_campaign_link_alias/
[4]: {{site.baseurl}}/get_canvas_link_alias/
