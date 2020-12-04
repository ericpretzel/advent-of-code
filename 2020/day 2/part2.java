import java.util.*;
import java.io.*;

public class part2 {
	static int count = 0;
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("input.in"));

		in.lines().forEach(line -> {

			Scanner sc = new Scanner(line);
			String[] arr = sc.next().split("-");
			int lower = Integer.parseInt(arr[0]);
			int upper = Integer.parseInt(arr[1]);

			char c = sc.next().charAt(0);

			String password = sc.next();

			if (password.charAt(lower-1) == c ^ password.charAt(upper-1) == c)
				incrementCount();
		});

		System.out.println(count);

	}

	static void incrementCount() {
		count++;
	}
}