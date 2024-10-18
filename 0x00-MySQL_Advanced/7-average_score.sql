-- Create stored procedure ComputerAverageScoreForUser
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (
	IN user_id INT
)
BEGIN
	DECLARE avg_score FLOAT;

	-- Compute the average score for the user
	SELECT AVG(score) INTO avg_score
	FROM corrections
	WHERE corrections.user_id = user_id;

	-- Update the user's average_score
	UPDATE users
	SET users.average_score = avg_score
	WHERE users.id = user_id;
END //
DELIMITER ;
