---
nav_title: Commencer
article_title: Commencer avec Braze Pilot
page_order: 2
page_type: reference
description: "Le présent article de référence couvre brièvement les étapes d’intégration dont vos ingénieurs ou développeurs ont besoin."
---

# Commencez avec Braze Pilot

> Cet article explique comment débuter avec Braze Pilot. Nous vous guiderons ici tout au long du processus de téléchargement de l'application, d'initialisation de la connexion avec votre tableau de bord de Braze et de finalisation de la configuration.

## Étape 1 : Télécharger le pilote Braze

Pour commencer à utiliser Braze Pilot, veuillez d'abord télécharger l'application depuis l'App Store d'Apple ou le Google Play Store. Vous pouvez rechercher l'application dans l'App Store ou scanner les codes QR ci-dessous pour accéder à la page de l'application pour votre appareil.

## Étape 2 : Veuillez accepter les conditions générales.

Veuillez ensuite accepter les conditions générales, puis saisir votre e-mail professionnel dans le formulaire. Votre e-mail sera utilisé uniquement à des fins d'analyse de l'utilisation de l'application et ne sera pas utilisé à des fins marketing.

![Page d'accueil de Braze Pilot.]({% image_buster /assets/img/braze_pilot/pilot_welcome.png %}){:style="max-width:30%"} ![Possibilité de saisir votre adresse e-mail professionnelle.]({% image_buster /assets/img/braze_pilot/pilot_signin.png %}){:style="max-width:30%"}

## Étape 3 : Veuillez initialiser la connexion avec le SDK Braze.

Braze Pilot vous permet d'initialiser le SDK Braze sur n'importe quel tableau de bord de Braze. Une fois le SDK initialisé, Pilot commencera à envoyer des données d'engagement à Braze et vous permettra de déclencher l'envoi de messages à partir du tableau de bord de Braze.

Il existe deux méthodes pour configurer la connexion SDK dans Pilot : Codes QR de démonstration et assistant de configuration.

{% tabs local %}
{% tab Demo QR codes %}

### Méthode 1 : Codes QR de démonstration

Veuillez scanner le code QR qui contient toutes les informations nécessaires pour initialiser le SDK, créer votre profil utilisateur et vous rediriger vers une simulation d'application spécifique dans Braze Pilot. Les codes QR de démonstration sont affichés dans le tiroir associé pour certaines campagnes de démonstration dans le cadre de votre essai gratuit.

| Pilote pour Android | Pilote pour iOS |
| --- | --- |
| ![Code QR pour Android.]({% image_buster /assets/img/braze_pilot/android_qr_code.png %}){:style="max-width:60%"} | ![Code QR pour iOS.]({% image_buster /assets/img/braze_pilot/ios_qr_code.png %}){:style="max-width:60%"} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Setup wizard %}

### Méthode 2 : Assistant de configuration de la configuration

Veuillez suivre le guide étape par étape pour initialiser la connexion avec votre espace de travail depuis la page **Paramètres de l'application** dans votre tableau de bord de Braze.

![Étape 1 de l'assistant de configuration de Braze Pilot.]({% image_buster /assets/img/braze_pilot/setup_wizard.png %}){:style="max-width:40%"}

Cette connexion est spécifique à l'espace de travail. Cela signifie que si vous initialisez la connexion à partir de l'espace de travail de démonstration, puis passez à l'espace de travail en ligne/en production/instantané dans votre tableau de bord d'essai gratuit, vous devrez réinitialiser le SDK à partir de cet espace de travail pour recevoir les campagnes qui y sont lancées.

![Le menu déroulant de l'espace de travail dans le tableau de bord de Braze avec « Démo - Braze » sélectionné comme espace de travail actif.]({% image_buster /assets/img/braze_pilot/dashboard_workspace.png %}){:style="max-width:60%"}

{% endtab %}
{% endtabs %}

## Étape 4 : Autoriser les autorisations push

Enfin, il est recommandé d'autoriser l'application à vous envoyer des notifications push si vous souhaitez tester les fonctionnalités push via l'application. Vous pouvez accorder ces autorisations à l'application de différentes manières : en mettant à jour les paramètres de l'application dans les paramètres de votre appareil ou en envoyant un message push depuis Braze vers l'application.

{% tabs local %}
{% tab Update the settings for the app %}

Veuillez ouvrir les paramètres de votre appareil et déterminer l'emplacement de Braze Pilot. Veuillez ensuite mettre à jour les paramètres afin d'autoriser l'affichage des notifications sur votre écran de verrouillage.

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

Vous pouvez utiliser un message in-app de Braze pour demander des autorisations push pour l'application, comme vous le feriez pour vos propres consommateurs. Pour découvrir comment créer ce type de message dans Braze, veuillez consulter [le guide d'introduction aux messages in-app dans l'application]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages#push-primer-in-app-messages).

<div class="imgDiv">
<img src="{% image_buster /assets/img/braze_pilot/push_primer1.png %}" style="max-width:40%">
</div>
<br>

{% endtab %}
{% endtabs %}

## Étape 5 : Découvrez l'envoi de messages Braze dans Pilot

Vous êtes désormais prêt à recevoir des campagnes et des canevas depuis votre tableau de bord de Braze en tant qu'utilisateur de Braze Pilot. Veuillez consulter l'une des campagnes lancées dans votre espace de travail de démonstration pour obtenir une démonstration rapide des cas d'utilisation de Braze, puis rendez-vous dans votre espace de travail en ligne/en production/instantané pour commencer à envoyer vos propres campagnes.

Pour plus d'informations sur l'implémentation des campagnes et des canevas dans Braze, veuillez consulter la section[ « Pour commencer » : Campagnes et toiles]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases).