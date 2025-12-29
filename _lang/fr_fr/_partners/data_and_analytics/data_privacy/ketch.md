---
title: Ketch
nav_title: Ketch
description: "Cet article de référence est consacré à l'intégration de Braze et de Ketch. Ketch permet de simplifier les opérations de confidentialité et d'assurer un contrôle complet et dynamique des données, ainsi que des informations qui en sont extraites."
alias: /partners/ketch
page_type: partner
search_tag: Ketch
---

# Ketch

> [Ketch](https://www.ketch.com) permet aux entreprises d'être des gestionnaires responsables de leurs données. Ketch permet de simplifier les opérations de confidentialité et d'assurer un contrôle et un traitement complet et dynamique des données. 

_Cette intégration est maintenue par Ketch._

## À propos de l'intégration

L'intégration de Braze et Ketch vous permet de contrôler les préférences de communication des clients dans le centre de préférences de Ketch et de propager automatiquement ces changements dans Braze. 

{% alert note %}
Vous souhaitez obtenir des conseils sur la création de groupes d'abonnement ? Consultez nos articles sur les <a href='/docs/user_guide/message_building_by_channel/sms/sms_subscription_group/'>groupes d'abonnement SMS</a> et les <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/'>groupes d'abonnement e-mail</a>.
{% endalert %}

## Conditions préalables

| Exigences | Description |
|---|---|
| Compte Ketch | Un compte [Ketch](https://www.ketch.com) avec des privilèges d'administrateur est nécessaire pour activer cette intégration. |
| Clé API de Braze | Une clé API REST de Braze avec les autorisations `users.track`, `subscription.status.get`, `subscription.status.set`, `users.delete`, `users.alias.new`, `users.export.ids`, `email.unsubscribe` et `email.blacklist`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze**(Console de développement** > **Clé API REST ** > **Créer une nouvelle clé API**). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Établir la connexion Braze

1. Dans votre [instance Ketch](https://app.ketch.com), naviguez vers **Data Systems**, et sélectionnez **Braze**. Cliquez ensuite sur **Nouvelle connexion**.
2. Donnez à votre connexion Braze un nom identifiable, qui sera utilisé pour faire référence à cette connexion dans les processus basés sur l'API. Notez qu'un code sera également créé pour cette connexion. Ce code doit être unique pour toutes les connexions.
3. Confirmez le mappage de l'identité de vos utilisateurs. Par défaut, Ketch mappera les identités des utilisateurs en fonction de leur adresse e-mail ou de leur adresse `external_id` dans Braze.
4. Ajoutez la clé API de Braze et indiquez l'endpoint de l'API. Notez que cet [endpoint API]({{site.baseurl}}/api/basics/#endpoints) dépend de l'instance de Braze utilisée par votre organisation.

### Étape 2 : Configurer les préférences d'abonnement

1. Allez dans **Centre des politiques > Abonnements**. Si vous ne voyez pas l'onglet des abonnements sous **Policy Center**, assurez-vous que vous avez accès au centre de préférences marketing et vérifiez que vous disposez des autorisations de compte correctes pour accéder à cette partie du produit.
2. Cliquez sur **Créer un nouvel abonnement** pour créer une nouvelle rubrique. Chaque abonnement aura un nom et un code.
3. Ajoutez les canaux pour l'envoi de vos sujets d'abonnement. Chaque canal s'affichera dans le centre de préférences marketing de vos utilisateurs. Vous pouvez également ajouter les détails de la manière dont vous souhaitez que le centre de préférences Ketch orchestre un signal d'abonnement ou de désabonnement particulier.
4. Sélectionnez la connexion Braze que vous souhaitez utiliser pour orchestrer les signaux d'abonnement et de retrait.
5. Saisissez le `subscription_group_id` de Braze pour le groupe d'abonnement auquel vous souhaitez envoyer les préférences utilisateur de Ketch.

![Braze Subscription groups ID.]({% image_buster /assets/img/ketch/ketch1.png %})

{% alert note %}
Afin de collecter et d'orchestrer les signaux d'abonnement et de désabonnement des utilisateurs, les identités doivent être correctement configurées. Ketch recommande de configurer l'e-mail comme identifiant pour orchestrer les signaux de préférence des utilisateurs pour cette intégration.
{% endalert %}


### Étape 3 : Configurer les identités

Un utilisateur ne peut voir le centre de préférences marketing que lorsque Ketch peut confirmer l'identité de cet utilisateur en matière de préférences marketing. Si Ketch ne peut pas saisir correctement l'identité de l'utilisateur, la page des préférences marketing ne s'affichera pas pour cet utilisateur, car Ketch ne pourra pas gérer ses préférences.

1. Pour configurer l'identité des préférences marketing, accédez à la page **Paramètres** dans Ketch, puis cliquez sur **Espace d'identité.** Vous devrez soit créer un nouvel espace d'identité, soit modifier un espace d'identité existant pour assigner cet espace d'identité comme identité de préférence marketing. Vérifiez que l'étiquette Ketch déployée sur la propriété capture correctement cet espace d'identité.
2. Allez dans **Experience Server** > **Propriétés**, et modifiez la propriété souhaitée. Sous la couche de données de cette propriété, veillez à activer l'espace d'identité personnalisé. Ensuite, configurez la manière dont l'identité du marketeur est capturée sur ce site.
3. Une fois l'espace d'identité configuré, vérifiez si le centre de préférences apparaît en ouvrant le centre de préférences sur le site web où l'étiquette Ketch a été déployée.


