---
nav_title: Aliasage de lien
article_title: Aliasage de lien
alias: /link_aliasing/
page_order: 4
description: "Le présent article décrit la manière dont l’aliasage de lien fonctionnent et à quoi ressembleront vos liens."
channel:
  - E-mail

---

# Aliasage de lien
 
> Utilisez l’aliasage de lien pour créer des noms reconnaissables et générés par l’utilisateur pour identifier les liens envoyés dans les e-mails de Braze. L’aliasage de lien vous permet de recibler les utilisateurs ayant cliqué sur des liens spécifiques, ce qui vous permet de créer des déclencheurs par événement lorsque les utilisateurs cliquent sur un lien d’alias particulier. 

L'aliasage de lien crée des noms générés par l’utilisateur qui sont disponibles pour le reciblage de segmentation, le déclenchement basé sur les actions et l’analyse des liens. L'aliasage de lien fonctionnent en décorant un paramètre de requête généré par Braze sur des liens dans le canal d’e-mail.

## Création d’un alias de lien

Pour créer un alias de lien, cliquez sur l’onglet **Link Management (Gestion des liens)** dans une campagne Braze ou un assistant Canvas pour décorer tous les liens connus du corps de l’e-mail. Vous pouvez également définir un alias qui sera utilisé pour référencer ce lien lors de la gestion de rapports ou de segmentation. 

Braze génère automatiquement des alias de lien par défaut uniques pour chacun de vos liens. Vous pouvez personnaliser ces alias, mais gardez à l’esprit que les alias doivent avoir un nom unique par variante de campagne par e-mail ou composant Canvas. L'aliasage de lien est uniquement pris en charge dans les attributs `href` dans les balises HTML où il est sûr d’ajouter un paramètre de requête. Il est préférable d’inclure un point d’interrogation (?) à la fin de votre lien afin que Braze puisse facilement ajouter la valeur `lid`. Sans l’ajout de la valeur `lid`, Braze ne reconnaît pas l’URL pour l’aliasage de lien.

### Vérification des flux de travail

Braze recommande d’évaluer les liens dans l’e-mail, d’ajouter des modèles de lien et de fournir une convention d'appellation qui fonctionne à des fins de segmentation et de reporting. Cela vous aide à suivre tous les liens ! 

### Extraction des données

Utilisez les endpoints [Alias de lien de campagne][3] et [Alias de lien Canvas][4] pour extraire l’`alias` compris dans chaque variante de message dans une campagne ou un composant e-mail de Canvas.

## Modèles de lien

Pour les nouvelles variantes de message, les modèles de lien existants peuvent être utilisés depuis l’onglet **Link Management (Gestion des liens)**. Pour les messages envoyés avec un modèle de lien, elles seront toujours appliqués. Si un message existant est modifié, le modèle de lien doit être réappliqué dans l’onglet **Link Management (Gestion des liens)**. 

Notez que les modèles de lien ne peuvent être appliqués que pour les liens visibles dans l’onglet **Link Management (Gestion des liens)**. Cela signifie que les liens sans le paramètre d’URL `lid`, comme les « anciens » blocs de contenu ou les liens qui ne peuvent pas être marqués, ne seront pas éligibles pour les modèles de lien. Pour résoudre cela, nous recommandons de copier les « anciens » blocs de contenu ou d’inclure un point d’interrogation (?) ou une esperluette (&) dans l’attribut `href` de l’URL.

## Aliasage de lien dans les blocs de contenu

Les nouveaux blocs de contenu verront leurs liens modifiés lorsque Braze ajoutera un `lid={{placeholder}}` à chaque lien, le cas échéant. Cette valeur de marque substitutive est résolue lorsqu’elle est insérée dans une variante d’e-mail.

Tous les blocs de contenu existants créés avant que Braze n’ait activé cette fonctionnalité ne seront modifiés que lorsque le HTML de ce bloc de contenu sera modifié et que le bloc de contenu sera relancé. Au lieu de relancer le bloc de contenu, nous recommandons de le dupliquer.

Lorsqu’un bloc de contenu sans valeur `lid` est inséré dans un nouveau message, les liens de ce bloc de contenu ne sont pas suivis avec un alias. Lorsqu’un nouveau bloc de contenu est inséré dans une « ancienne » variante de message, les liens de cette variante sont reconnus par l’aliasage de lien. Les liens du bloc de contenu sont également reconnus. Cependant, les « anciens » blocs de contenu ne peuvent pas imbriquer de « nouveaux » blocs de contenu.

