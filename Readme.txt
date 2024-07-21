XYZ Company

This company operates in the field of distribution of electronic goods. 
They use Odoo to manage the process their business, especially in the purchasing (Purchase), sales (Sales), and inventory (Inventory) sections. 
To increase efficiency, the company wants to add a Booking Order feature to manage future orders.

- Asg2 module contain Booking Order Menu.
    Customers can make orders in advance (booking orders) for items that are not yet available in inventory (state:Booking). 
    When the item is available, the order will be changed become a sales order and processed further (state:Sales Order).

- Asg4 module contain Report and Wizard for Inventory Module.
    To especially see the report for Booking Order, please EDIT the record that have been created in Delivery Orders Form to make sure that boolean Booking Order is CHECKED. Because the field haven't done yet to automatic True, but the report domain has been created to display booking order data only.
    The report is available on the Report Booking Order sub menu under the Reporting menu.

- Final Exam module contain security for Sales, Booking Order, Purchase, and Inventory module.
    1. Customer Sales, Purchase, Inventory
        - Only see his record (Still process for Purchase and Inventory)
        - Only see specific menu
        - Can't see Unit Price and Salesperson field

    2. Admin Sales, Purchase, Inventory
        - Can see all record
        - Only see specific menu
        - Can't see Unit Price field

    3. Manager Sales, Purchase, Inventory 
        - Can manage all record