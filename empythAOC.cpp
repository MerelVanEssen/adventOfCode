#include <iostream>
#include <fstream>
#include <stack>
#include <vector>
#include <string>



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

	}
	std::cout << "Results: " << total1 << "," << total2 << std::endl;
	return 0;
}