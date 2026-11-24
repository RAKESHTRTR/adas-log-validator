#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

int main(int argc, char* argv[]) {
    if (argc < 2)
    {
        std::cerr << "Error: missing file argument (exit code 2)\n";
        return 2;
    }
        
    std::ifstream in(argv[1]);
    std::string line;
    std::getline(in, line); // skip header
    long long prev_ts = -1, max_dt = 0, count = 0;
    while (std::getline(in, line)) {
        std::stringstream ss(line);
        std::string ts_str;
        std::getline(ss, ts_str, ',');
        long long ts = std::stoll(ts_str);
        if (prev_ts != -1 && (ts - prev_ts) > max_dt) max_dt = ts - prev_ts;
        prev_ts = ts;
        count++;
    }
    std::cout << "Rows: " << count << " | Max dt_ms: " << max_dt << "\n";
    return 0;
}