print("hello world")
print("good morning")
print("good afternoon")
print("good night")
a=10
b=5
print(a+b)
print("hello")
/**
     * 
     * @throws Exception
     * This method displays the books issued to the User along with Date of Issue
     * It also displays the books returned by the user along with the Date of Return
     * This method throws FileNotFoundException if the file is not available
     * FileName : BookTransactionData.csv
     */

    public  void booksHistory() throws Exception{
         
        File file = new File("BookTransactionData.csv");
        Scanner scan = new Scanner(file);
        scan.useDelimiter("\n");
        while(scan.hasNext()){
            String temp = scan.next().trim();
            String[] data = temp.split(",");
            if(data[0].equals(this.email) && data.length >=1){
                int issued = 0;
                int returned = 0;
                if(data.length>=2){
                    String[] booksIssued = data[1].split(";");
                    System.out.println("Books issued are");
                    System.out.println("Book name  Issued Date");
                    for(String a :booksIssued){
                        System.out.println(a);
                        issued =1;
                    }
                }
                if(issued ==0){
                    System.out.println("No books Issued");
                }
                if(data.length ==3){
                    String[] booksReturned = data[2].split(";");
                    System.out.println("Books returned are");
                    System.out.println("Book name  Returned Date");
                    for(String a :booksReturned){
                        System.out.println(a);
                        returned =1;
                    }
                }
                if(returned ==0){
                    System.out.println("No books returned");
                }
            }
           
        }
        scan.close();
    }
