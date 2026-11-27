# PowerPoint 템플릿으로 슬라이드 레이아웃 구성

[English](README.md) | 한국어

## 이 스킬의 목적

제공된 문구, 이미지 또는 데이터 차트를 로컬 `.pptx` 또는 `.potx` 템플릿 **한 개**의 기존 레이아웃에 배치합니다. 결과는 요청한 슬라이드만 담은 새 `.pptx` 파일이며, 템플릿의 예시 슬라이드는 포함하지 않습니다. 템플릿이 없으면 브랜딩이 없는 내장 템플릿을 명시적으로 선택할 수 있습니다. 이 스킬은 Python과 `python-pptx` 라이브러리를 사용해 로컬에서 동작합니다. 발표 내용을 작성하거나 새 테마를 디자인하지는 않습니다.

전체 작업 절차, 레이아웃 결정 기준, 배치안 형식과 사전 요구 사항은 [SKILL.md](SKILL.md)를 참조하십시오.

## GitHub Copilot CLI로 설치

GitHub Copilot CLI를 설치한 뒤 터미널에서 다음 명령을 실행합니다.

```sh
copilot plugin marketplace add justinyoo/skills
copilot plugin install pptx-layout@justinyoo-skills
```

마켓플레이스를 이미 등록했다면 첫 번째 명령은 건너뜁니다. 전체 컬렉션을 설치했다면 이 스킬도 포함되어 있습니다.

다른 에이전트, 설치 방법, 로컬 체크아웃에 관한 내용은 [스킬 설치 안내서](../../docs/skills-installation-guide.md)를 참조하십시오.

## 사용법

GitHub Copilot CLI 세션에서 다음과 같이 요청합니다.

```text
/pptx-layout "brand.potx"를 사용해 "이제 운영 배포만 승인이 필요합니다"라는 제목의 슬라이드 한 장을 구성해 주십시오. 빌드, 테스트, 배포를 기준으로 이전과 이후를 비교합니다. 이전에는 세 단계 모두 승인이 필요했고, 이후에는 배포만 승인이 필요합니다. 템플릿의 기존 영역을 사용하고 "approvals.pptx"로 저장해 주십시오.
```
