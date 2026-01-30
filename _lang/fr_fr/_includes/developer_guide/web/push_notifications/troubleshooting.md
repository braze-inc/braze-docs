## Résolution des problèmes

Si vous rencontrez des problèmes après avoir configuré les notifications push, pensez à ce qui suit :

- Les notifications push Web exigent que votre site soit en HTTPS.
- Tous les navigateurs ne peuvent pas recevoir de messages de notification push. Assurez-vous que `braze.isPushSupported()` retourne `true` dans le navigateur.
- Certains navigateurs, comme Firefox, n'affichent pas les images dans les notifications push. Pour plus de détails sur la prise en charge des navigateurs, reportez-vous à la [documentation MDN sur les images de notification.](https://developer.mozilla.org/en-US/docs/Web/API/Notification/image)
- Si un utilisateur a refusé au site l’accès aux notifications push, il ne recevra plus de demande d’autorisation à moins qu’il ne supprime l’état refusé de ses préférences de navigateur.
