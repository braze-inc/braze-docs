---
nav_title: Autenticação de e-mail
article_title: Autenticação de e-mail
page_order: 2
page_type: reference
description: "Este artigo de referência aborda a autenticação de e-mail, um conjunto de técnicas destinadas a equipar seu e-mail com informações verificáveis sobre sua origem."
channel: email

---

# Autenticação de e-mail

> A autenticação de e-mail é um conjunto de técnicas que equipam seus e-mails com informações verificáveis sobre sua origem.<br><br>A autenticação adequada é crucial para que os provedores de acesso à internet (ISPs) o reconheçam como remetente de e-mails desejáveis e entreguem seus e-mails imediatamente. Sem autenticação, presume-se que seu alcance seja fraudulento. 

## Métodos de autenticação

### Sender Policy Framework (SPF)

Esse método confirma que seu endereço IP de envio de e-mail do Braze está autorizado a enviar e-mails em seu nome. O SPF é a autenticação básica e é realizado por meio da publicação dos registros de texto nas configurações de DNS. O servidor receptor verificará os registros DNS e determinará se eles são autênticos. Esse método foi criado para validar o remetente do e-mail.

A Braze configura seu registro SPF quando configuramos seus IPs e domínios. Além de adicionar os registros DNS que fornecemos, você não precisa tomar mais nenhuma ação.

### Domain Keys Identified Mail (DKIM)

Esse método confirma que seu domínio de envio de e-mail do Braze está autorizado a enviar e-mails em seu nome. Esse método foi projetado para validar a autenticidade do remetente e validar a preservação da integridade da mensagem. Ele também usa assinaturas digitais criptográficas individuais para que os provedores de acesso à internet possam ter certeza de que o e-mail que estão entregando é o mesmo que você enviou.

A Braze faz o login no e-mail com sua chave privada secreta. Os provedores de acesso à internet verificam a assinatura em relação à sua chave pública, que está armazenada no seu registro DNS personalizado. Não há duas assinaturas exatamente iguais, e somente a sua chave pública pode verificar com êxito a assinatura da sua chave privada.

A Braze configura seu registro DKIM quando configuramos seus IPs e domínios. Além de adicionar os registros DNS que fornecemos, você não precisa tomar mais nenhuma ação.

### Autenticação, relatório e conformidade de mensagens baseadas em domínio (DMARC)

[Autenticação de Mensagem Baseada em Domínio, Relatório & Conformidade (DMARC)](https://dmarc.org/) é um protocolo de autenticação de e-mail para remetentes de e-mail provarem a legitimidade de seu correio, o que permite confiança do receptor da caixa de entrada e incentiva a aceitação do correio. O DMARC permite que os remetentes de e-mail especifiquem como lidar com os e-mails que não foram autenticados usando o Sender Policy Framework (SPF) ou o Domain Keys Identified Mail (DKIM). Isso é feito verificando se as verificações SPF e DKIM foram aprovadas. 

Os remetentes instruem os provedores de caixa de entrada sobre como lidar com e-mails que falham em verificações de assinatura ou autenticação. Falhas podem indicar falsificação. Você pode instruir os provedores a rejeitar ou colocar em quarentena e-mails que falham e enviar relatórios automatizados. Isso ajuda os provedores a identificar spammers, bloquear e-mails maliciosos, minimizar falsos positivos e melhorar a transparência dos relatórios de autenticação.

#### Como funciona?

Para implementar o DMARC, é necessário publicar um registro DMARC no DNS (Domain Naming System). Esse é um registro TXT que expressa publicamente a política do seu domínio de e-mail após verificar o status do SPF e do DKIM. O DMARC autentica se o SPF ou o DKIM, ou ambos, forem aprovados. Isso é chamado de Alinhamento DMARC.

Um registro DMARC também diz aos servidores de e-mail para enviar relatórios XML de volta ao endereço de e-mail de relatório listado no registro DMARC. Esses relatórios fornecem insight sobre como seu e-mail está se movendo pelo ecossistema e permitem identificar tudo o que está tentando usar seu domínio de e-mail para enviar comunicações por e-mail.

Defina uma política DMARC no domínio raiz para que se aplique a todos os subdomínios. Isso evita configurações adicionais em subdomínios atuais e futuros. Você pode definir uma das seguintes políticas:

| Política | Impacto |
| --- | --- |
| Nenhuma | Diga ao provedor de caixa de e-mail para não executar nenhuma ação em relação às mensagens que falharem. |
| Quarentena | Diga ao provedor de caixa de e-mail para enviar as mensagens que falharem para a pasta de spam. |
| Rejeitar | Informe ao provedor de caixa de e-mail que as mensagens que falharem irão para a pasta de spam e deverão ser bloqueadas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Como verificar a autenticação DMARC do seu domínio

Há duas opções para verificar a autenticação DMARC de seu domínio:

- **Opção 1:** Você pode inserir seu domínio ou subdomínio principal em qualquer verificador DMARC de terceiros, como o [MXToolbox](https://mxtoolbox.com/dmarc.aspx), para auditar se você tem uma política DMARC em vigor e qual é a configuração dessa política.
    - **MXToolbox**: Se você definir seu DMARC como o domínio raiz, insira isso no MXToolbox. Se você definir o DMARC no subdomínio, insira o subdomínio no MXToolbox. Esteja ciente de que o MXToolbox não "olha para cima ou para baixo" ao realizar pesquisas. Isso significa que se você definir o DMARC no domínio raiz e inserir o subdomínio, o MXToolbox mostrará uma falha, pois não sabe que o DMARC foi definido no domínio raiz.
- **Opção 2:** Abra um e-mail de seu domínio ou subdomínio em sua caixa de correio e localize a mensagem original para verificar se o DMARC está passando a autenticação nesse e-mail.

Por exemplo, se estiver usando o Gmail, siga estas etapas:

1. Clique em **More (Mais)** <i class="fa-solid fa-ellipsis"></i> em uma mensagem de e-mail.
2. Selecione **Mostrar original**.
3. Verifique se você tem um status "PASS" para **DMARC**.

![Um e-mail que tem "PASS" como valor DMARC.]({% image_buster /assets/img_archive/dmarc_example.png %})

