import java.util.*;
import java.io.*;

public class part1 {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("input.in"));

		List<String> list = new ArrayList<>();

		in.lines().forEach(line -> {
			list.add(line);
		});

		int count = 0;
		int x = 0, y = 0;
		while (y < list.size()) {
			String line = list.get(y);
			if (line.charAt(x % line.length()) == '#')
				count++;

			x+=3;
			y++;
		}

		System.out.println(count);

	}
}