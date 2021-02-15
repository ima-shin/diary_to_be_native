/*** テーブル作成SQL ***/

/* テーブル作成 */
CREATE TABLE diaries (
    id VARCHAR(36) PRIMARY KEY,
    content LONGTEXT DEFAULT NULL,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
)