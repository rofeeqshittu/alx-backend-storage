-- Creates a SQL func SafeDiv that divides 2 integers
DELIMIER //
CREATE FUNCTION SafeDiv(
	a INT,
	b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
	-- Check if b is 0, return 0 if true, else return a / b
	IF b = 0 THEN
		RETURN 0;
	ELSE
		RETURN a / b;
	END IF
END //
DELIMITER ;
