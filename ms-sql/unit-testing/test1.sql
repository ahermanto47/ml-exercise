USE DEV;
GO

-- create temp table to store test and its result
CREATE TABLE #TEST_RESULTS
(
    TEST_NUMBER int,
    TEST_DESCRIPTION varchar(100),
    TEST_RESULT varchar(20)
);

-- setup variables for test
DECLARE @RC AS INT, 
   @CustomerName AS NVARCHAR (40), 
   @ActualCustomerName AS NVARCHAR (40), 
   @TestNumber AS INT, 
   @TestDescription AS NVARCHAR(100), 
   @TestResult AS NVARCHAR(20);


-- start recording the test
SELECT 
       @TestNumber = 1,
       @TestDescription = 'sp Sales.uspNewCustomer should add record to [Sales].[Customer] table',
       @TestResult = null;

INSERT INTO #TEST_RESULTS (TEST_NUMBER, TEST_DESCRIPTION, TEST_RESULT) 
   VALUES (@TestNumber, @TestDescription, @TestResult);

-- initialized the variables
SELECT @RC = 0,  
       @CustomerName = 'Fictitious Customer',
       @ActualCustomerName = null;

-- execute the code in test
EXECUTE @RC = [Sales].[uspNewCustomer] @CustomerName;

-- verify the outcome of the test
SELECT @ActualCustomerName = [CustomerName] FROM [Sales].[Customer] WHERE CustomerID = @RC;

IF (@RC > 0) AND (@ActualCustomerName = @CustomerName)
BEGIN
   SELECT @TestResult = 'Successful';
END
ELSE
BEGIN
   SELECT @TestResult = 'Failed';
END

UPDATE #TEST_RESULTS SET TEST_RESULT = @TestResult WHERE TEST_NUMBER = @TestNumber;

-- report the result
SELECT * FROM #TEST_RESULTS;

GO