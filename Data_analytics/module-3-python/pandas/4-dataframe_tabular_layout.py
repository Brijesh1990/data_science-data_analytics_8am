# A `DataFrame` is a two-dimensional labelled table with rows and columns. It is similar to a spreadsheet or a database table.
# Data frame provides structured type of data

import pandas as pd 
import matplotlib.pyplot as mlt
import openpyxl
data = {
	"Name": ["Asha", "Ravi", "John"],
	"Age": [20, 21, 19],
	"Marks": [85, 90, 78],
}

df=pd.DataFrame(data)
# find max data or marks
max_values=df["Marks"].max()
print("Max marks values",max_values)

# find count of member or  data
total_members=df["Name"].count()
print("Totals Member count ",total_members)

# find the average marks 
avg_marks=df["Marks"].mean()
print("Avg marks values",avg_marks)


# find total sum of  marks
sum_marks=df["Marks"].sum()
print("Sum of marks ",sum_marks)
# who is getting max marks or highest marks find name
name_max_marks=df.loc[df["Marks"].idxmax(), "Name"]
print("Getting max marks name is :",name_max_marks)
print('--------------------------------------------------')
print(df)

# generated excels

# Export the student data and marks summary in one Excel workbook.
summary = pd.DataFrame(
    {
        "Metric": [
            "Highest marks name",
            "Mean marks",
            "Max marks",
            "Sum of marks",
        ],
        "Value": [
            name_max_marks,
            avg_marks,
            max_values,
            sum_marks,
        ],
    }
)

with pd.ExcelWriter("employee_data.xlsx", engine="openpyxl") as writer:
    df[["Name", "Age", "Marks"]].to_excel(
        writer, sheet_name="Data", index=False
    )
    summary.to_excel(writer, sheet_name="Summary", index=False)
    worksheet = writer.sheets["Summary"]
    header_fill = openpyxl.styles.PatternFill(
        fill_type="solid", fgColor="1F4E78"
    )
    header_font = openpyxl.styles.Font(color="FFFFFF", bold=True)
    for cell in worksheet[1]:
        cell.fill = header_fill
        cell.font = header_font

    metric_colors = ["FFD966", "A9D18E", "9DC3E6", "F4B183"]
    for row_number, color in enumerate(metric_colors, start=2):
        for cell in worksheet[row_number]:
            cell.fill = openpyxl.styles.PatternFill(
                fill_type="solid", fgColor=color
            )

    worksheet.column_dimensions["A"].width = 24
    worksheet.column_dimensions["B"].width = 18

print("Excel workbook generated successfully")

# for display data in chart matplotlib
# find title of chart
mlt.title("highest getting marks in charts with name")
mlt.pie(
    df["Marks"],
    labels=df["Name"], 
    autopct="%1.1f%%",
    colors=["yellow","green","red"]
)
# display chart
mlt.show()
