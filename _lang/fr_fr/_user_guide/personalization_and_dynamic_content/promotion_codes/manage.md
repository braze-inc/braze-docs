---
nav_title: Utilisation des codes
article_title: Utilisation des codes de promotion
page_order: 0.2
description: "Apprenez à utiliser les codes de promotion et à visualiser l'utilisation de vos campagnes et de vos toiles."
---

# Utilisation des codes de promotion

> Apprenez à utiliser les codes de promotion et à visualiser l'utilisation de vos campagnes et de vos toiles.

## Conditions préalables

Avant de pouvoir utiliser des codes de promotion, vous devez [créer une liste de codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/).

## Utilisation des codes de promotion

Pour envoyer un code de promotion dans un message, sélectionnez **Copier l'extrait en** regard de la liste de codes de promotion [que vous avez précédemment créée]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#create).

![Une option permettant de copier l'extrait de code pour le coller dans votre message.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Collez les extraits de code dans l'un de vos messages dans Braze, puis utilisez [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) pour insérer l'un des codes de promotion uniques de votre liste. Ce code est marqué comme envoyé, ce qui garantit qu'aucun autre message n'envoie le même code.

![Un exemple de message "Offrez-vous quelque chose de beau ce printemps avec notre offre exclusive" suivi de l'extrait de code.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### À travers les étapes du canvas

Lorsqu'un extrait de code est utilisé dans une campagne ou un canvas avec des messages multicanaux, chaque utilisateur reçoit un code unique. Dans un canvas comportant plusieurs étapes qui font référence à des codes de promotion, l'utilisateur reçoit un nouveau code pour chaque étape qu'il franchit.

Pour attribuer un code de promotion dans un canvas et le réutiliser dans toutes les étapes :

1. Attribuez le code de promotion en tant qu'attribut personnalisé lors de la première étape (Mise à jour de l'utilisateur).
2. Utilisez Liquid dans les étapes suivantes pour faire référence à cet attribut personnalisé au lieu de générer un nouveau code.

Lorsqu'un utilisateur se qualifie pour un code sur plusieurs canaux, il reçoit le même code sur chaque canal. Par exemple, s'ils reçoivent des messages par e-mail et par push, le même code est envoyé aux deux. Les rapports reflètent également un code unique.

{% alert note %}
Si aucun code de promotion n'est disponible, les messages de test ou en ligne/en production qui dépendent des codes ne sont pas envoyés.
{% endalert %}

### Campagnes de messages in-app {#promotion-codes-iam-campaigns}

Après avoir créé une [campagne de messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), vous pouvez insérer un [extrait de liste de codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes-1) dans le corps de votre message in-app. Les codes promotionnels dans les messages in-app sont déduits et utilisés uniquement lorsqu'un utilisateur déclenche l'affichage du message in-app.

### Envois de messages

Les envois de test et les envois d'e-mails de groupes initiateurs utilisent des codes promotionnels, sauf demande contraire. Contactez votre gestionnaire de compte Braze pour mettre à jour le comportement de cette fonctionnalité afin que les codes de promotion ne soient pas utilisés lors des envois de tests et des envois d'e-mails de groupes initiateurs.

### Avec envoi de messages supplémentaires pour Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Enregistrer les codes de promotion dans les profils utilisateurs {#save-to-profile}

Pour référencer le même code de promotion dans les messages suivants, le code doit être enregistré dans le profil de l'utilisateur en tant qu'attribut personnalisé. Cela peut se faire par le biais d'une [étape de mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) qui attribue le code de réduction à un attribut personnalisé, tel que "Code promo", directement avant une étape de message.

Tout d'abord, sélectionnez les éléments suivants pour chaque champ de l'étape de mise à jour de l'utilisateur :

- **Nom de l'attribut :** Code promo
- **Action :** Mettre à jour
- **Valeur clé :** L'extrait de code liquid du code de promotion, par exemple {% raw %}`{% promotion('spring25') %}`{% endraw %}

Ensuite, ajoutez l'attribut personnalisé (dans cet exemple, {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}) à un message. Le code de réduction est présenté sous forme de modèle.

## Visualisation de l'utilisation des codes de promotion

Vous trouverez le nombre de codes restants dans la colonne **Reste de** la liste des codes de promotion sur la page **Codes de promotion**.

![Un exemple de code de promotion avec des codes non utilisés.]({% image_buster /assets/img/promocodes/promocode11.png %})

Ce nombre de codes peut également être trouvé en revisitant une page de liste de codes de promotion préexistante. Vous pouvez également exporter les codes d'exportation sous la forme d'un fichier CSV. 

![Un code de promotion nommé "Black Friday Sale" avec 992 codes restants.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Envois multicanaux et monocanaux

Pour les campagnes multicanales et à envoi unique et les Canvases, tous les codes de promotion référencés dans le Liquid d'un message sont déduits pour être utilisés **avant l'** envoi du message afin de s'assurer de ce qui suit :

- Les mêmes codes de promotion sont utilisés d'un canal à l'autre dans un message multicanal.
- Les codes de promotion supplémentaires ne sont pas utilisés en cas d'échec ou d'interruption d'un message.

Si un utilisateur a deux listes de codes promotionnels référencées dans un message qui est divisé par une étiquette de logique conditionnelle Liquid, tous les codes promotionnels sont toujours déduits, quel que soit le flux conditionnel suivi par l'utilisateur.

Si un utilisateur entre dans une nouvelle étape du Canvas ou réintègre un Canvas, et que le code promotionnel Liquid snippet est à nouveau appliqué pour un envoi de messages à cet utilisateur, un nouveau code promotionnel est utilisé.

### Exemple

Dans l'exemple suivant, les deux listes de codes de promotion `vip-deal` et `regular-deal` sont déduites. Voici le Liquid :

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze recommande de télécharger plus de codes de promotion que ce que vous estimez utiliser. Si une liste de codes de promotion expire ou s'il n'y a plus de codes de promotion, les messages suivants sont interrompus.

{% alert tip %}
**Voici une analogie de l'utilisation des codes de promotion dans Braze.** <br><br>Imaginez que l'envoi de votre message s'apparente à l'envoi d'une lettre à la poste. Vous remettez la lettre à un employé, qui constate que votre lettre doit comporter un coupon. L'employé retire le premier coupon de la pile et l'ajoute à l'enveloppe. Le greffier envoie la lettre, mais pour une raison quelconque, la lettre se perd dans le courrier (et le coupon est également perdu). <br><br>Dans ce scénario, Braze est l'employé de la poste et votre code de promotion est le coupon. Nous ne pouvons pas le récupérer une fois qu'il a été retiré de la pile de codes de promotion, quel que soit le résultat du webhook.
{% endalert %}
