import java.util.*;
import java.util.stream.*;
import java.io.*;

public class part1 {
	static int maxID = Integer.MIN_VALUE;
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("test.in"));

		List<String> lines = in.lines().collect(Collectors.toList());

		for (String line : lines) {
			int r = 0;
			for (int i = 0; i < 7; i++) {
				int pow = 1 << (6-i);
				if (line.charAt(i) == 'B')
					r += pow;
			}
			int c = 0;
			for (int i = 0; i < 3; i++) {
				int pow = 1 << (2-i);
				if (line.charAt(i+7) == 'R')
					c += pow;
			}
			int id = r*8 + c;
			System.out.println(r+","+c);

			updateMax(id);
		}
		System.out.println(maxID);
	}

	static void updateMax(int id) {
		maxID = Math.max(id, maxID);
	}
}