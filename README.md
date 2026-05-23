# 🎵 YT Audio Extractor — PWA

YouTube 음원 추출 커맨드 생성기 **Progressive Web App**

> GitHub Pages 링크 하나로 Android/iOS 홈 화면에 앱처럼 설치 가능!

---

## 📱 설치 방법 (사용자)

1. 아래 링크를 **Android Chrome** 또는 **iOS Safari**로 열기
   ```
   https://your-username.github.io/yt-audio-pwa
   ```
2. 브라우저 하단 **"홈 화면에 추가"** 또는 배너의 **"설치"** 버튼 클릭
3. 완료! 일반 앱처럼 아이콘으로 실행 가능 🎉

---

## 🚀 GitHub Pages 배포 (개발자)

### 1단계 — 레포 생성 & 파일 업로드
```bash
git init
git add .
git commit -m "init: YT Audio PWA"
git remote add origin https://github.com/your-username/yt-audio-pwa.git
git push -u origin main
```

### 2단계 — GitHub Pages 활성화
- 레포 **Settings → Pages**
- Source: **Deploy from a branch**
- Branch: `main` / `/ (root)`
- **Save** 클릭

### 3단계 — 배포 확인
약 1~2분 후 아래 URL에서 접속:
```
https://your-username.github.io/yt-audio-pwa
```

---

## 🗂 파일 구조

```
yt-audio-pwa/
├── index.html          # 메인 앱 (PWA)
├── manifest.json       # PWA 설정 (앱 이름, 아이콘, 색상)
├── sw.js               # Service Worker (오프라인 지원)
├── generate_icons.py   # 아이콘 자동 생성 스크립트
├── icons/
│   ├── icon-192.png    # 앱 아이콘 (소)
│   └── icon-512.png    # 앱 아이콘 (대)
└── README.md
```

---

## 🎨 아이콘 생성

```bash
pip install Pillow
python generate_icons.py
```

---

## ✨ PWA 기능

| 기능 | 설명 |
|------|------|
| 홈 화면 설치 | 앱처럼 아이콘 추가 |
| 오프라인 지원 | 캐시로 인터넷 없이도 실행 |
| 전체화면 | 주소바 없는 네이티브 앱 느낌 |
| 설치 배너 | 자동으로 설치 유도 |

---

## ⚠️ 주의사항

저작권이 있는 콘텐츠는 개인 용도로만 사용하세요.

---

MIT License
