---
nav_title: Codes de promotion
article_title: Codes de promotion
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Cet article de référence explique comment créer des listes de codes de promotion et les ajouter à vos campagnes et Canvas."
---

# Codes de promotion

> Cette page explique comment créer des listes de codes de promotion et les ajouter à vos campagnes et Canvas.

## A propos des codes de promotion

Les codes de promotion - également appelés codes promo - sont un excellent moyen de maintenir l'engagement des utilisateurs en suscitant des interactions avec un fort accent sur les achats. Vous pouvez créer des messages à partir de votre liste de codes de promotion. 

Chaque code de promotion a une date d'expiration pouvant aller jusqu'à six mois. Vous pouvez stocker et gérer jusqu'à 20 millions de codes par liste. En gérant et en analysant les performances de vos codes de promotion, vous pouvez prendre des décisions ciblées pour vos stratégies promotionnelles et vos envois de messages.

{% alert important %}
Les codes de promotion ne peuvent pas être envoyés dans les messages in-app dans Canvas.
{% endalert %}

## Création d'une liste de codes de promotion {#create}

### Étape 1 : Accédez à la section Code de promotion

\![Bouton pour créer un code de promotion.]({% image_buster /assets/img/promocodes/promocode1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

1. Dans le tableau de bord, allez dans **Paramètres des données** > **Codes de promotion**.
2. Sélectionnez **Créer une liste de codes de promotion**.

### Étape 2 : Nommez le code de promotion

1. Donnez un nom à votre liste de codes de promotion et ajoutez une description facultative.
2. Créez ensuite un extrait de code pour le code de promotion. 

Voici quelques détails à prendre en compte lors de la création d'un extrait de code :

- Une fois enregistrés, les extraits de code ne peuvent plus être modifiés.
- Les extraits de code sont sensibles à la casse. Par exemple, "Birthday_promo" et "birthday_promo" seront reconnus comme deux extraits de code différents.
- Utilisez le nom de l'extrait dans Liquid pour référencer cet ensemble de codes de promotion.
- Assurez-vous que l'extrait de code n'est pas déjà utilisé dans une autre liste.

Une liste de codes de promotion nommée "SpringSale2025" avec l'extrait de code "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Étape 3 : Choisissez les options du code de promotion

Chaque liste de codes de promotion est assortie d'une date et d'une heure d'expiration qui sont définies lors de la création. La durée maximale d'expiration est de six mois à compter du jour où vous créez ou modifiez votre liste. 

Pendant cette période, vous pouvez modifier et mettre à jour la date d'expiration à plusieurs reprises. Cette date d'expiration s'appliquera à tous les codes ajoutés à cette liste. À l'expiration, les codes seront supprimés du système Braze et les messages appelant l'extrait de code de cette liste ne seront pas envoyés.

Les paramètres d'expiration de la liste indiquent que tous les codes restants expireront le 30 avril 2025 à 12 heures.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Vous avez également la possibilité de mettre en place des alertes de seuil facultatives et personnalisées. Si elles sont paramétrées, ces alertes enverront un e-mail au destinataire désigné soit lorsque le nombre de codes de promotion disponibles dans cette liste est faible, soit lorsque votre liste de codes de promotion est proche de l'expiration. Le destinataire sera informé une fois par jour.

\![Exemple d'alerte de seuil pour avertir "marketeur@abc.com" lorsque la liste des codes de promotion expire dans 5 jours.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Étape 4 : Télécharger des codes de promotion

Braze ne gère pas la création ou l'échange de codes, ce qui signifie que vous devez générer vos codes de promotion dans un fichier CSV et les télécharger dans Braze. 

Veillez à ce que votre fichier CSV respecte ces directives :

- Comprend une colonne pour les codes de promotion.
- Chaque ligne contient un code de promotion.

Vous pouvez utiliser notre intégration intégrée avec [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) pour créer et exporter des codes de promotion.

{% alert important %}
La taille maximale du fichier est de 100 Mo et la taille maximale de la liste est de 20MM de codes non utilisés. Si vous constatez que le fichier téléchargé n'est pas le bon, téléchargez-en un nouveau et le précédent sera remplacé.
{% endalert %}

1. Une fois le téléchargement terminé, sélectionnez **Enregistrer la liste** pour enregistrer tous les détails et les codes que vous venez de saisir.

!fichier CSV nommé "springsale" qui a été téléchargé avec succès.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Après avoir choisi d'enregistrer, une nouvelle ligne apparaît dans l'**historique des importations.**
3\. Pour actualiser le tableau afin de savoir si votre importation est terminée, sélectionnez <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** en haut du tableau.

Les codes de promotion sont en cours de téléchargement.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
L'importation de fichiers plus volumineux prendra quelques minutes. Pendant que vous attendez, vous pouvez quitter la page et travailler sur quelque chose pendant que l'importation est en cours. Lorsque l'importation est terminée, le statut devient **Complet** dans le tableau.
{% endalert %}

## Mise à jour d'une liste de codes de promotion

Pour mettre à jour une liste, sélectionnez l'une de vos listes existantes. Vous pouvez modifier le nom, la description, l'expiration de la liste et les seuils d'alerte. Vous pouvez également ajouter d'autres codes à la liste en téléchargeant de nouveaux fichiers et en sélectionnant **Mettre à jour la liste.** Tous les codes de la liste auront la même date d'expiration, quelle que soit la date d'importation.

{% alert important %}
Les codes de promotion ne peuvent pas être supprimés.
{% endalert %}

### Modification de la liste des codes de promotion incorrects 

Si vous avez téléchargé un fichier CSV contenant des codes de promotion incorrects et sélectionné **Enregistrer la liste**, vous pouvez résoudre le problème par l'une ou l'autre méthode :

- Déprécier la liste entière : N'utilisez plus la liste actuelle des codes de promotion dans les campagnes, les canevas ou les modèles. Ensuite, téléchargez le fichier CSV avec les codes corrects et utilisez-les dans votre envoi de messages.
- Utilisez les codes incorrects : Créez une campagne qui envoie les codes de promotion de la liste des codes de promotion incorrects à un marque substitutive jusqu'à ce que tous les codes incorrects soient utilisés. Ensuite, téléchargez les codes de promotion corrects dans la même liste.

## Utilisation des codes de promotion {#update}

Pour envoyer un code de promotion dans un message, sélectionnez **Copier l'extrait en** regard de la liste de codes de promotion [que vous avez précédemment créée](#create).

\![Une option permettant de copier l'extrait de code pour le coller dans votre message.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:50%"}

Collez les extraits de code dans l'un de vos messages dans Braze, puis utilisez [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) pour insérer l'un des codes de promotion uniques de votre liste. Ce code sera marqué comme envoyé, ce qui garantit qu'aucun autre message n'enverra le même code.

\![Un exemple de message "Offrez-vous quelque chose de beau ce printemps avec notre offre exclusive" suivi de l'extrait de code.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:50%"}

### À travers les étapes du canvas

Lorsqu'un extrait de code est utilisé dans une campagne ou un canvas avec des messages multicanaux, chaque utilisateur reçoit un code unique. Dans un canvas comportant plusieurs étapes qui font référence à des codes de promotion, l'utilisateur reçoit un nouveau code pour chaque étape qu'il franchit.

Pour attribuer un code de promotion dans un canvas et le réutiliser dans toutes les étapes :

1. Attribuez le code de promotion en tant qu'attribut personnalisé lors de la première étape (Mise à jour de l'utilisateur).
2. Utilisez Liquid dans les étapes suivantes pour faire référence à cet attribut personnalisé au lieu de générer un nouveau code.

Lorsqu'un utilisateur se qualifie pour un code sur plusieurs canaux, il reçoit le même code sur chaque canal. Par exemple, s'ils reçoivent des messages par e-mail et par push, le même code est envoyé aux deux. Les rapports reflètent également un code unique.

{% alert note %}
Si aucun code de promotion n'est disponible, les messages de test ou en ligne/en production qui s'appuient sur des codes ne seront pas envoyés.
{% endalert %}

### Dans les campagnes de messages in-app. {#promotion-codes-iam-campaigns}

Après avoir créé une [campagne de messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), vous pouvez insérer un [extrait de liste de codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) dans le corps de votre message in-app. 

Les codes promotionnels dans les messages in-app seront déduits et utilisés uniquement lorsqu'un utilisateur déclenche l'affichage du message in-app.

### Dans les messages de test

Les envois de tests et les envois d'e-mails de groupes initiateurs utiliseront les codes promotionnels, sauf demande contraire. Contactez votre gestionnaire de compte Braze pour mettre à jour le comportement de cette fonctionnalité afin que les codes de promotion ne soient pas utilisés lors des envois de tests et des envois d'e-mails de groupes initiateurs.

### Avec envoi de messages supplémentaires pour Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Enregistrer les codes de promotion dans les profils utilisateurs {#save-to-profile}

Pour référencer le même code de promotion dans les messages suivants, le code doit être enregistré dans le profil de l'utilisateur en tant qu'attribut personnalisé. Cela peut se faire par le biais d'une [étape de mise à jour de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) qui attribue le code de réduction à un attribut personnalisé, comme "Code promo", directement avant une étape de message.

Tout d'abord, sélectionnez les éléments suivants pour chaque champ de l'étape de mise à jour de l'utilisateur :

- **Nom de l'attribut :** Code promo
- **Action :** Mise à jour
- **Valeur clé :** L'extrait de code liquid du code de promotion, par exemple {% raw %}`{% promotion('spring25') %}`{% endraw %}

Ensuite, ajoutez l'attribut personnalisé (dans cet exemple, {% raw %}`{{custom_attribute.${Promo Code}}`{% endraw %}) à un message. Le code de réduction sera intégré dans le modèle.

## Visualisation de l'utilisation des codes de promotion

Vous trouverez le nombre de codes restants dans la colonne **Reste de** la liste des codes de promotion sur la page **Codes de promotion**.

\![Un exemple de code de promotion avec des codes non utilisés.]({% image_buster /assets/img/promocodes/promocode11.png %})

Ce nombre de codes peut également être trouvé en revisitant une page de liste de codes de promotion préexistante. Vous pouvez également exporter les codes d'exportation sous la forme d'un fichier CSV. 

Un code de promotion nommé "Black Friday Sale" avec 992 codes restants.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:50%"}

## Envois multicanaux et monocanaux

Pour les campagnes multicanales et à envoi unique et les Canvases, tous les codes de promotion référencés dans le Liquid d'un message sont déduits pour être utilisés **avant l'** envoi du message afin de s'assurer de ce qui suit :

- Les mêmes codes de promotion sont utilisés d'un canal à l'autre dans un message multicanal.
- Les codes de promotion supplémentaires ne sont pas utilisés en cas d'échec ou d'interruption d'un message.

Si un utilisateur a deux listes de codes promotionnels référencées dans un message qui est divisé par une étiquette de logique conditionnelle Liquid, tous les codes promotionnels seront toujours déduits, quel que soit le flux conditionnel suivi par l'utilisateur.

Si un utilisateur entre dans une nouvelle étape du canvas ou réintègre un canvas, et que l'extrait de liquid code de promotion est à nouveau appliqué pour un envoi de messages à cet utilisateur, un nouveau code de promotion sera utilisé.

### Exemple

Dans l'exemple suivant, les deux listes de codes de promotion `vip-deal` et `regular-deal` seront déduites. Voici le liquide :

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze recommande de télécharger plus de codes de promotion que ce que vous estimez être utilisé. Si une liste de codes de promotion expire ou s'il n'y a plus de codes de promotion, les messages suivants seront interrompus.

{% alert tip %}
**Voici une analogie de l'utilisation des codes de promotion dans Braze.** <br><br>Imaginez que l'envoi de votre message s'apparente à l'envoi d'une lettre à la poste. Vous remettez la lettre à un employé, qui constate que votre lettre doit comporter un coupon. L'employé retire le premier coupon de la pile et l'ajoute à l'enveloppe. Le greffier envoie la lettre, mais pour une raison quelconque, la lettre se perd dans le courrier (et le coupon est également perdu). <br><br>Dans ce scénario, Braze est l'employé de la poste et votre code de promotion est le coupon. Nous ne pouvons pas le récupérer une fois qu'il a été retiré de la pile de codes de promotion, quel que soit le résultat du webhook.
{% endalert %}

## Questions fréquemment posées

### Quels canaux de communication puis-je utiliser avec les codes de promotion ?

Les codes de promotion sont actuellement pris en charge pour l'e-mail, le push mobile, le push web, les cartes de contenu, le webhook, les SMS et WhatsApp. Les campagnes d'e-mails transactionnels de Braze et les messages in-app ne prennent actuellement pas en charge les codes de promotion.

### Les envois de tests et d'initiateurs sont-ils pris en compte dans le calcul de l'utilisation ?

Par défaut, les envois de tests et les envois d'e-mails de groupes initiateurs utiliseront des codes promotionnels par utilisateur, par envoi de tests. Cependant, vous pouvez contacter votre gestionnaire de compte Braze pour mettre à jour ce comportement afin de ne pas utiliser de codes de promotion pendant les tests.

### Que se passe-t-il lorsque plusieurs canaux de communication utilisent le même extrait de code de promotion ?

Si un utilisateur donné est éligible pour recevoir un code par le biais de plusieurs canaux, il recevra le même code par le biais de chaque canal. Un seul code promo sera utilisé, quels que soient les canaux reçus.

### Puis-je utiliser plusieurs extraits liquid pour référencer la même liste de codes de promotion dans un message ?

Oui. Braze appliquera le même code de promotion à toutes les instances de cet extrait dans le message, afin que l'utilisateur ne reçoive qu'un code unique.

### Que se passe-t-il lorsqu'une liste de codes de promotion est expirée ou vide ?

Les codes expirés sont supprimés au bout de six mois.

Si le message aurait dû contenir un code de promotion provenant d'une liste vide ou expirée, le message sera annulé. 

Si le message contient une logique conditionnelle d'insertion d'un code promotionnel, le message ne sera annulé que s'il aurait dû contenir un code promotionnel. Si le message n'aurait pas dû contenir de code de promotion, le message sera envoyé normalement.

### Si j'ai téléchargé les mauvais codes de promotion, puis-je les mettre à jour ?

Oui. Vous pouvez résoudre ce problème en dépréciant la liste entière ou en utilisant un marque substitutive pour supprimer la liste. Pour plus d'informations, voir [Mise à jour des codes de promotion](#update).

### Puis-je enregistrer un code de promotion dans le profil d'un utilisateur pour des messages ultérieurs ?

Oui. Vous pouvez enregistrer des codes de promotion dans le profil d'un utilisateur par le biais d'une étape de mise à jour de l'utilisateur. Pour plus d'informations, voir [Enregistrer les codes de promotion dans les profils utilisateurs](#save-to-profile).
