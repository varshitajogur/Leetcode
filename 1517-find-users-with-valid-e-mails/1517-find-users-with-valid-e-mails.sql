SELECT user_id, name, mail
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9._-]*@leetcode\\.com$'
  AND BINARY mail LIKE '%@leetcode.com';