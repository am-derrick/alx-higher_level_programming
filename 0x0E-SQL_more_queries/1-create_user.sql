-- creates user user_0d_1
-- password set to user_0d_1_pwd

CREATE USER IF NOT EXISTS user_0d_1'@'localhost IDENTIFIED BY user_0d_1_pwd;
GRANT PRIVILEGES *.* TO user_0d_1@localhost;
