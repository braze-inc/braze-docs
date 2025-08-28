---
nav_title: Test
article_title: Tester des cartes de contenu
page_order: 3
description: "Le présent article de référence explique comment prévisualiser et tester les cartes de contenu, et décrit certaines des meilleures pratiques."
channel:
  - content cards
  
---

# Tester des cartes de contenu

> Il est extrêmement important de toujours tester vos cartes de contenu avant d’envoyer vos campagnes. Nos capacités de prévisualisation et de test offrent deux façons de vérifier vos cartes de contenu. Vous pouvez prévisualiser votre message pendant que vous le composer, et vous envoyer un message de test (ou un autre appareil spécifique). Nous vous recommandons d’utiliser les deux.

## Aperçu

Vous pouvez prévisualiser votre carte lorsque vous la composez. Cela devrait vous aider à visualiser à quoi ressemblera votre message final du point de vue de l’utilisateur.

Dans l'onglet **Aperçu** de votre compositeur, l'affichage de votre message peut ne pas être identique à son rendu réel sur l'appareil de l'utilisateur. Nous vous recommandons d’envoyer toujours un message test à un appareil pour vérifier que votre support, votre texte, votre personnalisation et vos attributs personnalisés sont générés correctement.

## Test

Pour envoyer un test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, la fonction push doit être activée sur vos appareils de test et des jetons push valides doivent être enregistrés pour l'utilisateur test avant l'envoi. Pour les utilisateurs iOS, vous devez appuyer sur la notification push envoyée par Braze pour afficher la carte de contenu test. Ce comportement s’applique uniquement aux tests des cartes de contenu.

### Aperçu du message en tant qu’utilisateur

Vous pouvez également prévisualiser les messages à partir de l'onglet **Test** comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur aléatoire ou créer un utilisateur personnalisé.

![Aperçu d'une carte de contenu dans l'onglet "Test".]({% image_buster /assets/img/cc-user-preview.png %}){: style="max-width:80%;"}

### Liste de contrôle des tests

- Les images et les données s’affichent-elles et se comportent-elles comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous prévu une [valeur d'attribut par défaut]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) au cas où Liquid ne renverrait aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos liens dirigent-ils l’utilisateur vers les bons endroits ?

## Débogage

Après l'envoi de vos cartes de contenu, vous pouvez résoudre ou déboguer tout problème à partir du [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) sur la console de développement. 

C’est notamment utile pour comprendre pourquoi un utilisateur n’arrive pas à voir une carte de contenu spécifique. Pour ce faire, vous pouvez rechercher dans les **journaux des événements utilisateurs** les cartes de contenu transmises au SDK au début de la session, mais avant une impression, et les rattacher à une campagne spécifique :

1. Sélectionnez **Paramètres** > **Journal des événements utilisateurs**.
2. Localisez et développez la demande SDK pour votre utilisateur test.
3. Cliquez sur **Données brutes**.
4. Trouvez le `id` pour votre session. Voici un échantillon d’exemple :

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

5. Utilisez un outil de décodage comme [Base64 Decode and Encode](https://www.base64decode.org/) pour décoder le `id` du format Base64 et trouver le `campaign_id` associé. Dans notre exemple, cela donne les résultats suivants :

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Où `4861692e-6fce-4215-bd05-3254fb9e9057` est le `campaign_id`.<br><br>

6. Rendez-vous sur la page des **campagnes** et recherchez le site `campaign_id`.

![Recherche de l'identifiant de la campagne sur la page des campagnes]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

Ensuite, vous pouvez examiner les paramètres et le contenu de vos messages pour déterminer pourquoi un utilisateur ne voit pas une carte de contenu particulière.

