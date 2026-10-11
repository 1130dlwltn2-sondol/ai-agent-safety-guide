# handoff.md — AI 에이전트 안전 사용 설명서

## 파일 구조

- chapters/01.md ~ 08.md: 장별 원고 (위키독스 게시용)
- pages/: 위키독스 페이지 순서 원고 (00-cover ~ 12-closing, 17개)
- assets/: cover.png (1000x1300), 도식 4종
- project/: 최종 프로젝트 제출물 (README, prompts, results, checklist, references)
- manuscript_full.md: 전체 통합 원고
- references.md: 공식 자료 목록
- QA_REPORT.md: 검증 기록
- tools/make_images.py: 이미지 생성 스크립트 (PIL, Noto CJK)

## 위키독스 업로드 안내

위키독스 공개 게시는 저자의 별도 승인 전에는 하지 않는다. 승인 후:

1. GitHub에 공개 저장소를 만들고 이 폴더의 파일들을 업로드한다.
2. 위키독스에서 GitHub 연동으로 책을 만든다.
3. 웹훅을 등록하고 동기화한다.
4. 목차 구조와 이미지 표시를 확인한 뒤 공개한다.

## 최신 정보 갱신 지점

- [S3] ICO 의견 수렴 마감일: 2026-11-20. 마감 후 결과를 확인해 6장과 참고 자료를 갱신한다.
- 제품별 승인 버튼·설정 화면: 기준일(2026-10-11) 이후 변경 가능. 출판 전 공식 문서를 다시 확인한다.
- [S5] 데이터 관리 설정: 갱신형 문서이므로 출판 전 최신 내용을 확인한다.

## 후속 수정 방법

- 원고 수정: chapters/의 해당 장을 고친 뒤, pages/의 같은 장 파일에도 반영한다.
- 이미지 재생성: tools/make_images.py를 실행한다 (python3 tools/make_images.py).
- 전체 원고 재생성: manuscript_full.md 생성 명령을 QA_REPORT.md 방식대로 다시 실행한다.
