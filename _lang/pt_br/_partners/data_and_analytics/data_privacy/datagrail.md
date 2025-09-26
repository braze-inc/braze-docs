---
nav_title: DataGrail
article_title: DataGrail
description: "Este artigo de referência descreve a parceria entre a Braze e a DataGrail, uma plataforma de gerenciamento de privacidade, que permite detectar os dados do consumidor coletados e armazenados na Braze para processar rapidamente as DSRs."
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> A [DataGrail](https://www.datagrail.io/), uma plataforma de gerenciamento de privacidade, ajuda a criar a confiança do consumidor e a eliminar negócios arriscados. Com a detecção contínua do sistema e o atendimento automatizado de solicitações de titulares de dados (DSR), a DataGrail potencializa os programas de privacidade, apoiando a conformidade com as leis e regulamentos de privacidade em evolução, como GDPR, CCPA e CPRA. 

_Essa integração é mantida pelo DataGrail._

## Sobre a integração

A integração entre a Braze e a DataGrail permite que você detecte os dados do consumidor coletados e armazenados na Braze para processar rapidamente as DSRs (solicitações de acesso, exclusão e não venda). O Braze será adicionado a um plano preciso de onde os dados do consumidor residem em sua organização com mapeamento de dados automatizado - não são mais necessárias pesquisas ou planilhas para manter uma estrutura de privacidade ou produzir um registro de atividades de processamento (RoPA). 

## Pré-requisitos

| Solicitações | Descrição |
|---|---|
| Conta DataGrail | Uma conta DataGrail para aproveitar essa parceria.<br>Entre em contato com o administrador ou envie um e-mail para support@datagrail.io se tiver algum problema ou dúvida sobre a integração. |
| chave de API Braze | Uma chave da API REST da Braze com as permissões `events.list`, `users.export.ids`, `users.delete` e `users.track`.<br><br>Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Instância do Braze | Sua instância do Braze pode ser obtida com seu gerente de integração do Braze ou pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Faça login no portal DataGrail e selecione **Connect (Conectar)** na página de integração do Braze. Em seguida, insira sua instância e a chave de API do Braze e selecione **Connect Braze**.

Se houver contas Braze adicionais a serem integradas:
1. Selecione **Editar conexão** na página de integração do Braze.
2. No menu suspenso, selecione **+Add New Connection (Adicionar nova conexão)**.
3. Em **Connection Name (Nome da conexão)**, digite um novo nome para identificar essa conta separada (por exemplo, Braze Training Account).
4. Insira uma instância separada e uma chave de API da Braze para essa nova conta.
5. Selecione **Conectar**.

Em caso de dúvidas ou problemas relacionados à integração, envie um e-mail para support@datagrail.io para pedir ajuda à DataGrail.

