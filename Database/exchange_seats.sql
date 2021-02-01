/*

Mary is a teacher in a middle school and she has a table seat storing students' names and their corresponding seat ids.

The column id is continuous increment.

Mary wants to change seats for the adjacent students.

Can you write a SQL query to output the result for Mary?

 

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Abbot   |
|    2    | Doris   |
|    3    | Emerson |
|    4    | Green   |
|    5    | Jeames  |
+---------+---------+
For the sample input, the output is:

+---------+---------+
|    id   | student |
+---------+---------+
|    1    | Doris   |
|    2    | Abbot   |
|    3    | Green   |
|    4    | Emerson |
|    5    | Jeames  |
+---------+---------+
Note:

If the number of students is odd, there is no need to change the last one's seat.

*/

# Write your MySQL query statement below

with cte as (
    select id, student, 
        lead(student) over (order by id asc) next_student,
        lag(student) over (order by id asc) prev_student
    from seat
)
select id,
    case when id%2<>0 and id <> (select max(id) from seat)then next_student
        when id%2 = 0 then prev_student 
        when id = (select max(id) from seat) then (select student from seat
                                                   where id = (select max(id) from seat))end as student
from cte        