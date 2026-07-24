# Write your MySQL query statement below
select e1.unique_id,f1.name
from Employees f1
left join EmployeeUNI e1
on f1.id = e1.id;