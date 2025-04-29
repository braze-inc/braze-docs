---
nav_title: Cliques push que abrem inesperadamente no app
article_title: Cliques push que abrem inesperadamente no app
page_type: solution
description: "Este artigo de ajuda aborda como solucionar problemas quando se espera que um link push seja aberto em um navegador da Web, e não no app."
channel: push
---

# Cliques push que abrem inesperadamente no app

Se estiver tendo problemas com links em notificações por push que abrem inesperadamente no app em vez de no navegador da Web, pode haver um problema com a configuração da campanha ou com a implementação do SDK. Consulte estas etapas para obter ajuda.

## Verificar o comportamento ao clicar

Na etapa de sua campanha ou do Canva, verifique se a opção **Abrir URL da Web dentro do app móvel** não está selecionada. Se for o caso, limpe a seleção e reinicie. 

![O campo "Comportamento ao clicar" da configuração de um push definido como "Abrir URL da web" com "Abrir URL da web dentro do app móvel" desmarcado.]({% image_buster /assets/img/push_on_click.png %})

A interação padrão para o comportamento ao clicar em "Abrir URL da Web" difere de acordo com a versão do SDK. Para as versões do SDK iOS 2.29.0 e Android 2.0.0 e superiores, essa opção é selecionada por padrão e os URLs da Web serão abertos em uma visualização da Web dentro do app. Antes dessas versões, essa opção é desmarcada por padrão e os URLs da Web são abertos no navegador da Web padrão do dispositivo.

Se esse não for o problema, pode haver um problema com sua implementação do push. 

## Verifique novamente a integração do push

Se os links em suas notificações por push estiverem abrindo no app inesperadamente, isso pode ser devido a problemas com a integração da notificação por push ou com as configurações de personalização. Siga estas etapas para solucionar o problema:

1. **Revise a implementação do delegado push:** Certifique-se de que o delegado do Braze push esteja implementado corretamente. Para obter instruções detalhadas, consulte o guia de integração para notificações por push de sua [plataforma]({{site.baseurl}}/developer_guide/home/).
2. **Inspecionar o tratamento de links personalizados:** Verifique se o app inclui tratamento personalizado para todos os links `https://`. As configurações personalizadas podem substituir os comportamentos padrão. Colabore com sua equipe de desenvolvimento para revisar e ajustar essas configurações, se necessário.
3. **Verifique o registro push do iOS:** Para iOS, reveja a etapa 1 do guia de integração por push sobre o [registro de notificações por push com APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Certifique-se de que seu objeto delegado seja atribuído de forma síncrona antes que o app termine de ser iniciado. Essa etapa deve ser concluída no método `application:didFinishLaunchingWithOptions:`.
4. **Teste sua integração:** Depois de fazer os ajustes, teste o comportamento da notificação por push nos dispositivos iOS e Android para confirmar que o problema foi resolvido.

Se o problema persistir, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact) para obter mais assistência.


*Última atualização em 6 de dezembro de 2024*