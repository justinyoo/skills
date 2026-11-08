# 현지화

[English](README.md) | 한국어

## 이 스킬의 목적

스킬의 로케일 규칙에서 지원하는 대상 로케일에 맞게 프로젝트의 루트 README와 Markdown 문서를 현지화합니다. Markdown 구조, 코드, 링크를 보존하고 번역 품질을 검토합니다. 저장해 둔 원문 사본을 기준으로 변경된 콘텐츠를 업데이트하되, 변경되지 않은 섹션은 불필요하게 다시 번역하지 않습니다.

전체 작업 흐름과 사전 요구 사항은 [SKILL.md](SKILL.md)를 참조하십시오.

## GitHub Copilot CLI로 설치

GitHub Copilot CLI를 설치한 뒤 터미널에서 다음 명령을 실행합니다.

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install localizations@justinyoo-skills
```

마켓플레이스를 이미 등록했다면 첫 번째 명령은 건너뜁니다. 전체 컬렉션을 설치했다면 이 스킬도 포함되어 있습니다.

다른 에이전트, 설치 방법, 로컬 체크아웃에 관한 내용은 [스킬 설치 안내서](../../docs/skills-installation-guide.md)를 참조하십시오.

## 사용법

GitHub Copilot CLI 세션에서 다음과 같이 요청합니다.

```text
/localizations 이 프로젝트의 README.md와 docs 디렉터리를 지원되는 모든 로케일로 현지화해 주십시오.
```
