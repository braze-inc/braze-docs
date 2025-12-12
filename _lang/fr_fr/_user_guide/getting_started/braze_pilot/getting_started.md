---
nav_title: Pour commencer
article_title: Démarrer avec Braze Pilot
page_order: 2
page_type: reference
description: "Cet article de référence couvre brièvement les étapes d'intégration requises de la part de vos ingénieurs ou développeurs."
---

# Démarrer avec Braze Pilot

> Cet article explique comment commencer à utiliser Braze Pilot. Nous allons ici vous guider pour télécharger l'appli, initialiser la connexion avec votre tableau de bord de Braze et terminer la configuration.

## Étape 1 : Télécharger le pilote Braze

Pour commencer à utiliser Braze Pilot, vous devrez d'abord télécharger l'application à partir de l'Apple App Store ou de l'application Google Play Store. Vous pouvez rechercher l'application dans l'app store ou scanner les codes QR ci-dessous pour visiter la page de l'application pour votre appareil.

## Étape 2 : Accepter les termes et conditions

Ensuite, acceptez les conditions générales, puis saisissez votre e-mail professionnel dans le formulaire. Votre e-mail sera utilisé pour l'analyse/analytique de l'utilisation de l'application uniquement et ne sera pas utilisé à des fins de marketing.

!Page d'accueil du Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"}\![Possibilité d'entrer votre adresse e-mail professionnelle.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Étape 3 : Initialiser la connexion avec le SDK de Braze

Braze Pilot vous permet d'initialiser le SDK de Braze par rapport à n'importe quel tableau de bord de Braze. Une fois le SDK initialisé, Pilot commencera à envoyer des données d'engagement à Braze et vous permettra de déclencher tout envoi de messages lancé depuis ce tableau de bord Braze.

Il existe deux méthodes pour configurer la connexion SDK dans Pilot : Démonstration des codes QR et de l'assistant de configuration.

{% tabs local %}
{% tab Demo QR codes %}

### Méthode 1 : Démonstration de codes QR

Scannez un code QR qui comprend tous les détails nécessaires à l'initialisation du SDK, à la création de votre profil utilisateur et à l'établissement d'un lien profond avec une simulation d'appli particulière dans Braze Pilot. Les codes QR de démonstration sont affichés dans le tiroir d'accompagnement pour des campagnes de démonstration particulières dans votre essai gratuit.

| Pilote pour Android | Pilote pour iOS |
| --- | --- |
| \![Code QR pour Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | \![Code QR pour iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### Méthode 2 : Assistant de configuration

Suivez un guide étape par étape pour initialiser la connexion avec l'espace de travail de votre tableau de bord à partir de la page **Paramètres de l'application** dans votre tableau de bord Braze.

!Étape 1 de l'assistant de configuration pour Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Cette connexion est spécifique à l'espace de travail. Cela signifie que si vous initialisez la connexion à partir de l'espace de travail de démonstration et que vous passez ensuite à l'espace de travail en direct dans votre tableau de bord d'essai gratuit, vous devrez réinitialiser le SDK à partir de cet espace de travail pour recevoir toutes les campagnes qui y sont lancées.

Le menu déroulant de l'espace de travail dans le tableau de bord de Braze avec "Demo - Braze" sélectionné comme espace de travail actif.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Étape 4 : Autoriser les permissions push

Enfin, il est recommandé d'autoriser l'application à vous envoyer des autorisations de push si vous souhaitez tester les fonctionnalités de push via l'application. Vous pouvez donner ces autorisations à l'app de la manière suivante : en mettant à jour les paramètres de l'app dans les réglages de votre appareil, ou en lançant un message push primer de Braze vers l'app.

{% tabs local %}
{% tab Update the settings for the app %}

Ouvrez les emplacements de votre appareil et localisez Braze Pilot. Ensuite, mettez à jour les paramètres pour permettre aux notifications d'apparaître sur votre écran de verrouillage.

<style>
  .imgDiv {
      text-align: center;
    }
</style>

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/device_settings.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% tab Launch a push primer message %}

Vous pouvez utiliser un message in-app de Braze pour demander des autorisations de push pour l'application, comme vous le feriez pour vos propres consommateurs. Pour savoir comment créer ce type de message dans Braze, consultez la rubrique [Messages in-app de Push primer]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages#push-primer-in-app-messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Étape 5 : Expérience de l'envoi de messages par Braze dans Pilot

Vous êtes maintenant prêt à commencer à recevoir des campagnes et des canevas depuis votre tableau de bord de Braze en tant qu'utilisateur de Braze Pilot ! Visitez l'une des campagnes lancées dans votre espace de travail de démonstration pour une démonstration rapide des cas d'utilisation de Braze, puis rendez-vous dans votre espace de travail en direct pour commencer à envoyer les vôtres.

Pour en savoir plus sur la manière d'implémenter des campagnes et des toiles dans Braze, consultez [Getting Started : Campagnes et toiles]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases).