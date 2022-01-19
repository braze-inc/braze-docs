---
nav_title: Comportements d'avancement
article_title: Comportements d'avancement
page_order: 3
alias: /fr/auto_advance/
page_type: Référence
description: "Cet article de référence décrit le comportement avancement de Braze et couvre divers scénarios qui peuvent se produire à mesure que vous progressez dans une Canvas."
tool: Toile
---

# Faire progresser vos utilisateurs à travers les étapes de Canvas

La fonction de comportement avancement de Braze vous permet de choisir les critères de progression à travers votre étape de Canvas .

!\[auto2.png\]\[1\]

## Avancer lorsque le message est envoyé

Lorsque **Message Envoyé** est sélectionné, les clients ne seront avancés que lors des étapes suivantes de Canvas lorsque l'une des conditions suivantes se produira :

- Un e-mail a été envoyé
- Un message push est envoyé
- Un webhook est envoyé
- Un message dans l'application est affiché
- Une carte de contenu est envoyée

## Avancer immédiatement le public

Lorsque __Immédiatement Advance Audience__ est sélectionné, les clients seront avancés aux étapes suivantes de Canvas lorsque l'une des conditions suivantes se produira :

- Tout message est envoyé ou le message dans l'application à l'étape devient en direct
- Le webhook n'est pas envoyé parce que le webhook provoque une erreur ou des erreurs
- Un push ou un email n'est pas envoyé car l'utilisateur n'est pas joignable par push ou email
- L'envoi de la carte de contenu est tenté
- Une carte est abandonnée et n'a pas été envoyée
- Un message n'est pas envoyé car il est limité à la fréquence
- Un message n'est pas envoyé car il est abandonné

{% alert important %}
Les utilisateurs doivent satisfaire aux critères de l'étape pour pouvoir passer à l'étape suivante.
{% endalert %}

### Étapes planifiées

Pour une étape planifiée, les utilisateurs doivent rencontrer les options du public pour l'étape afin d'être avancé à travers l'étape. Si l'étape a un [événement d'exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/), les utilisateurs qui effectuent l'événement d'exception ne seront pas avancés à travers l'étape.

Lors de l'envoi d'une étape multi-canal avec le [timing intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/), nous pouvons envoyer ou tenter d'envoyer des messages à des moments différents pour différents canaux. Braze fera avancer automatiquement les utilisateurs au moment où le premier message dans une étape tente d'envoyer.

### Étapes basées sur l'action

Pour les étapes basées sur l'action, les utilisateurs doivent effectuer l'action de déclenchement et répondre aux options du public afin de pouvoir passer à l'étape suivante. Si l'étape a un événement d'exception, les utilisateurs qui effectuent l'événement d'exception ne seront pas avancés à travers l'étape.

{% alert important %}
  Les clients qui passent par une étape sans recevoir de messages ne seront pas considérés comme un destinataire unique pour cette étape. Les utilisateurs doivent recevoir un ou plusieurs messages d'une étape pour être comptés comme un destinataire unique.
{% endalert %}

## Utilisation de l'avancement de Canvas

L'avancement fonctionne bien lorsque la messagerie suivante se rapporte aux messages précédents. Par exemple, vous ne voudriez pas envoyer de push de suivi à propos d'un e-mail qui n'a jamais été envoyé aux utilisateurs.

Il arrive parfois que vous vouliez que les utilisateurs continuent à progresser à travers un Canvas même s'ils ne reçoivent pas un certain message. Par exemple, vous pourriez avoir un message "Bienvenue" le jour 3 et un courriel "Bienvenue" le jour 6. Certains de vos utilisateurs peuvent ne pas être joignables via les notifications push, car tout le monde n'accepte pas de recevoir des messages push. Vous pouvez envoyer l'e-mail du jour 6 à tous les utilisateurs, même s'ils n'ont pas été envoyés le push Day 3.

Dans ce scénario, vous pouvez utiliser les options de comportement d'avancement de Braze pour vous assurer que les utilisateurs poursuivent sur le Canvas, même s'ils ne sont pas envoyés la Push Jour 3.

Si vous voulez que tous les utilisateurs reçoivent l'email du jour 6, même s'ils n'ont pas reçu le push Day 3, vous pouvez définir le **comportement d'avancement** à __Audience immédiatement Avancée__  pour la poussée du jour 3.

Lorsque vous sélectionnez __immédiatement le comportement d'avancement de l'audience__ pour la poussée du jour 3, les utilisateurs avanceront lorsque Braze tente d'envoyer le push. Les utilisateurs qui correspondent aux options du public et qui ne sont pas accessibles par push ne seront pas envoyés par push, mais seront de toute façon avancés.

{% details Previous Canvas Advancement Behavior %}

Avant la publication de Advancement Behavior, les utilisateurs avancés de Braze à travers une étape de Canvas une fois qu'ils avaient reçu un message de cette étape. Par exemple, si une étape de Canvas inclut un courriel et un push, les utilisateurs ne passeront pas aux étapes suivantes de la Canvas jusqu'à:

- Braze a envoyé à l'utilisateur l'e-mail, ou
- Braze a envoyé à l'utilisateur le push.

Si l'utilisateur n'a pas envoyé le courriel ou la push, il ne passerait pas aux étapes suivantes dans le Canvas.

Les clients qui n'ont pas participé à la première partie de la bêta de message de Canvas dans l'application verront l'option "Message Envoyé" du comportement d'avancement appliquée à toutes les étapes de Canvas créées avant le 30 juillet, 2019. Avant la publication de l'avancement des comportements, des avancements des utilisateurs se sont produits lorsque des messages ont été envoyés à partir des étapes de Canvas .

Les clients qui ont participé à la première partie de la bêta de message dans l'application de Canvas verront l'option "Message Envoyé" du comportement de l'avancement appliquée à toutes les étapes de Canvas sans que les messages intégrés à l'application aient été créés avant le 30 juillet, 2019 et "Avance Public After Delay" appliqués à toutes les étapes de Canvas avec des messages intégrés créés avant le 30 juillet 2019. Avant la publication du comportement d'avancement, l'avancement de l'utilisateur s'est produit lorsque les messages de Canvas dans l'application sont devenus en direct.

{% enddetails %}
[1]: {% image_buster /assets/img/push-advancement-behavior.png %} "Comportement avancé"
