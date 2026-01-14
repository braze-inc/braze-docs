---
nav_title: Essais
article_title: Test des cartes de contenu
page_order: 3
description: "Cet article de référence explique comment prévisualiser et tester les cartes de contenu, ainsi que quelques bonnes pratiques."
channel:
  - content cards
  
---

# Test des cartes de contenu

> Il est extrêmement important de toujours tester vos cartes de contenu avant d'envoyer vos campagnes. Nos fonctionnalités de prévisualisation et de test offrent deux façons de jeter un coup d'œil à vos cartes de contenu. Vous pouvez prévisualiser votre message pour vous aider à le visualiser lorsque vous le composez, ainsi qu'envoyer un message test à vous-même ou à l'appareil d'un utilisateur spécifique. Nous vous recommandons de profiter des deux.

## Avant-première

Vous pouvez prévisualiser votre carte au fur et à mesure que vous la composez. Cela devrait vous aider à visualiser ce à quoi ressemblera votre message final du point de vue de l'utilisateur.

Dans l'onglet **Aperçu** de votre compositeur, l'affichage de votre message peut ne pas être identique à son rendu réel sur l'appareil de l'utilisateur. Nous vous recommandons de toujours envoyer un message test à un appareil pour vous assurer que vos médias, votre texte, votre personnalisation et vos attributs personnalisés sont générés correctement.

## Test

Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, la fonction "push" doit être activée sur vos appareils de test et des jetons "push" valides doivent être enregistrés pour l'utilisateur test avant l'envoi. Pour les utilisateurs iOS, vous devez appuyer sur la notification push envoyée par Braze afin d'afficher la carte contenu du test. Ce comportement ne s'applique qu'aux cartes de contenu testées.

### Prévisualisation du message en tant qu'utilisateur

Vous pouvez également prévisualiser les messages à partir de l'onglet **Test** comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur aléatoire ou créer un utilisateur personnalisé.

\![Un aperçu de la carte de contenu dans l'onglet "Test".]({% image_buster /assets/img/cc-user-preview.png %}){: style="max-width:80%;"}

### Liste de contrôle des tests

- Les images et les médias apparaissent-ils et agissent-ils comme prévu ?
- Le liquide fonctionne-t-il comme prévu ? Avez-vous prévu une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) au cas où le liquide ne renverrait aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos liens dirigent-ils l'utilisateur vers l'endroit où il doit se rendre ?

## Débogage

Après l'envoi de vos cartes de contenu, vous pouvez résoudre ou déboguer tout problème à partir du [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) dans la console de développement. 

Un cas d'utilisation courant consiste à essayer de comprendre pourquoi un utilisateur ne peut pas voir une carte de contenu particulière. Pour ce faire, vous pouvez rechercher dans les **journaux des événements utilisateurs** les cartes de contenu transmises au SDK au début de la session, mais avant une impression, et les rattacher à une campagne spécifique :

1. Allez dans **Paramètres** > Journal des événements utilisateurs.
2. Emplacement/localisation de la demande de SDK pour votre utilisateur test.
3. Cliquez sur **Données brutes**.
4. Trouvez le site `id` pour votre session. Vous trouverez ci-dessous un exemple d'extrait :

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

5. Utilisez un outil de décodage comme [Base64 Decode and Encode](https://www.base64decode.org/) pour décoder le `id` du format Base64 et trouver le `campaign_id` associé. Dans notre exemple, le résultat est le suivant :

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Où `4861692e-6fce-4215-bd05-3254fb9e9057` est le `campaign_id`.<br><br>

6. Rendez-vous sur la page des **campagnes** et recherchez le site `campaign_id`.

\![Recherchez campaign_id sur la page des campagnes]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

À partir de là, vous pouvez examiner les paramètres et le contenu de vos messages pour déterminer pourquoi un utilisateur ne peut pas voir une carte de contenu particulière.

