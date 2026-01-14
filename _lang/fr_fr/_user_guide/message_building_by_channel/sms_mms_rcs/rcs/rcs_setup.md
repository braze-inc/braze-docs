---
nav_title: "Configuration du RCS"
article_title: Configuration du RCS
page_order: 1
alias: /rcs_setup/
description: "Cet article de référence couvre les conditions requises pour mettre en place et faire fonctionner RCS."
page_type: reference
channel:
  - RCS
---

# Mise en place du RCS

> Cet article couvre les conditions requises pour que votre canal RCS soit opérationnel.

L'installation du RCS est aussi simple que celle du SMS. Poursuivez votre lecture pour découvrir comment vous pouvez commencer à envoyer des messages riches et interactifs.

## Étape 1 : Remplir les critères d'éligibilité

Pour être éligible à l'envoi de RCS avec Braze, votre entreprise doit répondre à trois critères en amont :

1. Votre contrat Braze Currents actuel doit inclure les crédits de message. 
2. Vous devez envoyer vos messages RCS à l'un des pays suivants pris en charge par Braze :
- États-Unis
- Royaume-Uni
- Allemagne
- Mexique
- Suède
- Espagne
- Singapour
- Brésil
- France
- Italie
- Colombie
3. Vous devez vous procurer une ou plusieurs unités de gestion des stocks à 0 $ dans votre contrat.

## Étape 2 : Enregistrer un expéditeur vérifié par RCS

Avant de pouvoir envoyer des messages RCS, vous devez vous enregistrer en tant qu'expéditeur vérifié RCS. Il s'agit de la représentation de votre marque que les utilisateurs verront sur leurs appareils mobiles, qui comprend le nom de votre marque, son logo, un badge de vérification et un slogan facultatif. L'expéditeur vérifié par le RCS renforce la confiance des clients et confirme que vos messages proviennent d'une source authentifiée. 

\![Un exemple d'expéditeur vérifié par RCS dans un message RCS intitulé "Cat Failz Cafe".]({% image_buster /assets/img/rcs/rcs_sender.png %}){: style="max-width:60%;"}

Après avoir ajouté la ou les unités de gestion des stocks à votre formulaire de commande, Braze en sera informé et vous contactera pour vous communiquer les informations relatives à l'enregistrement de l'expéditeur RCS. Leur format dépend des pays auxquels vous souhaitez envoyer des messages RCS. 

Une fois que vous aurez envoyé vos formulaires remplis à Braze, nous effectuerons la procédure d'enregistrement en votre nom. 

### Étape 2.1 : Mettre en place des fallbacks SMS pour les groupes d'abonnement RCS

Parce que la couverture actuelle des opérateurs varie selon les pays, et que le matériel et le logiciel de l'utilisateur varient selon les individus, la solution de repli par SMS est un élément clé de la réussite d'un programme RCS aujourd'hui. Nous vous recommandons de mettre en place une solution de repli par SMS. Si un opérateur ne prend pas en charge le RCS ou si l'appareil d'un utilisateur n'est pas en mesure de recevoir des messages RCS, la solution de repli SMS enverra votre message malgré tout, afin que vous ne manquiez jamais un moment important avec vos utilisateurs.

Nous vous recommandons vivement d'examiner votre expérience actuelle d'abonnement par SMS, vos groupes d'abonnement et la segmentation de votre audience avant de déployer votre première campagne RCS. Si nécessaire, votre gestionnaire de satisfaction client est toujours disponible pour vous guider et vous aider à naviguer dans le processus de configuration.

### Calendrier pour l'approbation du transporteur

Le délai d'approbation du transporteur varie d'un pays à l'autre et peut également varier au sein d'un même pays. Gardez à l'esprit que le marché RCS en est encore à ses balbutiements, de sorte que les processus des opérateurs et des agrégateurs évoluent rapidement. Aux États-Unis, Braze estime que le délai d'approbation des transporteurs pour un expéditeur vérifié par le RCS est généralement compris entre 4 et 6 semaines, et qu'un expéditeur test est généralement approuvé en une semaine.

Lorsque votre expéditeur vérifié par RCS est approuvé, notre équipe opérationnelle mettra à jour vos groupes d'abonnement si nécessaire pour confirmer qu'ils contiennent l'expéditeur RCS. 

## Étape 3 : Créer des groupes d'abonnement

Le RCS est généralement utilisé de deux manières : 
- Améliorer le trafic SMS existant 
- Permettre de nouveaux cas d'utilisation qui ne sont possibles qu'avec les fonctionnalités plus riches fournies par le RCS

En fonction de votre intégration, Braze peut ajouter des expéditeurs vérifiés par RCS à vos groupes d'abonnement SMS existants ou créer de nouveaux groupes d'abonnement pour vous. Dans les deux cas, votre équipe Braze vous guidera dans la mise à niveau du trafic SMS de façon fluide/sans façon homogène, etc. Pour plus d'informations, reportez-vous à la section [Groupes d'abonnement SMS et RCS.]({{site.baseurl}}/sms_rcs_subscription_groups/)

Pour les nouveaux cas d'utilisation qui ne sont pas possibles avec les SMS, envisagez de mettre en place des groupes d'abonnement RCS dédiés pour s'aligner sur les objectifs de votre programme.