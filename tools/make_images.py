#!/usr/bin/env python3
"""AI 에이전트 안전 사용 설명서 - PIL 기반 이미지 생성 스크립트."""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(os.path.dirname(HERE), "assets")
os.makedirs(ASSETS, exist_ok=True)

BOLD = "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
REG = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"

# 따뜻한 아이보리·살구·브라운 계열
IVORY = (253, 248, 238)
CREAM = (247, 235, 214)
APRICOT = (238, 178, 130)
BROWN = (101, 67, 45)
DARK = (62, 44, 32)
TEAL = (72, 160, 150)
CORAL = (224, 122, 95)
WHITE = (255, 255, 255)
MUTED = (140, 120, 100)
CARD = (255, 252, 246)


def font(path, size):
    return ImageFont.truetype(path, size, index=1)


def text_center(d, cx, y, s, f, fill):
    bb = d.textbbox((0, 0), s, font=f)
    w = bb[2] - bb[0]
    d.text((cx - w / 2 - bb[0], y), s, font=f, fill=fill)


def make_cover():
    W, H = 1000, 1300
    img = Image.new("RGB", (W, H), IVORY)
    d = ImageDraw.Draw(img)
    # 상단 그라데이션
    for y in range(520):
        t = y / 520
        r = int(253 - (253 - 247) * t)
        g = int(248 - (248 - 235) * t)
        b = int(238 - (238 - 214) * t)
        d.line([(0, y), (W, y)], fill=(r, g, b))
    # 장식 원
    d.ellipse([700, 60, 980, 340], fill=(238, 220, 190))
    d.ellipse([-120, 900, 220, 1240], fill=(240, 225, 200))
    # 방패 일러스트 (친근한 애니메이션풍, 무텍스트)
    cx, cy = 500, 830
    # 방패 몸통
    d.polygon([(cx - 130, cy - 110), (cx + 130, cy - 110), (cx + 130, cy + 20),
               (cx, cy + 150), (cx - 130, cy + 20)], fill=TEAL)
    d.polygon([(cx - 130, cy - 110), (cx + 130, cy - 110), (cx + 130, cy + 20),
               (cx, cy + 150), (cx - 130, cy + 20)], outline=BROWN, width=6)
    # 체크 표시
    d.line([(cx - 55, cy - 10), (cx - 10, cy + 35)], fill=WHITE, width=18, joint="curve")
    d.line([(cx - 10, cy + 35), (cx + 65, cy - 55)], fill=WHITE, width=18, joint="curve")
    # 자물쇠 장식
    d.ellipse([cx - 160, cy - 160, cx - 100, cy - 100], fill=APRICOT, outline=BROWN, width=4)
    d.rectangle([cx - 150, cy - 135, cx - 110, cy - 105], fill=BROWN)
    # 체크리스트 카드 장식
    d.rounded_rectangle([cx + 110, cy - 150, cx + 210, cy - 40], radius=12, fill=CARD, outline=BROWN, width=4)
    for i in range(3):
        yy = cy - 130 + i * 32
        d.line([(cx + 125, yy), (cx + 140, yy + 10)], fill=TEAL, width=5)
        d.line([(cx + 140, yy + 10), (cx + 160, yy - 12)], fill=TEAL, width=5)
        d.line([(cx + 168, yy - 2), (cx + 198, yy - 2)], fill=MUTED, width=5)
    # 제목 영역 (그림과 분리)
    text_center(d, W / 2, 120, "AI 에이전트", font(BOLD, 96), DARK)
    text_center(d, W / 2, 240, "안전 사용 설명서", font(BOLD, 96), BROWN)
    text_center(d, W / 2, 380, "개인정보·권한·승인·검증을", font(REG, 44), MUTED)
    text_center(d, W / 2, 440, "처음부터 배우는 실습 교재", font(REG, 44), MUTED)
    text_center(d, W / 2, 1120, "이준수 지음", font(BOLD, 44), DARK)
    text_center(d, W / 2, 1180, "기준일 2026-10-11", font(REG, 34), MUTED)
    img.save(os.path.join(ASSETS, "cover.png"))
    print("cover.png saved")


def concept_card(path, title, rows):
    """개념도 카드 생성. rows: [(라벨, 설명, 색상)]"""
    W, H = 900, 200 + len(rows) * 110
    img = Image.new("RGB", (W, H), CARD)
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([10, 10, W - 10, H - 10], radius=24, outline=BROWN, width=4)
    text_center(d, W / 2, 40, title, font(BOLD, 44), DARK)
    text_center(d, W / 2, 105, "개념도 (실제 화면 아님)", font(REG, 28), MUTED)
    y = 170
    for label, desc, color in rows:
        d.rounded_rectangle([60, y, W - 60, y + 90], radius=16, fill=color)
        d.text((90, y + 14), label, font=font(BOLD, 36), fill=WHITE)
        d.text((90, y + 52), desc, font=font(REG, 28), fill=WHITE)
        y += 110
    img.save(os.path.join(ASSETS, path))
    print(path, "saved")


def make_diagrams():
    concept_card("fig-action-types.png", "AI 행동 네 가지 구분", [
        ("읽기", "자료를 보고 요약한다 · 위험도 낮음", TEAL),
        ("쓰기", "파일이나 일정을 바꾼다 · 위험도 중간", APRICOT),
        ("전송", "외부로 보낸다 · 되돌리기 어려움 · 위험도 높음", CORAL),
        ("삭제", "자료를 지운다 · 위험도 높음", BROWN),
    ])
    concept_card("fig-permission-matrix.png", "연결 권한 최소화", [
        ("읽기 전용", "바꿀 필요가 없는 업무는 읽기만 허용", TEAL),
        ("기간 제한", "프로젝트가 끝나면 연결을 끊는다", APRICOT),
        ("범위 제한", "특정 폴더·문서만 연결한다", CORAL),
    ])
    concept_card("fig-injection.png", "프롬프트 인젝션 개념도", [
        ("사용자 지시", "직접 내린 요청 · 가장 우선", TEAL),
        ("외부 문서", "웹·이메일·문서 속 글 · 참고만 한다", MUTED),
        ("숨은 지시", "문서 속 몰래 심은 명령 · 실행하지 않는다", CORAL),
    ])
    concept_card("fig-response-flow.png", "오류 대응 네 단계", [
        ("1. 즉시 중단", "추가 행동을 시키지 않는다", CORAL),
        ("2. 권한 회수", "연결된 권한을 끊는다", APRICOT),
        ("3. 영향 확인", "무엇이 어디까지 나갔는지 파악", TEAL),
        ("4. 보고와 기록", "알리고 원인과 조치를 기록", BROWN),
    ])


if __name__ == "__main__":
    make_cover()
    make_diagrams()
