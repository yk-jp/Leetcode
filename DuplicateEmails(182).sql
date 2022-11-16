SELECT email as Email FROM Person
GROUP BY Email
HAVING count(Email) > 1;