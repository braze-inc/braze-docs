---
nav_title: Réinitialisation des autorisations de Push
article_title: Réinitialisation des autorisations de Push
page_type: solution
description: "Cet article d'aide explique comment réinitialiser les autorisations et les données de push du navigateur."
channel: push
---

# Réinitialisation des autorisations de push

Si vous rencontrez des problèmes avec les notifications push dans votre navigateur, vous devrez peut-être réinitialiser les autorisations de notification de votre site et effacer le stockage de votre site. Reportez-vous à ces étapes pour obtenir de l'aide.

## Réinitialiser Chrome sur le bureau

1. À côté de votre URL dans le navigateur Chrome, cliquez sur l'icône du curseur **Afficher les informations sur le site.** 
2. Sous **Notifications**, cliquez sur **Réinitialiser l'autorisation**.
3. Ouvrez Chrome DevTools. Vous trouverez ci-dessous les raccourcis pertinents pour chaque système d'exploitation.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | Raccourcis clavier                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\. Dans DevTools, accédez à l'onglet **Application**.
5\. Dans la barre latérale, sélectionnez **Stockage**.
6\. Cliquez sur **Effacer les données du site**.
7\. Chrome vous demandera de recharger la page pour appliquer les paramètres mis à jour. Cliquez sur **Recharger**.

Vos autorisations de push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez-le.

## Réinitialiser Chrome sur Android

Si une notification de votre site est visible dans le tiroir de notification de votre Android :

1. À partir de la notification push, appuyez sur <i class="fas fa-cog" title="Paramètres"></i> et sélectionnez **Paramètres du site.**
2. Dans les **paramètres du site**, appuyez sur **Effacer et réinitialiser.**

Si vous n'avez pas reçu de notification de votre site, ouvrez-le :

1. Ouvrez Chrome sur Android.
2. Appuyez sur le menu <i class="fas fa-ellipsis-vertical"></i>.
3. Allez dans **Réglages** > **Réglages du site** > **Notifications.**
4. Vérifiez que les notifications sont réglées sur "Demander avant d'envoyer (recommandé)".
5. Trouvez votre site dans la liste.
6. Sélectionnez l'entrée et appuyez sur **Effacer et réinitialiser**.

Vos autorisations de push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez-le.

## Réinitialiser Firefox sur le bureau

1. A côté de l'URL de votre site, cliquez sur <i class="fa-solid fa-circle-info" alt="info icon"></i> ou <i class="fas fa-lock" alt="lock icon"></i>.
2. Sous **Autorisations**, à côté de **Recevoir des notifications**, sélectionnez <i class="fa-solid fa-circle-xmark" title="Effacer cette autorisation et redemander"></i> pour supprimer les autorisations de notification.
3. Dans le même menu, sélectionnez **Effacer les cookies et les données du site**.
4. Une boîte de dialogue apparaît pour confirmer votre choix. Cliquez sur **OK**.

Vos autorisations de push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez-le.

## Réinitialiser Firefox sur Android

Pour réinitialiser les autorisations push sur Android, reportez-vous à cet [article d'assistance de Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

## Réinitialiser Safari sur macOS

{% alert note %}
Ces étapes ne concernent que macOS, car Apple ne prend pas en charge les notifications push Web pour Safari sous Windows.
{% endalert %}

1. Ouvrez Safari.
2. Dans la [barre de menus sur Mac,](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac) accédez à **Safari** > **Réglages** > **Sites web** > **Notifications.**
3. Sélectionnez votre site dans la liste.
4. Cliquez sur **Supprimer** pour supprimer les autorisations de notification pour le site.
5. Ensuite, allez dans **Confidentialité** > **Gérer les données du site web.**
6. Sélectionnez votre site dans la liste.
7. Cliquez sur **Supprimer**, ou pour supprimer toutes les données du site, cliquez sur **Supprimer tout**.
8. Cliquez sur **Terminé**.

Vos autorisations de push sont maintenant réinitialisées. Ouvrez un nouvel onglet vers votre site et essayez-le.


*Dernière mise à jour le 12 février 2024*