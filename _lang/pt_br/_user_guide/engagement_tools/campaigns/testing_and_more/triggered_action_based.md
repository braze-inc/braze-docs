---
nav_title: Campanhas acionadas por API e baseadas em ações
article_title: Testando campanhas acionadas por API e baseadas em ações
page_order: 2
page_type: reference
description: "Este artigo de referência explica como testar campanhas acionadas por API e baseadas em ações."

---

# Campanhas acionadas por API e baseadas em ações

> Ao configurar campanhas, é sempre uma boa prática testar suas mensagens antes de lançar. Este artigo de referência cobre a criação de um segmento de usuário teste que permitirá inspecionar solicitações de API, cargas úteis e visualizar logs de entregabilidade.

## Etapa 1: Crie um segmento de usuário teste

A única maneira de testar o acionamento de uma campanha com a API ou evento personalizado é colocar a campanha no ar com um push. Como parte do lançamento de uma nova campanha, recomendamos fortemente adicionar um segmento de usuário teste às campanhas ao testar a entregabilidade de disparo. Isso fornecerá uma rede de segurança, garantindo que, mesmo que uma campanha seja enviada acidentalmente, ela seja direcionada apenas para usuários internos.

1. **Importar usuários de teste**<br>Os usuários de teste podem ser importados para o Braze através de um CSV ou uma solicitação em lote única através do [Postman]({{site.baseurl}}/api/postman_collection/). Ao importar esses usuários, recomendamos definir um atributo personalizado em seus perfis (como `internal_test_user: true`) que pode ser usado para construir um segmento de grupo de teste. <br><br>
2. **Adicione usuários de teste como usuários de teste reconhecidos pela Braze**<br>[Marcar seus usuários de teste como usuários de teste reconhecidos pelo Braze]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/) no dashboard lhe dá acesso a logs detalhados para cada usuário, permitindo inspecionar solicitações de API, seus payloads e visualizar logs de entregabilidade. Esses logs podem ajudá-lo a determinar se houve algum problema na entrega de campanhas aos usuários finais. <br><br>
3. **Crie segmento**<br>Para criar um segmento de usuário teste, crie um segmento de usuários com o atributo personalizado `internal_test_user` definido como `true`. Este segmento pode ser removido quando a campanha for ao ar. 

## Etapa 2: Envios de teste

Em seguida, você pode fazer um envio de teste do dashboard da Braze ou usar o Inbox Vision (e-mail apenas) para ver como será o layout enquanto a campanha ainda estiver no modo de rascunho. Você pode então enviar a campanha para o seu segmento de usuário teste para verificar se está se comportando como esperado. Independentemente de a campanha ser acionada por API ou baseada em ação, use o Postman para enviar uma solicitação única para a API da Braze, acionando a campanha. 

## Etapa 3: Use os registros da Braze para inspecionar os resultados recebidos

Use os registros da Braze para solucionar problemas de gatilho, envio e eventos. 
- O [registro de usuários de eventos]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) mostrará a carga útil bruta da solicitação disparada pela API, o evento personalizado disparando a campanha e quaisquer propriedades associadas ao disparo ou evento.
- O [registro de atividade de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) registrará quaisquer erros e ajudará você a entender por que uma determinada mensagem pode não ter sido entregue.

## Etapa 4: Remova o segmento de teste e lance a campanha

Depois que a mensagem estiver acionando e renderizando corretamente com todos os links clicados registrados, você pode remover o segmento e atualizar a campanha. Se preferir iniciar a campanha do zero para que as poucas impressões de usuário teste não sejam incluídas, você pode duplicar a campanha e reiniciá-la sem o segmento de usuário teste. 
