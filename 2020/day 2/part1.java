import java.util.*;
import java.io.*;

public class part1 {
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

			int cCount = 0;
			for (int i = 0; i < password.length(); i++) {
				if (password.charAt(i) == c)
					cCount++;
				if (cCount > upper)
					break;
			}

			if (cCount >= lower && cCount <= upper)
				incrementCount();
		});

		System.out.println(count);

	}

	static void incrementCount() {
		count++;
	}
}