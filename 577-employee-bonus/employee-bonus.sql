SELECT Employee.name, Bonus.bonus
FROM Employee
LEFT JOIN Bonus
ON Employee.empID = Bonus.empID
WHERE Bonus.bonus IS NULL OR Bonus.bonus < 1000;