-- script that creates a stored procedure AddBonus that adds a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name varchar(255), IN score INT)
BEGIN
	IF (SELECT id from projects WHERE name = project_name) IS NULL THEN
		INSERT INTO projects(id, name) VALUES (DEFAULT, project_name);
	END IF;
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END $$
DELIMITER ;