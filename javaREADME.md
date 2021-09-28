public final String itteratorRebalancedData()
{
	int lastRow = 0;
	 Worksheets("RebalancedData").Activate;
	lastRow = Worksheets("RebalancedData").UsedRange.rows.Count;
//VB TO JAVA CONVERTER NOTE: The ending condition of VB 'For' loops is tested only on entry to the loop. VB to Java Converter has created a temporary variable in order to use the initial value of lastRow - 2 Step1 for every iteration:
	int tempVar = lastRow - 2 Step1;
	for (var i = 0; i <= tempVar; i++)
	{
		matchDate = Worksheets("RebalancedData").Range("A" + (i + 2)).Value;
		FilePath = Worksheets("RebalancedData").Range("A" + (i + 2)).Value;
		Debug.Print FilePath;
		if (FilePath.equals(""))
		{
			feedBlankInMainWithComments("RebalancedData", i + 10);
		}
		else
		{
			ParseExcelRebalancedDataSheet(FilePath, i + 10);
		}
		ElseIf)
		{
	}
	Debug.Print ".....End...";
//VB TO JAVA CONVERTER NOTE: Inserted the following 'return' since all code paths must return a value in Java:
	return null;
}
