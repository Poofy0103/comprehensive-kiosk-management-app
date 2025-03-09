DROP PROCEDURE IF EXISTS kioskapp.usp_create_a_new_user;

DELIMITER $$
$$
CREATE PROCEDURE usp_create_a_new_user(
	IN p_name VARCHAR(100),
	IN p_email VARCHAR(100),
	IN p_username VARCHAR(20),
	IN p_password VARCHAR(128),
	IN p_hashAlgorithm VARCHAR(12))
BEGIN
	DECLARE randomSalt VARCHAR(100) DEFAULT 'kioskAdminApp';
	DECLARE hashAlgorithmID INT;

	SET @randomSalt = CONCAT('kioskAdminApp', SUBSTRING(MD5(RAND()), 1, 8));

	SET @hashAlgorithmID = (SELECT ID FROM hashingalgorithm WHERE Name = p_hashAlgorithm);

	IF @hashAlgorithmID IS NULL THEN
		SIGNAL SQLSTATE '45000'
		SET MESSAGE_TEXT = 'Invalid hashing algorithm';
	END IF;

	IF p_hashAlgorithm = 'sha256' THEN
		INSERT INTO `user` (HashingAlgorithmID, Name, Email, Username, PasswordHash, PasswordSalt)
		VALUES (@hashAlgorithmID, p_name, p_email, p_username, SHA2(CONCAT(p_password, @randomSalt), 256), @randomSalt);
	END IF;
END$$
DELIMITER ;
