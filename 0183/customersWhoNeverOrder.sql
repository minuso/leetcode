Select Name as Customers
from Customers
where Id not in (Select Distinct CustomerId from Orders)