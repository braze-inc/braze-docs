---
nav_title: Codes de promotion
article_title: Codes de promotion
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Découvrez les listes de codes de promotion, afin de pouvoir les ajouter à vos campagnes et Canvas."
---

# Codes de promotion

> Découvrez les listes de codes de promotion, afin de pouvoir les ajouter à vos campagnes et Canvas.

## À propos des codes de promotion

Les codes de promotion vous permettent d'insérer des valeurs uniques et limitées dans le temps dans les messages afin de favoriser les conversions. Chaque liste peut contenir jusqu'à 20 millions de codes, et chaque code peut durer jusqu'à six mois avant d'expirer.

Lorsque Braze envoie un message avec un code de promotion, le code est déduit avant l'envoi du message. Veiller à ce que les codes soient cohérents, uniques et jamais réutilisés :

- Un message qui n'a pas abouti consomme toujours le code.
- Dans les envois multicanaux, le même code est appliqué sur tous les canaux.
- Avec le liquide conditionnel, toutes les listes référencées ont des codes déduits, même si une seule branche est affichée.
- L'entrée ou la réentrée dans une étape du canvas consomme un nouveau code.

Si vous placez plusieurs extraits de la même liste dans un message, Braze appliquera le même code à tous les extraits. Pour éviter d'en manquer, nous vous recommandons de télécharger plus de codes que vous ne prévoyez d'en utiliser.

{% tabs local %}
{% tab Example %}
Considérez les codes de promotion comme des coupons dans un bureau de poste. Une fois que l'employé a retiré un coupon de la pile pour votre lettre, il n'y a plus de coupon, même si la lettre n'arrive jamais.  

Par exemple, dans le Liquid conditionnel suivant, les codes des deux listes (`vip-deal` et `regular-deal`) sont déduits, même si chaque utilisateur ne voit qu'une seule branche :

{% raw %}
```liquid
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert important %}
Les codes de promotion ne peuvent pas être envoyés dans les messages in-app dans Canvas.
{% endalert %}

## Étapes suivantes

Vous cherchez les prochaines étapes ? Commencez ici :

- [Créer une liste de codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/)
- [Utilisation des codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes)
- [Visualisation de l'utilisation des codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#viewing-promotion-code-usage)

## Foire aux questions

### Quels canaux de communication puis-je utiliser avec les codes de promotion ?

Les codes de promotion sont actuellement pris en charge pour l'e-mail, les notifications push sur mobile, les notifications push Web, les cartes de contenu, le webhook, les SMS et WhatsApp. Les campagnes d'e-mails transactionnels de Braze et les messages in-app ne prennent actuellement pas en charge les codes de promotion.

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

Oui. Vous pouvez résoudre ce problème en dépréciant la liste entière ou en utilisant un marque substitutive pour supprimer la liste. Pour plus d'informations, voir [Mise à jour d'une liste de codes de promotion]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#updating-a-promotion-code-list).

### Puis-je enregistrer un code de promotion dans le profil d'un utilisateur pour des messages ultérieurs ?

Oui. Vous pouvez enregistrer des codes de promotion dans le profil d'un utilisateur par le biais d'une étape de mise à jour de l'utilisateur. Pour plus d'informations, voir [Enregistrer les codes de promotion dans les profils utilisateurs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#save-to-profile).
