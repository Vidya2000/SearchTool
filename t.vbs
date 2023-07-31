Option Explicit

Sub Main()
    Dim objExcel As Object, objWorkbook As Object
    Dim strWorkbookPath As String, strFunctionName As String, strSearchKeyword As String
    Dim strCategory As String, strResult As String
    Dim i As Integer, objArgs As Object

    ' Set the workbook path
    strWorkbookPath = "C:\ST_EXCEL\SearchTool_Vidya\SearchTool.xlsm"  ' Replace with the actual file path and name

    ' Set the function name and category
    strFunctionName = "Search"
    strCategory = "Documents"

    ' Check if Excel is already running or create a new instance
    On Error Resume Next
    Set objExcel = GetObject(, "Excel.Application")
    If Err.Number <> 0 Then
        ' Excel is not running or no instance found, create a new instance
        Set objExcel = CreateObject("Excel.Application")
        objExcel.Visible = True
    End If
    On Error GoTo 0

    ' Open the workbook without updating links
    On Error Resume Next
    Set objWorkbook = objExcel.Workbooks.Open(strWorkbookPath)
    If Err.Number <> 0 Then
        ' Workbook couldn't be opened, so open it again
        Set objWorkbook = objExcel.Workbooks.Open(strWorkbookPath, 0)
    End If
    On Error GoTo 0

    ' Check if objExcel and objWorkbook are valid objects
    If Not (IsObject(objExcel) And IsObject(objWorkbook)) Then
        MsgBox "Failed to initialize Excel objects. Exiting..."
        Set objWorkbook = Nothing
        Set objExcel = Nothing
        Exit Sub
    End If

    ' Get the command line arguments
    Set objArgs = WScript.Arguments
    If objArgs.Count > 0 Then
        ' Use all arguments as the search keyword (space-separated)
        For i = 0 To objArgs.Count - 1
            strSearchKeyword = strSearchKeyword & " " & objArgs(i)
        Next
        strSearchKeyword = Trim(strSearchKeyword)
    Else
        ' No arguments provided, prompt for the search keyword
        strSearchKeyword = InputBox("Enter the search keyword:", "Search Tool")
        If strSearchKeyword = "" Then
            MsgBox "No search keyword provided. Exiting..."
            objWorkbook.Close False
            objExcel.Quit
            Set objWorkbook = Nothing
            Set objExcel = Nothing
            Exit Sub
        End If
    End If

    ' Set the value of cell A5 with the search keyword
    objWorkbook.Sheets(1).Range("A5").Value = strSearchKeyword

    ' Run the Search macro
    objExcel.Run strFunctionName, strSearchKeyword, strCategory

    ' Clean up
    objWorkbook.Close False
    objExcel.Quit
    Set objWorkbook = Nothing
    Set objExcel = Nothing
End Sub

Main
