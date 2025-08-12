-- Membuat database
CREATE DATABASE IF NOT EXISTS assetUniv;
USE assetUniv;

-- 1. Membuat tabel `user_agent`
CREATE TABLE user_agent (
    user_admin_uuid VARCHAR(36) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    time_zone VARCHAR(50),
    role VARCHAR(50)
);

-- 2. Membuat tabel `user_client`
CREATE TABLE user_client (
    user_client_uuid VARCHAR(36) PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(20),
    time_zone VARCHAR(50)
);

-- 3. Membuat tabel `tickets_details`
CREATE TABLE tickets_details (
    assets_details_id INT AUTO_INCREMENT PRIMARY KEY,
    issue_summary VARCHAR(255) NOT NULL,
    issue_details TEXT,
    subject VARCHAR(255) NOT NULL,
    department VARCHAR(255),
    user_admin_uuid VARCHAR(36),
    user_client_uuid VARCHAR(36),
    FOREIGN KEY (user_admin_uuid) REFERENCES user_agent(user_admin_uuid),
    FOREIGN KEY (user_client_uuid) REFERENCES user_client(user_client_uuid)
);

-- 4. Membuat tabel `tickets_status`
CREATE TABLE tickets_status (
    assets_status_id INT AUTO_INCREMENT PRIMARY KEY,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(50),
    assets_details_id INT,
    FOREIGN KEY (assets_details_id) REFERENCES tickets_details(assets_details_id)
);

-- 5. Membuat tabel `help_topics`
CREATE TABLE help_topics (
    help_topics_id INT AUTO_INCREMENT PRIMARY KEY,
    help_description TEXT
);

-- 6. Membuat tabel `knowledgebase`
CREATE TABLE knowledgebase (
    knowledgebase_id INT AUTO_INCREMENT PRIMARY KEY,
    created_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    category VARCHAR(255),
    text TEXT,
    user_admin_uuid VARCHAR(36),
    help_topics_id INT,
    FOREIGN KEY (user_admin_uuid) REFERENCES user_agent(user_admin_uuid),
    FOREIGN KEY (help_topics_id) REFERENCES help_topics(help_topics_id)
);