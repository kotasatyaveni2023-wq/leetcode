# Write your MySQL query statement below
select Employee.name,Bonus.bonus from Employee left join Bonus
on Employee.empid=Bonus.empId
where bonus<1000 or Bonus is NULL;