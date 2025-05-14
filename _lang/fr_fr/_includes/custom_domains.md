# Domaines personnalisés

> Cette page explique comment utiliser des domaines personnalisés pour donner une image de marque cohérente. 

{% alert note %}
Contactez votre gestionnaire de compte Braze pour commencer à utiliser des domaines personnalisés.
{% endalert %}

## Exigences du domaine

- Les domaines doivent être achetés, détenus et gérés par vous.
- Le domaine utilisé pour cette fonctionnalité doit être unique (c'est-à-dire différent du domaine de votre site Web) et il ne peut pas être utilisé pour héberger du contenu Web.
  - Vous pouvez également utiliser des sous-domaines uniques, tels que `sms.braze.com` ou `whatsapp.braze.com`.

### Déléguer votre domaine personnalisé

Lorsque vous déléguez votre domaine à Braze, nous nous chargeons automatiquement du renouvellement du certificat afin d'éviter toute interruption de service. 

Pour déléguer votre domaine à Braze, procédez comme suit : 

1. Présentez à votre gestionnaire de la satisfaction client un domaine qui répond aux exigences susmentionnées. Braze vérifie alors la configuration DNS existante pour le domaine et s’assure que :

- Il n'existe pas d’enregistrements CAA OU
- Des enregistrements CAA **existent** mais ont un enregistrement pour {% raw %}`<any number> issue "letsencrypt.org"`{% endraw %} ou {% raw %}`<anynumber> issuewild "letsencrypt.org"`{% endraw %}

{:start="2"}
2\. Créez quatre nouveaux enregistrements A, un pour chaque adresse IP, et vérifiez qu'il s'agit des seuls enregistrements A qui existent pour l'hôte du lien de domaine :
- `151.101.130.133`
- `151.101.194.133`
- `151.101.2.133`
- `151.101.66.133`

## Utilisation de domaines personnalisés

Une fois configurés, les domaines personnalisés peuvent être affectés à un ou plusieurs groupes d'abonnement WhatsApp et SMS. 

![Paramètres des groupes d’abonnement vous permettant de sélectionner un domaine de raccourcissement de lien.][7]

{% if include.channel == 'WhatsApp' %}
Les campagnes envoyées avec le suivi des clics activé ou créées dans les modèles de messages WhatsApp utiliseront le domaine attribué associé à vos groupes d'abonnement.

![Aperçu du compositeur de messages WhatsApp avec un domaine de lien raccourci qui est différent du domaine dans la boîte "Message".][6]
{% endif %}

{% if include.channel == 'SMS' %}
Les campagnes envoyées avec le raccourcissement de lien activé utiliseront le domaine attribué associé à votre groupe d'abonnement SMS.

![Aperçu du compositeur de messages SMS avec un domaine de lien raccourci qui est différent du domaine dans la boîte "Message".][8]
{% endif %}

## Foire aux questions

### Les domaines délégués peuvent-ils être partagés entre plusieurs groupes d’abonnement ?

Oui. Un seul domaine peut être utilisé avec plusieurs groupes d'abonnement. Pour ce faire, sélectionnez le domaine de chaque groupe d’abonnement auquel il doit être associé.

### Les domaines délégués peuvent-ils être partagés entre plusieurs espaces de travail ?

Oui. Les domaines peuvent être associés à des groupes d'abonnement dans plusieurs espaces de travail, à condition que les espaces de travail soient situés dans la même entreprise.

[6]: {% image_buster /assets/img/custom_domain_whatsapp_composer.png %}
[7]: {% image_buster /assets/img/custom_domain.png %}
[8]: {% image_buster /assets/img/custom_domain2.png %}