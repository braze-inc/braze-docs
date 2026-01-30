---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre o push
page_order: 25
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem durante a configuração de campanhas push."
page_type: FAQ
channel:
  - Push
---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre o canal push.

### O que acontece quando vários usuários registram-se em um único dispositivo?

Quando um usuário se desconecta de um dispositivo ou site, ele permanecerá acessível por push até que outro usuário se conecte. Nesse momento, o token por push é reatribuído ao novo usuário. Isso ocorre porque cada dispositivo só pode ter uma inscrição push ativa por app ou site.

Quando um token por push é reatribuído, a alteração é refletida no Push Changelog do perfil do usuário. Você pode encontrar isso acessando a guia **Engajamento** no perfil do usuário.

![O "Push Changelog" na seção "Contact Settings" (Configurações de contato).]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### Por que um usuário com aceitação não tem um token por push?

Isso pode acontecer se o token por push do usuário foi reatribuído a outra pessoa que usou o mesmo dispositivo.

1. Acesse o **changelog do push** na guia **Engajamento** do perfil do usuário afetado.
2. Procure uma mensagem que diga que o token por push foi movido para outro usuário.
3. Copie o token por push e cole-o na barra de pesquisa do usuário. 
4. Se o token por push ainda existir, você será direcionado para o usuário que fez o registro mais recente no dispositivo.

Se quiser que o token por push seja reatribuído ao usuário original:

1. Faça com que o usuário original registre o perfil com o token por push ausente.
2. Disparar um novo envio push. Isso moverá o token de volta para a conta se ela ainda tiver o push ativado no nível do dispositivo.

