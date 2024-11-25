declare @Sql nvarchar(max), @columnName VARCHAR(30) = 's%';

select @Sql = 


(select '
SELECT ' + QUOTENAME(name,'''') + ' as [DB Name], table_schema as [Schema Name], table_name as [Table Name], [column_name] from ' + 
QUOTENAME(Name) + '.INFORMATION_SCHEMA.columns
WHERE column_name like @columnName
order by [DB Name],[Schema Name], [Table Name], [column_name];' from sys.databases
order by name FOR XML PATH(''), TYPE).value('.', 'varchar(max)')

PRINT @SQL;

EXECUTE sp_executeSQL @SQL, N'@columnName varchar(30)', @columnName = @columnName;