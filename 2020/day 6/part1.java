import java.util.*;
import java.io.*;
import java.util.stream.*;

public class part1 {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("input.in"));
		
		List<String> lines = in.lines().collect(Collectors.toList());

		int sum = 0;
		boolean[] yes = new boolean[26];
		for (String line : lines) {
			if (line.equals("") || line.equals("\n")) {
				for (boolean b : yes) 
					if (b) sum++;
				Arrays.fill(yes, false);
			}
			line.chars().forEach(c -> yes[c-'a'] = true);
		}
		System.out.println(sum);

	}
}