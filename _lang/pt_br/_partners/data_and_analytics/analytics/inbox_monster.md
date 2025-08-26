---
nav_title: Monstro da Caixa de Entrada
article_title: Monstro da Caixa de Entrada
alias: /partners/inbox_monster/
description: "Este artigo de referência descreve a parceria entre Braze e Inbox Monster, uma ferramenta de marketing por e-mail online que permite aos clientes da Braze desbloquear poderosas percepções de entregabilidade e análise criativa para potencializar a performance da caixa de entrada."
page_type: partner
search_tag: Partner

---

# Monstro da Caixa de Entrada

> [Inbox Monster](https://inboxmonster.com/) é uma plataforma de sinais de caixa de entrada que ajuda marcas empresariais a garantir cada envio. É um conjunto integrado de soluções para entregabilidade, renderização criativa e monitoramento de SMS, que capacita as equipes modernas de gestão de relacionamento com o cliente (CRM) e acaba com os medos de envio.

A integração Braze e Inbox Monster permite eliminar os testes manuais de lista de sementes, automatizar a criação de sinais de colocação de caixa de entrada poderosos e acionáveis, simplificar o processo de revisão e aprovação de ativos criativos de e-mail e obter insights valiosos sobre entregabilidade. Você também pode importar modelos de e-mail para diagnósticos criativos e visualizações de dispositivos de forma integrada.

## Pré-requisitos

| Requisito                    | Descrição                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Conta da plataforma Inbox Monster | Uma conta na plataforma Inbox Monster é necessária para aproveitar esta parceria.                                                                                                                                                                                                                                                                                                                                                                 |
| Chave da API REST do Braze             | Uma chave da API REST do Braze com as seguintes permissões:  <br> - `messages.send` <br>  - `templates.email.create`<br> - `templates.email.update` <br> - `templates.email.info`<br> `templates.email.list` <br><br> E com os seguintes ips autorizados: <br> `3.136.16.19` <br>  - `3.140.233.31`<br> `18.220.127.138` <br><br> Isso pode ser criado no dashboard do Braze a partir de **Configurações** > **APIs e Identificadores** na guia **Chaves de API** |
| Identificador do app Braze           | Um identificador de app Braze. <br><br>Isso pode ser encontrado no dashboard do Braze em **Configurações** > **APIs e Identificadores** na guia **Identificadores de Aplicativos**.                                                                                                                                                                                                                                                                                                |
| Ponto de extremidade do Braze                 | [Seu endpoint Braze]({{site.baseurl}}/api/basics/#endpoints) está alinhado com o URL do dashboard Braze.<br><br> Por exemplo, se o URL do dashboard for `https://dashboard-03.braze.com`, seu endpoint será `dashboard-03`.                                                                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Integração

Para integrar o Inbox Monster, siga os passos em [Integrando com o Inbox Monster](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_80147afaf3).

## Uso

Para aprender como enviar testes de posicionamento na caixa de entrada programados através do Inbox Monster, consulte [Testes de Posicionamento na Caixa de Entrada Programados](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_7e74bc474e).
