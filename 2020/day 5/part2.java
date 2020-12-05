import java.util.*;
import java.util.stream.*;
import java.io.*;

public class part2 {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("input.in"));

		List<String> lines = in.lines().collect(Collectors.toList());

		Set<Integer> set = new TreeSet<>();
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
			set.add(r*8+c);
		}
		boolean firstFound = false;
		for (int r = 0; r < 128; r++) {
			for (int c = 0; c < 7; c++) {
				int id = r*8+c;
				boolean found = set.contains(id);
				if (!firstFound && found) {
					firstFound = true;
				} else if (firstFound && !found) {
					System.out.println(id);
					return;
				}
			}
		}
	}
}