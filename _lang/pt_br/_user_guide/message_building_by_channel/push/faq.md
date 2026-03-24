---
nav_title: Perguntas frequentes
article_title: Perguntas Frequentes sobre Push
page_order: 25
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem ao configurar campanhas de push."
page_type: FAQ
channel:
  - Push
---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre o canal de push.

### O que acontece quando vários usuários fazem login em um único dispositivo?

Quando um usuário sai de um dispositivo ou site, ele continuará acessível por push até que outro usuário faça login. Nesse ponto, o token por push é reatribuído ao novo usuário. Isso ocorre porque cada dispositivo pode ter apenas uma inscrição ativa de push por app ou site.

Quando um token por push é reatribuído, a mudança é refletida no **changelog de push** do perfil de usuário. Você pode encontrá-lo acessando a guia **Engajamento** no perfil de usuário.

![O "changelog de push" na seção "Configurações de Contato".]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### Quando envio um push de teste, ele é enviado para todos os meus dispositivos?

Sim. O push de teste é enviado para todos os dispositivos com push ativado associados ao perfil de usuário selecionado. Se você tiver vários telefones ou tablets conectados com o mesmo usuário, cada dispositivo com um token por push válido receberá a notificação.

Para enviar o push de teste para apenas um dispositivo, você pode remover os tokens por push dos outros dispositivos no perfil de usuário antes de testar. Alternativamente, se estiver enviando com o [endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/), defina `send_to_most_recent_device_only` como `true` no objeto `apple_push` ou `android_push` para que apenas o dispositivo ativo mais recentemente receba o push.

### O que significa "Erro ao enviar push porque a carga útil era inválida"?

Esta mensagem indica que o APNs rejeitou a solicitação de push devido a uma carga útil inválida (por exemplo, uma carga útil vazia ou uma carga útil grande demais).

Para mais detalhes e próximas etapas, consulte [Mensagens de erro comuns de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_error_codes/).

### Por que um usuário que optou por receber não tem um token por push?

Isso pode acontecer se o token por push do usuário foi reatribuído a outra pessoa que usou o mesmo dispositivo.

1. Acesse o **changelog de push** na guia **Engajamento** do perfil do usuário afetado.
2. Procure uma mensagem indicando que o token por push foi movido para outro usuário.
3. Copie o token por push e cole na barra de pesquisa de usuários. 
4. Se o token por push ainda existir, você será direcionado ao usuário que fez login mais recentemente no dispositivo.

Se você quiser que o token por push seja reatribuído ao usuário original:

1. Faça o usuário original fazer login no perfil com o token por push ausente.
2. Dispare um novo envio de push. Isso moverá o token de volta para a conta, caso o push ainda esteja ativado no nível do dispositivo.

### Qual é a diferença entre "Enviar para Produção" e "Enviar para Desenvolvimento" nos certificados de push do iOS?

Ao adicionar um certificado de push da Apple na Braze, as opções **Enviar para Produção** e **Enviar para Desenvolvimento** determinam qual gateway do APNs (serviço de Notificações por Push da Apple) a Braze usa para entregar notificações por push:

- **Enviar para Desenvolvimento:** Selecione esta opção se o app foi compilado em modo de desenvolvimento no Xcode e assinado com um perfil de provisionamento de desenvolvimento. As notificações por push são roteadas pelo gateway de desenvolvimento (sandbox) da Apple.
- **Enviar para Produção:** Selecione esta opção se o app é distribuído via TestFlight da Apple, App Store ou distribuição corporativa. As notificações por push são roteadas pelo gateway de produção da Apple.

Se a opção errada for selecionada, as notificações por push falham silenciosamente porque o tipo de token por push não corresponde ao gateway. Normalmente, apps distribuídos pelo TestFlight ou pela App Store devem usar **Enviar para Produção**.