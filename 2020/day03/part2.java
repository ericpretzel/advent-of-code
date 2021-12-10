import java.util.*;
import java.io.*;

public class part2 {
	static List<String> list = new ArrayList<>();
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("input.in"));

		in.lines().forEach(line -> {
			list.add(line);
		});

		long product = trees(1,1) * trees(1,3) * trees(1,5) * trees(1,7) * trees(2,1);
		System.out.println(product);

	}

	static long trees(int rise, int run) {
		long count = 0;
		int x = 0, y = 0;
		while (y < list.size()) {
			String line = list.get(y);
			if (line.charAt(x % line.length()) == '#')
				count++;

			x+=run;
			y+=rise;
		}
		return count;
	}
}