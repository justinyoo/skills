# TDD 작성

[English](README.md) | 한국어

## 이 스킬의 목적

제품 요구 사항 문서(PRD)와 기술 요구 사항 문서(TRD)를 바탕으로 기술 설계 문서(TDD)를 작성하거나 업데이트합니다. 사용 가능한 맥락을 조사하고, 장단점이 있는 솔루션을 제안하며, 요구 사항을 충족하는 설계를 발전시키기 위해 구체적인 질문을 합니다. 초안을 작성하려면 PRD와 TRD가 모두 필요합니다. 여기서 TDD는 테스트 주도 개발이 아니라 기술 설계 문서를 뜻합니다.

이 워크플로는 독자가 메커니즘, 책임, 설계 결정을 파악하도록 돕고, 기술적 의미와 사용자가 선택한 언어를 보존합니다. ISO 24495-1의 독자 중심 지침과 영어 문장에 대한 ASD-STE100의 일부 원칙을 참고하지만, 두 표준의 준수나 인증을 주장하지 않습니다. 문장 표현을 별도로 다듬거나 검토할 때는 영어 문서에 `/technical-writing` 스킬을, 한국어 문서에 `/korean-technical-writing` 스킬을 사용할 수 있습니다. 두 스킬도 일부 원칙을 참고하며 표준 준수나 인증을 주장하지 않습니다.

전체 작업 흐름과 사전 요구 사항은 [SKILL.md](SKILL.md)를 참조하십시오.

## GitHub Copilot CLI로 설치

GitHub Copilot CLI를 설치한 뒤 터미널에서 다음 명령을 실행합니다.

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install create-tdd@justinyoo-skills
```

마켓플레이스를 이미 등록했다면 첫 번째 명령은 건너뜁니다. 전체 컬렉션을 설치했다면 이 스킬도 포함되어 있습니다.

다른 에이전트, 설치 방법, 로컬 체크아웃에 관한 내용은 [스킬 설치 안내서](../../docs/skills-installation-guide.md)를 참조하십시오.

## 사용법

GitHub Copilot CLI 세션에서 다음과 같이 요청합니다.

```text
/create-tdd 기존 코드를 활용해 PRD.md와 TRD.md의 솔루션을 설계해 주십시오.
```
