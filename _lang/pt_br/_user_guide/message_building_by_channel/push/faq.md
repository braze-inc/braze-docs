---
nav_title: Perguntas frequentes
article_title: FAQs sobre Push
page_order: 80
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem ao configurar campanhas de push."
page_type: FAQ
channel:
  - Push
---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre o canal de push.

### O que acontece quando vários usuários fazem login em um único dispositivo?

Quando um usuário sai de um dispositivo ou site, ele continuará acessível por push até que outro usuário faça login. Nesse ponto, o token por push é reatribuído ao novo usuário. Isso ocorre porque cada dispositivo pode ter apenas uma inscrição ativa por push por aplicativo ou site.

Quando um token por push é reatribuído, a mudança é refletida no **Changelog de Push** do perfil do usuário. Você pode encontrar isso acessando a guia **Engajamento** no perfil do usuário.

![O "Changelog de Push" na seção "Configurações de Contato".]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### Por que um usuário que optou por receber não tem um token por push?

Isso pode acontecer se o token por push do usuário foi reatribuído a outra pessoa que usou o mesmo dispositivo.

1. Acesse o **Changelog de Push** na guia **Engajamento** do perfil do usuário afetado.
2. Procure uma mensagem que diga que o token por push foi movido para outro usuário.
3. Copie o token por push e cole na barra de pesquisa de usuários. 
4. Se o token por push ainda existir, você será direcionado ao usuário que fez login mais recentemente no dispositivo.

Se você quiser que o token por push seja reatribuído ao usuário original:

1. Faça com que o usuário original faça login no perfil com o token por push ausente.
2. Dispare um novo envio de push. Isso moverá o token de volta para a conta se eles ainda tiverem push habilitado no nível do dispositivo.

