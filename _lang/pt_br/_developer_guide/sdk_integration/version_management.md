---
page_order: 10
nav_title: Gerenciamento de versões
article_title: Sobre o gerenciamento de versões para o SDK do Braze
description: "Saiba sobre o gerenciamento de versões para o SDK do Braze."
---

# Sobre o gerenciamento de versões

> Saiba sobre o gerenciamento de versões para o SDK do Braze, para que seu app possa ficar atualizado com os últimos recursos e melhorias de qualidade. Como versões mais antigas do SDK podem não receber o último patch, correções de bugs ou suporte, recomendamos sempre mantê-lo atualizado como parte do seu ciclo de desenvolvimento contínuo.

## Recomendações de versionamento

Todos os SDKs do Braze seguem a [Especificação de Versionamento Semântico (SemVer)](https://semver.org/), então, dado um número de versão `MAJOR.MINOR.PATCH`, recomendamos o seguinte:

|versão|Sobre esta versão|Recomendação|
|-------|------------------|--------------|
| `PATCH` | As atualizações são sempre não disruptivas e incluem correções de bugs importantes. Elas sempre serão seguras. | Você deve sempre tentar atualizar para a versão de patch mais recente da sua versão principal e secundária atual imediatamente. |
| `MINOR` | As atualizações são sempre não disruptivas e incluem novas funcionalidades. Elas nunca exigirão mudanças no código da sua aplicação. | Embora você não precise fazer isso imediatamente, deve atualizar para a versão menor mais recente da sua versão principal atual o mais rápido possível. 
| `MAJOR` | As atualizações são mudanças disruptivas e podem exigir mudanças no código da sua aplicação. | Como isso pode exigir mudanças no código, atualize para a versão principal mais recente em um período que funcione melhor para sua equipe. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert note %}
Às vezes, novas atualizações do Android ou do iOS da Apple exigem mudanças no SDK do Braze. Para garantir que seu app seja compatível com telefones mais novos, é importante que você mantenha seu SDK atualizado.
{% endalert %}

## Sobre problemas conhecidos

Para garantir que nossas mudanças não quebrem suas pipelines de build, **nunca alteraremos ou removeremos uma versão depois que ela for publicada em um sistema de distribuição**—mesmo que essa versão específica tenha problemas conhecidos.

Nesses casos, documentaremos o problema no [changelog do SDK Braze]({{site.baseurl}}/developer_guide/changelogs/), e então lançaremos um novo patch para as versões principais ou secundárias impactadas o mais rápido possível.
