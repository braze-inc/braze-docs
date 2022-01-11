---
nav_title: Février
page_order: 11
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour février 2022."
---

# Février 2022

## Étape des chemins d'expérience de Canvas
La nouvelle Étape des chemins d'expérience de Canvas permet de suivre les performances des chemins en testant plusieurs chemins de Canvas les uns contre les autres et un groupe de contrôle à n'importe quel moment du parcours de l'utilisateur. Maintenant, vous pouvez tirer parti des analyses rassemblées ici pour déterminer quel chemin est le plus efficace. En savoir plus sur la façon de créer une [étape des chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).

## Gestion des numéros de téléphone non valides
Vous avez rencontré un scénario où un utilisateur a entré un numéro de téléphone invalide. Voici votre solution! Braze marque ces numéros de téléphone non valides et ne tentera pas d'envoyer d'autres communications à ces numéros. En savoir plus sur la façon dont Braze [gère les numéros de téléphone non valides]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers/).

### Nouveaux points de terminaison SMS
Vous pouvez maintenant gérer des numéros de téléphone non valides en utilisant le nouveau [Braze SMS Endpoints]({{site.baseurl}}/api/endpoints/sms/)! Fonctionnalités de cette mise à jour :
- [GET: Interrogation ou liste de numéros de téléphone non valides]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) renvoie une liste de numéros de téléphone qui sont considérés comme « invalides » par Brésil.
- [POST: Supprimer les numéros de téléphone non valides]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) vous permet de supprimer les numéros de téléphone « invalides » de la liste invalide de Brase.

## Limites de taux
Les limites de taux de l'API ont été incluses pour tous les [articles Braze Endpoint]({{site.baseurl}}/api/basics/#nav_top_endpoints). Vous pouvez maintenant facilement voir les limites de taux par type de requête. Pour plus d'informations sur les limites de taux, consultez notre article sur [les limites de taux API]({{site.baseurl}}/api/api_limits/).

## Nouveau point de terminaison REST
Braze a ajouté un [nouveau point d'extrémité REST EU-02]({{site.baseurl}}/api/basics/#api-definitions).

## À propos de l'e-mail
Les messages électroniques sont un excellent moyen de se connecter avec vos clients. Pour une brève introduction sur la façon dont vous pouvez personnaliser et tirer parti des messages électroniques, consultez notre nouvel article sur [À propos de l'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/).

## À propos des messages dans l'application
Les messages intégrés fournissent un contenu enrichi à vos utilisateurs actifs dans votre application. Vous pouvez facilement vous engager auprès de vos clients actifs en créant des messages dans l'application pour des messages de vœux personnalisés ou l'adoption de fonctionnalités. Pour en savoir plus sur les avantages et les types de messages, consultez notre nouvel article sur [À propos des messages dans l'application]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/).