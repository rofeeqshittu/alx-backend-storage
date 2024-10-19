-- Creates a procedure ComputeAverageWeightedScoreForUsers
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	-- Update the average_score for each user based on their total weighted score and total weight
	UPDATE users u
	SET u.average_score = (
		SELECT IFNULL(SUM(c.score * p.weight) / SUM(p.weight), 0)
		FROM corrections c
		JOIN projects p ON c.project_id = p.id
		WHERE c.user_id = u.id
	);
END //
DELIMITER ;
