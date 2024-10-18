CREATE PROCEDURE lowerQuantity
   @Quantity INT
AS   
   SET NOCOUNT ON;
   SELECT Id, Name, Quantity FROM TestDB.Inventory WHERE Quantity < @Quantity;
GO