{% alert tip %}
Pour les blocs de contenu, Braze recommande de créer des copies des blocs de contenu existants à utiliser dans les nouveaux messages. Cela peut être fait en les dupliquant en masse pour éviter les scénarios où vous pourriez référencer un bloc de contenu qui n’a pas été activé pour l’aliasage de lien dans un nouveau message.
{% endalert %}

## Exemples

Le tableau suivant fournit des exemples de liens dans un corps d’e-mail, des résultats d’aliasage de lien et des explications sur la façon dont le lien d’origine est mis à jour avec l’aliasage de lien.

{%raw%}
| Lien dans le corps de l’e-mail | Lien avec aliasage| Logique |
|---|---|---|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk | Braze insère un point d’interrogation (?) et ajoute le premier paramètre de requête dans l’URL. |
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz | Braze détecte d’autres paramètres de requête et ajoute `lid=` à la fin de l’URL. |
| `<a href="{{custom_attribute.{product_url}}?">` | `<a href=”{{custom_attribute.{product_url}}?lid=ac7a548g5kl7”>` | Braze reconnaît qu’il s’agit d’une URL et qu’elle contient déjà un point d’interrogation (?). Ensuite, il ajoute le paramètre de requête `lid` après le point d’interrogation. |
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email | Braze attend de l’URL qu’elle utilise une structure standard où les ancres (#) sont présentes après un point d’interrogation (?).  Comme Braze lit de gauche à droite, nous ajoutons le point d’interrogation et la valeur `lid` avant l’ancre. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{%endraw%}

## Aliasage de lien pour les URL générées via Liquid

Pour les URL générées par une instruction `assign` dans le HTML ou dans un bloc de contenu, nous vous recommandons d’ajouter un point d’interrogation (?) dans la balise d’ancrage. Cela aidera Braze à ajouter les paramètres de requête (`lid = somevalue`) pour que l’aliasage de lien puisse fonctionner correctement. Sans identifier là où ajouter les paramètres de requête, l’aliasage de lien ne reconnaîtra pas ces URL.

### Exemple

Consultez cet exemple de l’aliasage de lien pour le formatage recommandé de la balise d’ancrage :

{% raw %}

```liquid
{% assign link1 = https://www.braze1.com %}

<a href="{{link1}}?">{{link1}}?</a>
```

{% endraw %}

## Segmentation des liens

Le reciblage des filtres d’alias vous permet de créer des filtres de segmentation en fonction de vos clients qui cliquent sur un alias spécifiquement suivi d’une campagne par e-mail ou composant de Canvas. Ce filtre n’est disponible que pour les campagnes ou Canvas qui ont suivi des alias.

### Suivi des liens

Lors de la rédaction de votre e-mail, une nouvelle colonne apparaîtra dans l’onglet **Link Management (Gestion des liens)**. Vous pouvez sélectionner ici les alias que vous désirez suivre à des fins de segmentation et qui doivent être présents dans les filtres de segmentation. Notez que les alias suivis le sont uniquement à des fins de segmentation et n’auront aucun impact sur votre lien suivi à des fins de reporting.

{% alert tip %}
Pour suivre les indicateurs d’engagement par lien, assurez-vous de faire précéder vos liens par HTTP ou HTTPS.
{% endalert %}

Même si vous pouvez sélectionner un nombre illimité de liens à suivre, Braze n’autorise le reciblage au niveau de l’utilisateur que pour les 100 derniers liens suivis qui ont été cliqués. Par exemple, si vous suivez 500 liens et qu’un utilisateur clique sur chacun d’entre eux, vous aurez la possibilité de recibler ou de créer des segments sur la base des 100 liens qui ont été cliqués en dernier.

{% tabs local %}
{% tab Éditeur Drag & Drop %}

![Onglet Link Management (Gestion des liens) de l’éditeur d’e-mail Drag-and-Drop]({% image_buster /assets/img/link_management_dnd.png %})

{% endtab %}
{% tab Éditeur HTML %}

![Onglet Link Management (Gestion des liens) de l’éditeur d’e-mail HTML]({% image_buster /assets/img/link_management_html.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Braze suit uniquement les 100 derniers alias de liaison cliqués au niveau du profil. 
{% endalert %}

Pour voir tous les alias de lien que vous suivez, rendez-vous sur la page **Manage Settings (Gérer les paramètres)** de la section **Settings(Paramètres)**. Sélectionnez ensuite **Email Settings (Paramètres des e-mails) > Link Aliasing Settings (Paramètres de l’Aliasage de lien)**. Sur la page **Tracked Link Aliases (Alias de lien suivis)**, vous pouvez également désactiver le suivi ainsi que rechercher et trier vos alias.

![Page Tracked Link Aliases (Alias de lien suivis) montrant un alias de lien appelé « test » qui est partie prenante d’une étape Canvas.][8]

### Abandon du suivi des liens

L’abandon du suivi des liens ne permet pas de désaffecter les segments existants avec le filtre de l’alias non suivi. Les anciennes données resteront sur les profils utilisateur jusqu’à ce qu’elles soient supprimées par des données plus récentes. Les filtres de segmentation suivants continuent d’exister, mais de nouveaux segments ne peuvent pas être créés avec ce filtre.

À des fins de segmentation, seuls 100 liens peuvent être suivis par groupe d’apps par défaut. Les liens dans les messages archivés ne seront automatiquement plus suivis. Cependant, si les messages archivés sont désarchivés, les liens devront être resuivis.

Lorsque des alias de liaison sont suivis, les rapports de liens sont indexés par l’alias plutôt que par des domaines de niveau supérieur ou des URL complètes.

![][1]

### Filtres de segment

#### Alias cliqué dans la campagne

Reciblez les utilisateurs sur la base d’un alias qui a été cliqué dans une campagne. Seules les campagnes qui disposent d’alias qui ont été suivis seront reflétées ici.

#### Alias cliqué dans Canvas Step

Reciblez les utilisateurs sur la base d’un alias qui a été cliqué dans un composant Canvas. Une option de filtre délimité par le canal affiche Canvas et composant de Canvas, suivie de l’alias dans le composant Canvas. Seules les Canvas Steps avec des alias suivis seront affichées ici.

#### Alias cliqué dans la campagne ou Canvas

Reciblez les utilisateurs sur la base d’un alias qui a été cliqué dans la campagne ou le composant Canvas. Étant donné que les alias sont considérés comme « globaux », tous les alias globaux ciblent les clics de lien de toutes les campagnes et Canvas Steps.

![][5]

### Filtres basés sur des actions
 
Vous pouvez créer des messages par événement ciblant n’importe quel lien (suivi ou non) ou reciblant des utilisateurs sur la base du fait qu’ils aient cliqué un alias dans une des campagnes par e-mail ou composant de Canvas. 

![][6]

### Événement de clic sur un e-mail

L’[événement de clic sur un e-mail][7] se produit lorsqu’un utilisateur clique sur un e-mail. Plusieurs événements peuvent être générés pour une même campagne si un utilisateur clique plusieurs fois sur un lien ou clique sur plusieurs liens dans l’e-mail. Il existe deux champs supplémentaires dans l’événement de clic sur un e-mail lorsque l’aliasage de lien est activé : `link_id` et `link_alias`.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) ID unique pour cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur,
  "external_user_id": (string) ID externe de l’utilisateur,
  "time": (int) heure en UTC à 10 chiffres de l’événement, en secondes, depuis la période,
  "timezone": (string) fuseau horaire de l’utilisateur au format IANA à l’heure de l’événement,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "message_variation_name": (string) le nom de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "email_address": (string) adresse e-mail pour cet événement,
  "url": (string) l’URL qui a été cliquée (événements e-mail cliqué uniquement),
  "user_agent": (string) description du système et du navigateur de l’utilisateur pour l’événement (événements e-mail cliqué et e-mail ouvert uniquement),
  "ip_pool": (string) ensemble d’IP utilisé pour l’envoi de messages,
  "link_id": (string) valeur unique générée par Braze pour l’URL,
  "link_alias": (string) alias de nom défini quand le message a été envoyé
}
```

{% alert update %}
Le comportement pour `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) comme des événements déclenchés, même lorsqu’ils sont « programmés ». En savoir plus sur le[ comportement de `dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) dans Canvas et les campagnes.

_Mis à jour en août 2019._
{% endalert %}


[1]: {% image_buster /assets/img/link_aliasing_click_table.png %}
[2]: {% image_buster /assets/img/link_aliasing_composer.png %}
[3]: {{site.baseurl}}/get_campaign_link_alias/ 
[4]: {{site.baseurl}}/get_canvas_link_alias/
[5]: {% image_buster /assets/img/link_aliasing_segmentation_filters.png %}
[6]: {% image_buster /assets/img/link_aliasing_action_based_filters.png %}
[7]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/
[8]: {% image_buster /assets/img/tracked_aliases.png %}
