#include <iostream>
#include <fstream>
#include <stack>
#include <vector>
#include <string>

std::string make_string(const std::stack<char>& stack) {
	std::string			result = "";
	std::stack<char>	temp = stack;

	while (!temp.empty()) {
		result = temp.top() + result;
		temp.pop();
	}
	return result;
}

long int search_biggest_combination(const std::string&line, long int keep) {
	std::stack<char>	stack;
	long int 				to_remove;

	to_remove = line.size() - keep;
	for (char c: line) {
		while (to_remove > 0 && !stack.empty() && stack.top() < c) {
			stack.pop();
			to_remove--;
		}
		stack.push(c);
	}
	std::string result = make_string(stack);
	try {
		return std::stol(result.substr(0, keep));
	} catch (const std::invalid_argument&) {
		return 0;
	} catch (const std::out_of_range&) {
		std::cout << "Out of range: " << result << std::endl;
		return std::stoi(result);
	}
}

std::vector<std::string> read_lines(const std::string& filename) {
    std::ifstream 				file(filename);
    std::vector<std::string>	lines;
    std::string					line;

	if (!file) {
        std::cerr << "Fout: kon bestand niet openen: " << filename << std::endl;
        exit(1);
    }

    while (std::getline(file, line))
        lines.push_back(line);
    return lines;
}

int main(void) {
	std::vector<std::string>	lines = read_lines("input/03.txt");
	long int 					total1 = 0;
	long int					total2 = 0;

	for (const std::string& line : lines) {
		total1 += search_biggest_combination(line, 2);
		total2 += search_biggest_combination(line, 12);
	}
	std::cout << "Results: " << total1 << "," << total2 << std::endl;
	return 0;
}