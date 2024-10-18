-- Creates a trigger to update the quantity of items after placing an order

DELIMITER //

CREATE TRIGGER update_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	-- Update the items table: reduce the quantity of the ordered item
	UPDATE items
	SET quantity = quantity - NEW.number -- substract the ordered quantity
	WHERE name = NEW.item_name;
END //

DELIMITER ;
