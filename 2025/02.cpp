#include <iostream>
#include <fstream>
#include <sstream>
#include <stack>
#include <vector>
#include <string>
#include "cpp_helpers.cpp"

bool valid_id(long int id) {
	std::string id_str = std::to_string(id);
	if (id_str.length() % 2 != 0) {
		return false;
	}
	int half_length = id_str.length() / 2;
	std::string first_half = id_str.substr(0, half_length);
	std::string second_half = id_str.substr(half_length, half_length);
	return first_half == second_half;
}

long int part1(std::vector<std::string> &all_ids) {
	long int 	total = 0;
	int			i = 0;	 

	for (const std::string& ids : all_ids) {
		std::vector<std::string> two_ids = split(ids, '-');
		long int id1 = std::stol(two_ids[0]);
		long int id2 = std::stol(two_ids[1]);
		while (id1 <= id2) {
			if (valid_id(id1)) {
				total += i;
			}
			id1++;
		}
		i++;
	}
	return total;
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
	std::vector<std::string>	ids = read_lines("input/02.txt");
	long int 					total1 = 0;
	long int					total2 = 0;

	std::vector<std::string> all_parts = split(ids[0], ',');
	total1 = part1(all_parts);

	std::cout << "Results: " << total1 << "," << total2 << std::endl;
	return 0;
}