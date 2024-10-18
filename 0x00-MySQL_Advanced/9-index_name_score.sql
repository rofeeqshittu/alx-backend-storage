-- Creates an index on both the first letter of the name & the score
CREATE INDEX idx_name_first_score ON names (name(1), score);
