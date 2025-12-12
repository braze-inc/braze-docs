---
nav_title: API 네트워크 연결 문제
article_title: API 네트워크 연결 문제
page_order: 4
description: "이 참조 문서에서는 API 연결 문제와 문제 해결 방법에 대해 설명합니다."
page_type: reference

---

# API 네트워크 연결 문제

> 이 참조 문서에서는 API 연결 문제와 문제 해결 방법에 대해 설명합니다.

Braze API 엔드포인트는 DNS 정보를 기반으로 가장 가까운 POP로 트래픽을 라우팅하는 CDN을 사용합니다.  연결에 문제가 있거나 효율적이지 않은 POP에 연결된 경우 제공업체의 DNS 서버 또는 서버와 동일한 데이터 센터에 설정되어 있고 적절한 IP 위치 메타 정보가 연결된 제공업체의 DNS 서버를 사용해야 합니다.

소수의 방화벽이 Braze API 엔드포인트에 대한 연결을 방해하는 HTTPS/TLS 트래픽을 수정하거나 보호하려고 시도하는 것을 발견했습니다. 서버가 물리적 방화벽 뒤에 있는 경우 방화벽이나 라우터가 수행하는 HTTPS/TLS 가속 또는 수정을 비활성화하세요. 또한 CDN 제공업체에 아웃바운드 트래픽을 허용 목록에 추가하여(Fastly.com) 문제가 해결되는지 확인할 수 있습니다.

간혹 SYN/ACK/RST 패킷을 필터링하는 설정으로 인해 문제가 발생할 수 있으므로 호스트에서 iptables를 사용하는 경우 CDN 제공업체(Fastly.com)로 아웃바운드 트래픽을 허용 목록에 추가하여 문제가 해결되는지 확인할 수 있습니다.

Braze API 엔드포인트에 연결하는 데 여전히 네트워크 문제가 있는 경우 [MTR 테스트](https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2)와 문제가 발생한 동안 [Fastly Debug](http://www.fastly-debug.com/) 결과를 제공하고 지원 요청과 함께 제출하세요. 테스트 결과는 개발 머신이 아닌 Braze API 엔드포인트에 연결하는 데 문제가 있는 서버에서 얻어야 한다는 점에 유의하세요. 네트워크 캡처(tcpdump 또는 .pcap 파일)를 얻을 수 있다면 도움이 될 것입니다.

MTR에 대한 자세한 내용은 운영 체제에 따라 다음 리소스를 참조하세요:

- [GNU/Linux](https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues)
- [macOS](https://formulae.brew.sh/formula/mtr)

## Braze API 엔드포인트 IP 범위 허용 목록 추가하기

방화벽을 통해 Braze API 엔드포인트를 허용 목록에 추가하기 위해, 저희 CDN은 JSON 덤프를 통해 할당된 IP 범위 목록에 대한 액세스를 제공합니다. Braze API IP 범위 목록은 [Fastly 퍼블릭 IP 목록](https://api.fastly.com/public-ip-list)과 [Cloudflare 퍼블릭 IP](https://api.cloudflare.com/client/v4/ips) 목록을 모두 참조하세요. 이러한 IP는 변경될 수 있습니다.

