---
nav_title: Autenticação de e-mail
article_title: Autenticação de E-mail
page_order: 2
page_type: reference
description: "Este artigo de referência cobre a autenticação de e-mail, uma coleção de técnicas destinadas a equipar seu e-mail com informações verificáveis sobre sua origem."
channel: email

---

# Autenticação de e-mail

> A autenticação de e-mail é uma coleção de técnicas que equipam seus e-mails com informações verificáveis sobre sua origem.<br><br>A autenticação adequada é crucial para que os provedores de serviços de internet (ISPs) o reconheçam como um remetente de e-mails desejáveis e entreguem sua correspondência imediatamente. Sem autenticação, sua divulgação é presumida como fraudulenta. 

## Métodos de autenticação

### Sender Policy Framework (SPF)

Este método confirma que o endereço IP de envio de e-mail da Braze está autorizado a enviar e-mails em seu nome. O SPF é sua autenticação básica e é realizado publicando os registros de texto nas configurações de DNS. O servidor receptor verificará os registros DNS e determinará se são autênticos. Este método é projetado para validar o remetente do e-mail.

Seu registro SPF será configurado quando a Braze configurar seus IPs e domínios - além de adicionar os registros DNS que fornecemos, nenhuma ação adicional é necessária.

### Domain Keys Identified Mail (DKIM)

Este método confirma que seu domínio de envio de e-mail da Braze está autorizado a enviar e-mails em seu nome. Este método é projetado para validar a autenticidade do remetente e valida que a integridade da mensagem é preservada. Ele também usa assinaturas digitais criptográficas individuais para que os ISPs possam ter certeza de que o e-mail que estão entregando é o mesmo que você enviou.

A Braze assina o e-mail com sua chave privada secreta. Os ISPs verificam a assinatura contra sua chave pública, que é armazenada em seu registro DNS personalizado. Nenhuma duas assinaturas são exatamente iguais, e apenas sua chave pública pode verificar com sucesso a assinatura da sua chave privada.

Seu registro DKIM será configurado quando a Braze configurar seus IPs e domínios - além de adicionar os registros DNS que fornecemos, nenhuma ação adicional é necessária.

### Autenticação de Mensagens Baseada em Domínio, Relatórios e Conformidade (DMARC)

[Autenticação de Mensagens Baseada em Domínio, Relatórios & Conformidade (DMARC)](https://dmarc.org/) é um protocolo de autenticação de e-mail para remetentes de e-mail provarem a legitimidade de seu correio, o que permite confiança do receptor da caixa de entrada e incentiva a aceitação de e-mails. O DMARC permite que os remetentes de e-mail especifiquem como lidar com e-mails que não foram autenticados usando o Sender Policy Framework (SPF) ou o Domain Keys Identified Mail (DKIM). Isso é alcançado verificando se tanto as verificações de SPF quanto de DKIM foram aprovadas. 

Os remetentes podem instruir os provedores de caixa de entrada sobre como devem lidar com e-mails que falharam em suas verificações de assinatura ou autenticação. Falhas podem indicar que outros estão tentando imitar você ou seu e-mail. Os remetentes podem informar aos provedores de caixa de entrada para rejeitar ou colocar em quarentena e-mails e até enviar relatórios automatizados sobre e-mails que falham nas verificações. Ao fazer isso, os provedores de caixa de entrada podem identificar melhor spammers e prevenir e-mails maliciosos de invadir as caixas de entrada, minimizando falsos positivos e fornecendo melhores relatórios de autenticação para maior transparência no mercado.

#### Como funciona

Para implantar o DMARC, você precisa publicar um Registro DMARC no seu Sistema de Nomes de Domínio (DNS). Este é um registro TXT que expressa publicamente a política do seu domínio de e-mail após verificar o status de SPF e DKIM. O DMARC autentica se o SPF ou o DKIM, ou ambos, passam. Isso é referido como Alinhamento DMARC.

Um registro DMARC também informa aos servidores de e-mail para enviar relatórios XML de volta para o endereço de e-mail de relatório listado no registro DMARC. Esses relatórios fornecem insights sobre como seu e-mail está se movendo pelo ecossistema e permitem que você identifique tudo que está tentando usar seu domínio de e-mail para enviar comunicações por e-mail.

A política que você tem em seu registro DMARC informará ao servidor de e-mail do destinatário participante o que fazer com e-mails que não passam no SPF e DKIM, mas afirmam ser do seu domínio. A Braze recomenda definir uma política DMARC no domínio raiz, que será aplicada a todos os subdomínios. Isso significa que nenhuma configuração adicional será necessária em quaisquer subdomínios atuais e novos no futuro. Existem três tipos de políticas que você pode definir:

| Política | Impacto |
| --- | --- |
| Nenhum | Diga ao provedor de caixa de entrada para não realizar ações contra mensagens que falham. |
| Quarentena | Diga ao provedor de caixa de entrada para enviar mensagens que falham para a pasta de spam. |
| Rejeitar | Diga ao provedor de caixa de entrada que mensagens que falham irão para a pasta de spam e devem ser bloqueadas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Como verificar a autenticação DMARC do seu domínio

Existem duas opções para verificar a autenticação DMARC do seu domínio:

- **Opção 1:** Você pode inserir seu domínio pai ou subdomínio em qualquer verificador DMARC de terceiros, como [MXToolbox](https://mxtoolbox.com/dmarc.aspx), para auditar se você tem uma política DMARC em vigor e qual é essa política.
    - **MXToolbox**: Se você definir seu DMARC como o domínio raiz, insira isso no MXToolbox. Se você definir o DMARC no subdomínio, insira o subdomínio no MXToolbox. Esteja ciente de que o MXToolbox não "procura para cima ou para baixo" ao realizar buscas. Isso significa que se você definir o DMARC no domínio raiz e inserir o subdomínio, o MXToolbox mostrará uma falha, pois não sabe que o DMARC foi definido no domínio raiz.
- **Opção 2:** Abra um e-mail do seu domínio ou subdomínio na sua caixa de entrada e encontre a mensagem original para verificar se o DMARC está passando a autenticação neste e-mail.

Por exemplo, se você estiver usando o Gmail, siga estas etapas:

1. Clique no **Mais** <i class="fa-solid fa-ellipsis"></i> em uma mensagem de email.
2. Selecione **Mostrar original**.
3. Verifique se você tem um status "PASS" para **DMARC**.

\![Um email que tem "PASS" como o valor DMARC.]({% image_buster /assets/img_archive/dmarc_example.png %})

