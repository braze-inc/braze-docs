---
nav_title: Desativar o rastreamento do SDK para iOS
article_title: Desativar o rastreamento do SDK para iOS
platform: Swift
page_order: 8
description: "Este artigo mostra como desativar a coleta de dados para o Swift SDK."

---

# Desativar o rastreamento do SDK para iOS

> Para cumprir os normas de privacidade de dados, a atividade de rastreamento de dados no SDK iOS pode ser completamente interrompida definindo a propriedade [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) como `false` na sua instância da Braze. 

Quando `enabled` é definido como `false`, o SDK da Braze ignora qualquer chamada para a API pública. O SDK também cancela todas as ações em andamento, como solicitações de rede, processamento de eventos, etc. Para retomar a coleta de dados, defina [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) como `true`.

Você também pode usar o método [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) para limpar completamente os dados do SDK armazenados localmente no dispositivo de um usuário. Se você estiver usando a versão 5.7.0 ou anterior do SWIFT SDK, ou `useUUIDAsDeviceId` estiver configurado para `false`, você também precisará fazer uma solicitação POST para [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/), pois seu Identificador para Fornecedores (IDFV) será usado como o ID do dispositivo deles. Para as versões 7.0.0 e posteriores do Swift da Braze, o SDK e o método `wipeData()` geram aleatoriamente um UUID para o ID do seu dispositivo.
