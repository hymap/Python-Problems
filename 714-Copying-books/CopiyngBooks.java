package copy.books;

import copy.books.InputAndGetHighestSum.InputReader;
 
public class CopyingBooks {
 
    public static void main(String[] args) throws Exception {
    	
    	// Initialize variable to store output while processing each case.
        // At last we will fire this at the end of loop
        StringBuilder out = new StringBuilder();
        InputReader in = new InputReader(System.in);
        int casesCnt = in.nextInt();
        while (casesCnt-- > 0) {
        	// Read input
            int booksCnt = in.nextInt();
            int scribers = in.nextInt();
            int[] pages = new int[booksCnt];
            for (int i = 0; i < pages.length; i++)
            	pages[i] = in.nextInt();
            
            InputAndGetHighestSum obj = new InputAndGetHighestSum();
            // Binary search is being used to find optimal assignment which is the 
        	// maximum sum of a single scriber that is as small as possible. 
            long optimal = obj.getOptimalAssignment(booksCnt, pages, scribers);
            //System.out.println(" avgPages : "+avgPages);
            
            // Assign books based on optimal value we found and store into an array
            int[] start = obj.bookAssignment(optimal, booksCnt, pages, scribers);

            out = obj.prepareOutput(start, pages, out, booksCnt);
            //System.out.println(" out "+out );
            out.append("\n");
        }
        System.out.println(out);
    }
}
