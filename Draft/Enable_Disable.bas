Attribute VB_Name = "Enable_Disable"
Sub Enable_DisableUpdate(Configuration As Integer)
    Dim NumRows As Integer
    Dim CurrentSheet As String
    Dim NewColumn As String

    CurrentSheet = ActiveSheet.Name
    Sheets("Data").Select
    Range("A5").Select
    
    Selection.End(xlDown).Select
    NumRows = Selection.row()


    Cells(5, 35 + Configuration).Select

    NewColumn = Selection.Address(ColumnAbsolute)
    
    Range("AE5").Value = "=" & NewColumn
    Range("AE5:AE" & NumRows).Select
    Selection.FillDown

    Sheets(CurrentSheet).Select
End Sub
