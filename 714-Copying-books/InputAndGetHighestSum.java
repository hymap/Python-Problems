package copy.books;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class InputAndGetHighestSum {
 
	static class InputReader {
        private BufferedReader reader;
        private StringTokenizer tokenizer;
 
		// Declaration to read input in streams 
        public InputReader(InputStream stream) {
            reader = new BufferedReader(new InputStreamReader(stream));
            tokenizer = null;
        }
 
        // Checks whether next input exists and reads as given by user
        public String next() {
            while (tokenizer == null || !tokenizer.hasMoreTokens()) {
                try {
                    tokenizer = new StringTokenizer(reader.readLine());
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
            return tokenizer.nextToken();
        }
 
        // Reads next integer from a line of input given by user
        public int nextInt() {
            return Integer.parseInt(next());
        }
    }

	// Binary search is being used to find optimal assignment which is the 
	// maximum sum of a single scriber that is as small as possible. 
	public long getOptimalAssignment(int booksCnt, int[] pages, int scribers) {
		//long high = 1L << 33;
		long high = 0;
        long low = 1;
        
        for (int i = 0; i < pages.length; i++)   
		{  
        	high += pages[i];
		}
        while (high > low) {
            long mid = (high + low) / 2;
            long accu = 0;
            int j = 0;
            for (int i = 0; i < booksCnt && j < scribers; i++) {
                while (pages[i] + accu > mid && j < scribers) {
                    accu = 0;
                    j++;
                }
                accu += pages[i];
            }
            if (j >= scribers)
                low = mid + 1;
            else
                high = mid;
        }
        return high;
	}
 
	public int[] bookAssignment(long avgPages, int booksCnt, int[] pages, int scribers) {
		int[] start = new int[scribers];
		long accu = 0;
        int current = scribers - 1;

		for (int i = booksCnt - 1; i >= 0; i--) {
             if (accu + pages[i] > avgPages) {
                 start[current] = i + 1;
                 accu = 0;
                 current--;
             }
             accu += pages[i];
         }

         start[current] = 0;
         int top = 0;
         for (int i = 0; i < start.length; i++) {
             if (start[i] == -1) {
                 start[i] = top++;
             }
         }

         for (int i = 0; i < start.length - 1; i++) { 
             if (start[i] >= start[i + 1]) {
                 start[i + 1] += (start[i] - start[i + 1] + 1);  
             }
         }
		return start;
	}
	
	public StringBuilder prepareOutput(int[] start, int[] pages,StringBuilder out, int booksCnt)
	{
		for (int i = 0; i < start.length; i++) {
            int next = booksCnt;
            if (i + 1 < start.length)
                next = start[i + 1];
            for (int j = start[i]; j < next; j++) {
                out.append(pages[j] + " ");
            }
            if (i == start.length-1) {
            	
            }else {
            	out.append("/ ");
            }
            
        }
	    
	    return out;
	}
}

