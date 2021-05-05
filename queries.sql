Queries
1.
/* Select the full name and item count of customers with more than 1 item in the cart*/

SELECT (p.firstname, p.lastname) as name, k.productcount as items
from people as p
INNER JOIN customer as c on c.personid = p.personid
INNER JOIN cart as k on k.customerid = c.customerid