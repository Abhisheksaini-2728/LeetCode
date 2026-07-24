# Write your MySQL query statement below
select t1.firstName,t1.lastName,a1.city,state
from Person t1
left join Address a1
on t1.personId = a1.personId;
