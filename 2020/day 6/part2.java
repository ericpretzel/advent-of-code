import java.util.*;
import java.io.*;
import java.util.stream.*;

public class part2 {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("input.in"));
		
		List<String> lines = in.lines().collect(Collectors.toList());

		int sum = 0;
		int[] yes = new int[26];
		int groupCount = 0;
		for (String line : lines) {
			if (line.equals("") || line.equals("\n")) {
				for (int i : yes) 
					if (i == groupCount) sum++;
				Arrays.fill(yes, 0);
				groupCount = 0;
			} else {
				groupCount++;
				line.chars().forEach(c -> yes[c-'a'] += 1);
			}
			
		}
		System.out.println(sum);

	}
}