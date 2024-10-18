-- Creates a procedure ComputeAverageWeightedScoreForUsers
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE done INT DEFAULT 0; 
	DECLARE current_user_id INT;

	-- Declare a cursor to iterate through all users
	DECLARE user_cursor CURSOR FOR
		SELECT id FROM users;

	-- Declare a handler to handle the end of the cursor
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	-- Open the cursor
	OPEN user_cursor;

	-- Loop through each user
	user_loop: LOOP
		-- Fetch the next user ID from the cursor
		FETCH user_cursor INTO current_user_id;

		-- If there are no more users, exit the loop
		IF done THEN
			LEAVE user_loop;
		END IF;

		-- Call the previously created procedure to compute the average weighted score for the current user
		CALL ComputeAverageWeightedScoreForUser(current_user_id);

	END LOOP;

	-- Close the cursor
	CLOSE user_cursor;

END //
DELIMITER ;
