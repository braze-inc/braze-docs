---
nav_title: "Envoi de message SMS"
article_title: Aperçu Envoi message SMS
page_order: 4
description: "Le présent article de référence couvre les bases et les meilleures pratiques de l’envoi par SMS."
page_type: reference
channel:
  - SMS
  
---

# Envoi de message SMS

## Principes de base d’envoi de SMS

L’envoi de message peut être compliqué, mais il n’a pas à être. Les sections suivantes répertorient les principes fondamentaux de l’envoi de message SMS envoyé chez Braze, notamment l’importance des groupes d’abonnement, les exigences pour les segments SMS et les corps de message, ainsi que des options de personnalisation avancées disponibles.

1. **Sélectionnez votre groupe d’abonnement**<br>
Les SMS doivent être envoyés à partir d’un [groupe d’abonnement]({{site.baseurl}}/user_guide/onboarding_with_braze/sms_setup/sms_subscription_groups/). Un groupe d’abonnement est une collection de numéros de téléphone émetteurs (c.-à-d. codes courts, codes longs et/ou identifiants alphanumériques d’émetteurs) qui sont utilisés pour envoyer un type spécifique de message. Vous devez désigner un groupe d’abonnement pour vous assurer que seuls les utilisateurs abonnés sont ciblés. Certains clients peuvent envisager d’avoir plusieurs groupes d’abonnement pour différents cas d’utilisation, tels que la messagerie SMS transactionnelle et la messagerie SMS promotionnelle.<br><br>

2. **Saisir le corps du message**<br>
Un corps de message SMS accepte jusqu’à 1 600 caractères, y compris Emojis, Liquid et Contenu connecté. Un envoi de campagne unique peut entraîner des envois de nombreux segments de messages. Les corps de message SMS de Braze peuvent être composés de normes d’encodage [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) ou [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set). Dans le cas où un caractère UCS-2 (par exemple, un Emoji) est utilisé, le corps du message sera automatiquement formaté pour cette norme d’encodage.<br><br> 

3. **Comprendre les segments de message et les limites de caractère**<br>
Les segments de messages SMS sont la manière dont les messages de l’industrie SMS sont envoyés. Un segment de message est un groupement allant jusqu’à un nombre défini de caractères (160 pour le codage GSM-7 ; 67 pour le codage UCS-2) qui sera envoyé dans une seule distribution par SMS. Si vous envoyez un SMS avec 161 caractères à l’aide du codage GSM-7, vous verrez qu’il y a deux (2) segments de messages envoyés. L’envoi de plusieurs segments de messages peut entraîner des frais supplémentaires.<br><br>

4. **Personnalisation du mot-clé (facultatif)**<br>
Les réglementations exigent qu’il y ait des réponses à toutes les questions sur l’abonnement, le désabonnement, l’aide/réponses par mot-clé SMS d'information. Avec Braze, vous pouvez définir vos propres mots-clés pour déclencher des réponses d’abonnement, de désabonnement et d’aide, gérer vos propres réponses qui sont envoyées aux utilisateurs et définir des jeux de mots-clés pour différentes langues. Pour en savoir plus, consultez notre collection [Traitement des mots-clés]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/).

{% alert tip %}
Vous souhaitez apprendre à créer une campagne SMS ? Consultez notre guide étape par étape [Créer une campagne SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/create/).
{% endalert %}

## Meilleures pratiques d’envoi

### Envoi de SMS dans plusieurs pays

Certaines marques peuvent souhaiter envoyer des messages à un groupe d’utilisateurs qui ont des numéros de téléphone de différents pays. Afin d’envoyer un SMS à un numéro de téléphone dans un pays particulier, la bonne pratique est d’utiliser un code long ou un code court provenant du même pays. En fait, les codes courts peuvent uniquement envoyer des SMS aux numéros de téléphone du pays où le code court a été créé. 

Pour surmonter cette limitation, pendant le [processus de configuration][5] des groupes d’abonnement, les groupes peuvent être configurés pour contenir des codes longs et courts de plusieurs pays différents. Après cela, l’envoi des numéros de téléphone avec le même code pays que le numéro de téléphone de l’utilisateur cible sera automatiquement utilisé lors du lancement d’une campagne. Vous n’aurez pas à créer de campagnes distinctes pour les utilisateurs ayant des numéros de téléphone avec des codes pays différents, ce qui vous permet de lancer une campagne ou d’utiliser un composant de Canvas pour cibler les utilisateurs concernés.

![Les charges utiles SMS sont envoyées en utilisant le même code pays que le numéro de téléphone de l’utilisateur cible][2]

#### Bonnes pratiques

1. **Demandez la permission**. L’une des règles les plus importantes de l’utilisation de SMS par une entreprise est que vous devez d’abord obtenir la permission des clients pour les contacter. Ne pas le faire peut endommager votre marque et entraîner des frais de justice élevés.<br><br>
2. **Choisissez le bon numéro pour votre cas d’utilisation**. Trois principaux types de numéros de téléphone peuvent envoyer et recevoir des SMS : les codes longs, les codes courts et les ID alphanumériques d’émetteur, ainsi que leurs capacités et disponibilités dans différentes régions. Demandez-vous à l’avance si votre activité est mieux servie avec un code personnalisé. <br><br>
3. **Faites attention au timing**. Gardez à l’esprit que les clients sont plus réactifs aux textes qui leur sont adressés directement. Une petite personnalisation a beaucoup d’effet, comme utiliser le prénom des destinataires ou ajouter une touche de conversation qui évoque les centres d’intérêt de vos clients.<br><br>
4. **Engager des conversations bilatérales**. SMS est un canal tellement efficace pour parler avec les clients qu’il est important d’anticiper - et de gérer - efficacement les réponses à vos messages. 85 % des consommateurs veulent non seulement recevoir des informations, mais aussi répondre aux entreprises ou participer à une conversation.<br><br>
5. **Mesurer ce qui fonctionne**. Atteignez-vous les clients au bon moment, avec la meilleure fréquence et en utilisant les appels à l’action les plus efficaces ? Utiliser les bons outils de suivi peut apporter des indicateurs directs et mesurables qui prouvent leur retour sur investissement. 

### Envoi en grand volume

Prévoyez-vous un envoi en grand volume ? Nous avons des bonnes pratiques pour vous assurer que cela fonctionne bien :

- Ajustez les limites de débit de livraison pour votre campagne/Canvas si nécessaire, en fonction de la taille cible du public. Cela garantira que vous atteignez le volume d'envoi dont vous avez besoin et que Braze envoie les messages au débit que Twilio attend et peut gérer.
- Assurez-vous de respecter la limite de 160 caractères et faites attention au double comptage des caractères spéciaux (par exemple, les barres obliques, `\`les carets `^`et les tildes `~`). 

[2]: {% image_buster /assets/img/sms/multi_country_subgroups.png %}
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
