# TRD 작성

[English](README.md) | 한국어

## 이 스킬의 목적

제품 요구 사항 문서(PRD)의 보완 문서로 기술 요구 사항 문서(TRD)를 작성하거나 업데이트합니다. 집중적인 질문을 통해 제품 요구 사항을 검증 가능한 기술 동작, 인터페이스, 품질 속성 및 제약 조건으로 구체화합니다. 초안을 작성하려면 PRD가 있어야 합니다. PRD가 없는 경우 먼저 PRD를 작성할지 확인합니다.

이 워크플로는 독자가 기술적 의무와 검증 조건을 쉽게 파악하도록 돕고, 기술적 의미와 사용자가 선택한 언어를 보존합니다. ISO 24495-1의 독자 중심 지침과 영어 문장에 대한 ASD-STE100의 일부 원칙을 참고하지만, 두 표준의 준수나 인증을 주장하지 않습니다. 문장 표현을 별도로 다듬거나 검토할 때는 영어 문서에 `/technical-writing` 스킬을, 한국어 문서에 `/korean-technical-writing` 스킬을 사용할 수 있습니다. 두 스킬도 일부 원칙을 참고하며 표준 준수나 인증을 주장하지 않습니다.

전체 작업 흐름과 사전 요구 사항은 [SKILL.md](SKILL.md)를 참조하십시오.

## GitHub Copilot CLI로 설치

GitHub Copilot CLI를 설치한 뒤 터미널에서 다음 명령을 실행합니다.

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install create-trd@justinyoo-skills
```

마켓플레이스를 이미 등록했다면 첫 번째 명령은 건너뜁니다. 전체 컬렉션을 설치했다면 이 스킬도 포함되어 있습니다.

다른 에이전트, 설치 방법, 로컬 체크아웃에 관한 내용은 [스킬 설치 안내서](../../docs/skills-installation-guide.md)를 참조하십시오.

## 사용법

GitHub Copilot CLI 세션에서 다음과 같이 요청합니다.

```text
/create-trd PRD.md를 바탕으로 TRD를 작성하고 기술적 공백에 관해 인터뷰해 주십시오.
```
