---
nav_title: API 네트워크 연결 문제
article_title: API 네트워크 연결 문제
page_order: 4
description: "이 참조 문서에서는 API 연결 문제와 문제 해결 방법을 다룹니다."
page_type: reference

---

# API 네트워크 연결 문제

> 이 참조 문서에서는 API 연결 문제와 문제 해결 방법을 다룹니다.

Braze API 엔드포인트는 DNS 정보를 기반으로 가장 가까운 POP로 트래픽을 라우팅하는 CDN을 사용합니다.  연결에 문제가 있거나 효율적이지 않은 POP에 연결된 경우 제공업체의 DNS 서버 또는 서버와 동일한 데이터 센터에 설정되어 있고 적절한 IP 위치 메타 정보가 연결된 제공업체의 DNS 서버를 사용해야 합니다.

일부 방화벽이 HTTPS를 수정하거나 보호하려고 시도하는 것으로 나타났습니다/TLS traffic which interferes with connections to Braze API endpoints. If your servers are behind any sort of physical firewall, disable any HTTPS/TLS acceleration or modifications that the firewall or router is performing. Additionally, you can allowlist outbound traffic to our CDN providers (Fastly.com) to see if that resolves the issue.

경우에 따라 SYN에서 필터링하는 iptables 설정은/ACK/RST packets can also cause issues, so if you are using iptables on your host you could also allowlist outbound traffic to our CDN providers (Fastly.com) to see if that resolves the issue.

Braze API 엔드포인트에 연결하는 데 여전히 네트워크 문제가 있는 경우 [MTR 테스트][1]와 문제가 발생한 동안 [Fastly Debug][2] 결과를 제공하고 지원 요청과 함께 제출하세요. 테스트 결과는 개발 컴퓨터가 아닌 Braze API 엔드포인트에 연결하는 데 문제가 있는 서버에서 가져와야 한다는 점에 유의하세요. 네트워크 캡처(tcpdump 또는.pcap 파일)를 얻을 수 있다면 유용할 것입니다.

MTR에 대한 자세한 내용은 운영 체제에 따른 다음 리소스를 확인하세요.

- [GNU/Linux][4]
- [macOS][5]

## Braze API 엔드포인트 IP 범위 허용 목록

방화벽을 통해 Braze API 엔드포인트를 허용 목록에 추가하기 위해 CDN은 JSON 덤프를 통해 할당된 IP 범위 목록에 대한 액세스를 제공합니다. Braze API IP 범위 목록은 [Fastly 퍼블릭 IP 목록][3]과 [Cloudflare 퍼블릭 IP][6] 목록을 모두 참조하세요. 참고로 이러한 IP는 변경될 수 있습니다.

[1]: https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2
[2]: http://www.fastly-debug.com/
[3]: https://api.fastly.com/public-ip-list
[4]: https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues
[5]: https://formulae.brew.sh/formula/mtr
[6]: https://api.cloudflare.com/client/v4/ips
