-- =======================================================
-- Create Stored Procedure Template for Azure SQL Database
-- =======================================================
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:      Andi Hermnto
-- Create Date: 10/17/2024
-- Description: Return items with lower quantity.
-- =============================================
CREATE PROCEDURE TestDB.lowerQuantity
(
    -- Add the parameters for the stored procedure here
    @Quantity INT = 0
)
AS
BEGIN
    -- SET NOCOUNT ON added to prevent extra result sets from
    -- interfering with SELECT statements.
    SET NOCOUNT ON

    -- Insert statements for procedure here
    SELECT Id, Name, Quantity
       FROM TestDB.Inventory
       WHERE Quantity < @Quantity;
END
GO