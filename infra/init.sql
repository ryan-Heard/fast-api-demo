-- This script will run automatically when the Docker container is first started.
-- It's a great way to set up your database schema and add initial data.

-- Create the codeusers table to store user information
CREATE TABLE codeusers (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);

-- Insert sample data into the codeusers table
INSERT INTO codeusers (username, email, password_hash) VALUES
('alice', 'alice@example.com', 'hashed_password_1'),
('bob', 'bob@example.com', 'hashed_password_2'),
('charlie', 'charlie@example.com', 'hashed_password_3');
