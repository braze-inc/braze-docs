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

## 

Les codes de promotion également appelés codes promo, sont un excellent moyen de maintenir l’engagement des utilisateurs en conduisant des interactions en soulignant les achats.  

  

{% alert important %}
Les codes de promotion ne peuvent pas être envoyés dans des messages in-app.
{% endalert %}

## Créer une liste de codes de promotion

### Étape 1 : 



1. 
2. 

### Étape 2 : 

1. Nommez votre liste de codes de promotion et ajoutez une description facultative.
2. Ensuite, créez un extrait de code pour le code de promotion. 



- 
- Les extraits de code sont sensibles à la casse. Par exemple, "Birthday_promo" et "birthday_promo" seront reconnus comme deux extraits de code différents.
- 
- 



### Étape 3 : 

Chaque liste de codes de promotion est assortie d'une date et d'une heure d'expiration qui sont définies lors de la création. La durée maximale d'expiration est de six mois à compter du jour où vous créez ou modifiez votre liste. 

Dans ce délai, vous pouvez modifier et mettre à jour la date d’expiration à plusieurs reprises. Cette date d’expiration s’applique à tous les codes ajoutés à cette liste. À l’expiration, les codes sont supprimés du système Braze et tous les messages appelant l’extrait de code de cette liste ne sont pas envoyés.



Vous avez également la possibilité de mettre en place des alertes de seuil facultatives et personnalisées. Si cette option est définie, ces alertes envoient un e-mail au destinataire désigné, soit lorsque la liste est en cours de fonctionnement sur les codes de promotion disponibles dans cette liste, soit lorsque votre liste de codes de promotion est proche de l’expiration. Le destinataire est notifié une fois par jour.



### Étape 4 : 

Braze ne gère pas la création ou l'échange de codes, ce qui signifie que vous devez générer vos codes de promotion dans un fichier CSV et les télécharger dans Braze. 



- Comprend une colonne pour les codes de promotion.
- Chaque ligne contient un code de promotion.

Vous pouvez utiliser notre intégration intégrée avec [Voucherify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/talonone/) pour créer et exporter des codes de promotion.

{% alert important %}
La taille maximale du fichier est de 100 Mo et la taille maximale de la liste est de 20 MM de codes non utilisés. Si vous constatez que le fichier téléchargé n'est pas le bon, téléchargez-en un nouveau et le précédent sera remplacé.
{% endalert %}

1. Une fois le téléchargement terminé, sélectionnez **Enregistrer la liste** pour enregistrer tous les détails et codes que vous venez de saisir.




 
 



{% alert note %}
Les fichiers plus volumineux prendront quelques minutes à importer. Pendant que vous attendez, vous pouvez quitter la page et travailler sur autre chose pendant que l'importation est en cours. Lorsque l'importation est terminée, le statut devient **Complet** dans le tableau.
{% endalert %}

#### Mettre à jour une liste de codes de promotion

Pour mettre à jour une liste, sélectionnez l'une de vos listes existantes. Vous pouvez modifier le nom, la description, l'expiration de la liste et les seuils d'alerte. Vous pouvez également ajouter d'autres codes à la liste en téléchargeant de nouveaux fichiers et en sélectionnant **Mettre à jour la liste.**

Tous les codes de la liste auront la même expiration, quelle que soit la date d’importation.

### Étape 5 : Utiliser des codes de promotion



1. 




 À partir de là, vous pouvez coller ce code dans un message du tableau de bord.



 Ce code sera marqué comme envoyé sur le backend Braze pour s’assurer qu’aucun autre message n’envoie ce même code.

#### 

Lorsqu’un extrait de code est utilisé dans une campagne multicanal ou une étape de Canvas, chaque utilisateur reçoit toujours un code unique. Pour les différentes étapes d'un Canvas, chaque utilisateur reçoit plusieurs codes de promotion.

  Ceci s’applique également aux objectifs de reporting : un code sera envoyé et reçu par l’utilisateur via les deux canaux. Par exemple, pour une étape Canvas multicanale, un seul code serait utilisé par l’utilisateur.

{% alert important %}
S'il n'y a plus de codes promotionnels disponibles lors de l'envoi de messages de test ou en ligne/en production à partir d'une campagne qui tire des codes promotionnels, le message ne sera pas envoyé.
{% endalert %}

#### Envoi de messages de test avec des codes de promotion

Les envois de tests et les envois d'e-mails de groupes initiateurs utiliseront les codes promotionnels, sauf demande contraire. Contactez votre gestionnaire de compte Braze pour mettre à jour le comportement de cette fonctionnalité afin que les codes de promotion ne soient pas utilisés lors des envois de tests et des envois d'e-mails de groupes initiateurs.

