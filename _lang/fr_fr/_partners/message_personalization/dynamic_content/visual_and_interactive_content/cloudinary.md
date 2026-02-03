---
nav_title: Cloudinary
article_title: Cloudinary
description: "Cet article de référence présente le partenariat entre Braze et cloudinary."
alias: /partners/cloudinary/
page_type: partner
search_tag: Partner
---

# Cloudinary

> [Cloudinary](https://www.cloudinary.com?utm_source=braze_partner_page) est une plateforme d'images et de vidéos utilisée pour gérer, modifier, optimiser et diffuser des images et des vidéos à l'échelle de n'importe quelle campagne à travers les canaux et les parcours clients. Lorsqu'elle est intégrée et activée, la gestion des médias de Cloudinary permet une réception/distribution dynamique, contextuelle et personnalisée des ressources pour vos campagnes et toiles Braze. 

## À propos de cette intégration

La connexion de Cloudinary à Braze permet aux marques d'accéder aux ressources visuelles stockées dans Cloudinary Assets pour les utiliser dans les canaux d'envoi de messages de Braze. Grâce aux liens dynamiques de Cloudinary, vous pouvez sélectionner et personnaliser des images et des vidéos en temps réel en fonction des attributs des utilisateurs de Braze. Ensemble, Cloudinary et Braze soutiennent l'élaboration de campagnes visuellement riches et personnalisées qui racontent l'histoire de chaque produit et offrent des expériences uniques à l'échelle.

Cette page présente quatre méthodes d'intégration possibles, mais non exhaustives, entre Cloudinary et Braze. Ces méthodes d'intégration reposent principalement sur la modification des liens de ressources copiés manuellement depuis la bibliothèque multimédia de Cloudinary. 

{% alert important %}
Des méthodes d'intégration plus avancées, notamment l'utilisation du [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) pour appeler l'[API d'administration](https://cloudinary.com/documentation/admin_api#banner) de Cloudinary, sont possibles, mais l'approche variera selon les clients. Contactez votre gestionnaire de satisfaction client Cloudinary et Braze pour obtenir des conseils.
{% endalert %}

## Conditions préalables

| Exigences     | Description |                        
|-----------------------|-----------------|
| Compte Cloudinary  | Un [compte Cloudinary](https://cloudinary.com/users/register_free?utm_source=braze+docs+page) est nécessaire pour profiter de ce partenariat.  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## Méthodes d’intégration

{% alert tip %}
Certaines de ces méthodes d'intégration utilisent les transformations Cloudinary `f_auto` et `q_auto`, qui offrent une personnalisation plus poussée du comportement et de l'apparence des ressources [image](https://cloudinary.com/documentation/image_transformations#banner) et [vidéo](https://cloudinary.com/documentation/video_manipulation_and_delivery#banner). Pour plus d'informations sur la modification d'un lien de ressource Cloudinary afin d'inclure des transformations, reportez-vous à la [structure de l'URL de transformation.](https://cloudinary.com/documentation/image_transformations#transformation_url_structure)
{% endalert %}

{% tabs %}
{% tab Cloudinary DAM %}

## Sélectionnez les ressources de la campagne via Cloudinary DAM

La façon la plus directe d'utiliser des images et des vidéos directement à partir du DAM de Cloudinary dans vos campagnes et Canvas Braze est de tirer l'URL de la **page** Asset de la bibliothèque multimédia de Cloudinary.

![Une vue en grille de la bibliothèque de ressources d'images de Cloudinary, avec la partie supérieure droite de l'une des images en surbrillance, montrant une infobulle "Copier l'URL".]({% image_buster /assets/img/cloudinary/one.png %})

### Configuration des images et des GIFs

1. Copiez l'URL de l'image ou du GIF depuis le DAM dans Cloudinary en allant dans **Ressources** > **Bibliothèque multimédia** > **Ressources** > **Copier l'URL**.
2. Créez l'étiquette de l'image en HTML, puis ajoutez `f_auto,q_auto` à l'URL copiée pour optimiser l'image ou le GIF.

#### Exemple d'URL d'une image

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/v1678993440/f_auto,q_auto/cld-sample.jpg" alt="Summer Campaign">
</img>
```
{% endraw %}

### Configuration des vidéos

1. Copiez l'image ou le lien GIF du DAM dans Cloudinary en allant dans **Ressources** > **Bibliothèque multimédia** > **Ressources** > **Copier l'URL.**
2. Créez l'étiquette vidéo en HTML, puis ajoutez `f_auto,q_auto` à l'URL copiée pour optimiser automatiquement le format et la qualité de la vidéo.

#### Exemple d'URL vidéo

{% raw %}
```bash
<video class="video" autoplay muted playsinline controls>
  <source src="https://res.cloudinary.com/demo/video/upload/v1651840278/f_auto,q_auto/samples/cld-sample-video.mp4">
</video>
```
{% endraw %}

Reportez-vous à la [vidéo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/video/) pour connaître les spécificités d'Android et d'iOS. 

{% endtab %}
{% tab Convert videoes into GIFs %}

## Convertissez des vidéos en GIFs pour vos e-mails

Utilisez la [transformation Cloudinary](https://cloudinary.com/documentation/image_transformations/) `f_auto:animated` pour convertir automatiquement des ressources vidéo en GIF. Ceci est particulièrement utile si vous utilisez le canal e-mail de Braze, car les GIF sont optimisés pour réduire les charges utiles des e-mails qui, si elles sont trop élevées, peuvent entraîner des problèmes de livrabilité. 

### Configuration de la conversion

1. Copiez l'URL de la vidéo depuis le DAM de Cloudinary.
2. Créez l'étiquette de l'image et ajoutez `f_auto:animated,fl_lossy` pour réduire la taille du GIF et choisissez le meilleur format d'animation pour le client.
3. Ajoutez `c_scale,w_nnn` pour correspondre à la largeur du GIF souhaitée dans la mise en page de l'e-mail.
4. Ajoutez `e_loop` pour boucler l'animation.

#### Exemple d'URL GIF

{% raw %}
```
https://res.cloudinary.com/demo/video/upload/c_scale,w_500,e_loop/f_auto:animated,fl_lossy/samples/cld-sample-video.gif
```
{% endraw %}

{% endtab %}
{% tab Target attributes %}

## Sélectionner dynamiquement les ressources de la campagne en fonction des attributs de ciblage.

Cette méthode d'intégration permet une personnalisation dynamique des médias en sélectionnant intelligemment la meilleure ressource pour chaque utilisateur en fonction de ses attributs en temps réel. 

Si vous incluez des étiquettes Liquid en tant que paramètres dans un lien Cloudinary au sein d'un message de campagne Braze, lors de l'envoi du message, les attributs Braze associés remplaceront dynamiquement les étiquettes Liquid. Il peut s'agir de données spécifiques à l'utilisateur, telles que la langue ou le niveau de clientèle. Cloudinary utilisera alors ces attributs pour déterminer quelle ressource de campagne correspond le mieux à cet utilisateur, et renverra automatiquement la bonne image ou vidéo. Ainsi, les destinataires ne reçoivent que des ressources pertinentes en termes de contexte et approuvées par la marque.

### Fonctionnement

Cloudinary organise les ressources de la campagne à l'aide de [tags](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#tags) et de [métadonnées structurées (SMD)](https://cloudinary.com/documentation/assets_onboarding_metadata_tags_tutorial#structured_metadata) pour les rendre consultables. 

Chaque ressource de la campagne est regroupée sous une étiquette de campagne (par exemple, `spring_launch`) et enrichie de champs de métadonnées structurés qui correspondent à des attributs de Braze tels que `language=en` ou `tier=gold`. Lorsque Braze appelle le lien Cloudinary, une [fonction personnalisée](https://cloudinary.com/documentation/custom_functions#javascript_filters) traite les attributs entrants, recherche la ressource avec les étiquettes et métadonnées correspondantes, puis renvoie la meilleure correspondance. 

Si une correspondance exacte n'est pas trouvée, la fonction sélectionne automatiquement une solution de repli ou une "meilleure option suivante" pour assurer la continuité de chaque expérience. Lorsque la ressource est sélectionnée, la couche de transformation de Cloudinary (par exemple, `f_auto` ou `q_auto`) optimise le média pour la réception/distribution. Cette combinaison d'étiquettes, de métadonnées et de fonctions personnalisées offre aux développeurs un moyen flexible, basé sur l'API, d'automatiser la réception/distribution de ressources personnalisées.

{% alert tip %}
Consultez le [dépôt GitHub`braze-personalization` ](https://github.com/cloudinary-devs/braze-personalization) de Cloudinary pour obtenir des instructions sur la création et l'application de fonctions personnalisées, ainsi qu'un exemple de fonction personnalisée pour la sélection des ressources et les options de repli pour une campagne donnée. Pour plus de conseils, contactez votre équipe d'assistance Cloudinary.
{% endalert %}

### Conditions préalables

Pour permettre une sélection dynamique des ressources, Cloudinary doit pouvoir renvoyer un ensemble de ressources en fonction des tags et des métadonnées. Si le type de réception/distribution de la liste est restreint, Cloudinary ne peut pas fournir la liste dynamique nécessaire à la sélection personnalisée des ressources dans les campagnes de Braze.
- Libérez le type de réception/distribution de la liste : Ouvrez les paramètres de sécurité dans votre console Cloudinary, et décochez l'élément de la liste des ressources sous Types d'images restreints.

### Configuration de la sélection dynamique

1. Configurez l'étiquette et les métadonnées des ressources dans Cloudinary.
2. Téléchargez votre fonction personnalisée sur le DAM de Cloudinary.
3. Créez l'URL Cloudinary pour l'étiquette souhaitée.
4. En utilisant l'URL de la balise comme base, ajoutez des étiquettes Liquid d'image dynamique pour incorporer les attributs Braze et la fonction personnalisée.

#### Exemple d'URL

Cet exemple suppose que les ressources dans Cloudinary ont deux champs SMD définis ("locale" et "audience") renseignés avec les valeurs attendues correspondant aux attributs Braze. En outre, les ressources nécessaires à la campagne ont reçu l'étiquette "samples" et la fonction personnalisée `segmentedBanner.js` a été téléchargée sur le compte Cloudinary. 

{% raw %}
```bash

// Use the appropriate Braze attributes.
{% assign audience = {{custom_attribute.${sample_audience_identifier}}} %} 
{% assign locale = {{${language}}}%} 

// The URL for the "samples" tag used in the campaign is https://papish.cloudinary.us/image/list/v1690000000/samples.json, which is the base for the dynamic image URL.
<img src="https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_#{locale}/$audience_!{audience}!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/campaigns/samples.json" alt="Banner"> 
```
{% endraw %}

##### URL de sortie

- URL de sortie pour les utilisateurs ayant l'audience `internal` et la locale `en`: 
```
https://papish.cloudinary.us/image/list/f_auto,q_auto/$locale_!en!/$audience_!Internal!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- URL de sortie pour les utilisateurs ayant l'audience `external` et la locale `es`: 
```
https://papish.cloudinary.us/image/list/$locale_!es!/$audience_!External!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```
- URL de l'image de repli : 
```
https://papish.cloudinary.us/image/list/$locale_!unknown!/$audience_!unknown!/fn_select:js:v1700000000:segmentedBanner.js/v1690000000/samples.json
```

{% endtab %}
{% tab Personalized image generation %}

## Génération d'images personnalisées

Les [transformations de superposition de texte](https://cloudinary.com/documentation/accessible_media_visual_audio_clarity#text_overlays_on_images_and_videos/) de Cloudinary utilisent les données utilisateur de Braze directement au sein d'une ressource Cloudinary. 

L'exemple suivant montre comment la transformation `l_text` peut être utilisée pour insérer le nom d'un utilisateur dans une ressource. Une personnalisation plus poussée peut être obtenue en exploitant les étiquettes Liquid lors de l'élaboration des campagnes et des canevas pour déterminer le texte qui doit remplir les paramètres `l_text`.

Pour plus de conseils sur la façon dont les paramètres de transformation peuvent être utilisés pour concevoir une ressource, contactez votre équipe d'assistance Cloudinary.

### Exemple `l_text` Transformation

{% raw %}
```bash
{% assign first_name = {{${first_name}}}%} 
{% assign second_name = {{${last_name}}}%} 

<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20{{first_name}}%20{{second_name}}%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

#### Exemple d'URL de sortie

{% raw %}
```bash
<img src="https://res.cloudinary.com/demo/image/upload/l_text:Arial_300:%20John%20Smith%20,co_white,b_rgb:00000080/fl_layer_apply,g_north_west,y_200/docs/white-church-europe-sea.jpg">
```
{% endraw %}

![Une église blanche avec un toit bleu surplombant la mer, en haut à gauche de l'image les mots "John Smith" sont imposés sur un grand rectangle foncé opaque.]({% image_buster /assets/img/cloudinary/two.png %})

```
{% endtab %}
{% endtabs %}
