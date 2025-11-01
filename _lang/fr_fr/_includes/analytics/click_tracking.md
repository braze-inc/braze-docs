{% if include.section == "UTM parameters" %}

Si le raccourcissement des liens vous permet de suivre vos URL automatiquement, vous pouvez également ajouter des paramètres UTM à vos URL pour suivre les performances des campagnes dans des outils d'analyse/analytique tiers, tels que Google Analytics.

Pour ajouter des paramètres UTM à votre URL, procédez comme suit :

1. Commencez par votre URL de base. Il s'agit de l'URL de la page que vous souhaitez suivre (par exemple `https://www.example.com`).
2. Ajoutez un point d'interrogation ( ?) après votre URL de base.
3. Ajoutez chaque paramètre UTM séparé par une esperluette (&).

Un exemple est `https://www.example.com?utm_source=newsletter&utm_medium=sms`.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Foire aux questions

### Les liens que je reçois lors des tests sont-ils de vraies URL ?

Si la campagne a été enregistrée en tant que brouillon avant l'envoi du test, oui. Sinon, il s’agit d’une marque substitutive d’URL. Notez que l'URL exacte envoyée lors d'une campagne lancée peut différer de celle envoyée lors d'un envoi test.

### Est-il possible d’ajouter des paramètres UTM à une URL avant qu’elle ne devienne courte ?

Oui. Des paramètres statiques et dynamiques peuvent être ajoutés. 

### Combien de temps les URL raccourcies restent-elles valides ?

Les URL personnalisées sont valables deux mois à compter de la date d'enregistrement de l'URL.

### Le SDK Braze doit-il être installé pour raccourcir des liens ?

Non. Le raccourcissement des liens fonctionne sans aucune intégration SDK.

{% endif %}

{% if include.section == "Custom Domains" %}

## Domaines personnalisés

Le raccourcissement de lien vous permet également d’utiliser votre propre domaine pour personnaliser l’apparence de vos URL raccourcies et présenter une image de marque cohérente. Pour plus d'informations, reportez-vous à la section [Domaines personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/).

{% endif %}