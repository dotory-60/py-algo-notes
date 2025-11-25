SET NAMES utf8mb4;
SET CHARACTER SET utf8mb4;

CREATE TABLE IF NOT EXISTS schedules (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    start_datetime DATETIME NOT NULL,
    end_datetime DATETIME,
    is_completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

INSERT INTO schedules (title, description, start_datetime, end_datetime, is_completed)
VALUES
('팀 회의', '주간 진행 상황 공유', '2025-01-10 09:00:00', '2025-01-10 10:00:00', FALSE),
('프로젝트 기획', '요구사항 정리 및 일정 확정', '2025-01-11 13:00:00', '2025-01-11 15:00:00', FALSE),
('운동', '웨이트 트레이닝 하체 위주', '2025-01-12 18:00:00', NULL, FALSE),
('독서', '기술 서적 1장 읽기', '2025-01-13 20:00:00', NULL, FALSE),
('병원 진료', '정기 검진', '2025-01-14 10:00:00', '2025-01-14 10:30:00', TRUE),
('스터디', '알고리즘 문제 풀이', '2025-01-15 19:00:00', '2025-01-15 21:00:00', FALSE),
('장보기', '식재료 구매', '2025-01-16 17:00:00', NULL, TRUE),
('친구 약속', '저녁 식사 모임', '2025-01-17 19:00:00', '2025-01-17 21:00:00', FALSE),
('출근', '업무 일정 체크', '2025-01-18 09:00:00', NULL, TRUE),
('퇴근', '업무 마무리', '2025-01-18 18:00:00', NULL, TRUE),
('헬스', '상체 운동', '2025-01-19 18:30:00', NULL, FALSE),
('강의 수강', 'FastAPI 강의 1시간', '2025-01-19 21:00:00', NULL, FALSE),
('코딩 테스트 준비', '프로그래머스 문제 풀기', '2025-01-20 20:00:00', NULL, FALSE),
('산책', '집 근처 30분 걷기', '2025-01-21 18:00:00', '2025-01-21 18:30:00', FALSE),
('회의', '디자인팀 협업 미팅', '2025-01-22 14:00:00', '2025-01-22 15:30:00', FALSE),
('블로그 글 작성', '기술 블로그 초안 작성', '2025-01-23 20:00:00', NULL, FALSE),
('집 청소', '방 정리 및 청소기 돌리기', '2025-01-24 16:00:00', NULL, TRUE),
('요리', '파스타 만들기', '2025-01-25 18:00:00', NULL, FALSE),
('가족 모임', '부모님과 저녁 식사', '2025-01-26 17:30:00', '2025-01-26 20:00:00', FALSE),
('휴식', '넷플릭스 시청', '2025-01-27 21:00:00', NULL, FALSE);
