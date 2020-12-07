import java.util.*;
import java.io.*;
import java.util.stream.*;

public class part2 {
	static Map<String, Map<String, Integer>> bags = new HashMap<>();
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new FileReader("input.in"));
		
		List<String> lines = in.lines().collect(Collectors.toList());
		for (String line : lines) {
			Scanner sc = new Scanner(line);

			String parentName = sc.next() + " " + sc.next();
			sc.next(); //bags
			sc.next(); //contain

			Map<String, Integer> children = new HashMap<>();
			if (line.contains("no other")) {
				bags.put(parentName, children);
				continue;
			}
			
			while (sc.hasNext()) {
				int amount = Integer.parseInt(sc.next());
				String childName = sc.next() + " " + sc.next();
				sc.next(); //bags(,)
				children.put(childName, amount);
			}

			bags.put(parentName, children);
		}
		System.out.println(bagsContained("shiny gold"));
	}

	static int bagsContained(String name) {
		Map<String, Integer> children = bags.get(name);
		if (children.size() == 0)
			return 0;

		int total = 0;
		for (String child : children.keySet()) {
			total += children.get(child);
			total += bagsContained(child) * children.get(child);
		} 
		return total;
	}

}