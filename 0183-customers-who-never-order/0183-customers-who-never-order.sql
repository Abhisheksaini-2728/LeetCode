# Write your MySQL query statement below
select f1.name as Customers
from Customers f1
left join Orders a1
on f1.id = a1.customerId
where a1.customerId is null;