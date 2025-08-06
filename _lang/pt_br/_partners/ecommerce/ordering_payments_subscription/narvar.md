---
nav_title: Narvar
article_title: Narvar
description: "Saiba como integrar o Narvar ao Braze."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> O Narvar é uma plataforma pós-compra que aumenta a fidelidade do cliente por meio de rastreamento de pedidos, atualizações de entrega e gerenciamento de devoluções. A integração entre a Braze e a Narvar ativa as marcas para aproveitar os eventos de notificação da Narvar para disparar mensagens diretamente da Braze, mantendo os clientes informados com atualizações oportunas.

## Pré-requisitos

| Requisito           | Descrição                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Conta Narvar        | É necessário ter uma conta Narvar para aproveitar essa parceria.                           |
| Chave da API REST do Braze    | Uma chave da API REST do Braze com permissão `messages.send`. Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**.                                            |
| Endpoint REST  do Braze   | O [URL do endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), que depende do URL para sua instância da Braze.         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Recursos suportados

|Tipo|Recursos suportados|
|-------|----------|
| Notificações | \- Antecipação de entrega<br>\- Postergação da operadora<br>\- Padrão entregue |
| Canais | Notificações por push |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Se estiver interessado em tipos ou canais de notificação adicionais, entre em contato com o CSM do Braze e do Narvar.
{% endalert %}

## Detalhes da integração

Para cada evento de notificação, o Narvar inicia uma solicitação ao ponto de extremidade do Braze [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging) para entregar uma mensagem push a cada consumidor com aceitação.

O Narvar é responsável por configurar as cargas úteis de notificação por push para cada mensagem. Atualmente, o Narvar não tem uma interface de design integrada para notificações por push, portanto, a equipe colaborará com a sua equipe para determinar e definir os requisitos de carga útil. Essas cargas úteis podem ser personalizadas da mesma forma que as enviadas por meio de seu próprio sistema, incluindo suporte para placeholders de conteúdo variável, como dados de pedidos e detalhes do cliente.

## Primeiros passos com a integração Braze-Narvar

1. **Entre em contato com o CSM da Narvar** para manifestar interesse na integração.
2. **Designar ambientes Braze** para preparação e produção.
3. **Gerar uma chave de API** no Braze para uso do Narvar.
4. **Gerar chave(s) de campanha** no Braze, conforme necessário.
5. **Forneça chaves de API e de campanha** ao Narvar por meio de um link seguro de uso único.
6. **Compartilhe os detalhes da carga útil da notificação por push** para finalizar a configuração.