## Déterminer le nombre de codes utilisés





Ce nombre de codes peut également être trouvé en revisitant une page de liste de codes de promotion préexistante.  



## Envois multicanaux et monocanaux

Pour les campagnes multicanales et à envoi unique et les Canvases, tous les codes de promotion référencés dans le Liquid d'un message sont déduits pour être utilisés **avant l'** envoi du message afin de s'assurer de ce qui suit :

- Les mêmes codes de promotion sont utilisés d'un canal à l'autre dans un message multicanal.
- Les codes de promotion supplémentaires ne sont pas utilisés en cas d'échec ou d'interruption d'un message.

Si un utilisateur a deux listes de codes promotionnels référencées dans un message qui est divisé par une étiquette de logique conditionnelle Liquid, tous les codes promotionnels seront toujours déduits, quel que soit le flux conditionnel suivi par l'utilisateur.

Si un utilisateur entre dans une nouvelle étape du canvas ou réintègre un canvas, et que l'extrait de liquid code de promotion est à nouveau appliqué pour un envoi de messages à cet utilisateur, un nouveau code de promotion sera utilisé.

### Cas d’utilisation

Dans l'exemple suivant, les deux listes de codes de promotion `vip-deal` et `regular-deal` seront déduites. Voici le Liquid :

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
**Voici une analogie de l'utilisation des codes de promotion dans Braze.** <br><br>Imaginez que l'envoi de votre message s'apparente à l'envoi d'une lettre à la poste. Vous remettez la lettre à un employé, qui constate que votre lettre doit comporter un coupon. L'employé retire le premier coupon de la pile et l'ajoute à l'enveloppe. Le greffier envoie la lettre, mais pour une raison quelconque, la lettre se perd dans le courrier (et le coupon est également perdu). <br><br>Dans ce scénario, Braze est l'employé de la poste et votre code de promotion est le coupon. Nous ne pouvons pas le récupérer une fois qu'il a été retiré de la pile des codes de promotion, quel que soit le résultat du webhook.
{% endalert %}

## Foire aux questions

### Quels canaux de communication puis-je utiliser avec les codes de promotion ?

Les codes de promotion sont actuellement pris en charge pour l'e-mail, les notifications push sur mobile, les notifications push Web, les cartes de contenu, le webhook, les SMS et WhatsApp. Les campagnes d'e-mails transactionnels de Braze et les messages in-app ne prennent actuellement pas en charge les codes de promotion.

### Les envois de test et d'initiateurs utiliseront-ils mes codes de promotion ?

Par défaut, les envois de tests et les envois d'e-mails de groupes initiateurs utiliseront des codes promotionnels par utilisateur, par envoi de tests. Cependant, vous pouvez contacter votre gestionnaire de compte Braze pour mettre à jour ce comportement afin de ne pas utiliser de codes de promotion pendant les tests.

### Comment les codes de promotion fonctionnent-ils dans le cadre d'une campagne multicanal ou d'une étape du canvas ?

Les codes de promotion sont déduits avant l'envoi du message. Si les canaux de communication de la campagne ou du Canvas envoient, cela peut entraîner l'utilisation du code de promotion pour des raisons telles que les heures calmes, les limites de débit, le plafonnement de la fréquence, les critères de sortie, etc. Toutefois, si l'un des canaux de communication est utilisé pour l’envoi, un seul code de promotion sera utilisé.

### Que se passe-t-il si j'ai plusieurs extraits de liquid qui font référence à la même liste de codes de promotion dans mon message ?

Le même code de promotion sera utilisé pour toutes les instances de l'extrait de code Liquid dans votre message.

### Que se passe-t-il lorsqu'une liste de codes de promotion est expirée ou vide ?



Si le message aurait dû contenir un code de promotion provenant d'une liste vide ou expirée, le message sera annulé. 

Si le message contient une logique conditionnelle d'insertion d'un code promotionnel, le message ne sera annulé que s'il aurait dû contenir un code promotionnel. Si le message n'aurait pas dû contenir de code de promotion, le message sera envoyé normalement.

### Comment enregistrer un code de promotion dans le profil d'un utilisateur afin de pouvoir l'utiliser dans des messages de suivi ?

Pour référencer le même code de promotion dans les messages suivants, le code doit être enregistré dans le profil de l'utilisateur en tant qu'attribut personnalisé. Pour ce faire, vous pouvez attacher un [webhook Braze à Braze à]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/) la même campagne ou à la même étape du message canvas.

[1]:{% image_buster /assets/img/promocodes/promocode1.png %}









