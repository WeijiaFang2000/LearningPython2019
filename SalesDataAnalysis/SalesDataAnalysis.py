# Author: Weijia Fang
# Title: Sales Data Analysis
# Completion Date: Apr 2019

def get_ID(filename):
    #Open the file
    SalesIDFile = open(filename, mode='r')
    #List to store sales ID
    id_list = []
    #Two dimensional list to initialize sales data
    sales_data = []
    #Read each line of sales id file and put it to id_list.
    for line in SalesIDFile.readlines():
        id_list.append(line.strip())
        sales_data.append([0,0,0,0])
    #Close file
    SalesIDFile.close()
    #Return the value of id_list and sales_data
    return id_list, sales_data

def process_sales_data(filename, id_list, sales_data):
    #Open the file of sales data
    SalesDataFile = open(filename, mode='r')
    #Read each line and splid the data and put them to sales_data
    for line in SalesDataFile.readlines():
        line = line.strip()
        #Split the data to a list, the first element is Sales ID, the second is month, and the third is sales amount
        linedata = line.split()
        RowOfSalesID = id_list.index(linedata[0])
        #Quarter 1's sales added to sales_data
        if(int(linedata[1]) in [1,2,3]):
            sales_data[RowOfSalesID][0] += float(linedata[2])
        #Quarter 2's sales added to sales_data
        if(int(linedata[1]) in [4,5,6]):
            sales_data[RowOfSalesID][1] += float(linedata[2])
        #Quarter 3's sales added to sales_data
        if(int(linedata[1]) in [7,8,9]):
            sales_data[RowOfSalesID][2] += float(linedata[2])
        #Quarter 4's sales added to sales_data
        if(int(linedata[1]) in [10,11,12]):
            sales_data[RowOfSalesID][3] += float(linedata[2])
    #Close file
    SalesDataFile.close()

def print_report(id_list, sales_data):
    print(" ------------Annual Sales Report------------\n")
    print("%-12s%12s%12s%12s%12s%12s"%("ID","QT1  ","QT2  ","QT3  ","QT4  ","Total  "))

    MaxSalesRow = 0
    MaxQuarterSaleofOneSalesman = 0

    QuarterSales = [0, 0, 0, 0]

    for row in range(len(sales_data)):
        for column in range(len(sales_data[row])):
            #Find the max sales of single quarter, it's row is used to find the sales id.
            if (MaxQuarterSaleofOneSalesman < float(sales_data[row][column])):
                MaxQuarterSaleofOneSalesman = float(sales_data[row][column])
                MaxSalesRow = row
            #Add quarter sales together and store on variable QuarterSales. This is the first quarter
            if (column == 0):
                QuarterSales[0] += sales_data[row][column]
            #Second quarter.
            if (column == 1):
                QuarterSales[1] += sales_data[row][column]
            #Third quarter.
            if (column == 2):
                QuarterSales[2] += sales_data[row][column]
            #Forth quarter.
            if (column == 3):
                QuarterSales[3] += sales_data[row][column]

        #Print each sales' data
        print("%-12s%12.2f%12.2f%12.2f%12.2f%12.2f"%(id_list[row],sales_data[row][0],sales_data[row][1],sales_data[row][2],sales_data[row][3],sum(sales_data[row])))

    #Print total sales of quarter
    print("%-12s%12.2f%12.2f%12.2f%12.2f%12.2f\n"%("Total", QuarterSales[0],QuarterSales[1],QuarterSales[2],QuarterSales[3],sum(QuarterSales)))

    # Find the sales id with max quarterly sales
    MaxSalesID = id_list[MaxSalesRow]

    #Find max sales of all quarters.
    MaxQuarterSale = max(QuarterSales)
    #Find the quarter which has max sales.
    MaxQuarter = QuarterSales.index(MaxQuarterSale) + 1
    
    #Print the result
    print("Max sales by Salesperson: ID = %s, Amount = $%.2f"%(MaxSalesID,  MaxQuarterSaleofOneSalesman))
    print("Max sales by Quarter: Quarter = %s, Amount = $%.2f"%(MaxQuarter, MaxQuarterSale))    
    
def main():
    #Ask user to input sales id file name
    salesIdFilename = input("Enter the name of the sales ids file: ")
    #Ask user to input sales data file name.
    salesDataFilename = input("Enter the name of the sales data file: ")
    print("\n")

    #Get the two list contains id list and sales initial data for quarters.
    (id_list, sales_data) = get_ID(salesIdFilename)
    #Read sales data of monthly and calculate it. Put the data to list sale_data.
    process_sales_data(salesDataFilename, id_list, sales_data)
    #Print all output
    print_report(id_list, sales_data)

if __name__ == "__main__":
    main()
