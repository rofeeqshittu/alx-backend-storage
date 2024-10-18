-- Trigger to reset valid_email when email changes

DELIMITER //

CREATE TRIGGER reset_valid_email_on_update
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	-- Only reset valid_email if the email has been changed
	IF OLD.email != NEW.email THEN
		SET NEW.valid_email = 0;
	END IF;
END //

DELIMITER ;
