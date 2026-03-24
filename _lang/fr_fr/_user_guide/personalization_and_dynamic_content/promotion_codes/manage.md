---
nav_title: Utilisation des codes
article_title: Utilisation des codes de promotion
page_order: 0.2
description: "Découvrez comment utiliser les codes de promotion et consulter leur utilisation pour vos campagnes et vos canevas."
---

# Utilisation des codes de promotion

> Découvrez comment utiliser les codes de promotion et consulter leur utilisation pour vos campagnes et vos canevas.

## Conditions préalables

Avant de pouvoir utiliser des codes de promotion, il est nécessaire de [créer une liste de codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/).

## Utilisation des codes de promotion

Pour inclure un code de promotion dans un message, veuillez sélectionner **Copier l'extrait de code** à côté de la liste des codes de promotion [que vous avez précédemment créée]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#create).

![Une option permettant de copier l'extrait de code afin de le coller dans votre message.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Veuillez coller les extraits de code dans l'un de vos messages dans Braze, puis utilisez [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) pour insérer l'un des codes de promotion uniques de votre liste. Ce code est marqué comme envoyé, garantissant qu'aucun autre message n'envoie le même code.

![Exemple de message : « Offrez-vous quelque chose de spécial ce printemps grâce à notre offre exclusive », suivi d'un extrait de code.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### À travers les étapes du canvas

Lorsqu'un extrait de code est utilisé dans une campagne ou un canvas avec des messages multicanaux, chaque utilisateur reçoit un code unique. Dans un canvas comportant plusieurs étapes faisant référence à des codes de promotion, un utilisateur reçoit un nouveau code pour chaque étape qu'il franchit.

Pour attribuer un code de promotion dans un canvas et le réutiliser à plusieurs étapes :

1. Veuillez attribuer le code de promotion en tant qu'attribut personnalisé lors de la première étape (Mise à jour utilisateur).
2. Veuillez utiliser Liquid dans les étapes suivantes pour référencer cet attribut personnalisé au lieu de générer un nouveau code.

Lorsqu'un utilisateur remplit les conditions requises pour obtenir un code sur plusieurs canaux, il reçoit le même code sur chaque canal. Par exemple, s'ils reçoivent des messages par e-mail et par notification push, le même code est envoyé aux deux. Le rapport reflète également un code unique.

{% alert note %}
Si aucun code de promotion n'est disponible, les messages de test ou en ligne/en production/instantanés qui dépendent de codes ne seront pas envoyés.
{% endalert %}

### Campagnes de messages in-app {#promotion-codes-iam-campaigns}

Après avoir créé une [campagne de messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), vous pouvez insérer un [extrait de liste de codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes-1) dans le corps de votre message in-app. Les codes de promotion contenus dans les messages in-app ne sont déduits et utilisés que lorsqu'un utilisateur déclenche l'affichage du message in-app.

### Messages de test

Les envois de test et les envois du groupe initiateur d'e-mails utilisent les codes de promotion, sauf indication contraire. Contactez votre gestionnaire de compte Braze pour mettre à jour le comportement de cette fonctionnalité afin que les codes de promotion ne soient pas utilisés lors des envois de tests et des envois d'e-mails de groupes initiateurs.

### Avec des messages supplémentaires pour Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Enregistrement des codes de promotion dans les profils utilisateurs {#save-to-profile}

Pour référencer le même code de promotion dans les messages suivants, le code doit être enregistré dans le profil de l'utilisateur en tant qu'attribut personnalisé. Cela peut être réalisé via une [étape « Mise à jour utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) » qui attribue le code de réduction à un attribut personnalisé, tel que « Code promotionnel », immédiatement avant une étape « Message ».

Tout d'abord, veuillez sélectionner les options suivantes pour chaque champ dans l'étape Mise à jour utilisateur :

- **Nom de l'attribut :** Code promotionnel
- **Action :** Mettre à jour
- **Valeur clé :** Le code de promotion est un extrait de code Liquid, tel que {% raw %}`{% promotion('spring25') %}`{% endraw %}

Deuxièmement, veuillez ajouter l'attribut personnalisé (dans cet exemple, {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}) à un message. Le code de réduction est intégré au modèle.

## Affichage de l'utilisation des codes de promotion

Vous trouverez le nombre de codes restants dans la colonne **Reste de** la liste des codes de promotion sur la page **Codes de promotion**.

![Exemple de code de promotion avec des codes non utilisés.]({% image_buster /assets/img/promocodes/promocode11.png %})

Ce nombre de codes peut également être trouvé en revisitant une page de liste de codes de promotion préexistante. Vous pouvez également exporter les codes d'exportation sous la forme d'un fichier CSV. 

![Un code de promotion intitulé « Black Friday Sale » avec 992 codes restants.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Envois multicanaux et monocanaux

Pour les campagnes multicanales et à envoi unique et les Canvases, tous les codes de promotion référencés dans le Liquid d'un message sont déduits pour être utilisés **avant l'** envoi du message afin de s'assurer de ce qui suit :

- Les mêmes codes de promotion sont utilisés d'un canal à l'autre dans un message multicanal.
- Les codes de promotion supplémentaires ne sont pas utilisés si un message échoue ou est interrompu.

Si un utilisateur dispose de deux listes de codes de promotion référencées dans un message divisé par une étiquette de logique conditionnelle Liquid, tous les codes de promotion sont toujours déduits, quel que soit le flux conditionnel suivi par l'utilisateur.

Si un utilisateur accède à une nouvelle étape du canvas ou accède à nouveau à Canvas, et que le code de promotion Liquid snippet est appliqué une nouvelle fois pour un message destiné à cet utilisateur, un nouveau code de promotion est utilisé.

### Exemple

Dans l'exemple suivant, les deux listes`vip-deal`de codes`regular-deal` de promotion sont déduites. Voici le Liquid :

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze recommande de télécharger un nombre de codes de promotion supérieur à celui que vous prévoyez d'utiliser. Si une liste de codes de promotion expire ou si les codes de promotion sont épuisés, les messages suivants sont interrompus.

{% alert tip %}
**Voici une analogie de l'utilisation des codes de promotion dans Braze.** <br><br>Imaginez que l'envoi de votre message s'apparente à l'envoi d'une lettre à la poste. Vous remettez la lettre à un employé, qui constate que votre lettre doit comporter un coupon. L'employé retire le premier coupon de la pile et l'ajoute à l'enveloppe. Le greffier envoie la lettre, mais pour une raison quelconque, la lettre se perd dans le courrier (et le coupon est également perdu). <br><br>Dans ce scénario, Braze représente l'employé de la poste et votre code de promotion correspond au coupon. Nous ne pouvons pas le récupérer une fois qu'il a été retiré de la pile des codes de promotion, quel que soit le résultat du webhook.
{% endalert %}
