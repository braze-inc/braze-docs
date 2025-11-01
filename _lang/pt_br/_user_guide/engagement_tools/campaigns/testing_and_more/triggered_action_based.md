---
nav_title: Campanhas acionadas por API e baseadas em ações
article_title: Teste de campanhas acionadas por API e baseadas em ações
page_order: 2
page_type: reference
description: "Este artigo de referência explica como testar campanhas acionadas por API e baseadas em ações."

---

# Campanhas acionadas por API e baseadas em ações

> Ao configurar campanhas, é sempre uma boa prática testar suas mensagens antes de lançá-las. Este artigo de referência aborda a criação de um segmento de usuário de teste que permitirá que você inspecione solicitações de API, cargas úteis e visualize logs de capacidade de entrega.

## Etapa 1: Crie um segmento de usuário de teste

A única maneira de testar o acionamento de uma campanha com a API ou com o evento personalizado é enviar a campanha ao vivo. Como parte da implementação de uma nova campanha, é altamente recomendável adicionar um segmento de usuário de teste às campanhas ao testar o acionamento da capacidade de entrega. Isso proporcionará uma rede de segurança, garantindo que, mesmo que uma campanha seja enviada acidentalmente, ela só será enviada para usuários internos.

1. **Importar usuários de teste**<br>Os usuários de teste podem ser importados para o Braze por meio de um CSV ou de uma solicitação única em lote por meio do [Postman]({{site.baseurl}}/api/postman_collection/). Ao importar esses usuários, recomendamos definir um atributo personalizado em seus perfis (como `internal_test_user: true`) que possa ser usado para criar um segmento de grupo de teste. <br><br>
2. **Adicionar usuários de teste como usuários de teste reconhecidos pelo Brasil**<br>[Marcar seus usuários de teste como usuários de teste reconhecidos pelo Braze]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/) no painel dá acesso ao registro detalhado de cada usuário, permitindo que você inspecione as solicitações de API e suas cargas úteis e visualize os registros de capacidade de entrega. Esses logs podem ajudá-lo a determinar se houve algum problema na entrega de campanhas aos usuários finais. <br><br>
3. **Criar segmento**<br>Para criar um segmento de usuário de teste, crie um segmento de usuários com o atributo personalizado `internal_test_user` definido como `true`. Esse segmento pode ser removido quando a campanha for ao ar. 

## Etapa 2: Envios de testes

Em seguida, você pode fazer um teste de envio no painel do Braze ou usar o Inbox Vision (somente e-mail) para ver como será o layout enquanto a campanha ainda estiver no modo de rascunho. Em seguida, você pode enviar a campanha para o seu segmento de usuários de teste para verificar se ela está se comportando conforme o esperado. Independentemente de a campanha ser acionada pela API ou baseada em ação, use o Postman para enviar uma solicitação única à API do Braze, acionando a campanha. 

## Etapa 3: Use o registro do Braze para inspecionar os resultados de entrada

Use o registro do Braze para solucionar problemas de acionamento, envio e eventos. 
- O [registro do usuário do evento]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) mostrará a carga útil bruta da solicitação do acionador da API, o evento personalizado que aciona a campanha e todas as propriedades associadas do acionador ou do evento.
- O [log de atividades de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) registrará todos os erros e o ajudará a entender por que uma determinada mensagem pode não ter sido entregue.

## Etapa 4: Remova o segmento de teste e implemente a campanha

Quando a mensagem estiver sendo acionada e renderizada corretamente com todos os links clicados registrados, você poderá remover o segmento e atualizar a campanha. Se preferir iniciar a campanha do zero para que as poucas impressões do usuário de teste não sejam incluídas, você pode duplicar a campanha e reiniciá-la sem o segmento do usuário de teste. 
