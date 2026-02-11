## Solução de problemas

Se você estiver enfrentando problemas após configurar notificações por push, considere o seguinte:

- As notificações por push da Web exigem que seu site seja HTTPS.
- Nem todos os navegadores podem receber mensagens de navegador. Certifique-se de que `braze.isPushSupported()` retorne `true` no navegador.
- Alguns navegadores, como o Firefox, não exibem imagens em notificações por push. Para detalhes sobre o suporte a navegadores, consulte a [documentação do MDN para imagens de Notificação](https://developer.mozilla.org/en-US/docs/Web/API/Notification/image).
- Se um usuário tiver negado o acesso push a um site, ele não será solicitado a dar permissão novamente, a menos que remova o status de negação das preferências do navegador.
