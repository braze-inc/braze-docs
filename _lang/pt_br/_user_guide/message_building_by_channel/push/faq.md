---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre push
page_order: 80
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem durante a configuração de campanhas push."
page_type: FAQ
channel:
  - Push
---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre o canal push.

### O que acontece quando vários usuários fazem login em um único dispositivo?

Quando um usuário faz logout de um dispositivo ou site, ele permanecerá acessível por push até que outro usuário faça login. Nesse momento, o token push é reatribuído ao novo usuário. Isso ocorre porque cada dispositivo só pode ter uma assinatura push ativa por aplicativo ou site.

Quando um token push é reatribuído, a alteração é refletida no **Push Changelog** do perfil do usuário. Você pode encontrar isso acessando a guia **Envolvimento** no perfil do usuário.

\![O "Push Changelog" na seção "Contact Settings" (Configurações de contato).]({% image_buster /assets/img/push_changelog_faq.png %}){: style="max-width:50%;"}

### Por que um usuário opt-in não tem um token de envio?

Isso pode acontecer se o token push do usuário tiver sido reatribuído a outra pessoa que usou o mesmo dispositivo.

1. Acesse o **Push Changelog** na guia **Engagement (Envolvimento** ) do perfil do usuário afetado.
2. Procure uma mensagem informando que o token push foi movido para outro usuário.
3. Copie o token de envio e cole-o na barra de pesquisa do usuário. 
4. Se o token push ainda existir, você será direcionado para o usuário que fez login mais recentemente no dispositivo.

Se quiser que o token push seja reatribuído ao usuário original:

1. Faça com que o usuário original faça login no perfil com o token push ausente.
2. Aciona um novo envio por push. Isso moverá o token de volta para a conta se ela ainda tiver o push ativado no nível do dispositivo.

