---
nav_title: "Envoi SMS dans plusieurs pays"
article_title: Envoi SMS dans plusieurs pays
page_order: 3
description: "Le présent article de référence couvre les bonnes pratiques d’envoi dans plusieurs pays pour la messagerie SMS."
page_type: reference
channel:
  - SMS
  
---

# Envoi de SMS dans plusieurs pays

> Certaines marques peuvent souhaiter envoyer des messages à un groupe d’utilisateurs qui ont des numéros de téléphone de différents pays. Afin d’envoyer un SMS à un numéro de téléphone dans un pays particulier, la bonne pratique est d’utiliser un code long ou un code court provenant du même pays. En fait, les codes courts peuvent uniquement envoyer des SMS aux numéros de téléphone du pays où le code court a été créé.

Pour surmonter cette limitation, pendant le [processus de configuration][5] des groupes d’abonnement, les groupes peuvent être configurés pour contenir des codes longs et courts de plusieurs pays différents. Après cela, l’envoi des numéros de téléphone avec le même code pays que le numéro de téléphone de l’utilisateur cible sera automatiquement utilisé lors du lancement d’une campagne. 

Vous n’aurez pas à créer de campagnes distinctes pour les utilisateurs ayant des numéros de téléphone avec des codes pays différents, ce qui vous permet de lancer une campagne ou d’utiliser un composant de Canvas pour cibler les utilisateurs concernés.

![][2]

## Bonnes pratiques

1. **Demandez la permission**. L’une des règles les plus importantes de l’utilisation de SMS par une entreprise est que vous devez d’abord obtenir la permission des clients pour les contacter. Ne pas le faire peut endommager votre marque et entraîner des frais de justice élevés.<br><br>
2. **Choisissez le bon numéro pour votre cas d’utilisation**. Trois principaux types de numéros de téléphone peuvent envoyer et recevoir des SMS : les codes longs, les codes courts et les ID alphanumériques d’émetteur, ainsi que leurs capacités et disponibilités dans différentes régions. Demandez-vous à l’avance si votre activité est mieux servie avec un code personnalisé. <br><br>
3. **Faites attention au timing**. Gardez à l’esprit que les clients sont plus réactifs aux textes qui leur sont adressés directement. Une petite personnalisation a beaucoup d’effet, comme utiliser le prénom des destinataires ou ajouter une touche de conversation qui évoque les centres d’intérêt de vos clients.<br><br>
4. **Engager des conversations bilatérales**. SMS est un canal tellement efficace pour parler avec les clients qu’il est important d’anticiper - et de gérer - efficacement les réponses à vos messages. 85 % des consommateurs veulent non seulement recevoir des informations, mais aussi répondre aux entreprises ou participer à une conversation.<br><br>
5. **Mesurer ce qui fonctionne**. Atteignez-vous les clients au bon moment, avec la meilleure fréquence et en utilisant les appels à l’action les plus efficaces ? Utiliser les bons outils de suivi peut apporter des indicateurs directs et mesurables qui prouvent leur retour sur investissement. 

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/
[2]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process