import java.util.*;
import java.io.*;

public class part1 {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("input.in"));
		
		List<Integer> list = new ArrayList<>();

		String line;
		while ( (line = in.readLine()) != null) {
			int i = Integer.parseInt(line);
			list.add(i);
		}

		Collections.sort(list);

		for (int i = 0; i < list.size(); i++) {
			int target = 2020 - list.get(i);
			int k = binSearch(list, target, 0, list.size()-1);
			if (k >= 0) {
				System.out.println(list.get(i) * list.get(k));
				return;
			}
		}
	}

	static int binSearch(List<Integer> list, int target, int l, int r) {
		if (l > r) return -1;

		int m = (l + r)/2;

		int i = list.get(m);


		if (i == target)
			return m;

		else if (i > target)
			return binSearch(list, target, l, m-1);

		return binSearch(list, target, m+1, r);
	}

}