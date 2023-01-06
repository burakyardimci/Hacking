# Hacking
 Identify any counterfeits
The PoliTo company wants to create an application capable of tracking the sales of its products in order to identify any counterfeits. The application must analyze the contents of two files. A first file of text products.txt is created by the parent company and contains, for each product manufactured, the identifier of the unique one official dealer who is authorized to sell the product. There are two for each line in the file information (strings separated by a space):

product_id reseller_id
Each product and each seller are identified by a unique alphanumeric code.

A second text file purchases.txt contains information on sales that have been recorded by buyers. The file contains on each line the code of the product purchased and the retailer who managed the delivery.

Since a product can only be sold by the official dealer authorized by the parent company, any purchase of that product by a buyer through an not official retailer must be reported as a suspicion to then allow the parent company to carry out the necessary checks.

The parent company therefore asks you to write a Python program which, after reading the two input files, prints the list of possible suspicious sales. Specifically, for each product sold by one or more non-resellers authorized.