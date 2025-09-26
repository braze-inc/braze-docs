---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "Este artigo de referência descreve a parceria entre a Braze e o Apteligent, um aplicativo móvel que detalha os relatórios de falhas, permitindo o registro de dados críticos na sua solução da Braze existente."
page_type: partner
search_tag: Partner

---

# Apteligent

> [A Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html) é uma plataforma de performance de aplicativos móveis que fornece ferramentas e insights para desenvolvedores e gerentes de produtos. 

_Essa integração é mantida pela Apteligent._

## Sobre a integração

A integração entre a Braze e a Apteligent fornece relatórios detalhados de falhas no iOS, permitindo o registro de dados críticos na sua solução Braze existente, além de segmentar, entender e engajar os usuários que sofreram falhas no aplicativo.

## Pré-requisitos 

| Requisito | Descrição |
|---|---|
| Conta do TestDrive | É necessário ter uma conta TestDrive para aproveitar essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert warning %}
No momento, essa integração só é compatível com o iOS.
{% endalert %}

## Integração {#apteligent-ios-integration}

### Etapa 1: Registre um observador

Primeiro, você deve registrar um observador. Faça isso antes de inicializar o Apteligent.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### Etapa 2: Registre análises personalizadas de dados de falhas

O SDK do Apteligent disparará uma notificação quando o usuário carregar a aplicação após uma falha. A notificação conterá o nome, o motivo e a data de ocorrência da falha.

Ao receber a notificação, registre um evento personalizado de falha e atualize os atributos do usuário com a análise de dados de relatórios de falhas da Apteligent:

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

Depois de concluído, você poderá aproveitar o poder da segmentação do Braze e da análise de dados de engajamento usando as informações sobre acidentes encontradas na plataforma Apteligent.

